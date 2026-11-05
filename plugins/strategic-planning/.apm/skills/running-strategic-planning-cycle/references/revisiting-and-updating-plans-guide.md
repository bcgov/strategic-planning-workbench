# Revisiting, updating, and storing strategic plans guide

## 1. Interactive storage path and source document discovery (Step 0)

Before creating, reading, or updating strategic registers, always confirm **where the team's living strategy outputs are stored** and **where any existing source documents live** using this plain-language prompt:

```text
Before we begin, where should I read and save your team's living strategy registers and visual outputs?
1. Dedicated user folder outside this repo — C:\Users\<username>\strategic-planning-outputs\<team-or-branch>\strategy\ (or ~/strategic-planning-outputs/<team-or-branch>/strategy/) (Recommended so your real strategy stays separate from the template repo)
2. Current workspace folder — ./strategy/ inside your currently open project folder
3. Custom folder or synced OneDrive / SharePoint path — Tell me the folder path you want to use

Also, do you have existing reference documents, briefing notes, or previous strategy files on disk that I should read from (and if so, what folder path are they in), or will you paste notes directly in our chat?
```

Record both the **Output directory path** and **Source documents path** at the top of `00-planning-session-status.md` so all subsequent skills use the exact same location without re-asking.

## 2. Interactive "revisit and refresh" sub-menu

When a user returns to an existing plan (Entry Option 3 or Option 4) or asks to revisit/update their strategy, present this 4-option cadence menu:

```text
What kind of strategy review or update are we running today?
1. Bi-weekly / monthly progress & team load check-in — Update active work (WORK-X), team capacity (MEM-X), and upcoming decision gates (GATE-X) (Recommended for regular check-ins)
2. Ingest new leadership direction or meeting notes — Parse notes from directors/CSB/Ministry, classify changes (TOGAF Phase H), and preview ripple impacts
3. Quarterly / horizon plateau refresh — Check whether Horizon 1 plateau (PLT-001) is met, promote validated ideas (IDEA-X), review measures (MSR-X), and audit expiring dispensations (DSP-X)
4. Urgent operational pivot or invalidated assumption — Handle a failed assumption (ASM-X) or urgent ministerial/court operational request (log a time-boxed dispensation DSP-X or rebalance horizons)
```

## 3. Four revisit workflows and ripple-impact chains

| Revisit cadence | Registers inspected & updated | Ripple-impact checks required before saving |
|---|---|---|
| **1. Progress & team load check-in** | `08-work-inventory.md`<br>`11-team-skills-and-allocation.md`<br>`00-planning-session-status.md` | Check if blocked or delayed `WORK-X` items overload a single `MEM-X` lead (`bus factor = 1` or `>100%` load) or delay a `GATE-X` milestone. |
| **2. Leadership note / priority ingestion** | `01-org-hierarchy-and-context.md`<br>`02-stakeholders-and-concerns.md`<br>`03-target-vision-and-objectives.md`<br>`changelog.md` | Classify via TOGAF Phase H (`Simplification`, `Incremental`, or `Re-direction`). Show which `OBJ-X`, `CAP-X`, `IDEA-X`, and `WORK-X` items are affected. |
| **3. Quarterly / horizon plateau review** | `05-business-capabilities.md`<br>`07-idea-inventory.md`<br>`09-alignment-traceability-matrix.md`<br>`10-roadmap-and-success-measures.md` | Verify whether target capability maturity (`CAP-X` `L-current -> L-target`) for `PLT-001` is reached, check `MSR-X` actuals vs. guardrails, and review any `candidate` `IDEA-X` ready for the Promotion Gate. |
| **4. Urgent pivot or invalidated assumption** | `06-constraints-assumptions-risks.md`<br>`08-work-inventory.md`<br>`10-roadmap-and-success-measures.md`<br>`changelog.md` | If an urgent request bypasses target principles (`PRN-X`) or capabilities (`CAP-X`), log a **Time-boxed strategic dispensation (`DSP-X`)** with an explicit expiry date and remediation trigger. |

## 4. Non-destructive update rules

1. **Never overwrite history silently**: Keep stable IDs (`MAN-X`, `OBJ-X`, `VST-X`, `CAP-X`, `IDEA-X`, `WORK-X`, `MEM-X`, `PLT-X`, `MSR-X`, `DSP-X`) intact and append a delta entry to `changelog.md`.
2. **Always pause at a recap confirmation gate**: Show the proposed additions, status changes, and ripple impacts across registers and wait for user approval before writing to disk.
