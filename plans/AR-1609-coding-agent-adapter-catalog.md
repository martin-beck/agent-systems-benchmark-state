# AR-1609 — Coding-agent adapter catalog and compatibility

Extend the ASB setup capability catalog with explicit coding-agent adapter
records for `opencode`, `opendesk`, and future agents. Each record declares
supported providers, model-selection constraints, authentication reference
requirements, availability diagnostics, and a stable identifier used by the
wizard and benchmark runner. The catalog must permit adding an adapter without
rewriting persisted configuration and must reject stale or incompatible
agent/provider/model tuples with an actionable human-readable explanation.

Dependencies: AR-1607. Downstream: AR-1608 and AR-1603.

Development mode is functional and warning-only for absent credentials,
signatures, and key-management services; it must never block catalog display,
fixture setup, or offline replay. Production authorization remains fail-closed.

Required evidence: versioned adapter/catalog schemas, opencode and opendesk
fixtures, supported/unsupported tuple tests, migration and unknown-adapter
negatives, redacted human-readable and `--json` output, exact-head hosted CI,
independent review, and a digest-bound receipt.
