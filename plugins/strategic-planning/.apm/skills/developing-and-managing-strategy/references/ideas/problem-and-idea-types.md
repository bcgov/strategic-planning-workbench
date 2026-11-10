# Problem and idea intake

Used by Ideas mode and by the `triaging-new-items` to split problems from solutions before an idea record exists.

## 1. Idea types

| Idea type | What it is | First validation question |
|---|---|---|
| `Problem` | A friction or gap with no solution chosen. | Who experiences it, how often, and what evidence shows it? |
| `Opportunity` | A possible benefit with no solution chosen. | What would change for the public or staff if we did nothing? |
| `Solution` | A specific proposal to build, buy or change. | What problem does it solve, and what are two other ways to solve it? |
| `Experiment` | A time-boxed test of an assumption. | What single assumption is tested, and what result would stop it? |

## 2. Problem versus solution separation

When someone says *"Let's build an AI tool for X"*, ask:
1. *What friction or failure are staff or service users experiencing today?*
2. *What are three non-technology and technology ways to address it?*

Log the problem as one row and the proposed tool as a linked `Solution` row.

## 3. Maturity states carried to the idea skill

`raw` $\rightarrow$ `explored` $\rightarrow$ `validated` $\rightarrow$ `candidate` / `deferred` / `rejected` $\rightarrow$ `promoted`. Triage only ever creates items at their first state: `observed` for a Problem and `raw` for the other types. A Problem then follows `observed` → `validated` → `sized` → `addressed` → `resolved` (or `accepted`), described in the lifecycle reference. Early items may be incomplete.

## 4. Minimum fields at intake

Title, source and date, idea type, one-line description, and linked problem (for a `Solution`). Strategic links (`OBJ-X`, `CAP-X`) are optional at intake.
