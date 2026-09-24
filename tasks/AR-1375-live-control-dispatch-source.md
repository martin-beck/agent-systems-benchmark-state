---
{
  "branch": "feature/ar-1375-live-control-dispatch-source",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1373", "AR-1374"],
  "id": "AR-1375",
  "next_action": "Wait for AR-1374 blocker resolution, then implement the runtime-owned authenticated control adapter for CLI live dispatch.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1375-live-control-dispatch-source.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Supply authenticated runtime control receipts to production live dispatch.",
  "task_revision": 1,
  "title": "Runtime-owned live control dispatch source",
  "updated_at": "2026-09-24T02:40:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1375-live-control-dispatch-source"
}
---

Created from the AR-1374 audit: the existing CLI accepts an opaque attempt
factory and the runtime bridge validates receipts, but no authenticated control
transport/chain source connects them. This AR must not synthesize authority.
