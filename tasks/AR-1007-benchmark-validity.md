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
  "observed_dirty": 6,
  "observed_head": "20ac1e507e678aff463ec5f6c7b37cfcd67a5ad0",
  "owner": "replay_20260906",
  "plan": "../plans/AR-1007.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Track dataset provenance, contamination risk, grader validity and native portability per workload revision.",
  "task_revision": 14,
  "title": "Maintain benchmark validity and portability registry",
  "updated_at": "2026-09-07T23:41:29+00:00",
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

- 2026-09-07T23:28:47+00:00: Recorded command exit 0; command argv SHA-256
  b3e29f2cbb6733a2838ea852d7ac6731d92ff49a5716b40ba590735d6a73ebae.

- 2026-09-07T23:37:36+00:00: Changed conclusion: the initial isolated source patch was applied by
  the workspace edit tool before the handoffctl wrapper instead of through the required wrapper.
  Exact affected paths are crates/asb-workloads/Cargo.toml, src/lib.rs, src/validity.rs, and
  examples/generate_validity_schema.rs; no build, Git, publication, network, or external effect
  occurred. Preserve and audit these effects; all subsequent product/build/test/Git mutations use
  handoffctl run.

- 2026-09-07T23:39:58+00:00: Recorded command exit 0; command argv SHA-256
  5f1114104d3919f72ee746fc7bea36de9b7fd8369650f9ab250d692d5ebc4bd2.

- 2026-09-07T23:40:12+00:00: Recorded command exit 127; command argv SHA-256
  19732f767eebd6a6e1839f95999f2ca1f0db3789500883e5d8dae5d8be4e8cfc.

- 2026-09-07T23:40:57+00:00: Recorded command exit 0; command argv SHA-256
  d80be3a7a0c3d33c85bb5705bf448503c1341ebce6352bdb0c8e8ac3800764b4.

- 2026-09-07T23:41:29+00:00: Recorded command exit 101; command argv SHA-256
  f4c9f5870426327d3cb87263d8d31031f4dd658fbc9a8139bcc19f8d99fe0442.
