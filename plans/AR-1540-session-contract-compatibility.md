# AR-1540 plan: coordinator session-contract compatibility

1. Read the AR-1539 failure evidence, ASB development/quality docs and the
   exact v0.3.50 `handoffctl` session/checkpoint/recovery API.
2. Adapt only ASB-owned argument construction, task fixtures and integration
   boundaries for checkpoint, resume, recovery, done-admission and command
   dispatch. Preserve exact owner/revision/session fencing and unknown-field
   rejection; do not patch the vendored coordinator implementation.
3. Add positive and negative tests for missing owners, missing session IDs,
   incomplete `spec_acceptance`, stale revisions and absent snapshots.
4. Run the focused and full state suites, strict lint/type/format/privacy and
   generated-view checks, then independently review and publish through the
   normal workflow.

Acceptance: ASB's complete state lifecycle tests pass against the immutable
v0.3.50 runtime without weakening admission or recovery semantics.
