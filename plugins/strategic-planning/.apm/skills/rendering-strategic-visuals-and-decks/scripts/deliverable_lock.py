#!/usr/bin/env python3
"""Deterministic source-to-JSON sync tracking for a workbench's ``deliverables/``.

Two mechanisms, both standard library only:

1. **Lockfile** (``data/sources.json`` declares which workbench files feed each page JSON;
   ``data/sync.lock.json`` records their SHA-256 hashes when the page was last synced).
   ``status`` is a pure hash comparison, so it works the same for a human edit, an agent
   edit, or an uncommitted change, and can fail CI. ``stamp`` records "this page now
   reflects those sources" and is run only after the page JSON was updated or confirmed.
2. **Derived-fact tokens** such as ``{{adr.latest}}`` or ``{{tech.count}}`` in page JSON,
   expanded at render time from the workbench files, so mechanical facts cannot drift.

CLI: ``init`` | ``status`` | ``worklist [--diff]`` | ``stamp PAGE... | --all`` | ``facts``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render_html_brief import expand_tokens  # noqa: E402,F401  (re-exported for callers)

SOURCES_FILE = "sources.json"
LOCK_FILE = "sync.lock.json"
DEFAULT_SOURCES = [
    "01-vision.md", "02-architecture.md", "04-open-questions.md", "05-mvp-three-domains.md",
    "06-architecture-principles.md", "implementation-plan.md", "adrs/README.md",
    "work-packages/README.md", "architecture/*.md", "architecture/patterns/*.md",
    "architecture/technologies/*.md", "architecture/architecture-registry.json", "diagrams/*.mmd",
]


# ---------------------------------------------------------------- helpers
def _git(root: Path, *args: str) -> Optional[str]:
    try:
        out = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, check=True)
        return out.stdout
    except (OSError, subprocess.CalledProcessError):
        return None


def file_hash(path: Path) -> str:
    """SHA-256 of the file with CRLF normalised to LF, so line endings never cause drift."""
    data = path.read_bytes().replace(b"\r\n", b"\n")
    return hashlib.sha256(data).hexdigest()


def page_files(data_dir: Path) -> List[str]:
    return sorted(p.name for p in data_dir.glob("*.json") if p.name not in (SOURCES_FILE, LOCK_FILE))


def load_json(path: Path, default: Any) -> Any:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def declared_sources(data_dir: Path, page: str) -> List[str]:
    cfg = load_json(data_dir / SOURCES_FILE, {})
    defaults = cfg.get("defaults", DEFAULT_SOURCES)
    entry = cfg.get("pages", {}).get(page)
    if entry is None:
        return list(defaults)
    out: List[str] = []
    for item in entry:
        out.extend(defaults if item == "$defaults" else [item])
    return out


def resolve_sources(root: Path, patterns: List[str]) -> Dict[str, str]:
    """Map every existing file matched by the patterns to its hash (relative POSIX paths)."""
    found: Dict[str, str] = {}
    for pat in patterns:
        for p in sorted(root.glob(pat)):
            if p.is_file():
                found[p.relative_to(root).as_posix()] = file_hash(p)
    return found


# ---------------------------------------------------------------- derived facts
def derive_facts(root: Path) -> Dict[str, str]:
    """Mechanical facts read from the workbench; used for ``{{token}}`` expansion."""
    facts: Dict[str, str] = {}
    adr = root / "adrs" / "README.md"
    if adr.exists():
        ids = sorted({int(n) for n in re.findall(r"^##\s+ADR-(\d+)", adr.read_text(encoding="utf-8"), re.M)})
        if ids:
            facts.update({"adr.latest": f"{ids[-1]:03d}", "adr.count": str(len(ids)),
                          "adr.range": f"ADR-001 to ADR-{ids[-1]:03d}"})
    reg = root / "architecture" / "architecture-registry.json"
    if reg.exists():
        ids = sorted({int(n) for n in re.findall(r"TECH-(\d{3})", reg.read_text(encoding="utf-8"))})
        if ids:
            facts.update({"tech.latest": f"{ids[-1]:03d}", "tech.count": str(len(ids)),
                          "tech.range": f"TECH-001 to TECH-{ids[-1]:03d}"})
    wp = root / "work-packages" / "README.md"
    if wp.exists():
        wps = re.findall(r"^##\s+(WP-\d+[A-Z]?)\b", wp.read_text(encoding="utf-8"), re.M)
        if wps:
            facts.update({"wp.count": str(len(wps)), "wp.ids": ", ".join(wps)})
    mmd = list((root / "diagrams").glob("*.mmd")) if (root / "diagrams").is_dir() else []
    if mmd:
        facts["diagram.count"] = str(len(mmd))
    return facts



# ---------------------------------------------------------------- status / stamp
def status(root: Path, data_dir: Path) -> List[Dict[str, Any]]:
    lock = load_json(data_dir / LOCK_FILE, {}).get("pages", {})
    results = []
    for page in page_files(data_dir):
        current = resolve_sources(root, declared_sources(data_dir, page))
        entry = lock.get(page)
        if entry is None:
            results.append({"page": page, "state": "unstamped", "changed": [], "added": sorted(current), "removed": []})
            continue
        old = entry.get("sources", {})
        changed = sorted(k for k in current if k in old and current[k] != old[k])
        added = sorted(k for k in current if k not in old)
        removed = sorted(k for k in old if k not in current)
        state = "ok" if not (changed or added or removed) else "stale"
        results.append({"page": page, "state": state, "changed": changed, "added": added, "removed": removed,
                        "commit": entry.get("commit")})
    return results


def stamp(root: Path, data_dir: Path, pages: List[str]) -> List[str]:
    lock_path = data_dir / LOCK_FILE
    lock = load_json(lock_path, {"version": 1, "pages": {}})
    head = (_git(root, "rev-parse", "HEAD") or "").strip() or None
    done = []
    for page in pages:
        path = data_dir / page
        if not path.exists():
            raise FileNotFoundError(f"{page} not found in {data_dir}")
        json.loads(path.read_text(encoding="utf-8"))  # must parse
        lock["pages"][page] = {"stamped": date.today().isoformat(), "commit": head,
                               "sources": resolve_sources(root, declared_sources(data_dir, page))}
        done.append(page)
    lock["pages"] = dict(sorted(lock["pages"].items()))
    lock_path.write_text(json.dumps(lock, indent=2) + "\n", encoding="utf-8")
    return done


def init_sources(data_dir: Path) -> Path:
    path = data_dir / SOURCES_FILE
    if path.exists():
        return path
    path.write_text(json.dumps({
        "_comment": "Workbench files (globs, relative to the repo root) that feed each page JSON. "
                    "A page without an entry uses 'defaults'. Use '$defaults' inside a page list to extend them.",
        "defaults": DEFAULT_SOURCES, "pages": {}}, indent=2) + "\n", encoding="utf-8")
    return path


def worklist(root: Path, data_dir: Path, with_diff: bool = False, max_diff_lines: int = 120) -> str:
    lines: List[str] = []
    for r in status(root, data_dir):
        if r["state"] == "ok":
            continue
        lines.append(f"## {r['page']} ({r['state']})")
        for label, key in (("changed", "changed"), ("new source", "added"), ("removed", "removed")):
            for f in r[key]:
                lines.append(f"- {label}: {f}")
        if with_diff and r.get("commit") and r["changed"]:
            diff = _git(root, "diff", "--unified=2", r["commit"], "--", *r["changed"])
            if diff:
                dl = diff.splitlines()
                lines.append("```diff")
                lines.extend(dl[:max_diff_lines])
                if len(dl) > max_diff_lines:
                    lines.append(f"... {len(dl) - max_diff_lines} more diff lines (run git diff {r['commit'][:8]} -- <file>)")
                lines.append("```")
        lines.append("")
    return "\n".join(lines).rstrip()


# ---------------------------------------------------------------- CLI
def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("command", choices=["init", "status", "worklist", "stamp", "facts"])
    ap.add_argument("pages", nargs="*", help="Page JSON names for stamp (e.g. executive-brief.json).")
    ap.add_argument("--all", action="store_true", help="stamp: every page JSON.")
    ap.add_argument("--diff", action="store_true", help="worklist: include source diffs since the last stamp.")
    ap.add_argument("--workbench", type=Path, default=Path.cwd())
    ap.add_argument("--deliverables", type=Path)
    args = ap.parse_args(argv)
    root = args.workbench.resolve()
    data_dir = (args.deliverables or root / "deliverables").resolve() / "data"
    if not data_dir.is_dir():
        print(f"ERROR: {data_dir} not found", file=sys.stderr)
        return 2
    if args.command == "init":
        print(f"Wrote {init_sources(data_dir)} (edit to narrow sources per page), then run: stamp --all")
        return 0
    if args.command == "facts":
        for k, v in sorted(derive_facts(root).items()):
            print(f"{{{{{k}}}}} = {v}")
        return 0
    if args.command == "stamp":
        pages = page_files(data_dir) if args.all else args.pages
        if not pages:
            print("ERROR: name pages to stamp, or use --all", file=sys.stderr)
            return 2
        for p in stamp(root, data_dir, pages):
            print(f"stamped {p}")
        return 0
    if args.command == "worklist":
        text = worklist(root, data_dir, with_diff=args.diff)
        print(text or "Nothing to do: every page is in sync with its sources.")
        return 1 if text else 0
    res = status(root, data_dir)
    bad = [r for r in res if r["state"] != "ok"]
    for r in res:
        extra = f" changed={r['changed']} new={r['added']} removed={r['removed']}" if r["state"] == "stale" else ""
        print(f"{r['state']:9} {r['page']}{extra if r['state'] == 'stale' else ''}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
