---
name: managing-architecture-registry
description: Manages, updates, validates, and queries an architecture and technology registry (JSON with CSV/Markdown export) aligned to TOGAF BDAT domains, trust zones, ADRs, and work packages. Use when initializing, adding, updating, querying, or auditing technology components, vector DBs, agent runtimes, or platform services in an architecture registry.
---

# Managing Architecture Registry

Maintains a project's canonical **Architecture & Technology Registry** (`architecture-registry.json`) with deterministic Python validation, querying, Private Endpoint IP footprint accounting, and CSV export.

## Contents

- [Constraints](#constraints) • [Quick start](#quick-start) • [Workflow](#workflow) • [Verification](#verification) • [References](#references)

## Constraints

1. **JSON canonical, CSV derived**: Store and edit the registry in JSON; generate CSV via `export-csv` rather than maintaining two divergent files.
2. **Stable IDs**: Use `TECH-NNN` IDs and never renumber existing entries; mark retired technologies `deprecated`.
3. **TOGAF BDAT & ADR linkage**: Every entry MUST map to a `togaf_domain` (`Business`, `Data`, `Application`, `Technology`) and `status` (`target`, `spike_verify`, `plan_b`, `deferred`, `deprecated`).
4. **Zero secrets or tenant IDs**: Never store subscription IDs, tenant IDs, IP literals, or credentials in the registry.

## Quick start

```bash
python3 scripts/managing_architecture_registry.py init <path/to/architecture-registry.json> --project "<Project Name>"
python3 scripts/managing_architecture_registry.py upsert <path/to/architecture-registry.json> --id TECH-001 --name "Azure AI Search (Zone 1)" --domain Data --status target --zones "Zone 1" --adrs "ADR-005,ADR-010" --pe-ips 1
python3 scripts/managing_architecture_registry.py query <path/to/architecture-registry.json> --domain Data --format table
python3 scripts/managing_architecture_registry.py summary <path/to/architecture-registry.json>
```

## Workflow

1. **Initialize or load**: Run `init` for a new project or `validate` on an existing `architecture-registry.json`.
2. **Upsert components**: Add or update entries with `upsert`, tagging `status` (`spike_verify` for unproven platform assumptions, `plan_b` for fallback options, `deferred` for Stage 2+/later).
3. **Query & budget**: Run `query` (by `--domain`, `--status`, `--zone`, `--adr`, `--work-package`, or `--search`) and `summary` to check total `private_endpoint_ips` against Landing Zone `/24` limits.
4. **Export**: Run `export-csv` when stakeholders need a spreadsheet view.

## Related skills

| Need | Skill |
|---|---|
| Repository scaffolding, BDAT docs, ADRs, quality/runtime scenarios, and coherence validation | `developing-solution-architecture` |
| Business strategy registers (`00`–`11`) | `developing-and-managing-strategy` |
| Audience HTML briefs, dashboards, or decks | `rendering-strategic-visuals-and-decks` |

## Verification

```bash
python3 scripts/managing_architecture_registry.py validate <path/to/architecture-registry.json>
python3 -m unittest discover -s scripts -p "test_*.py"
```

## References

- [Registry Schema](references/registry-schema.md) — JSON fields, enums, and TOGAF/ADR linkage rules.
- [Acceptance Criteria](references/acceptance-criteria.md) — validation and registry integrity gates.
