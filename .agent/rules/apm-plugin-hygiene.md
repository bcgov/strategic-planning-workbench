---
description: Enforces APM-native plugin architecture, self-contained skills under .apm/skills/, dual manifests, and zero raw symlinks.
globs: ["plugins/**/*", "apm.yml", ".claude-plugin/**/*"]
---

# Rule: APM-Native Plugin & Skill Packaging Hygiene

## 1. The Iron Law
> **All plugin primitives MUST reside inside `.apm/` as self-contained files with zero raw symlinks and zero duplicate root directories.** Every change to plugins or skills MUST pass structural and APM package audits.

## 2. Invariants & Forbidden Actions

1. **Unified `.apm/` Primitive Root**: Deployable skills, agents, hooks, and prompts MUST live exclusively under `plugins/<plugin>/.apm/`. Creating duplicate root `skills/`, `agents/`, `hooks/`, or `commands/` folders outside `.apm/` is PROHIBITED.
2. **Self-Contained Skills**: Every skill in `plugins/<plugin>/.apm/skills/<skill-name>/` MUST contain its own `SKILL.md` (<= 80 lines), `references/`, `assets/templates/`, and `evals/`. Placing shared templates or scripts at the plugin root is PROHIBITED.
3. **Zero Raw Symlinks**: Raw filesystem symlinks and legacy copy manifests (`symlinks.json`) are PROHIBITED across the repository.
4. **Dual Manifest Compliance**:
   - Every plugin root MUST maintain `apm.yml` and `.claude-plugin/plugin.json`.
   - `.claude-plugin/plugin.json` MUST define `author` as an object (`{"name": "..."}`) and MUST NEVER declare `skills`, `agents`, `hooks`, or `commands` arrays.
5. **Gerund Naming & Third-Person Descriptions**: Skill folder names and frontmatter `name` fields MUST match in kebab-case gerund form, with third-person descriptions stating what the skill does and when to use it.

## 3. Evaluation Checklist

- Do all skills reside under `plugins/<plugin>/.apm/skills/<skill-name>/` with `SKILL.md` <= 80 lines?
- Does every skill include `references/acceptance-criteria.md`, `evals/evals.json`, and `evals/task-success.json`?
- Does `.claude-plugin/plugin.json` use an `author` object and omit auto-discovered component arrays?
- Do `audit_plugin_structure.py`, `audit_skill.py`, and `validate_apm_package.py` pass with zero errors?
