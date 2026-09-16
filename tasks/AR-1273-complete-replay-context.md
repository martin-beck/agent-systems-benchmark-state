---
{
  "branch": "feature/ar-1273-complete-replay-context",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1273",
  "next_action": "Promote after dependency verification; implement the complete opaque runtime-issued replay request context and real supervised execution.",
  "observed_branch": "feature/ar-1273-complete-replay-context",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1273.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Provide complete runtime-owned context for strict-replay execution.",
  "task_revision": 2,
  "title": "Complete runtime-owned replay request context",
  "updated_at": "2026-09-16T23:29:59+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1273-complete-replay-context"
}
---
## AR-1273

Implement the complete runtime-owned replay request context and actual supervised execution. Preserve
AR-1272's blocked evidence; never accept caller-provided authority or fabricate lifecycle results.

- 2026-09-16T23:29:59+00:00: Dependencies done; AR-1272 proves complete caller-free replay context
  is required for real supervised execution.
