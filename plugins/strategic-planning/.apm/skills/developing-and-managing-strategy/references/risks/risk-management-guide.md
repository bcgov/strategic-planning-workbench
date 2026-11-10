# Risk management guide

How to record, assess, respond to and review risks (`RSK-X`) in register `06`. Assumptions (`ASM-X`), constraints (`CON-X`) and evidence gaps (`GAP-X`) in the same file are owned by the Context mode of `developing-and-managing-strategy`; this guide covers only `RSK-X`.

## Contents

- [What counts as a risk](#1-what-counts-as-a-risk)
- [Public-sector risk taxonomy](#2-public-sector-risk-taxonomy)
- [Assessment](#3-assessment)
- [Responses](#4-responses)
- [Linking and review](#5-linking-and-review)
- [Interactive flow](#6-interactive-flow)

## 1. What counts as a risk

A risk is something that **might** happen and would hurt an objective or a piece of work. Use the right record:

| It is... | Record |
|---|---|
| Uncertain future event | `RSK-X` |
| Already happening | Problem (`IDEA-X`, type `Problem`) or a blocker on the `WORK-X` item |
| Something we are assuming is true | `ASM-X` |
| A fixed limit we cannot change | `CON-X` |

A risk that occurs becomes `materialized` and spawns a problem or blocker; it is never edited into one.

## 2. Public-sector risk taxonomy

Check each risk against seven lenses:

1. **Strategic and mandate**: drift from ministerial or executive direction, or conflicting stakeholder expectations.
2. **Policy, legislative and procedural fairness**: actions that conflict with statutes, court rules or administrative fairness.
3. **Privacy, security and records**: unauthorized data exposure, FOIPPA non-compliance, or unapproved AI data handling.
4. **Judicial and operational independence**: blurring executive administration with judicial decision-making.
5. **Workforce and change readiness**: change fatigue, key-person dependency, or lack of support capacity.
6. **Cross-ministry and partner dependency**: reliance on other ministries, central IT or justice partners without agreed service levels.
7. **Vendor and platform lock-in**: over-dependence on proprietary tooling or unapproved shadow IT.

## 3. Assessment

Rate on three dimensions, each `High`, `Med` or `Low`:

| Dimension | Question |
|---|---|
| Likelihood | How likely is it in the planning horizon? |
| Severity | How bad if it happens: service, public trust, legal, cost? |
| Proximity | How soon could it happen? |

Exposure is likelihood combined with severity; use proximity to order ties. Record the date and rating each time (`Last scored`). Do not invent numbers; if evidence is missing, mark the rating `Unvalidated` and add an evidence action.

## 4. Responses

| Response | Meaning | Required |
|---|---|---|
| `mitigate` | Reduce likelihood or severity | Owner, action, due date; offer a work package under the affected `WORK-X` |
| `transfer` | Shift to another party | Named party and agreement |
| `avoid` | Change plans so it cannot occur | The decision and the changed scope |
| `accept` | Live with it | Rationale, approver and a review date |

## 5. Linking and review

- Link every risk to the affected `WORK-X` or `OBJ-X`. A risk with neither is `Unlinked`; ask which it threatens.
- Set `Next review date` by exposure (high: monthly or at each check-in; low: quarterly).
- When an assumption (`ASM-X`) is invalidated or a constraint (`CON-X`) changes in Context or Update mode, a follow-up is raised for this mode. Review every linked risk and work item, record the outcome, and keep the existing records and links. Do not convert an assumption into a risk.
- Review triggers, states and closure rules: see the lifecycle reference.

## 6. Interactive flow

1. Ask what could go wrong and what it would affect; draft the risk event, cause and impact.
2. Confirm the taxonomy lens, link and owner.
3. Rate likelihood, severity and proximity; show the result.
4. Offer the response menu; capture the required fields.
5. Recap (`yes / adjust`), save to `06`, log in `changelog.md`.
