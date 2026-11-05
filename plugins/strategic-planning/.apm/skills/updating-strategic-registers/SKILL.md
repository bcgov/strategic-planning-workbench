---
name: updating-strategic-registers
description: "Guides users interactively to import, capture, and incrementally update evolving strategic priorities, multi-tier org mandates (Province, Ministry, Branch, Division, Team), business drivers, stakeholders, objectives, ideas, and work progress in persistent workspace registers. Use when ingesting new meeting notes, recording evolving direction, logging progress on active initiatives, or updating any strategic register over time."
---

# Updating strategic registers

Guides users interactively to import new meeting notes, leadership communications, stakeholder updates, new ideas, or project progress into the 10 living `strategy/` registers—presenting a clear preview diff and ripple-impact check before saving.

## Contents

- [Constraints](#constraints)
- [Quick start](#quick-start)
- [Workflow](#workflow)
- [Verification](#verification)
- [References](#references)

## Constraints

1. **Interactive preview & confirmation gate**: Always show the user a plain-language summary of proposed additions, status updates, and ripple impacts, and ask for confirmation (`1. Apply all updates (Recommended)`, `2. Adjust specific items`, `3. Preview full markdown diff`) before modifying files in `strategy/`.
2. **Non-destructive updates**: Preserve existing record IDs (`MAN-X`, `OBJ-X`, `CAP-X`, `IDEA-X`, `WORK-X`, `ASM-X`, `RSK-X`, `MSR-X`) and append a change-log entry.
3. **Five-tier hierarchy tagging**: Classify upstream direction across Tier 1 (Province of BC), Tier 2 (Ministry of Attorney General), Tier 3 (Court Services Branch), Tier 4 (Division), and Tier 5 (Team).
4. **B.C. Government Design System style**: Use sentence case for headings and labels, plain language, and zero emoji.

## Quick start

1. Read [living-register-update-guide.md](references/living-register-update-guide.md) and [bc-gov-csb-hierarchy-reference.md](references/bc-gov-csb-hierarchy-reference.md).
2. Ask what new information the user wants to import or update (or offer a numbered menu of the 10 registers).
3. Present the proposed updates and ripple impacts for confirmation, then update the target `strategy/` registers, [org-hierarchy-and-mandates.md](assets/templates/org-hierarchy-and-mandates.md), and [register-update-changelog.md](assets/templates/register-update-changelog.md).

## Workflow

1. **Interactive Intake**: Ask the user to paste their notes/updates or select which register area changed (1. Leadership/org mandates & drivers, 2. Stakeholders, 3. Vision/objectives/benefits, 4. Capabilities, 5. Ideas, 6. Active work progress/blockers, 7. Assumptions/risks/measures).
2. **Parse & Map to Registers**: Classify each extracted item by organizational tier (Province $\rightarrow$ AG $\rightarrow$ CSB $\rightarrow$ Division $\rightarrow$ Team) and target register (`strategy/01`–`strategy/10`), asking 1–2 clarifying questions if an item's status (`Confirmed` vs. `Interpreted`, or `Idea` vs. `Committed Work`) is ambiguous.
3. **Present Ripple-Impact Recap Gate**: Show how the changes affect linked objectives, capabilities, ideas, or active work, and wait for user confirmation.
4. **Save & Chain**: Write the confirmed updates, log the entry in `strategy/changelog.md`, and offer next steps (e.g., refresh visuals via `rendering-strategic-visuals-and-decks`).

## Verification

Check all updates against [acceptance-criteria.md](references/acceptance-criteria.md):
- Presents a recap confirmation gate and ripple-impact summary before writing to disk.
- Preserves existing record IDs and uses B.C. Government sentence case.

## References

- Methodology & hierarchy: [living-register-update-guide.md](references/living-register-update-guide.md) • [bc-gov-csb-hierarchy-reference.md](references/bc-gov-csb-hierarchy-reference.md)
- Templates: [org-hierarchy-and-mandates.md](assets/templates/org-hierarchy-and-mandates.md) • [register-update-changelog.md](assets/templates/register-update-changelog.md)
- Quality gate: [acceptance-criteria.md](references/acceptance-criteria.md)
