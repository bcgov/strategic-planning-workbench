---
name: developing-and-managing-strategy
description: "Builds, changes and runs a team's strategy and the items under it. On first use it asks where to save outputs and runs the strategic interview; afterwards it resumes and revisits the plan, updates the strategy, develops ideas and problems, records committed work, rates risks, scores investments, audits alignment, sets success measures, builds the roadmap and reviews items against their lifecycle. Use when the user asks 'where do we start', 'help us build our strategy', 'where did we leave off', 'our priorities changed', 'promote this idea', 'update the status of WORK-12', 'rate this risk', 'score these funding requests', 'does our work align to our objectives', 'define success measures' or 'make a roadmap'. Not for sorting a new, mixed or unclear list (use triaging-new-items), team capacity (use managing-team-skills-and-allocation), logic models (use designing-logic-models) or decks and dashboards (use rendering-strategic-visuals-and-decks)."
---

# Developing and managing strategy

One skill with two layers: the strategy (registers `00`–`05`, assumptions and constraints in `06`, `09`, success measures in `10`) and the items under it (ideas `07`, work `08`, risks in `06`, roadmap in `10`). The team skill owns `11`. It finds the team's strategy folder, runs the first-time interview or resumes, and routes each request to one mode.

## Contents

- [Constraints](#constraints) • [Modes](#modes) • [Quick start](#quick-start) • [Workflow](#workflow) • [Other skills](#other-skills) • [Verification](#verification) • [References](#references)

## Constraints

1. **Resolve the folder first**: Check the remembered path, `./strategy/`, then `~/strategic-planning-outputs/*/strategy/`. Create nothing until every candidate is resolved ([workspace guide](references/cycle/workspace-and-first-run-guide.md)). Only a true first run asks where to save and where source documents live.
2. **Resume, never restart**: Read `00` and the registers; an unfinished step resumes where it stopped.
3. **One mode, its own sections**: Write only the sections the current mode owns ([bookkeeping contract](references/shared/bookkeeping-contract.md)). A change that touches another mode's records becomes a listed `Open follow-ups` row in `00`, not an edit.
4. **Ideas are not committed work**: Committed means a named sponsor with approval date, a named owner and confirmed capacity. Approval without capacity is `Capacity unconfirmed` and shows on the roadmap only as a decision gate. Rule `three-inventory-separation` applies.
5. **Ask when the request is ambiguous**: "Review our priorities" or "update the plan" needs one question: the strategy (objectives, measures) or the items (ranking, delivery status)?
6. **Guided interaction**: Guide the user step by step with questions, following [guided-interaction.md](references/guided-interaction.md): open with a numbered menu or one question, ask 1–2 per turn with a recommended default, show progress, accept "I don't know" as an open item, and confirm a recap before every write. Separate `Confirmed` from `Interpreted`.
7. **Preview, then write**: Show changes, affected records and the Phase H class; wait for confirmation; keep IDs; never delete; append to `changelog.md`.
8. **B.C. Government Design System style**: Sentence case, plain language, zero emoji, recap gate (`yes / adjust`).

## Modes

| Group | Mode | Use when | Read |
|---|---|---|---|
| Establish direction | Cycle | First run, resume, what is missing | [workspace and first run](references/cycle/workspace-and-first-run-guide.md) |
| | Context | Leadership direction, stakeholders, current state, assumptions | [context guide](references/context/context-and-stakeholder-guide.md) |
| | Vision | Target state, principles, outcome objectives, value | [vision guide](references/vision/vision-and-objectives-guide.md) |
| | Capabilities | Value streams, capabilities, maturity gaps | [capability guide](references/capabilities/capability-based-planning-guide.md) |
| Change direction | Update | Priorities, objectives, stakeholders, assumptions or constraints changed; dispensations; revisit on a cadence | [register guide](references/update/living-register-update-guide.md) • [revisit guide](references/cycle/revisiting-and-updating-plans-guide.md) |
| Manage items | Ideas | Capture, stress-test, decide on ideas and problems | [funnel guide](references/ideas/idea-funnel-and-evaluation-guide.md) |
| | Work | Record or audit committed work, promote, status | [work guide](references/work/work-portfolio-guide.md) |
| | Risks | Record, rate and respond to risks | [risk guide](references/risks/risk-management-guide.md) |
| | Score | Weight, score and rank candidates or funding requests | [rubric](references/scoring/scoring-rubric-and-weighting-guide.md) |
| Review alignment and delivery | Alignment | Traceability audit and transformation readiness | [alignment guide](references/alignment/alignment-and-readiness-guide.md) |
| | Measures | Outcome, leading and guardrail measures | [measures guide](references/measures/measures-guide.md) |
| | Roadmap | Horizons, plateaus, decision gates | [roadmap guide](references/roadmap/roadmap-guide.md) |
| | Review | Items against lifecycle states; open follow-ups | [lifecycle](references/lifecycle/item-lifecycle-and-transitions.md) |

## Quick start

1. Resolve the folder. First run: ask where to save, then offer `1. Top-down interview (Recommended)`, `2. Bottom-up from existing items`, `3. Import notes`; options 2 and 3 go to `triaging-new-items`.
2. Returning: report status, then offer `1. Continue`, `2. Update the strategy`, `3. Alignment or measures`, `4. Revisit on a cadence`, `5. Visuals or a deck`.
3. If the request names a record with a verb ("promote IDEA-9") or asks for ideas, work, risks, scoring or the roadmap, go straight to that mode.

## Workflow

1. **Direction modes**: Follow [direction-workflows.md](references/workflows/direction-workflows.md) for Cycle, Context, Vision, Capabilities and Update.
2. **Item modes**: Follow [item-workflows.md](references/workflows/item-workflows.md) for Ideas, Work, Risks, Score and Review.
3. **Alignment, Measures and Roadmap**: Steps are in both workflow files; Roadmap and Alignment read both layers but write only their own section.
4. **Recap, save, log**: Confirm, write, append to [register-update-changelog](assets/templates/register-update-changelog.md), update `00` and its follow-ups.

## Other skills

| Request | Skill |
|---|---|
| New, mixed or unclear material; "log this problem or risk" | `triaging-new-items` |
| Team skills and capacity (`11`) | `managing-team-skills-and-allocation` |
| Logic models and results chains | `designing-logic-models` |
| Dashboards, roadmaps as visuals, decks | `rendering-strategic-visuals-and-decks` |

## Verification

Each mode's gate is `acceptance-criteria.md` in its reference folder (`references/<mode>/`). Before finishing check: folder resolved, only owned sections written, IDs kept, no idea or uncapacitated item shown as committed, and follow-ups visible in `00`.

## References

- Per-mode steps and templates: [direction-workflows.md](references/workflows/direction-workflows.md) • [item-workflows.md](references/workflows/item-workflows.md)
- Cycle, stages and chat agents: [cycle and TOGAF stages](references/cycle/strategic-planning-cycle-and-togaf-adm-guide.md) • [chat agents](references/cycle/grokbot-and-chat-agent-guide.md)
- Shared rules for `00`, the changelog and section ownership: [bookkeeping-contract.md](references/shared/bookkeeping-contract.md)
- Reference map (direct links to every template, gate and guide the workflow files use):
  - Templates: [alignment traceability matrix](assets/templates/alignment-traceability-matrix.md) • [assumptions and evidence register](assets/templates/assumptions-and-evidence-register.md) • [benefits dependency map](assets/templates/benefits-dependency-map.md) • [capability map and gaps](assets/templates/capability-map-and-gaps.md) • [idea evaluation](assets/templates/idea-evaluation.md) • [idea inventory](assets/templates/idea-inventory.md) • [idea record](assets/templates/idea-record.md) • [investment scoring brief](assets/templates/investment-scoring-brief.md) • [org hierarchy and mandates](assets/templates/org-hierarchy-and-mandates.md) • [planning session status](assets/templates/planning-session-status.md) • [shared vision model](assets/templates/shared-vision-model.md) • [stakeholder map](assets/templates/stakeholder-map.md) • [strategic context brief](assets/templates/strategic-context-brief.md) • [strategic risk register](assets/templates/strategic-risk-register.md) • [strategic roadmap](assets/templates/strategic-roadmap.md) • [strategic vision brief](assets/templates/strategic-vision-brief.md) • [strategy on a page](assets/templates/strategy-on-a-page.md) • [success measures register](assets/templates/success-measures-register.md) • [transformation readiness assessment](assets/templates/transformation-readiness-assessment.md) • [work inventory](assets/templates/work-inventory.md)
  - Mode gates: [alignment gate](references/alignment/acceptance-criteria.md) • [capabilities gate](references/capabilities/acceptance-criteria.md) • [context gate](references/context/acceptance-criteria.md) • [cycle gate](references/cycle/acceptance-criteria.md) • [ideas gate](references/ideas/acceptance-criteria.md) • [measures gate](references/measures/acceptance-criteria.md) • [risks gate](references/risks/acceptance-criteria.md) • [roadmap gate](references/roadmap/acceptance-criteria.md) • [scoring gate](references/scoring/acceptance-criteria.md) • [update gate](references/update/acceptance-criteria.md) • [vision gate](references/vision/acceptance-criteria.md) • [work gate](references/work/acceptance-criteria.md)
  - Guides and examples: [public sector context lens](references/context/public-sector-context-lens.md) • [problem and idea types](references/ideas/problem-and-idea-types.md) • [4 quadrant portfolio guide](references/scoring/4-quadrant-portfolio-guide.md) • [bc gov csb hierarchy reference](references/update/bc-gov-csb-hierarchy-reference.md) • [cats court transformation shared vision](references/vision/examples/cats-court-transformation-shared-vision.md) • [shared vision model guide](references/vision/shared-vision-model-guide.md) • [project and work package types](references/work/project-and-work-package-types.md)
