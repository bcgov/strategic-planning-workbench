#!/usr/bin/env python3
"""Unit tests for scaffold_project_structure.py and validate_project_structure.py."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from scaffold_project_structure import load_profile, scaffold  # noqa: E402
from validate_project_structure import validate_repo  # noqa: E402


class TestProjectStructureScripts(unittest.TestCase):
    """Verify scaffolding and validation across all four canonical profiles."""

    def test_scaffold_and_validate_all_profiles(self) -> None:
        for profile_id in (
            "strategy-only",
            "solution-architecture",
            "strategy-and-architecture",
            "enterprise-architecture",
        ):
            with tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                profile = load_profile(profile_id)
                scaffold(
                    target=root,
                    profile=profile,
                    project_name="Test Initiative",
                    with_execution=True,
                )
                report = validate_repo(
                    target=root, profile_id="auto", with_execution=True
                )
                self.assertEqual(report["profile"], profile_id)
                self.assertEqual(report["status"], "PASS", report)

    def test_dry_run_writes_nothing_and_no_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            profile = load_profile("solution-architecture")
            scaffold(target=root, profile=profile, project_name="Dry", dry_run=True)
            self.assertFalse((root / "README.md").exists())

            (root / "README.md").write_text("custom", encoding="utf-8")
            result = scaffold(target=root, profile=profile, project_name="Real")
            self.assertIn("README.md", result["skipped_files"])
            self.assertEqual((root / "README.md").read_text(encoding="utf-8"), "custom")

    def test_detects_legacy_alias_and_broken_link(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            profile = load_profile("solution-architecture")
            scaffold(target=root, profile=profile, project_name="Legacy Test")
            (root / "capabilities").mkdir()
            (root / "README.md").write_text(
                "# Test\n\nSee [Missing](does-not-exist.md).\n", encoding="utf-8"
            )
            report = validate_repo(target=root, profile_id="solution-architecture")
            self.assertEqual(report["status"], "FAIL")
            self.assertTrue(
                any("capabilities" in w for w in report["warnings"]), report["warnings"]
            )
            self.assertTrue(
                any("does-not-exist.md" in b for b in report["broken_links"]),
                report["broken_links"],
            )

    def test_coherence_warnings_for_forgotten_adr_and_broken_registry_ref(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            profile = load_profile("solution-architecture")
            scaffold(target=root, profile=profile, project_name="Coherence Test")
            (root / "adrs" / "ADR-0002-pending.md").write_text(
                "# ADR-0002: Pending\n\n- **Status:** Proposed\n", encoding="utf-8"
            )
            (root / "architecture" / "architecture-registry.json").write_text(
                '{"components": [{"id": "TECH-001", "adrs": ["ADR-9999"]}]}',
                encoding="utf-8",
            )
            report = validate_repo(
                target=root, profile_id="solution-architecture", strict_coherence=True
            )
            self.assertEqual(report["status"], "FAIL")
            self.assertTrue(
                any("ADR-0002-pending.md" in w for w in report["coherence_warnings"]),
                report["coherence_warnings"],
            )
            self.assertTrue(
                any("ADR-9999" in w for w in report["coherence_warnings"]),
                report["coherence_warnings"],
            )


if __name__ == "__main__":
    unittest.main()
