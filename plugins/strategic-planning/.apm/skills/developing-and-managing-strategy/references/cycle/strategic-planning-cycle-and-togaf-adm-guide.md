# Strategic planning cycle and TOGAF ADM guide

## 1. Interactive front-door entry menu (for Claude Cowork & GitHub Copilot)

After checking whether `strategy/00-planning-session-status.md` and `strategy/01`–`11` exist, welcome the user with a concise status summary and present this 5-option menu:

```text
How would you like to work on your strategy today?
1. Start or refine from leadership direction (Top-down: Context -> Vision -> Capabilities -> Portfolio) (Recommended for new plans)
2. Organize our existing projects, team workload, and ideas first (Bottom-up: capture what is already underway, then align upward)
3. Resume where we left off / run a readiness check (Review current registers, open gaps, and next 15-minute step)
4. Import new meeting notes, leadership updates, or project progress (Update living registers and check ripple impacts)
5. Prepare a roadmap visual, B.C. Gov HTML dashboard, or leadership briefing right now (Fast-track to visuals and decks)
```

## 2. Six-stage workbench lifecycle mapped to TOGAF ADM

The workbench translates the **TOGAF Architecture Development Method (ADM)** into plain-language public-sector strategic planning stages:

| Workbench stage | TOGAF ADM phase | Specialist skill(s) | Living registers updated | Core question answered |
|---|---|---|---|---|
| **Stage 1: Context, mandates and players** | **Preliminary & Phase A** *(Architecture Vision — Context & Stakeholders)* | `developing-and-managing-strategy` (Context mode) | `strategy/01-org-hierarchy-and-context.md`<br>`strategy/02-stakeholders-and-concerns.md`<br>`strategy/06-constraints-assumptions-risks.md` | *What have Province, AG Ministry, CSB, and Division leaders asked for, who are the players, and what is our evidence-based current state?* |
| **Stage 2: Target vision, principles and outcomes** | **Phase A** *(Architecture Vision & Principles)* | `developing-and-managing-strategy` (Vision mode) | `strategy/03-target-vision-and-objectives.md`<br>`strategy/04-expected-benefits-and-value.md` | *Where are we trying to go, what operating principles (`Statement • Rationale • Implications`) guide trade-offs, and what measurable outcomes (`OBJ-X`) and public value (`BEN-X`) will we deliver?* |
| **Stage 3: Value streams and business capabilities** | **Phase B** *(Business Architecture — Value Streams & Capabilities)* | `developing-and-managing-strategy` (Capabilities mode) | `strategy/05-business-capabilities.md` | *Across our end-to-end service value streams (`VST-X`), what must our branch/team be able to do (`CAP-X`), and where are the 5-pillar maturity gaps?* |
| **Stage 4: Idea funnel, committed work and team allocation** | **Phase E** *(Opportunities & Solutions — Work Packages & Capacity)* | `triaging-new-items`<br>`developing-and-managing-strategy` (Ideas, Score and Work modes)<br>`managing-team-skills-and-allocation` | `strategy/07-idea-inventory.md`<br>`strategy/08-work-inventory.md`<br>`strategy/11-team-skills-and-allocation.md` | *What might we do (`IDEA-X`), what are we actually committed to doing (`WORK-X`), and who on our team (`MEM-X`) leads or backs up each commitment?* |
| **Stage 5: Alignment, readiness and plateau roadmap** | **Phase E & Phase F** *(Transformation Readiness & Migration Planning)* | `developing-and-managing-strategy` (Alignment and Measures modes)<br>`developing-and-managing-strategy` (Roadmap mode) | `strategy/09-alignment-traceability-matrix.md`<br>`strategy/06-constraints-assumptions-risks.md`<br>`strategy/10-roadmap-and-success-measures.md` | *How does everything connect, can the organization absorb the change (BTRA), what does each Transition State (Plateau) achieve, and how do we measure success (`MSR-X`)?* |
| **Stage 6: Executive visuals and living governance** | **Phase G, Phase H & Requirements Management** | `rendering-strategic-visuals-and-decks`<br>`developing-and-managing-strategy` (Update mode) | `strategy/00-planning-session-status.md`<br>`strategy/changelog.md` | *How do we communicate this to leadership in B.C. Gov style, and how do we govern evolving priorities and time-boxed dispensations (`DSP-X`)?* |

## 3. Supporting both top-down and bottom-up teams

1. **Top-down path (Option 1)**:
   - Best when a branch, division, or team is kicking off a new strategic cycle or responding to new executive direction from Chris, Jessica, or CSB leadership.
   - Sequence: `developing-and-managing-strategy` (Context, Vision, Capabilities) $\rightarrow$ `triaging-new-items` $\rightarrow$ `developing-and-managing-strategy` (Ideas, Score, Work, Risks) $\rightarrow$ `managing-team-skills-and-allocation` $\rightarrow$ `developing-and-managing-strategy` (Alignment, Measures) $\rightarrow$ `developing-and-managing-strategy` (Roadmap mode) $\rightarrow$ `rendering-strategic-visuals-and-decks`.
2. **Bottom-up / middle-out path (Option 2)**:
   - Best when a team already has 10+ active projects, operational duties, and informal ideas on their plate and feels overwhelmed.
   - Sequence: Run `triaging-new-items` on the mixed list of projects, problems and ideas, capture active commitments in Work mode of `developing-and-managing-strategy` (`08`) and team assignments in `managing-team-skills-and-allocation` (`11`), move unapproved suggestions into Ideas mode (`07`), then use `developing-and-managing-strategy` (`01`–`05`) and the Alignment mode of `developing-and-managing-strategy` (`09`) to test which active projects align upward and which are orphans.
3. **Fast-track briefing path (Option 5)**:
   - If the user needs a presentation or HTML dashboard today but `strategy/03-target-vision-and-objectives.md` or `strategy/08-work-inventory.md` is empty, ask **3 quick intake questions** (1. Top 2–3 leadership priorities/objectives, 2. Top 3–5 active initiatives vs. candidate ideas, classified with `developing-and-managing-strategy`, 3. Target audience), save draft registers, and immediately invoke `rendering-strategic-visuals-and-decks`.
