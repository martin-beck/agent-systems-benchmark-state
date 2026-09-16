---
{
  "branch": "feature/ar-1271-cassette-operation-contract",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T01:12:53+00:00",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1271",
  "next_action": "Add CLI adapter over RuntimeCassetteOperation with exact handle binding and real replay service request/response fixtures; then lifecycle/egress/no-fallback gates.",
  "observed_branch": "feature/ar-1271-cassette-operation-contract",
  "observed_dirty": 3,
  "observed_head": "af60454e00ba51ee384b85e2060b5957fbffa7e7",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1271.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Define a dependency-neutral cassette request/response operation contract.",
  "task_revision": 24,
  "title": "Dependency-neutral cassette operation contract",
  "updated_at": "2026-09-16T23:17:58+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1271-cassette-operation"
}
---
## AR-1271

Implement the shared cassette operation envelope needed for runtime-supervised strict replay.
Preserve AR-1270's blocked evidence and do not fabricate responses or authority.

- 2026-09-16T23:12:37+00:00: Dependencies are done; AR-1270 identified the missing
  dependency-neutral cassette request/response operation boundary.

- 2026-09-16T23:12:53+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-16T23:13:28+00:00: Recorded command exit 1; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T23:13:52+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T23:14:01+00:00: Recorded command exit 0; command argv SHA-256
  474ef19f4556278dcc77a99527fc880d499f620aa0c31805226d7b3f058f0232.

- 2026-09-16T23:14:17+00:00: Recorded command exit 0; command argv SHA-256
  9ff70cca28895297f2ace932096325353e27a41c95a05a144f3f011af9d5c9f6.

- 2026-09-16T23:14:28+00:00: Recorded command exit 0; command argv SHA-256
  d0958de777d136886944988d6dd52bebf6c24780633604e92f48bc2019752c3b.

- 2026-09-16T23:14:51+00:00: Signed checkpoint 2a04d51 adds dependency-neutral
  CassetteRequestV1/CassetteResponseV1 operation contract with version, generation, cassette/route
  identities, uppercase method, bounded body, status and response body fields, plus
  positive/negative validation tests. asb-core suite passes 18/18 and fmt pass; product tree clean.
  Initial fmt failed on malformed compact struct/enum delimiters in fresh file; corrected before
  green rerun. Runtime transport and actual CLI operation remain next.

- 2026-09-16T23:15:33+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T23:15:44+00:00: Recorded command exit 101; command argv SHA-256
  176cab5b29a40fa8794f09725ed51520aae1b944c519cabbe22bf8591c02577a.

- 2026-09-16T23:16:13+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T23:16:28+00:00: Recorded command exit 0; command argv SHA-256
  27d39a604a9b05a81c44b764ba09d60cf2b61c7a27e523f6fa49d6f4e78e7e37.

- 2026-09-16T23:16:45+00:00: Recorded command exit 0; command argv SHA-256
  6ba79e2f5f047fa129bc001399fe4d31cac276cd7ef43198579ac21575d11a49.

- 2026-09-16T23:16:55+00:00: Recorded command exit 0; command argv SHA-256
  82864b0b07ed4d1f69e9dbf1cf30537454e222b350e3cd53ac755b03f4930d21.

- 2026-09-16T23:17:16+00:00: Signed checkpoint af60454 adds RuntimeCassetteOperation over shared
  CassetteRequestV1/CassetteResponseV1 and ReplayServiceHandleV1. Runtime validates and
  identity-binds generation/cassette/route, consumes each request once, and validates bounded
  response envelopes without importing replay types. asb-core 18/18 and asb-runtime 39/39 pass; fmt
  pass; clean tree. CLI adapter and actual service invocation remain next.

- 2026-09-16T23:17:51+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.
