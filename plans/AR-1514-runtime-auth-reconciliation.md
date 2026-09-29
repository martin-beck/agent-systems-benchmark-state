# AR-1514 plan: reconciled development auth handoff

1. Start from protected ASB main in an isolated worktree and audit the
   `auth_enroll` and `auth_helper_invoke` control-runtime paths, including the
   durable intent/catalog and restart reconciliation code.
2. Reproduce the development-only failure with a fresh disposable state root:
   digest-only enrollment commits, the allowlisted helper executes, and the
   following v1.10 helper mutation currently returns `-33008`.
3. Repair startup and post-mutation reconciliation so committed enrollment
   state is materialized before helper invocation. Reconcile stale intents and
   `NeedsReconciliation` state deterministically; retain fail-closed behavior
   for genuinely uncertain mutations.
4. Preserve generation, restart, cancellation, and idempotency fencing. Do not
   add production authorization requirements, raw credentials, or provider
   reachability to the development path.
5. Add provider-free tests for clean startup, stale-intent recovery, restart,
   retry, duplicate idempotency keys, uncertain mutation, and digest-only
   `AuthStatus`; record exact runtime revision, endpoint/helper identities, and
   result digests without raw helper output or secrets.
6. Run the locked serial workspace/formal/privacy gates, obtain independent
   exact-head review, merge only with signed DCO and green hosted checks, then
   rerun the standalone asb-tui AR-1323 qualification and update its paired
   evidence.

The development runtime may be unauthorized and local. Production trust,
credential storage, and provider access remain outside this AR.
