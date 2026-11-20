#!/usr/bin/env python3
"""Manage, validate, query, and export a TOGAF BDAT architecture & technology registry (JSON + CSV)."""

import argparse
import csv
import datetime as _dt
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

VALID_DOMAINS = ("Business", "Data", "Application", "Technology")
VALID_STATUSES = ("target", "spike_verify", "plan_b", "deferred", "deprecated")
SCHEMA_VERSION = "1.0"


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _split_csv_arg(val: Optional[str]) -> List[str]:
    if not val:
        return []
    return [x.strip() for x in val.split(",") if x.strip()]


def load_registry(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def save_registry(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data["updated_at"] = _utc_now()
    with path.open("w", encoding="utf-8", newline="\n") as fh:
        json.dump(data, fh, indent=2)
        fh.write("\n")


def init_registry(path: Path, project: str, force: bool = False) -> Dict[str, Any]:
    if path.exists() and not force:
        raise FileExistsError(f"Registry already exists: {path} (use --force to overwrite)")
    data: Dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "project": project,
        "updated_at": _utc_now(),
        "entries": [],
    }
    save_registry(path, data)
    return data


def upsert_entry(
    data: Dict[str, Any],
    entry_id: str,
    name: Optional[str] = None,
    togaf_domain: Optional[str] = None,
    category: Optional[str] = None,
    vendor_or_service: Optional[str] = None,
    plane: Optional[str] = None,
    status: Optional[str] = None,
    trust_zones: Optional[List[str]] = None,
    adrs: Optional[List[str]] = None,
    work_packages: Optional[List[str]] = None,
    private_endpoint_ips: Optional[int] = None,
    residency: Optional[str] = None,
    owner: Optional[str] = None,
    notes: Optional[str] = None,
) -> Dict[str, Any]:
    entries = data.setdefault("entries", [])
    existing = next((e for e in entries if e.get("id") == entry_id), None)
    if existing is None:
        existing = {
            "id": entry_id,
            "name": name or "",
            "togaf_domain": togaf_domain or "",
            "category": category or "",
            "vendor_or_service": vendor_or_service or "",
            "plane": plane or "",
            "status": status or "target",
            "trust_zones": trust_zones or [],
            "adrs": adrs or [],
            "work_packages": work_packages or [],
            "private_endpoint_ips": private_endpoint_ips if private_endpoint_ips is not None else 0,
            "residency": residency or "",
            "owner": owner or "",
            "notes": notes or "",
        }
        entries.append(existing)
    else:
        if name is not None:
            existing["name"] = name
        if togaf_domain is not None:
            existing["togaf_domain"] = togaf_domain
        if category is not None:
            existing["category"] = category
        if vendor_or_service is not None:
            existing["vendor_or_service"] = vendor_or_service
        if plane is not None:
            existing["plane"] = plane
        if status is not None:
            existing["status"] = status
        if trust_zones is not None:
            existing["trust_zones"] = trust_zones
        if adrs is not None:
            existing["adrs"] = adrs
        if work_packages is not None:
            existing["work_packages"] = work_packages
        if private_endpoint_ips is not None:
            existing["private_endpoint_ips"] = private_endpoint_ips
        if residency is not None:
            existing["residency"] = residency
        if owner is not None:
            existing["owner"] = owner
        if notes is not None:
            existing["notes"] = notes
    return existing


def validate_registry(data: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    if not isinstance(data.get("entries"), list):
        return ["'entries' must be a JSON list."]
    seen_ids = set()
    for idx, entry in enumerate(data["entries"]):
        eid = entry.get("id", "")
        if not eid:
            errors.append(f"Entry[{idx}] missing required 'id'.")
        elif eid in seen_ids:
            errors.append(f"Duplicate entry id: '{eid}'.")
        seen_ids.add(eid)

        for req in ("name", "togaf_domain", "status"):
            if not entry.get(req):
                errors.append(f"Entry '{eid or idx}' missing required '{req}'.")

        dom = entry.get("togaf_domain")
        if dom and dom not in VALID_DOMAINS:
            errors.append(f"Entry '{eid}' invalid togaf_domain '{dom}' (expected {VALID_DOMAINS}).")

        st = entry.get("status")
        if st and st not in VALID_STATUSES:
            errors.append(f"Entry '{eid}' invalid status '{st}' (expected {VALID_STATUSES}).")

        pe_ips = entry.get("private_endpoint_ips", 0)
        if not isinstance(pe_ips, int) or pe_ips < 0:
            errors.append(f"Entry '{eid}' private_endpoint_ips must be a non-negative integer.")
    return errors


def query_entries(
    data: Dict[str, Any],
    domain: Optional[str] = None,
    status: Optional[str] = None,
    zone: Optional[str] = None,
    adr: Optional[str] = None,
    work_package: Optional[str] = None,
    search: Optional[str] = None,
) -> List[Dict[str, Any]]:
    results = []
    needle = search.lower() if search else None
    for e in data.get("entries", []):
        if domain and e.get("togaf_domain", "").lower() != domain.lower():
            continue
        if status and e.get("status", "").lower() != status.lower():
            continue
        if zone and zone not in e.get("trust_zones", []):
            continue
        if adr and adr not in e.get("adrs", []):
            continue
        if work_package and work_package not in e.get("work_packages", []):
            continue
        if needle:
            blob = json.dumps(e).lower()
            if needle not in blob:
                continue
        results.append(e)
    return results


def export_csv(data: Dict[str, Any], out_path: Path) -> int:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "id",
        "name",
        "togaf_domain",
        "category",
        "vendor_or_service",
        "plane",
        "status",
        "trust_zones",
        "adrs",
        "work_packages",
        "private_endpoint_ips",
        "residency",
        "owner",
        "notes",
    ]
    entries = data.get("entries", [])
    with out_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for e in entries:
            row = dict(e)
            for list_col in ("trust_zones", "adrs", "work_packages"):
                row[list_col] = "; ".join(e.get(list_col, []))
            writer.writerow({k: row.get(k, "") for k in fieldnames})
    return len(entries)


def summarize_registry(data: Dict[str, Any]) -> Dict[str, Any]:
    entries = data.get("entries", [])
    by_domain: Dict[str, int] = {}
    by_status: Dict[str, int] = {}
    total_pe_ips = 0
    for e in entries:
        d = e.get("togaf_domain", "Unknown")
        s = e.get("status", "unknown")
        by_domain[d] = by_domain.get(d, 0) + 1
        by_status[s] = by_status.get(s, 0) + 1
        total_pe_ips += int(e.get("private_endpoint_ips", 0) or 0)
    return {
        "project": data.get("project", ""),
        "total_entries": len(entries),
        "by_domain": by_domain,
        "by_status": by_status,
        "total_private_endpoint_ips": total_pe_ips,
    }


def _format_table(entries: List[Dict[str, Any]]) -> str:
    if not entries:
        return "No matching entries."
    lines = ["| ID | Name | Domain | Status | Zones | PE IPs | ADRs |", "|---|---|---|---|---|---:|---|"]
    for e in entries:
        lines.append(
            f"| {e.get('id','')} | {e.get('name','')} | {e.get('togaf_domain','')} | "
            f"{e.get('status','')} | {','.join(e.get('trust_zones', []))} | "
            f"{e.get('private_endpoint_ips', 0)} | {','.join(e.get('adrs', []))} |"
        )
    return "\n".join(lines)


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Manage TOGAF BDAT architecture & technology registry.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_init = sub.add_parser("init", help="Initialize a new JSON registry.")
    p_init.add_argument("registry", type=Path)
    p_init.add_argument("--project", default="Architecture Workbench")
    p_init.add_argument("--force", action="store_true")

    p_up = sub.add_parser("upsert", help="Add or update a registry entry.")
    p_up.add_argument("registry", type=Path)
    p_up.add_argument("--id", required=True)
    p_up.add_argument("--name")
    p_up.add_argument("--domain", choices=VALID_DOMAINS)
    p_up.add_argument("--category")
    p_up.add_argument("--vendor")
    p_up.add_argument("--plane")
    p_up.add_argument("--status", choices=VALID_STATUSES)
    p_up.add_argument("--zones")
    p_up.add_argument("--adrs")
    p_up.add_argument("--work-packages")
    p_up.add_argument("--pe-ips", type=int)
    p_up.add_argument("--residency")
    p_up.add_argument("--owner")
    p_up.add_argument("--notes")

    p_q = sub.add_parser("query", help="Filter and display registry entries.")
    p_q.add_argument("registry", type=Path)
    p_q.add_argument("--domain")
    p_q.add_argument("--status")
    p_q.add_argument("--zone")
    p_q.add_argument("--adr")
    p_q.add_argument("--work-package")
    p_q.add_argument("--search")
    p_q.add_argument("--format", choices=("table", "json"), default="table")

    p_val = sub.add_parser("validate", help="Validate registry schema and invariants.")
    p_val.add_argument("registry", type=Path)

    p_csv = sub.add_parser("export-csv", help="Export registry entries to CSV.")
    p_csv.add_argument("registry", type=Path)
    p_csv.add_argument("output_csv", type=Path)

    p_sum = sub.add_parser("summary", help="Print registry counts and PE IP footprint.")
    p_sum.add_argument("registry", type=Path)

    args = parser.parse_args(argv)

    if args.cmd == "init":
        init_registry(args.registry, args.project, args.force)
        print(f"Initialized registry at {args.registry}")
        return 0

    data = load_registry(args.registry)

    if args.cmd == "upsert":
        entry = upsert_entry(
            data,
            entry_id=args.id,
            name=args.name,
            togaf_domain=args.domain,
            category=args.category,
            vendor_or_service=args.vendor,
            plane=args.plane,
            status=args.status,
            trust_zones=_split_csv_arg(args.zones) if args.zones is not None else None,
            adrs=_split_csv_arg(args.adrs) if args.adrs is not None else None,
            work_packages=_split_csv_arg(args.work_packages) if args.work_packages is not None else None,
            private_endpoint_ips=args.pe_ips,
            residency=args.residency,
            owner=args.owner,
            notes=args.notes,
        )
        errs = validate_registry(data)
        if errs:
            for err in errs:
                print(f"ERROR: {err}", file=sys.stderr)
            return 1
        save_registry(args.registry, data)
        print(json.dumps(entry, indent=2))
        return 0

    if args.cmd == "query":
        hits = query_entries(
            data,
            domain=args.domain,
            status=args.status,
            zone=args.zone,
            adr=args.adr,
            work_package=args.work_package,
            search=args.search,
        )
        if args.format == "json":
            print(json.dumps(hits, indent=2))
        else:
            print(_format_table(hits))
        return 0

    if args.cmd == "validate":
        errs = validate_registry(data)
        if errs:
            for err in errs:
                print(f"ERROR: {err}", file=sys.stderr)
            return 1
        print(f"VALID: {len(data.get('entries', []))} entries in {args.registry}")
        return 0

    if args.cmd == "export-csv":
        count = export_csv(data, args.output_csv)
        print(f"Exported {count} entries to {args.output_csv}")
        return 0

    if args.cmd == "summary":
        print(json.dumps(summarize_registry(data), indent=2))
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
