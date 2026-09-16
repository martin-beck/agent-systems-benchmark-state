---
{
  "branch": "feature/ar-1260-runtime-owned-strict-replay-integration",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T22:27:18+00:00",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1260",
  "next_action": "Promote and claim after reconciliation; wire replay_plan through runtime-issued StrictReplayLaunchBridge spawn and prove bounded transport lifecycle, egress denial, cancellation, cleanup, and no-fallback.",
  "observed_branch": "feature/ar-1260-runtime-owned-strict-replay-integration",
  "observed_dirty": 0,
  "observed_head": "055c86dc6594e2a31a153cdfe12f66323509e22d",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1260.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Integrate strict replay with runtime-owned attestation and supervised sandbox execution.",
  "task_revision": 7,
  "title": "Runtime-owned strict-replay integration",
  "updated_at": "2026-09-16T20:28:27+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1260-runtime"
}
---

## AR-1260

Implement the runtime-owned strict-replay handoff described in the plan. Preserve the reviewed
AR-1248 CLI contract and fail closed whenever runtime authority or supervised launch context is
missing, stale, duplicated, or mismatched.

- 2026-09-16T20:25:00+00:00: Created as the coordinator successor to AR-1248 after independent
  review confirmed that CLI-created readiness cannot replace runtime-issued namespace authority.

- 2026-09-16T20:27:04+00:00: Dependencies AR-1237, AR-1238, AR-1239 independently done; promote
  runtime-owned strict-replay integration.

- 2026-09-16T20:27:18+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-16T20:27:37+00:00: Recorded command exit 0; command argv SHA-256
  463a2b3478e4c4c507ddcb3a04a8ee990994c543356db5c621784f31dd43d354.

- 2026-09-16T20:28:20+00:00: Recorded command exit 0; command argv SHA-256
  df3f51288a439e254d63ec6692caf22033d5b5f9dbb9294e1c455f7eec83d16d.
