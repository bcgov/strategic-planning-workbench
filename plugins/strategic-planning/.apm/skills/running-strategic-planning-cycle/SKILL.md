---
name: running-strategic-planning-cycle
description: "Orchestrates the end-to-end strategic planning cycle for business users: checks existing strategy/ registers, presents a plain-language entry menu (Top-Down from leadership direction, Bottom-Up from existing projects/ideas, Resume where we left off, Ingest meeting notes, or Fast-Track briefing), coaches across TOGAF ADM-aligned stages, maintains strategy/00-planning-session-status.md, and routes to the right specialist skill. Use when the user asks 'where do we start', 'help us build our strategy', 'where did we leave off', 'walk me through strategic planning', or 'what is missing in our strategy'."
---

# Running strategic planning cycle

Acts as the front-door navigator, TOGAF ADM cycle coach, and session state tracker for the Strategic Planning Workbench. Helps non-developer business users start, resume, or audit their branch, division, or team strategy and routes each step to the right specialist skill.

## Contents

- [Constraints](#constraints)
- [Quick start](#quick-start)
- [Workflow](#workflow)
- [Verification](#verification)
- [References](#references)

## Constraints

1. **Interactive plain-language coaching**: Never overwhelm the user with TOGAF jargon or all 11 templates at once. Scan `strategy/` first, report what exists in plain language, and present the 5-option entry menu from [strategic-planning-cycle-and-togaf-adm-guide.md](references/strategic-planning-cycle-and-togaf-adm-guide.md).
2. **Maintain session state (`strategy/00-planning-session-status.md`)**: Record completed registers, current TOGAF ADM stage, open assumptions (`ASM-X`), pending idea gates (`IDEA-X`), active dispensations (`DSP-X`), and the recommended next 15-minute step.
3. **Gentle phase-gate coaching**: If a user asks for a downstream output (such as a roadmap or slide deck) before minimum upstream inputs exist, offer a 3-question fast-track rather than refusing or inventing strategy.
4. **B.C. Government Design System style**: Use sentence case for headings and labels, calm direct language, zero emoji, and `<br>` tags inside Mermaid boxes.

## Quick start

1. Read [strategic-planning-cycle-and-togaf-adm-guide.md](references/strategic-planning-cycle-and-togaf-adm-guide.md) and inspect `strategy/00-planning-session-status.md` plus `strategy/01` through `11`.
2. Present a brief readiness snapshot and the 5-option entry menu so the user can choose Top-Down, Bottom-Up/Middle-Out, Resume, Note Ingestion, or Fast-Track Briefing.
3. Update [planning-session-status.md](assets/templates/planning-session-status.md) (`strategy/00-planning-session-status.md`) and route to the selected specialist skill.

## Workflow

1. **Readiness Scan**: Check which files in `strategy/` (`00`–`11`) exist and summarize their state (`Not started`, `Draft`, `Baseline confirmed`).
2. **Interactive Entry Menu**: Present the 5 plain-language entry options (1. Top-Down from leadership direction, 2. Bottom-Up from current projects/team workload/ideas, 3. Resume & gap check, 4. Import meeting notes or changes, 5. Fast-track executive briefing/visuals).
3. **Stage Routing & TOGAF ADM Coaching**: Guide the user through the selected stage (Stage 1 Context $\rightarrow$ Stage 2 Vision & Principles $\rightarrow$ Stage 3 Value Streams & Capabilities $\rightarrow$ Stage 4 Ideas, Work & Team $\rightarrow$ Stage 5 Alignment, Readiness & Plateau Roadmap $\rightarrow$ Stage 6 Visuals & Living Governance).
4. **Update Session Scorecard**: Save progress and the next recommended action in `strategy/00-planning-session-status.md` after every stage confirmation gate.

## Verification

Check outputs against [acceptance-criteria.md](references/acceptance-criteria.md):
- Scans `strategy/` before asking questions and presents the 5-option entry menu in plain language.
- Keeps `strategy/00-planning-session-status.md` synchronized with the 11 registers using B.C. Government sentence case.

## References

- Cycle navigation & TOGAF ADM mapping: [strategic-planning-cycle-and-togaf-adm-guide.md](references/strategic-planning-cycle-and-togaf-adm-guide.md)
- Session scorecard template: [planning-session-status.md](assets/templates/planning-session-status.md)
- Quality gate: [acceptance-criteria.md](references/acceptance-criteria.md)
