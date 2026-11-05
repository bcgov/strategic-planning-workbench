# Governance & Packaging Policy

## Overview

`strategic-planning-workbench` is authored as an APM-native plugin repository adhering to the Agent Skills Open Standard and Agent Package Manager (APM) specifications.

## Architectural Invariants

1. **Pure `.apm/` Primitive Layout**: All skills reside inside `plugins/<plugin-name>/.apm/skills/<skill-name>/`. Duplicate root `skills/`, `agents/`, or `hooks/` folders outside `.apm/` are prohibited.
2. **Self-Contained Skills**: Every skill owns its `references/`, `assets/templates/`, and `evals/` directly inside its skill directory with zero raw filesystem symlinks.
3. **Evidence & Commitment Guardrails**:
   - Strategic planning skills never fabricate organizational facts, baselines, or leadership mandates. Missing facts are logged in an Assumptions & Evidence Register.
   - Unapproved opportunities remain in the **Idea Inventory** until explicit sponsorship, ownership, and capacity commitment promote them into the **Work Inventory**.
4. **Dual Manifests**: Every plugin maintains `apm.yml` and `.claude-plugin/plugin.json` (with an `author` object and auto-discovered components).
5. **Protected `main` Branch & Documentation Synchronization**: `main` is branch-protected on `bcgov/strategic-planning-workbench`. All contributions must be developed on a feature branch (`feat/*`, `fix/*`, `docs/*`), pass the full compliance audit suite, update `AGENTS.md`, `architecture.md`, and `README.md` when skills or registers change, and merge via Pull Request.
