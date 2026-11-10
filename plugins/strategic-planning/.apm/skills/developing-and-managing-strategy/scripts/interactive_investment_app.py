#!/usr/bin/env python3
"""Interactive B.C. Government Investment Prioritization Web Application.

A lightweight, zero-dependency interactive dashboard for scoring, weighting,
filtering, and visualizing candidate investments on a dynamic 4-quadrant chart.

Usage:
    python interactive_investment_app.py --input strategy/court-investment-scoring-ledger.json
    python interactive_investment_app.py --input strategy/court-investment-scoring-ledger.csv --port 8080
"""

import argparse
import csv
import http.server
import json
import os
import socketserver
import sys
import urllib.parse
import webbrowser

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


LEDGER_FIELDS = [
    "ID", "Name", "Sponsor", "Lead Division",
    "Drivers (25%)", "Alignment (25%)", "Outcomes (25%)", "Sector Benefits (25%)",
    "Value Score (0-10)", "Readiness (20%)", "Research (20%)", "Cost Affordability (20%)",
    "Exec Support (20%)", "Ease of Implementation (20%)", "Delivery Score (0-10)",
    "Composite Score (0-10)", "Quadrant", "Recommendation", "Related Idea ID", "State",
    "Owner", "Sponsor Approval Date", "Capacity Confirmed", "Capacity Source",
    "Commitment Status", "Recommended Action", "Scored On", "Scored By", "Score History (JSON)"
]


def ledger_row(itm: dict) -> dict:
    """Return one lossless ledger CSV row (raw criteria, computed scores, lifecycle fields, history)."""
    sc = itm.get("scores", {})
    return {
        "ID": itm.get("id", ""),
        "Name": itm.get("name", ""),
        "Sponsor": itm.get("sponsor", ""),
        "Lead Division": itm.get("lead_division", ""),
        "Drivers (25%)": sc.get("drivers", 0.0),
        "Alignment (25%)": sc.get("alignment", 0.0),
        "Outcomes (25%)": sc.get("outcomes_and_benefits", 0.0),
        "Sector Benefits (25%)": sc.get("sector_benefits", 0.0),
        "Value Score (0-10)": f"{itm.get('value_score', 0.0):.2f}",
        "Readiness (20%)": sc.get("readiness", 0.0),
        "Research (20%)": sc.get("extent_of_research", 0.0),
        "Cost Affordability (20%)": sc.get("investment_cost", 0.0),
        "Exec Support (20%)": sc.get("executive_support", 0.0),
        "Ease of Implementation (20%)": sc.get("ease_of_implementation", 0.0),
        "Delivery Score (0-10)": f"{itm.get('delivery_score', 0.0):.2f}",
        "Composite Score (0-10)": f"{itm.get('composite_score', 0.0):.2f}",
        "Quadrant": itm.get("quadrant", ""),
        "Recommendation": itm.get("recommendation", ""),
        "Related Idea ID": itm.get("related_idea_id", ""),
        "State": itm.get("state", ""),
        "Owner": itm.get("owner", ""),
        "Sponsor Approval Date": itm.get("approval_date", ""),
        "Capacity Confirmed": itm.get("capacity_confirmed", ""),
        "Capacity Source": itm.get("capacity_source", ""),
        "Commitment Status": itm.get("commitment_status", ""),
        "Recommended Action": itm.get("recommended_action", ""),
        "Scored On": itm.get("scored_on", ""),
        "Scored By": itm.get("scored_by", ""),
        "Score History (JSON)": json.dumps(itm.get("score_history", []), ensure_ascii=False),
    }


def _num(value) -> float:
    """Parse a score cell; blank or invalid cells become 0.0 instead of crashing."""
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def _history(value) -> list:
    """Parse the Score History (JSON) cell."""
    try:
        parsed = json.loads(value) if value else []
        return parsed if isinstance(parsed, list) else []
    except (TypeError, ValueError):
        return []


def load_dataset(file_path: str) -> list:
    """Load items from JSON or CSV."""
    if not os.path.exists(file_path):
        return []

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
                        "drivers": _num(row.get("Drivers (25%)", row.get("drivers", 0.0))),
                        "alignment": _num(row.get("Alignment (25%)", row.get("alignment", 0.0))),
                        "outcomes_and_benefits": _num(row.get("Outcomes (25%)", row.get("outcomes_and_benefits", 0.0))),
                        "sector_benefits": _num(row.get("Sector Benefits (25%)", row.get("sector_benefits", 0.0))),
                        "readiness": _num(row.get("Readiness (20%)", row.get("readiness", 0.0))),
                        "extent_of_research": _num(row.get("Research (20%)", row.get("extent_of_research", 0.0))),
                        "investment_cost": _num(row.get("Cost Affordability (20%)", row.get("investment_cost", 0.0))),
                        "executive_support": _num(row.get("Exec Support (20%)", row.get("executive_support", 0.0))),
                        "ease_of_implementation": _num(row.get("Ease of Implementation (20%)", row.get("ease_of_implementation", 0.0)))
                    },
                    "recommendation": row.get("Recommendation", ""),
                    "related_idea_id": row.get("Related Idea ID", ""),
                    "state": row.get("State", ""),
                    "owner": row.get("Owner", ""),
                    "approval_date": row.get("Sponsor Approval Date", ""),
                    "capacity_confirmed": row.get("Capacity Confirmed", ""),
                    "capacity_source": row.get("Capacity Source", ""),
                    "scored_on": row.get("Scored On", ""),
                    "scored_by": row.get("Scored By", ""),
                    "score_history": _history(row.get("Score History (JSON)", ""))
                }
                items.append(item)
        return items
    return []


def framework_path(file_path: str) -> str:
    """Companion file that stores the scoring weights next to the ledger."""
    return file_path.rsplit(".", 1)[0] + ".framework.json"


def load_framework(file_path: str) -> dict:
    """Load saved scoring weights if present, else the defaults. An invalid file raises ValueError."""
    fw = json.loads(json.dumps(DEFAULT_FRAMEWORK))
    path = framework_path(file_path)
    if not os.path.exists(path):
        return fw
    try:
        with open(path, "r", encoding="utf-8") as f:
            saved = json.load(f)
    except (OSError, ValueError) as exc:
        raise ValueError(f"cannot read scoring weights from {path}: {exc}")
    if not isinstance(saved, dict):
        raise ValueError(f"{path} must contain a JSON object")
    for key in ("overall_weights", "value_weights", "delivery_weights"):
        if key in saved:
            if not isinstance(saved[key], dict):
                raise ValueError(f"{path}: '{key}' must be an object")
            fw[key].update(saved[key])
    for key in ("threshold_x", "threshold_y", "version"):
        if key in saved:
            fw[key] = saved[key]
    return fw


