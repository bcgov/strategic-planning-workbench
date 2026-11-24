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
import deliverable_lock as lock  # noqa: E402
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

    def test_legacy_date_check_without_sources_json(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dl = make_workbench(root, date="2000-01-01")
            self.assertIn("source-newer", [f["category"] for f in sync.run_checks(root, dl)])

    def test_registry_range_flagged(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dl = make_workbench(root)
            (root / "architecture").mkdir()
            (root / "architecture" / "architecture-registry.json").write_text('{"a":"TECH-001","b":"TECH-005"}', encoding="utf-8")
            (dl / "data" / "page.json").write_text(json.dumps({"summary": "TECH-001 to TECH-003 WP-01 WP-01C"}), encoding="utf-8")
            self.assertIn("registry", [f["category"] for f in sync.run_checks(root, dl)])


class TestLockfile(unittest.TestCase):
    def _setup(self, tmp: str):
        root = Path(tmp)
        dl = make_workbench(root, date="2026-01-01")
        data = dl / "data"
        (data / lock.SOURCES_FILE).write_text(json.dumps({"defaults": ["adrs/README.md", "diagrams/*.mmd"], "pages": {}}), encoding="utf-8")
        return root, data

    def test_unstamped_then_ok_then_stale_then_ok(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root, data = self._setup(tmp)
            states = {r["page"]: r["state"] for r in lock.status(root, data)}
            self.assertEqual(set(states.values()), {"unstamped"})
            lock.stamp(root, data, lock.page_files(data))
            self.assertEqual({r["state"] for r in lock.status(root, data)}, {"ok"})
            (root / "adrs" / "README.md").write_text("## ADR-001: a\n## ADR-004: new\n", encoding="utf-8")
            res = lock.status(root, data)
            self.assertTrue(all(r["state"] == "stale" and r["changed"] == ["adrs/README.md"] for r in res))
            lock.stamp(root, data, ["page.json"])
            self.assertEqual({r["page"]: r["state"] for r in lock.status(root, data)}["page.json"], "ok")

    def test_new_and_removed_source_files_detected_and_crlf_ignored(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root, data = self._setup(tmp)
            lock.stamp(root, data, ["page.json"])
            (root / "adrs" / "README.md").write_bytes((root / "adrs" / "README.md").read_bytes().replace(b"\n", b"\r\n"))
            self.assertEqual(lock.status(root, data)[1]["state"], "ok")  # CRLF only
            (root / "diagrams" / "new.mmd").write_text("flowchart LR\nA-->B\n", encoding="utf-8")
            (root / "diagrams" / "flow.mmd").unlink()
            r = [x for x in lock.status(root, data) if x["page"] == "page.json"][0]
            self.assertEqual((r["added"], r["removed"]), (["diagrams/new.mmd"], ["diagrams/flow.mmd"]))

    def test_page_specific_sources_and_defaults_extension(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root, data = self._setup(tmp)
            cfg = {"defaults": ["adrs/README.md"], "pages": {"page.json": ["$defaults", "work-packages/README.md"]}}
            (data / lock.SOURCES_FILE).write_text(json.dumps(cfg), encoding="utf-8")
            self.assertEqual(lock.declared_sources(data, "page.json"), ["adrs/README.md", "work-packages/README.md"])
            self.assertEqual(lock.declared_sources(data, "other.json"), ["adrs/README.md"])

    def test_worklist_names_changed_sources(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root, data = self._setup(tmp)
            lock.stamp(root, data, lock.page_files(data))
            (root / "work-packages" / "README.md").write_text("## WP-09: z\n", encoding="utf-8")
            (data / lock.SOURCES_FILE).write_text(json.dumps({"defaults": ["work-packages/README.md"], "pages": {}}), encoding="utf-8")
            self.assertIn("work-packages/README.md", lock.worklist(root, data))

    def test_facts_and_token_expansion(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_workbench(root)
            facts = lock.derive_facts(root)
            self.assertEqual(facts["adr.range"], "ADR-001 to ADR-003")
            self.assertEqual(facts["wp.count"], "2")
            self.assertEqual(facts["diagram.count"], "1")
            out = lock.expand_tokens({"a": ["{{ adr.latest }} of {{adr.count}}"]}, facts)
            self.assertEqual(out, {"a": ["003 of 3"]})
            with self.assertRaises(ValueError):
                lock.expand_tokens("{{nope.nothing}}", facts, "x.json")

    def test_build_refuses_stale_pages_unless_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            dl = make_workbench(root)
            data = dl / "data"
            (data / "site.json").write_text(json.dumps({
                "title": "T", "org_trail": "O", "summary": "S",
                "pages": [{"label": "P", "filename": "p.html", "type": "executive-brief", "input": "page.json"}]}), encoding="utf-8")
            (data / "page.json").write_text(json.dumps({
                "title": "B", "org_trail": "O", "audience": "A", "summary": "{{adr.range}} WP-01 WP-01C",
                "sections": [{"heading": "H", "body": "text"}]}), encoding="utf-8")
            (data / "architecture-diagrams.json").unlink()
            (data / lock.SOURCES_FILE).write_text(json.dumps({"defaults": ["adrs/README.md"], "pages": {}}), encoding="utf-8")
            self.assertEqual(build_deliverables.main(["--workbench", str(root), "--skip-mmd"]), 1)  # unstamped
            lock.stamp(root, data, lock.page_files(data))
            self.assertEqual(build_deliverables.main(["--workbench", str(root), "--skip-mmd"]), 0)
            self.assertIn("ADR-001 to ADR-003", (dl / "p.html").read_text(encoding="utf-8"))


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
