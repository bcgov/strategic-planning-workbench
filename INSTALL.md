# Repository installation and lifecycle — central authority

This document defines how to install, configure, update, and manage plugins and skills in the **Strategic Planning Workbench** (`strategic-planning-workbench`), as well as how to pair it with the **B.C. Government Design System** (`bc-gov-design-system`) and governance extensions from **Agent Plugins & Skills** (`agent-plugins-skills`).

All packages are managed with [APM](https://github.com/microsoft/apm) (Agent Package Manager). APM copies skills from `plugins/strategic-planning/.apm/skills/` into your agent harness folders (`~/.claude/skills/`, `~/.agents/skills/`, `~/.gemini/antigravity-cli/skills/`), keeps a manifest and lockfile, and handles updates and removal on Windows, macOS, and Linux with zero symlinks and no build step.

## Dependencies and install order

The workbench is a **level 2** package that pairs with two level 1 packages:

| Level | Package | Repository | Role |
|---|---|---|---|
| 1 | `bc-gov-design-system` | [`richfrem/bc-gov-design-system`](https://github.com/richfrem/bc-gov-design-system) | Official B.C. Government Design System tokens, BC Sans fonts, HTML components, and PowerPoint (`pptx`) generator |
| 1 | `agent-plugins-skills` | [`richfrem/agent-plugins-skills`](https://github.com/richfrem/agent-plugins-skills) | Authoring, packaging, memory, and governance skills |
| 2 | `strategic-planning` (this repo) | [`bcgov/strategic-planning-workbench`](https://github.com/bcgov/strategic-planning-workbench) | 11 interactive strategic planning, TOGAF ADM cycle orchestration, capability/value-stream mapping, idea/work/team inventory, and visual rendering skills |

`plugins/strategic-planning/apm.yml` declares no transitive dependencies, so installing that plugin alone never pulls unexpected packages. Check what is already installed globally first:

```bash
apm deps list --global
```

---

## Option 1: APM package management (recommended)

### 1. Install the APM CLI

Use APM 0.35.0 or newer; the `agy` (Antigravity) target requires it.

**Windows (PowerShell):**
```powershell
irm https://aka.ms/apm-windows | iex
```

**macOS / Linux:**
```bash
curl -sSL https://aka.ms/apm-unix | sh -s -- @v0.35.0
```

Verify the installation:
```bash
apm --version
```

---

### 2. Install from GitHub or get a local clone

From a consuming project or workstation, you can install directly from GitHub or from a local clone:

```bash
# Install from GitHub (global)
apm install bcgov/strategic-planning-workbench/plugins/strategic-planning --global --target claude,copilot,codex,agy

# Pin to a specific release tag or commit SHA for reproducibility
apm install "bcgov/strategic-planning-workbench/plugins/strategic-planning#<tag-or-commit>" --global --target claude,copilot,codex,agy
```

#### Clone-based alternative (recommended on Windows to avoid 260-character cache path limits)

```bash
git clone https://github.com/bcgov/strategic-planning-workbench.git
cd strategic-planning-workbench
git checkout <tag-or-commit>      # optional: pin a release
```

---

### 3. Install the `strategic-planning` plugin

#### A. Global install (recommended for workstations, Claude Cowork, GitHub Copilot, and GrokBot)

> **Note for GrokBot (`grok-bot`, `grok-build`, `grok-cloud`) and Antigravity (`agy`)**: In APM `0.35.0+`, `--target all` explicitly excludes `grok-bot` and `agy`. Include `grok-bot,grok-build,grok-cloud` explicitly in `--target` when deploying to GrokBot environments (`apm install "$PWD\plugins\strategic-planning" --global --target claude,copilot,codex,agy,grok-bot,grok-build,grok-cloud --parallel-downloads 0`).

Make all 5 strategic planning skills available across every workspace. Global installs require the **absolute path** to the plugin folder; a relative path such as `./plugins/strategic-planning` is rejected by APM.

**Windows (PowerShell):**
```powershell
apm install "$PWD\plugins\strategic-planning" --global --target claude,copilot,codex,agy --parallel-downloads 0
```

**macOS / Linux:**
```bash
apm install "$PWD/plugins/strategic-planning" --global --target claude,copilot,codex,agy
```

`--parallel-downloads 0` avoids an "Access denied" error on Windows when APM renames its staging folder. If a skill folder already exists that APM did not create, APM skips it; add `--force` to overwrite.

The global installation writes to your user-level harness directories:
```text
APM state & cache:           ~/.apm/                              (Windows: %USERPROFILE%\.apm\)
Claude Code / Cowork skills: ~/.claude/skills/
Copilot & Codex skills:      ~/.agents/skills/                    (shared)
Antigravity (agy) skills:    ~/.gemini/antigravity-cli/skills/
```

#### B. Project-local install (for dedicated branch/team strategy repositories)

To install the plugin into a single strategy repository (for example, a dedicated Court Services Branch planning repo), run from that repository's root:

```bash
cd <path-to-strategy-repo>
apm install <path-to-clone>/plugins/strategic-planning --target claude,copilot,codex,agy
```

This records the dependency in the project's `apm.yml`, writes `apm.lock.yaml`, and deploys skills to `.claude/skills/` and `.agents/skills/`. Commit `apm.yml` and `apm.lock.yaml` together. In CI, reproduce the exact install with `apm install --frozen`.

#### Windows vs. macOS / Linux quick reference

| Setting | Windows | macOS / Linux |
| :--- | :--- | :--- |
| Install APM | `irm https://aka.ms/apm-windows \| iex` | `curl -sSL https://aka.ms/apm-unix \| sh -s -- @v0.35.0` |
| Plugin path | Absolute: `"$PWD\plugins\strategic-planning"` | Absolute: `"$PWD/plugins/strategic-planning"` |
| Extra flag | `--parallel-downloads 0` | not needed |
| State folder | `%USERPROFILE%\.apm\` | `~/.apm/` |

---

### 4. Install only specific skills (optional)

All 5 skills in `strategic-planning` are designed to work together, but you can install a subset using repeatable `--skill` flags:

```powershell
apm install "$PWD\plugins\strategic-planning" --global --target claude,copilot,codex,agy --parallel-downloads 0 --skill developing-and-managing-strategy --skill triaging-new-items
```

Available skills in `plugins/strategic-planning`:
1. `developing-and-managing-strategy` *(main skill: strategy interview, registers, ideas, work, risks, scoring, roadmap)*
2. `triaging-new-items` *(classify and route new or unclear material)*
3. `managing-team-skills-and-allocation` *(team skills, capacity evidence)*
4. `designing-logic-models`
5. `rendering-strategic-visuals-and-decks`

---

### 5. Install companion level 1 packages (`bc-gov-design-system`)

For full B.C. Government Design System font assets (`BC Sans`), CSS tokens, and automated PowerPoint (`.pptx`) deck generation alongside `rendering-strategic-visuals-and-decks`, ensure `bc-gov-design-system` is installed globally:

```powershell
apm install "<path-to-clone>\bc-gov-design-system" --global --target claude,copilot,codex,agy --parallel-downloads 0
```

---

### 6. Updating, backing up, and uninstalling

```powershell
# List all globally installed APM packages
apm deps list --global

# Preview an install without writing files
apm install "$PWD\plugins\strategic-planning" --target claude --dry-run

# Update from local clone after pulling changes
git pull
apm install "$PWD\plugins\strategic-planning" --global --target claude,copilot,codex,agy --parallel-downloads 0

# Uninstall globally
apm uninstall "$PWD\plugins\strategic-planning" --global
```

If `packaging-with-apm` is installed, you can also back up and roll back your global `~/.apm/` state before making changes:

```powershell
python "$HOME\.gemini\antigravity-cli\skills\packaging-with-apm\scripts\apm_consumer.py" backup
python "$HOME\.gemini\antigravity-cli\skills\packaging-with-apm\scripts\apm_consumer.py" list-backups
python "$HOME\.gemini\antigravity-cli\skills\packaging-with-apm\scripts\apm_consumer.py" rollback
```

---

### 7. Troubleshooting on Windows

**`Failed to resolve transitive dep ... [WinError 3] The system cannot find the path specified`**
- **Cause**: Installing from a remote GitHub reference places files under `%LOCALAPPDATA%\apm\cache\git\checkouts_v1\...`, which can exceed Windows' 260-character path limit when combined with deep skill paths.
- **Fix**: Clone the repository to a local folder (such as `C:\src\strategic-planning-workbench` or `C:\Users\<user>\source\repos\strategic-planning-workbench`) and install using the absolute path in section 3A.

**`Access denied` on `.apm-resolution-staging`**
- Always pass `--parallel-downloads 0` on Windows. If a previous install was interrupted, remove `%USERPROFILE%\.apm\apm_modules\.apm-resolution-staging` and `%USERPROFILE%\.apm\.apm-lifecycle.lock`, then retry.

**`N files skipped -- local files exist, not managed by APM`**
- A skill folder already exists that APM did not create. Add `--force` to overwrite it.

---

## Option 2: Native agent plugin marketplace (Claude Code / Copilot CLI)

If you are using **Claude Code** or **GitHub Copilot CLI**, you can register this repository's `.claude-plugin/marketplace.json` catalog directly:

### Claude Code syntax
```text
/plugin marketplace add bcgov/strategic-planning-workbench
/plugin install strategic-planning@strategic-planning-workbench
```

### Copilot CLI syntax
```bash
copilot plugin marketplace add bcgov/strategic-planning-workbench
copilot plugin install strategic-planning@bcgov-strategic-planning-workbench
```

---

## Local development and compliance auditing (contributors)

Before committing changes to skills, rules, or manifests, run the verification suite from the repository root:

```powershell
$env:PYTHONIOENCODING = "utf-8"

# 1. Audit root AGENTS.md, CLAUDE.md, and policy rules
python "$HOME\.gemini\antigravity-cli\skills\authoring-instructions\scripts\audit_agents_md.py" AGENTS.md --strict
python "$HOME\.gemini\antigravity-cli\skills\authoring-instructions\scripts\audit_agents_md.py" CLAUDE.md --strict
python "$HOME\.gemini\antigravity-cli\skills\authoring-instructions\scripts\audit_rule.py" . --all --strict

# 2. Audit plugin structure and Open Standard compliance
python "$HOME\.gemini\antigravity-cli\skills\authoring-plugins\scripts\audit_plugin_structure.py" plugins\strategic-planning
python "$HOME\.gemini\antigravity-cli\skills\authoring-plugins\scripts\audit.py" --path plugins\strategic-planning

# 3. Audit all 5 skills (source and installed modes)
python "$HOME\.gemini\antigravity-cli\skills\authoring-skills\scripts\audit_skill.py" plugins\strategic-planning --all --mode source
python "$HOME\.gemini\antigravity-cli\skills\authoring-skills\scripts\audit_skill.py" plugins\strategic-planning --all --mode installed

# 3b. Run the scoring script regression checks
python plugins\strategic-planning\.apm\skills\developing-and-managing-strategy\scripts\test_investment_scripts.py

# 4. Validate APM manifests and marketplace catalog
python "$HOME\.gemini\antigravity-cli\skills\packaging-with-apm\scripts\validate_apm_package.py" --path .
python "$HOME\.gemini\antigravity-cli\skills\packaging-with-apm\scripts\validate_apm_package.py" --path plugins\strategic-planning
python "$HOME\.gemini\antigravity-cli\skills\packaging-with-apm\scripts\audit_marketplace_sources.py" .
```
