---
{
  "branch": "repair/ar-1312-post-merge-coverage-floor",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1310"
  ],
  "id": "AR-1312",
  "next_action": "No supported transfer can make AR-1312 promotable: handoffctl promote requires every dependency done, and AR-1310 remains blocked by the real 89.99% post-merge coverage failure. Keep planned/ownerless; repair AR-1310's coverage blocker first, then promote at a fresh revision.",
  "owner": "",
  "plan": "../plans/AR-1312.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Repair the post-merge workspace coverage deficit without weakening the 90% floor.",
  "task_revision": 2,
  "title": "Post-merge workspace coverage floor repair",
  "updated_at": "2026-09-18T21:02:02+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1312-post-merge-coverage-floor"
}
---

# AR-1312: Post-merge workspace coverage floor repair

The AR-1310 implementation is merged, but required post-merge policy run
35393146183 failed at the existing workspace line-coverage floor: 89.99% at
merge commit 17a1530e620608a4d53b6d92ba48c642400778e2. This planned successor
must add meaningful tests for the uncovered paths and preserve the threshold.

- 2026-09-18T21:02:02+00:00: Dependency-policy audit: AR-1310 cannot be marked done or superseded
  while its post-merge coverage gate is unresolved; promote correctly refuses AR-1312. No bypass or
  manual dependency edit performed.
