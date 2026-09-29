# AR-1510 plan: authenticated control source and production provider wiring

1. Reconcile state and verify AR-1509 is blocked with its 53/53 focused-gate
   evidence. Create an isolated worktree from protected main; do not inherit
   AR-1509's unmerged façade commits without an explicit reviewed extraction.
2. Read the complete product development, architecture and quality docs and
   map the existing control enrollment, receipt, scheduler, live run/sweep,
   cancellation and teardown contracts.
3. Define the private authenticated control-source interface and receipt
   verification path. Bind all authority material to the authenticated
   endpoint/session, enrollment/credential capability, generation, namespace,
   roots, tools, policy, restart and cancellation fences. Reject malformed,
   expired, revoked, replayed, mismatched and alternate-egress material.
4. Implement the non-test provider and wire runtime/control bootstrap,
   ordinary CLI live execution and scheduler transitions to obtain only opaque
   verified authority. Keep test fixtures behind explicit test-only adapters.
5. Add deterministic positive and negative tests covering source
   authentication, receipt integrity, expiry/revocation/cancellation/restart,
   teardown and egress denial. Run focused crate tests, workspace quality,
   formal/privacy/native applicable gates and fresh offline installation.
6. Independently review the complete diff against protected main. Only after
   clean exact-head evidence, SSH-signed DCO and review approval publish a PR;
   wait for exact-head hosted checks, merge through handoffctl, then verify all
   required post-merge workflows and release AR-1510 with durable evidence.

Blocking rule: if authenticated control state or production callsites cannot
be implemented without inventing authority, release this AR blocked with
captured evidence and create a narrower successor; never publish the test
facade or weaken a gate.
