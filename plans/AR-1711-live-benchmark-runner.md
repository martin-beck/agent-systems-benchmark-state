# AR-1711 — Explicit live benchmark runner

Add the selection-driven ASB runner path for a fresh user who has completed
the wizard. The command must make online mode explicit, allow selected/all
agents and implemented workloads, fan out using the reviewed provider/model
configuration, and produce human-readable output by default with `--json` as
the machine-readable contract. Preserve typed provider, auth, timeout, and
transport failures and forbid implicit mock/cassette fallback.

Acceptance:

1. A disposable exact-head run executes selected and all-agent workload sets
   through the explicit online route when credentials are supplied.
2. Missing key, unavailable model, provider non-2xx, timeout, and transport
   failures are typed, actionable, and nonzero.
3. Local/mock and offline replay remain explicit separate commands/modes.
4. Human-default/`--json`, privacy, fan-out, and hosted checks pass.
