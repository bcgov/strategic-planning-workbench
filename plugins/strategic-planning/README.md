# Strategic Planning Plugin (`strategic-planning`)

An APM-native agent plugin for **organizational, division, and public-sector branch strategic planning** (tailored for the **BC Government / Ministry of Attorney General / Court Services Branch** hierarchy). Guides teams from multi-tier leadership direction and stakeholder analysis through target vision, business capabilities, idea funnel evaluation, committed work tracking, alignment auditing, living register updates, and visual/executive presentation rendering.

## Directory Structure

```text
strategic-planning/
├── .apm/
│   └── skills/
│       ├── aligning-strategy-and-portfolio/
│       │   ├── SKILL.md
│       │   ├── assets/templates/
│       │   ├── evals/
│       │   └── references/
│       ├── analyzing-strategic-context/
│       │   ├── SKILL.md
│       │   ├── assets/templates/
│       │   ├── evals/
│       │   └── references/
│       ├── defining-strategic-vision/
│       │   ├── SKILL.md
│       │   ├── assets/templates/
│       │   ├── evals/
│       │   └── references/
│       ├── designing-logic-models/
│       │   ├── SKILL.md
│       │   ├── assets/templates/
│       │   ├── evals/
│       │   └── references/
│       ├── managing-idea-inventory/
│       │   ├── SKILL.md
│       │   ├── assets/templates/
│       │   ├── evals/
│       │   └── references/
│       ├── managing-work-inventory/
│       │   ├── SKILL.md
│       │   ├── assets/templates/
│       │   ├── evals/
│       │   └── references/
│       ├── managing-team-skills-and-allocation/
│       │   ├── SKILL.md
│       │   ├── assets/templates/
│       │   ├── evals/
│       │   └── references/
│       ├── planning-business-capabilities/
│       │   ├── SKILL.md
│       │   ├── assets/templates/
│       │   ├── evals/
│       │   └── references/
│       ├── prioritizing-and-scoring-investments/
│       │   ├── SKILL.md
│       │   ├── assets/templates/
│       │   ├── evals/
│       │   ├── references/
│       │   └── scripts/
│       ├── rendering-strategic-visuals-and-decks/
│       │   ├── SKILL.md
│       │   ├── assets/templates/
│       │   ├── evals/
│       │   └── references/
│       ├── running-strategic-planning-cycle/
│       │   ├── SKILL.md
│       │   ├── assets/templates/
│       │   ├── evals/
│       │   └── references/
│       ├── sequencing-roadmaps-and-measures/
│       │   ├── SKILL.md
│       │   ├── assets/templates/
│       │   ├── evals/
│       │   └── references/
│       └── updating-strategic-registers/
│           ├── SKILL.md
│           ├── assets/templates/
│           ├── evals/
│           └── references/
├── .claude-plugin/
│   └── plugin.json
├── apm.yml
├── README.md
└── rules/
    ├── apm-plugin-hygiene.md
    ├── evidence-and-hierarchy-alignment.md
    └── three-inventory-separation.md
```

## Skills

| Skill | What It Covers | Primary Templates |
|---|---|---|
| `running-strategic-planning-cycle` | **Front-door orchestrator & TOGAF ADM cycle coach**: scans existing `strategy/` registers, offers a 5-option entry menu (Top-Down, Bottom-Up, Resume, Import Notes, Fast-Track Briefing), maintains `00-planning-session-status.md`, and routes across the 10 specialist skills. | `planning-session-status.md` |
| `analyzing-strategic-context` | Multi-tier leadership direction, mandates, business drivers, stakeholder power/interest mapping ("the players") and TOGAF Phase A viewpoints, evidence-based current state, and assumption tracking. | `strategic-context-brief.md`, `stakeholder-map.md`, `assumptions-and-evidence-register.md` |
| `defining-strategic-vision` | Target future state, 4-part TOGAF operating principles (`PRN-X`), outcome-oriented strategic objectives (detecting disguised activities), and public/business value. | `strategy-on-a-page.md`, `strategic-vision-brief.md`, `benefits-dependency-map.md`, `shared-vision-model.md` |
| `designing-logic-models` | Designing, reviewing, and documenting program logic models, results chains, outcome chains, theories of change, and results frameworks connecting inputs and activities to outputs and successive outcomes. | `logic-model-template.md` |
| `planning-business-capabilities` | Translating vision and objectives into TOGAF Phase B value streams (`VST-X`), required business capabilities (`CAP-X`), maturity levels, and 5-pillar capability gap analysis. | `capability-map-and-gaps.md` |
| `managing-idea-inventory` | Capturing, clarifying, assumption-testing, and evaluating unapproved opportunities across maturity states (`raw` → `candidate` / `deferred` / `rejected`). | `idea-inventory.md`, `idea-record.md`, `idea-evaluation.md` |
| `prioritizing-and-scoring-investments` | Evaluating, weighting, and ranking candidate investments across Value/ROI and Ability to Deliver using a 4-quadrant scatter chart, dual-format JSON/CSV ledgers, and executive briefs. | `investment-scoring-framework.json`, `investment-scoring-ledger.json`, `investment-scoring-ledger.csv`, `investment-scoring-brief.md` |
| `managing-work-inventory` | Maintaining the portfolio of committed initiatives, active experiments, and operational responsibilities with verified sponsorship and ownership. | `work-inventory.md` |
| `managing-team-skills-and-allocation` | Mapping team members (`MEM-X`), current skills/proficiency, growth interests, and active `WORK-X` assignments; exporting Excel CSV trackers and Mermaid workload charts. | `team-skills-and-allocation-register.md`, `team-work-tracker.csv` |
| `aligning-strategy-and-portfolio` | Auditing end-to-end traceability (Province/AG/CSB → Vision → Objectives → Capabilities → Ideas → Work), TOGAF Transformation Readiness (`BTRA`), and strategic risk registers. | `alignment-traceability-matrix.md`, `strategic-risk-register.md` |
| `sequencing-roadmaps-and-measures` | Sequencing committed initiatives into Now/Next/Later or Three Horizons roadmaps with TOGAF Transition State plateaus (`PLT-X`), decision gates, OKRs, leading indicators, and guardrails. | `strategic-roadmap.md`, `success-measures-register.md` |
| `updating-strategic-registers` | Importing and incrementally updating evolving priorities, multi-tier org mandates, drivers, stakeholder shifts, new ideas, work progress, and time-boxed dispensations (`DSP-X`) with TOGAF Phase H change classification. | `org-hierarchy-and-mandates.md`, `register-update-changelog.md` |
| `rendering-strategic-visuals-and-decks` | Generating Mermaid alignment diagrams, value-stream maps, capability charts, high-level horizon/Gantt roadmaps, B.C. Gov HTML dashboards, and executive presentation decks. | `mermaid-strategy-visuals.md`, `bc-gov-strategy-dashboard.html`, `executive-strategy-deck.md` |

## Non-Negotiable Guardrails

1. **Five-Tier Alignment**: Trace team objectives upward through Division, Court Services Branch (CSB), Ministry of Attorney General, and BC Government mandates.
2. **No Premature Solutioning**: Do not generate project schedules, technology wish lists, or feature specifications before strategic context, target vision, outcome objectives, and required capabilities are established.
3. **Evidence Over Invention**: Distinguish confirmed leadership direction and documented evidence from interpretations and unproven assumptions. Record gaps in the Assumptions & Evidence Register.
4. **Separate Ideas from Committed Work**: Never represent a brainstormed idea, suggestion, or unapproved experiment as committed work in the Work Inventory or as a scheduled roadmap bar unless sponsorship, ownership, and capacity commitment are confirmed.
