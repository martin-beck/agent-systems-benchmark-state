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
  "task_revision": 5,
  "title": "Task schema and metadata consistency",
  "updated_at": "2026-09-17T05:29:29+00:00",
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
