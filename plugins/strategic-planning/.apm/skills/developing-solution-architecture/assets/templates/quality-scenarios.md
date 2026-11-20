# Quality Attribute Scenarios & Non-Functional Targets

> **Purpose:** Make architectural principles testable. Each scenario pairs a concrete stimulus with a measurable response target (inspired by arc42 Chapter 10).

## Quality goals (prioritized)

| Priority | Quality attribute | Why it matters for this initiative | Linked ADRs / WPs |
|---|---|---|---|
| 1 | Security & trust-boundary isolation | Prevent prompt-level or cross-zone privilege escalation | `ADR-001` |
| 2 | Privacy & data residency | Keep citizen PII within approved Canadian boundaries | `WP-01` |
| 3 | Availability & graceful degradation | Preserve human service fallback when AI components degrade | — |

## Testable scenarios

| ID | Attribute | Stimulus | Environment | Expected response | Measure / target |
|---|---|---|---|---|---|
| `QAS-01` | Latency | Citizen submits a routing query | Normal load (Zone 1) | Front door shortlists domain & responds | p95 <= 2.5s |
| `QAS-02` | Security | Untrusted prompt attempts tool invocation | Zone 1 public session | Gateway/identity policy blocks unauthenticated tool call | 0 unauthorized tool calls |
| `QAS-03` | Resilience | Downstream domain agent times out | Peak load | Front door degrades to deterministic link + human handoff | 100% fallback success |
