# B.C. Government Design System visual and brand style

All visual outputs, HTML dashboards, SharePoint-bound summaries, and slide decks produced by `strategic-planning` align with the **B.C. Government Design System (tokens v5.0.0, components v0.8.1)** and delegate full binary `.pptx` or React/Blazor component builds to the `bc-gov-design-system` skill when installed.

## 1. Content and editorial fundamentals

1. **Voice and tone**: Professional, plain, direct, calm, and authoritative. Avoid corporate buzzwords, legalese, or exclamation marks.
2. **Sentence case**: Use sentence case for all headings, slide titles, table column headers, and button/tag labels (*"Strategic objectives and expected value"*, never *"Strategic Objectives And Expected Value"*). Preserve proper nouns and acronyms: B.C., CSB, AG, FOIPPA, DRIPA, OKR.
3. **Zero emoji**: Never use emoji in headings, status badges, tables, Mermaid nodes, or slide decks. Use clean text labels or Font Awesome 6 outline icons in HTML.
4. **Mandatory Indigenous acknowledgment**:
   - Full-page HTML views must include the dark `#252423` footer band with a `3px solid #FBD389` top border and the B.C. Public Service territorial acknowledgment text.
   - Slide decks must include the `#FBD389` amber band on title and closing slides.

## 2. Official B.C. Government Design System color tokens

| Token role | CSS variable | Hex | PowerPoint (`pptxgenjs`, no `#`) | Strategic planning usage |
|---|---|---|---|---|
| **Primary navy** | `--color-brand-primary` | `#013366` | `013366` | Header bar, primary action buttons, table headers, Committed Work (`WORK-X`) accents |
| **Primary hover** | `--color-brand-primary-hover` | `#1E5189` | `1E5189` | Interactive hover states, section divider numbers |
| **Focus / info blue** | `--color-brand-focus` / `--color-info` | `#2E5DD7` | `2E5DD7` | 2px focus ring (`4px` offset), info banners, Exploring/Validated idea badges |
| **Info background** | `--color-info-bg` | `#D8EAFD` | `D8EAFD` | Info callouts, `.tag-blue` backgrounds |
| **Indigenous gold/amber** | `--color-border-indigenous` | `#FBD389` | `FBD389` | Header/footer gold accent line, slide title/closing band, key stat callouts on navy |
| **Surface default** | `--color-surface-default` | `#FAF9F8` | `FAFAF8` | Secondary section backgrounds, alternating table rows, cards |
| **Surface dark** | `--color-surface-dark` | `#252423` | `252423` | Indigenous acknowledgment band, closing slide background |
| **Text primary** | `--color-text-primary` | `#2D2D2D` | `2D2D2D` | Body copy and primary table text (WCAG 2.1 AA $\ge 4.5:1$) |
| **Text secondary** | `--color-text-secondary` | `#474543` | `474543` | Captions, metadata, source citations |
| **Border** | `--color-border` | `#D8D8D8` | `D8D8D8` | `1px solid` card borders, table gridlines, section dividers |
| **Success green** | `--color-success` / `--color-success-bg` | `#42814A` / `#F6FFF8` | `42814A` | Confirmed direction, Validated assumptions, Active/Completed work tags (`.tag-green`) |
| **Warning amber** | `--color-warning` / `--color-warning-bg` | `#F8BB47` / `#FEF1D8` | `F8BB47` | Interpreted direction, Unvalidated assumptions, Candidate decision gates (`.tag-yellow`) |
| **Danger red** | `--color-danger` / `--color-danger-bg` | `#CE3E39` / `#F4E1E2` | `CE3E39` | High strategic risks, Blocked work, Unaddressed capability gaps (`.tag-red`) |

## 3. Typography and layout rules

- **Font family**: `'BC Sans', 'Noto Sans', sans-serif` for HTML/web (`Calibri` as the portable fallback in PowerPoint `.pptx` when BC Sans is not installed locally).
- **Type scale (px)**: `12` (label/tag) $\rightarrow$ `14` (body-sm/table) $\rightarrow$ `16` (body) $\rightarrow$ `18` (body-lg/h6) $\rightarrow$ `20` (h5) $\rightarrow$ `24` (h4) $\rightarrow$ `28` (h3) $\rightarrow$ `32` (h2) $\rightarrow$ `36` (h1).
- **Flat aesthetic**: Zero gradients, zero heavy drop shadows; `4px` border radius on cards, tags, and buttons.
