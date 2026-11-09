# Output Templates & Representation Formats

## Contents

- [Mermaid Flowchart Syntax Guidelines](#mermaid-flowchart-syntax-guidelines)
- [Canonical B.C. Government Mermaid Palette](#canonical-bc-government-mermaid-palette)
- [Program Need Link and ClassDef Styling](#program-need-link-and-classdef-styling)
- [Python Mermaid Generator Script](#python-mermaid-generator-script)
- [Standard Markdown Tabular Format](#standard-markdown-tabular-format)
- [Logframe Matrix Template](#logframe-matrix-template)
- [JSON Schema](#json-schema)
- [YAML Schema](#yaml-schema)

---

## Mermaid Flowchart Syntax Guidelines

To ensure robust rendering across all markdown viewers, IDEs, and documentation platforms:
1. **Line length**: Keep every source line under 200 characters.
2. **Node IDs**: Use short identifiers (`I`, `A`, `O`, `IO`, `MO`, `LO` or `INP1`, `ACT1`, `OUT1`, `IMM1`, `INT1`, `LNG1`). When starting with a Program Need, use `N`.
3. **Escaping**: Always quote node text: `id["Text here"]`. Avoid nested raw quotes or special characters (`()`, `[]`, `{}`) without proper escaping.
4. **Line breaks**: Use `<br/>` for line breaks within node labels.
5. **Causal link labels**:
   - Program Need to Inputs: `-->|"justifies"|`
   - Inputs to Activities: `-->|"enables"|`
   - Activities to Outputs: `-->|"produces"|`
   - Outputs to Immediate Outcomes: `-->|"leads to"|`
   - Immediate to Intermediate Outcomes: `-->|"contributes to"|`
   - Intermediate to Long-term Outcomes: `-->|"contributes to"|`
6. **Layout**:
   - Use `flowchart LR` for compact models with brief text.
   - Use `flowchart TB` when nodes contain multi-line descriptions, multiple items per stage, or a top Program Need block.
7. **Box width & text wrapping**:
   - Mermaid defaults to a narrow `120px` wrapping width, which clips multi-line text horizontally.
   - Always include an `%%{init: ...}%%` directive at the top of the diagram:
     - For `flowchart TB`: `%%{init: {"flowchart": {"wrappingWidth": 450, "minNodeWidth": 350}} }%%`
     - For `flowchart LR`: `%%{init: {"flowchart": {"wrappingWidth": 260, "minNodeWidth": 220}} }%%`

---

## Canonical B.C. Government Mermaid Palette

Use these high-contrast, accessible token hex values:

```mermaid
%% Direct style syntax
style N fill:#F4F4F4,stroke:#555555,stroke-width:2px
style I fill:#E8F1FA,stroke:#2B6EA6,stroke-width:2px
style A fill:#E5F3F3,stroke:#258080,stroke-width:2px
style O fill:#E9F4E4,stroke:#518A3A,stroke-width:2px
style IO fill:#FFF4D6,stroke:#C49102,stroke-width:2px
style MO fill:#FCE8D5,stroke:#C76B19,stroke-width:2px
style LO fill:#F3E5F5,stroke:#7B4B94,stroke-width:2px
```

| Stage | Fill Color | Stroke Color | Semantic Meaning |
|---|---|---|---|
| **Program Need (N)** | `#F4F4F4` (Light Grey) | `#555555` (Grey) | Justifying Problem / Operational Reality |
| **Inputs (I)** | `#E8F1FA` (Light Blue) | `#2B6EA6` (Blue) | Investment & Resource Foundation |
| **Activities (A)** | `#E5F3F3` (Light Teal) | `#258080` (Teal) | Work Performed |
| **Outputs (O)** | `#E9F4E4` (Light Green) | `#518A3A` (Green) | Controllable Deliverables |
| **Immediate Outcomes (IO)** | `#FFF4D6` (Light Gold) | `#C49102` (Gold) | Early Access & Skill Shifts |
| **Intermediate Outcomes (MO)** | `#FCE8D5` (Light Orange) | `#C76B19` (Orange) | Practice & Operational Changes |
| **Long-Term Outcomes (LO)** | `#F3E5F5` (Light Purple) | `#7B4B94` (Purple) | Enduring Public & Social Impact |

---

## Program Need Link and ClassDef Styling

Alternatively, define classes with `classDef` for clean visual separation:

```mermaid
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

---

## Python Mermaid Generator Script

The skill provides an automated generator script at `scripts/generate_mermaid.py`:

```bash
# Generate top-to-bottom Need-driven court modernization diagram
python scripts/generate_mermaid.py --preset need-driven

# Generate left-to-right canonical digital service transformation diagram
python scripts/generate_mermaid.py --preset canonical-lr

# Generate from a custom JSON definition and save to file
python scripts/generate_mermaid.py --input my-model.json --layout TB --style classDef --output model.mmd
```

---

## Standard Markdown Tabular Format

```markdown
### Logic Model: [Initiative or Objective Name]

| Stage | Element ID | Statement & Scope | Key Assumptions & Dependencies | Accountability / Target Date |
|---|---|---|---|---|
| **Inputs** | INP-01 | [What we invest] | [Resource availability] | [Branch / Sponsor] |
| **Activities** | ACT-01 | [What we do] | [Specialist capability] | [Team Lead] |
| **Outputs** | OUT-01 | [What we produce] | [Technical dependency] | [Release Date] |
| **Immediate Outcomes** | IMM-01 | [What changes first] | [User awareness & uptake] | [3–6 Months] |
| **Intermediate Outcomes** | INT-01 | [What changes next] | [Operating practice change] | [6–18 Months] |
| **Long-Term Outcomes** | LNG-01 | [Ultimate public impact] | [Multi-partner cooperation] | [2–4 Years] |
```

---

## Logframe Matrix Template

```markdown
| Results Hierarchy | Narrative Summary | Objectively Verifiable Indicators (OVI) | Means of Verification (MoV) | Critical Assumptions & Risks |
|---|---|---|---|---|
| **Impact (Long-Term)** | Enduring public outcome | Macro trend indicator (e.g. public clearance rate) | Annual ministry reports, justice data audits | Judicial policy stability |
| **Outcomes (Intermediate)** | Systemic behavioral shift | Performance measure (e.g. days to file resolution) | Court administration BI database | Staff retention & adoption |
| **Outcomes (Immediate)** | Early capacity or access uptake | Adoption rate (% digital submissions) | Digital service telemetry logs | Legal profession readiness |
| **Outputs** | Tangible deliverables | Output quantity (e.g. 1 portal, 5 guides) | Delivery acceptance sign-off | Vendor delivery milestones |
| **Activities & Inputs** | Work packages & resources | Budget spent ($), FTE hours allocated | Financial reports, team timesheets | Budget appropriation approved |
```

---

## JSON Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "LogicModel",
  "type": "object",
  "properties": {
    "id": { "type": "string" },
    "title": { "type": "string" },
    "scope": { "type": "string", "enum": ["program", "objective", "initiative", "policy"] },
    "targetPopulation": { "type": "string" },
    "needOrProblem": { "type": "string" },
    "inputs": { "type": "array", "items": { "$ref": "#/$defs/element" } },
    "activities": { "type": "array", "items": { "$ref": "#/$defs/element" } },
    "outputs": { "type": "array", "items": { "$ref": "#/$defs/element" } },
    "immediateOutcomes": { "type": "array", "items": { "$ref": "#/$defs/element" } },
    "intermediateOutcomes": { "type": "array", "items": { "$ref": "#/$defs/element" } },
    "longTermOutcomes": { "type": "array", "items": { "$ref": "#/$defs/element" } }
  },
  "required": ["id", "title", "inputs", "activities", "outputs", "immediateOutcomes", "intermediateOutcomes", "longTermOutcomes"],
  "$defs": {
    "element": {
      "type": "object",
      "properties": {
        "id": { "type": "string" },
        "statement": { "type": "string" },
        "actorOrOwner": { "type": "string" },
        "timeHorizon": { "type": "string" },
        "indicators": { "type": "array", "items": { "type": "string" } },
        "assumptions": { "type": "array", "items": { "type": "string" } },
        "downstreamLinks": { "type": "array", "items": { "type": "string" } }
      },
      "required": ["id", "statement"]
    }
  }
}
```

---

## YAML Schema

```yaml
logic_model:
  id: "LM-CSB-001"
  title: "Digital Court Scheduling Initiative"
  scope: "initiative"
  target_population: "Court registry clerks, trial coordinators, judicial officers, litigants"
  need_or_problem: "Manual telephone and paper scheduling causes hearing trial delays."
  inputs:
    - id: "INP-01"
      statement: "Digital transformation capital funding ($240,000)"
  activities:
    - id: "ACT-01"
      statement: "Design automated docket reservation workflow"
  outputs:
    - id: "OUT-01"
      statement: "Online court calendar reservation portal deployed"
  immediate_outcomes:
    - id: "IMM-01"
      statement: "Legal counsel book contested motions online without clerk phone calls"
  intermediate_outcomes:
    - id: "INT-01"
      statement: "Registry scheduling turnaround drops from 8 business days to same day"
  long_term_outcomes:
    - id: "LNG-01"
      statement: "Timely access to court hearings across British Columbia regional registries"
```
