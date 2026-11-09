# Worked Example 1: Court Registry Digital E-Filing System

> **Initiative ID**: `WORK-012`  
> **Scope**: Provincial Court Registry Modernization  
> **Methodology Depth**: Extended Logic Model

---

## 1. Context & Scope

- **Need / Problem**: Paper court filings require in-person registry visits, manual entry into legacy mainframes, and cause 10-day processing backlogs for unrepresented litigants.
- **Target Population**: Self-represented litigants, legal counsel, court registry clerks, and trial coordinators.

---

## 2. Results Chain Diagram

```mermaid
%%{init: {"flowchart": {"wrappingWidth": 460, "minNodeWidth": 360}} }%%
flowchart TD
    IN1["<b>INPUTS</b><br/>Modern cloud platform<br/>Target capital funding<br/>Court registry expertise"]
    AC1["<b>ACTIVITIES</b><br/>Design e-filing web portal<br/>Map statutory court filing rules<br/>Train court registry clerks"]
    OP1["<b>OUTPUTS</b><br/>WCAG 2.1 AA e-filing portal<br/>Digitized filing checklists<br/>85 certified court clerks"]
    IM1["<b>IMMEDIATE OUTCOMES</b><br/>Litigants submit filings online<br/>Clerks verify submissions digitally<br/>Earlier document rejection feedback"]
    IT1["<b>INTERMEDIATE OUTCOMES</b><br/>Turnaround drops from 10 days to 24 hours<br/>Counter lineups and calls cut by 60%<br/>Filing error rates drop below 5%"]
    LT1["<b>LONG-TERM OUTCOMES</b><br/>Timely, accessible and equitable justice<br/>Sustainable digital court operations"]

    IN1 -->|"enables"| AC1
    AC1 -->|"produces"| OP1
    OP1 -->|"leads to"| IM1
    IM1 -->|"contributes to"| IT1
    IT1 -->|"contributes to"| LT1

    style IN1 fill:#E8F1FA,stroke:#2B6EA6,stroke-width:2px,color:#111
    style AC1 fill:#E5F3F3,stroke:#258080,stroke-width:2px,color:#111
    style OP1 fill:#E9F4E4,stroke:#518A3A,stroke-width:2px,color:#111
    style IM1 fill:#FFF4D6,stroke:#C49102,stroke-width:2px,color:#111
    style IT1 fill:#FCE8D5,stroke:#C76B19,stroke-width:2px,color:#111
    style LT1 fill:#F3E5F5,stroke:#7B4B94,stroke-width:2px,color:#111
```

---

## 3. Results Chain Details

| Stage | Element | Key Deliverables & Expected Changes |
|---|---|---|
| **Inputs** | Capital funding ($450k), CSB digital team FTEs, modern cloud infrastructure, judicial practice directives |
| **Activities** | Map court filing rules, conduct UX testing with clerks and litigants, build WCAG 2.1 AA web form, deliver training |
| **Outputs** | Modern e-filing web application, digitized filing checklists, 85 court clerks trained, updated public practice notices |
| **Immediate Outcomes** | Self-represented litigants submit online from home; clerks process structured electronic submissions without re-typing |
| **Intermediate Outcomes** | Filing turnaround drops from 10 business days to 24 hours; counter lineups and telephone inquiries decrease by 60% |
| **Long-Term Outcomes** | Equitable, timely access to justice for British Columbians regardless of geographic location or mobility limitations |

---

## 4. Critical Assumptions & Common Mistakes

- **Assumptions**: Legal counsel and the public have reliable internet access; the judiciary accepts digitally authenticated document stamps.
- **Common Mistake Avoided**: Listing "E-filing application built" as an outcome (VAL-03). The software build is an Output; the operational change in filing speed and counter reduction is the Outcome.
