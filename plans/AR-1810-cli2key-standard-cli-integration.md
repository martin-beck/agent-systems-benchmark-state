# AR-1810 plan: complete cli2key standard CLI integration

1. Reproduce the ordinary executable failure separately from the injected
   runtime-factory test path and prove the binary enters the default dispatcher
   without cli2key authority.
2. Add the narrow runtime bootstrap at the standard `run`/`sweep` boundary:
   resolve the verified project-local receipt, validate its frozen bridge
   identity, create `Cli2KeyRuntimeAuthority`, and call the existing
   opaque-factory dispatch path. Keep direct non-runtime dispatch forbidden for
   cli2key.
3. Preserve one supervised loopback sidecar for the requested run/bounded sweep
   and provide no fallback to OpenRouter, platform keys, replay, or an
   alternative bridge. Keep OAuth and ephemeral keys out of arguments, output,
   project state, results, and receipts.
4. Add deterministic command-level fake tests for install, status, model
   selection, normal workload execution, bounded sweep, result/report/compare,
   cancellation, timeout, missing login, invalid receipt, substitute binary,
   non-loopback readiness, stale key, and cleanup.
5. Execute a bounded opt-in live development workload using a user-managed
   bridge login. Record only typed redacted evidence; any unavailable login,
   quota, or remote failure is actionable development evidence, not a reason to
   fall back or weaken the test.
6. Obtain independent review, exact-head checks, signed merge, and post-merge
   command-level qualification.
