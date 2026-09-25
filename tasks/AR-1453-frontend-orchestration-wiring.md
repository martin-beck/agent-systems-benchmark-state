---
{
  "branch": "feature/ar-1453-frontend-orchestration-wiring",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1452"
  ],
  "id": "AR-1453",
  "next_action": "Promote after AR-1452 post-merge verification and wire run, sweep, replay, cancellation, and status through the service.",
  "owner": "",
  "plan": "../plans/AR-1453.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Make CLI and control use the central service for every run lifecycle.",
  "task_revision": 2,
  "title": "Route ASB frontends through central orchestration",
  "updated_at": "2026-09-25T20:40:23+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1453-frontend-orchestration-wiring"
}
---

Keep asb-tui out of scope; its future adapter can consume the same stable
asb-control protocol after this AR is complete.


- 2026-09-25T20:40:23+00:00: AR-1452 is merged and all seven exact-main post-merge workflows passed.
  Promote AR-1453 to implement CLI/control routing through the central runtime-owned orchestration
  service; keep asb-tui out of scope.
