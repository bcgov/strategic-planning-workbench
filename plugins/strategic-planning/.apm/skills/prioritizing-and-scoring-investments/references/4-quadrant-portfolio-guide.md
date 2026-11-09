# Four-Quadrant Portfolio Guide

This guide describes how to interpret, communicate, and act upon the **Value vs. Ability to Deliver 4-Quadrant Portfolio Matrix**.

---

## 1. Visualizing the Portfolio Landscape

The portfolio matrix maps candidate investments along two orthogonal dimensions:
- **Horizontal Axis (X)**: Ability to Deliver / Readiness (0.0 to 10.0)
- **Vertical Axis (Y)**: Value / Return on Investment (0.0 to 10.0)

```text
 10 ┌───────────────────────────────┬───────────────────────────────┐
    │                               │                               │
    │  Quadrant 2: Strategic Bets   │  Quadrant 1: High Priority    │
    │  (High Value × Low Delivery)  │  (High Value × High Delivery) │
    │                               │                               │
    │  Action: De-risk & Discover   │  Action: Fund & Execute       │
Y   │                               │                               │
    ├───────────────────────────────┼───────────────────────────────┤ 5.0 Threshold
    │                               │                               │
    │  Quadrant 4: Defer / Retire   │  Quadrant 3: Tactical Quick   │
    │  (Low Value × Low Delivery)   │  (Low Value × High Delivery)  │
    │                               │                               │
    │  Action: Decline or Archive   │  Action: Deliver if Bandwidth │
  0 └───────────────────────────────┴───────────────────────────────┘
    0                              5.0                             10
                                    X (Ability to Deliver)
```

---

## 2. Quadrant Definitions and Executive Actions

### Quadrant 1: Strategic Priorities & Quick Wins (Top-Right)
- **Criteria Profile**: Value $\ge 5.0$, Ability to Deliver $\ge 5.0$.
- **Characteristics**: Clear legislative or operational imperative, substantial public/citizen benefit, validated research, engaged executive sponsor, and high organizational readiness.
- **Recommended Action**: **Fund and prioritize immediately**. These initiatives represent the core commitments of the capital plan and should be promoted directly into `managing-work-inventory` (`WORK-X`).

### Quadrant 2: Strategic Big Bets (Top-Left)
- **Criteria Profile**: Value $\ge 5.0$, Ability to Deliver $< 5.0$.
- **Characteristics**: Transformational potential and high stakeholder demand, but hindered by low discovery maturity, architectural uncertainty, high cost, or constrained organizational readiness.
- **Recommended Action**: **Fund phased discovery and de-risking**. Do not commit full multi-million capital budgets until technical spikes, service design, or privacy impact assessments increase deliverability past the 5.0 threshold.

### Quadrant 3: Tactical Efficiencies & Low-Hanging Fruit (Bottom-Right)
- **Criteria Profile**: Value $< 5.0$, Ability to Deliver $\ge 5.0$.
- **Characteristics**: Straightforward, turn-key, or low-cost projects with localized or incremental benefit.
- **Recommended Action**: **Deliver opportunistically**. Execute if spare delivery bandwidth exists or bundle into larger modernization initiatives. Avoid diverting resources from Quadrant 1 commitments.

### Quadrant 4: Deprioritize & Defer (Bottom-Left)
- **Criteria Profile**: Value $< 5.0$, Ability to Deliver $< 5.0$.
- **Characteristics**: Discretionary or cosmetic ideas facing high technical friction, absent sponsorship, or unvalidated problems.
- **Recommended Action**: **Decline funding or defer**. Log explicit rationale in `strategy/07-idea-inventory.md` under `rejected` or `deferred` status to maintain transparent institutional memory without cluttering active delivery backlogs.

---

## 3. Portfolio Balance Guidelines for Executive Boards

For a healthy public-sector capital portfolio:
- **60% – 70% of Funding**: Quadrant 1 (core strategic priorities delivering predictable value).
- **20% – 30% of Funding**: Quadrant 2 (time-boxed discovery investments de-risking next year's pipeline).
- **10% of Funding**: Quadrant 3 (tactical continuous improvement and operational hygiene).
- **0% of Funding**: Quadrant 4 (active elimination of unfocused pet projects).

---

## 4. Downstream Traceability

```text
[Investment Scoring Matrix]
         │
         ├── Q1 (Strategic Priority) ──> Promote to `managing-work-inventory` (WORK-X)
         │                                 └── Sequence into Now/Next in `sequencing-roadmaps-and-measures`
         │
         ├── Q2 (Strategic Big Bet)  ──> Commission Discovery in `managing-work-inventory` (time-boxed spike)
         │                                 └── Retain proposal record in `managing-idea-inventory`
         │
         ├── Q3 (Tactical Win)       ──> Queue for spare capacity in `managing-work-inventory`
         │
         └── Q4 (Deprioritize)       ──> Record rejection rationale in `strategy/07-idea-inventory.md`
```
