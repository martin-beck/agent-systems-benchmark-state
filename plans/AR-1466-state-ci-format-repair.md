# AR-1466: State CI formatting repair

## Required work

1. Read the state development documentation and the complete CI failure
   evidence for the current protected `main` revision.
2. Apply only the deterministic formatter change required by the repository
   gate to `tools/validate_ar1308_capacity.py`; do not alter validation logic.
3. Run the focused validator tests, Ruff format/check and mypy gates, then the
   applicable full state test and coordination checks offline.
4. Independently inspect the diff, verify SSH signature and DCO, publish the
   reviewed state PR, wait for exact-head CI, and merge only after all required
   checks pass.

## Acceptance evidence

- formatter/check/type gates pass on the exact merge head;
- validator behavior and AR-1308 fail-closed semantics are unchanged;
- signed+DCO merge and exact-head CI evidence are recorded in the AR.

## Boundaries

No product source, formal contract, seed, runner capacity, handoffctl logic,
or asb-tui source may change in this repair.
