---
name: planning-business-capabilities
description: "Guides users interactively to translate strategic vision and outcome objectives into end-to-end service value streams (VST-X) and required organizational capabilities (CAP-X), assessing current versus target capability maturity and 5-pillar gaps. Use when asking what the organization or branch must be able to do to achieve its vision, mapping business capabilities or value streams, or identifying capability gaps before selecting initiatives. Not for evaluating individual ideas (use managing-idea-inventory)."
---

# Planning business capabilities

Guides users interactively to bridge the gap between strategic vision/objectives and projects by mapping **end-to-end value streams (`VST-X`)**, defining **what the organization or branch must be able to do (`CAP-X`)**, and assessing maturity gaps across people, process, information, technology, and governance.

## Contents

- [Constraints](#constraints)
- [Quick start](#quick-start)
- [Workflow](#workflow)
- [Verification](#verification)
- [References](#references)

## Constraints

1. **Interactive plain-language facilitation**: Avoid heavy enterprise-architecture jargon. Ask *"What end-to-end service journey does this support, and what must our team reliably be able to do to achieve Objective X?"* and offer a numbered list of candidate value streams and capabilities for the user to confirm or edit.
2. **Capabilities define *what*, not *how***: Name capabilities as enduring organizational abilities (`CAP-X`) paired with value-stream stages (`VST-X`), never as software tools, org-chart teams, or one-off projects.
3. **Five-pillar assessment**: Guide the user to check **People/skills, Process, Information/data, Technology, and Policy/governance** for every capability gap.
4. **B.C. Government Design System style**: Use sentence case for headings and labels, plain language, zero emoji, and confirm via a recap gate before writing files.

## Quick start

1. Read [capability-based-planning-guide.md](references/capability-based-planning-guide.md) for conversational facilitation prompts, TOGAF Phase B value-stream cross-mapping, and the 0–5 maturity scale.
2. Propose candidate value streams (`VST-X`) and capabilities (`CAP-X`) linked to the user's strategic objectives (`OBJ-X`), walk through maturity scoring interactively, and populate [capability-map-and-gaps.md](assets/templates/capability-map-and-gaps.md).

## Workflow

1. **Map Value Streams & Candidate Capabilities**: Based on the team's objectives (`OBJ-X`), identify the high-level value stream stages (`VST-X`) and present 4–8 plain-language candidate business capabilities (`CAP-X`) for the user to keep, rename, or add.
2. **Interactive Maturity Rating (0–5)**: Present a simple 0–5 maturity table (`0: Absent` to `5: Optimized`) and ask the user to rate `Current` vs. `Target` maturity for their top capabilities.
3. **Five-Pillar Gap Walk-Through**: For high-priority gaps, ask what is missing across People/skills, Process, Information/data, Technology, and Policy/governance.
4. **Recap Gate & Hand Off**: Present the capability summary for confirmation (`yes / adjust`), save to [capability-map-and-gaps.md](assets/templates/capability-map-and-gaps.md), and offer a numbered menu to move to `managing-idea-inventory` or `aligning-strategy-and-portfolio`.

## Verification

Check outputs against [acceptance-criteria.md](references/acceptance-criteria.md):
- Candidate capabilities are proposed and refined interactively with a recap confirmation gate.
- Zero capabilities are named after software products or temporary projects.

## References

- Methodology & facilitation prompts: [capability-based-planning-guide.md](references/capability-based-planning-guide.md)
- Template: [capability-map-and-gaps.md](assets/templates/capability-map-and-gaps.md)
- Quality gate: [acceptance-criteria.md](references/acceptance-criteria.md)
