---
name: developing-solution-architecture
description: "Scaffolds, documents, and validates solution and enterprise architecture workbenches (TOGAF BDAT views, ADRs, quality and runtime scenarios, interface contracts, and work packages). Use when creating a new architecture repository, onboarding an existing architecture workbench, writing ADRs or quality/runtime scenarios, or running structure and ADR/WP coherence checks. Not for organizational strategy registers 00-11 (use developing-and-managing-strategy), technology inventory JSON CRUD (use managing-architecture-registry), audience HTML/PPTX rendering (use rendering-strategic-visuals-and-decks), or Azure/OpenShift/GitHub Actions CI/CD (use bcgov-devops-platform-workbench)."
---

# Developing solution architecture

Guides architects and teams through scaffolding, documenting, and validating `solution-architecture`, `strategy-and-architecture`, and `enterprise-architecture` repositories using TOGAF BDAT, ADRs, and coherence checks.

## Contents

- [Constraints](#constraints) • [Modes](#modes) • [Quick start](#quick-start) • [Workflow](#workflow) • [Related skills](#related-skills) • [Verification](#verification) • [References](#references)

## Constraints

1. **Guided interaction**: Follow [guided-interaction.md](references/guided-interaction.md): open with a numbered menu, ask 1–2 questions per turn with a recommended default, accept "I don't know" as an open item, and confirm a recap before writing.
2. **Naming & separation**: Reserve `capabilities/` for Business Capability Maps; put APIs, schemas, and agent manifests in `contracts/`. Keep the **model** (`architecture-registry.json`, `contracts/`, `adrs/`, `work-packages/`) separate from **views** (`diagrams/`, `deliverables/`).
3. **ADR discipline**: Every `Proposed` ADR requires an `Owner` and `Target review date` so decisions do not go stale.
4. **No platform duplication**: Delegate Azure Landing Zones, OIDC, Terraform, OpenShift Emerald, and GitHub Actions/Rulesets to `bcgov-devops-platform-workbench`.
5. **B.C. Government style**: Sentence case, plain language, zero emoji.

## Modes

| Mode | Use when | Entry point | Guide |
|---|---|---|---|
| `scaffold` | New repository or adding architecture structure | `scripts/scaffold_project_structure.py` | [project structure guide](references/project-structure-and-templates-guide.md) |
| `document` | Authoring BDAT views, ADRs, quality/runtime scenarios | `assets/templates/` | [architecture artifacts guide](references/architecture-artifacts-and-registry-guide.md) |
| `validate` | Auditing structure, links, JSON, and ADR/WP coherence | `scripts/validate_project_structure.py` | [acceptance criteria](references/acceptance-criteria.md) |

## Quick start

```bash
python3 scripts/scaffold_project_structure.py --profile solution-architecture --target <repo> --project-name "<Name>" [--with-execution] [--init-registry]
python3 scripts/validate_project_structure.py --profile auto --target <repo> [--strict-coherence]
```

Note: `--init-registry` invokes the sibling `managing-architecture-registry` skill if installed; otherwise it prints a reminder to initialize `architecture/architecture-registry.json` separately.

## Workflow

1. **Select profile & action**: Ask whether this is a new scaffold or an existing repo validation, and confirm the profile (`solution-architecture`, `strategy-and-architecture`, `enterprise-architecture`, or `strategy-only`).
2. **Scaffold or validate**: Run `scripts/scaffold_project_structure.py` (with `--dry-run` preview first) or `scripts/validate_project_structure.py`.
3. **Document & link**: Populate TOGAF BDAT views, [ADR template](assets/templates/adr-template.md), [quality scenarios](assets/templates/quality-scenarios.md), and [runtime scenarios](assets/templates/runtime-scenarios.md).
4. **Verify**: Re-run `validate_project_structure.py --strict-coherence` and check [acceptance criteria](references/acceptance-criteria.md).

## Related skills

| Need | Skill |
|---|---|
| Business strategy registers (`00`–`11`) or `strategy/` half of a hybrid repo | `developing-and-managing-strategy` |
| `architecture/architecture-registry.json` (`TECH-NNN`, CSV, Private Endpoint IPs) | `managing-architecture-registry` |
| Audience HTML briefs, logic-model cards, Mermaid packages, or decks | `rendering-strategic-visuals-and-decks` |
| Azure Landing Zones/OIDC/Terraform, OpenShift Emerald, GitHub Actions/Rulesets | `bcgov-devops-platform-workbench` |

## Verification

Run `python3 scripts/test_project_structure_scripts.py -v` and `python3 scripts/validate_project_structure.py --profile auto --target <repo> --strict-coherence`. Check [acceptance criteria](references/acceptance-criteria.md).

## References

- Guides: [project structure & templates](references/project-structure-and-templates-guide.md) • [architecture artifacts & registry](references/architecture-artifacts-and-registry-guide.md) • [guided interaction](references/guided-interaction.md)
- Templates: [adr-template.md](assets/templates/adr-template.md) • [quality-scenarios.md](assets/templates/quality-scenarios.md) • [runtime-scenarios.md](assets/templates/runtime-scenarios.md)
- Gate: [acceptance-criteria.md](references/acceptance-criteria.md)
