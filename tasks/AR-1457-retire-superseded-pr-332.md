---
{
  "branch": "maintenance/ar-1457-retire-superseded-pr-332",
  "checkpoint_commit": "23b2fb5f241934168131efe6cd5173d5d316a857",
  "claim_expires": "",
  "depends_on": [
    "AR-1453"
  ],
  "id": "AR-1457",
  "next_action": "Close obsolete PR #332 as superseded by merged PR #333, then verify the repository has no stale open PR for AR-1453 and release this maintenance AR with durable evidence.",
  "owner": "",
  "plan": "../plans/AR-1457.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "open",
  "summary": "Retire the obsolete pre-repair AR-1453 pull request without changing product code.",
  "task_revision": 2,
  "title": "Retire superseded AR-1453 pull request",
  "updated_at": "2026-09-26T18:34:36+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1457-retire-superseded-pr-332"
}
---

This maintenance AR exists solely to reconcile GitHub hygiene after AR-1453
was repaired and merged through PR #333. PR #332 is an earlier superseded
head with a DCO failure and a timing-sensitive test failure; it must not be
merged or amended. Close it as superseded, verify PR #333 remains the
authoritative merged head, and record the exact observations. No product,
asb-tui, or release changes are in scope.

- 2026-09-26T18:34:36+00:00: AR-1453 is done; promote narrowly scoped Git hygiene repair for
  obsolete PR #332.
