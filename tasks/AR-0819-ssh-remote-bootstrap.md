---
{
  "branch": "feature/ssh-remote-bootstrap",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0803",
    "AR-0804"
  ],
  "id": "AR-0819",
  "next_action": "Integrate signed no-ff PR #98 onto current main, then run and verify all exact-main post-merge workflows before release.",
  "observed_branch": "feature/ssh-remote-bootstrap",
  "observed_dirty": 0,
  "observed_head": "980276dd2885682ad2251893395eedf55558dc98",
  "owner": "",
  "plan": "../plans/AR-0819.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "done",
  "summary": "Use configured SSH hosts as the safe default path to a remote runner and help establish dedicated key authentication.",
  "task_revision": 44,
  "title": "Add SSH remote discovery and bootstrap",
  "updated_at": "2026-09-09T03:41:05+00:00",
  "worktree_key": "agent-systems-benchmark-ssh-remote-bootstrap"
}
---
## AR-0819

Use configured SSH hosts as the safe default path to a remote runner and help establish dedicated key authentication.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-09T03:18:52+00:00: Dependencies AR-0803 and AR-0804 are done; promote SSH remote bootstrap
  as the next highest-priority implementable track.

- 2026-09-09T03:18:55+00:00: Claimed by replay_20260909.

- 2026-09-09T03:18:58+00:00: Heartbeat by replay_20260909.

- 2026-09-09T03:19:19+00:00: Recorded command exit 0; command argv SHA-256
  5624c9837a58856e6fa3911d3b5dc8c8d53afbcc1bb42042cfb083f5c1222cd1.

- 2026-09-09T03:21:20+00:00: Recorded command exit 101; command argv SHA-256
  bd6d4cd0b6e36ea55d1688716fc8a4195edbcc46be3b6a431528778ec24add00.

- 2026-09-09T03:21:52+00:00: Recorded command exit 0; command argv SHA-256
  bd6d4cd0b6e36ea55d1688716fc8a4195edbcc46be3b6a431528778ec24add00.

- 2026-09-09T03:23:19+00:00: Recorded command exit 0; command argv SHA-256
  bd6d4cd0b6e36ea55d1688716fc8a4195edbcc46be3b6a431528778ec24add00.

- 2026-09-09T03:25:15+00:00: Recorded command exit 0; command argv SHA-256
  bd6d4cd0b6e36ea55d1688716fc8a4195edbcc46be3b6a431528778ec24add00.

- 2026-09-09T03:25:56+00:00: Recorded command exit 0; command argv SHA-256
  87266716b00741d7a80840dd4903145b7d64c73c32170a8c2f02059ca18ef686.

- 2026-09-09T03:26:16+00:00: Recorded command exit 0; command argv SHA-256
  982c6010a9b918a95c06425d6471d37241d9b94995e2360aac238c600bdbc46b.

- 2026-09-09T03:26:36+00:00: Recorded command exit 0; command argv SHA-256
  5209e70e0d76346940af636c3e9914e31692bd2d3fef2b2fa10d4f995c3aa76b.

- 2026-09-09T03:26:57+00:00: Implemented and tested SSH discovery/bootstrap slice: bounded Include
  parsing, OpenSSH ssh -G resolution, fixed no-shell stdio probe argv, private recent ledger,
  confirmation-gated restricted Ed25519 enrollment, atomic authorized_keys update, docs, 24 asb-tui
  tests, Clippy, policy, DCO, and diff checks all pass.

- 2026-09-09T03:27:00+00:00: Heartbeat by replay_20260909.

- 2026-09-09T03:27:27+00:00: Recorded command exit 0; command argv SHA-256
  55e684d1f25085854fe16f2f2fc59ae7e10e662f279c9a109f8feacdc178a714.

- 2026-09-09T03:27:48+00:00: Recorded command exit 8; command argv SHA-256
  eed410fedf8fda4d7ec90faacbf65b391487b06f09a0c48e7d7bcb8410046db7.

- 2026-09-09T03:28:52+00:00: Recorded command exit 8; command argv SHA-256
  eed410fedf8fda4d7ec90faacbf65b391487b06f09a0c48e7d7bcb8410046db7.

