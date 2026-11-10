# Item workflows

Steps, templates and gates for the item layer: Ideas, Work, Risks, Score, Roadmap and Review.

## Contents

- [Ideas](#ideas)
- [Work](#work)
- [Risks](#risks)
- [Score](#score)
- [Roadmap](#roadmap)
- [Review](#review)

## Ideas

Offer the 4-option menu (quick-capture, clarify and align, stress-test, compare). Capture the idea with its type (`Problem`, `Opportunity`, `Solution`, `Experiment`) at its first state: `observed` for a Problem, `raw` for the others, separate problem from solution, link `OBJ-X` and `CAP-X`, run the riskiest assumption test, and record a disposition (`Promote`, `Explore`, `Defer`, `Combine`, `Reject`). Allow incomplete early ideas.
Templates: [idea-inventory](../../assets/templates/idea-inventory.md), [idea-record](../../assets/templates/idea-record.md), [idea-evaluation](../../assets/templates/idea-evaluation.md). Guides: [funnel](../ideas/idea-funnel-and-evaluation-guide.md), [idea and problem types](../ideas/problem-and-idea-types.md). Gate: [acceptance criteria](../ideas/acceptance-criteria.md).

## Work

Offer the menu (catalog work, promote an approved idea, update status and blockers, audit orphans and shadow operations). Check commitment evidence (sponsor with approval date, owner, confirmed capacity), tag the work type with `Parent Work ID` for work packages, link `OBJ-X` and `CAP-X`, and flag over-committed owners.
Template: [work-inventory](../../assets/templates/work-inventory.md). Guides: [work portfolio](../work/work-portfolio-guide.md), [work types and hierarchy](../work/project-and-work-package-types.md). Gate: [acceptance criteria](../work/acceptance-criteria.md).

## Risks

Draft event, cause and impact; confirm taxonomy lens, owner and link to `WORK-X` or `OBJ-X`; rate likelihood, severity and proximity; choose a response (`mitigate`, `transfer`, `avoid`, `accept`). Writes only the risks section of register `06`.
Template: [strategic-risk-register](../../assets/templates/strategic-risk-register.md). Guide: [risk management](../risks/risk-management-guide.md). Gate: [acceptance criteria](../risks/acceptance-criteria.md).

## Score

Score only `candidate` Solution, Opportunity or Experiment ideas, or `Planned` work awaiting a funding decision. Confirm weights (100 points per axis, default 50/50), score 4 value and 5 delivery criteria one proposal at a time, run [generate_investment_quadrant.py](../../scripts/generate_investment_quadrant.py) or [interactive_investment_app.py](../../scripts/interactive_investment_app.py), and confirm the quadrant (Q1 Strategic Priority, Q2 Big Bet, Q3 Tactical, Q4 Defer). Persist scores in JSON and CSV (the CSV is lossless and keeps score history). After changing the scripts, run `python scripts/test_investment_scripts.py`.
Templates: [framework](../../assets/templates/investment-scoring-framework.json), ledgers ([json](../../assets/templates/investment-scoring-ledger.json), [csv](../../assets/templates/investment-scoring-ledger.csv)), [brief](../../assets/templates/investment-scoring-brief.md). Guides: [rubric](../scoring/scoring-rubric-and-weighting-guide.md), [4-quadrant](../scoring/4-quadrant-portfolio-guide.md). Gate: [acceptance criteria](../scoring/acceptance-criteria.md).

## Roadmap

Decision items from `triaging-new-items` become decision gates (`GATE-X`) with the options and an owner. Choose the horizon format (`Now / Next / Later`, Three Horizons, fiscal quarters), place as committed only items with commitment evidence, show everything else as decision gates, and define plateaus and prerequisites. Writes only the roadmap and decision gates section of register `10`.
Template: [strategic-roadmap](../../assets/templates/strategic-roadmap.md). Guide: [roadmap guide](../roadmap/roadmap-guide.md). Gate: [acceptance criteria](../roadmap/acceptance-criteria.md).

## Review

Compare each item to its state, review trigger and allowed next states. Work through open follow-ups in `00`: review the affected record, apply any change in the owning mode, log it, and close the follow-up only after that.
Guide: [lifecycle](../lifecycle/item-lifecycle-and-transitions.md).
