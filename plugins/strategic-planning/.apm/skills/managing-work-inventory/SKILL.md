---
name: managing-work-inventory
description: "Guides users interactively to maintain the portfolio of approved initiatives, active experiments, and operational commitments with verified sponsorship, ownership, deliverables, and linked capabilities. Use when recording committed work, auditing active projects and operational responsibilities, or promoting an approved idea into execution. Not for unapproved possibilities or proposals (use managing-idea-inventory)."
---

# Managing work inventory

Guides users interactively to maintain the **Committed work inventory** (*"What are we actually doing or committed to doing?"*), tracking approved initiatives, projects, active time-boxed experiments, and operational responsibilities.

## Contents

- [Constraints](#constraints)
- [Quick start](#quick-start)
- [Workflow](#workflow)
- [Verification](#verification)
- [References](#references)

## Constraints

1. **Interactive commitment check**: When a user lists items their team is working on, ask 1–2 clarifying questions per group to distinguish approved commitments (`WORK-X`) from unapproved ideas (`IDEA-X`) or shadow operations.
2. **Commitment verification required**: Require a confirmed sponsor, delivery owner, and capacity allocation before recording an initiative as committed work.
3. **B.C. Government Design System style**: Use sentence case for headings and table labels, plain language, zero emoji, and present a recap confirmation gate before saving.

## Quick start

1. Read [work-portfolio-guide.md](references/work-portfolio-guide.md) and offer the **Work Inventory Action Menu** (1. Catalog current projects & operational work, 2. Promote an approved idea from the Idea Inventory, 3. Update status/blockers on active work, 4. Audit for orphaned work or shadow operations).
2. Confirm the recap with the user and update [work-inventory.md](assets/templates/work-inventory.md).

## Workflow

1. **Interactive Triage (Work vs. Idea)**: Review the user's list of activities. If any item lacks approval or ownership, ask whether to keep it in `managing-idea-inventory` or flag it as a `Shadow Operation` needing governance review.
2. **Classify & Link**: Walk the user through tagging each committed item (`Initiative`, `Project`, `Product-Service`, `Experiment`, `Operational`, `Research`) and linking it to `OBJ-X` and `CAP-X`.
3. **Surface Capacity & Governance Signals**: Highlight over-committed owners, experiments running in production without support, or unaligned work items.
4. **Recap Gate & Hand Off**: Present the recap table for confirmation (`yes / adjust`), save to [work-inventory.md](assets/templates/work-inventory.md), and offer next-step options (`aligning-strategy-and-portfolio` or `sequencing-roadmaps-and-measures`).

## Verification

Check outputs against [acceptance-criteria.md](references/acceptance-criteria.md):
- Interactively separates unapproved ideas from committed work with user confirmation.
- Every `WORK-X` record includes work type, owner, sponsor, status, and B.C. Government sentence-case formatting.

## References

- Methodology & triage prompts: [work-portfolio-guide.md](references/work-portfolio-guide.md)
- Template: [work-inventory.md](assets/templates/work-inventory.md)
- Quality gate: [acceptance-criteria.md](references/acceptance-criteria.md)
