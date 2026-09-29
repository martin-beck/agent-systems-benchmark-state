# AR-1534 plan: coordinator vendor-integrity repair

1. Read the coordinator vendor documentation, `coordinator.vendor.json`, the
   exact AR-1530 diff, and the state development process. Confirm the mismatch
   against the protected state head and record the expected immutable digests.
2. Determine whether the bounded `CURRENT.md` projection change is an approved
   coordinator upgrade/patch. Do not edit the vendor manifest merely to make the
   check pass and do not copy or extract handoffctl into a new implementation.
3. If approved, update the vendor contract through its documented upgrade path;
   otherwise move only the non-vendor projection behavior to an allowed state
   layer, preserving generated output, schema validation, locking, lease and
   race semantics. Add positive and negative tests for the repaired boundary.
4. Run vendor verification, the complete state suite, strict mypy/Ruff/format,
   source-header/privacy/schema/generated-view checks and the exact-head hosted
   coordination workflow. Independently review the full diff and signed+DCO
   history.
5. Publish and merge only from a clean exact tree. Reconcile AR-1532 and its
   dependents with the terminal result; do not claim formal AR-1307/1308
   qualification from development fixtures.

Acceptance: vendor verification passes against an approved immutable contract;
no handoffctl replacement or weakened gate is introduced; all coordinator fault,
lease, generated-view and privacy gates remain green; AR-1532 can rerun its full
quality gates on the exact repaired head.

