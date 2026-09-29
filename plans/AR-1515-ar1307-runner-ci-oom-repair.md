# AR-1515 plan: AR-1307 runner CI and bounded-resource repair

1. Start from the protected ASB head and independently reproduce the AR-1307
   formal/hosted CI OOM or admission failure with a disposable generated seed.
   Record only bounded, privacy-safe counters and exit classifications.
2. Audit the canonical TLC runner, tier profile, JVM limits, thread admission,
   timeout, and attestation path. Identify whether the failure is runner
   implementation, CI resource provisioning, or an invalid fixture; do not
   silently increase AR-1307's declared memory/swap contract.
3. Repair the smallest responsible layer so portable development execution is
   deterministic and fail-closed: generated unsigned-development seeds remain
   sufficient for development, while signed/formal qualification keeps its
   independent reviewed-input gate.
4. Add positive and negative tests for resource admission, OOM classification,
   cancellation/cleanup, stale or mismatched attestation, and exact tier
   selection. Keep subprocess argv bounded and discard subprocess output.
5. Run focused runner tests, the complete state suite, lint/type/privacy/vendor
   gates, and an independent exact-head review. Publish only a clean signed+DCO
   PR and wait for exact-head hosted checks before merging.
6. Update AR-1307 and AR-1293 with durable evidence. Do not claim formal or
   release qualification from development fixtures.

Dependency: completed AR-1302. It repairs AR-1307's recorded failure and must not modify handoffctl itself, require a
native ARM host, require a live provider, or introduce reviewed seed digests as
a development prerequisite.
