# Work Inventory & Commitment Governance Guide

## 1. The Commitment Boundary

The most common failure in team strategic planning is collapsing:
1. A person mentioning an idea in a meeting,
2. The team considering or exploring the idea,
3. A developer running an informal proof-of-concept, and
4. Leadership approving and resourcing an initiative

into a single undifferentiated list of *"things we are doing."*

The **Work Inventory** strictly records items that the branch or team is **actively doing or formally committed to doing**.

## 2. Work Taxonomy

| Work Type | Definition | Governance Requirement |
|---|---|---|
| **Initiative** | Group of related projects serving one strategic objective. | Requires Sponsor, Owner, a linked `OBJ-X`, and target completion window. |
| **Project** | Bounded delivery effort creating or strengthening a business capability. | Requires Sponsor, Owner, target outcomes, and target completion window. |
| **Work Package** | Defined slice of a project with one deliverable (`WORK-012.1`). | Requires a `Parent Work ID`, a deliverable, and a due date. See the hierarchy in [project-and-work-package-types.md](project-and-work-package-types.md). |
| **Product / Ongoing Service** | Continuously supported digital tool, knowledge asset, or branch service. | Requires Service Owner, operational capacity allocation, and lifecycle review. |
| **Active Experiment / Pilot** | Time-boxed, approved proof of concept testing specific assumptions. | Requires explicit exit criteria (promote, pivot, or retire) so it does not quietly become unsupported production software. |
| **Operational Responsibility** | Recurring statutory, reporting, or support obligation ("keep the lights on"). | Tracked to make baseline capacity visible before layering on new strategic initiatives. |
| **Assigned Research / Discovery** | Formally assigned investigation or options analysis requested by leadership. | Requires concrete deliverable (brief/options paper) and decision date. |

## 3. Portfolio Hygiene Signals to Surface

- **Orphaned Work**: Active projects or services that do not trace to any Strategic Objective (`OBJ-X`) or Capability (`CAP-X`).
- **Shadow Operations**: Experiments or prototypes that users now rely on daily without formal sponsorship, security review, or support funding.
- **Over-Committed Owners**: Single individuals listed as the primary owner across too many concurrent initiatives.

## 4. Commitment evidence

A work item is committed (`Planned` or `Active`) only with all three: a named **sponsor** with approval date, a named **owner**, and **capacity** (an allocation in register `11`, or confirmed by the owner with the source stated). Approval alone is not enough. If capacity is missing, keep the item as an `IDEA-X` decision gate or, if it already exists, flag it `Capacity unconfirmed`, and list the missing evidence as the next action. The same rule applies on the roadmap. See the shared bookkeeping contract.
