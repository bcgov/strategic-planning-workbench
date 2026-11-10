# Acceptance criteria: `developing-and-managing-strategy` (Ideas mode)

## Mandatory Quality Gates

1. **Strict Separation from Committed Work**:
   - **Pass**: Ideas are stored in the Idea Inventory with an explicit maturity state (`raw`, `explored`, `validated`, `candidate`, `deferred`, `rejected`, `promoted`) and never listed as active commitments without verified approval.
   - **Fail**: Brainstormed ideas or workshop suggestions are presented as approved roadmap initiatives.
2. **Stage-Appropriate Rigor**:
   - **Pass**: Early (`raw`) ideas are captured cleanly with incomplete fields allowed; formal comparative scoring is applied only to `validated` or `candidate` ideas.
   - **Fail**: Rejects or invents fake RICE scores for raw, unresearched ideas.
3. **Decision History Preservation**:
   - **Pass**: Deferred, combined, and rejected ideas retain their status and decision rationale in the inventory.
   - **Fail**: Rejected or deferred ideas are silently deleted, losing institutional memory.
