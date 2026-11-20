#!/usr/bin/env python3
"""Render B.C. Government Design System-compliant HTML outputs from JSON.

Supports three output types:
  - executive-brief: Audience-tailored 1-2 page executive or architecture brief
  - logic-model:     7-stage causal results chain card view (compatible with designing-logic-models JSON)
  - dashboard:       Strategy on a Page / portfolio dashboard with WORK vs IDEA gating
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001F9FF"
    "\U0001FA00-\U0001FAFF"
    "\U00002600-\U000027BF"
    "]+",
    flags=re.UNICODE,
)

INDIGENOUS_TEXT = (
    "We acknowledge with respect that the Government of British Columbia operates on the "
    "traditional territories of Indigenous Peoples across the province, and we recognize their "
    "continuing relationships with the land."
)

BASE_CSS = """
:root {
  --font-primary: 'BC Sans', 'Noto Sans', sans-serif;
  --color-brand-primary: #013366;
  --color-brand-primary-hover: #1E5189;
  --color-brand-focus: #2E5DD7;
  --color-brand-link: #255A90;
  --color-text-primary: #2D2D2D;
  --color-text-secondary: #474543;
  --color-surface-white: #FFFFFF;
  --color-surface-default: #FAF9F8;
  --color-surface-dark: #252423;
  --color-border: #D8D8D8;
  --color-border-indigenous: #FBD389;
  --color-success: #42814A;
  --color-success-bg: #F6FFF8;
  --color-warning: #F8BB47;
  --color-warning-bg: #FEF1D8;
  --color-danger: #CE3E39;
  --color-danger-bg: #F4E1E2;
  --color-info: #2E5DD7;
  --color-info-bg: #D8EAFD;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: var(--font-primary);
  font-size: 16px;
  line-height: 1.5;
  color: var(--color-text-primary);
  background: var(--color-surface-default);
}
:focus-visible {
  outline: 2px solid var(--color-brand-focus);
  outline-offset: 4px;
}
header.bc-header {
  background: var(--color-brand-primary);
  color: var(--color-surface-white);
  border-bottom: 3px solid var(--color-border-indigenous);
  padding: 20px 36px;
}
header.bc-header .org-trail {
  font-size: 12px;
  color: #CADCFC;
  margin-bottom: 4px;
}
header.bc-header h1 {
  font-size: 28px;
  line-height: 1.3;
  margin: 0;
  font-weight: 700;
}
header.bc-header .meta-row {
  margin-top: 8px;
  font-size: 14px;
  color: #E2ECF7;
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}
main.container {
  max-width: 1120px;
  margin: 0 auto;
  padding: 24px 36px 40px;
}
section.block {
  margin-bottom: 24px;
}
h2.section-title {
  font-size: 20px;
  color: var(--color-brand-primary);
  margin: 0 0 12px;
  padding-bottom: 6px;
  border-bottom: 1px solid var(--color-border);
}
.summary-box {
  background: var(--color-surface-white);
  border: 1px solid var(--color-border);
  border-left: 4px solid var(--color-brand-primary);
  border-radius: 4px;
  padding: 16px 20px;
  margin-bottom: 20px;
}
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 16px;
}
.card {
  background: var(--color-surface-white);
  border: 1px solid var(--color-border);
  border-radius: 4px;
  padding: 16px;
}
.card.gate {
  border: 1px dashed var(--color-warning);
  background: var(--color-warning-bg);
}
.card h3 {
  font-size: 16px;
  margin: 0 0 6px;
  color: var(--color-brand-primary);
}
.card p {
  margin: 0;
  font-size: 14px;
  color: var(--color-text-secondary);
}
.metric-value {
  font-size: 24px;
  font-weight: 700;
  color: var(--color-brand-primary);
  margin: 4px 0;
}
.metric-label {
  font-size: 12px;
  color: var(--color-text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.03em;
}
.tag {
  display: inline-block;
  font-size: 12px;
  font-weight: 600;
  padding: 2px 8px;
  border-radius: 4px;
  border: 1px solid var(--color-border);
  background: var(--color-surface-default);
  color: var(--color-text-primary);
  margin-bottom: 8px;
}
.tag-info { background: var(--color-info-bg); border-color: var(--color-info); color: #1A3A8F; }
.tag-success { background: var(--color-success-bg); border-color: var(--color-success); color: #27532D; }
.tag-warning { background: var(--color-warning-bg); border-color: var(--color-warning); color: #5C4308; }
.tag-danger { background: var(--color-danger-bg); border-color: var(--color-danger); color: #7C201D; }
.tag-neutral { background: var(--color-surface-default); border-color: var(--color-border); color: var(--color-text-secondary); }
table {
  width: 100%;
  border-collapse: collapse;
  background: var(--color-surface-white);
  border: 1px solid var(--color-border);
  font-size: 14px;
}
th {
  background: var(--color-brand-primary);
  color: var(--color-surface-white);
  text-align: left;
  padding: 10px 12px;
  font-weight: 600;
}
td {
  padding: 10px 12px;
  border-top: 1px solid var(--color-border);
  vertical-align: top;
}
tr:nth-child(even) td {
  background: var(--color-surface-default);
}
.stage-chain {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 14px;
}
.stage-card {
  background: var(--color-surface-white);
  border: 1px solid var(--color-border);
  border-top: 4px solid var(--color-brand-primary);
  border-radius: 4px;
  padding: 14px;
}
.stage-card .stage-sub {
  font-size: 12px;
  color: var(--color-text-secondary);
  margin-bottom: 8px;
}
.stage-card ul {
  margin: 0;
  padding-left: 18px;
  font-size: 14px;
}
.stage-card li { margin-bottom: 4px; }
footer.bc-indigenous-footer {
  background: var(--color-surface-dark);
  color: var(--color-surface-white);
  border-top: 3px solid var(--color-border-indigenous);
  padding: 18px 36px;
  font-size: 13px;
  line-height: 1.5;
}
@media print {
  body { background: #FFFFFF; font-size: 12px; }
  header.bc-header { padding: 14px 20px; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  main.container { padding: 14px 20px; }
  .card, .stage-card, .summary-box { break-inside: avoid; }
  footer.bc-indigenous-footer { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
}
"""


def esc(val: Any) -> str:
    """HTML-escape any value safely."""
    return html.escape("" if val is None else str(val), quote=True)


def check_no_emoji(data: Any, path: str = "root") -> None:
    """Raise ValueError if any string field contains emoji."""
    if isinstance(data, str):
        if EMOJI_RE.search(data):
            raise ValueError(f"Emoji detected at '{path}': {data!r}. Remove emoji to comply with B.C. Gov style.")
    elif isinstance(data, list):
        for idx, item in enumerate(data):
            check_no_emoji(item, f"{path}[{idx}]")
    elif isinstance(data, dict):
        for k, v in data.items():
            check_no_emoji(v, f"{path}.{k}")


def evaluate_commitment(item: Dict[str, Any]) -> Tuple[bool, str]:
    """Return (is_committed, reason_if_gate) enforcing WORK-X vs IDEA-X rules."""
    kind = item.get("kind", "IDEA")
    if kind == "IDEA":
        return False, "Decision gate (IDEA)"
    missing: List[str] = []
    if not item.get("sponsor"):
        missing.append("sponsor")
    if not item.get("owner"):
        missing.append("owner")
    if item.get("capacity_confirmed") is not True:
        missing.append("confirmed capacity")
    if missing:
        return False, f"Decision gate (missing: {', '.join(missing)})"
    return True, "Committed work"


def render_shell(title: str, org_trail: str, meta_items: List[str], body_html: str, include_footer: bool) -> str:
    """Wrap body HTML in a compliant B.C. Government Design System page."""
    meta_html = "".join(f"<span>{esc(m)}</span>" for m in meta_items if m)
    footer_html = (
        f'<footer class="bc-indigenous-footer" role="contentinfo">{esc(INDIGENOUS_TEXT)}</footer>'
        if include_footer
        else ""
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(title)}</title>
  <style>{BASE_CSS}</style>
</head>
<body>
  <header class="bc-header">
    <div class="org-trail">{esc(org_trail)}</div>
    <h1>{esc(title)}</h1>
    {f'<div class="meta-row">{meta_html}</div>' if meta_html else ''}
  </header>
  <main class="container">
    {body_html}
  </main>
  {footer_html}
</body>
</html>
"""


def render_executive_brief(data: Dict[str, Any]) -> str:
    """Render an audience-tailored executive or architecture brief."""
    for req in ("title", "org_trail", "summary", "sections"):
        if not data.get(req):
            raise ValueError(f"executive-brief JSON missing required field: {req}")

    parts: List[str] = [f'<div class="summary-box"><strong>Executive summary:</strong> {esc(data["summary"])}</div>']

    highlights = data.get("highlights") or []
    if highlights:
        cards = []
        for h in highlights:
            tone = h.get("tone", "neutral")
            cards.append(
                f'<div class="card"><div class="metric-label">{esc(h["label"])}</div>'
                f'<div class="metric-value">{esc(h["value"])}</div>'
                f'<span class="tag tag-{esc(tone)}">{esc(tone.capitalize())}</span></div>'
            )
        parts.append(f'<section class="block"><div class="grid">{"".join(cards)}</div></section>')

    for sec in data["sections"]:
        sec_html = [f'<section class="block"><h2 class="section-title">{esc(sec["heading"])}</h2>']
        if sec.get("body"):
            sec_html.append(f'<p>{esc(sec["body"])}</p>')
        if sec.get("bullets"):
            items = "".join(f"<li>{esc(b)}</li>" for b in sec["bullets"])
            sec_html.append(f"<ul>{items}</ul>")
        if sec.get("cards"):
            c_html = []
            for c in sec["cards"]:
                is_gate = c.get("committed") is False or bool(c.get("missing_evidence"))
                tone = c.get("tone", "warning" if is_gate else "neutral")
                tag_text = c.get("tag") or ("Decision gate" if is_gate else "Detail")
                if c.get("missing_evidence"):
                    tag_text = f"{tag_text} ({c['missing_evidence']})"
                cls = "card gate" if is_gate else "card"
                title_prefix = f"{c['id']}: " if c.get("id") else ""
                c_html.append(
                    f'<div class="{cls}"><span class="tag tag-{esc(tone)}">{esc(tag_text)}</span>'
                    f'<h3>{esc(title_prefix + c["title"])}</h3><p>{esc(c["description"])}</p></div>'
                )
            sec_html.append(f'<div class="grid">{"".join(c_html)}</div>')
        sec_html.append("</section>")
        parts.append("".join(sec_html))

    decisions = data.get("decisions_needed") or []
    if decisions:
        rows = "".join(
            f"<tr><td>{esc(d['decision'])}</td><td>{esc(d['owner'])}</td>"
            f"<td>{esc(d.get('target_date', 'TBD'))}</td><td>{esc(d.get('impact', ''))}</td></tr>"
            for d in decisions
        )
        parts.append(
            '<section class="block"><h2 class="section-title">Decisions needed</h2>'
            "<table><thead><tr><th>Decision</th><th>Owner</th><th>Target date</th><th>Impact</th></tr></thead>"
            f"<tbody>{rows}</tbody></table></section>"
        )

    meta = [
        f"Audience: {data['audience']}" if data.get("audience") else "",
        f"Status: {data['status']}" if data.get("status") else "",
        f"Date: {data['date']}" if data.get("date") else "",
    ]
    return render_shell(
        data["title"],
        data["org_trail"],
        meta,
        "\n".join(parts),
        data.get("indigenous_acknowledgment", True),
    )


def render_logic_model(data: Dict[str, Any]) -> str:
    """Render a 7-stage logic model JSON payload as a clean BC Gov HTML card chain."""
    for req in ("inputs", "activities", "outputs", "immediate_outcomes"):
        if not data.get(req):
            raise ValueError(f"logic-model JSON missing required stage: {req}")

    stage_order = [
        ("need", "#474543"),
        ("inputs", "#255A90"),
        ("activities", "#1E5189"),
        ("outputs", "#42814A"),
        ("immediate_outcomes", "#013366"),
        ("intermediate_outcomes", "#2E5DD7"),
        ("long_term_outcomes", "#252423"),
    ]
    cards: List[str] = []
    for key, accent in stage_order:
        st = data.get(key)
        if not st:
            continue
        items = "".join(f"<li>{esc(i)}</li>" for i in st.get("items", []))
        sub = f'<div class="stage-sub">{esc(st.get("subtitle", ""))}</div>' if st.get("subtitle") else ""
        cards.append(
            f'<div class="stage-card" style="border-top-color: {accent};">'
            f'<h3>{esc(st.get("title", key.replace("_", " ").capitalize()))}</h3>{sub}'
            f"<ul>{items}</ul></div>"
        )

    parts: List[str] = [
        '<section class="block"><h2 class="section-title">Causal results chain</h2>'
        f'<div class="stage-chain">{"".join(cards)}</div></section>'
    ]

    assumptions = data.get("assumptions") or []
    risks = data.get("external_risks") or []
    if assumptions or risks:
        cols: List[str] = []
        if assumptions:
            a_items = "".join(f"<li>{esc(a)}</li>" for a in assumptions)
            cols.append(f'<div class="card"><span class="tag tag-info">Assumptions</span><ul>{a_items}</ul></div>')
        if risks:
            r_items = "".join(f"<li>{esc(r)}</li>" for r in risks)
            cols.append(f'<div class="card"><span class="tag tag-warning">External risks</span><ul>{r_items}</ul></div>')
        parts.append(
            '<section class="block"><h2 class="section-title">Assumptions and external risks</h2>'
            f'<div class="grid">{"".join(cols)}</div></section>'
        )

    meta = [f"Date: {data['date']}" if data.get("date") else ""]
    return render_shell(
        data.get("title", "Program logic model"),
        data.get("org_trail", "Government of British Columbia"),
        meta,
        "\n".join(parts),
        data.get("indigenous_acknowledgment", True),
    )


def render_dashboard(data: Dict[str, Any]) -> str:
    """Render a Strategy on a Page / Portfolio Dashboard with WORK vs IDEA gating."""
    for req in ("title", "org_trail", "objectives", "work_items"):
        if not data.get(req):
            raise ValueError(f"dashboard JSON missing required field: {req}")

    parts: List[str] = []
    if data.get("vision"):
        parts.append(f'<div class="summary-box"><strong>Vision:</strong> {esc(data["vision"])}</div>')

    metrics = data.get("metrics") or []
    if metrics:
        m_cards = "".join(
            f'<div class="card"><div class="metric-label">{esc(m["label"])}</div>'
            f'<div class="metric-value">{esc(m["value"])}</div>'
            f'<span class="tag tag-{esc(m.get("tone", "neutral"))}">{esc(m.get("tone", "neutral").capitalize())}</span></div>'
            for m in metrics
        )
        parts.append(f'<section class="block"><div class="grid">{m_cards}</div></section>')

    obj_cards = "".join(
        f'<div class="card"><span class="tag tag-info">{esc(o["id"])}</span>'
        f'<h3>{esc(o["title"])}</h3><p>{esc(o.get("description", ""))}</p></div>'
        for o in data["objectives"]
    )
    parts.append(f'<section class="block"><h2 class="section-title">Strategic objectives</h2><div class="grid">{obj_cards}</div></section>')

    work_cards: List[str] = []
    for w in data["work_items"]:
        committed, reason = evaluate_commitment(w)
        cls = "card" if committed else "card gate"
        tone = "success" if committed else "warning"
        horizon = f"Horizon: {w['horizon']}" if w.get("horizon") else ""
        work_cards.append(
            f'<div class="{cls}"><span class="tag tag-{tone}">{esc(w["id"])} — {esc(reason)}</span>'
            f'<h3>{esc(w["title"])}</h3><p>{esc(horizon)}</p></div>'
        )
    parts.append(
        '<section class="block"><h2 class="section-title">Committed work and decision gates</h2>'
        f'<div class="grid">{"".join(work_cards)}</div></section>'
    )

    caps = data.get("capabilities") or []
    if caps:
        rows = "".join(
            f"<tr><td>{esc(c['id'])}</td><td>{esc(c['name'])}</td>"
            f"<td>L{esc(c['current_maturity'])}</td><td>L{esc(c['target_maturity'])}</td></tr>"
            for c in caps
        )
        parts.append(
            '<section class="block"><h2 class="section-title">Capability maturity</h2>'
            "<table><thead><tr><th>ID</th><th>Capability</th><th>Current</th><th>Target</th></tr></thead>"
            f"<tbody>{rows}</tbody></table></section>"
        )

    risks = data.get("risks") or []
    if risks:
        rows = "".join(
            f"<tr><td>{esc(r['id'])}</td><td>{esc(r['title'])}</td>"
            f"<td>{esc(r['severity'])}</td><td>{esc(r.get('mitigation', ''))}</td></tr>"
            for r in risks
        )
        parts.append(
            '<section class="block"><h2 class="section-title">Key risks</h2>'
            "<table><thead><tr><th>ID</th><th>Risk</th><th>Severity</th><th>Mitigation</th></tr></thead>"
            f"<tbody>{rows}</tbody></table></section>"
        )

    meta = [f"Date: {data['date']}" if data.get("date") else ""]
    return render_shell(
        data["title"],
        data["org_trail"],
        meta,
        "\n".join(parts),
        data.get("indigenous_acknowledgment", True),
    )


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Render B.C. Gov Design System HTML briefs and dashboards from JSON.")
    parser.add_argument("--type", required=True, choices=["executive-brief", "logic-model", "dashboard"], help="Output template type.")
    parser.add_argument("--input", required=True, type=Path, help="Path to input JSON file.")
    parser.add_argument("--output", type=Path, help="Path to write HTML output (defaults to stdout).")
    parser.add_argument("--validate-only", action="store_true", help="Validate input JSON without writing HTML.")
    args = parser.parse_args(argv)

    data = json.loads(args.input.read_text(encoding="utf-8"))
    check_no_emoji(data)

    if args.type == "executive-brief":
        rendered = render_executive_brief(data)
    elif args.type == "logic-model":
        rendered = render_logic_model(data)
    else:
        rendered = render_dashboard(data)

    if args.validate_only:
        print(f"OK: {args.input} passed {args.type} validation.")
        return 0

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
        print(f"Wrote {args.type} HTML to {args.output}")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    sys.exit(main())
