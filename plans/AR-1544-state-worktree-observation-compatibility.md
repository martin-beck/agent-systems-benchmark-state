# AR-1544 plan: state-worktree observation compatibility

1. Read AR-1530, AR-1534, AR-1540, AR-1541, AR-1542 and AR-1543 plus the ASB
   coordination and vendor documentation. Reconcile the exact v0.3.50 source
   and the failing state-worktree test.
2. Reproduce the failure in a clean disposable state/product pair and record
   the expected bounded observations without private paths or raw command
   output.
3. Determine whether the fix belongs in the coordinator source release or an
   ASB-owned composition boundary. Do not edit a vendored coordinator file in
   place, and do not remove the state-worktree requirement from tests.
4. Implement the smallest reviewed fix with positive and negative coverage for
   state-root inclusion, product worktrees, detached heads, dirty paths,
   duplicate/overlapping worktrees and unavailable metadata.
5. Run vendor verification, focused/full state tests, lint/type/privacy gates,
   independent exact-head review and required hosted checks on the same SHA.
6. Update AR-1540 and the 1307/1308 closure ARs with the exact compatibility
   result. If a coordinator release is required, leave a named dependency and
   do not publish a mixed or locally altered vendor snapshot.
