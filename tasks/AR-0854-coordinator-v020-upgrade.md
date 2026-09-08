---
{
  "branch": "upgrade/coordinator-v0.2.0",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-0854",
  "next_action": "Promote and claim the upgrade, vendor signed v0.2.0 in an isolated worktree, and publish only after exact-head gates pass.",
  "owner": "",
  "plan": "../plans/AR-0854.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "done",
  "summary": "Adopt coordinator v0.2.0 concurrency, recovery, durable-run, replica, and vendor hardening.",
  "task_revision": 6,
  "title": "Upgrade shared workflow coordinator to v0.2.0",
  "updated_at": "2026-09-08T11:51:35+00:00",
  "worktree_key": "agent-systems-benchmark-coordinator-v020"
}
---

This task upgrades only the pinned shared coordinator artifact and its directly associated
verification and documentation.

- 2026-09-08T10:30:36+00:00: Signed v0.2.0 release and both upstream green CI runs verified.

- 2026-09-08T10:30:38+00:00: Claimed by codex-coordinator-v020-20260908.

- 2026-09-08T10:31:07+00:00: Recorded command exit 0; command argv SHA-256
  620eb891b904b4e7a6c94cc5211d797e375d4128444efb562a6fc9d8043a3975.

- 2026-09-08T10:31:43+00:00: Recorded command exit 0; command argv SHA-256
  93a6e911c7abbed05c4b37d2de90ca01b4b86c1cd76c734892cdf4344e6c64d3.

- 2026-09-08T11:51:35+00:00: Merged PR #14 at GitHub-signed 055748439df71db6c51dfde53a383710e30ff3ca
  after exact-head strict, AWQ, and formal gates passed. Post-merge formal run 34221859215 passed on
  the dedicated repository runner; reconciled-main strict run 34222172572 passed. Coordinator v0.2.0
  vendor verification, 60 tests with 95% coverage, all four TLC models, project binding,
  concurrency, recovery, durability, replica, and liveness checks are green.