def save_dataset(file_path: str, items: list, framework: dict):
    """Save items to JSON, a lossless companion CSV, and the scoring weights."""
    json_path = file_path if file_path.endswith(".json") else file_path.rsplit(".", 1)[0] + ".json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)

    csv_path = file_path if file_path.endswith(".csv") else file_path.rsplit(".", 1)[0] + ".csv"
    with open(csv_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=LEDGER_FIELDS)
        writer.writeheader()
        for itm in items:
            writer.writerow(ledger_row(itm))

    with open(framework_path(file_path), "w", encoding="utf-8") as f:
        json.dump(framework, f, indent=2)


HTML_DASHBOARD = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>B.C. Gov Investment Prioritization Workbench</title>
    <style>
        :root {
            --bc-navy: #1E3A8A;
            --bc-navy-dark: #172554;
            --bc-blue: #2563EB;
            --bc-blue-light: #EFF6FF;
            --bc-surface: #F8FAFC;
            --bc-card: #FFFFFF;
            --bc-text: #1F2937;
            --bc-muted: #64748B;
            --bc-border: #E2E8F0;
        }
        * { box-sizing: border-box; }
        body {
            font-family: 'BC Sans', 'Noto Sans', Calibri, sans-serif;
            color: var(--bc-text);
            background-color: var(--bc-surface);
            margin: 0;
            padding: 20px;
            line-height: 1.5;
        }
        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: var(--bc-navy);
            color: #FFFFFF;
            padding: 16px 24px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        }
        header h1 {
            margin: 0;
            font-size: 22px;
            font-weight: 700;
        }
        header p {
            margin: 4px 0 0 0;
            font-size: 13px;
            color: #BFDBFE;
        }
        .header-actions {
            display: flex;
            gap: 12px;
        }
        button {
            cursor: pointer;
            border: none;
            border-radius: 6px;
            padding: 8px 16px;
            font-size: 13px;
            font-weight: 600;
            transition: all 0.2s;
        }
        .btn-primary { background: #3B82F6; color: #FFFFFF; }
        .btn-primary:hover { background: #2563EB; }
        .btn-success { background: #10B981; color: #FFFFFF; }
        .btn-success:hover { background: #059669; }
        .btn-outline { background: #FFFFFF; color: var(--bc-navy); border: 1px solid var(--bc-border); }
        .btn-outline:hover { background: #F1F5F9; }

        .layout-grid {
            display: grid;
            grid-template-columns: 340px 1fr;
            gap: 20px;
        }
        @media (max-width: 1024px) {
            .layout-grid { grid-template-columns: 1fr; }
        }
        .panel {
            background: var(--bc-card);
            border: 1px solid var(--bc-border);
            border-radius: 8px;
            padding: 18px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.04);
            margin-bottom: 20px;
        }
        .panel-title {
            font-size: 15px;
            font-weight: 700;
            color: var(--bc-navy);
            margin: 0 0 14px 0;
            border-bottom: 2px solid var(--bc-blue-light);
            padding-bottom: 6px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .control-group {
            margin-bottom: 14px;
        }
        label {
            display: block;
            font-size: 12px;
            font-weight: 600;
            color: #334155;
            margin-bottom: 4px;
        }
        .slider-row {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        input[type="range"] {
            flex: 1;
            accent-color: var(--bc-blue);
        }
        .slider-val {
            font-size: 12px;
            font-weight: 700;
            color: var(--bc-navy);
            width: 42px;
            text-align: right;
        }
        .filter-chip-group {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-bottom: 12px;
        }
        .chip {
            padding: 4px 10px;
            border-radius: 14px;
            font-size: 11px;
            font-weight: 600;
            cursor: pointer;
            border: 1px solid var(--bc-border);
            background: #F1F5F9;
            color: #475569;
            user-select: none;
        }
        .chip.active {
            background: var(--bc-navy);
            color: #FFFFFF;
            border-color: var(--bc-navy);
        }
        input[type="text"] {
            width: 100%;
            padding: 8px 12px;
            border: 1px solid var(--bc-border);
            border-radius: 6px;
            font-size: 13px;
        }

        .chart-box {
            background: #FFFFFF;
            border: 1px solid var(--bc-border);
            border-radius: 8px;
            padding: 16px;
            display: flex;
            justify-content: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.04);
            margin-bottom: 20px;
        }
        svg { overflow: visible; }
        .point-label {
            paint-order: stroke;
            stroke: #FFFFFF;
            stroke-width: 3px;
            cursor: pointer;
        }
        .chart-point { cursor: pointer; transition: transform 0.2s; }
        .chart-point:hover circle { stroke: #000000; stroke-width: 3px; }

        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 13px;
        }
        th {
            background: var(--bc-navy);
            color: #FFFFFF;
            text-align: left;
            padding: 10px 12px;
            font-weight: 600;
        }
        td {
            padding: 10px 12px;
            border-bottom: 1px solid var(--bc-border);
        }
        tr:hover td { background: #F8FAFC; }
        .badge {
            display: inline-block;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 600;
        }
        .badge-q1 { background: #DCFCE7; color: #166534; }
        .badge-q2 { background: #F3E8FF; color: #6B21A8; }
        .badge-q3 { background: #E0F2FE; color: #0369A1; }
        .badge-q4 { background: #FEE2E2; color: #991B1B; }

        /* Modal styling */
        .modal-overlay {
            display: none;
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(0,0,0,0.5);
            z-index: 1000;
            justify-content: center;
            align-items: center;
        }
        .modal {
            background: #FFFFFF;
            border-radius: 8px;
            width: 580px;
            max-width: 90%;
            max-height: 90vh;
            overflow-y: auto;
            padding: 24px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        }
        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 2px solid var(--bc-blue-light);
            padding-bottom: 12px;
            margin-bottom: 16px;
        }
        .modal-header h3 { margin: 0; color: var(--bc-navy); }
        .grid-2col {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 14px;
        }
        .save-alert {
            display: none;
            background: #DCFCE7;
            color: #166534;
            padding: 8px 14px;
            border-radius: 6px;
            font-size: 13px;
            font-weight: 600;
            margin-left: 12px;
        }
    </style>
</head>
<body>
    <header>
        <div>
            <h1>Investment Prioritization Workbench</h1>
            <p>Interactive 4-Quadrant Scoring, Dynamic Weighting & Portfolio Alignment</p>
        </div>
        <div class="header-actions">
            <span id="saveAlert" class="save-alert">✓ Saved to ledger!</span>
            <button class="btn-primary" onclick="openOnboardModal()">+ Onboard New Proposal</button>
            <button class="btn-success" onclick="saveToDisk()">Save Ledger to Disk</button>
        </div>
    </header>

    <div class="layout-grid">
        <!-- Controls Column -->
        <div>
            <div class="panel">
                <div class="panel-title">Search & Filters</div>
                <div class="control-group">
                    <label>Search Proposal or Sponsor</label>
                    <input type="text" id="searchInput" placeholder="Type keyword..." oninput="applyFilters()">
                </div>
                <div class="control-group">
                    <label>Quadrant Filter</label>
                    <div class="filter-chip-group">
                        <div class="chip active" data-q="all" onclick="toggleQuadFilter('all')">All (5)</div>
                        <div class="chip active" data-q="Q1" onclick="toggleQuadFilter('Q1')">Q1 Priorities</div>
                        <div class="chip active" data-q="Q2" onclick="toggleQuadFilter('Q2')">Q2 Big Bets</div>
                        <div class="chip active" data-q="Q3" onclick="toggleQuadFilter('Q3')">Q3 Tactical</div>
                        <div class="chip active" data-q="Q4" onclick="toggleQuadFilter('Q4')">Q4 Defer</div>
                    </div>
                </div>
                <div class="control-group">
                    <label>Min Composite Score: <span id="minCompVal">0.0</span></label>
                    <div class="slider-row">
                        <input type="range" id="minCompSlider" min="0" max="10" step="0.5" value="0" oninput="applyFilters()">
                    </div>
                </div>
            </div>

            <div class="panel">
                <div class="panel-title">
                    <span>Axis Weights</span>
                    <button class="btn-outline" style="padding: 2px 8px; font-size: 11px;" onclick="resetWeights()">Reset</button>
                </div>
                <div class="control-group">
                    <label>Overall Axis Split: <span id="axisSplitLabel">50% Value / 50% Delivery</span></label>
                    <div class="slider-row">
                        <input type="range" id="axisSplitSlider" min="10" max="90" step="5" value="50" oninput="updateWeights()">
                    </div>
                </div>
                
                <div class="panel-title" style="font-size: 13px; margin-top: 14px;">Value Categories Weighting</div>
                <div class="control-group">
                    <label>Drivers: <span id="w_drivers_val" class="slider-val">25%</span></label>
                    <div class="slider-row">
                        <input type="range" id="w_drivers" min="0" max="100" step="5" value="25" oninput="updateCategoryWeights()">
                    </div>
                </div>
                <div class="control-group">
                    <label>Strategic Alignment: <span id="w_alignment_val" class="slider-val">25%</span></label>
                    <div class="slider-row">
                        <input type="range" id="w_alignment" min="0" max="100" step="5" value="25" oninput="updateCategoryWeights()">
                    </div>
                </div>
                <div class="control-group">
                    <label>Outcomes & Benefits: <span id="w_outcomes_val" class="slider-val">25%</span></label>
                    <div class="slider-row">
                        <input type="range" id="w_outcomes" min="0" max="100" step="5" value="25" oninput="updateCategoryWeights()">
                    </div>
                </div>
                <div class="control-group">
                    <label>Sector Benefits: <span id="w_sector_val" class="slider-val">25%</span></label>
                    <div class="slider-row">
                        <input type="range" id="w_sector" min="0" max="100" step="5" value="25" oninput="updateCategoryWeights()">
                    </div>
                </div>

                <div class="panel-title" style="font-size: 13px; margin-top: 14px;">Delivery Categories Weighting</div>
                <div class="control-group">
                    <label>Readiness & Capacity: <span id="w_readiness_val" class="slider-val">20%</span></label>
                    <div class="slider-row">
                        <input type="range" id="w_readiness" min="0" max="100" step="5" value="20" oninput="updateCategoryWeights()">
                    </div>
                </div>
                <div class="control-group">
                    <label>Extent of Research: <span id="w_research_val" class="slider-val">20%</span></label>
                    <div class="slider-row">
                        <input type="range" id="w_research" min="0" max="100" step="5" value="20" oninput="updateCategoryWeights()">
                    </div>
                </div>
                <div class="control-group">
                    <label>Cost Affordability: <span id="w_cost_val" class="slider-val">20%</span></label>
                    <div class="slider-row">
                        <input type="range" id="w_cost" min="0" max="100" step="5" value="20" oninput="updateCategoryWeights()">
                    </div>
                </div>
                <div class="control-group">
                    <label>Executive Support: <span id="w_sponsor_val" class="slider-val">20%</span></label>
                    <div class="slider-row">
                        <input type="range" id="w_sponsor" min="0" max="100" step="5" value="20" oninput="updateCategoryWeights()">
                    </div>
                </div>
                <div class="control-group">
                    <label>Ease of Implementation: <span id="w_ease_val" class="slider-val">20%</span></label>
                    <div class="slider-row">
                        <input type="range" id="w_ease" min="0" max="100" step="5" value="20" oninput="updateCategoryWeights()">
                    </div>
                </div>
            </div>
        </div>

        <!-- Chart and Table Column -->
        <div>
            <div class="chart-box">
                <svg id="quadrantSvg" width="760" height="540" viewBox="0 0 760 540">
                    <defs>
                        <filter id="bubbleGlow" x="-20%" y="-20%" width="140%" height="140%">
                            <feDropShadow dx="0" dy="2" stdDeviation="2" flood-color="#000000" flood-opacity="0.3"/>
                        </filter>
                        <linearGradient id="quadGrad" x1="0%" y1="100%" x2="100%" y2="0%">
                            <stop offset="0%" stop-color="#FEE2E2" stop-opacity="0.6"/>
                            <stop offset="50%" stop-color="#FEF3C7" stop-opacity="0.5"/>
                            <stop offset="100%" stop-color="#DCFCE7" stop-opacity="0.65"/>
                        </linearGradient>
                    </defs>
                    <rect id="bgRect" x="65" y="30" width="650" height="450" fill="url(#quadGrad)" stroke="#64748B" stroke-width="2"/>
                    <g id="gridGroup"></g>
                    <g id="labelGroup"></g>
                    <g id="bubbleGroup"></g>
                    <text x="390" y="520" text-anchor="middle" font-size="13" font-weight="bold" fill="#1E3A8A">Ability to Deliver / Readiness (0 – 10)</text>
                    <text x="20" y="255" text-anchor="middle" font-size="13" font-weight="bold" fill="#1E3A8A" transform="rotate(-90, 20, 255)">Value / Return on Investment (0 – 10)</text>
                </svg>
            </div>

            <div class="panel">
                <div class="panel-title">
                    <span>Ranked Investment Proposals (<span id="visibleCount">5</span> displayed)</span>
                </div>
                <table>
                    <thead>
                        <tr>
                            <th style="width: 40px; text-align: center;">Rank</th>
                            <th>ID & Proposal Name</th>
                            <th>Executive Sponsor</th>
                            <th style="text-align: right;">Value</th>
                            <th style="text-align: right;">Delivery</th>
                            <th style="text-align: right;">Composite</th>
                            <th>Quadrant</th>
                            <th>Commitment evidence</th>
                            <th style="text-align: center;">Actions</th>
                        </tr>
                    </thead>
                    <tbody id="tableBody"></tbody>
                </table>
            </div>
        </div>
    </div>

    <!-- Onboard / Edit Modal -->
    <div id="onboardModal" class="modal-overlay">
        <div class="modal">
            <div class="modal-header">
                <h3 id="modalTitle">Onboard New Investment Proposal</h3>
                <button class="btn-outline" onclick="closeModal()">✕</button>
            </div>
            <form id="proposalForm" onsubmit="handleFormSubmit(event)">
                <input type="hidden" id="editItemIndex" value="-1">
                <div class="grid-2col">
                    <div class="control-group">
                        <label>Proposal ID</label>
                        <input type="text" id="propId" placeholder="INV-106" required>
                    </div>
                    <div class="control-group">
                        <label>Proposal Name</label>
                        <input type="text" id="propName" placeholder="e.g. Online Document Portal" required>
                    </div>
                </div>
                <div class="grid-2col">
                    <div class="control-group">
                        <label>Executive Sponsor</label>
                        <input type="text" id="propSponsor" placeholder="e.g. Executive Director CSB">
                    </div>
                    <div class="control-group">
                        <label>Lead Division</label>
                        <input type="text" id="propDivision" placeholder="e.g. Court Digital Services">
                    </div>
                </div>

                <div class="panel-title" style="font-size: 13px; margin-top: 14px;">Lifecycle and commitment evidence</div>
                <div class="grid-2col">
                    <div class="control-group">
                        <label>Related idea ID</label>
                        <input type="text" id="propIdea" placeholder="e.g. IDEA-009">
                    </div>
                    <div class="control-group">
                        <label>State (score only candidate or Planned)</label>
                        <select id="propState">
                            <option value="">Not set</option>
                            <option value="candidate">candidate</option>
                            <option value="Planned">Planned</option>
                            <option value="raw">raw</option>
                            <option value="explored">explored</option>
                            <option value="validated">validated</option>
                        </select>
                    </div>
                </div>
                <div class="grid-2col">
                    <div class="control-group">
                        <label>Delivery owner</label>
                        <input type="text" id="propOwner" placeholder="Named owner">
                    </div>
                    <div class="control-group">
                        <label>Sponsor approval date</label>
                        <input type="date" id="propApproval">
                    </div>
                </div>
                <div class="grid-2col">
                    <div class="control-group">
                        <label><input type="checkbox" id="propCapacity"> Capacity confirmed</label>
                        <input type="text" id="propCapSource" placeholder="Source, e.g. allocation in register 11">
                    </div>
                    <div class="control-group">
                        <label>Scored by</label>
                        <input type="text" id="propScoredBy" placeholder="Your name">
                    </div>
                </div>

                <div class="panel-title" style="font-size: 13px; margin-top: 14px;">Value / ROI Scores (0 to 10)</div>
                <div class="grid-2col">
                    <div class="control-group">
                        <label>Drivers: <span id="f_val_drivers">5.0</span></label>
                        <input type="range" id="f_drivers" min="0" max="10" step="0.5" value="5.0" oninput="updateFormScores()">
                    </div>
                    <div class="control-group">
                        <label>Strategic Alignment: <span id="f_val_alignment">5.0</span></label>
                        <input type="range" id="f_alignment" min="0" max="10" step="0.5" value="5.0" oninput="updateFormScores()">
                    </div>
                </div>
                <div class="grid-2col">
                    <div class="control-group">
                        <label>Outcomes & Benefits: <span id="f_val_outcomes">5.0</span></label>
                        <input type="range" id="f_outcomes" min="0" max="10" step="0.5" value="5.0" oninput="updateFormScores()">
                    </div>
                    <div class="control-group">
                        <label>Sector Benefits: <span id="f_val_sector">5.0</span></label>
                        <input type="range" id="f_sector" min="0" max="10" step="0.5" value="5.0" oninput="updateFormScores()">
                    </div>
                </div>

                <div class="panel-title" style="font-size: 13px; margin-top: 14px;">Ability to Deliver Scores (0 to 10)</div>
                <div class="grid-2col">
                    <div class="control-group">
                        <label>Readiness: <span id="f_val_readiness">5.0</span></label>
                        <input type="range" id="f_readiness" min="0" max="10" step="0.5" value="5.0" oninput="updateFormScores()">
                    </div>
                    <div class="control-group">
                        <label>Extent of Research: <span id="f_val_research">5.0</span></label>
                        <input type="range" id="f_research" min="0" max="10" step="0.5" value="5.0" oninput="updateFormScores()">
                    </div>
                </div>
                <div class="grid-2col">
                    <div class="control-group">
                        <label>Cost Affordability: <span id="f_val_cost">5.0</span></label>
                        <input type="range" id="f_cost" min="0" max="10" step="0.5" value="5.0" oninput="updateFormScores()">
                    </div>
                    <div class="control-group">
                        <label>Executive Support: <span id="f_val_sponsor">5.0</span></label>
                        <input type="range" id="f_sponsor" min="0" max="10" step="0.5" value="5.0" oninput="updateFormScores()">
                    </div>
                </div>
                <div class="control-group">
                    <label>Ease of Implementation: <span id="f_val_ease">5.0</span></label>
                    <input type="range" id="f_ease" min="0" max="10" step="0.5" value="5.0" oninput="updateFormScores()">
                </div>

                <div class="control-group">
                    <label>Recommended Action / Notes</label>
                    <input type="text" id="propRec" placeholder="e.g. Fund in Phase 1">
                </div>

                <div style="display: flex; justify-content: flex-end; gap: 10px; margin-top: 20px;">
                    <button type="button" class="btn-outline" onclick="closeModal()">Cancel</button>
                    <button type="submit" class="btn-primary" id="modalSubmitBtn">Save Proposal</button>
                </div>
            </form>
        </div>
    </div>

    <script>
        let rawData = [];
        let activeFilters = {
            search: '',
            quadrants: new Set(['all', 'Q1', 'Q2', 'Q3', 'Q4']),
            minComposite: 0.0
        };

        const framework = {
            overall_weights: { value_weight: 50.0, delivery_weight: 50.0 },
            value_weights: { drivers: 25.0, alignment: 25.0, outcomes_and_benefits: 25.0, sector_benefits: 25.0 },
            delivery_weights: { readiness: 20.0, extent_of_research: 20.0, investment_cost: 20.0, executive_support: 20.0, ease_of_implementation: 20.0 },
            threshold_x: 5.0,
            threshold_y: 5.0,
            version: 'default'
        };

        let baseline = [];
        let loadedFrameworkStr = '';
        let loadedFrameworkVersion = 'default';
        let loadedWeights = {};

        function esc(v) {
            return String(v === undefined || v === null ? '' : v)
                .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
        }

        function hasValue(v) {
            if (v === undefined || v === null || typeof v === 'boolean' || typeof v === 'object') return false;
            return !['', 'none', 'null', 'n/a', 'na', 'tbd', '-', 'unknown'].includes(String(v).trim().toLowerCase());
        }

        function validDate(v) {
            const text = String(v === undefined || v === null ? '' : v).trim();
            if (!/^\d{4}-\d{2}-\d{2}$/.test(text)) return false;
            const d = new Date(text + 'T00:00:00Z');
            return !isNaN(d.getTime()) && d.toISOString().slice(0, 10) === text;
        }

        function isTrue(v) {
            return v === true || ['true', 'yes', 'y', '1'].includes(String(v === undefined || v === null ? '' : v).trim().toLowerCase());
        }

        function weightsHash(fw) {
            const text = JSON.stringify([fw.overall_weights, fw.value_weights, fw.delivery_weights, fw.threshold_x, fw.threshold_y]);
            let h = 5381;
            for (let i = 0; i < text.length; i++) { h = ((h << 5) + h + text.charCodeAt(i)) | 0; }
            return (h >>> 0).toString(16).padStart(8, '0');
        }

        function applySaveSnapshots(items, base, ctx) {
            items.forEach(item => {
                const b = base.find(x => x.id === item.id);
                if (!b) return;
                const scoresChanged = JSON.stringify(item.scores || {}) !== JSON.stringify(b.scores || {});
                if (!(ctx.fwChanged || scoresChanged)) return;
                const snap = {
                    scored_on: b.scored_on || '', scored_by: b.scored_by || '', framework: ctx.loadedVersion,
                    reason: ctx.fwChanged && scoresChanged ? 'scores and weights changed' : (ctx.fwChanged ? 'scoring weights changed' : 'scores changed'),
                    value_score: b.value_score, delivery_score: b.delivery_score,
                    composite_score: b.composite_score, quadrant: b.quadrant
                };
                if (ctx.fwChanged) snap.weights = ctx.loadedWeights;
                item.score_history = (item.score_history || []).concat([snap]);
                item.scored_on = ctx.today;
            });
        }

        function snapshotBaseline() {
            baseline = rawData.map(i => ({
                id: i.id, scores: JSON.parse(JSON.stringify(i.scores || {})),
                scored_on: i.scored_on || '', scored_by: i.scored_by || '',
                value_score: i.value_score, delivery_score: i.delivery_score,
                composite_score: i.composite_score, quadrant: i.quadrant
            }));
            loadedFrameworkStr = JSON.stringify(framework);
            loadedFrameworkVersion = framework.version || 'default';
            loadedWeights = JSON.parse(JSON.stringify({
                overall_weights: framework.overall_weights, value_weights: framework.value_weights,
                delivery_weights: framework.delivery_weights, threshold_x: framework.threshold_x, threshold_y: framework.threshold_y
            }));
        }

        function applyFramework(fw) {
            Object.assign(framework.overall_weights, fw.overall_weights || {});
            Object.assign(framework.value_weights, fw.value_weights || {});
            Object.assign(framework.delivery_weights, fw.delivery_weights || {});
            if (fw.threshold_x !== undefined) framework.threshold_x = fw.threshold_x;
            if (fw.threshold_y !== undefined) framework.threshold_y = fw.threshold_y;
            if (fw.version) framework.version = fw.version;
            const sliders = {
                w_drivers: framework.value_weights.drivers, w_alignment: framework.value_weights.alignment,
                w_outcomes: framework.value_weights.outcomes_and_benefits, w_sector: framework.value_weights.sector_benefits,
                w_readiness: framework.delivery_weights.readiness, w_research: framework.delivery_weights.extent_of_research,
                w_cost: framework.delivery_weights.investment_cost, w_sponsor: framework.delivery_weights.executive_support,
                w_ease: framework.delivery_weights.ease_of_implementation
            };
            for (const id in sliders) {
                const el = document.getElementById(id);
                if (el) el.value = sliders[id];
            }
            const split = document.getElementById('axisSplitSlider');
            if (split) split.value = framework.overall_weights.value_weight;
            updateWeights();
            updateCategoryWeights();
        }

        const bubbleColors = ["#4338CA", "#6D28D9", "#2563EB", "#0891B2", "#0D9488", "#7C3AED", "#4F46E5"];

        async function init() {
            try {
                const res = await fetch('/api/data');
                const json = await res.json();
                rawData = json.items || [];
                if (json.framework) { applyFramework(json.framework); } else { recalculate(); }
                snapshotBaseline();
            } catch (err) {
                console.error('Failed to load data', err);
            }
        }

        function commitmentStatus(item) {
            const missing = [];
            if (!hasValue(item.sponsor) || !validDate(item.approval_date)) missing.push('sponsor approval date');
            if (!hasValue(item.owner)) missing.push('owner');
            if (!isTrue(item.capacity_confirmed) || !hasValue(item.capacity_source)) missing.push('confirmed capacity with source');
            if (!missing.length) return { status: 'Committable', missing: missing };
            if (missing.length === 1 && missing[0].startsWith('confirmed capacity')) return { status: 'Capacity unconfirmed', missing: missing };
            return { status: 'Evidence incomplete', missing: missing };
        }

        function recommendedAction(item) {
            const note = String(item.recommendation || '').trim();
            const base = { Q1: 'Fund and execute immediately', Q2: 'Fund phased discovery & de-risking', Q3: 'Deliver opportunistically if capacity allows', Q4: 'Defer or decline funding' }[item.qCode] || '';
            if (item.qCode === 'Q1' && item.commitment_status !== 'Committable') {
                return 'Strong candidate. Hold as a decision gate until: ' + (item.commitment_missing || []).join(', ') + (note ? '. Planning note: ' + note : '');
            }
            return note || base;
        }

        function recalculate() {
            const vWts = framework.value_weights;
            const dWts = framework.delivery_weights;
            const vSum = Object.values(vWts).reduce((a, b) => a + b, 0) || 100;
            const dSum = Object.values(dWts).reduce((a, b) => a + b, 0) || 100;

            const wVal = framework.overall_weights.value_weight;
            const wDel = framework.overall_weights.delivery_weight;
            const axisTotal = (wVal + wDel) || 100;

            rawData.forEach(item => {
                const sc = item.scores || {};
                let v = 0;
                for (let k in vWts) { v += (parseFloat(sc[k] || 0) * (vWts[k] / vSum)); }
                let d = 0;
                for (let k in dWts) { d += (parseFloat(sc[k] || 0) * (dWts[k] / dSum)); }

                const cs = commitmentStatus(item);
                item.commitment_status = cs.status;
                item.commitment_missing = cs.missing;

                item.value_score = Math.round(v * 100) / 100;
                item.delivery_score = Math.round(d * 100) / 100;
                item.composite_score = Math.round(((v * (wVal / axisTotal)) + (d * (wDel / axisTotal))) * 100) / 100;

                if (item.value_score >= framework.threshold_y && item.delivery_score >= framework.threshold_x) {
                    item.quadrant = 'Strategic Priorities & Quick Wins';
                    item.qCode = 'Q1';
                } else if (item.value_score >= framework.threshold_y && item.delivery_score < framework.threshold_x) {
                    item.quadrant = 'Strategic Big Bets';
                    item.qCode = 'Q2';
                } else if (item.value_score < framework.threshold_y && item.delivery_score >= framework.threshold_x) {
                    item.quadrant = 'Tactical Efficiencies';
                    item.qCode = 'Q3';
                } else {
                    item.quadrant = 'Deprioritize & Defer';
                    item.qCode = 'Q4';
                }
                item.recommended_action = recommendedAction(item);
            });

            rawData.sort((a, b) => b.composite_score - a.composite_score);
            render();
        }

        function render() {
            const search = activeFilters.search.toLowerCase();
            const minC = activeFilters.minComposite;
            const qSet = activeFilters.quadrants;

            const filtered = rawData.filter(item => {
                const matchText = (item.name + ' ' + (item.sponsor||'') + ' ' + item.id).toLowerCase().includes(search);
                const matchQuad = qSet.has('all') || qSet.has(item.qCode);
                const matchComp = item.composite_score >= minC;
                return matchText && matchQuad && matchComp;
            });

            document.getElementById('visibleCount').innerText = filtered.length;
            renderChart(filtered);
            renderTable(filtered);
        }

        function renderChart(items) {
            const pW = 650, pH = 450, mL = 65, mT = 30;
            const gridGroup = document.getElementById('gridGroup');
            const labelGroup = document.getElementById('labelGroup');
            const bubbleGroup = document.getElementById('bubbleGroup');

            gridGroup.innerHTML = '';
            labelGroup.innerHTML = '';
            bubbleGroup.innerHTML = '';

            // Draw grid
            for (let i = 0; i <= 10; i++) {
                const x = mL + (i / 10.0) * pW;
                const y = mT + (1.0 - i / 10.0) * pH;
                const isMid = i === 5;
                const stroke = isMid ? '#94A3B8' : '#E2E8F0';
                const strokeW = isMid ? '2' : '1';
                const dash = isMid ? 'stroke-dasharray="4,4"' : '';

                gridGroup.innerHTML += `<line x1="${x}" y1="${mT}" x2="${x}" y2="${mT+pH}" stroke="${stroke}" stroke-width="${strokeW}" ${dash}/>`;
                gridGroup.innerHTML += `<text x="${x}" y="${mT+pH+18}" text-anchor="middle" font-size="11" fill="#64748B">${i}</text>`;

                gridGroup.innerHTML += `<line x1="${mL}" y1="${y}" x2="${mL+pW}" y2="${y}" stroke="${stroke}" stroke-width="${strokeW}" ${dash}/>`;
                gridGroup.innerHTML += `<text x="${mL-12}" y="${y+4}" text-anchor="end" font-size="11" fill="#64748B">${i}</text>`;
            }

            // Quadrant Background Labels
            labelGroup.innerHTML += `<text x="${mL + 0.25*pW}" y="${mT + 0.22*pH}" text-anchor="middle" font-size="13" font-weight="bold" fill="#6B21A8" opacity="0.75">Strategic Big Bets<tspan x="${mL + 0.25*pW}" dy="16" font-size="11" font-weight="normal">De-risk & Discover</tspan></text>`;
            labelGroup.innerHTML += `<text x="${mL + 0.75*pW}" y="${mT + 0.22*pH}" text-anchor="middle" font-size="13" font-weight="bold" fill="#15803D" opacity="0.75">Strategic Priorities<tspan x="${mL + 0.75*pW}" dy="16" font-size="11" font-weight="normal">Fund & Execute</tspan></text>`;
            labelGroup.innerHTML += `<text x="${mL + 0.25*pW}" y="${mT + 0.75*pH}" text-anchor="middle" font-size="13" font-weight="bold" fill="#991B1B" opacity="0.75">Deprioritize & Defer<tspan x="${mL + 0.25*pW}" dy="16" font-size="11" font-weight="normal">Decline Funding</tspan></text>`;
            labelGroup.innerHTML += `<text x="${mL + 0.75*pW}" y="${mT + 0.75*pH}" text-anchor="middle" font-size="13" font-weight="bold" fill="#0369A1" opacity="0.75">Tactical Efficiencies<tspan x="${mL + 0.75*pW}" dy="16" font-size="11" font-weight="normal">Deliver Opportunistically</tspan></text>`;

            // Draw Bubbles
            items.forEach((item, idx) => {
                const cx = mL + (item.delivery_score / 10.0) * pW;
                const cy = mT + (1.0 - item.value_score / 10.0) * pH;
                const color = bubbleColors[idx % bubbleColors.length];
                const realIdx = rawData.indexOf(item);

                bubbleGroup.innerHTML += `
                    <g class="chart-point" onclick="editItem(${realIdx})">
                        <title>${esc(item.id)}: ${esc(item.name)}&#10;Value: ${item.value_score.toFixed(2)} | Delivery: ${item.delivery_score.toFixed(2)} | Composite: ${item.composite_score.toFixed(2)}&#10;Quadrant: ${esc(item.quadrant)}</title>
                        <circle cx="${cx}" cy="${cy}" r="12" fill="${color}" stroke="#FFFFFF" stroke-width="2" filter="url(#bubbleGlow)" opacity="0.88"/>
                        <circle cx="${cx}" cy="${cy}" r="4" fill="#FFFFFF"/>
                        <text x="${cx + 15}" y="${cy + 4}" font-size="11" font-weight="600" fill="#1E293B" class="point-label">${esc(item.name)}</text>
                    </g>
                `;
            });
        }

        function renderTable(items) {
            const tbody = document.getElementById('tableBody');
            tbody.innerHTML = '';
            items.forEach((item, rank) => {
                const realIdx = rawData.indexOf(item);
                let badgeClass = 'badge-q1';
                if (item.qCode === 'Q2') badgeClass = 'badge-q2';
                if (item.qCode === 'Q3') badgeClass = 'badge-q3';
                if (item.qCode === 'Q4') badgeClass = 'badge-q4';

                tbody.innerHTML += `
                    <tr>
                        <td style="text-align: center; font-weight: bold;">${rank + 1}</td>
                        <td><strong>${esc(item.id)}</strong>: ${esc(item.name)}</td>
                        <td>${esc(item.sponsor || '—')}</td>
                        <td style="text-align: right; font-weight: 600;">${item.value_score.toFixed(2)}</td>
                        <td style="text-align: right; font-weight: 600;">${item.delivery_score.toFixed(2)}</td>
                        <td style="text-align: right; font-weight: bold; color: var(--bc-navy);">${item.composite_score.toFixed(2)}</td>
                        <td><span class="badge ${badgeClass}">${esc(item.quadrant)}</span></td>
                        <td title="${esc((item.commitment_missing || []).join(', '))}">${esc(item.commitment_status || '')}</td>
                        <td style="text-align: center;">
                            <button class="btn-outline" style="padding: 2px 8px; font-size: 11px;" onclick="editItem(${realIdx})">Edit</button>
                        </td>
                    </tr>
                `;
            });
        }

        function applyFilters() {
            activeFilters.search = document.getElementById('searchInput').value;
            activeFilters.minComposite = parseFloat(document.getElementById('minCompSlider').value) || 0.0;
            document.getElementById('minCompVal').innerText = activeFilters.minComposite.toFixed(1);
            render();
        }

        function toggleQuadFilter(q) {
            const chips = document.querySelectorAll('.chip');
            if (q === 'all') {
                activeFilters.quadrants = new Set(['all', 'Q1', 'Q2', 'Q3', 'Q4']);
                chips.forEach(c => c.classList.add('active'));
            } else {
                activeFilters.quadrants.delete('all');
                document.querySelector('[data-q="all"]').classList.remove('active');
                if (activeFilters.quadrants.has(q)) {
                    activeFilters.quadrants.delete(q);
                    document.querySelector(`[data-q="${q}"]`).classList.remove('active');
                } else {
                    activeFilters.quadrants.add(q);
                    document.querySelector(`[data-q="${q}"]`).classList.add('active');
                }
                if (activeFilters.quadrants.size === 0) {
                    activeFilters.quadrants = new Set(['all', 'Q1', 'Q2', 'Q3', 'Q4']);
                    chips.forEach(c => c.classList.add('active'));
                }
            }
            render();
        }

        function updateWeights() {
            const val = parseInt(document.getElementById('axisSplitSlider').value);
            const del = 100 - val;
            framework.overall_weights.value_weight = val;
            framework.overall_weights.delivery_weight = del;
            document.getElementById('axisSplitLabel').innerText = `${val}% Value / ${del}% Delivery`;
            recalculate();
        }

        function updateCategoryWeights() {
            framework.value_weights.drivers = parseFloat(document.getElementById('w_drivers').value);
            framework.value_weights.alignment = parseFloat(document.getElementById('w_alignment').value);
            framework.value_weights.outcomes_and_benefits = parseFloat(document.getElementById('w_outcomes').value);
            framework.value_weights.sector_benefits = parseFloat(document.getElementById('w_sector').value);

            document.getElementById('w_drivers_val').innerText = framework.value_weights.drivers + '%';
            document.getElementById('w_alignment_val').innerText = framework.value_weights.alignment + '%';
            document.getElementById('w_outcomes_val').innerText = framework.value_weights.outcomes_and_benefits + '%';
            document.getElementById('w_sector_val').innerText = framework.value_weights.sector_benefits + '%';

            framework.delivery_weights.readiness = parseFloat(document.getElementById('w_readiness').value);
            framework.delivery_weights.extent_of_research = parseFloat(document.getElementById('w_research').value);
            framework.delivery_weights.investment_cost = parseFloat(document.getElementById('w_cost').value);
            framework.delivery_weights.executive_support = parseFloat(document.getElementById('w_sponsor').value);
            framework.delivery_weights.ease_of_implementation = parseFloat(document.getElementById('w_ease').value);

            document.getElementById('w_readiness_val').innerText = framework.delivery_weights.readiness + '%';
            document.getElementById('w_research_val').innerText = framework.delivery_weights.extent_of_research + '%';
            document.getElementById('w_cost_val').innerText = framework.delivery_weights.investment_cost + '%';
            document.getElementById('w_sponsor_val').innerText = framework.delivery_weights.executive_support + '%';
            document.getElementById('w_ease_val').innerText = framework.delivery_weights.ease_of_implementation + '%';

            recalculate();
        }

        function resetWeights() {
            document.getElementById('axisSplitSlider').value = 50;
            document.getElementById('w_drivers').value = 25;
            document.getElementById('w_alignment').value = 25;
            document.getElementById('w_outcomes').value = 25;
            document.getElementById('w_sector').value = 25;
            document.getElementById('w_readiness').value = 20;
            document.getElementById('w_research').value = 20;
            document.getElementById('w_cost').value = 20;
            document.getElementById('w_sponsor').value = 20;
            document.getElementById('w_ease').value = 20;
            updateWeights();
            updateCategoryWeights();
        }

        function openOnboardModal() {
            document.getElementById('modalTitle').innerText = 'Onboard New Investment Proposal';
            document.getElementById('editItemIndex').value = '-1';
            document.getElementById('propId').value = `INV-${rawData.length + 101}`;
            document.getElementById('propName').value = '';
            document.getElementById('propSponsor').value = '';
            document.getElementById('propDivision').value = '';
            document.getElementById('propRec').value = '';
            document.getElementById('propIdea').value = '';
            document.getElementById('propState').value = '';
            document.getElementById('propOwner').value = '';
            document.getElementById('propApproval').value = '';
            document.getElementById('propCapacity').checked = false;
            document.getElementById('propCapSource').value = '';
            document.getElementById('propScoredBy').value = '';
            ['drivers','alignment','outcomes','sector','readiness','research','cost','sponsor','ease'].forEach(k => {
                document.getElementById(`f_${k}`).value = 5.0;
            });
            updateFormScores();
            document.getElementById('onboardModal').style.display = 'flex';
        }

        function editItem(idx) {
            const itm = rawData[idx];
            if (!itm) return;
            document.getElementById('modalTitle').innerText = `Edit Proposal: ${itm.id}`;
            document.getElementById('editItemIndex').value = idx;
            document.getElementById('propId').value = itm.id;
            document.getElementById('propName').value = itm.name;
            document.getElementById('propSponsor').value = itm.sponsor || '';
            document.getElementById('propDivision').value = itm.lead_division || '';
            document.getElementById('propRec').value = itm.recommendation || '';
            document.getElementById('propIdea').value = itm.related_idea_id || '';
            document.getElementById('propState').value = itm.state || '';
            document.getElementById('propOwner').value = itm.owner || '';
            document.getElementById('propApproval').value = itm.approval_date || '';
            document.getElementById('propCapacity').checked = ['true', 'yes', 'y', '1'].includes(String(itm.capacity_confirmed || '').toLowerCase());
            document.getElementById('propCapSource').value = itm.capacity_source || '';
            document.getElementById('propScoredBy').value = itm.scored_by || '';
            const sc = itm.scores || {};
            document.getElementById('f_drivers').value = sc.drivers ?? 5.0;
            document.getElementById('f_alignment').value = sc.alignment ?? 5.0;
            document.getElementById('f_outcomes').value = sc.outcomes_and_benefits ?? 5.0;
            document.getElementById('f_sector').value = sc.sector_benefits ?? 5.0;
            document.getElementById('f_readiness').value = sc.readiness ?? 5.0;
            document.getElementById('f_research').value = sc.extent_of_research ?? 5.0;
            document.getElementById('f_cost').value = sc.investment_cost ?? 5.0;
            document.getElementById('f_sponsor').value = sc.executive_support ?? 5.0;
            document.getElementById('f_ease').value = sc.ease_of_implementation ?? 5.0;
            updateFormScores();
            document.getElementById('onboardModal').style.display = 'flex';
        }

        function updateFormScores() {
            ['drivers','alignment','outcomes','sector','readiness','research','cost','sponsor','ease'].forEach(k => {
                const el = document.getElementById(`f_${k}`);
                const valEl = document.getElementById(`f_val_${k}`);
                if (el && valEl) valEl.innerText = parseFloat(el.value).toFixed(1);
            });
        }

        function closeModal() {
            document.getElementById('onboardModal').style.display = 'none';
        }

        function handleFormSubmit(e) {
            e.preventDefault();
            const editIdx = parseInt(document.getElementById('editItemIndex').value);
            const prev = editIdx >= 0 ? rawData[editIdx] : {};
            const item = Object.assign({}, prev, {
                id: document.getElementById('propId').value,
                name: document.getElementById('propName').value,
                sponsor: document.getElementById('propSponsor').value,
                lead_division: document.getElementById('propDivision').value,
                recommendation: document.getElementById('propRec').value,
                related_idea_id: document.getElementById('propIdea').value,
                state: document.getElementById('propState').value,
                owner: document.getElementById('propOwner').value,
                approval_date: document.getElementById('propApproval').value,
                capacity_confirmed: document.getElementById('propCapacity').checked ? 'true' : 'false',
                capacity_source: document.getElementById('propCapSource').value,
                scored_by: document.getElementById('propScoredBy').value,
                scores: {
                    drivers: parseFloat(document.getElementById('f_drivers').value),
                    alignment: parseFloat(document.getElementById('f_alignment').value),
                    outcomes_and_benefits: parseFloat(document.getElementById('f_outcomes').value),
                    sector_benefits: parseFloat(document.getElementById('f_sector').value),
                    readiness: parseFloat(document.getElementById('f_readiness').value),
                    extent_of_research: parseFloat(document.getElementById('f_research').value),
                    investment_cost: parseFloat(document.getElementById('f_cost').value),
                    executive_support: parseFloat(document.getElementById('f_sponsor').value),
                    ease_of_implementation: parseFloat(document.getElementById('f_ease').value)
                }
            });

            const scoresChanged = editIdx >= 0 && JSON.stringify(prev.scores || {}) !== JSON.stringify(item.scores);
            if (editIdx < 0 || scoresChanged) {
                item.scored_on = new Date().toISOString().slice(0, 10);
            }

            if (editIdx >= 0) {
                rawData[editIdx] = item;
            } else {
                rawData.push(item);
            }
            closeModal();
            recalculate();
        }

        async function saveToDisk() {
            const fwChanged = JSON.stringify(framework) !== loadedFrameworkStr;
            const today = new Date().toISOString().slice(0, 10);
            const scoreChanges = rawData.filter(item => {
                const b = baseline.find(x => x.id === item.id);
                return b && JSON.stringify(item.scores || {}) !== JSON.stringify(b.scores || {});
            }).length;
            let msg = 'Save ' + rawData.length + ' proposals to disk?';
            if (fwChanged) { msg += '\n\nScoring weights changed.'; }
            if (fwChanged || scoreChanges) { msg += '\n\nThe previous scores will be kept in each changed proposal\'s score history.'; }
            if (!window.confirm(msg)) { return; }
            applySaveSnapshots(rawData, baseline, { fwChanged: fwChanged, loadedVersion: loadedFrameworkVersion, loadedWeights: loadedWeights, today: today });
            if (fwChanged) { framework.version = 'custom-' + today + '-' + weightsHash(framework); }
            try {
                const res = await fetch('/api/save', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ items: rawData, framework: framework })
                });
                if (res.ok) {
                    snapshotBaseline();
                    const alert = document.getElementById('saveAlert');
                    alert.style.display = 'inline-block';
                    setTimeout(() => { alert.style.display = 'none'; }, 3000);
                }
            } catch (err) {
                alert('Error saving data to disk');
            }
        }

        window.onload = init;
    </script>
</body>
</html>
"""


class DashboardHandler(http.server.BaseHTTPRequestHandler):
    """Custom HTTP handler serving the dashboard and handling JSON save requests."""

    data_file_path = ""
    framework = DEFAULT_FRAMEWORK

    def do_GET(self):
        url = urllib.parse.urlparse(self.path)
        if url.path in ["/", "/index.html"]:
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(HTML_DASHBOARD.encode("utf-8"))
        elif url.path == "/api/data":
            items = load_dataset(self.data_file_path)
            payload = {
                "items": items,
                "framework": self.framework
            }
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(payload).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        url = urllib.parse.urlparse(self.path)
        if url.path == "/api/save":
            content_len = int(self.headers.get("Content-Length", 0))
            post_body = self.rfile.read(content_len)
            try:
                data = json.loads(post_body.decode("utf-8"))
                items = data.get("items", [])
                fw = data.get("framework", self.framework)
                save_dataset(self.data_file_path, items, fw)
                DashboardHandler.framework = fw
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "success", "saved_count": len(items)}).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        # Quiet standard HTTP access logs
        return


def run_app(file_path: str, port: int = 8050, open_browser: bool = True):
    """Run local dashboard web server."""
    DashboardHandler.data_file_path = os.path.abspath(file_path)
    try:
        DashboardHandler.framework = load_framework(DashboardHandler.data_file_path)
    except ValueError as exc:
        print(f"Error: {exc}. Fix or delete that file; scoring weights are not being silently reset.", file=sys.stderr)
        sys.exit(2)

    # Find open port if 8050 is occupied
    actual_port = port
    server = None
    for p in range(port, port + 20):
        try:
            server = socketserver.TCPServer(("127.0.0.1", p), DashboardHandler)
            actual_port = p
            break
        except OSError:
            continue

    if not server:
        print(f"Error: could not bind server to ports {port}-{port+20}", file=sys.stderr)
        sys.exit(1)

    url = f"http://localhost:{actual_port}"
    print(f"============================================================")
    print(f" B.C. Gov Investment Prioritization Interactive Workbench")
    print(f"============================================================")
    print(f" Ledger File : {os.path.abspath(file_path)}")
    print(f" Live Server : {url}")
    print(f" Press Ctrl+C in terminal to stop.")
    print(f"============================================================")

    if open_browser:
        webbrowser.open(url)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping dashboard server.")
        server.server_close()


def main():
    parser = argparse.ArgumentParser(description="Launch Interactive Investment Prioritization Dashboard.")
    parser.add_argument("--input", "-i", required=True, help="Path to input JSON or CSV scoring ledger")
    parser.add_argument("--port", "-p", type=int, default=8050, help="Port to bind server (default 8050)")
    parser.add_argument("--no-browser", action="store_true", help="Do not automatically launch web browser")

    args = parser.parse_args()
    run_app(args.input, port=args.port, open_browser=not args.no_browser)


if __name__ == "__main__":
    main()
