# Scoring Rubric and Weighting Guide

This guide establishes the scoring standards, interactive scoring interview protocol, and mathematical weighting rules for evaluating public-sector project investments and requests for funding (RFF).

## Contents

- [The 10-point evaluation scale](#1-the-10-point-evaluation-scale)
- [Axis 1: Value / Return on Investment criteria rubric](#2-axis-1-value--return-on-investment-criteria-rubric)
- [Axis 2: Ability to Deliver criteria rubric](#3-axis-2-ability-to-deliver-criteria-rubric)
- [Mathematical weighting and scoring formulas](#4-mathematical-weighting-and-scoring-formulas)
- [Interactive interview workflow](#5-interactive-interview-workflow)

---

## 1. The 10-Point Evaluation Scale

Every criterion is evaluated on an anchored 0.0 to 10.0 scale (increments of 0.5):

| Score Range | Maturity & Evidence Level | Interpretation |
|---|---|---|
| **0.0 – 2.5** | Absent / Very Weak | Criterion is not met or evidence does not exist. Substantial risk or negligible value. |
| **3.0 – 4.5** | Preliminary / Weak | Partial evidence or minor alignment. Significant hurdles or limited public return. |
| **5.0 – 6.5** | Moderate / Acceptable | Baseline requirement met. Standard business value and manageable implementation effort. |
| **7.0 – 8.5** | Strong / Well-Evidenced | Clearly documented value or robust delivery readiness. High confidence. |
| **9.0 – 10.0** | Exceptional / Compelling | Mandatory driver, transformational public outcome, or turn-key, de-risked delivery. |

---

## 2. Axis 1: Value / Return on Investment Criteria Rubric

Default Category Weight: 100 points total (typically 25 points each).

### 1. Drivers (Default Weight: 25%)

> Evidence for this score comes from the business drivers (`DRV-X`) recorded in register `01`. Cite the driver IDs; a driver that is not recorded there is an assumption, not evidence.
- **0–3**: Discretionary idea; no legislative, legal, or risk imperative.
- **4–6**: Solves recurring operational pain or anticipated business need; non-urgent.
- **7–8**: Directly driven by formal ministry commitments, audit findings, or impending tech obsolescence.
- **9–10**: Explicit statutory mandate, binding court ruling, severe security/privacy vulnerability, or system failure risk.

### 2. Strategic Alignment (Default Weight: 25%)
- **0–3**: Narrow, isolated utility with no link to published ministry service plan goals.
- **4–6**: Indirectly supports administrative efficiency or operational hygiene.
- **7–8**: Directly reinforces major ministry strategic priorities or branch transformation objectives.
- **9–10**: Core enabler of provincial priorities (e.g., Access to Justice, DRIPA, modern digital public service).

### 3. Outcomes and Benefits (Default Weight: 25%)
- **0–3**: Negligible or cosmetic improvement; benefits confined to a handful of individuals.
- **4–6**: Measurable cycle time or error reduction for registry/court staff.
- **7–8**: Substantial citizen access enhancement, major operational time savings, or significant cost avoidance.
- **9–10**: Sector-wide transformation improving public trust, equity, and accessibility for hundreds of thousands of users.

### 4. Sector Benefits & Reusability (Default Weight: 25%)
- **0–3**: Completely bespoke silo; zero reuse potential for any other agency or court level.
- **4–6**: Architectural patterns or documentation may be shared with effort.
- **7–8**: Directly reusable API, service component, or data exchange standard for justice sector partners.
- **9–10**: Enterprise public-sector platform establishing an interoperable standard across government.

---

## 3. Axis 2: Ability to Deliver Criteria Rubric

Default Category Weight: 100 points total (typically 20 points each).

### 1. Readiness & Capacity (Default Weight: 20%)
- **0–3**: Severe change resistance, zero staff capacity, lack of operational management bandwidth.
- **4–6**: Willingness exists, but requires significant training and backfill to absorb the project.
- **7–8**: Core project team and operational change champions identified; capacity accounted for.
- **9–10**: Dedicated cross-functional team funded, organizational readiness validated, eager user base.

### 2. Extent of Research & Discovery (Default Weight: 20%)
- **0–3**: Problem asserted without user interviews, data, or comparative analysis.
- **4–6**: Initial problem brief completed; informal user surveys or basic desk research compiled.
- **7–8**: Formal discovery completed; user journey mapped, cross-jurisdictional review documented, architecture validated.
- **9–10**: Clickable prototype or pilot tested with live users; quantitative usability metrics available.

### 3. Investment Cost & Affordability (Default Weight: 20%)
*Note: Higher score denotes greater affordability / lower capital demand.*
- **0–3**: Massive multi-million dollar requirement, unbudgeted, high recurring licensing burden.
- **4–6**: Substantial capital required; feasible only with multi-year Treasury Board submission.
- **7–8**: Manageable capital and operating footprint; fits within existing branch capital envelop.
- **9–10**: Low or negligible cost; leverages existing shared platforms and staff resources.

### 4. Executive Sponsorship (Default Weight: 20%)
- **0–3**: No executive sponsor confirmed; grassroots proposal.
- **4–6**: Senior operational manager advocates, but no Assistant Deputy Minister or Executive Director sign-off.
- **7–8**: Strong sponsorship from Executive Director or Assistant Deputy Minister with regular governance reporting.
- **9–10**: Coordinated joint sponsorship across Ministry Executive, Court Services Branch, and Judiciary.

### 5. Ease of Implementation & Low Complexity (Default Weight: 20%)
*Note: Higher score denotes lower complexity / easier delivery.*
- **0–3**: Extremely high complexity, legacy mainframe dependencies, heavy privacy/security hurdles, contested governance.
- **4–6**: Moderate complexity involving multiple institutional handoffs and bespoke custom integration.
- **7–8**: Standard modern architecture, low legacy footprint, well-understood deployment patterns.
- **9–10**: Turnkey, cloud-native SaaS or standard component; fast time-to-value with minimal external dependencies.

---

## 4. Mathematical Weighting and Scoring Formulas

### Category Normalized Value Score ($V_i$)
$$V_i = \sum_{c \in \text{Value Categories}} \left( \text{RawScore}_{i,c} \times \frac{\text{Weight}_c}{\sum \text{Value Weights}} \right)$$

### Category Normalized Delivery Score ($D_i$)
$$D_i = \sum_{c \in \text{Delivery Categories}} \left( \text{RawScore}_{i,c} \times \frac{\text{Weight}_c}{\sum \text{Delivery Weights}} \right)$$

### Overall Composite Score ($C_i$)
$$C_i = V_i \times \left(\frac{\text{AxisWeight}_V}{100}\right) + D_i \times \left(\frac{\text{AxisWeight}_D}{100}\right)$$

---

## 5. Interactive Interview Workflow

When guiding users through scoring:
1. Present 1 candidate proposal at a time.
2. Ask 1–2 criteria per turn, showing the plain-language rubric anchors.
3. Allow the user to provide a raw score (e.g. 7.5) and a brief supporting rationale.
4. Auto-calculate the resulting Value and Delivery coordinates.
5. Provide a recap gate showing where the item lands in the 4-quadrant matrix before writing to the ledger.
