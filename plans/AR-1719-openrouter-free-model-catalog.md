# AR-1719 — OpenRouter free-model catalog and wizard selection

Enumerate the current OpenRouter provider catalog without hard-coding one free
model. Include explicit `:free` and free-router eligible models, preserve
dynamic metadata/capabilities/context/modalities/availability, normalize into
provider-catalog/provider-plan, and expose all eligible models through wizard
selection.

Add deterministic fixtures for explicit free models, free-router eligibility,
dynamic metadata changes, stale/unknown/unavailable/model mismatch,
credential-free discovery, and bounded live smoke. Authentication and quota
may warn in development; no production security expansion is required.

Acceptance covers complete eligible enumeration, metadata digest/generation
handling, typed diagnostics, human/JSON contracts, bounded live smoke without
fallback or secret/raw-payload persistence, and hosted quality checks.

Collision rationale: this is the collision-safe successor to the previously
numbered AR-1718 free-model catalog scope. AR-1718 is reserved for the
portable fault-matrix repair.
