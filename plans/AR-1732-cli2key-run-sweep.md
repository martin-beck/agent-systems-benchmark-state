# AR-1732 — cli2key run and sweep orchestration

Wire the provider selection into CLI/orchestrator/runtime launch factories for
single runs and bounded sweeps. Reuse one validated supervised sidecar across a
sweep without reusing authority outside it. Bind every attempt to the same
provider/model/runtime generation, preserve normal result/report compatibility,
and make retries explicit and safe. Never silently retry uncertain effects or
fall back to another provider mode.
