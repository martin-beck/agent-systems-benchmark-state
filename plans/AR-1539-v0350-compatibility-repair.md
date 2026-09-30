# AR-1539 plan: v0.3.50 runtime compatibility repair

1. Read AR-1538, the ASB state development/quality docs, the preserved
   `preserve/ar1538-v0350-mixed-snapshot` diff and the exact v0.3.50 source.
   Classify each failure as a coordinator API contract, ASB-owned adapter,
   SQLite fixture identity, or test-only expectation.
2. Reconcile the coordinator lifecycle/session interface with ASB's bound
   state backend without weakening lease, revision, admission, WAL identity or
   privacy guarantees. Keep formal files and AR-1307/1308 validators owned by
   ASB unless an explicit reviewed compatibility change is required.
3. Repair disposable SQLite test isolation and exact argument construction for
   checkpoint, resume, recovery and done-admission paths. Add positive and
   negative regression tests for every corrected failure, including process
   death and identity-change rejection.
4. Re-run the exact v0.3.50 vendor verifier, full state suite, Ruff/format/
   mypy, schema/generated-view/privacy/source-header checks and independent
   diff/signature review. Publish only from a clean exact tree with green
   hosted checks.

Acceptance: ASB consumes the immutable v0.3.50 runtime while all state,
lease/session, SQLite fence, formal and AR-1307/1308 development gates remain
green and fail-closed.
