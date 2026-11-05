---
name: sequencing-roadmaps-and-measures
description: "Guides users interactively to organize committed initiatives into Now/Next/Later or Three Horizons roadmaps with TOGAF Phase E/F Transition State plateaus (PLT-X), dependencies, and decision gates, and define outcome measures, leading indicators, and guardrails. Use when creating or updating a strategic roadmap, defining transition states, establishing OKRs and success measures, or setting review cadences. Not for detailed project schedules or feature backlogs."
---

# Sequencing roadmaps and measures

Guides users interactively to sequence **committed initiatives** (`WORK-X`), **TOGAF Transition State plateaus** (`PLT-X`), and candidate decision gates (`IDEA-X`) into strategic horizons (`Now / Next / Later` or `Three Horizons`) and co-design outcome measures, leading indicators, and quality/fairness guardrails.

## Contents

- [Constraints](#constraints)
- [Quick start](#quick-start)
- [Workflow](#workflow)
- [Verification](#verification)
- [References](#references)

## Constraints

1. **Interactive sequencing & measure design**: Offer a numbered option menu for roadmap format (`1. Now / Next / Later (Recommended)`, `2. Three Horizons`, `3. Fiscal quarter view`) and co-design transition states (`PLT-X`) and measures 1–2 objectives at a time.
2. **Never mix unapproved ideas into committed horizons**: Only `WORK-X` items appear as committed roadmap initiatives; `IDEA-X` items appear strictly as **Decision / validation gates**.
3. **Balanced measurement**: Pair every outcome or speed measure with a **guardrail measure** (procedural fairness, privacy compliance, accuracy, staff workload) and mark missing baselines honestly as `Baseline needed`.
4. **B.C. Government Design System style**: Use sentence case for headings and labels, plain language, zero emoji, and confirm via a recap gate before saving.

## Quick start

1. Read [roadmapping-and-measures-guide.md](references/roadmapping-and-measures-guide.md) and ask the user to choose their preferred horizon view and review cadence.
2. Walk through transition state plateaus (`PLT-X`), prerequisite dependencies, and decision gates interactively, then populate [strategic-roadmap.md](assets/templates/strategic-roadmap.md) and [success-measures-register.md](assets/templates/success-measures-register.md).

## Workflow

1. **Interactive Horizon & Plateau Placement**: Propose an initial `Now / Next / Later` grouping of committed `WORK-X` initiatives and define the **Transition State (Plateau `PLT-X`)** achieved at the end of each horizon; ask the user what to shift based on team capacity.
2. **Place Candidate Decision Gates**: Ask where unvalidated assumptions (`ASM-X`) and candidate ideas (`IDEA-X`) need leadership decision checkpoints (`GATE-X`).
3. **Co-Design the Measures Triad**: For each objective (`OBJ-X`), propose 1 Outcome measure, 1–2 Leading indicators, and 1 Guardrail measure; ask whether baseline data exists today or should be tagged `Baseline needed`.
4. **Recap Gate & Hand Off**: Confirm the roadmap and measures summary, save to `strategy/10-roadmap-and-success-measures.md`, and offer to generate Mermaid visuals or presentations via `rendering-strategic-visuals-and-decks`.

## Verification

Check outputs against [acceptance-criteria.md](references/acceptance-criteria.md):
- Committed `WORK-X` initiatives and `IDEA-X` decision gates are clearly separated and confirmed interactively.
- Every objective includes Outcome, Leading, and Guardrail measures in B.C. Government sentence case.

## References

- Methodology & interactive prompts: [roadmapping-and-measures-guide.md](references/roadmapping-and-measures-guide.md)
- Templates: [strategic-roadmap.md](assets/templates/strategic-roadmap.md) • [success-measures-register.md](assets/templates/success-measures-register.md)
- Quality gate: [acceptance-criteria.md](references/acceptance-criteria.md)
