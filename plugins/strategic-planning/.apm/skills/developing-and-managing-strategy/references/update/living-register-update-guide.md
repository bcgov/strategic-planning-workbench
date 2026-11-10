# Living Register Capture, Import & Update Guide

## 1. The 11 Canonical Living Registers (`strategy/`)

Strategic planning is not a one-time document dump; it is a living knowledge base that evolves as leadership priorities shift, new problems surface, and work progresses. Store and maintain team artifacts in `strategy/`:

| Register File | What It Captures & Records | Stable ID Prefix |
|---|---|---|
| `strategy/01-org-hierarchy-and-context.md` | Multi-tier mandates (Province, Ministry, CSB, Division, Team), business drivers (problems/opportunities), and current-state summary | `MAN-`, `DRV-` |
| `strategy/02-stakeholders-and-concerns.md` | Stakeholders ("the players"), influence/impact, core concerns, desired outcomes, and tensions | `STK-` |
| `strategy/03-target-vision-and-objectives.md` | Target future state, operating principles, and outcome-oriented strategic objectives | `PRN-`, `OBJ-` |
| `strategy/04-expected-benefits-and-value.md` | Public, service, operational, workforce, risk-reduction, and financial value | `BEN-` |
| `strategy/05-business-capabilities.md` | Required business capabilities and 5-pillar maturity gaps | `CAP-` |
| `strategy/06-constraints-assumptions-risks.md` | Constraints, assumptions and evidence gaps (Context and Update modes); risks (Risks mode) | `CON-`, `ASM-`, `GAP-`, `RSK-` |
| `strategy/07-idea-inventory.md` | Unapproved ideas, opportunities, and proposals across maturity states | `IDEA-` |
| `strategy/08-work-inventory.md` | Committed initiatives, active experiments, operational duties, and progress updates | `WORK-` |
| `strategy/09-alignment-traceability-matrix.md` | End-to-end linkage, the 8 alignment diagnostic checks, and the transformation readiness assessment (`BTRA`) | `ALN-` |
| `strategy/10-roadmap-and-success-measures.md` | Roadmap, plateaus and decision gates (Roadmap mode); outcome, leading and guardrail measures (Measures mode) | `PLT-`, `GATE-`, `MSR-` |
| `strategy/11-team-skills-and-allocation.md` | Team member skills, proficiency, growth interests, and active `WORK-X` assignments | `MEM-`, `ASG-` |

## 2. Rules for Importing Evolving Information

When the user provides new meeting notes, emails, leadership updates, or progress reports:
1. **Extract & Triage**: Identify every distinct update:
   - *New/Evolving Leadership Direction or Business Driver* $\rightarrow$ Update `01-org-hierarchy-and-context.md`
   - *New Stakeholder or Shifting Concern* $\rightarrow$ Update `02-stakeholders-and-concerns.md`
   - *Refined Target Vision or Strategic Objective* $\rightarrow$ Update `03-target-vision-and-objectives.md`
   - *New Benefit or Value Claim* $\rightarrow$ Update `04-expected-benefits-and-value.md`
   - *New Value Stream or Capability Gap* $\rightarrow$ Update `05-business-capabilities.md`
   - *New Constraint, or Validated/Invalidated Assumption* $\rightarrow$ Update the matching section of `06` and raise a follow-up for every dependent `RSK-X` and `WORK-X`
   - *Emerging Risk* $\rightarrow$ Hand to Risks mode; Update mode does not write `RSK-X`
   - *New Problem, Idea, Opportunity, Solution Proposal or Experiment Proposal* $\rightarrow$ Hand to `triaging-new-items` if it is mixed or unclear; otherwise to Ideas mode, which writes `07` at the first state for the idea type (`observed` for a Problem, `raw` for the others) (`Problem`, `Opportunity`, `Solution`, `Experiment`)
   - *Progress / Blocker / Milestone Update on Committed Work (initiative, project, or work package)* $\rightarrow$ Hand to Work mode; Update mode does not write `08`
   - *Mixed or unsorted list of new items, or an item whose status is unclear (idea vs. committed work)* $\rightarrow$ Hand to `triaging-new-items`. Do not decide commitment state here.
   - *A named record with an explicit verb ("update WORK-12", "promote IDEA-9")* $\rightarrow$ Hand straight to the matching mode (Ideas, Work, Risks or Score); no triage needed.
   - *Team Skill, Growth Interest, or Assignment Update* $\rightarrow$ Hand to `managing-team-skills-and-allocation`
   - *Note: registers vs. record types.* Registers are the files `01`–`11`. Problems and solution proposals are idea types inside `07`; projects and work packages are work types inside `08`; risks (`RSK-X`) live in their own section of `06`. Do not create a separate register for a record type.
2. **Ripple-Impact Check**: Always report how the update affects connected items (e.g., *"Invalidating assumption ASM-003 puts Initiative WORK-002 at risk and blocks Decision Gate GATE-001"*).
3. **Compound changes**: A change often touches records other modes or skills own (an objective change can affect work, risks, allocations and the roadmap). List every affected record by ID with its owner (mode or skill), write one `Open follow-ups` row per record in `00`, and show them in the recap. Do not edit another mode's section. A follow-up stays `Open` until the owning mode or skill applies it and logs it. See the bookkeeping contract.

## 3. TOGAF Phase H Change Classification & Time-Boxed Dispensations (`DSP-X`)

1. **Classify each incoming strategic change (TOGAF Phase H)**:
   - `Simplification`: Minor wording, status, or progress update within existing scope.
   - `Incremental`: Adds or adjusts a capability, idea, or work item without altering strategic objectives.
   - `Re-direction`: Shifts target objectives, mandates, or horizon commitments; requires leadership confirmation.
2. **Time-boxed strategic dispensations (`DSP-X`)**:
   - When an urgent ministerial, judicial, or operational demand forces a temporary workaround that deviates from operating principles (`PRN-X`) or target capabilities (`CAP-X`), log a **Time-Boxed Dispensation (`DSP-X`)** with an explicit **Expiry / review date** and **Remediation path** so tactical exceptions never silently become permanent technical or operational debt.