- 2026-09-09T03:29:03+00:00: Heartbeat by replay_20260909.

- 2026-09-09T03:30:12+00:00: Recorded command exit 8; command argv SHA-256
  eed410fedf8fda4d7ec90faacbf65b391487b06f09a0c48e7d7bcb8410046db7.

- 2026-09-09T03:31:22+00:00: Recorded command exit 8; command argv SHA-256
  eed410fedf8fda4d7ec90faacbf65b391487b06f09a0c48e7d7bcb8410046db7.

- 2026-09-09T03:31:32+00:00: Heartbeat by replay_20260909.

- 2026-09-09T03:32:29+00:00: Recorded command exit 0; command argv SHA-256
  eed410fedf8fda4d7ec90faacbf65b391487b06f09a0c48e7d7bcb8410046db7.

- 2026-09-09T03:32:37+00:00: Heartbeat by replay_20260909.

- 2026-09-09T03:32:58+00:00: PR #98 exact head 980276d is fully green across all required quality,
  formal, fault, fuzz, mutation, Rust x86/arm, and emulated aarch64 checks.

- 2026-09-09T03:33:23+00:00: Recorded command exit 0; command argv SHA-256
  7d8ea69f222b0a250ecb8c2ad1eea560cdcfc8e4763c86f2f2974784b4c24700.

- 2026-09-09T03:33:52+00:00: Recorded command exit 0; command argv SHA-256
  99851735031344b5ff5587e1222adb4e5b1da47333db148c45f1d32f4a4ee63e.

- 2026-09-09T03:34:14+00:00: Recorded command exit 0; command argv SHA-256
  ba937448e654e169e2d4cb023b6152dc2337e41ba3c2e507127654fb1c937b28.

- 2026-09-09T03:34:41+00:00: Recorded command exit 0; command argv SHA-256
  3a0d2d32a7984d707d3b4f0196844bd7de9fa14767be7cfa323aa9948a83a3a8.

- 2026-09-09T03:34:52+00:00: Recorded command exit 0; command argv SHA-256
  58716a0f563be2733c59e6fbd2e99f52c225afda9d5781504f8b46052d9f9ec8.

- 2026-09-09T03:35:02+00:00: Heartbeat by replay_20260909.

- 2026-09-09T03:36:10+00:00: Recorded command exit 0; command argv SHA-256
  58716a0f563be2733c59e6fbd2e99f52c225afda9d5781504f8b46052d9f9ec8.

- 2026-09-09T03:36:17+00:00: Heartbeat by replay_20260909.

- 2026-09-09T03:37:27+00:00: Recorded command exit 0; command argv SHA-256
  58716a0f563be2733c59e6fbd2e99f52c225afda9d5781504f8b46052d9f9ec8.

- 2026-09-09T03:37:36+00:00: Heartbeat by replay_20260909.

- 2026-09-09T03:38:35+00:00: Recorded command exit 0; command argv SHA-256
  58716a0f563be2733c59e6fbd2e99f52c225afda9d5781504f8b46052d9f9ec8.

- 2026-09-09T03:38:43+00:00: Heartbeat by replay_20260909.

- 2026-09-09T03:39:44+00:00: Heartbeat by replay_20260909.

- 2026-09-09T03:39:58+00:00: Recorded command exit 0; command argv SHA-256
  f3bdc94cebf0c7f91c7cfcd6f1db638c32f6c8ddc78f5f799f3049835bfa5ceb.

- 2026-09-09T03:40:07+00:00: Heartbeat by replay_20260909.

- 2026-09-09T03:40:41+00:00: Recorded command exit 0; command argv SHA-256
  01e813eb80f58957dc36c890b6ab64db170daaf456de36ce71ed558c4a9b960f.

- 2026-09-09T03:41:05+00:00: Completed and released: signed candidate 980276d, PR #98 fully green at
  exact head, signed no-ff merge 7d9191c onto main, 24 asb-tui tests plus Clippy passed, repository
  policy and DCO passed, all six exact-main workflows green (runs 34307633249, 34307633250,
  34307633251, 34307633246, 34307633287, 34307633299), primary checkout synchronized clean at
  7d9191c, temporary integration worktree removed.
