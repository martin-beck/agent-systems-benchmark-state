# AR-1819 plan: fail-closed expired-claim recovery

## Scope

1. Reconcile the current state repository and preserve AR-1796's expired-claim
   history and AR-1818's clean-publication work without editing generated views.
2. Change `recover-expired` so an expired in-progress claim is recoverable only
   when exactly one validated session record exists at the current task
   revision. Reject absent, malformed, duplicate, or future snapshots before
   any state mutation. Do not impersonate the former owner.
3. Retain process-scope validation as diagnostic evidence, but do not allow a
   claim-time PID/start-time to authorize snapshotless recovery.
4. Add positive coverage for exact-snapshot recovery and negative coverage for
   missing snapshot, duplicate snapshot, future revision, invalid session, and
   live worker identity. Preserve rollback-on-failure behavior.
5. Run focused and applicable full state quality gates, independent exact-head
   review, signed DCO integration, post-merge reconciliation, and
   `handoffctl doctor --live`.

## Acceptance

- No expired claim can become open without an exact current-revision session
  snapshot.
- AR-1796 and AR-1818 records and their historical evidence are not rewritten.
- State schema, generated projections, privacy, DCO, signatures, and CI remain
  green.
