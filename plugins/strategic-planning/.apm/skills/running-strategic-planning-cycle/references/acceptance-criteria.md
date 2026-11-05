# Acceptance criteria: running-strategic-planning-cycle

1. **Output path & source document confirmation first**: Confirms where strategy registers/outputs should be saved (offering `C:\Users\<username>\strategic-planning-outputs\<team-name>\strategy\` / `~/strategic-planning-outputs/<team-name>/strategy/`, `./strategy/`, or a custom path) and asks where existing reference documents live before reading or writing files.
2. **Plain-language 5-option entry menu & 4-option revisit menu**: Offers Top-Down, Bottom-Up/Middle-Out, Resume/Readiness Check, Meeting Note Ingestion, and Fast-Track Briefing options—plus the 4 revisit cadences in `revisiting-and-updating-plans-guide.md` when updating existing plans.
3. **TOGAF ADM stage traceability**: Maps progress across the 6 workbench stages (ADM Preliminary/Phase A through Phase H) without exposing heavy jargon unless requested.
4. **Persistent session status (`00-planning-session-status.md`)**: Records the chosen output folder path, source document path, register status, open assumptions (`ASM-X`), pending idea promotion gates (`IDEA-X`), active strategic dispensations (`DSP-X`), and next recommended action.
5. **B.C. Government Design System formatting**: Uses sentence-case headings and table labels, plain direct language, zero emoji, and `<br>` tags inside Mermaid boxes.
