# Classification and routing guide

Record types, states and the work taxonomy are defined in `developing-and-managing-strategy`. This guide only decides where a new item goes.

## Contents

- [Gate 1: commitment state](#1-gate-1-commitment-state)
- [Gate 2: nature](#2-gate-2-nature)
- [Funding flag](#3-funding-flag)
- [Routing table](#4-routing-table)
- [Tie-breakers](#5-tie-breakers)

## 1. Gate 1: commitment state

Ask: *"Has someone with authority approved this, is someone named to deliver it, and is anyone working on it today?"*

| State | Meaning | Evidence needed |
|---|---|---|
| `Heard` | Mentioned in a meeting, email or note. | None. |
| `Considering` | Being discussed or explored, not approved. | None. |
| `Approved` | Sponsor, owner and capacity confirmed, not yet started. | Sponsor with approval date, owner, capacity. |
| `Running` | Work is under way today. | Approved: as above. Not approved: flag `Shadow Operation`. |
| `Ongoing` | Recurring duty or supported service. | Service or duty owner. |

Gate 1 applies to Opportunity, Solution, Experiment, Delivery, Operational, Research and Training. The other natures (Problem, Driver, Risk, Strategy change, Assumption or constraint, Exception, Decision, Blocker, Team change, Action item and Status update) are not commitments, so skip Gate 1 and ask what they affect instead. A Problem is recorded at `observed`.

## 2. Gate 2: nature

Match on meaning, not on the user's exact words. The middle column shows words people often use.

| Nature | People say | Test question |
|---|---|---|
| `Problem` | "it keeps failing", "clerks complain" | Is this a friction, failure or gap with no solution chosen yet? |
| `Opportunity` | "we could", "what if" | Is this a possible benefit with no solution chosen yet? |
| `Solution` | "build a tool", "buy a system" | Is this a specific thing to build, buy or change? |
| `Experiment` | "pilot", "proof of concept", "try" | Is this a time-boxed test of an assumption? |
| `Delivery` (project, initiative, work package) | "project", "phase 2", "work package" | Is this a bounded effort with deliverables? |
| `Operational` | "monthly report", "keep it running" | Is this a recurring obligation or supported service? |
| `Research` | "options paper", "look into" | Is this an investigation with a decision date? |
| `Training` | "course", "certification", "upskill" | Is this learning or development for a person or team? |
| `Risk` | "might fail", "if X happens" | Might this happen, and would it hurt an objective or a work item? |
| `Driver` | "the law changed", "budget cut", "new court rule", "incident" | Is this an outside or inside pressure that makes change necessary or urgent? |
| `Strategy change` | "new mandate", "priorities changed" | Is this new leadership direction, a stakeholder shift or a changed objective? |
| `Assumption or constraint` | "we assume", "policy requires" | Is this a belief to test, or a fixed limit? |
| `Exception` | "temporary workaround", "waiver" | Is this a time-boxed deviation from a principle or capability? |
| `Decision` | "leadership must choose" | Is a choice needed between named options? |
| `Blocker` | "stuck waiting on" | Is something holding up a named work item right now? |
| `Team change` | "new hire", "leaving", "availability" | Does this change people, skills or availability? |
| `Action item` | "follow up with", "send" | Is this a small task with no deliverable? (Not a record.) |
| `Status update` | "WORK-12 is done" | Does this change an existing record? (Not new: skip triage.) |

If an item mixes natures (for example, "build an AI tool for X"), split it into a `Problem` row and a linked `Solution` row. A risk or blocker noticed inside a project becomes its own row.

## 3. Funding flag

Investment, budget and request-for-funding asks are a **flag**, not a nature. Set `Funding request` on a Solution, Experiment, Delivery or Training item. A funding ask never skips validation: if the idea is a validated `candidate`, route to Score; otherwise route to Ideas first and say what is needed before it can be scored.

## 4. Routing table

| Commitment state | Nature | Destination | Record |
|---|---|---|---|
| `Heard` / `Considering` | Problem | `developing-and-managing-strategy` (Ideas) | `IDEA-X`, type `Problem`, state `observed` |
| `Heard` / `Considering` | Opportunity | `developing-and-managing-strategy` (Ideas) | `IDEA-X`, type `Opportunity`, state `raw` |
| `Heard` / `Considering` | Solution, Experiment | `developing-and-managing-strategy` (Ideas) | `IDEA-X`, type `Solution` or `Experiment`, state `raw` |
| `Heard` / `Considering` | Research | `developing-and-managing-strategy` (Ideas) | `IDEA-X`, next step `Research` |
| Any, with `Funding request` and a validated `candidate` | Solution, Experiment, Delivery, Training | `developing-and-managing-strategy` (Score) | Score before the promotion gate |
| `Approved` with sponsor, owner and confirmed capacity | Delivery, Experiment, Research | `developing-and-managing-strategy` (Work) | `WORK-X`, status `Planned` |
| `Approved` without confirmed capacity | Delivery, Experiment, Research | `developing-and-managing-strategy` (Ideas or Roadmap) | Decision gate flagged `Capacity unconfirmed`; not committed work |
| `Running` (approved) | Delivery, Experiment, Research | `developing-and-managing-strategy` (Work) | `WORK-X`, status `Active` |
| `Running` (not approved) | Any | `developing-and-managing-strategy` (Work) | `WORK-X` flagged `Shadow Operation`, plus a governance decision |
| `Ongoing` | Operational | `developing-and-managing-strategy` (Work) | `WORK-X`, type `Operational` or `Product-Service` |
| `Heard` / `Considering` / `Approved` | Training | `managing-team-skills-and-allocation` | Growth interest or learning assignment for a member (`MEM-X`); if it needs funding or has deliverables, also an idea |
| Not applicable | Risk | `developing-and-managing-strategy` (Risks) | `RSK-X`, linked to `WORK-X` or `OBJ-X` |
| Not applicable | Driver | `developing-and-managing-strategy` (Update) | `DRV-X` in register `01`, with its source and date; if it exposes an unsolved need, also log a Problem or Opportunity; later, evidence for the Drivers score in Score mode |
| Not applicable | Strategy change | `developing-and-managing-strategy` (Update) | Registers `01`-`06` (strategy sections) with a changelog entry; any effect on `09` or `10` becomes a follow-up for Alignment, Measures or Roadmap mode |
| Not applicable | Assumption or constraint | `developing-and-managing-strategy` (Update) | `ASM-X` or `CON-X` in register `06`; dependent risks and work become follow-ups |
| Not applicable | Exception | `developing-and-managing-strategy` (Update) | `DSP-X` with expiry date and remediation trigger |
| Not applicable | Decision | `developing-and-managing-strategy` (Roadmap) | Decision gate (`GATE-X`); if it is about one idea, Ideas mode disposition |
| Not applicable | Blocker | `developing-and-managing-strategy` (Work) | Status `Blocked` on the named work item; if no item is named, ask which |
| Not applicable | Team change | `managing-team-skills-and-allocation` | Roster, skills or availability in register `11` |
| Not applicable | Action item | None (not a record) | Note it on the parent work item or leave it in the notes; ask the owner if it needs a deliverable |
| Not applicable | Status update | Skip triage | Owner mode of `developing-and-managing-strategy` |

## 5. Tie-breakers

0. Triage is for new, mixed or unclear material. If the user names an existing record and an explicit action ("update WORK-12", "promote IDEA-9", "re-score RSK-3"), skip triage and hand it straight to the owner.
1. Approval is claimed but not confirmed: treat as `Considering` and ask for the sponsor's name and date.
2. Approved but no confirmed capacity: it is a decision gate, never committed work.
3. Unsure of nature: route as an idea of type `Opportunity` and ask in the next session.
4. Work package whose parent project is not in the work inventory: ask whether to onboard the parent first.
5. Already happening, not a possibility: a `Problem` or a `Blocker`, not a `Risk`.
5a. A `Driver` is the pressure or cause (a statute, mandate letter, court rule, funding change, incident); a `Strategy change` is what leadership now wants as a result. Log the driver as `DRV-X` and the resulting direction separately.
6. A course that a team member wants for their own growth is `Training`; a training program the branch is funding and delivering is a `Delivery` item with a `Funding request` flag.
7. Never promote on triage. Promotion belongs to the idea funnel and the commitment check in `developing-and-managing-strategy`.
8. No strategy folder yet: hand off to `developing-and-managing-strategy` first so the folder is created, then route the items.
