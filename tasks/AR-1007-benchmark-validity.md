---
{
  "branch": "feature/benchmark-validity",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T02:27:10+00:00",
  "depends_on": [
    "AR-0401",
    "AR-0701",
    "AR-1001"
  ],
  "id": "AR-1007",
  "next_action": "Implement registry schema and validation for built-in and imported workloads.",
  "observed_branch": "feature/benchmark-validity",
  "observed_dirty": 0,
  "observed_head": "20ac1e507e678aff463ec5f6c7b37cfcd67a5ad0",
  "owner": "replay_20260906",
  "plan": "../plans/AR-1007.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Track dataset provenance, contamination risk, grader validity and native portability per workload revision.",
  "task_revision": 5,
  "title": "Maintain benchmark validity and portability registry",
  "updated_at": "2026-09-07T23:27:52+00:00",
  "worktree_key": "agent-systems-benchmark-benchmark-validity"
}
---
## AR-1007

Track dataset provenance, contamination risk, grader validity and native portability per workload revision.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-07T23:27:08+00:00: Dependencies AR-0401, AR-0701, and AR-1001 are durably done. Selected
  highest-priority dependency-ready leaf; workload registry/provenance scope is disjoint from active
  AR-0505 replay integration, AR-0840 frontend protocol, and AR-0848 native capacity. Declared
  branch, worktree, and remote ref are absent.

- 2026-09-07T23:27:10+00:00: Claimed by replay_20260906.

- 2026-09-07T23:27:52+00:00: Recorded command exit 0; command argv SHA-256
  f8e83446a4a364c5e265648164c1fcc18c0b30e0b72c156dcc3049075b0574af.
