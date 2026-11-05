---
name: managing-team-skills-and-allocation
description: "Guides users interactively to manage team members, their current skills, proficiency levels, learning/growth interests, and work allocations linked to the committed Work Inventory and Business Capabilities, producing Markdown registers, Excel/CSV trackers, and Mermaid workload visuals. Use when mapping team skills and interests, tracking who is assigned to which projects or operational work, detecting key-person bottlenecks, or generating team workload visuals and spreadsheets."
---

# Managing team skills and allocation

Guides users interactively to map **team members (`MEM-X`), their current skills/capabilities, career/learning interests, and active work assignments** linked to the Committed work inventory (`WORK-X`) and Business capabilities (`CAP-X`), with exports to Markdown, Excel-ready CSV, and Mermaid workload visuals.

## Contents

- [Constraints](#constraints)
- [Quick start](#quick-start)
- [Workflow](#workflow)
- [Verification](#verification)
- [References](#references)

## Constraints

1. **Interactive HITL pacing & format choice**: Open with a numbered action menu, ask 1–2 plain-language questions at a time, and let the user choose their preferred output format (`1. Markdown register + Mermaid workload visuals (Recommended)`, `2. Excel-ready CSV work & skills tracker`, `3. Both`).
2. **Only assign committed work**: Active work allocations must reference verified items from the Committed work inventory (`WORK-X`). Unapproved ideas (`IDEA-X`) may be linked *only* as **Growth / exploration interests**, never as active project assignments.
3. **Constructive developmental framing**: Frame skills and capacity data to identify growth opportunities, co-mentoring pairs, and single-point-of-failure ("bus factor") risks—never as punitive surveillance.
4. **B.C. Government Design System style**: Use sentence case for headings and labels, plain language, zero emoji, and confirm via a recap gate before saving.

## Quick start

1. Read [team-skills-and-workload-guide.md](references/team-skills-and-workload-guide.md) and present the **4-option Team & Work Tracker Menu**.
2. Capture or update team skills, interests, and `WORK-X` assignments interactively with a recap confirmation gate.
3. Generate [team-skills-and-allocation-register.md](assets/templates/team-skills-and-allocation-register.md) (with embedded Mermaid visuals) and/or `assets/templates/team-work-tracker.csv` for Microsoft Excel or SharePoint.

## Workflow

1. **Interactive Roster & Skills Capture**: Ask who is on the team (`MEM-X`), their primary role, their current strengths/capabilities (`CAP-X`), and what areas or skills they are interested in developing.
2. **Map Work Assignments (`MEM-X` $\leftrightarrow$ `WORK-X`)**: Link each person's active projects, experiments, and operational duties from `managing-work-inventory` with their role (`Lead / Owner`, `Contributor`, `Backup / Reviewer`) and estimated capacity split (`Operational %` vs. `Project / Strategic %`).
3. **Run Capacity & Coverage Diagnostics**: Surface key-person dependencies (capabilities or critical work items with only 1 person and no backup), overloaded owners, and matches between a team member's growth interest and a branch capability gap.
4. **Recap Gate & Multi-Format Export**: Confirm the summary, save to `strategy/11-team-skills-and-allocation.md` ([team-skills-and-allocation-register.md](assets/templates/team-skills-and-allocation-register.md)) and/or `assets/templates/team-work-tracker.csv`, and render Mermaid person-to-work diagrams.

## Verification

Check outputs against [acceptance-criteria.md](references/acceptance-criteria.md):
- Every work assignment links to a committed `WORK-X` item (or flags unverified work for triage).
- Includes both current proficiency and growth interests, plus key-person risk diagnostics and Mermaid visuals.

## References

- Methodology & interactive prompts: [team-skills-and-workload-guide.md](references/team-skills-and-workload-guide.md)
- Templates: [team-skills-and-allocation-register.md](assets/templates/team-skills-and-allocation-register.md) • `assets/templates/team-work-tracker.csv`
- Quality gate: [acceptance-criteria.md](references/acceptance-criteria.md)
