---
{
  "branch": "repair/ar-1312-post-merge-coverage-floor",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-19T10:07:32+00:00",
  "depends_on": [],
  "id": "AR-1312",
  "next_action": "Promote and claim the independent coverage repair; preserve AR-1310 and AR-1313 as evidence, then raise exact workspace coverage above 90% without weakening the floor.",
  "owner": "ar1312_coverage_worker",
  "plan": "../plans/AR-1312.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair the post-merge workspace coverage deficit without weakening the 90% floor.",
  "task_revision": 5,
  "title": "Post-merge workspace coverage floor repair",
  "updated_at": "2026-09-19T08:07:32+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1312-post-merge-coverage-floor"
}
---

# AR-1312: Post-merge workspace coverage floor repair

The AR-1310 implementation is merged, but required post-merge policy run
35393146183 failed at the existing workspace line-coverage floor: 89.99% at
merge commit 17a1530e620608a4d53b6d92ba48c642400778e2. This planned successor
must add meaningful tests for the uncovered paths and preserve the threshold.

- 2026-09-19T08:06:30+00:00: Dependency deadlock repaired by signed coordinator metadata revision.
  AR-1310 remains preserved as the merged implementation/evidence reference, but cannot be a hard
  prerequisite because its post-merge coverage failure is exactly the defect AR-1312 must repair.
  AR-1312 is now independent and remains subject to the unchanged 90% gate, exact-head CI, review,
  merge, and post-merge verification. No product or quality gate was weakened.

- 2026-09-19T08:06:48+00:00: Dependency deadlock corrected: independent coverage repair authorized;
  AR-1310 remains evidence, 90% floor unchanged.

- 2026-09-19T08:07:32+00:00: Claimed by ar1312_coverage_worker.
