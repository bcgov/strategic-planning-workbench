# Acceptance criteria: `managing-architecture-registry`

1. **JSON canonical, CSV derived**: `architecture-registry.json` is the single source of truth; CSV views are generated via `export-csv`.
2. **Valid schema & stable IDs**: `managing_architecture_registry.py validate` exits `0`; every entry uses a stable `TECH-NNN` ID, valid `togaf_domain`, and valid `status`.
3. **Zero secrets or tenant IDs**: No subscription IDs, tenant IDs, IP literals, or credentials are stored in the registry.
