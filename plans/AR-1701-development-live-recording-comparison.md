# AR-1701 — Development live recording and comparison qualification

Extend the existing selected/all recording and replay routes to the live
OpenRouter runner. Capture normalized request/response metadata, redact
credentials, seal coverage and integrity metadata, and make the cassette
available to the next invocation without manual copying. Qualify strict
network-denied replay plus comparison and analysis for the same workloads,
agents, provider, and model. Include incomplete-coverage and provider-error
diagnostics and keep development authenticity warnings visible but non-blocking.
