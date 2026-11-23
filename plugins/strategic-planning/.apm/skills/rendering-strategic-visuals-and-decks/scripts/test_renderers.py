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

    def test_convert_mmd_falls_back_to_npx_when_mmdc_fails(self):
        import subprocess
        from unittest import mock

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            mmd = tmp_path / "sample.mmd"
            svg = tmp_path / "out" / "sample.svg"
            mmd.write_text("flowchart LR\nA --> B\n", encoding="utf-8")

            calls = []

            def fake_run(cmd, check=True):
                calls.append(cmd)
                if cmd[0] == "/usr/local/bin/mmdc":
                    raise subprocess.CalledProcessError(1, cmd)
                svg.write_text("<svg></svg>", encoding="utf-8")
                return subprocess.CompletedProcess(cmd, 0)

            with (
                mock.patch.object(render_html_brief.shutil, "which", side_effect=lambda name: f"/usr/local/bin/{name}"),
                mock.patch.object(render_html_brief.subprocess, "run", side_effect=fake_run),
            ):
                result = render_html_brief.convert_mmd_to_svg(mmd, svg)

            self.assertEqual(result, svg)
            self.assertTrue(svg.is_file())
            self.assertEqual(len(calls), 2)
            self.assertEqual(calls[0][0], "/usr/local/bin/mmdc")
            self.assertEqual(calls[1][0], "/usr/local/bin/npx")
            self.assertIn("-c", calls[0])

    def test_sanitize_mermaid_svg_and_stale_foreignobject_regeneration(self) -> None:
        from unittest import mock

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            mmd = tmp_path / "sample.mmd"
            svg = tmp_path / "out" / "sample.svg"
            mmd.write_text("flowchart LR\nA --> B\n", encoding="utf-8")
            svg.parent.mkdir(parents=True, exist_ok=True)
            # Pre-existing newer SVG with <foreignObject> should be treated as stale and regenerated
            svg.write_text("<svg><foreignObject></foreignObject></svg>", encoding="utf-8")

            calls = []

            def fake_run(cmd, check=True):
                calls.append(cmd)
                svg.write_text(
                    '<svg><path d="M0,0 L10,10" class="edge-thickness-normal edge-pattern-dotted flowchart-link" style=";"/></svg>',
                    encoding="utf-8",
                )

            with (
                mock.patch.object(render_html_brief.shutil, "which", side_effect=lambda name: f"/usr/local/bin/{name}" if name == "mmdc" else None),
                mock.patch.object(render_html_brief.subprocess, "run", side_effect=fake_run),
            ):
                render_html_brief.convert_mmd_to_svg(mmd, svg)

            self.assertEqual(len(calls), 1)
            rendered_svg = svg.read_text(encoding="utf-8")
            self.assertIn('fill="none"', rendered_svg)
            self.assertIn('stroke="#333333"', rendered_svg)
            self.assertIn('stroke-dasharray="3 3"', rendered_svg)

    def test_cross_page_links_anchors_and_xss_safety(self):
        payload = {
            "title": "Linked Brief",
            "org_trail": "Government of British Columbia",
            "summary": "See [MAF 1.0](technology-profiles.html#maf-1-0) and [bad](javascript:alert(1)).",
            "highlights": [
                {"label": "Runtime", "value": "ACA + MAF 1.0", "href": "technology-profiles.html#hosting-profiles", "tone": "success"}
            ],
            "sections": [
                {
                    "id": "maf-1-0",
                    "heading": "MAF 1.0 Details",
                    "body": "Uses [Decision 1.1](technology-profiles.html#decision-1-1).",
                    "cards": [
                        {"id": "TECH-004", "title": "ACA", "description": "Hosted on [ACA](technology-profiles.html#hosting-profiles).", "href": "technology-profiles.html#hosting-profiles"}
                    ],
                }
            ],
        }
        html_out = render_html_brief.render_executive_brief(payload)
        self.assertIn('id="maf-1-0"', html_out)
        self.assertIn('href="technology-profiles.html#maf-1-0"', html_out)
        self.assertIn('href="technology-profiles.html#hosting-profiles"', html_out)
        self.assertIn('href="technology-profiles.html#decision-1-1"', html_out)
        self.assertNotIn('href="javascript:', html_out)

    def test_non_embedded_image_paths_are_rebased_and_validated(self) -> None:
        from unittest import mock

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            data_dir = tmp_path / "deliverables" / "data"
            out_dir = tmp_path / "deliverables"
            img_dir = out_dir / "images"
            mmd_dir = tmp_path / "diagrams"
            data_dir.mkdir(parents=True)
            img_dir.mkdir(parents=True)
            mmd_dir.mkdir(parents=True)

            (img_dir / "conceptual.svg").write_text("<svg></svg>", encoding="utf-8")
            (mmd_dir / "flow.mmd").write_text("flowchart LR\nA --> B\n", encoding="utf-8")

            (data_dir / "brief.json").write_text(
                json.dumps({
                    "title": "Brief",
                    "org_trail": "Government of British Columbia",
                    "summary": "Summary",
                    "sections": [
                        {
                            "heading": "View",
                            "images": [{"src": "../images/conceptual.svg", "alt": "Conceptual"}],
                        }
                    ],
                }),
                encoding="utf-8",
            )
            (data_dir / "aoap.json").write_text(
                json.dumps({
                    "title": "AOAP",
                    "org_trail": "Government of British Columbia",
                    "hypothesis": "H",
                    "invariants": "I",
                    "planes": [{"title": "P", "items": ["X"]}],
                    "diagram": {"src": "../../diagrams/flow.mmd", "alt": "Flow"},
                }),
                encoding="utf-8",
            )
            (data_dir / "gallery.json").write_text(
                json.dumps({
                    "title": "Gallery",
                    "org_trail": "Government of British Columbia",
                    "summary": "All",
                    "domains": [
                        {
                            "name": "Core",
                            "description": "Core",
                            "items": [
                                {"slug": "flow", "title": "Flow", "src": "../../diagrams/flow.mmd", "intro": "Intro"}
                            ],
                        }
                    ],
                }),
                encoding="utf-8",
            )
            site_data = {
                "title": "Portal",
                "org_trail": "Government of British Columbia",
                "summary": "Hub",
                "pages": [
                    {"label": "Brief", "filename": "executive-brief.html", "type": "executive-brief", "input": "brief.json"},
                    {"label": "AOAP", "filename": "architecture-on-a-page.html", "type": "architecture-on-a-page", "input": "aoap.json"},
                    {"label": "Diagrams", "filename": "architecture-diagrams.html", "type": "diagram-gallery", "input": "gallery.json"},
                ],
            }

            def fake_convert(mmd_path: Path, svg_path: Path) -> Path:
                svg_path.parent.mkdir(parents=True, exist_ok=True)
                svg_path.write_text("<svg></svg>", encoding="utf-8")
                return svg_path

            with mock.patch.object(render_html_brief, "convert_mmd_to_svg", side_effect=fake_convert):
                render_html_brief.render_site(
                    site_data, site_dir=data_dir, output_dir=out_dir, embed_images=False, convert_mmd=True
                )

            brief_html = (out_dir / "executive-brief.html").read_text(encoding="utf-8")
            aoap_html = (out_dir / "architecture-on-a-page.html").read_text(encoding="utf-8")
            gal_html = (out_dir / "architecture-diagrams.html").read_text(encoding="utf-8")
            sub_html = (out_dir / "diagrams" / "flow.html").read_text(encoding="utf-8")

            self.assertIn('src="images/conceptual.svg"', brief_html)
            self.assertIn('src="images/flow.svg"', aoap_html)
            self.assertIn('src="images/flow.svg"', gal_html)
            self.assertIn('src="../images/flow.svg"', sub_html)

            missing_payload = {
                "title": "Missing",
                "org_trail": "Government of British Columbia",
                "summary": "Summary",
                "sections": [
                    {"heading": "Broken", "images": [{"src": "../images/does-not-exist.svg", "alt": "Missing"}]}
                ],
            }
            with self.assertRaises(FileNotFoundError):
                render_html_brief.render_executive_brief(
                    missing_payload, base_dir=data_dir, embed_images=False, html_output_dir=out_dir
                )


if __name__ == "__main__":
    unittest.main()
