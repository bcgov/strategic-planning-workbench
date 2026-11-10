# Acceptance criteria: `developing-and-managing-strategy` (Risks mode)

## Mandatory quality gates

1. **Right record type**
   - **Pass**: Uncertain future events are `RSK-X`; things already happening are problems or blockers; assumptions and constraints are not logged as risks.
   - **Fail**: An occurring issue or an assumption is logged as a risk.
2. **Assessed and linked**
   - **Pass**: Each risk has likelihood, severity, proximity (or `Unvalidated` with an evidence action), a taxonomy lens, an owner, and a link to `WORK-X` or `OBJ-X` (or an explicit `Unlinked` flag).
   - **Fail**: Ratings are invented without evidence, or the risk has no owner.
3. **Response recorded**
   - **Pass**: A response (`mitigate`, `transfer`, `avoid`, `accept`) is chosen with its required fields; `accept` records rationale, approver and a review date.
   - **Fail**: A risk is left unanswered or accepted with no approver.
4. **Lifecycle kept**
   - **Pass**: State, `Next review date` and `Last scored` are filled in; closed and materialized risks keep a note and date; nothing is deleted.
   - **Fail**: Risks are overwritten or removed.
