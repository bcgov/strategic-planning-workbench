---
name: prioritizing-and-scoring-investments
description: "Guides users interactively to evaluate, score, and rank proposed investments, projects, and opportunities using a weighted multi-criteria decision framework across Value/ROI and Ability to Deliver, producing 4-quadrant portfolio charts, JSON/CSV ledgers, and executive ranking briefs. Use when scoring candidate investments, evaluating requests for funding (RFF), prioritizing project portfolios, weighting decision criteria, or generating 4-quadrant investment scatter charts. Not for capturing raw ideas (use managing-idea-inventory) or detailed roadmap sequencing (use sequencing-roadmaps-and-measures)."
---

# Prioritizing and scoring investments

Guides executive sponsors and teams interactively to evaluate, weight, and rank candidate projects and funding requests across Value/ROI and Ability to Deliver in a 4-quadrant portfolio landscape.

## Contents

- [Constraints](#constraints)
- [Quick start](#quick-start)
- [Workflow](#workflow)
- [Verification](#verification)
- [References](#references)

## Constraints

1. **Interactive scoring pacing**: Present 1 proposal at a time and ask at most 1–2 criteria per turn using anchored 0–10 rubrics.
2. **Three-inventory separation**: Never treat candidate proposals as committed work until formally approved through an executive gate.
3. **Dual-format persistence**: Keep evaluations synchronized across machine-readable JSON and spreadsheet-compatible CSV.
4. **B.C. Government Design System style**: Use sentence case for all headings and labels, plain language, zero emoji, and zero exclamation marks.
5. **Recap confirmation gate**: Present calculated scores and quadrant placement for user confirmation before writing to registers.

## Quick start

1. Review [scoring-rubric-and-weighting-guide.md](references/scoring-rubric-and-weighting-guide.md) and [4-quadrant-portfolio-guide.md](references/4-quadrant-portfolio-guide.md).
2. Configure category weights in [investment-scoring-framework.json](assets/templates/investment-scoring-framework.json) or accept standard defaults.
3. Intake and score proposals in [investment-scoring-ledger.json](assets/templates/investment-scoring-ledger.json) or [investment-scoring-ledger.csv](assets/templates/investment-scoring-ledger.csv).
4. Generate the 4-quadrant visual and executive report using [generate_investment_quadrant.py](scripts/generate_investment_quadrant.py) and compile [investment-scoring-brief.md](assets/templates/investment-scoring-brief.md).

## Workflow

1. **Weighting Configuration**: Confirm category weights (summing to 100 points per axis) and overall axis split (default 50% Value / 50% Delivery).
2. **Interactive Proposal Scoring**: Walk through candidate proposals across 4 Value criteria (Drivers, Alignment, Outcomes, Sector) and 5 Delivery criteria (Readiness, Research, Cost, Sponsor, Ease) on the 0–10 rubric.
3. **Calculate & Classify**: Run [generate_investment_quadrant.py](scripts/generate_investment_quadrant.py) to compute normalized scores and classify into Quadrants (Q1 Strategic Priority, Q2 Big Bet, Q3 Tactical, Q4 Defer).
4. **Recap Confirmation Gate**: Present the ranking table and visual placement for leadership validation.
5. **Commitment Handoff**: Promote Q1 approved items to `managing-work-inventory` (`WORK-X`) and archive rejected or deferred proposals in `strategy/07-idea-inventory.md`.

## Verification

Check outputs against [acceptance-criteria.md](references/acceptance-criteria.md):
- Category weights sum to 100% and composite scores apply axis weighting accurately.
- Evaluated proposals are preserved in both JSON and CSV with B.C. Government sentence case.

## References

- Framework & rubrics: [scoring-rubric-and-weighting-guide.md](references/scoring-rubric-and-weighting-guide.md) • [4-quadrant-portfolio-guide.md](references/4-quadrant-portfolio-guide.md)
- Templates: [investment-scoring-framework.json](assets/templates/investment-scoring-framework.json) • [investment-scoring-ledger.json](assets/templates/investment-scoring-ledger.json) • [investment-scoring-ledger.csv](assets/templates/investment-scoring-ledger.csv) • [investment-scoring-brief.md](assets/templates/investment-scoring-brief.md)
- Generator script: [generate_investment_quadrant.py](scripts/generate_investment_quadrant.py)
- Quality gate: [acceptance-criteria.md](references/acceptance-criteria.md)
