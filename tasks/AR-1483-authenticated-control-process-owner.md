---
{
  "branch": "feature/ar-1483-authenticated-control-process-owner",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1472",
    "AR-1473",
    "AR-1480"
  ],
  "id": "AR-1483",
  "next_action": "Promote and claim, then audit whether the runtime/control owner contract can be implemented without caller authority.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1483-authenticated-control-process-owner.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Own authenticated control session and lifecycle while minting opaque CLI dispatch sources.",
  "task_revision": 2,
  "title": "Authenticated control process owner",
  "updated_at": "2026-09-27T12:06:55+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1483-authenticated-control-process-owner"
}
---

Smallest successor for the concrete process-owner gap recorded by AR-1482.
It must remain ASB-only, provider-free, and fail closed; it must not expose
caller authority or modify asb-tui.


- 2026-09-27T12:06:55+00:00: Smallest dependency-safe process-owner successor for AR-1482. Depends
  only on completed AR-1472, AR-1473, and AR-1480; owns authenticated control session, chain store,
  resolver, and lifecycle without AR-1374/1375.
