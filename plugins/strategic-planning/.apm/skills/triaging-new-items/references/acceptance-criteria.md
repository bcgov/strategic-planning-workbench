# Acceptance criteria: `triaging-new-items`

See [classification acceptance criteria](classification/acceptance-criteria.md) for the full triage gate:

1. **Interactive intake**: Presents a concise summary table classifying each item by nature and commitment state before routing.
2. **Three-inventory separation**: Unapproved ideas or uncapacitated items are routed to `07-idea-inventory.md` or `Open follow-ups`, never directly into committed `08-work-inventory.md`.
3. **Stable IDs & non-destructive routing**: Preserves existing record IDs and logs open follow-ups in `00-planning-session-status.md`.
