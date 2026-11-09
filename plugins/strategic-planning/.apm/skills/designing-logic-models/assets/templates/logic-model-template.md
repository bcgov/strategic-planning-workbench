# Logic Model & Results Chain: [Initiative or Objective Name]

> **Status**: Draft | Reviewed | Approved  
> **Date**: [YYYY-MM-DD]  
> **Owning Team**: [Team Name]  
> **Related Register IDs**: `OBJ-[X]`, `WORK-[X]`, `BEN-[X]`, `CAP-[X]`, `MSR-[X]`  
> **Methodology Depth**: Simple | Extended | Measurement-Ready (Logframe)

---

## 1. Context & Problem Statement

- **Need or Problem**: [Describe the current condition, bottleneck, or opportunity that justifies this intervention]
- **Target Population / Beneficiaries**: [Identify the client groups, staff roles, or justice system participants directly affected]
- **Scope & Delivery Bounds**: [Clarify what is inside versus outside the boundary of this initiative]

---

## 2. Canonical Results Chain

```mermaid
%%{init: {"flowchart": {"wrappingWidth": 450, "minNodeWidth": 350}} }%%
flowchart TB

N["PROGRAM NEED<br/>[Current operational problem or policy gap]"]
I["INPUTS<br/>[What we invest: funding, court policy, expertise, platform]"]
A["ACTIVITIES<br/>[What we do: encode rules, validation, integrations, training]"]
O["OUTPUTS<br/>[What we produce: validation portal, APIs, schemas, tools]"]
IO["IMMEDIATE OUTCOMES<br/>[What changes first: earlier client feedback, structured data]"]
MO["INTERMEDIATE OUTCOMES<br/>[What changes next: fewer rejected filings, faster delivery]"]
LO["LONG-TERM OUTCOMES<br/>[Ultimate impact: timely, accessible, sustainable court services]"]

N -->|"justifies"| I
I -->|"enables"| A
A -->|"produces"| O
O -->|"leads to"| IO
IO -->|"contributes to"| MO
MO -->|"contributes to"| LO

classDef need fill:#F4F4F4,stroke:#555,color:#111
classDef input fill:#E8F1FA,stroke:#2B6EA6,color:#111
classDef activity fill:#E5F3F3,stroke:#258080,color:#111
classDef output fill:#E9F4E4,stroke:#518A3A,color:#111
classDef immediate fill:#FFF4D6,stroke:#C49102,color:#111
classDef intermediate fill:#FCE8D5,stroke:#C76B19,color:#111
classDef longterm fill:#F3E5F5,stroke:#7B4B94,color:#111

class N need
class I input
class A activity
class O output
class IO immediate
class MO intermediate
class LO longterm
```

> **Tip**: For compact 5-stage views without the Program Need box, switch to `flowchart LR` using direct `style` tokens. Generate automatically via `python scripts/generate_mermaid.py`.

---

## 3. Results Chain Matrix

| Stage | Element ID | Statement | Critical Assumptions & External Factors | Target Horizon | Indicators & Verification |
|---|---|---|---|---|---|
| **Inputs** | `INP-01` | [Investment statement] | [Resource availability] | Month 0 | [Budget / FTE tracking] |
| **Activities** | `ACT-01` | [Team work performed] | [Staff availability] | Months 1–3 | [Sprint progress logs] |
| **Outputs** | `OUT-01` | [Deliverable produced] | [Technical dependency] | Month 4 | [Release acceptance] |
| **Immediate Outcomes** | `IMM-01` | [Early user uptake] | [User willingness to adopt] | Months 4–6 | [Active user count] |
| **Intermediate Outcomes** | `INT-01` | [Behavioral shift] | [Process continuity] | Months 6–18 | [Turnaround time reduction] |
| **Long-Term Outcomes** | `LNG-01` | [Enduring public value] | [Partner policy alignment] | Years 2–4 | [Annual client survey] |

---

## 4. Theory of Change Causal Rationale

- **Outputs ──> Immediate Outcomes**: [Explain *why* releasing this output will cause users or staff to change behavior]
- **Immediate ──> Intermediate Outcomes**: [Explain *how* initial adoption translates into sustained operational efficiency]
- **Intermediate ──> Long-Term Outcomes**: [Explain the team's contribution to broader provincial or ministry mandates]

---

## 5. Risk & Validation Audit

- [ ] Activities and outputs are not confused with outcomes (VAL-01, VAL-03).
- [ ] No causal leaps or missing intermediate stepping stones (VAL-07).
- [ ] Technology implementation is treated as an enabler, not the final benefit (VAL-11).
- [ ] Direct control is claimed only for outputs; long-term results state contribution (VAL-05).
