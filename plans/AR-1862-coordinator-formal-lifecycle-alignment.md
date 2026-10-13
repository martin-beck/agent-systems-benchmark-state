# AR-1862 plan: Coordinator formal lifecycle inventory alignment

Repair the downstream ASB formal lifecycle inventory so the exact upstream
AR-0034 Coordinator snapshot can pass vendor verification without weakening
formal or authority gates.

1. Reproduce AR-1861's exact failure against upstream signed merge
   `3b200c9accc000339e2f9009257ce8a10bce79e0` and preserve the failed-closed
   evidence.
2. Compare the downstream runtime `LIFECYCLE_MUTATION_COMMANDS` and formal
   operation sets with the upstream contract; add only the reviewed
   downstream-owned compatibility declarations and transition coverage for
   `bind-envelope`, `recover-execution`, `change-drift`, and `assumption`.
3. Add positive and negative tests for exact runtime/model parity, unknown or
   omitted operations, authority/lease fences, and vendor verification.
4. Run focused state tests, full state/schema/generated/privacy/formal gates,
   independent review, signed DCO exact-head CI, merge, and post-merge
   verification. Preserve coverage and all fail-closed behavior.
5. Re-run AR-1861 adoption only after this repair is merged and verified;
   AR-1826 remains untouched until the complete adoption is green.

This task does not modify upstream Coordinator sources, bypass vendor
provenance, or lower any formal/quality threshold.
