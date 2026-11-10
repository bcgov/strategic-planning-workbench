# AGENTS.md

## Overview
`strategic-planning-workbench` is an APM-native collection of interactive agent plugins, skills, rules, and templates for public-sector and organizational strategic planning, tailored for non-developer and technical teams in the Province of British Columbia, Ministry of Attorney General, Court Services Branch (CSB), Division, and Team levels.

## Architecture & Layout
High-level architectural pointers. For full layout, multi-tier hierarchy, and living register flows, see [architecture.md](architecture.md).
- `plugins/strategic-planning/.apm/skills/`: Five self-contained interactive skills: strategy and item management (`developing-and-managing-strategy`), triage (`triaging-new-items`), team skills and allocation, logic models, and B.C. Gov visual rendering.
- `plugins/strategic-planning/rules/` & `.agent/rules/`: Non-negotiable governance invariants.
- `strategy/` (or user-selected `~/strategic-planning-outputs/<team>/strategy/`): Default workspace directory where living team strategic registers (`00`–`11`), inventories, and visual outputs are persisted.

## Core Commands
Essential commands for validating plugins, skills, rules, and APM packaging:
```bash
apm compile --validate
python -m pytest
python plugins/strategic-planning/.apm/skills/developing-and-managing-strategy/scripts/test_investment_scripts.py
```

## Non-Negotiable Rules / Invariants
1. **Multi-Tier Mandate & Evidence Integrity**: Agents MUST trace team objectives upward through Division, Branch (CSB), Ministry, and Provincial mandates and NEVER fabricate evidence or baselines ([evidence-and-hierarchy-alignment.md](.agent/rules/evidence-and-hierarchy-alignment.md)).
2. **Interactive Plain-Language Pacing**: Agents MUST guide users interactively with numbered option menus, 1–2 plain-language questions per turn, progress indicators, "I don't know" accepted as an open item, and a recap confirmation gate before saving (each skill carries `references/guided-interaction.md`) ([evidence-and-hierarchy-alignment.md](.agent/rules/evidence-and-hierarchy-alignment.md)).
3. **B.C. Government Design System Style**: All outputs MUST use B.C. Government sentence case, plain language, zero emoji, and official B.C. Design System v5 tokens ([evidence-and-hierarchy-alignment.md](.agent/rules/evidence-and-hierarchy-alignment.md)).
4. **Three-Inventory Separation**: Agents MUST keep Strategic Vision, the Idea Inventory, and the Committed Work Inventory strictly separate and NEVER treat unapproved ideas as committed work. Work is committed only with a named sponsor and approval date, a named owner and confirmed capacity; approval without capacity is a decision gate flagged `Capacity unconfirmed` ([three-inventory-separation.md](.agent/rules/three-inventory-separation.md)).
5. **Non-Destructive Register Updates**: Agents MUST preserve stable record IDs and decision histories when importing evolving priorities, new ideas, or work progress, edit only the register sections their mode owns, and record changes that touch another owner's records as `Open follow-ups` in `00` ([three-inventory-separation.md](.agent/rules/three-inventory-separation.md)).
6. **APM-Native Packaging Hygiene**: All plugin skills MUST reside in `.apm/skills/` with zero raw symlinks, dual manifests, and `SKILL.md` as a router under 80 lines with depth in `references/` ([apm-plugin-hygiene.md](.agent/rules/apm-plugin-hygiene.md)).
7. **Feature-Branch PR & Doc Synchronization**: `main` is branch-protected; all changes MUST use a feature branch (`feat/*`, `fix/*`, `docs/*`) and Pull Request, keeping `AGENTS.md`, [architecture.md](architecture.md), and [README.md](README.md) synchronized ([apm-plugin-hygiene.md](.agent/rules/apm-plugin-hygiene.md)).

## On-Demand Skills & Reference Index
- Read [architecture.md](architecture.md) when orienting to the 5-tier B.C. Gov / CSB hierarchy, the TOGAF ADM stage mapping, the 12 living strategy files (`00`–`11`) and their section ownership, skill routing, or data flows.
- Read [docs/governance.md](docs/governance.md) when reviewing repository packaging and governance policies.
- Use `developing-and-managing-strategy` for the main workflow. On first use it asks where to save outputs and runs the strategic interview; afterwards it resumes and revisits the plan. Modes: Cycle, Context, Vision, Capabilities (establish direction); Update (change direction, dispensations `DSP-X`, TOGAF Phase H); Ideas (`IDEA-X`), Work (`WORK-X`), Risks (`RSK-X`), Score (Value/ROI vs. Ability to Deliver with 4-quadrant charts and JSON/CSV ledgers) (manage items); Alignment (incl. `BTRA`), Measures (`MSR-X`), Roadmap (`PLT-X`, `GATE-X`), Review (review alignment and delivery). Works across Claude, Copilot, Codex, Antigravity (`agy`) and GrokBot (`grok-bot`).
- Use `triaging-new-items` when sorting a new, mixed or unclear list (meeting notes, a spreadsheet, "log this problem or risk"): it classifies by commitment state and nature (problem, driver, risk, idea, project, training, decision, blocker and more), then routes each item. Not needed for an explicit request on a named record such as "update WORK-12".
- Use `managing-team-skills-and-allocation` when mapping team member skills (`MEM-X`), growth interests, training requests, and active `WORK-X` assignments, recording capacity evidence for commitments, or exporting Excel/CSV and Mermaid workload trackers.
- Use `designing-logic-models` when constructing, stress-testing, or documenting program logic models, results chains, outcome chains, theories of change, or results frameworks connecting inputs and activities to outputs and progressive immediate, intermediate, and long-term public outcomes.
- Use `rendering-strategic-visuals-and-decks` when producing B.C. Gov Design System HTML dashboards, Mermaid roadmaps, Gantt charts, value-stream maps, or slide decks from the registers.
