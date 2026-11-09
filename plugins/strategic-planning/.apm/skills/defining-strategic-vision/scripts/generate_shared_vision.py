#!/usr/bin/env python3
"""Generate Shared Vision Model Canvas in Markdown, B.C. Gov HTML, or Mermaid formats.

Usage:
    python generate_shared_vision.py --preset cats --format html --output vision.html
    python generate_shared_vision.py --preset cats --format markdown --output vision.md
    python generate_shared_vision.py --preset cats --format mermaid --output vision_diagram.md
    python generate_shared_vision.py --input my_data.json --format markdown
"""

import argparse
import html
import json
import os
import sys

CATS_PRESET = {
    "title": "Court Administration Transformation Initiative Vision",
    "audiences": [
        {
            "group": "The 4.3m citizens of BC inclusive of direct justice clients such as complainants, victims, witnesses, litigants, legal counsel, accused persons, prisoners, offenders, parolees and justice stakeholders.",
            "needs": "Access to justice in a way that is both timely and engenders confidence in the justice system through the provision of effective, fair, and efficient justice services."
        },
        {
            "group": "Frontline public-safety and justice service providers and managers:\n• Law enforcement\n• Crown counsel\n• Defence Bar\n• Civil Litigators\n• Court Administration staff",
            "needs": "Enabling systems that take advantage of new technologies in order to:\n• Effect enhanced business processes;\n• Acquire necessary information and documents without delay;\n• Maximize the effective use of available court resources;\n• Reduce process error; and,\n• Make better informed decisions that lead to better justice."
        },
        {
            "group": "The Judiciary:\n• Provincial Court Judges\n• Supreme Court Justices\n• Appeal Court Justices\n• Other Judicial Officers (e.g. Judicial Justices, Court Services Justices of the Peace)",
            "needs": "A more effective way to:\n• Manage and schedule judicial resources more efficiently and to greatest effect;\n• Access documents, administrative information and legal references in order to make more timely and better informed decisions; and,\n• Monitor and manage system performance through the use of operational business intelligence and reporting tools."
        }
    ],
    "characteristics": "The development and implementation of a series of applications that leverage previous and current investments to create an ecosystem of interconnected business systems and processes.",
    "outputs": [
        "Court Clerk Desktop (CCD) - Integrate the civil and criminal case tracking systems with the electronic court record",
        "Provincial Court Scheduling Project (PCSP) - Supports the new integrated scheduling model",
        "Judicial Desktop - Enable the judiciary to work electronically to access court files, rotas, schedules, exhibits, etc.",
        "Court Services Scheduling - Development of an application to support scheduling of Court Services Branch in-court resources based on availability",
        "Crown Scheduling - Application to support Crown file ownership by identifying Crown availability when scheduling",
        "Scheduling - External facing web application to provide private counsel and self-represented litigants ability to perform remote scheduling",
        "In-court Exhibit Management and Evidence Presentation - Application for the consistent and efficient management of physical and electronic exhibits and electronic evidence presented",
        "Courts Fees and Fines Accounting System - Replacement of legacy application with a system that is fully integrated with all components of the Justice Suite",
        "Superior Courts Management Information System to support strategic planning, analytics, and performance measurement"
    ],
    "outcomes": {
        "increases": [
            "the seamless transfer of electronic information and data between justice system participants, managers and partners",
            "the means by which to monitor, measure and refine system performance based on evidence acquired through operational business intelligence tools",
            "the ability to provide the same, real-time information to all justice system administrators and participants as appropriate to enable faster and better decisions",
            "allowing for performance reporting to create system transparency and identify opportunities to enhance efficiencies",
            "connected business process and document flow between independent justice system participants",
            "new services channels for citizens and increase access to more timely justice",
            "fine and fee recoveries"
        ],
        "decreases": [
            "the number of court appearances, through the support of the transformation of court processes and practices to enable fewer, more meaningful court appearances"
        ]
    },
    "sector_outcomes": "Ministry of Justice: Balanced, accessible and efficient processes and services",
    "corporate_outcomes": "Government Priorities: Improving Access and Outcomes to Justice",
    "current_state": "The disparate and compartmentalized system where efficiencies gained in one business area are lost as information transfers to another part of the system, leading to delays, errors and the inefficient use of justice resources.",
    "future_state": "Support government's commitment to a transparent, timely and balanced justice system as articulated in the October 2012 White Paper on Justice Reform by supporting the elements of reform, which includes: a performance focus; efficient case management practices; integrated approaches; programs based on what works; and citizen-focused services."
}


