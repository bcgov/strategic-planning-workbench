#!/usr/bin/env python3
"""Generate 4-Quadrant Investment Prioritization Visuals & Reports.

Reads investment scores from JSON or CSV and produces:
1. Interactive SVG/HTML 4-quadrant scatter chart styled with B.C. Gov Design System tokens.
2. Executive Markdown summary ranking table.
3. Updated CSV/JSON scoring ledgers with calculated weighted scores.

Usage:
    python generate_investment_quadrant.py --input ledger.json --format html --output quadrant.html
    python generate_investment_quadrant.py --input ledger.json --format markdown --output brief.md
    python generate_investment_quadrant.py --input ledger.json --format csv --output scored_ledger.csv
"""

import argparse
import csv
import html
import json
import os
import sys

DEFAULT_FRAMEWORK = {
    "overall_weights": {
        "value_weight": 50.0,
        "delivery_weight": 50.0
    },
    "value_weights": {
        "drivers": 25.0,
        "alignment": 25.0,
        "outcomes_and_benefits": 25.0,
        "sector_benefits": 25.0
    },
    "delivery_weights": {
        "readiness": 20.0,
        "extent_of_research": 20.0,
        "investment_cost": 20.0,
        "executive_support": 20.0,
        "ease_of_implementation": 20.0
    },
    "threshold_x": 5.0,
    "threshold_y": 5.0
}


def calculate_scores(items: list, framework: dict) -> list:
    """Calculate normalized Value, Delivery, Composite scores and Quadrant."""
    v_weights = framework.get("value_weights", DEFAULT_FRAMEWORK["value_weights"])
    d_weights = framework.get("delivery_weights", DEFAULT_FRAMEWORK["delivery_weights"])
    overall = framework.get("overall_weights", DEFAULT_FRAMEWORK["overall_weights"])

    total_v_weight = sum(v_weights.values()) or 100.0
    total_d_weight = sum(d_weights.values()) or 100.0

    w_val = overall.get("value_weight", 50.0)
    w_del = overall.get("delivery_weight", 50.0)
    total_axis_weight = (w_val + w_del) or 100.0

    th_x = framework.get("threshold_x", 5.0)
    th_y = framework.get("threshold_y", 5.0)

    calculated = []
    for item in items:
        scores = item.get("scores", {})

        # Value score
        v_sum = 0.0
        for cat, wt in v_weights.items():
            raw = float(scores.get(cat, item.get(cat, 0.0)))
            v_sum += raw * (wt / total_v_weight)
        value_score = round(v_sum, 2)

        # Delivery score
        d_sum = 0.0
        for cat, wt in d_weights.items():
            raw = float(scores.get(cat, item.get(cat, 0.0)))
            d_sum += raw * (wt / total_d_weight)
        delivery_score = round(d_sum, 2)

        # Composite score
        composite = round(
            (value_score * (w_val / total_axis_weight)) +
            (delivery_score * (w_del / total_axis_weight)),
            2
        )

        # Quadrant determination
        if value_score >= th_y and delivery_score >= th_x:
            quadrant = "Strategic Priorities & Quick Wins"
            action = "Fund and execute immediately"
        elif value_score >= th_y and delivery_score < th_x:
            quadrant = "Strategic Big Bets"
            action = "Fund phased discovery & de-risking"
        elif value_score < th_y and delivery_score >= th_x:
            quadrant = "Tactical Efficiencies"
            action = "Deliver opportunistically if capacity allows"
        else:
            quadrant = "Deprioritize & Defer"
            action = "Defer or decline funding"

        item_copy = dict(item)
        item_copy["value_score"] = value_score
        item_copy["delivery_score"] = delivery_score
        item_copy["composite_score"] = composite
        item_copy["quadrant"] = quadrant
        if not item_copy.get("recommendation"):
            item_copy["recommendation"] = action

        calculated.append(item_copy)

    # Sort descending by composite score
    calculated.sort(key=lambda x: x["composite_score"], reverse=True)
    return calculated


