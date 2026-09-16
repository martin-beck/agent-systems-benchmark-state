---
{
  "branch": "feature/ar-1232",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T04:14:41+00:00",
  "depends_on": [
    "AR-0505",
    "AR-1100",
    "AR-1230"
  ],
  "id": "AR-1232",
  "next_action": "Implement the approved SandboxBackend process-supervision seam for strict replay, including real child egress denial and bounded cancellation/restart/crash recovery tests.",
  "observed_branch": "feature/ar-1232",
  "observed_dirty": 0,
  "observed_head": "a83ba8e278e40b538160e87a2a40c0fb26418dae",
  "owner": "asb_ar1232_sandbox_supervision",
  "plan": "../plans/AR-1232.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Supervise strict replay adapters inside the approved network-denied sandbox.",
  "task_revision": 5,
  "title": "Sandboxed replay process supervision",
  "updated_at": "2026-09-16T02:14:57+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1232"
}
---

- 2026-09-16T02:15:00+00:00: Created from AR-1231 review. AR-1231 provides the typed launch,
  route identity, endpoint policy, and capability contract; runtime child-process supervision and
  descendant egress proof require this separate implementation slice.

- 2026-09-16T02:14:38+00:00: Dependencies AR-0505, AR-1100 and AR-1230 are done; promote runtime
  process supervision.

- 2026-09-16T02:14:41+00:00: Claimed by asb_ar1232_sandbox_supervision.

- 2026-09-16T02:14:50+00:00: Recorded command exit 0; command argv SHA-256
  1c610d376f7e1941d69ba01298d4d9058ff38ae02a75c57f0f3963898a2c5334.
