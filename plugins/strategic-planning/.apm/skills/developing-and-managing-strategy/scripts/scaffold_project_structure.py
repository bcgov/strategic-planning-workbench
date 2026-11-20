#!/usr/bin/env python3
"""Scaffold a strategic planning or architecture repository from a structure profile."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
PROFILES_DIR = SKILL_DIR / "assets" / "structure-profiles"
TEMPLATES_DIR = SKILL_DIR / "assets" / "templates"
REGISTRY_SCRIPT = (
    SKILL_DIR.parent
    / "managing-architecture-registry"
    / "scripts"
    / "managing_architecture_registry.py"
)


def load_profile(profile_id: str) -> dict:
    """Load a structure profile JSON definition by ID."""
    profile_path = PROFILES_DIR / f"{profile_id}.json"
    if not profile_path.exists():
        available = sorted(p.stem for p in PROFILES_DIR.glob("*.json"))
        raise SystemExit(
            f"Unknown profile '{profile_id}'. Available profiles: {', '.join(available)}"
        )
    return json.loads(profile_path.read_text(encoding="utf-8"))


def scaffold(
    target: Path,
    profile: dict,
    project_name: str,
    with_execution: bool = False,
    dry_run: bool = False,
    force: bool = False,
    init_registry: bool = False,
) -> dict[str, list[str]]:
    """Create directories and starter stubs defined by the profile."""
    created_dirs: list[str] = []
    created_files: list[str] = []
    skipped_files: list[str] = []

    dirs = list(profile.get("directories", []))
    if with_execution:
        dirs.extend(profile.get("execution_directories", []))

    for rel_dir in dirs:
        dest = target / rel_dir
        if not dest.exists():
            created_dirs.append(rel_dir)
            if not dry_run:
                dest.mkdir(parents=True, exist_ok=True)

    stubs = dict(profile.get("starter_stubs", {}))
    if with_execution:
        stubs.update(profile.get("execution_stubs", {}))

    for rel_file, template in stubs.items():
        dest = target / rel_file
        if dest.exists() and not force:
            skipped_files.append(rel_file)
            continue
        created_files.append(rel_file)
        if not dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            if template.startswith("@template:"):
                tpl_name = template.split(":", 1)[1].strip()
                content = (TEMPLATES_DIR / tpl_name).read_text(encoding="utf-8")
            else:
                content = template.format(project_name=project_name)
            dest.write_text(content, encoding="utf-8")

    if init_registry and "architecture" in profile.get("directories", []):
        registry_path = target / "architecture" / "architecture-registry.json"
        if registry_path.exists() and not force:
            skipped_files.append("architecture/architecture-registry.json")
        elif REGISTRY_SCRIPT.exists():
            created_files.append("architecture/architecture-registry.json")
            if not dry_run:
                subprocess.run(
                    [
                        sys.executable,
                        str(REGISTRY_SCRIPT),
                        "init",
                        str(registry_path),
                        "--project",
                        project_name,
                    ],
                    check=True,
                )

    return {
        "created_dirs": created_dirs,
        "created_files": created_files,
        "skipped_files": skipped_files,
    }


def main() -> int:
    """CLI entry point for scaffolding a project structure."""
    parser = argparse.ArgumentParser(
        description="Scaffold a strategic planning or architecture repository."
    )
    parser.add_argument(
        "--profile",
        required=True,
        help="Profile ID (strategy-only, solution-architecture, strategy-and-architecture, enterprise-architecture)",
    )
    parser.add_argument(
        "--target",
        required=True,
        type=Path,
        help="Target repository directory",
    )
    parser.add_argument(
        "--project-name",
        default="Untitled Initiative",
        help="Human-readable project or team name for starter files",
    )
    parser.add_argument(
        "--with-execution",
        action="store_true",
        help="Also create execution folders (spikes/, evals/, infra/, .github/workflows/)",
    )
    parser.add_argument(
        "--init-registry",
        action="store_true",
        help="Initialize architecture/architecture-registry.json if architecture/ is part of the profile",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without creating files or directories",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing starter files",
    )
    args = parser.parse_args()

    profile = load_profile(args.profile)
    result = scaffold(
        target=args.target.resolve(),
        profile=profile,
        project_name=args.project_name,
        with_execution=args.with_execution,
        dry_run=args.dry_run,
        force=args.force,
        init_registry=args.init_registry,
    )
    mode = "DRY RUN" if args.dry_run else "APPLIED"
    print(f"[{mode}] Profile: {profile['id']} -> {args.target.resolve()}")
    print(f"  Directories to create ({len(result['created_dirs'])}): {result['created_dirs']}")
    print(f"  Files to write ({len(result['created_files'])}): {result['created_files']}")
    if result["skipped_files"]:
        print(f"  Existing files preserved ({len(result['skipped_files'])}): {result['skipped_files']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
