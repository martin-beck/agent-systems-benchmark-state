---
{
  "branch": "feature/ar-1272-authenticated-cassette-backend",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T01:20:45+00:00",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1272",
  "next_action": "Bind RuntimeCassetteContent into CLI decoding and actual replay command; prove response parity, egress/no-fallback, cancellation/restart, timeout/crash cleanup.",
  "observed_branch": "feature/ar-1272-authenticated-cassette-backend",
  "observed_dirty": 0,
  "observed_head": "9328e4fa906b919d0dbca6c5b557bf1d00ed6f8a",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1272.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Bind immutable cassette content to a runtime-authenticated replay backend handle.",
  "task_revision": 21,
  "title": "Authenticated immutable cassette backend",
  "updated_at": "2026-09-16T23:25:19+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1272-cassette-backend"
}
---
## AR-1272

Implement the runtime-authenticated immutable cassette backend required for real strict-replay
execution. Preserve AR-1271's blocked evidence and do not accept caller-supplied cassette bytes or
paths as authority.

- 2026-09-16T23:20:28+00:00: Dependencies are done; AR-1271 proves immutable cassette content must
  be runtime-authenticated before real replay execution.

- 2026-09-16T23:20:45+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-16T23:21:19+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T23:21:30+00:00: Recorded command exit 101; command argv SHA-256
  474ef19f4556278dcc77a99527fc880d499f620aa0c31805226d7b3f058f0232.

- 2026-09-16T23:21:56+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T23:22:05+00:00: Recorded command exit 0; command argv SHA-256
  474ef19f4556278dcc77a99527fc880d499f620aa0c31805226d7b3f058f0232.

- 2026-09-16T23:22:14+00:00: Recorded command exit 0; command argv SHA-256
  ab16a93c8e5bfcf7484bb3fc451bee42c6092d9a711b42c51e59638f5caa7034.

- 2026-09-16T23:22:24+00:00: Recorded command exit 0; command argv SHA-256
  375ef5fde325e7d90fd05af238d4ed1e14366dbb1fe80d3479bc9e4725bee98e.

- 2026-09-16T23:22:50+00:00: Signed checkpoint d7d17b7 adds dependency-neutral CassetteContentRefV1
  with schema/generation/sha256/exact-size validation, path-free identities, 16 MiB bound, and
  positive/negative tests. asb-core suite passes 18/18; fmt pass; product tree clean. Initial test
  failure accepted /tmp-like generation because allowed-character validation was absent; fixed by
  restricting generation to bounded alphanumeric/dot/underscore/dash and reran green. Runtime
  content handle and real supervised CLI replay remain next.

- 2026-09-16T23:23:39+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T23:23:53+00:00: Recorded command exit 0; command argv SHA-256
  176cab5b29a40fa8794f09725ed51520aae1b944c519cabbe22bf8591c02577a.

- 2026-09-16T23:24:11+00:00: Recorded command exit 0; command argv SHA-256
  9fff9be7528a728c2691ffa25f75aa4d136970cc17fbc56dc6906b16f63c61ad.

- 2026-09-16T23:24:22+00:00: Recorded command exit 0; command argv SHA-256
  d1501acf0be91ca30596f5d4b48cc7811d2a775fd8669a241b7ae8fd204a7aed.

- 2026-09-16T23:24:44+00:00: Signed checkpoint 9328e4f adds RuntimeCassetteContent: runtime-owned
  immutable bytes are validated against CassetteContentRefV1 exact size and SHA-256, then consumed
  exactly once. Runtime remains dependency-neutral (bytes only), while CLI can decode after
  authenticated transfer. Runtime suite passes 39/39 and fmt pass; clean tree. CLI decoding and real
  supervised fixtures remain next.

- 2026-09-16T23:25:19+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.
