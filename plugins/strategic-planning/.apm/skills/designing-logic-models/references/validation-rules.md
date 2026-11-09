# Logic Model Validation Rules & Anti-Patterns

## Contents

- [The 15 Anti-Pattern Validation Checks](#the-15-anti-pattern-validation-checks)
- [Severity Levels & Remediation Guidance](#severity-levels--remediation-guidance)
- [Automated Audit Checklist](#automated-audit-checklist)

---

## The 15 Anti-Pattern Validation Checks

Before finalizing any logic model, evaluate each element against these 15 rules:

| Rule Code | Anti-Pattern | Description | Example of Error | Remediation |
|---|---|---|---|---|
| **VAL-01** | **Activity written as outcome** | Stating an internal operational action as if it were a result. | *"Outcome: Conduct 15 court stakeholder interviews."* | Reframe to the resulting change: *"Stakeholder concerns and operational barriers are documented and validated."* |
| **VAL-02** | **Output written as activity** | Expressing a deliverable as a continuous verb phrase instead of a completed object. | *"Output: Designing the digital scheduling tool."* | Reframe to the deliverable: *"Digital court scheduling portal deployed to production."* |
| **VAL-03** | **Output mistaken for outcome** | Treating the delivery of a widget or document as evidence of successful change. | *"Immediate outcome: Modernized filing guidelines published on intranet."* | Move to Output. Frame outcome as user adoption: *"Registry staff reference new guidelines, decreasing document rejections by 30%."* |
| **VAL-04** | **Vague outcome statement** | Using hollow words ("better", "enhanced", "streamlined") without specifying what changes. | *"Outcome: Enhanced justice system efficiency."* | State the specific mechanism: *"Court hearing delays caused by lost paperwork reduced from 18% to under 2%."* |
| **VAL-05** | **Over-claimed attribution** | Claiming full team control over a systemic, multi-partner result. | *"Project deliverable will eliminate court backlogs across British Columbia."* | Clarify attribution boundary: Project outputs *contribute* to backlog reduction in cooperation with judiciary and Crown. |
| **VAL-06** | **Missing target beneficiary or system** | Omitting the specific human group, client segment, or organizational unit affected. | *"Outcome: Faster response times."* | Name the actor: *"Small claims litigants receive hearing confirmation within 48 hours."* |
| **VAL-07** | **Causal leap / Missing intermediate step** | Jumping directly from an early output to a distant societal impact with no intervening steps. | *"Output: Train 10 analysts" ──> "Long-term: Reduced provincial public debt."* | Insert immediate and intermediate outcomes (skills gained -> faster policy turnaround -> reduced program cost). |
| **VAL-08** | **Circular reasoning / Tautology** | Defining the outcome simply as the presence of the activity or output. | *"Activity: Implement case tracking" ──> "Outcome: Cases are tracked."* | Identify the behavioral or decision shift: *"Judicial managers reallocate courtroom resources based on real-time docket loads."* |
| **VAL-09** | **Duplicate concept at multiple levels** | Listing the identical concept across activities, outputs, and outcomes. | *"Training delivered" (activity), "Training provided" (output), "Staff trained" (outcome).* | Restrict to distinct causal states: Activity = conduct workshops; Output = 40 clerks certified; Outcome = filing error rate drops. |
| **VAL-10** | **Metric disguised as outcome** | Stating an arbitrary KPI number without naming the real-world operational change. | *"Outcome: 5,000 transactions."* | Identify the outcome behind the count: *"Citizens resolve uncontested legal forms independently without visiting a court counter."* |
| **VAL-11** | **Tech implementation as final benefit** | Treating software deployment or tool migration as the ultimate public value. | *"Long-term outcome: 100% cloud migration on Microsoft Azure."* | Tech is an input/output. Public value is service reliability, data security, and zero downtime for court sittings. |
| **VAL-12** | **Dead-end output (No identified users)** | Generating a report, portal, or tool that has no defined consumer or uptake path. | *"Output: Bi-weekly statistical summary PDF produced." (with no downstream link).* | Either identify who uses it to make what decision, or eliminate the unneeded output. |
| **VAL-13** | **Unsupported outcome (No enabling output)** | Expecting an outcome to materialize with no deliverable designed to provoke it. | *"Immediate outcome: Lawyers use electronic document upload." (but no upload portal is built).* | Add the missing output or activity required to enable the change. |
| **VAL-14** | **Unsupported causal hypothesis** | Asserting a causal link with no plausible behavioral or operational logic. | *"Output: New intranet banner" ──> "Immediate outcome: 50% increase in employee retention."* | Reject the link or require documented evidence/precedent before accepting. |
| **VAL-15** | **Inconsistent time horizons** | Assigning an unrealistic timeline for complex institutional or cultural change. | *"Immediate outcome (Month 1): Institutional culture transformed across all court registries."* | Move cultural/behavioral maturation to Intermediate or Long-term outcomes (Months 12–24+). |

---

## Severity Levels & Remediation Guidance

- **Blocker (Must resolve before saving)**: VAL-01 (Activity as outcome), VAL-03 (Output as outcome), VAL-07 (Causal leap), VAL-11 (Tech as final value).
- **Warning (Coach user to improve)**: VAL-04 (Vague outcome), VAL-05 (Over-attribution), VAL-06 (Missing beneficiary), VAL-10 (Metric as outcome).
- **Advisory (Clarify during extended review)**: VAL-14 (Causal hypothesis), VAL-15 (Time horizon alignment).

---

## Automated Audit Checklist

When auditing a user's proposed model, report findings in a concise table:

```text
| Element ID | Stage | Finding / Rule | Suggested Remediation |
|---|---|---|---|
| ACT-02 | Activities | VAL-01: Written as outcome | Reframe from passive goal to concrete team action |
| OUT-04 | Outputs | VAL-12: Dead-end output | Connect to immediate user uptake or mark for deprecation |
| OUC-01 | Immediate | VAL-03: Output mistaken for outcome | Move deliverable to Outputs; focus on client behavior |
```
