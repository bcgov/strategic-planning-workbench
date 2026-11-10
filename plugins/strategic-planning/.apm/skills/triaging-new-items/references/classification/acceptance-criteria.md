# Acceptance criteria: `triaging-new-items`

## Mandatory quality gates

1. **Both gates applied where they apply**
   - **Pass**: Every item has a nature, a destination and a reason. Items whose nature is a commitment (opportunity, solution, experiment, delivery, operational, research, training) also have a commitment state; all other natures show `Not applicable`.
   - **Fail**: Items are routed on title alone, or a commitment item has no state.
2. **No commitment by assumption**
   - **Pass**: Items are routed to the work inventory only with a confirmed sponsor, owner and capacity, or flagged `Shadow Operation`.
   - **Fail**: Mentioned or discussed items are logged as work.
3. **Problems split from solutions**
   - **Pass**: Mixed items become a linked `Problem` row and `Solution` row.
   - **Fail**: A solution is logged with no problem statement.
4. **Hierarchy respected**
   - **Pass**: Work packages name a parent; a missing parent is raised.
   - **Fail**: Work packages are logged as stand-alone projects.
5. **Recap gate and no direct register writes**
   - **Pass**: The user confirms the table; only the triage log is saved; records are created by the receiving skill.
   - **Fail**: `IDEA-X` or `WORK-X` rows are written by this skill.

6. **Funding asks and non-record items handled**
   - **Pass**: A funding or investment ask is flagged `Funding request` and routed to Score only when the item is a validated `candidate`, otherwise to Ideas first. Action items are not turned into records. Training and team changes go to `managing-team-skills-and-allocation`.
   - **Fail**: A funding ask skips validation, an action item becomes a project, or a training request is logged as work.
