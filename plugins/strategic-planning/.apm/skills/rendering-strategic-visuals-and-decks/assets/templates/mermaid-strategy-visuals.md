# Visual Strategy Package (Mermaid Diagrams & Roadmaps)

**Branch / Team:** [Name]  

## 1. Five-Tier Organizational Line-of-Sight (`Province -> Ministry -> CSB -> Division -> Team`)

```mermaid
flowchart TD
    T1["Tier 1 (BC Gov):<br>[Provincial<br>Mandate]"]
    T2["Tier 2 (AG):<br>[Ministry<br>Goal]"]
    T3["Tier 3 (CSB):<br>[Branch<br>Pillar]"]
    T4["Tier 4 (Div):<br>[Divisional<br>Priority]"]
    OBJ1["Tier 5 (OBJ-1):<br>[Outcome<br>Objective 1]"]
    OBJ2["Tier 5 (OBJ-2):<br>[Outcome<br>Objective 2]"]

    T1 --> T2 --> T3 --> T4
    T4 --> OBJ1
    T4 --> OBJ2
```

## 2. End-to-End Strategy, Capability & Portfolio Alignment Map

```mermaid
flowchart LR
    OBJ1["OBJ-1:<br>[Outcome<br>Objective]"] --> CAP1["CAP-001:<br>[Capability]<br>(L1 -> L3)"]
    CAP1 --> WORK1["WORK-001:<br>[Committed<br>Initiative]"]
    CAP1 -.-> IDEA1["IDEA-002:<br>[Candidate<br>Opportunity]"]

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

## 5. Value Stream to Capability Cross-Map (TOGAF Phase B)

```mermaid
flowchart LR
    subgraph V["Value Stream: VST-001"]
        S1["Stage 1:<br>Intake &<br>Triage"] --> S2["Stage 2:<br>Guidance &<br>Processing"]
        S2 --> S3["Stage 3:<br>Resolution &<br>Assurance"]
    end

    CAP1["CAP-001:<br>Policy Triage<br>(L1 -> L3)"] -.-> S1
    CAP2["CAP-002:<br>Knowledge Mgmt<br>(L1 -> L3)"] -.-> S2
    CAP3["CAP-003:<br>Quality Metrics<br>(L1 -> L4)"] -.-> S3
```
