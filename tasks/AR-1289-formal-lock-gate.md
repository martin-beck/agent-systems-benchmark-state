---
{
  "branch": "fix/ar-1289-formal-lock-gate",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T05:13:50+00:00",
  "depends_on": [],
  "id": "AR-1289",
  "next_action": "Promote and claim; reproduce formal/Cargo.lock failure on protected main, determine exact lock drift, and repair the smallest ASB formal gate scope.",
  "observed_branch": "fix/ar-1289-formal-lock-gate",
  "observed_dirty": 0,
  "observed_head": "2fd90557a4e7be32fab590f47bc501462127c1c1",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1289.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair the stale formal Cargo.lock required by hosted exact-head gates.",
  "task_revision": 9,
  "title": "Repair formal lock gate",
  "updated_at": "2026-09-17T03:14:24+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1289-formal-lock-gate"
}
---

## AR-1289

The required formal workflow currently fails before model tests because `formal/Cargo.lock` cannot
be used with `--locked`. Repair and verify this gate independently of feature ARs.

- 2026-09-17T03:12:39+00:00: Hosted exact-head formal job fails because formal/Cargo.lock is stale
  under --locked; repair independently of certificate feature.

- 2026-09-17T03:13:06+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-17T03:13:22+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-09-17T03:13:31+00:00: Recorded command exit 0; command argv SHA-256
  d0f0b52a0a5d46ebd4657c74ecbcbb904e0df02a72c4b192d4e9d74ecd6c4182.

- 2026-09-17T03:13:50+00:00: Heartbeat by asb_ar1024_lifecycle_router.

- 2026-09-17T03:14:06+00:00: Recorded command exit 101; command argv SHA-256
  7a92628b9c4db3b74a33f295f28b9b6f3786588dca51c09e12ba3282f2d2a9a2.

- 2026-09-17T03:14:24+00:00: Recorded command exit 0; command argv SHA-256
  fd4fe86de1f65ae1bf0c3c1dd2bf5e9211b2f05e99214a0f2b49ebabaae38d5b.
