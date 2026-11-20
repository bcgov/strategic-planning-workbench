# Runtime & Trust-Boundary Scenarios

> **Purpose:** Document key end-to-end runtime flows across trust boundaries, identity hops, and failure fallbacks (inspired by arc42 Chapter 6).

## Scenario 1: Public citizen intent routing (Zone 1)

- **Trigger:** Citizen states a goal in plain language without knowing the responsible ministry.
- **Trust boundary:** Public unauthenticated (`Zone 1`); zero PII persisted.
- **Step-by-step flow:**
  1. Web/channel ingress sends sanitized query to Front Door orchestrator.
  2. Orchestrator queries Level-1 capability index (compact manifests only).
  3. Orchestrator delegates via A2A or returns deterministic guidance + warm human escalation link.
- **Failure / fallback:** If confidence < threshold or downstream unavailable, present direct ministry service link and human contact channel.
- **Linked contracts & diagrams:** `contracts/`, `diagrams/`

## Scenario 2: Authenticated citizen / OBO delegation (Zone 2)

- **Trigger:** Citizen authenticates (e.g., BCSC OIDC) to complete a stateful transaction.
- **Trust boundary:** Authenticated citizen (`Zone 2`); scoped OBO token via Entra Agent ID + APIM gateway.
- **Step-by-step flow:**
  1. ...
- **Failure / fallback:** ...