def render_markdown(data: dict) -> str:
    """Render Shared Vision Model as GitHub Flavored Markdown."""
    lines = []
    title = data.get("title", "Shared Vision Model")
    lines.append(f"# {title}\n")
    lines.append("| Strategic Dimension | Audience & Solution Scope | Alignment Focus & Operational Impact |")
    lines.append("|---|---|---|")

    # For (Target Groups)
    audiences = data.get("audiences", [])
    groups_md = "<br/><br/>".join(
        [html.escape(a.get("group", "")).replace("\n", "<br/>") for a in audiences]
    )
    needs_md = "<br/><br/>".join(
        [html.escape(a.get("needs", "")).replace("\n", "<br/>") for a in audiences]
    )

    lines.append(f"| **For (Target Groups)** | {groups_md} | Target beneficiary and operational user tiers |")
    lines.append(f"| **Who Have These Needs** | {needs_md} | Operational and public access needs |")

    # Characteristics / Program
    char = html.escape(data.get("characteristics", "")).replace("\n", "<br/>")
    lines.append(f"| **This (Program Identity)** | {char} | Modernization program vehicle |")

    # Outputs
    outputs = data.get("outputs", [])
    outputs_md = "<br/>".join([f"• {html.escape(o)}" for o in outputs])
    lines.append(f"| **Through (Project Outputs)** | {outputs_md} | Controllable project application outputs |")

    # Outcomes
    outcomes = data.get("outcomes", {})
    inc_list = outcomes.get("increases", [])
    dec_list = outcomes.get("decreases", [])
    inc_md = "<br/>".join([f"• {html.escape(i)}" for i in inc_list])
    dec_md = "<br/>".join([f"• {html.escape(d)}" for d in dec_list])
    outcomes_md = f"**Measurable Increases in**:<br/>{inc_md}<br/><br/>**Measurable Decreases in**:<br/>{dec_md}"
    lines.append(f"| **Will Enable (Investment Outcomes)** | {outcomes_md} | Measurable business and citizen outcomes |")

    # Sector Outcomes
    sector = html.escape(data.get("sector_outcomes", "")).replace("\n", "<br/>")
    lines.append(f"| **Which Support (Sector Outcomes)** | {sector} | Ministry service plan goals and objectives |")

    # Corporate Outcomes
    corp = html.escape(data.get("corporate_outcomes", "")).replace("\n", "<br/>")
    lines.append(f"| **In Alignment With (Corporate Outcomes)** | {corp} | Provincial government priorities |")

    # Unlike
    current = html.escape(data.get("current_state", "")).replace("\n", "<br/>")
    lines.append(f"| **Unlike (Current State AS-IS)** | {current} | Baseline compartmentalization and friction |")

    # So to be
    future = html.escape(data.get("future_state", "")).replace("\n", "<br/>")
    lines.append(f"| **So As To Be (Future State TO-BE)** | {future} | Target state operating model |")

    # Synthesize audience phrase
    first_grp = data.get('audiences', [{}])[0].get('group', 'our target audiences')
    audience_summary = first_grp.split("\n")[0]
    if len(audiences) > 1:
        audience_summary += f", frontline practitioners, and governance bodies"

    lines.append("\n---\n")
    lines.append("## Synthesized Vision Pitch\n")
    lines.append(f"> **For** {audience_summary},  ")
    lines.append(f"> **Who need** timely, accessible, and trusted justice,  ")
    lines.append(f"> **The** {title}  ")
    lines.append(f"> **Is an** initiative that creates an ecosystem of interconnected business systems  ")
    lines.append(f"> **Through** integrated desktops, modern scheduling, and digital exhibits,  ")
    lines.append(f"> **Will enable** seamless data exchange and fewer, more meaningful court appearances,  ")
    lines.append(f"> **Which supports** {data.get('sector_outcomes', '')}  ")
    lines.append(f"> **In alignment with** {data.get('corporate_outcomes', '')}.  ")
    lines.append(f"> **Unlike** {data.get('current_state', '')}  ")
    lines.append(f"> **Our future state will** {data.get('future_state', '')}\n")

    return "\n".join(lines)


