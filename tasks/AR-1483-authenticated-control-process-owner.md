---
{
  "branch": "feature/ar-1483-authenticated-control-process-owner",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1472", "AR-1473", "AR-1480"],
  "id": "AR-1483",
  "next_action": "Promote and claim, then audit whether the runtime/control owner contract can be implemented without caller authority.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1483-authenticated-control-process-owner.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Own authenticated control session and lifecycle while minting opaque CLI dispatch sources.",
  "task_revision": 1,
  "title": "Authenticated control process owner",
  "updated_at": "2026-09-27T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1483-authenticated-control-process-owner"
}
---

Smallest successor for the concrete process-owner gap recorded by AR-1482.
It must remain ASB-only, provider-free, and fail closed; it must not expose
caller authority or modify asb-tui.

