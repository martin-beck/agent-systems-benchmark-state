# AR-1607 — OpenRouter provider and model setup

Extend the development setup contract and provider catalog with an explicit
OpenRouter profile. The wizard must enumerate supported agents and models for
the selected provider, accept an API-key reference (including
`OPENROUTER_API_KEY`), validate connectivity when requested, and persist a
redacted selection without writing the secret into state, logs, or receipts.

Development mode uses generated local identity material and warning-only
authentication/signature/key-service absence; it must never block a functional
prototype. Stable/production authorization remains fail-closed.

Dependencies: AR-1595, AR-1601. Downstream: AR-1603 and paired TUI AR-1605.

Required evidence: versioned catalog/config schemas, OpenRouter model fixtures,
selection and unavailable-model negatives, redaction tests, human-readable
default output with opt-in `--json`, exact-head hosted CI, independent review,
and a digest-bound acceptance receipt.
