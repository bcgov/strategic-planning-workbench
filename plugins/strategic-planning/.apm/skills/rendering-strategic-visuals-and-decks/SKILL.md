---
name: rendering-strategic-visuals-and-decks
description: "Guides users interactively to generate B.C. Government Design System-styled strategic outputs including Mermaid alignment diagrams, capability maps, high-level roadmaps and Gantt charts, HTML Strategy on a Page dashboards, and executive presentation slide decks from the existing registers. Use when asked to visualize the strategy, draw a Mermaid roadmap or Gantt chart, build a BC Gov HTML strategy view, or create a leadership presentation deck. Not for creating or changing the content being shown (use developing-and-managing-strategy), classifying new items (use triaging-new-items), logic model diagrams (use designing-logic-models) or team allocation data (use managing-team-skills-and-allocation)."
---

# Rendering strategic visuals and decks

Guides users interactively to choose the right audience and format, then transforms the team's living strategic registers (`strategy/`) into **Mermaid diagrams**, **B.C. Government Design System HTML dashboards**, and **executive presentation decks** (Markdown/Marp or PowerPoint via `bc-gov-design-system`).

## Contents

- [Constraints](#constraints)
- [Quick start](#quick-start)
- [Workflow](#workflow)
- [Verification](#verification)
- [References](#references)

## Constraints

1. **Interactive format negotiation**: Open with a numbered format menu (`1. Mermaid roadmap, Gantt & alignment diagrams`, `2. B.C. Gov HTML Strategy on a Page dashboard`, `3. Executive slide deck (Markdown / PowerPoint)`, `4. Complete visual package`) and ask who the audience is.
1a. **Guided interaction**: Guide the user step by step with questions, following [guided-interaction.md](references/guided-interaction.md): open with a numbered menu or one question, ask 1–2 per turn with a recommended default, show progress, accept "I don't know" as an open item, and confirm a recap before every write.
2. **B.C. Government Design System compliance**: Follow [bc-gov-visual-and-brand-style.md](references/bc-gov-visual-and-brand-style.md) (BC Sans typography, primary navy `#013366`, gold accent `#FBD389`, off-white surface `#FAF9F8`, focus ring `#2E5DD7`, WCAG 2.1 AA contrast, sentence-case headings, zero emoji, zero gradients, and the mandatory Indigenous acknowledgment footer on full-page HTML and slide decks).
3. **Visually separate committed work from ideas**: Committed initiatives (`WORK-X`) render as solid bars/cards; unapproved ideas (`IDEA-X`) render strictly as dashed nodes or `milestone` decision gates. A `WORK-X` item flagged `Capacity unconfirmed`, or lacking a sponsor with approval date, an owner or confirmed capacity, is not committed: render it as a decision gate and label the missing evidence.
4. **Safe Mermaid syntax and `<br>` box wrapping**: Quote node labels containing parentheses, colons, or brackets, and insert `<br>` tags every 15–18 characters inside node and edge labels so boxes wrap vertically without horizontal clipping on GitHub.

## Quick start

1. Read [visual-and-presentation-guide.md](references/visual-and-presentation-guide.md) and [bc-gov-visual-and-brand-style.md](references/bc-gov-visual-and-brand-style.md).
2. Ask the user to select their audience and output format from the numbered menu.
3. Generate the chosen output using [mermaid-strategy-visuals.md](assets/templates/mermaid-strategy-visuals.md), [executive-strategy-deck.md](assets/templates/executive-strategy-deck.md), or `assets/templates/bc-gov-strategy-dashboard.html` (and delegate `.pptx` binary generation to `bc-gov-design-system` when requested).

## Workflow

1. **Interactive Audience & Format Selection**: Present the 4-option format menu and confirm whether the output is for executive leadership (Chris/Jessica/CSB), a team workshop, or partner branches.
2. **Extract & Confirm Register Scope**: Pull current objectives (`OBJ-X`), capabilities (`CAP-X`), committed work (`WORK-X`), decision gates (`IDEA-X`), and measures (`MSR-X`) from `strategy/` and confirm the scope via a brief recap gate.
3. **Render Compliant Visuals**: Produce the selected Mermaid diagrams ([mermaid-strategy-visuals.md](assets/templates/mermaid-strategy-visuals.md)), B.C. Gov HTML Strategy Dashboard (`assets/templates/bc-gov-strategy-dashboard.html`), or slide deck ([executive-strategy-deck.md](assets/templates/executive-strategy-deck.md)).

## Related skills

| Need | Skill |
|---|---|
| A register is empty or out of date (objectives, capabilities, work, roadmap, measures) | `developing-and-managing-strategy` |
| New or unclear items to show | `triaging-new-items` |
| Allocation or capacity visuals from register `11` | `managing-team-skills-and-allocation` |
| Logic model diagrams | `designing-logic-models` |

This skill reads the registers and writes no register content; if something is missing, ask or hand off instead of inventing it.

## Verification

Check outputs against [acceptance-criteria.md](references/acceptance-criteria.md):
- Follows B.C. Government Design System tokens, sentence case, zero emoji, and Indigenous acknowledgment rules.
- Separates `WORK-X` commitments from `IDEA-X` decision gates in all charts and slides.

## References

- Methodology & brand rules: [visual-and-presentation-guide.md](references/visual-and-presentation-guide.md) • [bc-gov-visual-and-brand-style.md](references/bc-gov-visual-and-brand-style.md)
- Templates: [mermaid-strategy-visuals.md](assets/templates/mermaid-strategy-visuals.md) • [executive-strategy-deck.md](assets/templates/executive-strategy-deck.md) • `assets/templates/bc-gov-strategy-dashboard.html`
- Quality gate: [acceptance-criteria.md](references/acceptance-criteria.md)
