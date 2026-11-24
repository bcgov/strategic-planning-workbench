# Deliverables sync workflow

Use when a project keeps generated audience pages under `deliverables/` (HTML site, SVGs, executive deck) that must track an architecture workbench (`02-architecture.md`, `architecture/`, `adrs/`, `work-packages/`, `diagrams/*.mmd`).

## Why there is a manual step

The renderers are one-way: JSON in, HTML, SVG or deck out. No script reads Markdown and writes JSON, because the pages are audience-written summaries, not copies. The agent reads the changed sources and edits `deliverables/data/*.json`. Two scripts make that step targeted and the rest one command.

## Steps

1. **Find what drifted.** From the workbench root run `python3 scripts/check_deliverable_sync.py` (path relative to this skill). It reports, without editing:
   - `adr-range`: an "ADR-001 to ADR-NNN" range that stops below the latest ADR
   - `work-package`: a `WP-NN` heading in `work-packages/README.md` that no JSON mentions
   - `diagram`: a `.mmd` with a missing or older `.svg`, or no gallery entry
   - `registry`: a `TECH-001 to TECH-NNN` range below `architecture-registry.json`
   - `source-newer`: a page whose `date` (or `reviewed`) is older than the newest change to its sources
2. **Update the JSON.** Read only the sources behind each finding (plus any changed in `git log`). Keep claims consistent with the source, label unapproved items as proposed, and keep `WORK-X` committed and `IDEA-X` as gates. If a flagged page is still accurate, set `"reviewed": "YYYY-MM-DD"` in its JSON instead of editing it.
3. **Build.** `python3 scripts/build_deliverables.py` runs the drift report, validates every page JSON listed in `data/site.json` (existence, emoji, required fields), renders the site and converts changed `.mmd` files to `.svg` (unchanged ones are skipped), renders the Marp and pptx-spec deck, then checks relative links and anchors. Use `--check` to stop after validation, `--skip-mmd` when Mermaid CLI is unavailable, `--skip-deck` to leave the deck alone.
4. **Review `git diff`** before committing. Binary `.pptx` is still delegated to `bc-gov-design-system`.

## Rules

- Never hand-edit generated HTML or SVG; the next build overwrites it.
- `--type site --validate-only` in `render_html_brief.py` only checks the site file; use `build_deliverables.py --check` to validate every page.
- Exit codes: `check_deliverable_sync.py` returns 1 on drift; `build_deliverables.py` returns 1 on validation errors or broken links (drift alone is informational during a build, and fails `--check`).
