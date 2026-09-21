---
{
  "branch": "feature/ar-1320-persisted-agent-release-index",
  "checkpoint_commit": "77571ff978b886e24d35e29c0febb553a90a2d65",
  "claim_expires": "",
  "depends_on": ["AR-1316"],
  "id": "AR-1320",
  "next_action": "Continue with AR-1322 for the bounded signed local release-index source and verified closure promotion; persistence/restart/refresh fencing is merged.",
  "owner": "",
  "plan": "../plans/AR-1320.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Persist and verify the ASB agent release index used by the setup wizard.",
  "task_revision": 3,
  "title": "Persisted authenticated agent release index",
  "updated_at": "2026-09-21T02:52:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1320-persisted-agent-release-index"
}
---

AR-1316 now publishes a truthful unavailable roster, but it is rebuilt in the
backend and does not yet persist a verified source snapshot across restart.
This AR owns the durable signed release-index and generation lifecycle needed
before any agent can become selectable.
