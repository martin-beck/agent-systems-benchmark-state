---
{
  "schema_version": 1,
  "id": "AR-1453",
  "title": "Route ASB frontends through central orchestration",
  "status": "planned",
  "priority": "P0",
  "summary": "Make CLI and control use the central service for every run lifecycle.",
  "next_action": "Promote after AR-1452 post-merge verification and wire run, sweep, replay, cancellation, and status through the service.",
  "task_revision": 1,
  "updated_at": "2026-09-25T17:29:20+00:00",
  "owner": "",
  "claim_expires": "",
  "worktree_key": "agent-systems-benchmark-ar-1453-frontend-orchestration-wiring",
  "branch": "feature/ar-1453-frontend-orchestration-wiring",
  "checkpoint_commit": "",
  "plan": "../plans/AR-1453.md",
  "depends_on": ["AR-1452"]
}
---

Keep asb-tui out of scope; its future adapter can consume the same stable
asb-control protocol after this AR is complete.

