# Project Structure & Templates Guide

How `developing-solution-architecture` scaffolds new planning/architecture repositories and validates existing ones.

## 1. Choosing the Right Structure Profile (4 Canonical Types)

Research across **Markdown/Git strategic planning**, **public-sector IT governance**, **arc42**, and **TOGAF Architecture-as-Code (AaC)** shows that no single folder layout fits every engagement. Ask the user to pick one of four canonical profiles on first run:

| Profile ID | Best For | Core Layout |
|---|---|---|
| `strategy-only` | Business, operations, or branch teams running strategy, OKRs/measures, capability maps, ideas, risks, scoring, and roadmaps | `strategy/` (registers `00`–`11`, `changelog.md`, `sources/`), `README.md` |
| `solution-architecture` | Single-initiative solution or platform architecture (TOGAF BDAT + arc42 + ADRs + machine-readable contracts) | `README.md`, `AGENTS.md`, `architecture.md`, `00-start-here.md`, `architecture/`, `adrs/`, `contracts/`, `diagrams/`, `work-packages/`, `research/`, `history/` |
| `strategy-and-architecture` | Programs running **both** business strategy (`00`–`11`) and technical architecture | `strategy/` (business registers) + `architecture/`, `adrs/`, `contracts/`, `diagrams/`, `work-packages/`, `research/`, `history/` |
| `enterprise-architecture` | Ministry- or org-wide TOGAF Architecture Repository across multiple initiatives | `meta/`, `standards/`, `reference/`, `landscape/{current,target}/`, `adm-cycles/`, `README.md` |

### Optional Execution Modifier (`--with-execution`)
For `solution-architecture` and `strategy-and-architecture`, when the team is moving from architecture into Stage 0 spikes, evaluations, or infrastructure-as-code, add:
- `spikes/` — time-boxed technical/identity compatibility spikes
- `evals/` — SME evaluation sets and regression harnesses
- `infra/` — Bicep/Terraform landing-zone and gateway policies

For GitHub Actions CI/CD, Rulesets, Azure Landing Zones/OIDC/Terraform, or OpenShift Emerald deployment workflows, **do not duplicate platform templates here**—use `bcgov-devops-platform-workbench` (`managing-github-workflows`, `designing-bc-gov-azure-landing-zones`, `configuring-azure-github-oidc`, `delivering-azure-terraform`, `deploying-bc-gov-workloads`).

Additional optional architecture templates in `assets/templates/`:
- `adr-template.md` — structured ADR with `Status`, `Owner`, `Target review date`, and `Traceability`
- `quality-scenarios.md` — testable non-functional / quality attribute scenarios
- `runtime-scenarios.md` — end-to-end runtime & trust-boundary flows
- `deliverables/` — optional root folder for rendered audience briefings (HTML, PDF, PPTX)

## 2. Key Naming & Separation Rules

1. **Reserve `capabilities/` for Business Capability Maps; use `contracts/` for specs:**
   In TOGAF and strategic planning, *capabilities* means a **Business Capability Map** (what the organization does, independent of technology). Interface specifications—OpenAPI, AsyncAPI, JSON/YAML schemas, agent discovery manifests, and handoff envelopes—belong in **`contracts/`** (not `capabilities/`). The validator flags `capabilities/` as a legacy alias if used for contracts in `solution-architecture`.
2. **Keep `strategy/` and `architecture/` linked, not mixed:**
   In `strategy-and-architecture`, business registers (`00`–`11`) stay in `strategy/` while BDAT views, ADRs, and `architecture-registry.json` stay in `architecture/` and `adrs/`, linked per [architecture-artifacts-and-registry-guide.md](architecture-artifacts-and-registry-guide.md).
3. **Text-first diagrams and PR governance:**
   Prefer Mermaid (`.mmd`) or PlantUML in `diagrams/` so diffs are reviewable in Pull Requests.

## 3. Interactive First-Run Questions

Ask 1–2 questions per turn with recommended defaults before creating any files:

1. **Engagement type:**
   - `1. General strategic planning (Recommended for business/ops teams)` → `strategy-only`
   - `2. Solution / platform architecture workbench` → `solution-architecture`
   - `3. Hybrid: Business strategy + Solution architecture` → `strategy-and-architecture`
   - `4. Org-wide Enterprise Architecture repository (TOGAF)` → `enterprise-architecture`
2. **New project or existing repository?**
   - `1. New project (scaffold structure)` → run `scaffold_project_structure.py`
   - `2. Existing repo (validate & report gaps without overwriting)` → run `validate_project_structure.py`
3. **Include Stage 0 execution folders? *(only for profiles 2 or 3)***
   - `1. Architecture & planning only (Recommended)`
   - `2. Include spikes/, evals/, and infra/` (`--with-execution`)

## 4. Running the Scripts

```bash
# Preview scaffolding without writing files
python3 scripts/scaffold_project_structure.py --profile solution-architecture --target /path/to/repo --project-name "My Initiative" --dry-run

# Scaffold a new project (and optionally initialize architecture-registry.json)
python3 scripts/scaffold_project_structure.py --profile solution-architecture --target /path/to/repo --project-name "My Initiative" --init-registry

# Validate an existing repository (read-only)
python3 scripts/validate_project_structure.py --profile solution-architecture --target /path/to/repo
```
