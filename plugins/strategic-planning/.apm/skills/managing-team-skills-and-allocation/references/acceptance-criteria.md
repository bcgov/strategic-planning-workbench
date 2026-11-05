# Acceptance criteria: `managing-team-skills-and-allocation`

## Mandatory quality gates

1. **Interactive HITL pacing & format choice**:
   - **Pass**: Guides the user with a numbered menu, progressive 1–2 question turns, format negotiation (Markdown + Mermaid vs. Excel/CSV), and a recap confirmation gate before saving.
   - **Fail**: Dumps a wall of questions or overwrites registers without confirmation.
2. **Strict linkage to committed work (`WORK-X`) and capabilities (`CAP-X`)**:
   - **Pass**: Active project and operational assignments trace to `WORK-X` items; unapproved `IDEA-X` items appear only as optional learning/exploration interests.
   - **Fail**: Lists unapproved brainstormed ideas as active staff workload commitments.
3. **Bus-factor & growth matching diagnostics**:
   - **Pass**: Identifies single-point-of-failure capabilities/work items (no backup assigned), overloaded staff, and matches between staff growth interests and capability gaps.
   - **Fail**: Lists names and projects without analyzing capacity balance, backup coverage, or skill development alignment.
4. **B.C. Government Design System editorial style**:
   - **Pass**: Uses sentence case for all headings and labels, plain language, zero emoji, and valid quoted Mermaid syntax.
   - **Fail**: Uses Title Case headings, emoji, or broken Mermaid syntax.
