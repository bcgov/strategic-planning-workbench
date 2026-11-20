#!/usr/bin/env python3
"""Validate an existing strategic planning or architecture repository against a profile."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
PROFILES_DIR = SKILL_DIR / "assets" / "structure-profiles"
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
IGNORED_PREFIXES = ("http://", "https://", "mailto:", "file://", "#")


def load_profiles() -> dict[str, dict]:
    """Load all structure profile definitions."""
    return {
        p.stem: json.loads(p.read_text(encoding="utf-8"))
        for p in sorted(PROFILES_DIR.glob("*.json"))
    }


def detect_profile(target: Path, profiles: dict[str, dict]) -> str:
    """Heuristically pick the closest matching profile for an existing repository."""
    has_strategy = (target / "strategy").is_dir()
    has_arch = (target / "architecture").is_dir()
    has_ea = (target / "landscape").is_dir() and (target / "adm-cycles").is_dir()

    if has_ea:
        return "enterprise-architecture"
    if has_strategy and has_arch:
        return "strategy-and-architecture"
    if has_arch:
        return "solution-architecture"
    if has_strategy:
        return "strategy-only"
    return next(iter(profiles))


def check_markdown_links(target: Path) -> list[str]:
    """Return broken relative Markdown links found in top-level and key folder docs."""
    broken: list[str] = []
    md_files = list(target.glob("*.md"))
    for subdir in ("architecture", "adrs", "contracts", "diagrams", "work-packages", "strategy"):
        sub = target / subdir
        if sub.is_dir():
            md_files.extend(sub.glob("*.md"))

    for md_file in md_files:
        in_fence = False
        for lineno, line in enumerate(
            md_file.read_text(encoding="utf-8", errors="replace").splitlines(), start=1
        ):
            if line.strip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            for match in LINK_RE.finditer(line):
                raw_target = match.group(1).strip().split("#")[0]
                if not raw_target or raw_target.startswith(IGNORED_PREFIXES):
                    continue
                resolved = (md_file.parent / raw_target).resolve()
                if not resolved.exists():
                    rel_src = md_file.relative_to(target)
                    broken.append(f"{rel_src}:{lineno} -> {raw_target}")
    return broken


def validate_repo(
    target: Path, profile_id: str, with_execution: bool = False
) -> dict:
    """Validate directories, required files, legacy aliases, JSON syntax, and links."""
    profiles = load_profiles()
    resolved_id = (
        detect_profile(target, profiles) if profile_id == "auto" else profile_id
    )
    if resolved_id not in profiles:
        raise SystemExit(
            f"Unknown profile '{resolved_id}'. Available: {', '.join(sorted(profiles))}"
        )

    profile = profiles[resolved_id]
    expected_dirs = list(profile.get("directories", []))
    if with_execution:
        expected_dirs.extend(profile.get("execution_directories", []))

    missing_dirs = [d for d in expected_dirs if not (target / d).is_dir()]
    missing_files = [
        f for f in profile.get("required_files", []) if not (target / f).exists()
    ]

    warnings: list[str] = []
    for legacy, preferred in profile.get("legacy_aliases", {}).items():
        if (target / legacy).exists():
            warnings.append(
                f"Legacy path '{legacy}' found; preferred standard path is '{preferred}'."
            )

    invalid_json: list[str] = []
    for json_file in target.glob("**/*.json"):
        if ".git" in json_file.parts or "node_modules" in json_file.parts:
            continue
        try:
            json.loads(json_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            invalid_json.append(f"{json_file.relative_to(target)}: {exc}")

    broken_links = check_markdown_links(target)
    passed = not missing_dirs and not missing_files and not invalid_json and not broken_links

    return {
        "profile": resolved_id,
        "target": str(target),
        "status": "PASS" if passed else "FAIL",
        "missing_directories": missing_dirs,
        "missing_files": missing_files,
        "warnings": warnings,
        "invalid_json": invalid_json,
        "broken_links": broken_links,
    }


def main() -> int:
    """CLI entry point for validating a project structure."""
    parser = argparse.ArgumentParser(
        description="Validate an existing strategic planning or architecture repository."
    )
    parser.add_argument(
        "--profile",
        default="auto",
        help="Profile ID or 'auto' (default: auto)",
    )
    parser.add_argument(
        "--target",
        required=True,
        type=Path,
        help="Target repository directory",
    )
    parser.add_argument(
        "--with-execution",
        action="store_true",
        help="Also require execution folders (spikes/, evals/, infra/, .github/workflows/)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON output",
    )
    args = parser.parse_args()

    report = validate_repo(
        target=args.target.resolve(),
        profile_id=args.profile,
        with_execution=args.with_execution,
    )
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"[{report['status']}] Profile: {report['profile']} ({report['target']})")
        for label, key in (
            ("Missing directories", "missing_directories"),
            ("Missing required files", "missing_files"),
            ("Warnings", "warnings"),
            ("Invalid JSON", "invalid_json"),
            ("Broken relative links", "broken_links"),
        ):
            items = report[key]
            if items:
                print(f"  {label} ({len(items)}):")
                for item in items:
                    print(f"    - {item}")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
