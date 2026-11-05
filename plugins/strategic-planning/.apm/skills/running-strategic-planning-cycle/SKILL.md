---
name: running-strategic-planning-cycle
description: "Orchestrates the end-to-end strategic planning cycle for business users: confirms where strategy outputs and source documents live, checks existing strategy/ registers, presents a plain-language entry menu (Top-Down, Bottom-Up, Resume/Revisit, Import notes, or Fast-Track briefing), coaches across TOGAF ADM-aligned stages, maintains 00-planning-session-status.md, and routes to the right specialist skill. Use when the user asks 'where do we start', 'help us build our strategy', 'where did we leave off', 'revisit or update our plan', or 'what is missing in our strategy'."
---

# Running strategic planning cycle

Acts as the front-door navigator, TOGAF ADM cycle coach, and session state tracker for the Strategic Planning Workbench. Helps non-developer business users start, resume, revisit, or audit their branch, division, or team strategy and routes each step to the right specialist skill.

## Contents

- [Constraints](#constraints)
- [Quick start](#quick-start)
- [Workflow](#workflow)
- [Verification](#verification)
- [References](#references)

## Constraints

1. **Confirm output folder & source docs first**: Before reading or writing files, ask the user where to store their strategy outputs—offering `1. Dedicated user folder (e.g., C:\Users\<username>\strategic-planning-outputs\<team-name>\strategy\ or ~/strategic-planning-outputs/<team-name>/strategy/) (Recommended)`, `2. Current workspace (./strategy/)`, or `3. Custom path`—and ask where any existing source documents/notes are located ([revisiting-and-updating-plans-guide.md](references/revisiting-and-updating-plans-guide.md)).
2. **Interactive plain-language coaching**: Scan the chosen output directory first, report what exists in plain language, and present the 5-option entry menu from [strategic-planning-cycle-and-togaf-adm-guide.md](references/strategic-planning-cycle-and-togaf-adm-guide.md) (or the 4-option revisit sub-menu in [revisiting-and-updating-plans-guide.md](references/revisiting-and-updating-plans-guide.md) when revisiting an existing plan).
3. **Maintain session state (`00-planning-session-status.md`)**: Record the active output directory path, source documents path, completed registers, current TOGAF ADM stage, open assumptions (`ASM-X`), pending idea gates (`IDEA-X`), active dispensations (`DSP-X`), and next 15-minute step.
4. **Gentle phase-gate coaching & B.C. Gov style**: Offer a 3-question fast-track if downstream visuals are requested early, and use B.C. Government sentence case, zero emoji, and `<br>` tags inside Mermaid boxes.

## Quick start

1. Read [strategic-planning-cycle-and-togaf-adm-guide.md](references/strategic-planning-cycle-and-togaf-adm-guide.md) and [revisiting-and-updating-plans-guide.md](references/revisiting-and-updating-plans-guide.md).
2. Confirm the user's output folder path (defaulting to `C:\Users\<username>\strategic-planning-outputs\<team-name>\strategy\` or `./strategy/`) and source documents location, then inspect `00-planning-session-status.md` and registers `01`–`11`.
3. Present a brief readiness snapshot and the 5-option entry menu (or 4-option revisit menu), update [planning-session-status.md](assets/templates/planning-session-status.md), and route to the selected specialist skill.

## Workflow

1. **Workspace & Document Path Check**: Ask where strategy outputs should be saved (`~/strategic-planning-outputs/<team>/strategy/`, `./strategy/`, or custom path) and where existing reference docs live.
2. **Readiness Scan & Entry Menu**: Check which files (`00`–`11`) exist in the target output directory and present the 5 plain-language entry options (or the 4 revisit cadences in [revisiting-and-updating-plans-guide.md](references/revisiting-and-updating-plans-guide.md)).
3. **Stage Routing & TOGAF ADM Coaching**: Guide the user through the selected stage or revisit workflow and save progress in `00-planning-session-status.md` after every confirmation gate.

## Verification

Check outputs against [acceptance-criteria.md](references/acceptance-criteria.md):
- Confirms output directory and source document paths before writing files, and presents the plain-language entry or revisit menu.
- Keeps `00-planning-session-status.md` synchronized with the 11 registers using B.C. Government sentence case.

## References

- Cycle navigation & TOGAF ADM mapping: [strategic-planning-cycle-and-togaf-adm-guide.md](references/strategic-planning-cycle-and-togaf-adm-guide.md) • [revisiting-and-updating-plans-guide.md](references/revisiting-and-updating-plans-guide.md) • [grokbot-and-chat-agent-guide.md](references/grokbot-and-chat-agent-guide.md)
- Session scorecard template: [planning-session-status.md](assets/templates/planning-session-status.md)
- Quality gate: [acceptance-criteria.md](references/acceptance-criteria.md)
