# AR-1797 plan: cli2key live runtime wiring

1. Reproduce the current direct-CLI rejection and trace the missing boundary
   between provider selection and `Cli2KeySidecar` ownership.
2. Consume only the AR-1779 verified project-local cli2key receipt; validate the
   exact executable, digest, bounded arguments, and development-only catalog
   identity before starting the sidecar.
3. Have the runtime issue one loopback-only sidecar launch per run or bounded
   sweep, retain its lifecycle ownership through every attempt, and pass only
   the ephemeral endpoint/key/model projection to the Codex Responses adapter.
4. Make success, cancellation, timeout, crash, stale-key, malformed readiness,
   wrong model, unavailable login, and teardown paths fail distinctly with no
   provider fallback or credential persistence.
5. Add deterministic public CLI fake-sidecar install/select/run/sweep/report/
   compare coverage, then perform one opt-in user-authorized live development
   benchmark. Preserve only redacted, bounded receipt evidence.
6. Obtain independent review, exact-head checks, protected merge, and exact-main
   post-merge qualification.
