---
name: triaging-new-items
description: "Classifies new, mixed or unclear material (problems, drivers, risks, ideas, projects and work packages, operational duties, training and funding requests, decisions, blockers, exceptions, strategy changes) by commitment state and nature of work, then routes each item to the right register and mode. Use when the user pastes a mixed list, meeting notes or a spreadsheet, or says 'onboard these', 'we have a new risk', 'log this problem', 'is this an idea or a project', or 'where does this go'. Not for explicit requests on a named record such as 'update WORK-12' or 'promote IDEA-9', the first-time strategy interview, changing the strategy, or developing, scoring and tracking items (all use developing-and-managing-strategy), team capacity (use managing-team-skills-and-allocation), logic models (use designing-logic-models) or decks (use rendering-strategic-visuals-and-decks)."
---

# Triaging new items

Front door for new or unclear material that is not yet a record. Asks two short questions per item, shows where it belongs, and hands it to the skill that owns that register. Writes only a triage log; the receiving skill creates the `IDEA-X`, `WORK-X` or `RSK-X` record. It is not a required gateway: explicit requests on named records go straight to their owner.

## Contents

- [Constraints](#constraints) • [Quick start](#quick-start) • [Workflow](#workflow) • [Verification](#verification) • [References](#references)

## Constraints

1. **Only for new or unclear material**: If the user names an existing record and an explicit action, skip triage and hand it to the owner skill.
2. **Two gates, in order**: Gate 1 asks commitment state (`Heard`, `Considering`, `Approved`, `Running`, `Ongoing`); Gate 2 asks nature (problem, opportunity, solution, experiment, delivery such as a project or work package, operational, research, training, driver, risk, strategy change, assumption or constraint, exception, decision, blocker, team change, action item). Natures that are not commitments skip Gate 1. A funding or investment ask is a flag on the item, never a shortcut past validation ([guide](references/classification/intake-classification-guide.md)).
3. **Approval is not commitment**: Treat an item as committed only with a named sponsor and approval date, a named owner, and capacity. "The director approved it" with no capacity routes as `Approved, capacity unconfirmed` (a decision gate, not committed work). Running without approval is a `Shadow Operation`. Never promote on triage.
4. **Split mixed items**: "Build an AI tool for X" becomes a `Problem` row and a linked `Solution` row; a risk noticed inside a project becomes its own row.
5. **Write nothing but the log**: Do not create records. If no strategy folder exists yet, hand off to `developing-and-managing-strategy` first.
6. **Guided interaction**: Guide the user step by step with questions, following [guided-interaction.md](references/guided-interaction.md): open with a numbered menu or one question, ask 1–2 per turn with a recommended default, show progress, accept "I don't know" as an open item, and confirm a recap before every write. Batch the obvious items into one confirmation table.
7. **B.C. Government Design System style**: Sentence case, plain language, zero emoji.

## Quick start

1. Read [intake-classification-guide.md](references/classification/intake-classification-guide.md) and ask the user to paste or describe the items.
2. Classify each item through both gates and show the routing table.
3. After confirmation, save [intake-triage-log.md](assets/templates/intake-triage-log.md) and offer to run the receiving skill.

## Workflow

1. **Collect**: Gather raw items from notes, spreadsheets or conversation; one row each.
2. **Gate 1**: Ask who approved it, who owns it, whether capacity exists, and whether anyone is working on it today.
3. **Gate 2**: Classify the nature; separate problem from solution; name the parent for work packages.
4. **Route**: Apply the routing table. Unclear items default to `raw` ideas, never to the work inventory.
5. **Recap and hand off**: Confirm, save the log, then chain to `developing-and-managing-strategy` (Ideas, Work, Risks, Score) or, for direction, stakeholder, objective, assumption or constraint changes, to `developing-and-managing-strategy` (Update mode). Record types and states are defined in `developing-and-managing-strategy`.

## Verification

Check outputs against [acceptance-criteria.md](references/classification/acceptance-criteria.md):
- Every item has a commitment state (or `Not applicable` for risks), a nature, a destination and a reason.
- No item is routed as committed without a confirmed sponsor, owner and capacity; no records are created here.

## References

- Classification, routing and tie-breakers: [intake-classification-guide.md](references/classification/intake-classification-guide.md) • [flow](references/classification/intake-flow.mmd)
- Template: [intake-triage-log.md](assets/templates/intake-triage-log.md)
