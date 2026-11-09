# Worked Example 2: Workforce Training & Capability Development

> **Initiative ID**: `WORK-024`  
> **Scope**: In-House Digital Delivery & Cloud Skills Academy  
> **Methodology Depth**: Extended Logic Model

---

## 1. Context & Scope

- **Need / Problem**: Internal development teams rely on manual testing and monolithic releases, causing frequent release outages and heavy vendor dependency.
- **Target Population**: Internal software engineers, technical leads, QA specialists, and engineering managers.

---

## 2. Results Chain Diagram

```mermaid
%%{init: {"flowchart": {"wrappingWidth": 460, "minNodeWidth": 360}} }%%
flowchart TD
    IN2["<b>INPUTS</b><br/>Training budget ($90k)<br/>Cloud lab sandbox environments<br/>Senior engineering mentors"]
    AC2["<b>ACTIVITIES</b><br/>Design hands-on CI/CD curriculum<br/>Run weekly pair-programming labs<br/>Refactor real pipeline modules"]
    OP2["<b>OUTPUTS</b><br/>6 modular learning tracks published<br/>40 certified internal engineers<br/>Automated test scaffolding library"]
    IM2["<b>IMMEDIATE OUTCOMES</b><br/>Engineers write automated tests<br/>Pipelines deploy to lower environments<br/>Confidence in release automation"]
    IT2["<b>INTERMEDIATE OUTCOMES</b><br/>Lead time drops from 6 weeks to 3 days<br/>Change failure rate drops below 2%<br/>Reduced vendor staff augmentation"]
    LT2["<b>LONG-TERM OUTCOMES</b><br/>Sustainable, resilient in-house delivery<br/>Rapid adaptation to public mandates"]

    IN2 -->|"enables"| AC2
    AC2 -->|"produces"| OP2
    OP2 -->|"leads to"| IM2
    IM2 -->|"contributes to"| IT2
    IT2 -->|"contributes to"| LT2

    style IN2 fill:#E8F1FA,stroke:#2B6EA6,stroke-width:2px,color:#111
    style AC2 fill:#E5F3F3,stroke:#258080,stroke-width:2px,color:#111
    style OP2 fill:#E9F4E4,stroke:#518A3A,stroke-width:2px,color:#111
    style IM2 fill:#FFF4D6,stroke:#C49102,stroke-width:2px,color:#111
    style IT2 fill:#FCE8D5,stroke:#C76B19,stroke-width:2px,color:#111
    style LT2 fill:#F3E5F5,stroke:#7B4B94,stroke-width:2px,color:#111
```

---

## 3. Results Chain Details

| Stage | Element | Key Deliverables & Expected Changes |
|---|---|---|
| **Inputs** | Training budget ($90k), learning management platform, cloud lab sandbox environments, 2 senior engineering mentors |
| **Activities** | Design interactive cloud curriculum, conduct weekly pair-programming labs, evaluate real codebase refactoring projects |
| **Outputs** | 6 modular training tracks published, 40 staff software engineers complete hands-on sandbox certification |
| **Immediate Outcomes** | Engineers demonstrate confidence writing automated integration tests and running CI/CD deployment pipelines |
| **Intermediate Outcomes** | Software delivery lead time decreases from 6 weeks to 3 days; change failure rate drops from 22% to under 2% |
| **Long-Term Outcomes** | Sustainable, resilient in-house digital delivery capability that adapts rapidly to changing public service mandates |

---

## 4. Critical Assumptions & Common Mistakes

- **Assumptions**: Managers protect 4 hours/week for staff learning; teams have repository permissions to modernize pipelines.
- **Common Mistake Avoided**: Stating "40 engineers trained" as an outcome (VAL-03). Completion of training is an Output; applying automation to slash deployment lead times is the Outcome.
