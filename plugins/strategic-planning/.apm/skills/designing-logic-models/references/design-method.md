# Logic Model Design Method & Pacing

## Contents

- [The 7-Stage Canonical Sequence](#the-7-stage-canonical-sequence)
- [Core Methodological Distinctions](#core-methodological-distinctions)
- [Forward vs Backward Design](#forward-vs-backward-design)
- [Causal Transition Probing Questions](#causal-transition-probing-questions)
- [Three Output Depths](#three-output-depths)
- [Interactive Plain-Language Pacing](#interactive-plain-language-pacing)

---

## The 7-Stage Canonical Sequence

Every logic model in the workbench uses this canonical 7-stage sequence as its standard architecture:

```text
[Need or Problem]
      ↓
   [Inputs] ──(enables)──> [Activities] ──(produces)──> [Outputs]
                                                            ↓ (leads to)
                                                    [Immediate Outcomes]
                                                            ↓ (contributes to)
                                                  [Intermediate Outcomes]
                                                            ↓ (contributes to)
                                                    [Long-term Outcomes]
```

1. **Need or Problem**:
   The documented public-sector condition, operational bottleneck, policy gap, or user problem that justifies public intervention.
2. **Inputs**:
   What we invest: capital and operational funding, staff full-time equivalents (FTEs), specialist vendor expertise, technology platforms, data assets, and statutory authorities.
3. **Activities**:
   What we do: business process redesign, software engineering, service blueprinting, policy drafting, stakeholder consultations, and staff training delivery.
4. **Outputs**:
   What we produce: directly delivered products, completed digital services, published guidelines, trained individuals, modernized workflow releases, and documented decisions. Outputs are substantially within the team's control.
5. **Immediate Outcomes**:
   What changes first: early changes in user access, frontline staff awareness, acquired technical capabilities, user adoption, initial confidence, and uptake.
6. **Intermediate Outcomes**:
   What changes next: sustained changes in organizational behaviour, operational throughput, reduced cycle times, improved client satisfaction, lower administrative burden, and evidence-informed decisions.
7. **Long-term Outcomes (Impact)**:
   Ultimate public value: enduring societal, economic, justice-sector, or public-trust improvements (e.g., more accessible justice, reduced legal backlogs, equitable public service delivery).

---

## Core Methodological Distinctions

The agent must enforce these foundational distinctions during coaching:

| Dimension | Activities & Outputs | Immediate & Intermediate Outcomes | Long-term Outcomes (Impact) |
|---|---|---|---|
| **Nature** | Action performed & deliverable produced | Behavioral, operational, or capability change | Enduring state or societal condition |
| **Team control** | **Direct control** (we control our actions and releases) | **Direct influence** (requires user uptake and response) | **Contribution** (influenced alongside external factors) |
| **Verification** | Project delivery records (was it built?) | Adoption and performance metrics (was it used?) | Macro evaluation data and sector indicators |
| **Causal status** | Enabler / Means | Intermediate effect / Stepping stone | Ultimate objective / End |

### Critical Invariants
- **Completion of an output does not prove an outcome occurred**: Releasing a court portal does not mean users found it accessible or that registry backlogs shrank.
- **A metric is not an outcome**: "Number of downloads" is an output measure; "Reduction in unrepresented litigant filing errors" is an outcome.
- **An aspiration without an affected entity is invalid**: "Become better" is rejected; "Court registry staff resolve probate filings in 3 business days instead of 14" is validated.

---

## Forward vs Backward Design

### Backward Design (Recommended for Strategy & Program Formulation)
Always recommend backward design when developing a new strategy, initiative, or business case:
1. Identify the intended **Long-Term Outcome** (What public or operational impact must change?).
2. Work backward to prerequisite **Intermediate Outcomes** (What organizational or user behaviors must change first?).
3. Identify required **Immediate Outcomes** (What early capability or access shift is necessary?).
4. Determine required **Outputs** (What specific deliverables will spark those early shifts?).
5. Determine required **Activities** (What work must the team perform?).
6. Specify required **Inputs** (What resources, funding, and authorities are needed?).

### Forward Design (Recommended for Delivery Audits & Existing Projects)
Use forward design when auditing an active project, team backlog, or committed initiative (`WORK-X`):
1. Catalog current **Inputs** and **Activities**.
2. Audit the actual **Outputs** being delivered.
3. Trace the hypothesized **Immediate Outcomes** (Who is using these outputs?).
4. Test whether they plausibly link to **Intermediate** and **Long-term Outcomes**.
5. Expose missing links, activity traps, and dead-end outputs.

---

## Causal Transition Probing Questions

For every arrow in the model, ask or verify:
1. **Plausibility**: *Why should this output directly cause this immediate outcome? What behavioral mechanism makes people use it?*
2. **Assumptions**: *What conditions must remain true in the operating environment for this link to hold?*
3. **External factors**: *What competing priorities, external policies, or judicial independence constraints could block this step?*
4. **Beneficiaries & actors**: *Who specifically must act or change their behavior at this stage?*
5. **Control boundary**: *Is the team claiming direct attribution, or acknowledging contribution alongside other justice partners?*
6. **Timeframe**: *How long after output deployment should this change become observable?*

---

## Three Output Depths

1. **Simple Logic Model**:
   Core 7-stage chain with clear, concise bullets and a BC Gov-styled Mermaid diagram. Best for quick team alignment or Strategy on a Page integration.
2. **Extended Logic Model**:
   Adds explicit problem statement, target beneficiaries, critical assumptions, external risks, and operational dependencies per stage.
3. **Measurement-Ready Model (Logframe Ready)**:
   Full extended model plus quantitative/qualitative indicators, baselines, target thresholds, data verification sources, collection frequency, and named accountabilities.

---

## Interactive Plain-Language Pacing

In alignment with BC Government and workbench standards:
- Ask **1–2 plain-language questions per turn**.
- Never overwhelm non-technical users with academic jargon.
- Offer structured choice menus:
  ```text
  1. Forward design (start from your existing project work and trace its outcomes)
  2. Backward design (Recommended: start from the public outcome you want to achieve)
  ```
- Always present a **Recap Confirmation Gate** before persisting models to `strategy/`.
