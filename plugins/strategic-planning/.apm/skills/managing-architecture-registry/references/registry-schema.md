# Architecture Registry Schema Reference

## File format
JSON (`architecture-registry.json`) is the canonical source of truth, with lossless CSV export (`export-csv`) for spreadsheet review.

## Top-level fields
- `schema_version`: `"1.0"`
- `project`: Project or initiative name
- `updated_at`: UTC ISO-8601 timestamp (`YYYY-MM-DDTHH:MM:SSZ`)
- `entries`: List of component objects

## Entry fields

| Field | Required | Allowed values / format | Purpose |
|---|---|---|---|
| `id` | Yes | `TECH-NNN` (unique) | Stable component identifier |
| `name` | Yes | String | Human-readable component name |
| `togaf_domain` | Yes | `Business` \| `Data` \| `Application` \| `Technology` | TOGAF BDAT alignment |
| `category` | No | String | Functional grouping (e.g., Vector Search, AI Gateway) |
| `vendor_or_service` | No | String | Product or Azure service name |
| `plane` | No | String | Architectural plane (Experience, Request Path, Data, Control) |
| `status` | Yes | `target` \| `spike_verify` \| `plan_b` \| `deferred` \| `deprecated` | Current lifecycle/decision posture |
| `trust_zones` | No | List (`Zone 1`, `Zone 2`, `Zone 3`) | Applicable trust boundaries |
| `adrs` | No | List (`ADR-NNN`) | Governing Architecture Decision Records |
| `work_packages` | No | List (`WP-NN`) | Linked TOGAF implementation work packages |
| `private_endpoint_ips` | No | Integer >= 0 | Private Endpoint IP count for `/24` subnet budgeting |
| `residency` | No | String | Region/geography (e.g., `Canada Central`, `Entra Tenant Geo`) |
| `owner` | No | String | Accountable team or role |
| `notes` | No | String | Constraints, Plan B notes, or verification status |
