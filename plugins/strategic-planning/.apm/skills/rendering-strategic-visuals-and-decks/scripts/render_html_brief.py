#!/usr/bin/env python3
"""Render B.C. Government Design System-compliant HTML outputs from JSON.

Supports three output types:
  - executive-brief: Audience-tailored 1-2 page executive or architecture brief
  - logic-model:     7-stage causal results chain card view (compatible with designing-logic-models JSON)
  - dashboard:       Strategy on a Page / portfolio dashboard with WORK vs IDEA gating
"""

from __future__ import annotations

import argparse
import base64
import html
import json
import mimetypes
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
nav.bc-nav {
  background: var(--color-surface-white);
  border-bottom: 1px solid var(--color-border);
  padding: 0 36px;
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}
nav.bc-nav a {
  display: inline-block;
  padding: 12px 14px;
  font-size: 14px;
  font-weight: 600;
  color: var(--color-brand-link);
  text-decoration: none;
  border-bottom: 3px solid transparent;
}
nav.bc-nav a:hover {
  color: var(--color-brand-primary);
  border-bottom-color: var(--color-border);
}
nav.bc-nav a.active {
  color: var(--color-brand-primary);
  border-bottom-color: var(--color-brand-primary);
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
figure.diagram-figure {
  background: var(--color-surface-white);
  border: 1px solid var(--color-border);
  border-radius: 4px;
  padding: 16px;
  margin: 14px 0 0;
  text-align: center;
}
figure.diagram-figure img {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 0 auto;
}
figure.diagram-figure figcaption {
  margin-top: 10px;
  font-size: 13px;
  color: var(--color-text-secondary);
}
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
  nav.bc-nav { display: none; }
  header.bc-header { padding: 14px 20px; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  main.container { padding: 14px 20px; }
  .card, .stage-card, .summary-box, figure.diagram-figure { break-inside: avoid; }
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


def render_shell(
    title: str,
    org_trail: str,
    meta_items: List[str],
    body_html: str,
    include_footer: bool,
    nav_items: Optional[List[Tuple[str, str]]] = None,
    active_href: Optional[str] = None,
) -> str:
    """Wrap body HTML in a compliant B.C. Government Design System page."""
    meta_html = "".join(f"<span>{esc(m)}</span>" for m in meta_items if m)
    nav_html = ""
    if nav_items:
        links = []
        for label, href in nav_items:
            cls = ' class="active"' if href == active_href else ""
            links.append(f'<a href="{esc(href)}"{cls}>{esc(label)}</a>')
        nav_html = f'<nav class="bc-nav" aria-label="Deliverable sections">{"".join(links)}</nav>'
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
  {nav_html}
  <main class="container">
    {body_html}
  </main>
  {footer_html}
</body>
</html>
"""


def resolve_image_src(src: str, base_dir: Optional[Path], embed: bool) -> str:
    """Resolve an image path, optionally embedding it as a base64 data URI."""
    if not embed or src.startswith(("http://", "https://", "data:")):
        return src
    candidate = Path(src)
    if not candidate.is_absolute() and base_dir is not None:
        candidate = (base_dir / candidate).resolve()
    if not candidate.is_file():
        raise FileNotFoundError(f"Image file not found for embedding: {src} (resolved: {candidate})")
    mime, _ = mimetypes.guess_type(str(candidate))
    if candidate.suffix.lower() == ".svg":
        mime = "image/svg+xml"
    if not mime:
        mime = "application/octet-stream"
    encoded = base64.b64encode(candidate.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def render_image_figure(
    img: Dict[str, Any], base_dir: Optional[Path] = None, embed_all: bool = False
) -> str:
    """Render a BC Gov styled <figure> block for a diagram or image."""
    src = img["src"]
    alt = img["alt"]
    embed = embed_all or bool(img.get("embed", False))
    resolved_src = resolve_image_src(src, base_dir, embed)
    style_attr = f' style="width: {esc(img["width"])};"' if img.get("width") else ""
    caption_html = f"<figcaption>{esc(img['caption'])}</figcaption>" if img.get("caption") else ""
    return (
        f'<figure class="diagram-figure">'
        f'<img src="{esc(resolved_src)}" alt="{esc(alt)}"{style_attr}>'
        f"{caption_html}</figure>"
    )


def render_executive_brief(
    data: Dict[str, Any],
    base_dir: Optional[Path] = None,
    embed_images: bool = False,
    nav_items: Optional[List[Tuple[str, str]]] = None,
    active_href: Optional[str] = None,
) -> str:
    """Render an audience-tailored executive or architecture brief."""
    for req in ("title", "org_trail", "summary", "sections"):
        if not data.get(req):
            raise ValueError(f"executive-brief JSON missing required field: {req}")

    parts: List[str] = [f'<div class="summary-box"><strong>Executive summary:</strong> {esc(data["summary"])}</div>']

    if data.get("hero_image"):
        parts.append(
            f'<section class="block">{render_image_figure(data["hero_image"], base_dir, embed_images)}</section>'
        )

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
        if sec.get("images"):
            for img in sec["images"]:
                sec_html.append(render_image_figure(img, base_dir, embed_images))
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
        nav_items=nav_items,
        active_href=active_href,
    )


def render_logic_model(
    data: Dict[str, Any],
    nav_items: Optional[List[Tuple[str, str]]] = None,
    active_href: Optional[str] = None,
) -> str:
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
        nav_items=nav_items,
        active_href=active_href,
    )


def render_dashboard(
    data: Dict[str, Any],
    base_dir: Optional[Path] = None,
    embed_images: bool = False,
    nav_items: Optional[List[Tuple[str, str]]] = None,
    active_href: Optional[str] = None,
) -> str:
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

    diagrams = data.get("diagrams") or []
    if diagrams:
        diag_blocks = []
        for d in diagrams:
            heading = f"<h3>{esc(d['title'])}</h3>" if d.get("title") else ""
            diag_blocks.append(f"{heading}{render_image_figure(d, base_dir, embed_images)}")
        parts.append(
            f'<section class="block"><h2 class="section-title">Architecture and strategy diagrams</h2>{"".join(diag_blocks)}</section>'
        )

    meta = [f"Date: {data['date']}" if data.get("date") else ""]
    return render_shell(
        data["title"],
        data["org_trail"],
        meta,
        "\n".join(parts),
        data.get("indigenous_acknowledgment", True),
        nav_items=nav_items,
        active_href=active_href,
    )


def render_site(
    site_data: Dict[str, Any],
    site_dir: Path,
    output_dir: Path,
    embed_images: bool = False,
) -> List[Path]:
    """Render an index.html hub and all linked subpages with shared BC Gov navigation."""
    for req in ("title", "org_trail", "summary", "pages"):
        if not site_data.get(req):
            raise ValueError(f"deliverable-site JSON missing required field: {req}")

    nav_items: List[Tuple[str, str]] = [("Overview", "index.html")] + [
        (p["label"], p["filename"]) for p in site_data["pages"]
    ]
    output_dir.mkdir(parents=True, exist_ok=True)
    written: List[Path] = []

    cards_html = "".join(
        f'<div class="card"><span class="tag tag-info">{esc(p["type"])}</span>'
        f'<h3><a href="{esc(p["filename"])}" style="color: var(--color-brand-primary); text-decoration: none;">'
        f'{esc(p["label"])}</a></h3>'
        f'<p>{esc(p.get("description", ""))}</p></div>'
        for p in site_data["pages"]
    )
    index_body = (
        f'<div class="summary-box"><strong>Overview:</strong> {esc(site_data["summary"])}</div>'
        f'<section class="block"><h2 class="section-title">Architecture and strategy deliverables</h2>'
        f'<div class="grid">{cards_html}</div></section>'
    )
    meta = [
        f"Subtitle: {site_data['subtitle']}" if site_data.get("subtitle") else "",
        f"Date: {site_data['date']}" if site_data.get("date") else "",
    ]
    index_path = output_dir / "index.html"
    index_path.write_text(
        render_shell(
            site_data["title"],
            site_data["org_trail"],
            meta,
            index_body,
            site_data.get("indigenous_acknowledgment", True),
            nav_items=nav_items,
            active_href="index.html",
        ),
        encoding="utf-8",
    )
    written.append(index_path)

    for page in site_data["pages"]:
        in_path = (site_dir / page["input"]).resolve()
        page_data = json.loads(in_path.read_text(encoding="utf-8"))
        check_no_emoji(page_data)
        ptype = page["type"]
        if ptype == "executive-brief":
            html_out = render_executive_brief(
                page_data, base_dir=in_path.parent, embed_images=embed_images,
                nav_items=nav_items, active_href=page["filename"],
            )
        elif ptype == "logic-model":
            html_out = render_logic_model(
                page_data, nav_items=nav_items, active_href=page["filename"],
            )
        else:
            html_out = render_dashboard(
                page_data, base_dir=in_path.parent, embed_images=embed_images,
                nav_items=nav_items, active_href=page["filename"],
            )
        dest = output_dir / page["filename"]
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(html_out, encoding="utf-8")
        written.append(dest)

    return written


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Render B.C. Gov Design System HTML briefs, dashboards, and multi-page sites from JSON.")
    parser.add_argument("--type", required=True, choices=["executive-brief", "logic-model", "dashboard", "site"], help="Output template type.")
    parser.add_argument("--input", required=True, type=Path, help="Path to input JSON file.")
    parser.add_argument("--output", type=Path, help="Path to write HTML output (for single-page types).")
    parser.add_argument("--output-dir", type=Path, help="Directory to write index.html and subpages (for --type site).")
    parser.add_argument("--embed-images", action="store_true", help="Embed local .svg/.png images as base64 data URIs for self-contained HTML.")
    parser.add_argument("--validate-only", action="store_true", help="Validate input JSON without writing HTML.")
    args = parser.parse_args(argv)

    data = json.loads(args.input.read_text(encoding="utf-8"))
    check_no_emoji(data)
    base_dir = args.input.resolve().parent

    if args.type == "site":
        if args.validate_only:
            print(f"OK: {args.input} passed site validation.")
            return 0
        out_dir = args.output_dir or base_dir
        written = render_site(data, site_dir=base_dir, output_dir=out_dir, embed_images=args.embed_images)
        for p in written:
            print(f"Wrote {p}")
        return 0

    if args.type == "executive-brief":
        rendered = render_executive_brief(data, base_dir=base_dir, embed_images=args.embed_images)
    elif args.type == "logic-model":
        rendered = render_logic_model(data)
    else:
        rendered = render_dashboard(data, base_dir=base_dir, embed_images=args.embed_images)

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
