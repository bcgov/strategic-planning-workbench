#!/usr/bin/env python3
"""Unit tests for rendering-strategic-visuals-and-decks Python renderers."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

import render_deck  # noqa: E402
import render_html_brief  # noqa: E402
import render_mermaid_package  # noqa: E402


class TestRenderers(unittest.TestCase):
    def test_executive_brief_html_has_tokens_and_footer(self) -> None:
        payload = {
            "title": "Unified front door architecture brief",
            "org_trail": "Government of British Columbia",
            "audience": "Executive leadership",
            "summary": "A federated discovery model reduces citizen navigation friction.",
            "sections": [
                {
                    "heading": "Delivery phases",
                    "cards": [
                        {
                            "id": "WP-01",
                            "title": "Stage 0 spikes",
                            "description": "Validate Entra Agent ID and OBO.",
                            "committed": True,
                        },
                        {
                            "id": "IDEA-02",
                            "title": "Cross-ministry expansion",
                            "description": "Pending privacy review.",
                            "committed": False,
                            "missing_evidence": "PIA pending",
                        },
                    ],
                }
            ],
        }
        out = render_html_brief.render_executive_brief(payload)
        self.assertIn("#013366", out)
        self.assertIn("#FBD389", out)
        self.assertIn("bc-indigenous-footer", out)
        self.assertIn("card gate", out)
        self.assertIn("PIA pending", out)

    def test_logic_model_html_renders_stages(self) -> None:
        payload = {
            "title": "Citizen navigation logic model",
            "inputs": {"title": "Inputs", "items": ["Engineering team", "Azure landing zone"]},
            "activities": {"title": "Activities", "items": ["Build capability registry"]},
            "outputs": {"title": "Outputs", "items": ["Published discovery contract"]},
            "immediate_outcomes": {"title": "Immediate outcomes", "items": ["Citizens routed accurately"]},
            "assumptions": ["Ministries maintain current manifests."],
        }
        out = render_html_brief.render_logic_model(payload)
        self.assertIn("Causal results chain", out)
        self.assertIn("Published discovery contract", out)
        self.assertIn("Assumptions and external risks", out)

    def test_emoji_rejected(self) -> None:
        with self.assertRaises(ValueError):
            render_html_brief.check_no_emoji({"title": "Launch 🚀"})

    def test_dashboard_gates_unconfirmed_work(self) -> None:
        payload = {
            "title": "Portfolio dashboard",
            "org_trail": "Government of British Columbia",
            "objectives": [{"id": "OBJ-1", "title": "Improve access"}],
            "work_items": [
                {
                    "id": "WORK-1",
                    "title": "Core gateway",
                    "kind": "WORK",
                    "sponsor": "ADM",
                    "owner": "Lead Architect",
                    "capacity_confirmed": True,
                    "start_date": "2026-01-15",
                    "duration": "30d",
                },
                {
                    "id": "WORK-2",
                    "title": "Unstaffed pilot",
                    "kind": "WORK",
                    "sponsor": "ADM",
                    "owner": "",
                    "capacity_confirmed": False,
                    "start_date": "2026-03-01",
                },
            ],
        }
        html_out = render_html_brief.render_dashboard(payload)
        self.assertIn("WORK-1 — Committed work", html_out)
        self.assertIn("WORK-2 — Decision gate (missing: owner, confirmed capacity)", html_out)

        gantt_out = render_mermaid_package.render_gantt(payload)
        self.assertIn("WORK-1 Core gateway :WORK_1, 2026-01-15, 30d", gantt_out)
        self.assertIn(":milestone, WORK_2, 2026-03-01, 0d", gantt_out)

    def test_mermaid_wrapping_and_quoting(self) -> None:
        wrapped = render_mermaid_package.wrap_label('CAP-1: Citizen "Front Door" Routing (Zone 1)', width=16)
        self.assertIn("<br>", wrapped)
        self.assertNotIn('"', wrapped)

    def test_deck_marp_and_pptx_spec(self) -> None:
        deck = {
            "title": "Architecture briefing",
            "org_trail": "Government of British Columbia",
            "slides": [
                {"layout": "bullets", "heading": "Key decisions", "bullets": ["Approve Stage 0 spike"]}
            ],
        }
        marp = render_deck.render_marp(deck)
        self.assertIn("marp: true", marp)
        self.assertIn("closing-slide", marp)

        spec = json.loads(render_deck.render_pptx_spec(deck))
        self.assertEqual(spec["tokens"]["navy"], "013366")
        self.assertEqual(len(spec["slides"]), 1)


if __name__ == "__main__":
    unittest.main()
