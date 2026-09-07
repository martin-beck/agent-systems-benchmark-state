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
  "observed_dirty": 5,
  "observed_head": "e85548d00cffcc3a014bfbc04b8fc79c5fe35da0",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-0902.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Stress parser, archive, path, recovery and cleanup boundaries with meaningful failure injection.",
  "task_revision": 22,
  "title": "Add fuzz mutation and lifecycle fault campaigns",
  "updated_at": "2026-09-07T02:08:26+00:00",
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

- 2026-09-07T01:54:46+00:00: Recorded command exit 0; command argv SHA-256
  458bab1b2166e0c145e1674942cae2bdd6cf91d78845fb9d62e3590af76f5681.

- 2026-09-07T01:55:07+00:00: Pinned cargo-fuzz 0.13.2 and cargo-mutants 27.1.0 installed
  successfully under /srv/data/projects/.asb-local/fault-tools through the AR wrapper without
  product-tree changes. A first evidence update invocation failed before mutation because update
  requires --expected-revision; corrected against fresh revision 9.

- 2026-09-07T02:03:47+00:00: Recorded command exit 0; command argv SHA-256
  6366629e62d3a7812026aa8926be8bb8fe27edc9b527575265acdd5bf1b754e2.

- 2026-09-07T02:04:00+00:00: Recorded command exit 101; command argv SHA-256
  5459c696e63d376e29c37e46169c5c1d8954e160487694704f8e21270cb889c0.

- 2026-09-07T02:04:11+00:00: Recorded command exit 0; command argv SHA-256
  89caf2d75d72f38a4ec90a6a9fc78b32c561ef3334d780682428eeecbe409920.

- 2026-09-07T02:04:35+00:00: Recorded command exit 101; command argv SHA-256
  5459c696e63d376e29c37e46169c5c1d8954e160487694704f8e21270cb889c0.

- 2026-09-07T02:05:17+00:00: Recorded command exit 0; command argv SHA-256
  53ca6d565a568971b812cde415b02e94c4953fb03601aa0996038cc0c6e4d07d.

- 2026-09-07T02:05:26+00:00: Recorded command exit 0; command argv SHA-256
  9e1abd45fe789d7a35901c61696bcef281f5d623d0c9b5556f78a5d654630d64.

- 2026-09-07T02:06:45+00:00: Recorded command exit 0; command argv SHA-256
  a50d1dd085e1cee41f06f6fb6c140298b95c49cf853d272eb5a7232f9f4b418d.

- 2026-09-07T02:07:41+00:00: Recorded command exit 0; command argv SHA-256
  d618142e53613401f51c15787bc8a24729b562ac3df10911391b0b03e5066e27.

- 2026-09-07T02:08:26+00:00: Recorded command exit 0; command argv SHA-256
  8379ea8a2ca088a8dd1804adfae4b72508177533d28de690dc3856acab8005f7.
