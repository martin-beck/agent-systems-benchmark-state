---
{
  "branch": "feature/ar-1232",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1231"],
  "id": "AR-1232",
  "next_action": "Implement the approved SandboxBackend process-supervision seam for strict replay, including real child egress denial and bounded cancellation/restart/crash recovery tests.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1232.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Supervise strict replay adapters inside the approved network-denied sandbox.",
  "task_revision": 1,
  "title": "Sandboxed replay process supervision",
  "updated_at": "2026-09-16T02:15:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1232"
}
---

- 2026-09-16T02:15:00+00:00: Created from AR-1231 review. AR-1231 provides the typed launch,
  route identity, endpoint policy, and capability contract; runtime child-process supervision and
  descendant egress proof require this separate implementation slice.
