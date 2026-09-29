# AR-1513 plan: authenticated lease-to-live-dispatch bridge

1. Reconcile state and verify AR-1512's blocked review. Start an isolated
   worktree from protected main; preserve a4064ab as evidence only.
2. Audit existing authenticated owner/enrollment/certificate contracts,
   `ProcessOwnerMaterialLease`, `LiveProviderRuntimeHandle`, dispatch source,
   CLI run/sweep and sandbox launch APIs.
3. Replace public/self-authenticated material issuance with a runtime-owned
   authenticated source. Bind owner/session/enrollment proof, generation,
   namespace, credential reference, roots, policy/allowlist, tools, target,
   expiry, restart and cancellation; keep private data out of receipts.
4. Implement the ordinary non-test runtime/control/CLI bridge from a validated
   lease to the live provider handle and dispatch source. Ensure transitions
   recheck expiry/revoke/cancel/teardown and cannot accept caller/PATH/config
   authority.
5. Add bounded executable provenance checks (no symlink/nonexistent path,
   permission and byte/hash mismatch, adapter/tool drift) plus replay,
   unknown-field, target/egress and lifecycle negative tests. Run all focused,
   serial workspace, formal/privacy and documentation gates.
6. Independently review the exact clean signed DCO diff, publish only after
   approval, wait exact-head CI, protected merge and terminal post-merge
   assurance, then release AR-1513 and resume AR-1511's final consumer wiring.

If authenticated issuance cannot be implemented from existing owner state,
record the precise missing primitive and create a narrower contract AR; never
publish the self-authenticated store or a test-only bridge.
