# Workspace, first run and returning sessions

How the skill decides whether this is a first run, where the strategy lives, and what to offer next. Follows the persistent plugin configuration pattern: read the remembered setting silently, and interview only when it is missing.

## Contents

- [Finding the strategy folder](#1-finding-the-strategy-folder)
- [First run](#2-first-run)
- [Returning sessions](#3-returning-sessions)
- [Partial progress](#4-partial-progress)
- [What is remembered](#5-what-is-remembered)

## 1. Finding the strategy folder

Check in this order and stop at the first hit:

1. The remembered path (see section 5).
2. `./strategy/` in the current workspace.
3. `~/strategic-planning-outputs/*/strategy/`. If several teams match, ask which one.

A hit counts only if `00-planning-session-status.md` or at least one of registers `01`–`11` exists. If the remembered path is gone, say so and fall back to the next check. If nothing is found, it is a first run.

### Resolution failure cases

Resolve the workspace fully before creating anything. Never create a new strategy folder while any candidate folder exists without asking.

| Situation | Do this |
|---|---|
| `00` is missing but registers `01`-`11` exist (for example, imported files) | Adopt them: create `00` from what exists, set register status from the files, and continue; do not restart the interview |
| Remembered path no longer exists | Say so, fall back to the scan, and update the remembered path after confirmation |
| More than one candidate folder | List them with last-updated dates and ask which to use, or whether to start a new one |
| Folder found but empty | Treat as a first run in that folder; confirm it is the right place |
| Folder is read-only or on an unavailable synced drive | Report it and offer another location; write nothing |

## 2. First run

1. **Ask where to save**: `1. ~/strategic-planning-outputs/<team>/strategy/ (Recommended)`, `2. ./strategy/`, `3. Custom path`. Ask where existing source documents and notes live.
2. **Ask the team name** if the folder uses one.
3. **Offer the starting path**:

| Path | Use when | What happens |
|---|---|---|
| 1. Top-down interview (Recommended) | The team has no written strategy | Context, then Vision, then Capabilities, one step at a time |
| 2. Bottom-up from existing items | The team has projects, problems or ideas but no strategy | Paste them; hand to `triaging-new-items`; return later to build the strategy around them |
| 3. Import notes | The team has meeting notes or leadership messages | Hand to `triaging-new-items`; use Update mode for direction and stakeholder changes |

4. **Create** `00-planning-session-status.md` from the template, record the folder, source path, chosen path and next 15-minute step, and remember the folder.

## 3. Returning sessions

Read `00` and the registers, then report in plain language what exists, what is unfinished and what changed since the last entry. Offer:

1. Continue where we left off (Recommended when a step is unfinished)
2. Update the strategy: priorities, stakeholders, objectives, assumptions, constraints (Update mode)
3. Check alignment or success measures (Alignment or Measures mode)
4. Revisit on a cadence: bi-weekly check-in, leadership note, quarterly refresh, or urgent pivot ([revisit guide](revisiting-and-updating-plans-guide.md)); item-level checks are handed to the owner skill
5. Produce visuals or a deck (`rendering-strategic-visuals-and-decks`)

Item work is not a menu option. Skip the menu and hand off directly:

| The user says | Hand to |
|---|---|
| A new, mixed or unclear item ("log this problem", pasted notes) | `triaging-new-items` |
| A named record with a verb ("promote IDEA-9", "update WORK-12"), or asks for ideas, work, risks, scoring or the roadmap | The matching item mode (Ideas, Work, Risks, Score or Roadmap) |
| Team skills or capacity | `managing-team-skills-and-allocation` |

If the strategy folder is not yet resolved, resolve it first.

## 4. Partial progress

`00` records the stage and the status of each register (`Not started`, `Draft`, `Baseline confirmed`). Resume at the first register that is not `Baseline confirmed`; a `Draft` register is resumed from where it stopped, not restarted. Never re-ask questions whose answers are already saved; summarize them and ask only whether anything changed.

## 5. What is remembered

| Setting | Meaning |
|---|---|
| `strategy_dir` | Resolved strategy folder |
| `source_docs_dir` | Where source documents and notes live |
| `team_name` | Team label used in the folder name and headings |

Store these in the plugin's persistent local configuration when the host provides one. If the host has none, skip the remembered path, use the folder scan, and confirm the result once per session ("Is this still your strategy folder?"). Never store secrets or personal data in this configuration.
