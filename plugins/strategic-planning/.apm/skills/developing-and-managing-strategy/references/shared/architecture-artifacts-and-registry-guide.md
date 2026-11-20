# Optional Architecture Artifacts & Technology Registry Guide

TOGAF BDAT architecture artifacts and technology registries are an **optional execution path**, not required for general organizational or branch strategic planning.

## 1. Dynamic path selection (ask before pulling in architecture skills)
On first run—or when the engagement scope is unclear—ask which path applies so irrelevant skills are not loaded:
1. **General strategic planning (Recommended for business/operations teams):** Uses registers `00`–`11`, `triaging-new-items`, `managing-team-skills-and-allocation`, `designing-logic-models`, and `rendering-strategic-visuals-and-decks`. Skip TOGAF BDAT docs and `managing-architecture-registry`.
2. **Architectural planning & technical strategy:** Pairs registers `00`–`11` with TOGAF BDAT domain docs (`Business`, `Data`, `Application`, `Technology`), ADRs, `work-packages/`, and `managing-architecture-registry`.

## 2. When to use architecture artifacts
- Only on the **Architectural planning** path—**after capabilities (`05`) and objectives (`03`) are clear**, or when onboarding an existing architecture workbench.
- Never invent a technology wish list before establishing drivers (`01`), objectives (`03`), and required capabilities (`05`).

## 2. How strategy registers connect to architecture artifacts

| Strategy Register | Optional Architecture Counterpart | How They Stay Linked |
|---|---|---|
| `03-target-vision-and-objectives.md` (`PRN-X`) | `06-architecture-principles.md` & ADRs | Operating principles inform Architecture Decision Records (`ADR-NNN`). |
| `05-business-capabilities.md` (`VST-X`, `CAP-X`) | TOGAF BDAT domain docs (`Business`, `Data`, `Application`, `Technology`) | Capabilities map to concrete data stores, agent/app runtimes, and landing-zone platforms. |
| `06-constraints-assumptions-risks.md` (`ASM-X`, `GAP-X`) | `contracts-v0.md` & spike questions (`Q1–Q6`) | Platform assumptions become explicit spike gates (`status: spike_verify`) with a named `plan_b`. |
| `07-idea-inventory.md` / `08-work-inventory.md` | `implementation-plan.md` & `work-packages/` (`WP-NN`) | Approved work packages trace to `WORK-X`; unapproved proposals remain `IDEA-X`. |
| Technical components & dependencies | `architecture-registry.json` (+ CSV export) | Managed by the **`managing-architecture-registry`** skill (`TECH-NNN` IDs, TOGAF domain, trust zones, ADRs, work packages, and Private Endpoint IP counts). |

## 3. Model vs. views separation

Keep the **architecture model** (single source of truth) distinct from **views and audience deliverables**:
- **Model:** `architecture/architecture-registry.json`, `contracts/`, `adrs/`, `work-packages/`, `architecture/quality-scenarios.md`, and `architecture/runtime-scenarios.md`.
- **Views & deliverables:** Editable Mermaid/PlantUML sources in `diagrams/` and audience-ready HTML/PPTX/PDF briefings in `deliverables/` (rendered via `rendering-strategic-visuals-and-decks`).

## 4. Handing off to `managing-architecture-registry`
Invoke `managing-architecture-registry` whenever the user wants to initialize, upsert, validate, query, summarize Private Endpoint IP footprints, or export a CSV of technology components (`architecture-registry.json`).
