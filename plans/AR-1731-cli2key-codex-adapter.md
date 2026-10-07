# AR-1731 — Codex adapter integration for cli2key

Parameterize the Codex adapter's provider credential and base URL projection,
consume the opaque runtime handle at the final child boundary, and preserve
secret redaction. Add exact projection, unsupported-model, stale-generation,
wrong-key, 401/429, malformed-response, timeout, and sidecar-crash tests. Keep
the adapter single-layer: Codex is the benchmarked agent; app-server is not
wrapped as a provider for another agent.
