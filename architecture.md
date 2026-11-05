# Architecture & Strategic Planning Model (`architecture.md`)

## Contents

- [1. Purpose & System Overview](#1-purpose--system-overview)
- [2. Five-Tier Public-Sector Organizational Hierarchy (BC Gov / AG / CSB)](#2-five-tier-public-sector-organizational-hierarchy-bc-gov--ag--csb)
- [3. The Three-Inventory Separation Model](#3-the-three-inventory-separation-model)
- [4. Canonical Living Strategic Registers (`strategy/`)](#4-canonical-living-strategic-registers-strategy)
- [5. End-to-End Skill Lifecycle & Continuous Update Loop](#5-end-to-end-skill-lifecycle--continuous-update-loop)
- [6. Repository & APM-Native Plugin Structure](#6-repository--apm-native-plugin-structure)

---

## 1. Purpose & System Overview

`strategic-planning-workbench` is an APM-native agentic workbench designed for **government and organizational strategic planning**. Rather than jumping prematurely from stakeholder conversations into feature backlogs or project wish lists, the workbench maintains a structured, evidence-backed chain from multi-tier leadership direction down to capabilities, candidate ideas, committed work, and measurable outcomes.

---

## 2. Five-Tier Public-Sector Organizational Hierarchy (BC Gov / AG / CSB)

Teams and units in government do not invent strategy in a vacuum; their strategic vision and objectives align upward through a multi-tier organizational structure while preserving clear scope boundaries at each level:

```mermaid
flowchart TD
    T1["Tier 1: Province<br>of BC<br>Mandate Letters,<br>Digital Plan &<br>DRIPA"]
    T2["Tier 2: Ministry<br>of Attorney<br>General<br>Service Plan &<br>Access to Justice"]
    T3["Tier 3: Court<br>Services Branch<br>(CSB)<br>Court Ops &<br>Modernization"]
    T4["Tier 4: Division<br>& Directorate<br>Executive<br>Direction &<br>Priorities"]
    T5["Tier 5: Team /<br>Unit Scope<br>Vision, Caps,<br>Inventories &<br>Measures"]

    T1 --> T2 --> T3 --> T4 --> T5
```

| Organizational Tier | Primary Artifacts & Signals | How the Team Uses It |
|---|---|---|
| **Tier 1: Province of BC** | Mandate Letters, BC Digital Plan, DRIPA Action Plan, CleanBC, Accessibility & FOIPPA statutes | Foundational policy, legislative, and public-value guardrails. |
| **Tier 2: Ministry of Attorney General (AG)** | Ministry Service Plan, Justice & Public Safety sector goals, Access to Justice commitments | Sector-level outcomes and non-negotiable judicial/operational independence boundaries. |
| **Tier 3: Court Services Branch (CSB)** | Branch strategic plan, court registry modernization, digital court operations, security/sheriff priorities | Branch-wide strategic themes and shared capability priorities. |
| **Tier 4: Division / Directorate** | Executive Director / Director communications (e.g., Chris, Jessica), divisional priorities, funding bounds | Direct upstream leadership direction (`Confirmed` vs. `Interpreted`). |
| **Tier 5: Team / Unit** | Team Strategy on a Page, Strategic Vision Brief, Capability Map, Idea Inventory, Work Inventory, Roadmap | Directly authored, maintained, and executed by the team. |

---

## 3. The Three-Inventory Separation Model

To prevent teams from confusing a casual suggestion or an exploratory prototype with funded, committed work, the workbench enforces three distinct layers:

```mermaid
flowchart LR
    subgraph L1["Layer 1: Vision & Capabilities"]
        A["Multi-Tier<br>Context, Drivers<br>& Stakeholders"] --> B["Target Vision<br>& Outcome<br>Objectives"]
        B --> C["Required<br>Business<br>Capabilities"]
    end

    subgraph L2["Layer 2: Idea Inventory"]
        D["Capture<br>(raw)"] --> E["Clarify & Align<br>(explored)"]
        E --> F["Validate<br>Assumptions<br>(validated)"]
        F --> G["Compare &<br>Decide<br>(candidate)"]
    end

    subgraph L3["Layer 3: Work Inventory"]
        H["Approved<br>Initiatives &<br>Projects"]
        I["Time-Boxed<br>Active<br>Experiments"]
        J["Ongoing<br>Operational<br>Work"]
    end

    C --> D
    G -->|"Promotion Gate<br>(Sponsor +<br>Owner +<br>Capacity)"| H
    H --> K["Strategic<br>Roadmap, Visuals<br>& Measures"]
```

---

## 4. Canonical Living Strategic Registers (`strategy/`)

When a team uses `strategic-planning-workbench` on an active planning engagement, its living knowledge is captured, saved, and incrementally updated across 10 structured markdown registers (typically stored in `strategy/`):

| Register File | Core Question Answered | Primary Owning Skills |
|---|---|---|
| `strategy/01-org-hierarchy-and-context.md` | *What have Provincial, Ministry (AG), Branch (CSB), and Division leaders communicated, and what are our business drivers and current-state realities?* | `analyzing-strategic-context`, `updating-strategic-registers` |
| `strategy/02-stakeholders-and-concerns.md` | *Who are "the players" (internal, external, judicial, partners), what are their interests/concerns, and where do perspectives conflict?* | `analyzing-strategic-context`, `updating-strategic-registers` |
| `strategy/03-target-vision-and-objectives.md` | *What is our target future state, operating principles, and outcome-oriented strategic objectives (`OBJ-X`)?* | `defining-strategic-vision`, `updating-strategic-registers` |
| `strategy/04-expected-benefits-and-value.md` | *What public, service, operational, workforce, risk-reduction, and financial value (`BEN-X`) will those objectives deliver?* | `defining-strategic-vision`, `updating-strategic-registers` |
| `strategy/05-business-capabilities.md` | *What must our team/branch be able to do (`CAP-X`), and where are the maturity gaps across people, process, data, tech, and governance?* | `planning-business-capabilities`, `updating-strategic-registers` |
| `strategy/06-constraints-assumptions-risks.md` | *What fixed constraints bind us, what unproven assumptions (`ASM-X`) and evidence gaps (`GAP-X`) need validation, and what strategic risks (`RSK-X`) exist?* | `analyzing-strategic-context`, `aligning-strategy-and-portfolio`, `updating-strategic-registers` |
| `strategy/07-idea-inventory.md` | *What possibilities, opportunities, and proposals (`IDEA-X`) are we exploring, deferring, or evaluating?* | `managing-idea-inventory`, `updating-strategic-registers` |
| `strategy/08-work-inventory.md` | *What approved initiatives, active experiments, and operational duties (`WORK-X`) are we committed to doing, and what is their current progress?* | `managing-work-inventory`, `updating-strategic-registers` |
| `strategy/09-alignment-traceability-matrix.md` | *How does everything connect from Province/Ministry/CSB down to team work, and where are the orphans, duplicates, or gaps?* | `aligning-strategy-and-portfolio` |
| `strategy/10-roadmap-and-success-measures.md` | *How is committed work sequenced (`Now / Next / Later`), what are the decision gates, and how is success measured (`MSR-X`: Outcome, Leading, Guardrail)?* | `sequencing-roadmaps-and-measures`, `rendering-strategic-visuals-and-decks` |
| `strategy/11-team-skills-and-allocation.md` | *Who is on our team (`MEM-X`), what are their skills and growth interests, which `WORK-X` items are assigned to them, and where are our key-person bottlenecks?* | `managing-team-skills-and-allocation`, `updating-strategic-registers` |

---

## 5. End-to-End Skill Lifecycle & Continuous Update Loop

1. **Initial Baseline (`analyzing-strategic-context` $\rightarrow$ `defining-strategic-vision` $\rightarrow$ `planning-business-capabilities`)**:
   Establishes multi-tier context, stakeholder map, current state, target vision, outcome objectives, benefits, and required capabilities.
2. **Inventory Capture & Triage (`managing-idea-inventory` & `managing-work-inventory`)**:
   Separates possibilities (`IDEA-X`) from committed work (`WORK-X`) and enforces the Promotion Gate.
3. **Alignment & Sequencing (`aligning-strategy-and-portfolio` & `sequencing-roadmaps-and-measures`)**:
   Audits the full traceability chain, logs strategic risks, sequences horizons, and defines balanced measures.
4. **Living Ingestion & Evolution (`updating-strategic-registers`)**:
   Imports new meeting notes, evolving leadership priorities, new business drivers, emerging problems, new ideas, and status/progress updates on existing work while preserving stable IDs and change logs.
5. **Visual & Executive Rendering (`rendering-strategic-visuals-and-decks`)**:
   Generates Mermaid roadmaps, Gantt/horizon charts, capability heatmaps, alignment flowcharts, Strategy on a Page summaries, and executive presentation decks directly from the living registers.

---

## 6. Repository & APM-Native Plugin Structure

```text
strategic-planning-workbench/
├── .agent/
│   └── rules/
│       ├── apm-plugin-hygiene.md
│       ├── evidence-and-hierarchy-alignment.md
│       └── three-inventory-separation.md
├── .claude-plugin/
│   └── marketplace.json
├── .gitignore
├── AGENTS.md
├── CLAUDE.md
├── README.md
├── apm.yml
├── architecture.md
├── docs/
│   └── governance.md
└── plugins/
    └── strategic-planning/
        ├── .apm/
        │   └── skills/
        │       ├── aligning-strategy-and-portfolio/
        │       ├── analyzing-strategic-context/
        │       ├── defining-strategic-vision/
        │       ├── managing-idea-inventory/
        │       ├── managing-work-inventory/
        │       ├── planning-business-capabilities/
        │       ├── rendering-strategic-visuals-and-decks/
        │       ├── sequencing-roadmaps-and-measures/
        │       └── updating-strategic-registers/
        ├── .claude-plugin/
        │   └── plugin.json
        ├── README.md
        ├── apm.yml
        └── rules/
            ├── apm-plugin-hygiene.md
            ├── evidence-and-hierarchy-alignment.md
            └── three-inventory-separation.md
```
