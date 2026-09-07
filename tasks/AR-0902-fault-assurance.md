---
{
  "branch": "feature/fault-assurance",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T03:52:33+00:00",
  "depends_on": [
    "AR-0103",
    "AR-0104",
    "AR-0503"
  ],
  "id": "AR-0902",
  "next_action": "Design bounded fuzz/fault targets in new owned paths and dedicated workflow; keep shared Cargo/schema and active agent paths untouched.",
  "observed_branch": "feature/fault-assurance",
  "observed_dirty": 0,
  "observed_head": "e85548d00cffcc3a014bfbc04b8fc79c5fe35da0",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-0902.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Stress parser, archive, path, recovery and cleanup boundaries with meaningful failure injection.",
  "task_revision": 8,
  "title": "Add fuzz mutation and lifecycle fault campaigns",
  "updated_at": "2026-09-07T01:52:33+00:00",
  "worktree_key": "agent-systems-benchmark-fault-assurance"
}
---
## AR-0902

Stress parser, archive, path, recovery and cleanup boundaries with meaningful failure injection.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-07T01:49:31+00:00: Coordinator verified AR-0103, AR-0104, and AR-0503 are durably done;
  AR-0902 fuzz/fault/scheduled-workflow paths are dependency-ready and disjoint from active AR-0801
  CLI, AR-0307 Goose registration/native workflow serialization, and AR-0308 mini-SWE isolated
  adapter work. Promotion authorizes only its declared bounded campaigns; shared workspace/schema
  changes remain coordinator-serialized.

- 2026-09-07T01:49:58+00:00: Claimed by contracts-20260906.

- 2026-09-07T01:50:14+00:00: Recorded command exit 0; command argv SHA-256
  9e6176fef0338084555f6e038c7a58f8f9d802b950b675780d3496a1eee59ccc.

- 2026-09-07T01:50:27+00:00: Claimed AR-0902 after signed+DCO promotion e04bdbb and created clean
  declared feature/fault-assurance worktree at exact product main e85548d. Exclusive fence before
  mutation: new fuzz targets, fault tests and a dedicated scheduled workflow only. No asb-cli paths,
  asb-agents/lib.rs, Goose or mini-SWE files; shared Cargo/workspace/schema remains
  coordinator-serialized. Workflow overlap must be acknowledged by AR-0307 before editing.

- 2026-09-07T01:51:28+00:00: AR-0307 owner confirmed no workflow overlap: AR-0902 exclusively owns
  new .github/workflows/fault-assurance.yml; verify.yml, quality.yml, formal.yml and all Goose paths
  remain excluded. Existing repository-policy/actionlint/zizmor expectations will be validated
  rather than changed without coordination.

- 2026-09-07T01:52:33+00:00: Heartbeat by contracts-20260906.
