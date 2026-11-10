# Project and work package intake

Used by Work mode and by the `triaging-new-items` to classify delivery work and check the commitment boundary.

## 1. Commitment check

Before any item is routed as `Approved` or `Running`, confirm:
1. **Sponsor**: a named person with authority who approved it.
2. **Owner**: a named delivery owner.
3. **Capacity**: time allocated, not assumed.

If any is missing: route to the idea inventory, or flag `Shadow Operation` if work is already under way.

## 2. Work taxonomy

| Work type | Definition | Extra requirement |
|---|---|---|
| `Initiative` | Group of related projects serving one objective. | Objective (`OBJ-X`), target window. |
| `Project` | Bounded delivery effort creating or strengthening a capability. | Sponsor, owner, outcomes, target window. |
| `Work package` | Defined slice of a project with one deliverable. | Parent project, deliverable, due date. |
| `Product-Service` | Continuously supported tool, asset or service. | Service owner, lifecycle review. |
| `Experiment` | Approved time-boxed test. | Exit criteria: promote, pivot or retire. |
| `Operational` | Recurring duty ("keep the lights on"). | Baseline capacity recorded. |
| `Research` | Assigned investigation or options paper. | Deliverable and decision date. |

## 3. Hierarchy

`Initiative` $\rightarrow$ `Project` $\rightarrow$ `Work package`. Record the parent in the `Parent Work ID` column of the work inventory. Work packages use child IDs such as `WORK-012.1` and inherit the parent's `OBJ-X` and `CAP-X` unless stated.

## 4. Signals to flag at intake

- **Orphaned**: no link to an `OBJ-X` or `CAP-X`.
- **Shadow Operation**: in daily use or under way without sponsor, security review or funding.
- **Over-committed owner**: one person named on many concurrent items.
- **Work package without parent**: onboard or name the parent first.
