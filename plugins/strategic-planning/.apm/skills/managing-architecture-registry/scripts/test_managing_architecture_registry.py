#!/usr/bin/env python3
"""Unit tests for managing_architecture_registry.py."""

import tempfile
import unittest
from pathlib import Path

from managing_architecture_registry import (
    export_csv,
    init_registry,
    load_registry,
    query_entries,
    summarize_registry,
    upsert_entry,
    validate_registry,
)


class TestArchitectureRegistry(unittest.TestCase):
    def test_full_lifecycle(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            reg_path = Path(tmp) / "architecture-registry.json"
            csv_path = Path(tmp) / "architecture-registry.csv"

            data = init_registry(reg_path, project="BC Gov AI Front Door")
            upsert_entry(
                data,
                entry_id="TECH-001",
                name="Azure AI Search (Zone 1)",
                togaf_domain="Data",
                category="Vector & Semantic Search",
                vendor_or_service="Azure AI Search",
                plane="Data Plane",
                status="target",
                trust_zones=["Zone 1"],
                adrs=["ADR-005", "ADR-010"],
                work_packages=["WP-01", "WP-03"],
                private_endpoint_ips=1,
                residency="Canada Central",
                owner="Platform Team",
            )
            upsert_entry(
                data,
                entry_id="TECH-002",
                name="Microsoft Foundry Hosted Agents",
                togaf_domain="Application",
                category="Agent Runtime",
                vendor_or_service="Microsoft Foundry Agent Service",
                plane="Request Path",
                status="spike_verify",
                trust_zones=["Zone 1", "Zone 2"],
                adrs=["ADR-009"],
                work_packages=["WP-01"],
                private_endpoint_ips=3,
                residency="Canada Central",
            )
            self.assertEqual(validate_registry(data), [])

            hits = query_entries(data, status="spike_verify", zone="Zone 1")
            self.assertEqual([h["id"] for h in hits], ["TECH-002"])

            summary = summarize_registry(data)
            self.assertEqual(summary["total_entries"], 2)
            self.assertEqual(summary["total_private_endpoint_ips"], 4)

            count = export_csv(data, csv_path)
            self.assertEqual(count, 2)
            self.assertTrue(csv_path.exists())
            reloaded = load_registry(reg_path)
            self.assertEqual(reloaded["project"], "BC Gov AI Front Door")

    def test_validation_rejects_bad_domain_and_duplicate_id(self) -> None:
        data = {
            "entries": [
                {"id": "TECH-001", "name": "A", "togaf_domain": "Invalid", "status": "target"},
                {"id": "TECH-001", "name": "B", "togaf_domain": "Data", "status": "bad_status", "private_endpoint_ips": -1},
            ]
        }
        errs = validate_registry(data)
        self.assertGreaterEqual(len(errs), 4)


if __name__ == "__main__":
    unittest.main()