def load_data(file_path: str) -> list:
    """Load items from JSON or CSV."""
    if not os.path.exists(file_path):
        print(f"Error: file not found: {file_path}", file=sys.stderr)
        sys.exit(1)

    if file_path.endswith(".json"):
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            elif isinstance(data, dict) and "items" in data:
                return data["items"]
            return []
    elif file_path.endswith(".csv"):
        items = []
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                item = {
                    "id": row.get("ID", ""),
                    "name": row.get("Name", ""),
                    "sponsor": row.get("Sponsor", ""),
                    "lead_division": row.get("Lead Division", ""),
                    "scores": {
                        "drivers": float(row.get("Drivers (25%)", row.get("drivers", 0.0))),
                        "alignment": float(row.get("Alignment (25%)", row.get("alignment", 0.0))),
                        "outcomes_and_benefits": float(row.get("Outcomes (25%)", row.get("outcomes_and_benefits", 0.0))),
                        "sector_benefits": float(row.get("Sector Benefits (25%)", row.get("sector_benefits", 0.0))),
                        "readiness": float(row.get("Readiness (20%)", row.get("readiness", 0.0))),
                        "extent_of_research": float(row.get("Research (20%)", row.get("extent_of_research", 0.0))),
                        "investment_cost": float(row.get("Cost Affordability (20%)", row.get("investment_cost", 0.0))),
                        "executive_support": float(row.get("Exec Support (20%)", row.get("executive_support", 0.0))),
                        "ease_of_implementation": float(row.get("Ease of Implementation (20%)", row.get("ease_of_implementation", 0.0)))
                    },
                    "recommendation": row.get("Recommendation", "")
                }
                items.append(item)
        return items
    return []


def render_markdown(items: list, framework: dict) -> str:
    """Render Markdown report."""
    lines = []
    lines.append("# Investment Prioritization & Scoring Matrix\n")
    lines.append("| Rank | ID & Proposal Name | Value (0–10) | Delivery (0–10) | Composite (0–10) | Quadrant | Recommended Action |")
    lines.append("|---|---|---|---|---|---|---|")

    for rank, itm in enumerate(items, 1):
        i_id = itm.get("id", f"INV-{rank:03d}")
        name = itm.get("name", "Unnamed Proposal")
        v = itm.get("value_score", 0.0)
        d = itm.get("delivery_score", 0.0)
        c = itm.get("composite_score", 0.0)
        q = itm.get("quadrant", "")
        rec = itm.get("recommendation", "")
        lines.append(f"| {rank} | **{i_id}**: {name} | {v:.2f} | {d:.2f} | **{c:.2f}** | {q} | {rec} |")

    lines.append("\n---\n")
    lines.append("## Quadrant Summary Counts\n")
    q_counts = {}
    for itm in items:
        q = itm.get("quadrant", "Other")
        q_counts[q] = q_counts.get(q, 0) + 1

    lines.append("| Quadrant | Count | Focus |")
    lines.append("|---|---|---|")
    lines.append(f"| **Strategic Priorities & Quick Wins (Q1)** | {q_counts.get('Strategic Priorities & Quick Wins', 0)} | High Value × High Deliverability |")
    lines.append(f"| **Strategic Big Bets (Q2)** | {q_counts.get('Strategic Big Bets', 0)} | High Value × Low Deliverability (requires discovery) |")
    lines.append(f"| **Tactical Efficiencies (Q3)** | {q_counts.get('Tactical Efficiencies', 0)} | Low Value × High Deliverability (opportunistic) |")
    lines.append(f"| **Deprioritize & Defer (Q4)** | {q_counts.get('Deprioritize & Defer', 0)} | Low Value × Low Deliverability (decline funding) |")

    return "\n".join(lines)


