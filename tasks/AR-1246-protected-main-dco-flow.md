---
{
  "branch": "fix/ar-1246-protected-main-dco-flow",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T11:50:36+00:00",
  "depends_on": [
    "AR-1242",
    "AR-1245"
  ],
  "id": "AR-1246",
  "next_action": "Monitor PR #195 required checks; after merge run post-merge protected-main verification and release done.",
  "observed_branch": "fix/ar-1246-protected-main-dco-flow",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "asb_ar1237_launch_bridge_worker",
  "plan": "../plans/AR-1246.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Durably admit authenticated GitHub protected-main merges without one-off DCO hash exceptions.",
  "task_revision": 4,
  "title": "Protected-main DCO flow",
  "updated_at": "2026-09-16T09:53:07+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1246"
}
---

Implement only AR-1246 in an isolated worktree using the ASB development documentation and
handoffctl. Preserve all published history and do not touch runtime, bundle, or TUI behavior.

- 2026-09-16T09:50:24+00:00: PR-194 repeated the GitHub merge DCO failure; approved durable
  protected-main web-flow validation instead of per-merge hash exceptions.

- 2026-09-16T09:50:36+00:00: Claimed by asb_ar1237_launch_bridge_worker.

- 2026-09-16T09:53:07+00:00: Checkpoint commit 35c69dc pushed in clean worktree and PR #195 opened.
  Removes one-off PR-192 hash exception; protected-main validates topic DCO/SSH then authenticates
  GitHub Web Flow final merge, while ssh-only and local final merges remain strict. Local
  signature-policy tests, fmt, clippy and workspace tests pass.
