# Strategic Planning Plugin (`strategic-planning`)

An APM-native agent plugin for **organizational, division, and public-sector branch strategic planning** (tailored for the **BC Government / Ministry of Attorney General / Court Services Branch** hierarchy). Guides teams from multi-tier leadership direction and stakeholder analysis through target vision, business capabilities, idea funnel evaluation, committed work tracking, alignment auditing, living register updates, and visual/executive presentation rendering.

## Directory Structure

```text
strategic-planning/
├── .apm/
│   └── skills/
│       ├── designing-logic-models/
│       │   ├── SKILL.md
│       │   ├── assets/templates/
│       │   ├── evals/
│       │   ├── references/
│       │   └── scripts/
│       ├── developing-and-managing-strategy/
│       │   ├── SKILL.md
│       │   ├── assets/templates/
│       │   ├── evals/
│       │   ├── references/
│       │   └── scripts/
│       ├── managing-team-skills-and-allocation/
│       │   ├── SKILL.md
│       │   ├── assets/templates/
│       │   ├── evals/
│       │   └── references/
│       ├── rendering-strategic-visuals-and-decks/
│       │   ├── SKILL.md
│       │   ├── assets/templates/
│       │   ├── evals/
│       │   └── references/
│       └── triaging-new-items/
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
| `developing-and-managing-strategy` | **Main skill.** First run asks where to save and runs the strategic interview; afterwards it resumes, revisits and updates the plan. 13 modes in four groups: Establish direction (Cycle, Context, Vision, Capabilities), Change direction (Update), Manage items (Ideas, Work, Risks, Score), Review alignment and delivery (Alignment, Measures, Roadmap, Review). Owns registers `00`–`10`. | `planning-session-status.md`, `register-update-changelog.md`, `org-hierarchy-and-mandates.md`, `strategic-context-brief.md`, `stakeholder-map.md`, `assumptions-and-evidence-register.md`, `strategy-on-a-page.md`, `strategic-vision-brief.md`, `benefits-dependency-map.md`, `shared-vision-model.md`, `capability-map-and-gaps.md`, `idea-inventory.md`, `idea-record.md`, `idea-evaluation.md`, `work-inventory.md`, `strategic-risk-register.md`, `investment-scoring-framework.json`, `investment-scoring-ledger.json`, `investment-scoring-ledger.csv`, `investment-scoring-brief.md`, `alignment-traceability-matrix.md`, `transformation-readiness-assessment.md`, `success-measures-register.md`, `strategic-roadmap.md` |
| `triaging-new-items` | Classifies new, mixed or unclear material by commitment state and nature (problem, driver, risk, idea, project, training, decision, blocker, and more), with a funding-request flag, and routes each item to the right mode or skill. Writes only a triage log. | `intake-triage-log.md` |
| `managing-team-skills-and-allocation` | Mapping team members (`MEM-X`), skills and proficiency, growth interests, training requests, and active `WORK-X` assignments; recording capacity evidence for commitments; exporting Excel CSV trackers and Mermaid workload charts. Owns register `11`. | `team-skills-and-allocation-register.md`, `team-work-tracker.csv` |
| `designing-logic-models` | Designing, reviewing, and documenting program logic models, results chains, outcome chains, theories of change, and results frameworks. Produces an artifact; writes no registers. | `logic-model-template.md` |
| `rendering-strategic-visuals-and-decks` | Generating Mermaid alignment diagrams, value-stream maps, capability charts, horizon/Gantt roadmaps, B.C. Gov HTML dashboards, and executive decks from the registers. Work without commitment evidence is drawn as a decision gate. | `mermaid-strategy-visuals.md`, `bc-gov-strategy-dashboard.html`, `executive-strategy-deck.md` |

**Shared files and ownership.** `developing-and-managing-strategy` and `managing-team-skills-and-allocation` carry the same `references/shared/bookkeeping-contract.md`: each mode edits only its own register sections, changes touching another owner become `Open follow-ups` in `00`, and every confirmed change is appended to `changelog.md`. Every skill also carries `references/guided-interaction.md`.

**Scripts.** `developing-and-managing-strategy/scripts/` holds the scoring generator, the interactive scoring dashboard, the shared-vision generator, and `test_investment_scripts.py`, which runs regression checks (lossless CSV round trips, evidence validation, escaping, and saved weights).

## Non-Negotiable Guardrails

1. **Five-Tier Alignment**: Trace team objectives upward through Division, Court Services Branch (CSB), Ministry of Attorney General, and BC Government mandates.
2. **No Premature Solutioning**: Do not generate project schedules, technology wish lists, or feature specifications before strategic context, target vision, outcome objectives, and required capabilities are established.
3. **Evidence Over Invention**: Distinguish confirmed leadership direction and documented evidence from interpretations and unproven assumptions. Record gaps in the Assumptions & Evidence Register.
4. **Separate Ideas from Committed Work**: Never represent a brainstormed idea, suggestion, or unapproved experiment as committed work in the Work Inventory or as a scheduled roadmap bar unless a named sponsor with approval date, a named owner, and confirmed capacity are recorded. Approval without capacity stays a decision gate flagged `Capacity unconfirmed`.
