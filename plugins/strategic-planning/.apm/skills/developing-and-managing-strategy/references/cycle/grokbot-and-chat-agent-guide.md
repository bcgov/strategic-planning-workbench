# GrokBot, Grok Build, Grok Cloud, and chat-agent integration guide

## 1. How GrokBot and APM targets interact with this workbench

The 11 skills in `strategic-planning` are authored to the **Agent Skills Open Standard** (`AGENTS.md` + self-contained `.apm/skills/<skill-name>/SKILL.md` with zero symlinks). In Microsoft APM (`0.35.0+`), all three xAI Grok targets have **full user-scope (`--global`) and project-scope primitive support**:

| APM target | Runtime environment | How it loads these skills | Important APM deployment note |
|---|---|---|---|
| **`grok-bot`** | Persistent multi-agent virtual teammate and chat bot platform | Reads root `AGENTS.md` and deployed `SKILL.md` folders | **Explicit-only target in APM**: `--target all` excludes `grok-bot` (just like `agy`). Pass `grok-bot` explicitly in `--target`. |
| **`grok-build`** | Terminal/TUI coding and workspace agent (supports Agent Client Protocol / ACP) | Reads root `AGENTS.md` and `.agents/skills/` | Included in standard APM multi-target installs; supports full user-scope primitives. |
| **`grok-cloud`** | Managed cloud agent execution environment | Reads root `AGENTS.md` and `.agents/skills/` | Supports full user-scope primitives and persistent cloud workspace directories. |

### Installation commands for GrokBot (`grok-bot`, `grok-build`, `grok-cloud`)

**Windows (PowerShell):**
```powershell
apm install "$PWD\plugins\strategic-planning" --global --target claude,copilot,codex,agy,grok-bot,grok-build,grok-cloud --parallel-downloads 0
```

**macOS / Linux / Grok Cloud:**
```bash
apm install "$PWD/plugins/strategic-planning" --global --target claude,copilot,codex,agy,grok-bot,grok-build,grok-cloud
```

## 2. Why no special `AGENTS.md` or `SKILL.md` syntax changes are required

Because the skills are already designed for non-developer conversational apps (Claude Cowork, GitHub Copilot App, and GrokBot), the interaction model works natively across chat and virtual-teammate channels:

1. **Short numbered-option turn-taking (`1`–`5`)**:
   - In chat channels (where users prefer quick replies), GrokBot presents the 5-option entry menu or 4-option revisit menu so users can reply with a single digit (`1`, `2`, `3`, `4`, or `5`) or paste raw meeting notes.
2. **Explicit Step 0 output path resolution**:
   - GrokBot asks where to save and read living strategy registers (`C:\Users\<username>\strategic-planning-outputs\<team-name>\strategy\` on Windows or `~/strategic-planning-outputs/<team-name>/strategy/` on Linux / Grok Cloud persistent computers) and records that path in `00-planning-session-status.md`.
3. **Inline `<br>`-wrapped Mermaid diagrams + file exports**:
   - GrokBot renders `<br>`-wrapped Mermaid flowcharts, Gantt roadmaps, and XY capability charts directly in chat while saving `bc-gov-strategy-dashboard.html`, `executive-strategy-deck.md`, and `team-work-tracker.csv` to the configured output folder.
