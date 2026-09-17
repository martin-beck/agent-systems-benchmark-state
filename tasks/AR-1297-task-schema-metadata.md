---
{
  "branch": "repair/ar-1297-task-schema-metadata",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T07:28:11+00:00",
  "depends_on": [],
  "id": "AR-1297",
  "next_action": "Repair every reported task schema/metadata error from durable evidence, add strict superseded_by schema coverage, regenerate views, and rerun all state gates.",
  "observed_branch": "repair/ar-1297-task-schema-metadata",
  "observed_dirty": 0,
  "observed_head": "98acd6d5f5a206b351a54689e7817dd43af406ca",
  "owner": "asb-ar1297-metadata",
  "plan": "../plans/AR-1297.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair task schema and metadata consistency without weakening coordinator validation.",
  "task_revision": 18,
  "title": "Task schema and metadata consistency",
  "updated_at": "2026-09-17T05:33:05+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1297-task-schema"
}
---

## AR-1297

AR-1296 exposed repository-wide schema failures in historical task metadata.
This AR owns only evidence-based task metadata and the versioned schema/test
contract. It must not relax validation, fabricate provenance, touch product or
asb-tui source, modify handoffctl implementation, or alter formal gates.

- 2026-09-17T05:27:58+00:00: Repository-wide schema failures are evidence-based metadata defects;
  promote strict normalization without weakening validation.

- 2026-09-17T05:28:11+00:00: Claimed by asb-ar1297-metadata.

- 2026-09-17T05:28:22+00:00: Recorded command exit 1; command argv SHA-256
  384a63992d15fbbc43a1690b017ee5f7bb89c0ecc9cc5540a5a1fa014c0dee17.

- 2026-09-17T05:29:29+00:00: Recorded command exit 0; command argv SHA-256
  af8d44f272b9296984eb51b1c82b5322671e72c002fe3017298a658c15644ac3.

- 2026-09-17T05:29:45+00:00: Recorded command exit 0; command argv SHA-256
  35208a4967ac6178ddeb78494fd81b501e28969a2519171895d1022836645b6f.

- 2026-09-17T05:29:59+00:00: Recorded command exit 0; command argv SHA-256
  384a63992d15fbbc43a1690b017ee5f7bb89c0ecc9cc5540a5a1fa014c0dee17.

- 2026-09-17T05:30:16+00:00: Recorded command exit 0; command argv SHA-256
  5fee026f8e9a7f506fee8acb40e6d7ba17ca1871cd06c4470eab260e3070f672.

- 2026-09-17T05:30:24+00:00: Recorded command exit 0; command argv SHA-256
  57aa684661b9badaf5caf256706c0ff03f2aa97681862aa8ba378effbed4e08c.

- 2026-09-17T05:30:33+00:00: Recorded command exit 0; command argv SHA-256
  b39a86595fdff2d53bb611c0b0ba124d1b7628a3cd61c31f0af8283fc7e6cce7.

- 2026-09-17T05:31:15+00:00: Recorded command exit 1; command argv SHA-256
  d7d69bb73d4c5faec99d910b9d794900b9c78f2c2eefdb01f20719f809393f83.

- 2026-09-17T05:31:24+00:00: Recorded command exit 0; command argv SHA-256
  1f7046dcd849643446879b9eb1d2a1bb4964a18a6708855b5a9773043edd0fc5.

- 2026-09-17T05:31:33+00:00: Recorded command exit 0; command argv SHA-256
  cb32aba10be4d5137422b2b1511c1ca1522efbc213c74d3a3a2fa756678f4e3c.

- 2026-09-17T05:31:42+00:00: Recorded command exit 0; command argv SHA-256
  cb32aba10be4d5137422b2b1511c1ca1522efbc213c74d3a3a2fa756678f4e3c.

- 2026-09-17T05:32:02+00:00: Recorded command exit 0; command argv SHA-256
  d7d69bb73d4c5faec99d910b9d794900b9c78f2c2eefdb01f20719f809393f83.

- 2026-09-17T05:32:11+00:00: Recorded command exit 0; command argv SHA-256
  cb32aba10be4d5137422b2b1511c1ca1522efbc213c74d3a3a2fa756678f4e3c.

- 2026-09-17T05:32:56+00:00: Recorded command exit 0; command argv SHA-256
  6a1251ccda4090eff34a63f3ea5e5418519e76d435752ea8b751486f1e90028e.

- 2026-09-17T05:33:05+00:00: Recorded command exit 0; command argv SHA-256
  b7c2984c8722b6f2b56d0c6a25131a8ca79ed6bdfddab0b1991edccc7c9aeab0.
