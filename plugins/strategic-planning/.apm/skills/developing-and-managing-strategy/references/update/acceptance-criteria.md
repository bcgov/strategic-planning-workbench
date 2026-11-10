# Acceptance criteria: `developing-and-managing-strategy` (Update mode)

## Mandatory Quality Gates

1. **ID & History Preservation**:
   - **Pass**: Existing IDs (`OBJ-X`, `CAP-X`, `IDEA-X`, `WORK-X`, `ASM-X`, `RSK-X`) are preserved; status changes and edits are logged in the Register Update Changelog.
   - **Fail**: Renumbers existing records or silently deletes superseded objectives, ideas, or work items.
2. **Multi-Tier Mandate Classification**:
   - **Pass**: Upstream goals and mandates are accurately classified across Tier 1 (Province of BC), Tier 2 (Ministry of Attorney General), Tier 3 (Court Services Branch), Tier 4 (Division), and Tier 5 (Team).
   - **Fail**: Flattens provincial, ministry, branch, and team goals into a single undifferentiated list.
3. **Ripple-Impact Analysis**:
   - **Pass**: Explicitly identifies downstream impacts when a priority, driver, constraint, or assumption changes.
   - **Fail**: Updates one register in isolation without flagging broken links or affected work items.
