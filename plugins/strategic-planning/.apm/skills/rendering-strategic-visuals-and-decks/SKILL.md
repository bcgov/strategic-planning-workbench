---
name: rendering-strategic-visuals-and-decks
description: "Guides users interactively to generate B.C. Government Design System-styled strategic outputs including Mermaid alignment diagrams, capability maps, high-level roadmaps and Gantt charts, HTML Strategy on a Page dashboards, and executive presentation slide decks from the existing registers. Use when asked to visualize the strategy, draw a Mermaid roadmap or Gantt chart, build a BC Gov HTML strategy view, or create a leadership presentation deck. Not for creating or changing the content being shown (use developing-and-managing-strategy), classifying new items (use triaging-new-items), logic model diagrams (use designing-logic-models) or team allocation data (use managing-team-skills-and-allocation)."
---

# Rendering strategic visuals and decks

Guides users interactively to choose the right audience and format, then transforms living strategic registers (`strategy/`), solution-architecture workbenches (`02-architecture.md`, `work-packages/`, `adrs/`, `04-open-questions.md`), or `designing-logic-models` JSON payloads into **Mermaid diagrams**, **B.C. Government Design System HTML briefs, logic-model cards, and dashboards**, and **executive presentation decks** (Markdown/Marp or PowerPoint via `bc-gov-design-system`).

## Contents

