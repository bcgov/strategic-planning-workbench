# Acceptance Criteria: `prioritizing-and-scoring-investments`

The following verifiable gates must be satisfied when evaluating and scoring investments:

1. **Interactive Pacing & Choice**:
   - The agent MUST present candidate items one at a time and ask at most 1–2 evaluation criteria per interaction turn.
   - The agent MUST offer clear rubric anchors (0–10 scale) to assist users in scoring.

2. **Mathematical Integrity & Weight Normalization**:
   - The agent MUST normalize category weights within each axis so they sum to 100%.
   - Overall composite scores MUST correctly apply the specified Value vs. Delivery axis weighting (default 50/50).

3. **Three-Inventory Separation**:
   - Candidate proposals MUST NOT be treated as committed work until approved and promoted through an executive decision gate.
   - Deferred or rejected proposals MUST preserve their evaluation scores and rationale.

4. **Dual-Format Persistence**:
   - Evaluated portfolios MUST be exportable to both machine-readable JSON (`investment-scoring-ledger.json`) and spreadsheet-friendly CSV (`investment-scoring-ledger.csv`).

5. **B.C. Government Style & Design System**:
   - Headings, tables, and labels MUST strictly follow B.C. Government sentence case.
   - Outputs MUST be plain language with zero emoji and zero exclamation marks.
   - The generated 4-quadrant visual MUST employ B.C. Government Design System v5 tokens (navy headers `#1E3A8A`, calm gradient quadrant background, legible bubble markers).
