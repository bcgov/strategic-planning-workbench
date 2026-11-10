# Shared bookkeeping contract

Contract version: 3. An identical copy is carried by `developing-and-managing-strategy` and `managing-team-skills-and-allocation` so each skill stays self-contained. If you change one copy, change both and keep the version line identical.

## Contents

- [Who writes what](#1-who-writes-what)
- [Write rules](#2-write-rules)
- [Changelog entry](#3-changelog-entry)
- [Session status file](#4-session-status-file)
- [Changes that touch records another mode or skill owns](#5-changes-that-touch-records-another-mode-or-skill-owns)
- [Commitment evidence](#6-commitment-evidence)

## 1. Who writes what

One skill, many modes: each mode writes only its own sections. The team skill writes only `11`.

| File and section | Writing mode or skill | Others |
|---|---|---|
| `00-planning-session-status.md` structure and register status | Cycle | Update only your own lines and the follow-ups table |
| `01`, `02` | Context (and Update for changes) | Read only |
| `03`, `04` | Vision (and Update) | Read only |
| `05` | Capabilities (and Update) | Read only |
| `06` `## Constraints (CON-)`, `## Assumptions (ASM-)`, `## Evidence gaps (GAP-)` | Context (and Update) | Read only |
| `06` `## Risks (RSK-)` | Risks | Read only |
| `07` | Ideas | Read only |
| `08` | Work | Read only |
| `09` (alignment matrix and `## Transformation readiness (BTRA)`) | Alignment | Read only |
| `10` `## Roadmap and decision gates (PLT-, GATE-)` | Roadmap | Read only |
| `10` `## Success measures (MSR-)` | Measures | Read only |
| `11` | `managing-team-skills-and-allocation` | Read only |
| `changelog.md` | Any mode or skill, append only | Never edit or remove earlier rows |

Section headings above are fixed. Do not rename, merge or reorder them.

## 2. Write rules

1. Read the whole target file first, then change only your own section.
2. Keep every heading and ID. A new ID is the highest existing number for that prefix plus one, checked across the whole file including closed, rejected and cancelled rows. Never reuse an ID.
3. Never delete a record. Change its state and add a note.
4. If another mode's or skill's section needs a change, do not edit it. Add a follow-up (see section 5).
5. Show the proposed change and wait for confirmation before writing.

## 3. Changelog entry

Append one row per confirmed change to `changelog.md` with: update ID (`CHG-` next number), date, skill and mode, change class (`Simplification`, `Incremental`, `Re-direction`), source, registers touched, record IDs added or changed, summary, and downstream records affected with the mode or skill that owns each.

## 4. Session status file

Update `00` only for the registers your mode owns (status, key records, next action) and the date. Keep the `Open follow-ups` table current.

## 5. Changes that touch records another mode or skill owns

When a change affects records owned elsewhere (for example, an invalidated assumption that raises risk reviews, a changed objective that affects work items and the roadmap, or an allocation that clears a capacity flag):

1. List every affected record by ID with its owner in the recap.
2. After confirmation, add one row per affected record to `Open follow-ups` in `00`: ID, owner, what is needed, date raised, status `Open`.
3. A follow-up closes only when the owning mode or skill applies the change and logs it. Never mark someone else's follow-up closed.
4. Keep the original change and its follow-ups visible together in the changelog row.

## 6. Commitment evidence

A record may be committed (`Planned` or `Active` work, or a committed roadmap item) only when all three exist:

1. **Sponsor**: a named person with authority and the approval date.
2. **Owner**: a named delivery owner.
3. **Capacity**: an allocation recorded in `11`, or confirmed by the owner with the source stated.

If capacity is missing, keep the record in its current state, flag `Capacity unconfirmed`, and show it on roadmaps only as a decision gate. "The director approved it" is a sponsor, not capacity.
