---
{
  "branch": "feature/ar-1485-process-owner-local-mock-lifecycle",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1472", "AR-1473", "AR-1480", "AR-1484"],
  "id": "AR-1485",
  "next_action": "Promote and claim, then audit the merged owner contract and implement the provider-free owner lifecycle slice.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1485-process-owner-local-mock-lifecycle.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Implement runtime-owned local/mock process lifecycle and opaque-source handoff.",
  "task_revision": 1,
  "title": "Process-owner local/mock lifecycle",
  "updated_at": "2026-09-27T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1485-process-owner-local-mock-lifecycle"
}
---

Bounded provider-free implementation successor for AR-1483. It owns only the
runtime/control lifecycle seam and must not modify asb-tui or accept caller
authority.

