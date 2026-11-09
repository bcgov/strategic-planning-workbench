---
name: designing-logic-models
description: "Guides users interactively to design, review, and document program logic models, results chains, outcome chains, theories of change, and results frameworks. Use when mapping causal relationships from inputs and activities to outputs and successive outcomes for a project or objective, validating causal assumptions, or generating BC Gov-styled Mermaid diagrams and logframe matrices. Not for drafting high-level strategic vision (use defining-strategic-vision) or scheduling roadmaps (use sequencing-roadmaps-and-measures)."
---

# Designing logic models

Guides teams through an interactive conversation to construct, stress-test, and document robust causal results chains—from resources and activities through controllable outputs to progressive immediate, intermediate, and long-term public outcomes.

## Contents

- [Constraints](#constraints)
- [Quick start](#quick-start)
- [Workflow](#workflow)
- [Verification](#verification)
- [References](#references)

## Constraints

1. **Strict causal purity**: Rigorously separate activities (work done), outputs (things produced), and outcomes (behavioral or operational changes resulting from use).
2. **Intermediate stepping**: Reject unmediated leaps from early outputs to macro impacts without immediate and intermediate stepping stones.
3. **Attribution vs. contribution**: Direct control applies only to outputs; long-term outcomes must be framed as contribution alongside external influences.
4. **Interactive plain-language pacing**: Ask 1–2 plain-language questions per turn with numbered option menus. Always run a recap confirmation gate before saving.
5. **B.C. Government style**: Use sentence case, plain language, zero emoji, zero exclamation marks, and official BC Gov token hex colors in Mermaid diagrams.

## Quick start

1. Review [terminology.md](references/terminology.md) to choose the right framework (Logic Model, Theory of Change, Results Chain, or Logframe).
2. Select direction: **Backward design** (recommended for strategy/objectives) or **Forward design** (for auditing existing project work).
3. Walk the user interactively through the 7 canonical stages in [design-method.md](references/design-method.md).
4. Run the 15-rule anti-pattern check in [validation-rules.md](references/validation-rules.md).
5. Generate the Mermaid flowchart (via `scripts/generate_mermaid.py`) and matrix using [output-templates.md](references/output-templates.md).

## Workflow

1. **Scope & Direction**: Identify the target program, objective (`OBJ-X`), or project (`WORK-X`), affected beneficiaries, and whether to use backward or forward design.
2. **Canonical Results Mapping**: Build the 7-stage chain: Need/Problem ──> Inputs ──> Activities ──> Outputs ──> Immediate Outcomes ──> Intermediate Outcomes ──> Long-term Outcomes.
3. **Causal Stress-Testing**: Probe assumptions, external risks, user adoption mechanics, and time horizons for every transition arrow.
4. **Validation Gate**: Audit the model against the 15 anti-patterns in [validation-rules.md](references/validation-rules.md), correcting activities-as-outcomes and causal leaps.
5. **Recap Confirmation Gate**: Present a concise draft recap to the user for confirmation before output generation.
6. **Artifact Generation**: Produce the copy-paste-ready B.C. Gov Mermaid diagram, tabular matrix, or full [logic-model-template.md](assets/templates/logic-model-template.md).

## Verification

Audit outputs against [acceptance-criteria.md](references/acceptance-criteria.md):
- Activities, outputs, and outcomes are strictly separated with zero category errors.
- Mermaid diagrams use source lines under 200 characters and valid BC Gov styling.
- All 15 validation rules in [validation-rules.md](references/validation-rules.md) pass.

## References

- Terminology & frameworks: [terminology.md](references/terminology.md)
- Design method & pacing: [design-method.md](references/design-method.md)
- Anti-pattern validation: [validation-rules.md](references/validation-rules.md)
- Templates & syntax: [output-templates.md](references/output-templates.md)
- Worked examples index: [worked-examples.md](references/worked-examples.md)
- Domain examples: [Court Evidence](references/examples/court-evidence-policy-validation.md) • [Canonical LR](references/examples/canonical-results-chain.md) • [Digital E-Filing](references/examples/court-registry-digital-efiling.md) • [Workforce Academy](references/examples/workforce-training-academy.md) • [Justice AI](references/examples/justice-ai-docket-summarizer.md)
- Quality gate: [acceptance-criteria.md](references/acceptance-criteria.md)
