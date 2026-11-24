# Deliverables sync workflow

For projects that keep generated audience pages under `deliverables/` (HTML site, SVGs, executive deck) fed by an architecture workbench (`02-architecture.md`, `architecture/`, `adrs/`, `work-packages/`, `diagrams/*.mmd`). Sources are often edited by people or AI directly; the JSON must follow deterministically where possible and by an LLM where not.

## Three kinds of content, three mechanisms

| Content | Mechanism | Deterministic? |
|---|---|---|
| Mechanical facts: latest ADR, ADR/TECH ranges and counts, work-package IDs, diagram count | `{{token}}` placeholders in the JSON, expanded at render time by `build_deliverables.py` (see `deliverable_lock.py facts`) | Yes, cannot drift |
| Diagram images | `.mmd` to `.svg` conversion, skipped when the SVG is newer | Yes |
| Narrative summaries, claims, decisions | LLM edit of the page JSON, guided by a hash-based worklist | Detection is deterministic; the edit is generative and reviewed |

Tokens: `{{adr.latest}}` `{{adr.count}}` `{{adr.range}}` `{{tech.latest}}` `{{tech.count}}` `{{tech.range}}` `{{wp.count}}` `{{wp.ids}}` `{{diagram.count}}`. An unknown token fails the build. Replace any hardcoded range or count the checker flags with a token.

## Lifecycle

1. **Source changes.** A user shares guidance or a vision; an agent edits the Markdown (in the workbench or the project repo). Nothing else happens yet.
2. **Detect.** `deliverable_lock.py status` compares the SHA-256 of every source file a page declares against `data/sync.lock.json`. States: `ok`, `stale` (a source changed, appeared or disappeared) or `unstamped`. Content hashes ignore timestamps, branches and CRLF, so any editor is caught, including uncommitted edits.
3. **Plan.** `deliverable_lock.py worklist --diff` lists each stale page, its changed sources, and the source diff since the last stamp, so the agent reads only what changed.
4. **Update the JSON.** Mechanical facts need no edit (tokens). For narrative, the agent edits `data/<page>.json` to match the sources: keep claims consistent with the source, label unapproved items as proposed, keep `WORK-X` committed and `IDEA-X` as gates. If the sources changed but the page is still accurate, say so to the user.
5. **Stamp.** `deliverable_lock.py stamp <page>.json` records the new hashes. Stamp only after step 4 (or after confirming no edit is needed); stamping is the claim "this page reflects those sources". Never `--all` to silence a worklist.
6. **Render on request.** `build_deliverables.py` refuses to render stale or unstamped pages (override with `--allow-stale`), validates every page JSON, expands tokens, renders the site and deck, converts changed diagrams, then checks links. Run it when the user asks for refreshed deliverables, not after every edit. Binary `.pptx` stays delegated to `bc-gov-design-system`.
7. **Enforce.** `build_deliverables.py --check` (or `deliverable_lock.py status`) exits 1 when any page is stale; wire it to a pre-commit hook or CI job so Markdown cannot change without the JSON being refreshed or confirmed.

## Files

- `data/sources.json`: per page, the globs (relative to the repo root) that feed it. `defaults` applies to pages without an entry; `$defaults` inside a list extends it. Narrow each page to its real sources so unrelated edits do not mark it stale. Created by `deliverable_lock.py init`.
- `data/sync.lock.json`: generated hashes, commit and date per page. Commit it with the JSON.
- `check_deliverable_sync.py`: extra read-only checks (stale hardcoded ADR/TECH ranges, work packages missing from the JSON, missing or older SVGs, diagrams absent from the gallery).

## Rules

- Never hand-edit generated HTML or SVG; the next build overwrites it.
- `render_html_brief.py --type site --validate-only` checks only `site.json`; use `build_deliverables.py --check` to validate every page.
- New sources: add them to `sources.json`; a new file matching an existing glob marks the page stale automatically.
