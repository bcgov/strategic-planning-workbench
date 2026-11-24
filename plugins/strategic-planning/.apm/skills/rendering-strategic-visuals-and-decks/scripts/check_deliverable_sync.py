#!/usr/bin/env python3
"""Report drift between an architecture workbench and its generated deliverables.

The renderers turn ``deliverables/data/*.json`` into HTML, SVG and decks, but nothing
extracts content from the workbench Markdown into that JSON. This read-only checker
tells an agent *what to update* so the manual sync step is targeted instead of a full
re-read. It never edits files.

Checks (all deterministic, standard library only):
  adr-range       "ADR-001 to ADR-NNN" ranges in the JSON that stop below the latest ADR
  work-package    WP-NN headings in work-packages/README.md that no JSON mentions
  diagram         diagrams/*.mmd with a missing or older images/*.svg, or no gallery entry
  registry        TECH-NNN upper bound in the JSON vs architecture/architecture-registry.json
  source-newer    JSON whose date is older than the newest change to its source documents
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Dict, List, Optional

SOURCE_GLOBS = [
    "02-architecture.md", "04-open-questions.md", "05-mvp-three-domains.md",
    "implementation-plan.md", "adrs/README.md", "work-packages/README.md",
    "architecture/*.md", "architecture/patterns/*.md", "diagrams/*.mmd",
]


def _git(root: Path, *args: str) -> Optional[str]:
    try:
        out = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, check=True)
        return out.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def last_change(root: Path, path: Path) -> float:
    """Epoch seconds of the last change: commit time, or mtime when uncommitted edits exist."""
    rel = str(path.relative_to(root))
    dirty = _git(root, "status", "--porcelain", "--", rel)
    committed = _git(root, "log", "-1", "--format=%ct", "--", rel)
    if dirty or not committed:
        return path.stat().st_mtime
    return float(committed)


def _finding(category: str, message: str, action: str) -> Dict[str, str]:
    return {"category": category, "message": message, "action": action}


def check_adr_range(root: Path, data_text: Dict[str, str]) -> List[Dict[str, str]]:
    readme = root / "adrs" / "README.md"
    if not readme.exists():
        return []
    ids = [int(n) for n in re.findall(r"^##\s+ADR-(\d+)", readme.read_text(encoding="utf-8"), re.M)]
    if not ids:
        return []
    latest = max(ids)
    findings = []
    for name, text in data_text.items():
        for m in re.finditer(r"ADR-0*1\s*(?:to|-|–)\s*(?:ADR-)?(\d+)", text):
            if int(m.group(1)) < latest:
                findings.append(_finding(
                    "adr-range", f"{name}: '{m.group(0)}' but latest ADR is ADR-{latest:03d}",
                    f"Update the range to ADR-001 to ADR-{latest:03d} and summarise new ADRs"))
    return findings


def check_work_packages(root: Path, data_text: Dict[str, str]) -> List[Dict[str, str]]:
    readme = root / "work-packages" / "README.md"
    if not readme.exists():
        return []
    wps = re.findall(r"^##\s+(WP-\d+[A-Z]?)\b", readme.read_text(encoding="utf-8"), re.M)
    blob = "\n".join(data_text.values())
    return [
        _finding("work-package", f"{wp} is defined in work-packages/README.md but absent from deliverables JSON",
                 f"Add {wp} to architecture-on-a-page.json work_packages and the delivery plan")
        for wp in wps if not re.search(rf"\b{re.escape(wp)}\b", blob)
    ]


def check_diagrams(root: Path, deliverables: Path, data_text: Dict[str, str]) -> List[Dict[str, str]]:
    findings = []
    gallery = data_text.get("architecture-diagrams.json", "")
    for mmd in sorted((root / "diagrams").glob("*.mmd")):
        svg = deliverables / "images" / f"{mmd.stem}.svg"
        if not svg.exists():
            findings.append(_finding("diagram", f"{mmd.name} has no images/{svg.name}", "Re-render with build_deliverables.py"))
        elif last_change(root, mmd) > last_change(root, svg):
            findings.append(_finding("diagram", f"{mmd.name} changed after images/{svg.name}", "Re-render with build_deliverables.py"))
        if gallery and mmd.stem not in gallery:
            findings.append(_finding("diagram", f"{mmd.name} is not in architecture-diagrams.json", "Add a gallery entry (slug, title, src, summary)"))
    return findings


def check_registry(root: Path, data_text: Dict[str, str]) -> List[Dict[str, str]]:
    reg = root / "architecture" / "architecture-registry.json"
    if not reg.exists():
        return []
    ids = [int(n) for n in re.findall(r"TECH-(\d{3})", reg.read_text(encoding="utf-8"))]
    if not ids:
        return []
    latest = max(ids)
    findings = []
    for name, text in data_text.items():
        for m in re.finditer(r"TECH-001 to TECH-(\d{3})", text):
            if int(m.group(1)) < latest:
                findings.append(_finding("registry", f"{name}: '{m.group(0)}' but registry reaches TECH-{latest:03d}",
                                         "Update the inventory range, service count and Private Endpoint figures"))
    return findings


def check_source_newer(root: Path, data_dir: Path) -> List[Dict[str, str]]:
    sources = [p for pat in SOURCE_GLOBS for p in root.glob(pat)]
    if not sources:
        return []
    newest = max(sources, key=lambda p: last_change(root, p))
    newest_day = datetime.fromtimestamp(last_change(root, newest)).date()
    findings = []
    for f in sorted(data_dir.glob("*.json")):
        try:
            doc = json.loads(f.read_text(encoding="utf-8"))
            stamps = [date.fromisoformat(s) for s in (doc.get("date"), doc.get("reviewed")) if s]
            json_day = max(stamps) if stamps else None
        except (ValueError, AttributeError, TypeError):
            continue
        if json_day and json_day < newest_day:
            findings.append(_finding(
                "source-newer", f"{f.name} is dated {json_day} but {newest.relative_to(root)} changed {newest_day}",
                "Update the page, or if it is still accurate set \"reviewed\": \"YYYY-MM-DD\" in its JSON"))
    return findings


def run_checks(root: Path, deliverables: Path) -> List[Dict[str, str]]:
    data_dir = deliverables / "data"
    data_text = {f.name: f.read_text(encoding="utf-8") for f in sorted(data_dir.glob("*.json"))}
    return (check_adr_range(root, data_text) + check_work_packages(root, data_text)
            + check_diagrams(root, deliverables, data_text) + check_registry(root, data_text)
            + check_source_newer(root, data_dir))


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--workbench", type=Path, default=Path.cwd(), help="Workbench repo root (default: cwd).")
    ap.add_argument("--deliverables", type=Path, help="Deliverables dir (default: <workbench>/deliverables).")
    ap.add_argument("--json", action="store_true", help="Emit findings as JSON.")
    args = ap.parse_args(argv)
    root = args.workbench.resolve()
    deliverables = (args.deliverables or root / "deliverables").resolve()
    if not (deliverables / "data").is_dir():
        print(f"ERROR: {deliverables / 'data'} not found", file=sys.stderr)
        return 2
    findings = run_checks(root, deliverables)
    if args.json:
        print(json.dumps(findings, indent=2))
    elif not findings:
        print("OK: deliverables are in sync with the workbench sources.")
    else:
        for f in findings:
            print(f"[DRIFT] {f['category']}: {f['message']}\n         -> {f['action']}")
        print(f"\n{len(findings)} drift finding(s). Edit deliverables/data/*.json, then run build_deliverables.py.")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
