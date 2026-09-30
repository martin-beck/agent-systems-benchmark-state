# AR-1547 plan: coordinator v0.3.52 vendor adoption

1. Read AR-1534, AR-1540, AR-1541, AR-1544 and the complete coordinator vendor
   contract.
2. Verify `v0.3.52` and merge `1d806fa2996bde732f624cd63c2088a99f839431` from
   a clean clone; run the vendor verifier and privacy checks.
3. Run focused session, SQLite and state-worktree tests, then the full state
   suite and applicable Ruff/format/mypy gates.
4. Repair only ASB-owned compatibility fixtures/adapters/docs; never edit the
   vendored coordinator source or formal gates.
5. Independently review the complete diff and publish only a clean exact-head
   signed+DCO PR if source changes are required.
6. Record exact evidence and update dependent ARs, or leave a precise blocker.
