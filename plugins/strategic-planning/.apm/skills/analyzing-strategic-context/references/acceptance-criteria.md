# Acceptance criteria: `analyzing-strategic-context`

## Mandatory quality gates

1. **Interactive HITL experience**:
   - **Pass**: Uses numbered option menus (with a recommended default) and progressive 1–2 question turns; presents a recap confirmation gate before writing register files.
   - **Fail**: Dumps a wall of 8+ simultaneous questions or writes files without confirming understanding when inputs are ambiguous.
2. **Fact vs. assumption separation**:
   - **Pass**: Every leadership statement and current-state claim is explicitly tagged as `Confirmed`, `Interpreted`, or `Assumption`, with source citations or evidence gaps noted.
   - **Fail**: Inferred goals or unverified complaints are presented as established facts.
3. **B.C. Government Design System editorial style**:
   - **Pass**: Uses plain language, sentence case for headings and table labels, zero emoji, and zero exclamation marks.
   - **Fail**: Uses Title Case headings, corporate jargon, or decorative emoji.
