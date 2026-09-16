---
{
  "branch": "feature/ar-1260-runtime-owned-strict-replay-integration",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1237", "AR-1238", "AR-1239"],
  "id": "AR-1260",
  "next_action": "Promote and claim after reconciliation; wire replay_plan through runtime-issued StrictReplayLaunchBridge spawn and prove bounded transport lifecycle, egress denial, cancellation, cleanup, and no-fallback.",
  "observed_branch": "feature/ar-1260-runtime-owned-strict-replay-integration",
  "observed_head": "0000000000000000000000000000000000000000",
  "observed_dirty": 0,
  "owner": "",
  "plan": "../plans/AR-1260.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Integrate strict replay with runtime-owned attestation and supervised sandbox execution.",
  "task_revision": 1,
  "title": "Runtime-owned strict-replay integration",
  "updated_at": "2026-09-16T20:25:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1260-runtime"
}
---

## AR-1260

Implement the runtime-owned strict-replay handoff described in the plan. Preserve the reviewed
AR-1248 CLI contract and fail closed whenever runtime authority or supervised launch context is
missing, stale, duplicated, or mismatched.

- 2026-09-16T20:25:00+00:00: Created as the coordinator successor to AR-1248 after independent
  review confirmed that CLI-created readiness cannot replace runtime-issued namespace authority.
