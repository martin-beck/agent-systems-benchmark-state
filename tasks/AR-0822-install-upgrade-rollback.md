---
{
  "branch": "feature/install-lifecycle",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T09:24:19+00:00",
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
  "task_revision": 52,
  "title": "Add safe installation lifecycle management",
  "updated_at": "2026-09-09T07:24:19+00:00",
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

- 2026-09-09T07:14:57+00:00: Recorded command exit 8; command argv SHA-256
  dd29b57455827e6183a38b744cc03833d2c5ff5d09fe2a23f69f3c0854ac12ca.

- 2026-09-09T07:15:05+00:00: Heartbeat by codex-longrun-install-lifecycle-20260909.

- 2026-09-09T07:15:45+00:00: Heartbeat by codex-longrun-install-lifecycle-20260909.

- 2026-09-09T07:15:49+00:00: Recorded command exit 8; command argv SHA-256
  dd29b57455827e6183a38b744cc03833d2c5ff5d09fe2a23f69f3c0854ac12ca.

- 2026-09-09T07:16:12+00:00: Heartbeat by codex-longrun-install-lifecycle-20260909.

- 2026-09-09T07:16:48+00:00: Heartbeat by codex-longrun-install-lifecycle-20260909.

- 2026-09-09T07:16:51+00:00: Recorded command exit 8; command argv SHA-256
  dd29b57455827e6183a38b744cc03833d2c5ff5d09fe2a23f69f3c0854ac12ca.

- 2026-09-09T07:17:04+00:00: Heartbeat by codex-longrun-install-lifecycle-20260909.

- 2026-09-09T07:17:42+00:00: Heartbeat by codex-longrun-install-lifecycle-20260909.

- 2026-09-09T07:17:46+00:00: Recorded command exit 0; command argv SHA-256
  dd29b57455827e6183a38b744cc03833d2c5ff5d09fe2a23f69f3c0854ac12ca.

- 2026-09-09T07:18:10+00:00: Heartbeat by codex-longrun-install-lifecycle-20260909.

- 2026-09-09T07:18:20+00:00: Heartbeat by codex-longrun-install-lifecycle-20260909.

- 2026-09-09T07:18:24+00:00: Recorded command exit 0; command argv SHA-256
  120b8de5892732879a617bfdd0927a2649325392ec3b90b88dc84ccabf5d4803.

- 2026-09-09T07:18:59+00:00: Recorded command exit 0; command argv SHA-256
  776bb85b1914b189614b6fa4035276a61e6dfadb7d567d376168ec0f5057efcc.

- 2026-09-09T07:19:18+00:00: PR #108 exact head c7d6da7 passed all 15 required checks and was signed
  no-ff merged as 624d4c0. One merge-boundary LOCK_TIMEOUT occurred and was retried successfully;
  begin exact-main post-merge verification.

- 2026-09-09T07:19:33+00:00: Heartbeat by codex-longrun-install-lifecycle-20260909.

- 2026-09-09T07:19:36+00:00: Recorded command exit 0; command argv SHA-256
  82a856b834b4da18750e9fa26758a7e28be16e1820608692c884c826a4ae3afc.

- 2026-09-09T07:20:20+00:00: Heartbeat by codex-longrun-install-lifecycle-20260909.

- 2026-09-09T07:20:23+00:00: Recorded command exit 0; command argv SHA-256
  82a856b834b4da18750e9fa26758a7e28be16e1820608692c884c826a4ae3afc.

- 2026-09-09T07:20:33+00:00: Heartbeat by codex-longrun-install-lifecycle-20260909.

- 2026-09-09T07:20:52+00:00: Recorded command exit 0; command argv SHA-256
  82a856b834b4da18750e9fa26758a7e28be16e1820608692c884c826a4ae3afc.

- 2026-09-09T07:21:08+00:00: Recorded command exit 0; command argv SHA-256
  05ce06b6c39404bffd0d08a54196f885a7557dcdfe7f2c764e6b9c2e06a7adfb.

- 2026-09-09T07:22:08+00:00: Heartbeat by codex-longrun-install-lifecycle-20260909.

- 2026-09-09T07:22:11+00:00: Heartbeat by codex-longrun-install-lifecycle-20260909.

- 2026-09-09T07:22:15+00:00: Recorded command exit 0; command argv SHA-256
  6056f492b05389c85a170e193d513e7521aed3b5bd6efe16e0ed076ca9e40adf.

- 2026-09-09T07:23:04+00:00: Heartbeat by codex-longrun-install-lifecycle-20260909.

- 2026-09-09T07:23:08+00:00: Recorded command exit 0; command argv SHA-256
  6056f492b05389c85a170e193d513e7521aed3b5bd6efe16e0ed076ca9e40adf.

- 2026-09-09T07:23:27+00:00: Heartbeat by codex-longrun-install-lifecycle-20260909.

- 2026-09-09T07:23:58+00:00: Heartbeat by codex-longrun-install-lifecycle-20260909.

- 2026-09-09T07:24:02+00:00: Recorded command exit 0; command argv SHA-256
  6056f492b05389c85a170e193d513e7521aed3b5bd6efe16e0ed076ca9e40adf.

- 2026-09-09T07:24:19+00:00: Heartbeat by codex-longrun-install-lifecycle-20260909.
