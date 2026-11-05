# Team skills, growth interests and work allocation guide

## 1. Interactive intake menu (for Claude Cowork & GitHub Copilot)

When a user asks to track team members, their skills/interests, or who is working on what, open with this numbered menu:

```text
What would you like to do with your team skills and work tracker today?
1. Map team members, skills, and growth interests — Capture who is on the team, what they do well, and what they want to learn (Recommended)
2. Assign and track active work (WORK-X) — Link projects, experiments, and operational duties to team members and check workload balance
3. Spot bottlenecks and capability coverage gaps — Find single-point-of-failure ("bus factor") risks and match growth interests to capability gaps
4. Export visuals or spreadsheet — Generate Mermaid workload charts, a B.C. Gov HTML summary, or an Excel-ready CSV tracker
```

## 2. Proficiency and interest scale

Capturing both **current proficiency** and **growth interest** turns capability planning into a talent-development tool:

| Level | Code | Definition | Strategic use |
|---|---|---|---|
| **Lead / Subject matter expert** | `L3 - Lead/SME` | Can design, govern, and mentor others in this capability. | Primary capability anchor; pair with a `G - Growth interest` colleague to reduce bus-factor risk. |
| **Practitioner** | `L2 - Practitioner` | Can execute independently in day-to-day work. | Reliable delivery capacity for `WORK-X` initiatives. |
| **Foundational / Familiar** | `L1 - Foundational` | Understands concepts and can assist with guidance. | Backup support capacity. |
| **Growth / Learning interest** | `G - Growth interest` | Wants to learn or gain hands-on experience in this area. | Ideal co-assignment or stretch pairing on upcoming Horizon 1/2 initiatives or candidate experiments. |

## 3. Four team & workload diagnostics to surface automatically

1. **Single-point-of-failure ("Bus factor = 1")**: A critical capability (`CAP-X`) or active initiative (`WORK-X`) where only one person is `L3 - Lead/SME` or `Lead / Owner` with zero `Backup / Reviewer` assigned.
2. **Over-allocated bottleneck**: A team member assigned as `Lead / Owner` across too many concurrent active `WORK-X` initiatives on top of high baseline operational duties.
3. **Growth-to-gap match**: A capability gap (`CAP-X`) where a team member has declared a `G - Growth interest`—an immediate opportunity for mentoring or training rather than external hiring.
4. **Unassigned committed work**: An item in the Work inventory (`WORK-X`) with no named team member or capacity allocated.

## 4. Selecting the right output format

| Need / Audience | Recommended output format |
|---|---|
| **Interactive planning, Git version control, Cowork preview** | **Markdown register + Mermaid diagrams** (`team-skills-and-allocation-register.md`): Includes `flowchart LR` (Person $\rightarrow$ Work $\rightarrow$ Capability) and `xychart-beta` (Operational vs. Project capacity split). |
| **Sorting, filtering, pivot tables, or SharePoint List import** | **Excel-ready CSV (`team-work-tracker.csv`)**: One row per person-to-work assignment with columns for Member ID, Name, Role, Skills, Growth Interests, Work ID, Work Type, Assignment Role, Allocation %, and Status. |
| **Leadership or branch briefing** | Delegate to `rendering-strategic-visuals-and-decks` to embed anonymized capability coverage and capacity balance in the B.C. Gov HTML dashboard or slide deck. |
