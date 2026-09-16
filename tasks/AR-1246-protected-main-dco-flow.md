---
{
  "branch": "fix/ar-1246-protected-main-dco-flow",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1242",
    "AR-1245"
  ],
  "id": "AR-1246",
  "next_action": "Implement protected-main-aware DCO validation using the authenticated web-flow merge attestation; retain strict topic and PR checks.",
  "observed_branch": "fix/ar-1246-protected-main-dco-flow",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1246.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Durably admit authenticated GitHub protected-main merges without one-off DCO hash exceptions.",
  "task_revision": 2,
  "title": "Protected-main DCO flow",
  "updated_at": "2026-09-16T09:50:24+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1246"
}
---

Implement only AR-1246 in an isolated worktree using the ASB development documentation and
handoffctl. Preserve all published history and do not touch runtime, bundle, or TUI behavior.

- 2026-09-16T09:50:24+00:00: PR-194 repeated the GitHub merge DCO failure; approved durable
  protected-main web-flow validation instead of per-merge hash exceptions.
