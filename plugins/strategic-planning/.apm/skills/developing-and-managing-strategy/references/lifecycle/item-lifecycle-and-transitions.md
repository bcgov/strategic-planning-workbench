# Item lifecycle and transitions

How problems, ideas, work and risks move, link and close. Records are never changed into another type; a transition creates a new record in the next register and links back both ways, so history stays intact.

## Contents

- [The chain](#1-the-chain)
- [States by record type](#2-states-by-record-type)
- [Cross-type transitions](#3-cross-type-transitions)
- [Review triggers](#4-review-triggers)
- [Scoring across the lifecycle](#5-scoring-across-the-lifecycle)
- [Closure rules](#6-closure-rules)
- [Fields every record carries](#7-fields-every-record-carries)

## 1. The chain

```
Problem ─► Idea (solution) ─► Work (project, work package) ─► Product or operational duty
   ▲                                │                                  │
   └──────── Issue or new problem ◄─┴──── Risk (materializes) ◄────────┘
```

Lineage example: `IDEA-004` (problem) → `IDEA-009` (solution, `Related Problem ID: IDEA-004`) → `WORK-012` (`Related Idea ID: IDEA-009`) → `WORK-012` closes as `Transitioned to operations` with a service owner. Risks (`RSK-X`) attach to `WORK-X` and `OBJ-X`.

## 2. States by record type

| Record | States (in order) | Gate to leave a state |
|---|---|---|
| Problem (`IDEA-X`, type `Problem`) | `observed` → `validated` → `sized` → `addressed` → `resolved` (or `accepted`) | `validated`: evidence of who is affected and how often. `sized`: severity, reach and urgency recorded. `addressed`: a linked solution idea or work item exists. |
| Idea (`IDEA-X`, other types) | `raw` → `explored` → `validated` → `candidate` → `promoted` / `deferred` / `rejected` | See the idea funnel guide. `promoted` records the resulting `WORK-X`. |
| Work (`WORK-X`) | `Planned` → `Active` ⇄ `Blocked` / `Paused` → `Completed` → `Transitioned to operations` or `Retired`; or `Cancelled` | `Active`: sponsor, owner and capacity confirmed. `Completed`: deliverables accepted. Leaving `Completed`: a named service owner or an explicit retirement. |
| Risk (`RSK-X`) | `identified` → `assessed` → `responding` → `monitoring` → `closed` / `materialized` / `accepted` | `assessed`: likelihood, impact and proximity rated. `responding`: response chosen (mitigate, transfer, avoid, accept) with an owner. `accepted`: rationale and approver recorded. |
| Assumption (`ASM-X`) | `unvalidated` → `validated` / `invalidated` | Invalidated assumptions trigger a ripple check. |

Experiments are work with exit criteria. At the exit date they become one of: promote (new `WORK-X` as project or product-service), pivot (new idea), or retire (closed with lessons).

## 3. Cross-type transitions

| From | Event | To |
|---|---|---|
| Problem `validated` | Solution proposed | New solution idea, `Related Problem ID` set |
| Idea `candidate` | Promotion gate passed | New `WORK-X` `Planned`, idea becomes `promoted` |
| Work `Active` | Risk event occurs | Risk `materialized`; new problem or blocker |
| Risk `responding` | Mitigation chosen | New work package under the affected `WORK-X` |
| Work `Completed` | Handover | `Transitioned to operations` (product-service or operational) |
| Operations | Service degrades | New problem |
| Shadow operation | Governance decision | Formalize as product-service, or retire |
| Assumption `invalidated` | Dependent items exist | Risk or problem raised; dependent ideas and work re-scored |
| Dispensation (`DSP-X`) | Expiry reached | Remediation work item |
| Idea `deferred` | Revisit date reached | Back to `explored` |

## 4. Review triggers

Time-based triggers reuse the cadences in the revisit guide (Cycle mode). Event-based triggers are the ripple check in Update mode, which lists affected records and raises follow-ups for the item modes (see the bookkeeping contract).

| Trigger type | Examples (defaults; the team may adjust) |
|---|---|
| Time | `raw` idea untouched 90 days: decide or defer. Deferred idea: revisit date. Experiment: exit date. Risk: review date by rating. Dispensation: expiry. Work `Blocked` more than 30 days: escalate. |
| Event | Assumption invalidated or constraint changed (review every `RSK-X` and `WORK-X` that depends on it; link, do not convert records). Objective changed (Phase H). Measure breaches a guardrail. Owner overloaded. Risk materializes. |

## 5. Scoring across the lifecycle

Scoring is a dated snapshot, not a one-time event. Keep each snapshot with the date, scorer and framework used. Re-score at decision points and on trigger events.

| Item | Lens | When to score or re-score |
|---|---|---|
| Idea or project proposal | Value × ability to deliver (Score mode) | At `candidate`, and when a key assumption changes |
| Problem | Severity × reach × evidence × urgency | At `sized`, and when evidence changes |
| Risk | Likelihood × impact × proximity | At `assessed`, and at each review |
| Work in flight | Health: on track, at risk, blocked | At each progress check-in |

The Score mode ships the value × delivery profile. Problem and risk profiles are specified here and are not yet scripted.

## 6. Closure rules

1. Rejected and deferred ideas stay in `07` with their decision rationale.
2. Work does not close without a named service owner or an explicit retirement, and records the outcome against its success measures.
3. A `promoted` idea links to its work item, and the work item's outcome is visible from the idea.
4. Resolved problems and closed risks keep a closing note and the date.
5. Every closure is appended to `changelog.md`; nothing is deleted.

## 7. Fields every record carries

`ID`, `Type`, `State`, `Owner`, `Related IDs` (problem, idea, work, risk, objective), `Next review date`, `Review trigger`, `Last scored` (date and value), and `Decision history`.
