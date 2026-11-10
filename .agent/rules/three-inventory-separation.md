---
description: Enforces strict separation between Strategic Vision, Idea Inventory, and Committed Work Inventory, and governs non-destructive register updates.
globs: ["**/*"]
---

# Rule: Three-Inventory Separation & Living Register Integrity

## 1. The Iron Law
> **Strategic Vision, the Idea Inventory, and the Committed Work Inventory MUST remain strictly separate.** An idea, suggestion, or experiment MUST NEVER be represented as committed work without verified sponsorship, ownership, and capacity commitment.

## 2. Invariants & Forbidden Actions

1. **Three Distinct Layers**:
   - **Strategic Vision & Capabilities**: Defines *where we are going, why it matters, and what capabilities the organization must possess*.
   - **Idea Inventory (`IDEA-NNN`)**: Captures *what we might do* across maturity states (`raw`, `explored`, `validated`, `candidate`, `deferred`, `rejected`, `promoted`); Problems use `observed`, `validated`, `sized`, `addressed`, `resolved`. Risks (`RSK-X`) are neither ideas nor work and live in register `06`.
   - **Committed Work Inventory (`WORK-NNN`)**: Tracks *what we are actually doing or committed to doing* (approved initiatives, active time-boxed experiments, and ongoing operational responsibilities).
2. **Promotion Gate Enforcement**: Agents MUST NOT move an item from the Idea Inventory into the Work Inventory or committed roadmap horizons unless source evidence confirms:
   - Alignment to a Strategic Objective (`OBJ-X`) and Business Capability (`CAP-X`),
   - Confirmed Executive/Branch Sponsor and Delivery Owner, and
   - Approved capacity commitment, recorded as an allocation in register `11` or confirmed by the owner with the source stated.
   - Approval alone is not enough. Approval without confirmed capacity keeps the item a decision gate flagged `Capacity unconfirmed`; it MUST NOT appear as committed work or as a committed roadmap bar.
3. **Non-Destructive Incremental Updates**: When importing evolving priorities, new drivers, stakeholder updates, or work progress, agents MUST preserve stable IDs (`OBJ-X`, `CAP-X`, `IDEA-X`, `WORK-X`, `ASM-X`, `RSK-X`) and append a change-log entry rather than silently deleting prior records.
4. **Preserve Deferred & Rejected Ideas**: Rejected or deferred ideas MUST remain in the Idea Inventory with their decision rationale to preserve institutional memory.
5. **Roadmap Commitment Honesty**: Visual roadmaps and Gantt/horizon diagrams MUST clearly distinguish committed `WORK-X` initiatives from unapproved `IDEA-X` decision gates.

## 3. Evaluation Checklist

- Are all unapproved proposals, brainstorms, and workshop suggestions isolated in the Idea Inventory?
- Does every `WORK-NNN` item have a verified Sponsor, Owner, Status, and work type?
- When registers are updated with new information, are existing IDs and decision histories preserved?
- Do visual roadmaps and presentations visually separate committed work from candidate decision gates?