def render_html(data: dict) -> str:
    """Render Shared Vision Model in B.C. Gov Design System table card styling."""
    title = html.escape(data.get("title", "Shared Vision Model"))
    audiences = data.get("audiences", [])
    outputs = data.get("outputs", [])
    outcomes = data.get("outcomes", {})
    inc_list = outcomes.get("increases", [])
    dec_list = outcomes.get("decreases", [])

    rows_html = []

    # Audiences & Needs
    for i, a in enumerate(audiences):
        lbl = "For:" if i == 0 else ""
        need_lbl = "Who Need:" if i == 0 else ""
        grp = html.escape(a.get("group", "")).replace("\n", "<br/>")
        nd = html.escape(a.get("needs", "")).replace("\n", "<br/>")
        annot = "=Target group needs" if i == 0 else ""
        rows_html.append(f"""
        <tr>
            <th class="label-col">{lbl}</th>
            <td class="content-col">{grp}</td>
            <th class="label-col">{need_lbl}</th>
            <td class="content-col">{nd}</td>
            <th class="meta-col">{annot}</th>
        </tr>
        """)

    # This (Characteristics)
    char = html.escape(data.get("characteristics", "")).replace("\n", "<br/>")
    rows_html.append(f"""
    <tr>
        <th class="label-col">This:</th>
        <td class="content-col" colspan="3">{char}</td>
        <th class="meta-col">=Program/Project/Process</th>
    </tr>
    """)

    # Through (Outputs)
    outputs_items = "".join([f"<li>{html.escape(o)}</li>" for o in outputs])
    rows_html.append(f"""
    <tr>
        <th class="label-col">Through:</th>
        <td class="content-col" colspan="3"><ul class="output-list">{outputs_items}</ul></td>
        <th class="meta-col">=Activities/Outputs</th>
    </tr>
    """)

    # Will Enable (Outcomes)
    inc_items = "".join([f"<li>{html.escape(x)}</li>" for x in inc_list])
    dec_items = "".join([f"<li>{html.escape(x)}</li>" for x in dec_list])
    rows_html.append(f"""
    <tr>
        <th class="label-col" rowspan="3">Will enable:</th>
        <td class="content-col" colspan="3">
            <strong>Measurable Increases in:</strong>
            <ul class="outcome-list">{inc_items}</ul>
            <strong>Measurable Decreases in:</strong>
            <ul class="outcome-list">{dec_items}</ul>
        </td>
        <th class="meta-col">Immediate Objectives</th>
    </tr>
    <tr>
        <td class="content-col" colspan="3"><strong>Which support sector outcomes:</strong><br/>{html.escape(data.get('sector_outcomes', ''))}</td>
        <th class="meta-col">Intermediate Objectives</th>
    </tr>
    <tr>
        <td class="content-col" colspan="3"><strong>In alignment with corporate outcomes:</strong><br/>{html.escape(data.get('corporate_outcomes', ''))}</td>
        <th class="meta-col">Ultimate Objectives</th>
    </tr>
    """)

    # So as to be / Unlike
    rows_html.append(f"""
    <tr>
        <th class="label-col">So as to be:</th>
        <td class="content-col" colspan="3">{html.escape(data.get('future_state', '')).replace(chr(10), '<br/>')}</td>
        <th class="meta-col">=TO-BE</th>
    </tr>
    <tr>
        <th class="label-col">Unlike:</th>
        <td class="content-col" colspan="3">{html.escape(data.get('current_state', '')).replace(chr(10), '<br/>')}</td>
        <th class="meta-col">=AS-IS</th>
    </tr>
    """)

    table_body = "\n".join(rows_html)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        :root {{
            --bc-navy: #1E3A8A;
            --bc-blue-dark: #1F4468;
            --bc-blue-mid: #2B6EA6;
            --bc-blue-light: #EBF3FA;
            --bc-border: #93C5FD;
            --bc-text: #1F2937;
            --bc-white: #FFFFFF;
        }}
        body {{
            font-family: 'BC Sans', 'Noto Sans', Calibri, sans-serif;
            color: var(--bc-text);
            background-color: #F8FAFC;
            padding: 24px;
            margin: 0;
            line-height: 1.5;
        }}
        .header {{
            margin-bottom: 20px;
        }}
        h1 {{
            color: #9D174D;
            font-size: 24px;
            margin: 0 0 8px 0;
            font-weight: 700;
        }}
        .lead {{
            color: #4B5563;
            font-size: 14px;
            margin: 0 0 16px 0;
        }}
        .canvas-table {{
            width: 100%;
            border-collapse: collapse;
            background-color: var(--bc-white);
            border: 2px solid var(--bc-navy);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }}
        .canvas-title-row th {{
            background-color: var(--bc-navy);
            color: var(--bc-white);
            font-size: 16px;
            font-weight: 600;
            text-align: center;
            padding: 12px;
            border: 1px solid var(--bc-navy);
        }}
        .label-col {{
            background-color: var(--bc-navy);
            color: var(--bc-white);
            font-weight: 600;
            font-size: 13px;
            text-align: left;
            vertical-align: top;
            padding: 12px 14px;
            width: 12%;
            border: 1px solid #3B82F6;
        }}
        .content-col {{
            background-color: var(--bc-blue-light);
            color: var(--bc-text);
            font-size: 13px;
            vertical-align: top;
            padding: 12px 14px;
            border: 1px solid var(--bc-white);
        }}
        .meta-col {{
            background-color: var(--bc-navy);
            color: var(--bc-white);
            font-weight: 500;
            font-size: 12px;
            text-align: left;
            vertical-align: middle;
            padding: 10px 12px;
            width: 15%;
            border: 1px solid #3B82F6;
        }}
        ul {{
            margin: 6px 0;
            padding-left: 20px;
        }}
        li {{
            margin-bottom: 4px;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{title}</h1>
        <p class="lead">The Shared Vision Model is a way to communicate the vision for a project or program looking at it through the lens of specific needs and how activities will produce outputs to achieve those needs.</p>
    </div>
    <table class="canvas-table">
        <tr class="canvas-title-row">
            <th colspan="5">Shared Vision Model</th>
        </tr>
        {table_body}
    </table>
</body>
</html>
"""


def render_mermaid(data: dict) -> str:
    """Render Shared Vision Model as a structured Mermaid flowchart."""
    title = data.get("title", "Shared Vision Model")
    outputs = data.get("outputs", [])
    sector = data.get("sector_outcomes", "Ministry Service Plan Goals")
    corp = data.get("corporate_outcomes", "Government Priorities")

    # Use directive to prevent clipping
    lines = [
        "%%{init: {\"flowchart\": {\"wrappingWidth\": 460, \"minNodeWidth\": 360}} }%%",
        "flowchart TD",
        "    classDef group fill:#1E3A8A,stroke:#1E3A8A,color:#FFFFFF,stroke-width:2px,font-weight:bold;",
        "    classDef output fill:#EBF3FA,stroke:#2B6EA6,color:#1F2937,stroke-width:2px;",
        "    classDef outcome fill:#FEF3C7,stroke:#D97706,color:#1F2937,stroke-width:2px;",
        "    classDef strategy fill:#DCFCE7,stroke:#16A34A,color:#1F2937,stroke-width:2px,font-weight:bold;",
        "",
        "    subgraph TargetAudiences[\"1. Target Audiences & Needs\"]",
        "        A1[\"B.C. Citizens & Justice Clients<br/>Need: Timely, fair, trusted justice\"]:::group",
        "        A2[\"Frontline Providers & Managers<br/>Need: Modern systems, zero delay, error reduction\"]:::group",
        "        A3[\"The Judiciary<br/>Need: Coordinated scheduling, BI, electronic records\"]:::group",
        "    end",
        "",
        "    subgraph CoreOutputs[\"2. Program Deliverables & Applications\"]",
        f"        O1[\"1. Court Clerk Desktop (CCD)<br/>2. Provincial Court Scheduling (PCSP)<br/>3. Judicial Desktop\"]:::output",
        f"        O2[\"4. Court Services Scheduling<br/>5. Crown Scheduling<br/>6. External Scheduling\"]:::output",
        f"        O3[\"7. Digital Exhibits & Evidence<br/>8. Modern Fees & Fines Accounting<br/>9. Superior Courts MIS\"]:::output",
        "    end",
        "",
        "    subgraph Outcomes[\"3. Investment Outcomes\"]",
        "        OC1[\"Measurable Increases:<br/>• Seamless electronic information transfer<br/>• Real-time BI for decision making<br/>• Expanded digital public service channels\"]:::outcome",
        "        OC2[\"Measurable Decreases:<br/>• Fewer, more meaningful court appearances<br/>• Reduced administrative delay and rework\"]:::outcome",
        "    end",
        "",
        "    subgraph Alignment[\"4. Strategic Mandate Alignment\"]",
        f"        M1[\"Sector Outcome:<br/>{sector}\"]:::strategy",
        f"        M2[\"Corporate Priority:<br/>{corp}\"]:::strategy",
        "    end",
        "",
        "    TargetAudiences --> CoreOutputs",
        "    CoreOutputs --> Outcomes",
        "    Outcomes --> Alignment"
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate Shared Vision Model Canvas.")
    parser.add_argument("--preset", choices=["cats"], help="Use built-in preset (cats)")
    parser.add_argument("--input", "-i", help="Path to input JSON file")
    parser.add_argument(
        "--format", "-f",
        choices=["markdown", "html", "mermaid"],
        default="markdown",
        help="Output format (markdown, html, mermaid)"
    )
    parser.add_argument("--output", "-o", help="Output file path (default stdout)")

    args = parser.parse_args()

    if args.preset == "cats":
        data = CATS_PRESET
    elif args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        # Default to CATS preset if nothing provided
        data = CATS_PRESET

    if args.format == "markdown":
        result = render_markdown(data)
    elif args.format == "html":
        result = render_html(data)
    elif args.format == "mermaid":
        result = render_mermaid(data)
    else:
        result = render_markdown(data)

    if args.output:
        os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"Generated {args.format} shared vision model at: {args.output}")
    else:
        print(result)


if __name__ == "__main__":
    main()
