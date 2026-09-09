---
{
  "branch": "feature/install-lifecycle",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T09:10:38+00:00",
  "depends_on": [
    "AR-0104",
    "AR-0820",
    "AR-0821"
  ],
  "id": "AR-0822",
  "next_action": "Implement verified upgrades, migrations, rollback, repair, and non-destructive uninstall.",
  "observed_branch": "feature/install-lifecycle",
  "observed_dirty": 3,
  "observed_head": "513c1d926458f1cb6a26d3f7277dc7d9b1496df3",
  "owner": "codex-longrun-install-lifecycle-20260909",
  "plan": "../plans/AR-0822.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Manage the complete installed lifecycle without losing configuration, history, runs, or trust state.",
  "task_revision": 10,
  "title": "Add safe installation lifecycle management",
  "updated_at": "2026-09-09T07:11:18+00:00",
  "worktree_key": "agent-systems-benchmark-install-lifecycle"
}
---

## AR-0822

Manage the complete installed lifecycle without losing configuration, history, runs, or trust state.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-09T07:07:07+00:00: Dependencies AR-0104, AR-0820, and AR-0821 are durably released done;
  promote safe installation lifecycle management.

- 2026-09-09T07:07:24+00:00: Claimed by codex-longrun-install-lifecycle-20260909.

- 2026-09-09T07:07:32+00:00: Heartbeat by codex-longrun-install-lifecycle-20260909.

- 2026-09-09T07:07:35+00:00: Recorded command exit 0; command argv SHA-256
  46d4d8735238a0821f3057456fa8fc8e317069526b6b4699be0eeb091f1d4897.

- 2026-09-09T07:10:38+00:00: Heartbeat by codex-longrun-install-lifecycle-20260909.

- 2026-09-09T07:11:07+00:00: Implemented tools/install/lifecycle.sh with status, bounded
  three-backup retention, doctor-gated rollback, drift repair, and non-destructive uninstall;
  extended bootstrap tests and CLI-first-run docs. Focused tests pass; shellcheck unavailable on the
  development host.
