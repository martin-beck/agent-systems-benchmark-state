# AR-1799 plan: cli2key runtime authority composition seam

1. Define a runtime-only receipt-to-sidecar bootstrap API with exact digest,
   entrypoint, platform, and development catalog checks.
2. Bind the sidecar lifecycle and invocation credential to an opaque
   `LiveProviderAttempt`; never expose key bytes, paths, or OAuth material.
3. Add positive fake coverage and hostile tests for receipt substitution,
   stale digest, non-loopback readiness, malformed readiness, cancellation,
   timeout, crash, teardown, and concurrent sweep lifetime.
4. Integrate the seam into direct CLI live cli2key run/sweep dispatch while
   retaining typed no-fallback failures and redacted evidence.
5. Run independent review, exact-head CI, protected merge, and post-merge
   acceptance before resuming AR-1797.
