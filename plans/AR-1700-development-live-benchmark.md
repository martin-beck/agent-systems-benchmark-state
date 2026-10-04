# AR-1700 — Development live OpenRouter benchmark execution

Wire the existing agent/provider/model configuration into the production-shaped
benchmark runner for a development live route. Support OpenCode and OpenDesk
ChatCompletions through OpenRouter, selected-agent and all-selected-agent
fan-out, bounded request timeout/retry policy, progress, cancellation, and
typed provider/model/auth/network errors. Preserve `--local-mock` as an
explicit offline route and add tests that prove live mode reaches a replaceable
HTTP boundary while mock mode never does. Include human-readable output and
stable `--json` results with provider, model, request count, failure, and cost
metadata (never key material).
