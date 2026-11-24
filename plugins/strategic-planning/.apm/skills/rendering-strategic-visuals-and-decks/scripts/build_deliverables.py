#!/usr/bin/env python3
"""One-command validate, render and verify for a workbench's ``deliverables/`` folder.

Runs, in order: drift report, real validation of every page JSON listed in
``data/site.json`` (existence, emoji, required fields), site render with Mermaid to SVG
conversion, deck render (Marp and pptx-spec), and a relative link and anchor check.
Standard library only; Mermaid conversion needs ``mmdc`` or ``npx``.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import List, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent))

import check_deliverable_sync  # noqa: E402
import render_deck  # noqa: E402
import render_html_brief  # noqa: E402


def validate_inputs(data_dir: Path) -> List[str]:
    """Return a list of problems with site.json, each page input and the deck JSON."""
    problems: List[str] = []
    site_path = data_dir / "site.json"
    if not site_path.exists():
        return [f"missing {site_path}"]
    site = json.loads(site_path.read_text(encoding="utf-8"))
    for req in ("title", "org_trail", "summary", "pages"):
        if not site.get(req):
            problems.append(f"site.json missing required field: {req}")
    inputs = [(p.get("label", "?"), data_dir / p["input"]) for p in site.get("pages", []) if p.get("input")]
    deck = data_dir / "executive-deck.json"
    if deck.exists():
        inputs.append(("executive deck", deck))
    for label, path in [("site", site_path)] + inputs:
        if not path.exists():
            problems.append(f"{label}: input {path.name} not found")
            continue
        try:
            render_html_brief.check_no_emoji(json.loads(path.read_text(encoding="utf-8")))
        except (ValueError, json.JSONDecodeError) as exc:
            problems.append(f"{path.name}: {exc}")
    return problems


def check_links(out_dir: Path) -> List[str]:
    """Verify relative href/src targets exist and cross-page #anchors resolve."""
    problems: List[str] = []
    cache: dict = {}
    pages = sorted(out_dir.glob("*.html")) + sorted((out_dir / "diagrams").glob("*.html"))
    for page in pages:
        text = page.read_text(encoding="utf-8")
        for target in re.findall(r'(?:href|src)="([^"#:]+)(?:#[^"]*)?"', text):
            if not (page.parent / target).exists():
                problems.append(f"{page.relative_to(out_dir)}: broken target {target}")
        for target, anchor in re.findall(r'href="([^"#:]+\.html)#([^"]+)"', text):
            dest = page.parent / target
            if dest.exists():
                cache.setdefault(dest, dest.read_text(encoding="utf-8"))
                if f'id="{anchor}"' not in cache[dest]:
                    problems.append(f"{page.relative_to(out_dir)}: no anchor #{anchor} in {target}")
    return problems


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--workbench", type=Path, default=Path.cwd(), help="Workbench repo root (default: cwd).")
    ap.add_argument("--deliverables", type=Path, help="Deliverables dir (default: <workbench>/deliverables).")
    ap.add_argument("--check", action="store_true", help="Drift report and validation only; write nothing.")
    ap.add_argument("--skip-mmd", action="store_true", help="Do not convert .mmd to .svg (reuse existing images).")
    ap.add_argument("--skip-deck", action="store_true", help="Do not render the executive deck.")
    args = ap.parse_args(argv)
    root = args.workbench.resolve()
    out = (args.deliverables or root / "deliverables").resolve()
    data_dir = out / "data"

    print("== 1/4 Drift report")
    drift = check_deliverable_sync.run_checks(root, out) if data_dir.is_dir() else []
    for f in drift:
        print(f"[DRIFT] {f['category']}: {f['message']}")
    print("none" if not drift else f"{len(drift)} finding(s) (informational: sync the JSON, then re-run)")

    print("== 2/4 Validate inputs")
    problems = validate_inputs(data_dir)
    for p in problems:
        print(f"[ERROR] {p}")
    if problems:
        return 1
    print("OK")
    if args.check:
        return 1 if drift else 0

    print("== 3/4 Render")
    site = json.loads((data_dir / "site.json").read_text(encoding="utf-8"))
    written = render_html_brief.render_site(site, site_dir=data_dir, output_dir=out, convert_mmd=not args.skip_mmd)
    print(f"Wrote {len(written)} HTML file(s)")
    deck = data_dir / "executive-deck.json"
    if deck.exists() and not args.skip_deck:
        d = json.loads(deck.read_text(encoding="utf-8"))
        (out / "executive-deck.marp.md").write_text(render_deck.render_marp(d), encoding="utf-8")
        (out / "executive-deck.pptx-spec.json").write_text(render_deck.render_pptx_spec(d), encoding="utf-8")
        print("Wrote executive-deck.marp.md and executive-deck.pptx-spec.json")

    print("== 4/4 Link check")
    bad = check_links(out)
    for p in bad:
        print(f"[ERROR] {p}")
    print("OK" if not bad else f"{len(bad)} link problem(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
