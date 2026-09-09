---
{
  "branch": "feature/install-lifecycle",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T09:14:51+00:00",
  "depends_on": [
    "AR-0104",
    "AR-0820",
    "AR-0821"
  ],
  "id": "AR-0822",
  "next_action": "Implement verified upgrades, migrations, rollback, repair, and non-destructive uninstall.",
  "observed_branch": "feature/install-lifecycle",
  "observed_dirty": 0,
  "observed_head": "c7d6da71c70931ae99a22447287f5027d46d50ff",
  "owner": "codex-longrun-install-lifecycle-20260909",
  "plan": "../plans/AR-0822.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Manage the complete installed lifecycle without losing configuration, history, runs, or trust state.",
  "task_revision": 21,
  "title": "Add safe installation lifecycle management",
  "updated_at": "2026-09-09T07:14:51+00:00",
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

- 2026-09-09T07:11:23+00:00: Recorded command exit 0; command argv SHA-256
  2549a95f37e84ad8dbbf53474b10714ce1a6e20c252dfb0e1ca93a9d1700dbee.

- 2026-09-09T07:11:43+00:00: Recorded command exit 0; command argv SHA-256
  6d932b2b1ece8f0729fb2e41c3f7ed0d75482db9c18bd3bfb9db66ba1388483c.

- 2026-09-09T07:11:57+00:00: Heartbeat by codex-longrun-install-lifecycle-20260909.

- 2026-09-09T07:12:01+00:00: Recorded command exit 8; command argv SHA-256
  dd29b57455827e6183a38b744cc03833d2c5ff5d09fe2a23f69f3c0854ac12ca.

- 2026-09-09T07:12:45+00:00: Heartbeat by codex-longrun-install-lifecycle-20260909.

- 2026-09-09T07:12:57+00:00: Heartbeat by codex-longrun-install-lifecycle-20260909.

- 2026-09-09T07:13:00+00:00: Recorded command exit 8; command argv SHA-256
  dd29b57455827e6183a38b744cc03833d2c5ff5d09fe2a23f69f3c0854ac12ca.

- 2026-09-09T07:13:53+00:00: Heartbeat by codex-longrun-install-lifecycle-20260909.

- 2026-09-09T07:14:02+00:00: Recorded command exit 8; command argv SHA-256
  dd29b57455827e6183a38b744cc03833d2c5ff5d09fe2a23f69f3c0854ac12ca.

- 2026-09-09T07:14:51+00:00: Heartbeat by codex-longrun-install-lifecycle-20260909.
