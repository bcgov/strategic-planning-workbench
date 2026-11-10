# Acceptance criteria: `rendering-strategic-visuals-and-decks`

## Mandatory quality gates

1. **Interactive format negotiation**:
   - **Pass**: Offers a clear numbered menu of visual output formats (Mermaid diagrams, B.C. Gov HTML dashboard, Executive slide deck) and confirms scope with the user.
   - **Fail**: Produces a single unrequested format without checking audience or format preference when ambiguous.
2. **B.C. Government Design System compliance**:
   - **Pass**: Uses B.C. Design System v5 color tokens (`#013366`, `#FAF9F8`, `#FBD389`, `#2E5DD7`), BC Sans typography, sentence case for all headings and labels, zero emoji, zero gradients, and includes the mandatory Indigenous acknowledgment footer on full-page HTML/slide outputs.
   - **Fail**: Uses Title Case headings, emoji, gradients, arbitrary colors, or omits the Indigenous acknowledgment band.
3. **Visual separation between ideas and committed work**:
   - **Pass**: Committed `WORK-X` items render as solid bars/cards, while unapproved `IDEA-X` items render only as dashed nodes or `milestone` decision gates.
   - **Fail**: Renders unapproved brainstormed ideas as scheduled Gantt bars alongside committed projects.

5. **Uncommitted work is not drawn as committed**:
   - **Pass**: A work item flagged `Capacity unconfirmed`, or missing sponsor, owner or confirmed capacity, appears as a decision gate with the missing evidence labeled.
   - **Fail**: Such an item is drawn as a solid bar, card or committed roadmap entry.
