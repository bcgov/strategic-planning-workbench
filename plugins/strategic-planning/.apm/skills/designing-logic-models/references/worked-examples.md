# Worked Examples & Reference Logic Models

This directory provides public-sector reference logic models and results chains tailored for the B.C. Government and Court Services Branch context. Each full model is maintained in a dedicated file in the [`examples/`](examples/) subfolder.

---

## Example Catalog

| Model | Domain & Scope | Architecture & Layout | Key Highlights | Link |
|---|---|---|---|---|
| **Program Need-Driven Court Evidence** | Court Services Branch (CSB) Digital Transformation | Top-to-Bottom (`flowchart TB`) with `classDef` tokens | Starts from explicit Program Need anchor; captures validation tokens, APIs, and digital exhibit handling. | [court-evidence-policy-validation.md](examples/court-evidence-policy-validation.md) |
| **Canonical Baseline Results Chain** | Digital Service Transformation | Left-to-Right (`flowchart LR`) with direct `style` | Standard 6-stage public-sector results pathway connecting investments to citizen outcomes. | [canonical-results-chain.md](examples/canonical-results-chain.md) |
| **Court Registry Digital E-Filing** | Provincial Court Registry Modernization (`WORK-012`) | Top-to-Bottom (`flowchart TD`) | Converts manual counter filing into WCAG 2.1 AA digital self-service with 24-hour turnaround. | [court-registry-digital-efiling.md](examples/court-registry-digital-efiling.md) |
| **Workforce Cloud Skills Academy** | In-House Engineering & DevOps (`WORK-024`) | Top-to-Bottom (`flowchart TD`) | Connects hands-on CI/CD training to slashed deployment lead times and lower vendor dependency. | [workforce-training-academy.md](examples/workforce-training-academy.md) |
| **Justice AI Docket Summarizer** | Judicial & Registry AI Adoption (`WORK-031`) | Top-to-Bottom (`flowchart TD`) | Embeds human-in-the-loop validation and sovereign AI privacy controls into docket drafting. | [justice-ai-docket-summarizer.md](examples/justice-ai-docket-summarizer.md) |

---

## Sizing & Rendering Guidance

All example diagrams use standard B.C. Government Design System tokens and include the Mermaid configuration directive:

```text
%%{init: {"flowchart": {"wrappingWidth": 460, "minNodeWidth": 360}} }%%
```

This prevents horizontal text truncation in GitHub and documentation viewers by setting minimum node widths and allowing up to 460px line wrapping. Generate diagrams automatically using `scripts/generate_mermaid.py`.
