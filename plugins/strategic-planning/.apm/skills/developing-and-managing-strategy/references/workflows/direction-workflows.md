# Direction workflows

Steps, templates and gates for the strategy layer: Cycle, Context, Vision, Capabilities, Update, Alignment and Measures.

## Contents

- [Cycle](#cycle)
- [Context](#context)
- [Vision](#vision)
- [Capabilities](#capabilities)
- [Update](#update)
- [Alignment](#alignment)
- [Measures](#measures)

## Cycle

1. Resolve the folder, scan `00`–`11`, and track stage and next step in `00` after every gate.
2. First run: ask where to save, then offer top-down interview, bottom-up from existing items, or import notes. Returning: report status and offer the menu in [workspace and first run](../cycle/workspace-and-first-run-guide.md).
3. A revisit runs only the strategy-level checks and dispatches item-level checks to the matching mode ([revisit guide](../cycle/revisiting-and-updating-plans-guide.md)).
4. Stages and TOGAF mapping: [cycle guide](../cycle/strategic-planning-cycle-and-togaf-adm-guide.md). Gate: [acceptance criteria](../cycle/acceptance-criteria.md). Template: [planning-session-status](../../assets/templates/planning-session-status.md).

## Context

Offer the 3-option intake menu (paste notes, guided interview, review existing context). Capture leadership direction by tier, map stakeholders and where views conflict, then walk current state one topic at a time, tagging points `Evidence-Backed` or `Anecdotal`.
Templates: [strategic-context-brief](../../assets/templates/strategic-context-brief.md), [stakeholder-map](../../assets/templates/stakeholder-map.md), [assumptions-and-evidence-register](../../assets/templates/assumptions-and-evidence-register.md). Guides: [context](../context/context-and-stakeholder-guide.md), [public-sector lens](../context/public-sector-context-lens.md). Gate: [acceptance criteria](../context/acceptance-criteria.md).

## Vision

Draft 2–3 vision statements, co-design 4–6 operating principles (statement, rationale, trade-off), draft 3–6 outcome objectives (`OBJ-X`) with the activity-to-outcome test, and map each to benefits. For major transformations use the 8-dimension canvas with [generate_shared_vision.py](../../scripts/generate_shared_vision.py) and the [worked example](../vision/examples/cats-court-transformation-shared-vision.md).
Templates: [strategy-on-a-page](../../assets/templates/strategy-on-a-page.md), [strategic-vision-brief](../../assets/templates/strategic-vision-brief.md), [benefits-dependency-map](../../assets/templates/benefits-dependency-map.md), [shared-vision-model](../../assets/templates/shared-vision-model.md). Guides: [vision](../vision/vision-and-objectives-guide.md), [shared vision model](../vision/shared-vision-model-guide.md). Gate: [acceptance criteria](../vision/acceptance-criteria.md).

## Capabilities

Propose 4–8 candidate capabilities per value stream, rate current versus target maturity (0–5), and walk the five pillars (people, process, information, technology, policy) for each gap. Name capabilities as abilities, never tools or projects.
Template: [capability-map-and-gaps](../../assets/templates/capability-map-and-gaps.md). Guide: [capability planning](../capabilities/capability-based-planning-guide.md). Gate: [acceptance criteria](../capabilities/acceptance-criteria.md).

## Update

Map each change to its register, list every affected record by ID with the mode that owns it, classify it (`Simplification`, `Incremental`, `Re-direction`), log dispensations (`DSP-X`), write after confirmation, then log in the changelog. Item changes (a status, a new risk) go to the item modes. A changed assumption or constraint raises follow-ups for every dependent risk and work item.
Templates: [register-update-changelog](../../assets/templates/register-update-changelog.md), [org-hierarchy-and-mandates](../../assets/templates/org-hierarchy-and-mandates.md). Guides: [register guide](../update/living-register-update-guide.md), [hierarchy](../update/bc-gov-csb-hierarchy-reference.md). Gate: [acceptance criteria](../update/acceptance-criteria.md).

## Alignment

Trace direction → `OBJ-X` → `CAP-X` → `IDEA-X` → `WORK-X` → `MSR-X`, present the 8 diagnostics with numbered resolution options (`Realign`, `Justify as baseline`, `Consolidate`, `Pause or retire`, `Commission discovery`), and rate readiness. Send risks found to Risks mode; never write them here.
Templates: [alignment-traceability-matrix](../../assets/templates/alignment-traceability-matrix.md), [transformation-readiness-assessment](../../assets/templates/transformation-readiness-assessment.md). Guide: [alignment and readiness](../alignment/alignment-and-readiness-guide.md). Gate: [acceptance criteria](../alignment/acceptance-criteria.md).

## Measures

For each objective, pair one outcome measure and 1–2 leading indicators with a guardrail (fairness, privacy, accuracy, workload). Mark missing baselines `Baseline needed`. Writes only the success measures section of register `10`.
Template: [success-measures-register](../../assets/templates/success-measures-register.md). Guide: [measures guide](../measures/measures-guide.md). Gate: [acceptance criteria](../measures/acceptance-criteria.md).
