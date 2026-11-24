#!/usr/bin/env python3
"""Tests for check_deliverable_sync.py and build_deliverables.py."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS_DIR))

import build_deliverables  # noqa: E402
import check_deliverable_sync as sync  # noqa: E402


def make_workbench(root: Path, adr_range: str = "ADR-001 to ADR-003", date: str = "2999-01-01") -> Path:
    (root / "adrs").mkdir()
    (root / "adrs" / "README.md").write_text("## ADR-001: a\n## ADR-002: b\n## ADR-003: c\n", encoding="utf-8")
    (root / "work-packages").mkdir()
    (root / "work-packages" / "README.md").write_text("## WP-01: x\n## WP-01C: y\n", encoding="utf-8")
    (root / "diagrams").mkdir()
    (root / "diagrams" / "flow.mmd").write_text("flowchart LR\nA-->B\n", encoding="utf-8")
    dl = root / "deliverables"
    (dl / "data").mkdir(parents=True)
    (dl / "images").mkdir()
    (dl / "images" / "flow.svg").write_text("<svg/>", encoding="utf-8")
    (dl / "data" / "page.json").write_text(json.dumps({
        "title": "T", "org_trail": "O", "date": date, "summary": f"{adr_range}; WP-01 and WP-01C"}), encoding="utf-8")
    (dl / "data" / "architecture-diagrams.json").write_text(json.dumps({"slug": "flow"}), encoding="utf-8")
    return dl


class TestSyncChecker(unittest.TestCase):
    def test_in_sync_reports_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dl = make_workbench(root)
            self.assertEqual(sync.run_checks(root, dl), [])

    def test_stale_adr_range_and_missing_wp_are_flagged(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dl = make_workbench(root, adr_range="ADR-001 to ADR-002")
            (dl / "data" / "page.json").write_text(json.dumps({"summary": "ADR-001 to ADR-002; WP-01"}), encoding="utf-8")
            cats = [f["category"] for f in sync.run_checks(root, dl)]
            self.assertIn("adr-range", cats)
            self.assertIn("work-package", cats)

    def test_subrange_not_flagged_as_stale(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dl = make_workbench(root)
            (dl / "data" / "page.json").write_text(json.dumps({"summary": "ADR-001 to ADR-003 and ADR-002 to ADR-002 WP-01 WP-01C"}), encoding="utf-8")
            self.assertEqual([f for f in sync.run_checks(root, dl) if f["category"] == "adr-range"], [])

    def test_missing_svg_and_gallery_entry_flagged(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dl = make_workbench(root)
            (dl / "images" / "flow.svg").unlink()
            (root / "diagrams" / "other.mmd").write_text("flowchart LR\nA-->B\n", encoding="utf-8")
            msgs = " ".join(f["message"] for f in sync.run_checks(root, dl) if f["category"] == "diagram")
            self.assertIn("flow.mmd has no images/flow.svg", msgs)
            self.assertIn("other.mmd is not in architecture-diagrams.json", msgs)

    def test_reviewed_date_clears_source_newer(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dl = make_workbench(root, date="2000-01-01")
            self.assertIn("source-newer", [f["category"] for f in sync.run_checks(root, dl)])
            doc = json.loads((dl / "data" / "page.json").read_text())
            doc["reviewed"] = "2999-01-01"
            (dl / "data" / "page.json").write_text(json.dumps(doc), encoding="utf-8")
            self.assertNotIn("source-newer", [f["category"] for f in sync.run_checks(root, dl)])

    def test_registry_range_flagged(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dl = make_workbench(root)
            (root / "architecture").mkdir()
            (root / "architecture" / "architecture-registry.json").write_text('{"a":"TECH-001","b":"TECH-005"}', encoding="utf-8")
            (dl / "data" / "page.json").write_text(json.dumps({"summary": "TECH-001 to TECH-003 WP-01 WP-01C"}), encoding="utf-8")
            self.assertIn("registry", [f["category"] for f in sync.run_checks(root, dl)])


class TestBuildDeliverables(unittest.TestCase):
    def test_validate_inputs_reports_missing_and_emoji(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            data = Path(tmp)
            (data / "site.json").write_text(json.dumps({
                "title": "T", "org_trail": "O", "summary": "S",
                "pages": [{"label": "A", "filename": "a.html", "type": "executive-brief", "input": "a.json"},
                          {"label": "B", "filename": "b.html", "type": "executive-brief", "input": "b.json"}]}), encoding="utf-8")
            (data / "a.json").write_text(json.dumps({"title": "ok \U0001F600"}), encoding="utf-8")
            problems = build_deliverables.validate_inputs(data)
            self.assertTrue(any("b.json" in p and "not found" in p for p in problems))
            self.assertTrue(any("a.json" in p for p in problems))

    def test_check_links_finds_broken_target_and_anchor(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            (out / "a.html").write_text('<a href="b.html#present">x</a><a href="b.html#gone">y</a><img src="missing.svg">', encoding="utf-8")
            (out / "b.html").write_text('<h2 id="present">p</h2>', encoding="utf-8")
            problems = build_deliverables.check_links(out)
            self.assertEqual(len(problems), 2)
            self.assertTrue(any("missing.svg" in p for p in problems))
            self.assertTrue(any("#gone" in p for p in problems))

    def test_end_to_end_render_without_mermaid(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dl = root / "deliverables"
            (dl / "data").mkdir(parents=True)
            (dl / "data" / "site.json").write_text(json.dumps({
                "title": "T", "org_trail": "O", "summary": "S",
                "pages": [{"label": "Brief", "filename": "brief.html", "type": "executive-brief", "input": "brief.json"}]}), encoding="utf-8")
            (dl / "data" / "brief.json").write_text(json.dumps({
                "title": "B", "org_trail": "O", "audience": "A", "summary": "S",
                "sections": [{"heading": "H", "body": "text"}]}), encoding="utf-8")
            rc = build_deliverables.main(["--workbench", str(root), "--skip-mmd"])
            self.assertEqual(rc, 0)
            self.assertTrue((dl / "index.html").exists())
            self.assertTrue((dl / "brief.html").exists())


if __name__ == "__main__":
    unittest.main()
