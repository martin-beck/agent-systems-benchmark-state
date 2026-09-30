# AR-1551 plan: first-customer platform authority deployment

1. Read AR-1505, AR-1513, AR-1514 and AR-1523 plus the ASB runtime/control
   architecture. Freeze the authenticated binding and ownership boundary.
2. Choose an isolated second-disk deployment boundary (owner-only Unix service
   or container/VM) and define its versioned opaque handoff. Keep private
   authority and credential capability outside public state.
3. Implement the deployment source and its runtime/control adapter. Bind every
   returned value to the authenticated session, generation, expiry, restart,
   cancellation, revocation and teardown fences; reject alternate egress and
   all caller-supplied authority.
4. Add deterministic local/mock/replay tests for positive issuance and hostile
   lifecycle, tampering, replay, mismatch, missing-source and cleanup cases.
5. Run focused and full ASB gates, independent exact-head review, hosted CI and
   a disposable first-customer-style deployment. Hand the sanitized receipt and
   opaque contract to AR-1523; never claim live provider or formal qualification
   from a fixture.

Completion requires an actual non-test deployment source and ordinary run/sweep
   handoff. A test façade, self-attested record, digest-only catalog or live
   provider probe is insufficient.
