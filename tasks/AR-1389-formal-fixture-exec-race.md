---
{
  "branch": "feature/ar-1389-formal-fixture-exec-race",
  "checkpoint_commit": "8c88b9ec9b4f529ebe30cb230029b2575ad4e6e5",
  "claim_expires": "",
  "depends_on": [
    "AR-1384"
  ],
  "id": "AR-1389",
  "next_action": "Claim the pre-bound isolated worktree, repair the evidenced formal fixture ETXTBSY race without weakening gates, and publish a signed PR.",
  "observed_branch": "feature/ar-1389-formal-fixture-exec-race",
  "observed_dirty": 0,
  "observed_head": "8c88b9ec9b4f529ebe30cb230029b2575ad4e6e5",
  "owner": "",
  "plan": "../plans/AR-1389-formal-fixture-exec-race.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Repair the formal online-build fixture race that caused ETXTBSY after AR-1388 merge.",
  "task_revision": 2,
  "title": "Formal fixture executable race repair",
  "updated_at": "2026-09-24T07:07:39+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1389-formal-fixture-exec-race"
}
---

This successor owns only the post-merge formal assurance failure recorded by
AR-1388. It must use a fresh isolated worktree and preserve all authority,
privacy, offline, boundedness, and local-mock boundaries.

- 2026-09-24T07:07:39+00:00: AR-1384 baseline verified; AR-1388 merge formal failure evidence
  reviewed; successor repair may proceed before release
