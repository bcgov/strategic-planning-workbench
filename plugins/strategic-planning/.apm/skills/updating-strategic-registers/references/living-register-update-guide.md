# Living Register Capture, Import & Update Guide

## 1. The 10 Canonical Living Registers (`strategy/`)

Strategic planning is not a one-time document dump; it is a living knowledge base that evolves as leadership priorities shift, new problems surface, and work progresses. Store and maintain team artifacts in `strategy/`:

| Register File | What It Captures & Records | Stable ID Prefix |
|---|---|---|
| `strategy/01-org-hierarchy-and-context.md` | Multi-tier mandates (Province, Ministry, CSB, Division, Team), business drivers (problems/opportunities), and current-state summary | `MAN-`, `DRV-` |
| `strategy/02-stakeholders-and-concerns.md` | Stakeholders ("the players"), influence/impact, core concerns, desired outcomes, and tensions | `STK-` |
| `strategy/03-target-vision-and-objectives.md` | Target future state, operating principles, and outcome-oriented strategic objectives | `PRN-`, `OBJ-` |
| `strategy/04-expected-benefits-and-value.md` | Public, service, operational, workforce, risk-reduction, and financial value | `BEN-` |
| `strategy/05-business-capabilities.md` | Required business capabilities and 5-pillar maturity gaps | `CAP-` |
| `strategy/06-constraints-assumptions-risks.md` | Fixed constraints, unvalidated assumptions, evidence gaps, and strategic risks | `CON-`, `ASM-`, `GAP-`, `RSK-` |
| `strategy/07-idea-inventory.md` | Unapproved ideas, opportunities, and proposals across maturity states | `IDEA-` |
| `strategy/08-work-inventory.md` | Committed initiatives, active experiments, operational duties, and progress updates | `WORK-` |
| `strategy/09-alignment-traceability-matrix.md` | End-to-end linkage and the 8 alignment diagnostic checks | `ALN-` |
| `strategy/10-roadmap-and-success-measures.md` | High-level sequencing (`Now / Next / Later`), decision gates, and outcome/leading/guardrail measures | `GATE-`, `MSR-` |

## 2. Rules for Importing Evolving Information

When the user provides new meeting notes, emails, leadership updates, or progress reports:
1. **Extract & Triage**: Identify every distinct update:
   - *New/Evolving Leadership Direction or Business Driver* $\rightarrow$ Update `01-org-hierarchy-and-context.md`
   - *New Stakeholder or Shifting Concern* $\rightarrow$ Update `02-stakeholders-and-concerns.md`
   - *Refined Target Vision or Strategic Objective* $\rightarrow$ Update `03-target-vision-and-objectives.md`
   - *New Benefit or Value Claim* $\rightarrow$ Update `04-expected-benefits-and-value.md`
   - *New Capability Gap* $\rightarrow$ Update `05-business-capabilities.md`
   - *New Constraint, Validated/Invalidated Assumption, or Emerging Risk* $\rightarrow$ Update `06-constraints-assumptions-risks.md`
   - *New Idea or Opportunity* $\rightarrow$ Append to `07-idea-inventory.md` as `raw` or `explored`
   - *Progress / Blocker / Milestone Update on Committed Work* $\rightarrow$ Update status and progress notes in `08-work-inventory.md`
2. **Ripple-Impact Check**: Always report how the update affects connected items (e.g., *"Invalidating assumption ASM-003 puts Initiative WORK-002 at risk and blocks Decision Gate GATE-001"*).
