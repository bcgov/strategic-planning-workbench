#!/usr/bin/env python3
"""Render B.C. Government Design System executive decks from JSON.

Supports:
  - marp:      Markdown deck with Marp frontmatter, BC Gov CSS tokens, and Indigenous acknowledgment slides
  - pptx-spec: Structured JSON payload aligned with bc-gov-design-system/assets/generate.js tokens
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from render_html_brief import INDIGENOUS_TEXT, check_no_emoji


def render_marp(data: Dict[str, Any]) -> str:
    """Render a Marp-compatible Markdown presentation deck."""
    for req in ("title", "org_trail", "slides"):
        if not data.get(req):
            raise ValueError(f"executive-deck JSON missing required field: {req}")

    frontmatter = """---
marp: true
theme: default
paginate: true
style: |
  section {
    font-family: 'BC Sans', 'Noto Sans', sans-serif;
    background-color: #FAF9F8;
    color: #2D2D2D;
    padding: 48px 56px;
  }
  section.title-slide, section.closing-slide {
    background-color: #013366;
    color: #FFFFFF;
    border-bottom: 8px solid #FBD389;
  }
  section.closing-slide {
    background-color: #252423;
    border-top: 6px solid #FBD389;
    border-bottom: none;
  }
  h1, h2 { color: #013366; font-weight: 700; }
  section.title-slide h1, section.title-slide h2, section.closing-slide h1, section.closing-slide h2 {
    color: #FFFFFF;
  }
  table { font-size: 0.85em; width: 100%; border-collapse: collapse; }
  th { background-color: #013366; color: #FFFFFF; padding: 8px 10px; text-align: left; }
  td { border-top: 1px solid #D8D8D8; padding: 8px 10px; }
  .columns { display: grid; grid-template-columns: 1fr 1fr; gap: 28px; }
  .ack { margin-top: 28px; padding-top: 12px; border-top: 2px solid #FBD389; font-size: 0.72em; color: #E2ECF7; }
---
"""
    parts: List[str] = [frontmatter]

    # Title slide
    ack_block = f'\n<div class="ack">{INDIGENOUS_TEXT}</div>' if data.get("indigenous_acknowledgment", True) else ""
    meta_line = " • ".join(x for x in [data.get("org_trail"), data.get("presenter"), data.get("date")] if x)
    subtitle = f"\n## {data['subtitle']}" if data.get("subtitle") else ""
    parts.append(f"<!-- _class: title-slide -->\n\n# {data['title']}{subtitle}\n\n{meta_line}{ack_block}\n")

    for sl in data["slides"]:
        layout = sl["layout"]
        slide_md: List[str] = [f"## {sl['heading']}"]
        if sl.get("lead"):
            slide_md.append(f"\n{sl['lead']}")

        if layout in ("summary", "bullets", "decisions"):
            for b in sl.get("bullets", []):
                slide_md.append(f"- {b}")
        elif layout == "two-column":
            left = "\n".join(f"- {b}" for b in sl.get("left_bullets", []))
            right = "\n".join(f"- {b}" for b in sl.get("right_bullets", []))
            slide_md.append(
                '\n<div class="columns">\n<div>\n\n'
                f"### {sl.get('left_title', 'Current state')}\n\n{left}\n\n"
                "</div>\n<div>\n\n"
                f"### {sl.get('right_title', 'Target state')}\n\n{right}\n\n"
                "</div>\n</div>"
            )
        elif layout == "table":
            headers = sl.get("table_headers", [])
            rows = sl.get("table_rows", [])
            if headers:
                slide_md.append("\n| " + " | ".join(headers) + " |")
                slide_md.append("| " + " | ".join("---" for _ in headers) + " |")
                for r in rows:
                    slide_md.append("| " + " | ".join(str(c) for c in r) + " |")

        if sl.get("image"):
            img = sl["image"]
            slide_md.append(f"\n![{img['alt']}]({img['src']})")
            if img.get("caption"):
                slide_md.append(f"*{img['caption']}*")

        if sl.get("notes"):
            slide_md.append(f"\n<!-- {sl['notes']} -->")
        parts.append("\n".join(slide_md))

    # Closing slide with Indigenous acknowledgment band
    if data.get("indigenous_acknowledgment", True):
        parts.append(
            "<!-- _class: closing-slide -->\n\n"
            "## Thank you\n\n"
            f"{data.get('org_trail', 'Government of British Columbia')}\n\n"
            f'<div class="ack">{INDIGENOUS_TEXT}</div>'
        )

    return "\n---\n\n".join(parts) + "\n"


def render_pptx_spec(data: Dict[str, Any]) -> str:
    """Emit a structured JSON spec aligned with bc-gov-design-system/assets/generate.js."""
    for req in ("title", "org_trail", "slides"):
        if not data.get(req):
            raise ValueError(f"executive-deck JSON missing required field: {req}")

    spec = {
        "theme": "bc-gov-design-system-v5",
        "font": "Calibri",
        "tokens": {
            "navy": "013366",
            "navyHover": "1E5189",
            "focus": "2E5DD7",
            "surface": "FAFAF8",
            "dark": "252423",
            "indigenous": "FBD389",
            "textPrimary": "2D2D2D",
            "textSecond": "474543",
            "border": "D8D8D8",
        },
        "titleSlide": {
            "title": data["title"],
            "subtitle": data.get("subtitle", ""),
            "orgTrail": data["org_trail"],
            "presenter": data.get("presenter", ""),
            "date": data.get("date", ""),
            "indigenousBand": data.get("indigenous_acknowledgment", True),
        },
        "slides": data["slides"],
        "closingSlide": {
            "indigenousAcknowledgment": INDIGENOUS_TEXT if data.get("indigenous_acknowledgment", True) else ""
        },
    }
    return json.dumps(spec, indent=2) + "\n"


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Render B.C. Gov executive decks (Marp or pptx-spec) from JSON.")
    parser.add_argument("--input", required=True, type=Path, help="Path to executive-deck JSON.")
    parser.add_argument("--format", required=True, choices=["marp", "pptx-spec"], help="Output format.")
    parser.add_argument("--output", type=Path, help="Path to write output (defaults to stdout).")
    args = parser.parse_args(argv)

    data = json.loads(args.input.read_text(encoding="utf-8"))
    check_no_emoji(data)

    rendered = render_marp(data) if args.format == "marp" else render_pptx_spec(data)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
        print(f"Wrote {args.format} deck to {args.output}")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    sys.exit(main())
