# AR-1699 — Development live-provider credential bridge

Implement the narrow bridge from the persisted provider/model selection to an
OpenRouter live attempt in development mode. Resolve `OPENROUTER_API_KEY` only
when a live run is explicitly requested, redact it from diagnostics, validate
the selected model against the connected provider catalog, and expose a
warning-only setup/connectivity result when the key is absent. Do not wait for
runtime attestation, production key storage, signatures, or a deployment
authority. Add unit and integration tests proving no secret is persisted and
that mock mode remains deterministic.
