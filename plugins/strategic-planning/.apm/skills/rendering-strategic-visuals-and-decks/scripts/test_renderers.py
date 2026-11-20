#!/usr/bin/env python3
"""Unit tests for rendering-strategic-visuals-and-decks Python renderers."""

from __future__ import annotations

import json
import sys
import tempfile
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
        self.assertIn("lm-chevron", out)
        self.assertIn("Your planned work", out)
        self.assertIn("Published discovery contract", out)
        self.assertIn("Assumptions and external factors", out)

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

    def test_executive_brief_renders_and_embeds_images(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            svg_path = tmp_path / "arch.svg"
            svg_path.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="10" height="10"></svg>', encoding="utf-8")
            payload = {
                "title": "Brief with diagram",
                "org_trail": "Government of British Columbia",
                "summary": "Includes architecture diagram.",
                "sections": [
                    {
                        "heading": "Overview",
                        "images": [
                            {"src": "arch.svg", "alt": "Architecture diagram", "caption": "Figure 1: Overview"}
                        ],
                    }
                ],
            }
            rel_html = render_html_brief.render_executive_brief(payload, base_dir=tmp_path, embed_images=False)
            self.assertIn('src="arch.svg"', rel_html)
            self.assertIn("Figure 1: Overview", rel_html)

            emb_html = render_html_brief.render_executive_brief(payload, base_dir=tmp_path, embed_images=True)
            self.assertIn("data:image/svg+xml;base64,", emb_html)

    def test_render_site_builds_index_and_linked_subpages(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            (tmp_path / "brief.json").write_text(
                json.dumps({
                    "title": "Brief",
                    "org_trail": "Government of British Columbia",
                    "summary": "Summary",
                    "sections": [{"heading": "One", "body": "Body"}],
                }),
                encoding="utf-8",
            )
            site_data = {
                "title": "Portal",
                "org_trail": "Government of British Columbia",
                "summary": "Hub summary",
                "pages": [
                    {"label": "Executive Brief", "filename": "executive-brief.html", "type": "executive-brief", "input": "brief.json"}
                ],
            }
            out_dir = tmp_path / "out"
            written = render_html_brief.render_site(site_data, site_dir=tmp_path, output_dir=out_dir)
            self.assertEqual(len(written), 2)
            idx = (out_dir / "index.html").read_text(encoding="utf-8")
            self.assertIn('href="executive-brief.html"', idx)
            self.assertIn("bc-nav", idx)

    def test_architecture_on_a_page_and_diagram_gallery(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            svg_path = tmp_path / "c.svg"
            svg_path.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="10" height="10"></svg>', encoding="utf-8")
            aoap = {
                "title": "Arch on a Page",
                "org_trail": "Government of British Columbia",
                "hypothesis": "Federated discovery",
                "invariants": "APIM /mcp",
                "planes": [{"title": "Experience", "items": ["Web App"]}],
                "diagram": {"src": "c.svg", "alt": "Conceptual"},
                "work_packages": [{"id": "WP-01", "summary": "Contracts", "committed": True}],
            }
            aoap_html = render_html_brief.render_architecture_on_a_page(aoap, base_dir=tmp_path, embed_images=True)
            self.assertIn("Core hypothesis and flow", aoap_html)
            self.assertIn("WP-01", aoap_html)

            gal = {
                "title": "Diagrams",
                "org_trail": "Government of British Columbia",
                "summary": "All views",
                "domains": [
                    {
                        "name": "Conceptual",
                        "description": "Core",
                        "items": [{"slug": "c", "title": "Conceptual", "src": "c.svg", "intro": "Intro"}],
                    }
                ],
            }
            written = render_html_brief.render_diagram_gallery(gal, base_dir=tmp_path, output_dir=tmp_path / "out", embed_images=True)
            self.assertEqual(len(written), 2)
            self.assertTrue((tmp_path / "out" / "diagrams" / "c.html").is_file())


if __name__ == "__main__":
    unittest.main()