def render_html(items: list, framework: dict) -> str:
    """Render self-contained HTML page with SVG 4-Quadrant chart and ranking table."""
    # Chart dimensions
    width = 800
    height = 600
    margin_left = 70
    margin_right = 50
    margin_top = 40
    margin_bottom = 60

    plot_w = width - margin_left - margin_right
    plot_h = height - margin_top - margin_bottom

    # Grid lines (0 to 10)
    grid_svg = []
    for i in range(11):
        x = margin_left + (i / 10.0) * plot_w
        y = margin_top + (1.0 - i / 10.0) * plot_h

        # Vertical line
        stroke_color = "#94A3B8" if i == 5 else "#E2E8F0"
        stroke_w = "2" if i == 5 else "1"
        dash = "stroke-dasharray='4,4'" if i == 5 else ""
        grid_svg.append(f"<line x1='{x}' y1='{margin_top}' x2='{x}' y2='{margin_top + plot_h}' stroke='{stroke_color}' stroke-width='{stroke_w}' {dash}/>")
        grid_svg.append(f"<text x='{x}' y='{margin_top + plot_h + 20}' text-anchor='middle' font-size='12' fill='#64748B'>{i}</text>")

        # Horizontal line
        grid_svg.append(f"<line x1='{margin_left}' y1='{y}' x2='{margin_left + plot_w}' y2='{y}' stroke='{stroke_color}' stroke-width='{stroke_w}' {dash}/>")
        grid_svg.append(f"<text x='{margin_left - 15}' y='{y + 4}' text-anchor='end' font-size='12' fill='#64748B'>{i}</text>")

    # Quadrant background labels
    mid_x = margin_left + 0.5 * plot_w
    mid_y = margin_top + 0.5 * plot_h

    quad_labels = [
        f"<text x='{margin_left + 0.25 * plot_w}' y='{margin_top + 0.25 * plot_h}' text-anchor='middle' font-size='13' font-weight='bold' fill='#6B21A8' opacity='0.7'>Strategic Big Bets<tspan x='{margin_left + 0.25 * plot_w}' dy='16' font-size='11' font-weight='normal'>De-risk & Discover</tspan></text>",
        f"<text x='{margin_left + 0.75 * plot_w}' y='{margin_top + 0.25 * plot_h}' text-anchor='middle' font-size='13' font-weight='bold' fill='#15803D' opacity='0.7'>Strategic Priorities<tspan x='{margin_left + 0.75 * plot_w}' dy='16' font-size='11' font-weight='normal'>Fund & Execute</tspan></text>",
        f"<text x='{margin_left + 0.25 * plot_w}' y='{margin_top + 0.75 * plot_h}' text-anchor='middle' font-size='13' font-weight='bold' fill='#991B1B' opacity='0.7'>Deprioritize & Defer<tspan x='{margin_left + 0.25 * plot_w}' dy='16' font-size='11' font-weight='normal'>Decline Funding</tspan></text>",
        f"<text x='{margin_left + 0.75 * plot_w}' y='{margin_top + 0.75 * plot_h}' text-anchor='middle' font-size='13' font-weight='bold' fill='#0369A1' opacity='0.7'>Tactical Efficiencies<tspan x='{margin_left + 0.75 * plot_w}' dy='16' font-size='11' font-weight='normal'>Deliver Opportunistically</tspan></text>"
    ]

    # Plot bubbles
    bubbles_svg = []
    # Palette for bubbles
    bubble_colors = ["#4338CA", "#6D28D9", "#2563EB", "#0891B2", "#0D9488", "#7C3AED", "#4F46E5"]

    for idx, itm in enumerate(items):
        v = float(itm.get("value_score", 0.0))
        d = float(itm.get("delivery_score", 0.0))
        name = itm.get("name", f"Item {idx+1}")
        i_id = itm.get("id", f"INV-{idx+1:03d}")
        comp = itm.get("composite_score", 0.0)

        cx = margin_left + (d / 10.0) * plot_w
        cy = margin_top + (1.0 - v / 10.0) * plot_h
        color = bubble_colors[idx % len(bubble_colors)]

        # Bubble with hover tooltip
        bubble = f"""
        <g class="chart-point" tabindex="0">
            <title>{html.escape(i_id)}: {html.escape(name)}&#10;Value: {v:.2f} | Delivery: {d:.2f} | Composite: {comp:.2f}&#10;Quadrant: {itm.get('quadrant', '')}</title>
            <circle cx="{cx}" cy="{cy}" r="11" fill="{color}" stroke="#FFFFFF" stroke-width="2" filter="url(#shadow)" opacity="0.88"/>
            <circle cx="{cx}" cy="{cy}" r="4" fill="#FFFFFF"/>
            <text x="{cx + 14}" y="{cy + 4}" font-size="11" font-weight="600" fill="#1E293B" class="point-label">{html.escape(name)}</text>
        </g>
        """
        bubbles_svg.append(bubble)

    # Table rows
    table_rows = []
    for rank, itm in enumerate(items, 1):
        i_id = itm.get("id", f"INV-{rank:03d}")
        name = html.escape(itm.get("name", ""))
        v = itm.get("value_score", 0.0)
        d = itm.get("delivery_score", 0.0)
        c = itm.get("composite_score", 0.0)
        q = html.escape(itm.get("quadrant", ""))
        rec = html.escape(itm.get("recommendation", ""))
        sponsor = html.escape(itm.get("sponsor", "—"))

        badge_class = "badge-q1"
        if "Big Bets" in q:
            badge_class = "badge-q2"
        elif "Tactical" in q:
            badge_class = "badge-q3"
        elif "Defer" in q:
            badge_class = "badge-q4"

        table_rows.append(f"""
        <tr>
            <td style="text-align: center; font-weight: bold;">{rank}</td>
            <td><strong>{i_id}</strong>: {name}</td>
            <td>{sponsor}</td>
            <td style="text-align: right; font-weight: 600;">{v:.2f}</td>
            <td style="text-align: right; font-weight: 600;">{d:.2f}</td>
            <td style="text-align: right; font-weight: bold; color: #1E3A8A;">{c:.2f}</td>
            <td><span class="badge {badge_class}">{q}</span></td>
            <td>{rec}</td>
        </tr>
        """)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Investment Prioritization 4-Quadrant Matrix</title>
    <style>
        :root {{
            --bc-navy: #1E3A8A;
            --bc-blue: #2563EB;
            --bc-surface: #F8FAFC;
            --bc-text: #1F2937;
            --bc-border: #E2E8F0;
        }}
        body {{
            font-family: 'BC Sans', 'Noto Sans', Calibri, sans-serif;
            color: var(--bc-text);
            background-color: var(--bc-surface);
            padding: 24px;
            margin: 0;
            line-height: 1.5;
        }}
        .header {{
            margin-bottom: 24px;
        }}
        h1 {{
            color: var(--bc-navy);
            font-size: 26px;
            margin: 0 0 6px 0;
            font-weight: 700;
        }}
        .lead {{
            color: #475569;
            font-size: 14px;
            margin: 0;
        }}
        .chart-container {{
            background: #FFFFFF;
            border: 1px solid var(--bc-border);
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            margin-bottom: 30px;
            display: flex;
            justify-content: center;
        }}
        svg {{
            overflow: visible;
        }}
        .point-label {{
            paint-order: stroke;
            stroke: #FFFFFF;
            stroke-width: 3px;
            stroke-linecap: butt;
            stroke-linejoin: miter;
        }}
        .table-container {{
            background: #FFFFFF;
            border: 1px solid var(--bc-border);
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 13px;
            text-align: left;
        }}
        th {{
            background-color: var(--bc-navy);
            color: #FFFFFF;
            padding: 12px 14px;
            font-weight: 600;
        }}
        td {{
            padding: 10px 14px;
            border-bottom: 1px solid var(--bc-border);
        }}
        tr:hover td {{
            background-color: #F1F5F9;
        }}
        .badge {{
            display: inline-block;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 600;
        }}
        .badge-q1 {{ background-color: #DCFCE7; color: #166534; }}
        .badge-q2 {{ background-color: #F3E8FF; color: #6B21A8; }}
        .badge-q3 {{ background-color: #E0F2FE; color: #0369A1; }}
        .badge-q4 {{ background-color: #FEE2E2; color: #991B1B; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Investment Prioritization Portfolio Matrix</h1>
        <p class="lead">Evaluating candidate investments across Value / Return on Investment (Y) and Ability to Deliver (X) to determine portfolio funding priorities.</p>
    </div>

    <div class="chart-container">
        <svg width="{width}" height="{height}" viewBox="0 0 {width} {height}">
            <defs>
                <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
                    <feDropShadow dx="0" dy="2" stdDeviation="2" flood-color="#000000" flood-opacity="0.25"/>
                </filter>
                <linearGradient id="quadrantGrad" x1="0%" y1="100%" x2="100%" y2="0%">
                    <stop offset="0%" stop-color="#FEE2E2" stop-opacity="0.55"/>
                    <stop offset="50%" stop-color="#FEF3C7" stop-opacity="0.45"/>
                    <stop offset="100%" stop-color="#DCFCE7" stop-opacity="0.6"/>
                </linearGradient>
            </defs>

            <!-- Gradient background -->
            <rect x="{margin_left}" y="{margin_top}" width="{plot_w}" height="{plot_h}" fill="url(#quadrantGrad)" stroke="#64748B" stroke-width="2"/>

            <!-- Grid lines -->
            {''.join(grid_svg)}

            <!-- Quadrant Labels -->
            {''.join(quad_labels)}

            <!-- Axis Labels -->
            <text x="{margin_left + plot_w / 2}" y="{height - 15}" text-anchor="middle" font-size="14" font-weight="bold" fill="#1E3A8A">Ability to Deliver / Readiness (0 – 10)</text>
            <text x="25" y="{margin_top + plot_h / 2}" text-anchor="middle" font-size="14" font-weight="bold" fill="#1E3A8A" transform="rotate(-90, 25, {margin_top + plot_h / 2})">Value / Return on Investment (0 – 10)</text>

            <!-- Bubbles -->
            {''.join(bubbles_svg)}
        </svg>
    </div>

    <div class="table-container">
        <table>
            <thead>
                <tr>
                    <th style="width: 40px; text-align: center;">Rank</th>
                    <th>Proposal</th>
                    <th>Executive Sponsor</th>
                    <th style="text-align: right;">Value Score</th>
                    <th style="text-align: right;">Delivery Score</th>
                    <th style="text-align: right;">Composite</th>
                    <th>Quadrant</th>
                    <th>Recommendation</th>
                </tr>
            </thead>
            <tbody>
                {''.join(table_rows)}
            </tbody>
        </table>
    </div>
</body>
</html>
"""


def export_csv(items: list, output_path: str):
    """Export scored items to CSV."""
    fieldnames = [
        "Rank", "ID", "Name", "Sponsor", "Lead Division",
        "Value Score (0-10)", "Delivery Score (0-10)", "Composite Score (0-10)",
        "Quadrant", "Recommendation"
    ]
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for rank, itm in enumerate(items, 1):
            writer.writerow({
                "Rank": rank,
                "ID": itm.get("id", f"INV-{rank:03d}"),
                "Name": itm.get("name", ""),
                "Sponsor": itm.get("sponsor", ""),
                "Lead Division": itm.get("lead_division", ""),
                "Value Score (0-10)": f"{itm.get('value_score', 0.0):.2f}",
                "Delivery Score (0-10)": f"{itm.get('delivery_score', 0.0):.2f}",
                "Composite Score (0-10)": f"{itm.get('composite_score', 0.0):.2f}",
                "Quadrant": itm.get("quadrant", ""),
                "Recommendation": itm.get("recommendation", "")
            })


def main():
    parser = argparse.ArgumentParser(description="Generate 4-Quadrant Investment Matrix Visual and Ranking.")
    parser.add_argument("--input", "-i", required=True, help="Path to input JSON or CSV scoring ledger")
    parser.add_argument("--framework", "-f", help="Optional path to custom investment-scoring-framework.json")
    parser.add_argument(
        "--format",
        choices=["html", "markdown", "csv"],
        default="html",
        help="Output format (html, markdown, csv)"
    )
    parser.add_argument("--output", "-o", help="Output file path (default stdout)")

    args = parser.parse_args()

    # Load framework if provided
    framework = DEFAULT_FRAMEWORK
    if args.framework and os.path.exists(args.framework):
        with open(args.framework, "r", encoding="utf-8") as f:
            cfg = json.load(f)
            # Merge
            if "overall_weights" in cfg:
                framework["overall_weights"] = cfg["overall_weights"]
            if "axes" in cfg:
                if "value" in cfg["axes"]:
                    framework["value_weights"] = {c["id"]: c["default_weight"] for c in cfg["axes"]["value"]["categories"]}
                if "delivery" in cfg["axes"]:
                    framework["delivery_weights"] = {c["id"]: c["default_weight"] for c in cfg["axes"]["delivery"]["categories"]}

    raw_items = load_data(args.input)
    scored_items = calculate_scores(raw_items, framework)

    if args.format == "html":
        result = render_html(scored_items, framework)
    elif args.format == "markdown":
        result = render_markdown(scored_items, framework)
    elif args.format == "csv":
        if not args.output:
            print("Error: --output path required for csv export", file=sys.stderr)
            sys.exit(1)
        export_csv(scored_items, args.output)
        print(f"Exported CSV to: {args.output}")
        return
    else:
        result = render_html(scored_items, framework)

    if args.output:
        os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"Generated {args.format} portfolio report at: {args.output}")
    else:
        print(result)


if __name__ == "__main__":
    main()
