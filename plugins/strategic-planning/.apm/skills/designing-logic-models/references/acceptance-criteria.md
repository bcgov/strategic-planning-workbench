# Acceptance Criteria: `designing-logic-models`

## Mandatory Quality Gates

1. **Causal Distinction Integrity**:
   - **Pass**: Activities (work performed), outputs (deliverables produced), and outcomes (changes resulting from use) are strictly distinguished. Every transition is an explicit, plausible causal hypothesis.
   - **Fail**: Activities or technical deliverables are presented as outcomes (e.g., "Build AI portal" or "Migrate database" listed as an outcome).
2. **Intermediate Stepping & Causal Plausibility**:
   - **Pass**: Results chains link immediate behavioral/access changes to intermediate operational shifts and long-term societal/public impact without unexplained leaps.
   - **Fail**: Immediate activities claim direct, unmediated attribution to long-term macro outcomes (e.g., "Train 10 staff" -> "Reduced public crime rate").
3. **Attribution vs. Contribution Clarity**:
   - **Pass**: Direct control is claimed only for outputs; immediate outcomes acknowledge target user response; long-term outcomes state contribution alongside external factors and assumptions.
   - **Fail**: A single team project claims 100% causal control over branch-wide or ministry-level strategic goals.
4. **Validation against Anti-Patterns**:
   - **Pass**: All 15 validation rules from `references/validation-rules.md` are evaluated before finalizing the logic model.
   - **Fail**: Vague outcomes ("improved services"), missing beneficiaries, circular reasoning, or outputs without users are accepted without flagging.
5. **BC Government Design System & Syntax Hygiene**:
   - **Pass**: Sentence case throughout, plain language, zero emoji, zero exclamation marks, and Mermaid code lines under 200 characters with proper BC Gov color palette styling.
   - **Fail**: CamelCase or Title Case headings, emojis in labels, or long unescaped Mermaid lines that break rendering.
