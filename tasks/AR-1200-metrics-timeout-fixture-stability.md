---
{
  "branch": "repair/metrics-timeout-flake",
  "checkpoint_commit": "0a7f6a192af9b6a538c7547dfff9e65842d59049",
  "claim_expires": "2026-09-15T11:29:16+00:00",
  "depends_on": [],
  "id": "AR-1200",
  "next_action": "Review and merge the isolated test-fixture stabilization after exact-head CI passes; do not modify production timeout policy.",
  "owner": "root-ar1200-metrics",
  "plan": "../plans/AR-1200.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Remove hosted timing flakiness from the bounded kernel diagnostic rejection test.",
  "task_revision": 2,
  "title": "Kernel diagnostic rejection fixture stability",
  "updated_at": "2026-09-15T09:29:16+00:00",
  "worktree_key": "agent-systems-benchmark-metrics-timeout-flake"
}
---

The bounded kernel diagnostic test launched the complete instrumented test binary for its
rejection case while enforcing a 100 ms deadline. Hosted CI intermittently observed
`TimedOut` instead of the expected `ProbeRejected`, because process startup and scheduler
load consumed the test deadline before the panic fixture ran. This AR keeps the production
deadline unchanged and uses a tiny pinned rejection fixture script instead. The actual
failure classification, output bounds, staging verification, and cleanup remain exercised.


- 2026-09-15T09:29:16+00:00: Claimed by root-ar1200-metrics.
