#!/usr/bin/env python3
"""Generate syntax-safe, B.C. Gov-styled Mermaid diagrams from strategy/architecture JSON.

Enforces:
  - Quoted node labels when containing parentheses, colons, brackets, or slashes
  - Automatic <br> line wrapping every 15-18 characters
  - Solid nodes/bars for committed WORK-X vs dashed nodes/milestone gates for IDEA-X or unconfirmed WORK-X
"""

from __future__ import annotations

import argparse
import json
import sys
import textwrap
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


def wrap_label(text: str, width: int = 16) -> str:
    """Wrap text with <br> every ~15-18 characters and normalize quotes."""
    clean = text.replace('"', "'").strip()
    lines = textwrap.wrap(clean, width=width, break_long_words=False, break_on_hyphens=False)
    return "<br>".join(lines) if lines else clean


def is_committed(item: Dict[str, Any]) -> Tuple[bool, str]:
    """Check whether a work item meets commitment criteria."""
    if item.get("kind", "IDEA") == "IDEA":
        return False, "IDEA gate"
    missing: List[str] = []
    if not item.get("sponsor"):
        missing.append("no sponsor")
    if not item.get("owner"):
        missing.append("no owner")
    if item.get("capacity_confirmed") is not True:
        missing.append("capacity unconfirmed")
    if missing:
        return False, "; ".join(missing)
    return True, "committed"


def render_gantt(data: Dict[str, Any]) -> str:
    """Render a Mermaid Gantt chart separating committed WORK-X bars from IDEA-X milestones."""
    title = data.get("title", "Strategic roadmap")
    lines = [
        "gantt",
        f"    title {title}",
        "    dateFormat  YYYY-MM-DD",
        "    axisFormat  %b %Y",
    ]
    by_horizon: Dict[str, List[Dict[str, Any]]] = {}
    for w in data.get("work_items", []):
        horizon = w.get("horizon", "Horizon 1")
        by_horizon.setdefault(horizon, []).append(w)

    for horizon, items in by_horizon.items():
        lines.append(f"    section {horizon}")
        for w in items:
            committed, reason = is_committed(w)
            start = w.get("start_date", "2026-01-01")
            dur = w.get("duration", "30d")
            safe_id = w["id"].replace("-", "_")
            label = f"{w['id']} {w['title']}".replace(":", " -")
            if committed:
                lines.append(f"    {label} :{safe_id}, {start}, {dur}")
            else:
                lines.append(f"    {label} ({reason}) :milestone, {safe_id}, {start}, 0d")
    return "\n".join(lines)


def render_traceability(data: Dict[str, Any]) -> str:
    """Render a left-to-right Mermaid traceability graph (OBJ -> CAP -> WORK/IDEA)."""
    lines = [
        "flowchart LR",
        "    classDef obj fill:#013366,stroke:#013366,color:#FFFFFF;",
        "    classDef cap fill:#D8EAFD,stroke:#2E5DD7,color:#2D2D2D;",
        "    classDef work fill:#F6FFF8,stroke:#42814A,color:#2D2D2D;",
        "    classDef gate fill:#FEF1D8,stroke:#F8BB47,stroke-dasharray: 5 5,color:#2D2D2D;",
    ]
    for obj in data.get("objectives", []):
        oid = obj["id"].replace("-", "_")
        lines.append(f'    {oid}["{wrap_label(obj["id"] + ": " + obj["title"])}"]:::obj')

    for cap in data.get("capabilities", []):
        cid = cap["id"].replace("-", "_")
        lines.append(f'    {cid}["{wrap_label(cap["id"] + ": " + cap["name"])}"]:::cap')
        for oid in cap.get("objective_ids", []):
            lines.append(f"    {oid.replace('-', '_')} --> {cid}")

    for w in data.get("work_items", []):
        wid = w["id"].replace("-", "_")
        committed, reason = is_committed(w)
        cls = "work" if committed else "gate"
        suffix = "" if committed else f" ({reason})"
        lines.append(f'    {wid}["{wrap_label(w["id"] + ": " + w["title"] + suffix)}"]:::{cls}')
        for cid in w.get("capability_ids", []):
            arrow = "-->" if committed else "-.->"
            lines.append(f"    {cid.replace('-', '_')} {arrow} {wid}")

    return "\n".join(lines)


def render_capability_gap(data: Dict[str, Any]) -> str:
    """Render a Mermaid xychart-beta comparing current vs target capability maturity (0-5)."""
    caps = data.get("capabilities", [])
    if not caps:
        raise ValueError("No capabilities found in JSON for capability-gap chart.")
    labels = ", ".join(f'"{c["id"]}"' for c in caps)
    currents = ", ".join(str(c["current_maturity"]) for c in caps)
    targets = ", ".join(str(c["target_maturity"]) for c in caps)
    title = data.get("title", "Capability maturity gap (0-5)")
    return "\n".join([
        "xychart-beta",
        f'    title "{title}"',
        f"    x-axis [{labels}]",
        '    y-axis "Maturity level" 0 --> 5',
        f"    bar [{currents}]",
        f"    line [{targets}]",
    ])


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Generate syntax-safe B.C. Gov Mermaid diagrams from JSON.")
    parser.add_argument("--type", required=True, choices=["gantt", "traceability", "capability-gap"], help="Diagram type.")
    parser.add_argument("--input", required=True, type=Path, help="Path to dashboard/roadmap JSON.")
    parser.add_argument("--output", type=Path, help="Write .mmd or .md file (defaults to stdout).")
    parser.add_argument("--raw", action="store_true", help="Omit ```mermaid code fence.")
    args = parser.parse_args(argv)

    data = json.loads(args.input.read_text(encoding="utf-8"))
    if args.type == "gantt":
        body = render_gantt(data)
    elif args.type == "traceability":
        body = render_traceability(data)
    else:
        body = render_capability_gap(data)

    rendered = body if args.raw else f"```mermaid\n{body}\n```"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
        print(f"Wrote {args.type} Mermaid diagram to {args.output}")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    sys.exit(main())
