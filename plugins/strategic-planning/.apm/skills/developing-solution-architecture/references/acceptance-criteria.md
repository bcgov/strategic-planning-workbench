# Acceptance criteria: `developing-solution-architecture`

## Mandatory quality gates

1. **Profile & boundary integrity**:
   - **Pass**: Uses the selected canonical profile (`solution-architecture`, `strategy-and-architecture`, `enterprise-architecture`, or `strategy-only`), keeps interface specs in `contracts/` (not `capabilities/`), and keeps `strategy/` and `architecture/` linked rather than mixed.
   - **Fail**: Places OpenAPI/YAML contracts under `capabilities/` or mixes strategy registers `00`–`11` into `architecture/`.
2. **Coherence & link validation**:
   - **Pass**: `validate_project_structure.py` reports `PASS` with zero broken relative links, zero invalid JSON files, and zero `Proposed` ADRs missing `Owner` or `Target review date`.
   - **Fail**: Broken Markdown links, invalid JSON, or stale `Proposed` ADRs without owner/review date.
3. **Model vs. views & platform separation**:
   - **Pass**: Authoritative model artifacts (`architecture-registry.json`, `contracts/`, `adrs/`, `work-packages/`) stay separate from `diagrams/` and `deliverables/`, and platform/CI/CD details delegate to `bcgov-devops-platform-workbench`.
   - **Fail**: Duplicates GitHub Actions, Terraform, or OpenShift deployment templates inside the planning workbench.
