---
{
  "branch": "feature/ar-1302-portable-tlc-runner",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T09:15:14+00:00",
  "depends_on": [],
  "id": "AR-1302",
  "next_action": "Promote and provision a digest-pinned x86_64 container/VM runner with portable cgroup containment, bounded thread/memory/swap capacity, and owner-private evidence paths for AR-1293.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "98acd6d5f5a206b351a54689e7817dd43af406ca",
  "owner": "codex-ar1302-runner-20260917",
  "plan": "../plans/AR-1302.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provision a clean portable TLC CI/VM runner for state formal admission.",
  "task_revision": 15,
  "title": "Portable TLC CI/VM runner",
  "updated_at": "2026-09-17T07:16:21+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1302-portable-tlc-runner"
}
---

## AR-1302

Provision the clean, portable-containment runner required to unblock AR-1293. Keep all images,
VMs, caches, queues, locks and evidence under `/srv/data/projects`; use immutable provenance,
offline-after-install behavior, no network or host-mount access, bounded execution and sanitized
evidence. Native ARM64 is optional and must not be a gate. Do not modify ASB product code,
asb-tui, handoffctl, or unrelated root-owned admission locks.

- 2026-09-17T07:09:22+00:00: Create clean portable TLC runner to unblock AR-1293; no product or
  asb-tui dependency

- 2026-09-17T07:10:38+00:00: Claimed by codex-ar1302-runner-20260917.

- 2026-09-17T07:10:47+00:00: Recorded command exit 0; command argv SHA-256
  fd092032b6d14bf8b53313beae3931f4074a2111f503bc5021464a0c35121252.

- 2026-09-17T07:12:48+00:00: Heartbeat by codex-ar1302-runner-20260917.

- 2026-09-17T07:12:50+00:00: Recorded command exit 0; command argv SHA-256
  b08c2d8d2773a00d8520aab8910dc444e48ccf8febeb51d9c0d825ed3a02ea55.

- 2026-09-17T07:13:41+00:00: Recorded command exit 0; command argv SHA-256
  d667a58d27e6920c90524c55ecd81df13e4a8f3080dbe844aff3ae9d5990a50c.

- 2026-09-17T07:14:13+00:00: Recorded command exit 1; command argv SHA-256
  4cc5bdf8eaa7b6f8f07d5f475f5048c08e48dd4d61cf2c1832e5339c2e843ed5.

- 2026-09-17T07:14:29+00:00: Recorded command exit 0; command argv SHA-256
  e4f842cc5744a8aeed6e22075832459707a5c67223e513c61840f6ffdb7c8b73.

- 2026-09-17T07:14:55+00:00: Recorded command exit 1; command argv SHA-256
  2e4709a3c708405760e333d4bfc380cf00fcbbf909bfbc301dab89d1e04a3d98.

- 2026-09-17T07:15:14+00:00: Heartbeat by codex-ar1302-runner-20260917.

- 2026-09-17T07:15:17+00:00: Recorded command exit 0; command argv SHA-256
  ad5f47b3effc3f08ed5739f48bc671ee6415b7f8560428c48d2ee12cf66f70c4.

- 2026-09-17T07:15:35+00:00: Recorded command exit 0; command argv SHA-256
  a7a2f6aa7ccac8f2f0a28af0ecd73b9218200bf9ca3364855714e6629ab7f648.

- 2026-09-17T07:16:00+00:00: Recorded command exit 0; command argv SHA-256
  1fe621021f432f3527d8d1a285759370986c899b0d4436b8342a23072e9c5ec9.

- 2026-09-17T07:16:21+00:00: Recorded command exit 0; command argv SHA-256
  9581b362f978b75783a138af2132c2427bd7ed9b49089ffdcf046a27856aa83d.
