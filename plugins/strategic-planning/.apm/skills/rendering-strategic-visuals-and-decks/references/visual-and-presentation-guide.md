# Visual strategy and executive presentation guide

## 1. Interactive format negotiation menu (for Claude Cowork & GitHub Copilot)

When a user asks to visualize their strategy, roadmap, or presentation, present this numbered menu:

```text
How would you like to visualize and share this material?
1. Mermaid visual package — line-of-sight tree, traceability map, capability gap chart, and Gantt roadmap (Recommended for Git/PRs)
2. B.C. Gov HTML Executive Brief — 1–2 page audience-tailored architecture or strategy brief (print-to-PDF ready)
3. B.C. Gov HTML Dashboard or Logic Model Card View — browser-ready Strategy on a Page or 7-stage causal results chain
4. Executive presentation deck — leadership briefing (Marp Markdown or B.C. Gov PowerPoint .pptx spec)
5. Custom combination — tell me your audience (e.g., executive leadership, privacy/policy reviewers, or partner branches) and I will tailor the package
```

## 2. Matching the visual format to the strategic question

| Strategic question | Recommended visual format | Key guardrail |
|---|---|---|
| *"How does our team's strategy fit into CSB, AG Ministry, and B.C. Government direction?"* | **Mermaid top-down flowchart (`flowchart TD`)** showing Tier 1 (Province) $\rightarrow$ Tier 2 (Ministry) $\rightarrow$ Tier 3 (CSB) $\rightarrow$ Tier 4 (Division) $\rightarrow$ Tier 5 (Team `OBJ-X`). | Tag any inferred link as `Interpreted`. |
| *"How do our objectives, capabilities, ideas, and active work connect?"* | **Mermaid left-to-right traceability graph (`flowchart LR`)** linking `OBJ-X` $\rightarrow$ `CAP-X` $\rightarrow$ `WORK-X` / `IDEA-X`, highlighting gaps in dashed nodes. | Visually highlight orphaned work and unaddressed capability gaps. |
| *"What is our roadmap and sequencing over the next 3 horizons or quarters?"* | **Mermaid horizon flowchart (`flowchart LR`)** + **High-level Mermaid Gantt chart (`gantt`)** with milestone gates. | Show `WORK-X` as active/committed bars and `IDEA-X` strictly as `milestone` decision gates. |
| *"Where are our biggest capability maturity gaps?"* | **Mermaid XY chart (`xychart-beta`)** comparing Current vs. Target maturity (0–5) across `CAP-X`. | Pair with the 5-pillar narrative (People, Process, Data, Tech, Governance). |
| *"How do we brief executive leadership, privacy reviewers, or partner branches in 10 minutes?"* | **Executive brief (`render_html_brief.py --type executive-brief`)**, **Logic model card (`--type logic-model`)**, or **Executive deck (`render_deck.py`)**. | End with concrete decisions and evidence gaps needing leadership resolution. |
| *"How do we give architects and product leads a readable reference on core technologies and hosting profiles?"* | **JSON-driven Technology Profiles page** (`technology-profiles.json` → `technology-profiles.html` via `render_html_brief.py --type executive-brief`, wired as a tab in `site.json`). | Separate *how capabilities are built* from *where they are hosted*; embed rendered `.svg` deployment/sequence views and flag spike/unproven items clearly. |

## 3. Mermaid syntax safety rules

1. **Always quote node labels** containing parentheses, colons, slashes, or brackets:
   - Correct: `CAP1["CAP-001:<br>Knowledge mgmt<br>(L1 -> L3)"]`
2. **Wrap box and edge labels with `<br>` tags**: Insert `<br>` line breaks every 15–18 characters inside flowchart node and edge labels so GitHub and Markdown viewers wrap text vertically instead of clipping boxes horizontally.
3. **Use dashed borders (`stroke-dasharray`)** to distinguish unapproved ideas (`IDEA-X`) or unaddressed gaps from committed work (`WORK-X`).
4. **In Mermaid `gantt` charts**, represent unapproved candidate ideas (`IDEA-X`) and assumption validations (`ASM-X`) using `:milestone,` rather than multi-month task bars.
