---
{
  "branch": "feature/ar-1270-runtime-cassette-handle",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T01:05:11+00:00",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1270",
  "next_action": "Implement runtime-owned handle issuance/one-shot consumption and bind CLI replay service; add real request/response and lifecycle/egress fixtures.",
  "observed_branch": "feature/ar-1270-runtime-cassette-handle",
  "observed_dirty": 4,
  "observed_head": "473d715aae490ec4c8a461cabf8bd8b00744090d",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1270.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide a runtime-issued cassette-service handle for supervised strict replay.",
  "task_revision": 17,
  "title": "Runtime-issued cassette-service handle",
  "updated_at": "2026-09-16T23:08:26+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1270-runtime-cassette-handle"
}
---
## AR-1270

Implement the dependency-neutral runtime-issued cassette-service handle required for real supervised
strict replay. Preserve AR-1269's authority evidence and blocker; do not move service authority into
the CLI.

- 2026-09-16T23:04:53+00:00: Dependencies are done; AR-1269 proves a runtime-issued cassette-service
  handle is required to execute real traffic without a crate cycle.

- 2026-09-16T23:05:11+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-16T23:06:03+00:00: Recorded command exit 1; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T23:06:28+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T23:06:37+00:00: Recorded command exit 0; command argv SHA-256
  474ef19f4556278dcc77a99527fc880d499f620aa0c31805226d7b3f058f0232.

- 2026-09-16T23:06:45+00:00: Recorded command exit 0; command argv SHA-256
  e2fb60616251de3c6a4e6e92438ad67c476f5e0b781bc63dfddfcae0764dadac.

- 2026-09-16T23:06:54+00:00: Recorded command exit 0; command argv SHA-256
  b2f9e212755ac21a94c2e70304dae6e0ecd4a23b2b136fccacd3cc432713dcde.

- 2026-09-16T23:07:19+00:00: Signed checkpoint 473d715 adds dependency-neutral asb-core
  ReplayServiceHandleV1 with bounded generation/cassette/route identity validation and
  positive/negative tests. asb-core suite passes 17/17 and fmt pass; product tree clean. Initial fmt
  command failed due malformed one-line enum delimiter in fresh file; corrected syntax before green
  rerun. Runtime issuance, CLI binding, and supervised cassette lifecycle remain next.

- 2026-09-16T23:07:54+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T23:08:07+00:00: Recorded command exit 0; command argv SHA-256
  176cab5b29a40fa8794f09725ed51520aae1b944c519cabbe22bf8591c02577a.

- 2026-09-16T23:08:18+00:00: Recorded command exit 0; command argv SHA-256
  59aa510e68afe1bc36106a5a99894e17959af68fd75bd1eee7a79d4365452252.

- 2026-09-16T23:08:26+00:00: Recorded command exit 0; command argv SHA-256
  79c29fb7b20bb0556f0c2b066e557f686d0ed8346b4b2cf2e59452aeff952747.
