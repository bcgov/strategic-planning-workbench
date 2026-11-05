# AGENTS.md

## Overview
`strategic-planning-workbench` is an APM-native collection of interactive agent plugins, skills, rules, and templates for public-sector and organizational strategic planning, tailored for non-developer and technical teams in the Province of British Columbia, Ministry of Attorney General, Court Services Branch (CSB), Division, and Team levels.

## Architecture & Layout
High-level architectural pointers. For full layout, multi-tier hierarchy, and living register flows, see [architecture.md](architecture.md).
- `plugins/strategic-planning/.apm/skills/`: Self-contained interactive strategic planning, register update, and B.C. Gov visual rendering skills.
- `plugins/strategic-planning/rules/` & `.agent/rules/`: Non-negotiable governance invariants.
- `strategy/` (or user-selected `~/strategic-planning-outputs/<team>/strategy/`): Default workspace directory where living team strategic registers (`00`–`11`), inventories, and visual outputs are persisted.

## Core Commands
Essential commands for validating plugins, skills, rules, and APM packaging:
```bash
apm compile --validate
python -m pytest
```

## Non-Negotiable Rules / Invariants
1. **Multi-Tier Mandate & Evidence Integrity**: Agents MUST trace team objectives upward through Division, Branch (CSB), Ministry, and Provincial mandates and NEVER fabricate evidence or baselines ([evidence-and-hierarchy-alignment.md](.agent/rules/evidence-and-hierarchy-alignment.md)).
2. **Interactive Plain-Language Pacing**: Agents MUST guide users interactively with numbered option menus, 1–2 plain-language questions per turn, and a recap confirmation gate before saving ([evidence-and-hierarchy-alignment.md](.agent/rules/evidence-and-hierarchy-alignment.md)).
3. **B.C. Government Design System Style**: All outputs MUST use B.C. Government sentence case, plain language, zero emoji, and official B.C. Design System v5 tokens ([evidence-and-hierarchy-alignment.md](.agent/rules/evidence-and-hierarchy-alignment.md)).
4. **Three-Inventory Separation**: Agents MUST keep Strategic Vision, the Idea Inventory, and the Committed Work Inventory strictly separate and NEVER treat unapproved ideas as committed work ([three-inventory-separation.md](.agent/rules/three-inventory-separation.md)).
5. **Non-Destructive Register Updates**: Agents MUST preserve stable record IDs and decision histories when importing evolving priorities, new ideas, or work progress ([three-inventory-separation.md](.agent/rules/three-inventory-separation.md)).
6. **APM-Native Packaging Hygiene**: All plugin skills MUST reside in `.apm/skills/` with zero raw symlinks, dual manifests, and `SKILL.md` under 80 lines ([apm-plugin-hygiene.md](.agent/rules/apm-plugin-hygiene.md)).
7. **Feature-Branch PR & Doc Synchronization**: `main` is branch-protected; all changes MUST use a feature branch (`feat/*`, `fix/*`, `docs/*`) and Pull Request, keeping `AGENTS.md`, [architecture.md](architecture.md), and [README.md](README.md) synchronized ([apm-plugin-hygiene.md](.agent/rules/apm-plugin-hygiene.md)).

## On-Demand Skills & Reference Index
- Read [architecture.md](architecture.md) when orienting to the 5-tier B.C. Gov / CSB hierarchy, the TOGAF ADM stage mapping, the 12 living strategy files (`00`–`11`), or skill data flows.
- Read [docs/governance.md](docs/governance.md) when reviewing repository packaging and governance policies.
- Use `running-strategic-planning-cycle` when starting or resuming a planning session, confirming the output directory (`~/strategic-planning-outputs/<team>/strategy/` or `./strategy/`), checking readiness across `00-planning-session-status.md`, or routing Top-Down, Bottom-Up, or Revisit flows across Claude, Copilot, Codex, Antigravity (`agy`), and GrokBot (`grok-bot`).
- Use `analyzing-strategic-context` when starting a guided discovery interview for leadership direction, drivers, stakeholders ("the players") and TOGAF Phase A viewpoints, current state, or assumptions.
- Use `defining-strategic-vision` when interactively coaching target future state, 4-part TOGAF operating principles (`PRN-X`), outcome-oriented strategic objectives (`OBJ-X`), and expected value (`BEN-X`).
- Use `planning-business-capabilities` when translating strategic objectives into TOGAF Phase B value streams (`VST-X`), required organizational capabilities (`CAP-X`), and 5-pillar maturity gaps.
- Use `managing-idea-inventory` when capturing, clarifying, assumption-testing, or evaluating unapproved opportunities in the Idea Inventory (`IDEA-X`).
- Use `managing-work-inventory` when cataloging committed initiatives, active experiments, and operational work (`WORK-X`) or promoting approved ideas.
- Use `managing-team-skills-and-allocation` when mapping team member skills (`MEM-X`), growth interests, and active `WORK-X` assignments or exporting Excel/CSV and Mermaid workload trackers.
- Use `aligning-strategy-and-portfolio` when interactively auditing end-to-end traceability, TOGAF Transformation Readiness (`BTRA`), and strategic, policy, privacy, and delivery risks (`RSK-X`).
- Use `sequencing-roadmaps-and-measures` when organizing committed work into Now/Next/Later horizons, TOGAF Transition State plateaus (`PLT-X`), and outcome, leading, and guardrail measures (`MSR-X`).
- Use `updating-strategic-registers` when importing evolving priorities, new drivers, stakeholder shifts, work progress, or time-boxed dispensations (`DSP-X`) with TOGAF Phase H change classification.
- Use `rendering-strategic-visuals-and-decks` when producing B.C. Gov Design System HTML dashboards, Mermaid roadmaps, Gantt charts, value-stream maps, or slide decks.