- [Constraints](#constraints)
- [Quick start](#quick-start)
- [Workflow](#workflow)
- [Verification](#verification)
- [References](#references)

## Constraints

1. **Interactive format negotiation**: Open with a numbered format menu (`1. Mermaid visual package`, `2. B.C. Gov HTML Executive Brief / Architecture One-Pager (print-to-PDF ready)`, `3. B.C. Gov HTML Strategy / Portfolio Dashboard or Logic Model Card View`, `4. Executive slide deck (Marp Markdown / PowerPoint .pptx spec)`, `5. Custom combination`) and ask who the audience is.
1a. **Guided interaction**: Guide the user step by step with questions, following [guided-interaction.md](references/guided-interaction.md): open with a numbered menu or one question, ask 1–2 per turn with a recommended default, show progress, accept "I don't know" as an open item, and confirm a recap before every write.
2. **B.C. Government Design System compliance**: Follow [bc-gov-visual-and-brand-style.md](references/bc-gov-visual-and-brand-style.md) (BC Sans typography, primary navy `#013366`, gold accent `#FBD389`, off-white surface `#FAF9F8`, focus ring `#2E5DD7`, WCAG 2.1 AA contrast, sentence-case headings, zero emoji, zero gradients, and the mandatory Indigenous acknowledgment footer on full-page HTML and slide decks).
3. **Visually separate committed work from ideas**: Committed initiatives (`WORK-X`) render as solid bars/cards; unapproved ideas (`IDEA-X`) render strictly as dashed nodes or `milestone` decision gates. A `WORK-X` item flagged `Capacity unconfirmed`, or lacking a sponsor with approval date, an owner or confirmed capacity, is not committed: render it as a decision gate and label the missing evidence.
4. **Safe Mermaid syntax and `<br>` box wrapping**: Quote node labels containing parentheses, colons, or brackets, and insert `<br>` tags every 15–18 characters inside node and edge labels so boxes wrap vertically without horizontal clipping on GitHub.

## Quick start

1. Read [visual-and-presentation-guide.md](references/visual-and-presentation-guide.md) and [bc-gov-visual-and-brand-style.md](references/bc-gov-visual-and-brand-style.md).
2. Ask the user to select their audience and output format from the numbered menu.
3. Structure the extracted content as JSON matching the appropriate schema in `assets/schemas/` (`executive-brief.schema.json`, `logic-model.schema.json`, `strategy-dashboard.schema.json`, or `executive-deck.schema.json`).
4. Render the output using the Python scripts in `scripts/` (`render_html_brief.py`, `render_mermaid_package.py`, `render_deck.py`) or the static templates in `assets/templates/` (and delegate `.pptx` binary generation to `bc-gov-design-system` using the `--format pptx-spec` output).

## Workflow

1. **Interactive Audience & Format Selection**: Present the 5-option format menu and confirm whether the output is for executive leadership, privacy/policy reviewers, a team workshop, or partner ministries/branches.
2. **Extract & Confirm Scope**: Pull current items from `strategy/` (`OBJ-X`, `CAP-X`, `WORK-X`, `IDEA-X`, `MSR-X`), from a `solution-architecture` workbench (`02-architecture.md`, `work-packages/`, `adrs/`, `04-open-questions.md`), or from a `designing-logic-models` JSON payload, and confirm the scope via a brief recap gate.
3. **Author Validated JSON & Render**: Write or update the structured JSON payload matching `assets/schemas/`, then run `scripts/render_html_brief.py`, `scripts/render_mermaid_package.py`, or `scripts/render_deck.py` to produce compliant B.C. Gov outputs.

## Related skills

| Need | Skill |
|---|---|
| A register is empty or out of date (objectives, capabilities, work, roadmap, measures) | `developing-and-managing-strategy` |
| New or unclear items to show | `triaging-new-items` |
| Allocation or capacity visuals from register `11` | `managing-team-skills-and-allocation` |
| Logic model diagrams | `designing-logic-models` |
| Scaffolding or validating `solution-architecture` / `enterprise-architecture` workbenches | `developing-solution-architecture` |
| Technology & architecture registry (`architecture-registry.json`) | `managing-architecture-registry` |

This skill reads the registers and writes no register content; if something is missing, ask or hand off instead of inventing it.

## Verification

Check outputs against [acceptance-criteria.md](references/acceptance-criteria.md):
- Follows B.C. Government Design System tokens, sentence case, zero emoji, and Indigenous acknowledgment rules.
- Separates `WORK-X` commitments from `IDEA-X` decision gates in all charts and slides.

## Dependencies

- **HTML, Mermaid, Marp Markdown, and `pptx-spec` JSON rendering (`scripts/render_*.py`):** Python 3.10+ standard library only (zero third-party `pip` packages). Supports `--embed-images` in `render_html_brief.py` to inline `.svg`/`.png` diagrams as self-contained data URIs.
- **Mermaid `.mmd` to `.svg`/`.png` image conversion (optional, for embedding diagrams in HTML/decks):** Node.js with `@mermaid-js/mermaid-cli` (`npx -y @mermaid-js/mermaid-cli -i <diagram.mmd> -o <out.svg>`).
- **Binary PowerPoint (`.pptx`) generation:** Delegates to `bc-gov-design-system` (`generate.js` and `bc-logo.png` in that skill), which requires **Node.js** and **`pptxgenjs`** (`npm install pptxgenjs`).
- **Optional Marp HTML/PDF export:** Requires `@marp-team/marp-cli` (`npx @marp-team/marp-cli`).

## References

- Methodology & brand rules: [visual-and-presentation-guide.md](references/visual-and-presentation-guide.md) • [bc-gov-visual-and-brand-style.md](references/bc-gov-visual-and-brand-style.md)
- JSON schemas: `assets/schemas/executive-brief.schema.json` • `assets/schemas/logic-model.schema.json` • `assets/schemas/strategy-dashboard.schema.json` • `assets/schemas/executive-deck.schema.json` • `assets/schemas/architecture-on-a-page.schema.json` • `assets/schemas/diagram-gallery.schema.json` • `assets/schemas/deliverable-site.schema.json`
- Renderers: `scripts/render_html_brief.py` • `scripts/render_mermaid_package.py` • `scripts/render_deck.py` • `scripts/test_renderers.py`
- Templates: [mermaid-strategy-visuals.md](assets/templates/mermaid-strategy-visuals.md) • [executive-strategy-deck.md](assets/templates/executive-strategy-deck.md) • `assets/templates/bc-gov-strategy-dashboard.html`
- Quality gate: [acceptance-criteria.md](references/acceptance-criteria.md)
