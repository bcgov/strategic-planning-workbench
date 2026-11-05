# Visual Strategy Package (Mermaid Diagrams & Roadmaps)

**Branch / Team:** [Name]  

## 1. Five-Tier Organizational Line-of-Sight (`Province -> Ministry -> CSB -> Division -> Team`)

```mermaid
flowchart TD
    T1["Tier 1 (BC Gov): [Provincial Mandate]"]
    T2["Tier 2 (Ministry of AG): [Ministry Goal]"]
    T3["Tier 3 (Court Services Branch): [CSB Strategic Pillar]"]
    T4["Tier 4 (Division): [Divisional Priority]"]
    OBJ1["Tier 5 (Team OBJ-1): [Outcome Objective 1]"]
    OBJ2["Tier 5 (Team OBJ-2): [Outcome Objective 2]"]

    T1 --> T2 --> T3 --> T4
    T4 --> OBJ1
    T4 --> OBJ2
```

## 2. End-to-End Strategy, Capability & Portfolio Alignment Map

```mermaid
flowchart LR
    OBJ1["OBJ-1: [Outcome Objective]"] --> CAP1["CAP-001: [Capability Name] (L1 -> L3)"]
    CAP1 --> WORK1["WORK-001: [Committed Initiative] (Active)"]
    CAP1 -.-> IDEA1["IDEA-002: [Candidate Opportunity] (Gate Pending)"]

    style IDEA1 stroke-dasharray: 5 5
```

## 3. Capability Maturity Gap Chart (`Current vs. Target`)

```mermaid
xychart-beta
    title "Business Capability Maturity (Current vs Target)"
    x-axis ["CAP-001", "CAP-002", "CAP-003", "CAP-004"]
    y-axis "Maturity Level (0-5)" 0 --> 5
    bar [1, 2, 1, 2]
    line [3, 4, 3, 4]
```

## 4. High-Level Strategic Roadmap & Decision Gate Gantt Chart

> **Note:** Solid bars represent **Committed Work (`WORK-X`)**. Milestones (`◆`) represent **Validation & Promotion Decision Gates (`GATE-X` / `IDEA-X`)**.

```mermaid
gantt
    title Strategic Roadmap: Horizons, Committed Initiatives & Decision Gates
    dateFormat YYYY-MM-DD
    axisFormat %Y-Q%q

    section Horizon 1 (Now)
    WORK-001 Foundational Capability :active, w1, 2026-04-01, 2026-09-30
    GATE-001 Validate Assumption ASM-001 :milestone, g1, 2026-09-30, 0d

    section Horizon 2 (Next)
    WORK-002 Capability Expansion :w2, 2026-10-01, 2027-03-31
    GATE-002 Promotion Decision for IDEA-002 :milestone, g2, 2027-01-15, 0d

    section Horizon 3 (Later)
    CAP-004 Long-Term Transformation Horizon :w3, 2027-04-01, 2027-12-31
```
