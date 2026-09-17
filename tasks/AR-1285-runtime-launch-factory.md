---
{
  "branch": "feature/ar-1285-runtime-launch-factory",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T03:53:36+00:00",
  "depends_on": [
    "AR-1282",
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1285",
  "next_action": "Token binding fix is implemented in launch_factory.rs and sandbox.rs; focused launch_factory tests pass 5/5 including mismatched-context rejection. Commit signed/DCO, run locked full gates, force-with-lease push PR #209, then request re-review.",
  "observed_branch": "feature/ar-1285-runtime-launch-factory",
  "observed_dirty": 0,
  "observed_head": "0f876c7ae7fdfdff240a9fd3ad51e79cddaa4ffe",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1285.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide a runtime-owned launch factory for authenticated strict-replay CLI execution.",
  "task_revision": 85,
  "title": "Runtime-owned strict-replay launch factory",
  "updated_at": "2026-09-17T01:57:46+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1285-runtime-launch-factory"
}
---

## AR-1285

Define the narrow authority boundary missing from AR-1284: the runtime, not the primary CLI,
must issue the authenticated launch context used for strict replay. This AR does not claim the
complete supervised cassette lifecycle; it supplies a real runtime-owned factory and entrypoint
that a later lifecycle AR can consume.

### Scope

ASB repository only. Owned paths are runtime launch/context construction, the primary CLI handoff
boundary, and focused integration fixtures/tests. No asb-tui or renderer paths. Do not reuse blocked
AR-1260--AR-1284 branches.

### Acceptance

- A runtime-owned factory issues opaque, generation-bound launch authority containing validated
  `SandboxLaunchInput`, `ResourceLease`, and pinned supervisor/sidecar command identities.
- The primary strict-replay CLI consumes that authority and cannot construct equivalent authority,
  relay handles, namespace readiness, or fallback providers itself.
- Unknown, stale, forged, caller-constructed, malformed, and mismatched authority is rejected
  fail closed; positive issuance/consumption and privacy-safe negative fixtures are included.
- No credentials, private paths, ambient host data, unbounded subprocess output, or runtime downloads
  enter evidence. Focused/full locked gates, review, signed+DCO exact-head CI, merge, and post-merge
  verification are required.

If the complete supervised lifecycle remains unavailable, stop at this boundary and create a
separate successor rather than claiming strict-replay execution.

- 2026-09-17T01:28:07+00:00: AR-1284 identified missing runtime-owned launch factory; promote narrow
  successor

- 2026-09-17T01:28:19+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-17T01:30:21+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T01:30:37+00:00: Recorded command exit 101; command argv SHA-256
  3af3bc63cabdb1c0e0102f50b8dac571e856ed25d9ce7a7d217405801142bcad.

- 2026-09-17T01:31:00+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T01:31:09+00:00: Recorded command exit 101; command argv SHA-256
  3af3bc63cabdb1c0e0102f50b8dac571e856ed25d9ce7a7d217405801142bcad.

- 2026-09-17T01:31:26+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T01:31:36+00:00: Recorded command exit 0; command argv SHA-256
  3af3bc63cabdb1c0e0102f50b8dac571e856ed25d9ce7a7d217405801142bcad.

- 2026-09-17T01:32:22+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T01:32:33+00:00: Recorded command exit 0; command argv SHA-256
  3af3bc63cabdb1c0e0102f50b8dac571e856ed25d9ce7a7d217405801142bcad.

- 2026-09-17T01:32:56+00:00: Recorded command exit 0; command argv SHA-256
  36c571ad891aa3f703a376cee9ea11d1c6f71c532e6ba09b743b20cfa7d4d72e.

- 2026-09-17T01:33:17+00:00: Recorded command exit 101; command argv SHA-256
  1b8efcb7c82823972cc8c616eda54bc9aae13a47bd9eb65b61bbdf097b0b5fab.

- 2026-09-17T01:33:53+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T01:34:03+00:00: Recorded command exit 0; command argv SHA-256
  ff31f4ffe24441052986cef09779d85ba0fd8c05a8a3966eba27cd5067d55ec3.

- 2026-09-17T01:34:25+00:00: Recorded command exit 0; command argv SHA-256
  1b8efcb7c82823972cc8c616eda54bc9aae13a47bd9eb65b61bbdf097b0b5fab.

- 2026-09-17T01:35:04+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T01:35:13+00:00: Recorded command exit 0; command argv SHA-256
  3af3bc63cabdb1c0e0102f50b8dac571e856ed25d9ce7a7d217405801142bcad.

- 2026-09-17T01:36:09+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T01:36:19+00:00: Recorded command exit 0; command argv SHA-256
  3af3bc63cabdb1c0e0102f50b8dac571e856ed25d9ce7a7d217405801142bcad.

- 2026-09-17T01:36:29+00:00: Recorded command exit 0; command argv SHA-256
  1b8efcb7c82823972cc8c616eda54bc9aae13a47bd9eb65b61bbdf097b0b5fab.

- 2026-09-17T01:36:44+00:00: Recorded command exit 0; command argv SHA-256
  de46c2a21b03d012626a632c1249cfab00f697002e833b4c3a92a2814cd546fd.

- 2026-09-17T01:36:54+00:00: Recorded command exit 0; command argv SHA-256
  89be15a3887b3956416a1a2537e1603f33c63c42475d4576334d1d993b00fce0.

- 2026-09-17T01:37:12+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-17T01:37:32+00:00: Recorded command exit 0; command argv SHA-256
  9b498ebdee73cab471971c5dafbe261dc25698666e300cea3661fb0b83d17145.

- 2026-09-17T01:37:45+00:00: Recorded command exit 101; command argv SHA-256
  5c65734e6538cf9e4793a7b2544e7ef4effba6047efc156c8474d0017efc7be6.

- 2026-09-17T01:39:06+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T01:39:17+00:00: Recorded command exit 101; command argv SHA-256
  3af3bc63cabdb1c0e0102f50b8dac571e856ed25d9ce7a7d217405801142bcad.

- 2026-09-17T01:39:38+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T01:39:47+00:00: Recorded command exit 0; command argv SHA-256
  3af3bc63cabdb1c0e0102f50b8dac571e856ed25d9ce7a7d217405801142bcad.

- 2026-09-17T01:40:05+00:00: Recorded command exit 0; command argv SHA-256
  1b8efcb7c82823972cc8c616eda54bc9aae13a47bd9eb65b61bbdf097b0b5fab.

- 2026-09-17T01:40:17+00:00: Recorded command exit 0; command argv SHA-256
  9b498ebdee73cab471971c5dafbe261dc25698666e300cea3661fb0b83d17145.

- 2026-09-17T01:40:37+00:00: Recorded command exit 0; command argv SHA-256
  dc65132f1d61f337093f6ede1cf678df7ebb2457171b478e7529f4c7b5ffbf25.

- 2026-09-17T01:40:45+00:00: Recorded command exit 0; command argv SHA-256
  d44b795d1de26ddf7be05e2bcffd6677c261dc254c0e6d8e51a8859ec64e968c.

- 2026-09-17T01:41:03+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-17T01:41:15+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-17T01:41:47+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-17T01:42:25+00:00: Recorded command exit 101; command argv SHA-256
  ea80ab75f67abc17ba8e38c5dd19501691dbc4fd67697c54523ad9f414c35508.

- 2026-09-17T01:43:16+00:00: Recorded command exit 101; command argv SHA-256
  bcb6eee4361540de80d59f5346b6c23a71393e552d5e028517e748391e7fd604.

- 2026-09-17T01:43:32+00:00: Recorded command exit 0; command argv SHA-256
  4a5326aa2cb459771ed82437fe5bcbe3861b2e882be6c1ff8508b25c5e82bb6d.

- 2026-09-17T01:43:59+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-17T01:44:11+00:00: Recorded command exit 0; command argv SHA-256
  ef19043205064ea87bec66574bfe246191c9311bc8c404cd8e347d08fbdc44f0.

- 2026-09-17T01:44:35+00:00: Recorded command exit 0; command argv SHA-256
  bea304b3ec9ec6e2132aeb6fd6e9cb529c10b0ead0ff0182e9ace4f34301028d.

- 2026-09-17T01:44:43+00:00: Recorded command exit 0; command argv SHA-256
  7067713b5315d9cb13b94f48b3d2235baf7c77114f76462704596774d465e7c9.

- 2026-09-17T01:45:07+00:00: Signed checkpoints: 20bedf2 initial opaque authority, daba285 added
  runtime attestation token and cassette digest binding, 9fde4d8 updated the offline CLI workflow
  transcript/provenance to record argument-only replay rejection. Focused runtime launch_factory
  tests pass 4/4; CLI authority-required replay boundary test passes; clippy and fmt checks pass.
  Worktree clean at 9fde4d8.

- 2026-09-17T01:45:15+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-17T01:45:24+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-17T01:45:38+00:00: Recorded command exit 0; command argv SHA-256
  649e9e1ebfaf13c15c95c6360ca922c0b7c73a9a7fd2cf6943002779fca093b1.

- 2026-09-17T01:46:17+00:00: Recorded command exit 0; command argv SHA-256
  ea80ab75f67abc17ba8e38c5dd19501691dbc4fd67697c54523ad9f414c35508.

- 2026-09-17T01:46:48+00:00: Recorded command exit 101; command argv SHA-256
  5c8da9b34935360f7399b9d4b260d9a460b442f2f0ca08eddaee6e8f11776ef0.

- 2026-09-17T01:47:02+00:00: Recorded command exit 0; command argv SHA-256
  3f63f65f8ba8e74b2fa51b3565ca54317286ba2166dff21c137e09c65a44be20.

- 2026-09-17T01:47:18+00:00: Recorded command exit 0; command argv SHA-256
  51a195d9c53fdb19d10a5539ac8ff4114b8da8a4d85a50d658588c9b1cd11a72.

- 2026-09-17T01:47:33+00:00: Recorded command exit 0; command argv SHA-256
  1c4aafd2e66e0c5ef7f4527dab971ff1286ec76cabc073ce635539aaaa70e25a.

- 2026-09-17T01:47:46+00:00: Recorded command exit 0; command argv SHA-256
  eb673f06db590ac863081e8a24b66e6363a9602cc9287f1054fb37fe86d8af8f.

- 2026-09-17T01:48:32+00:00: Recorded command exit 0; command argv SHA-256
  ea80ab75f67abc17ba8e38c5dd19501691dbc4fd67697c54523ad9f414c35508.

- 2026-09-17T01:48:41+00:00: Recorded command exit 0; command argv SHA-256
  3fbcfd18f9c19d92d7ebca58b477c48d9aa165c29e609f9fb94679ea2519eb3c.

- 2026-09-17T01:48:57+00:00: Recorded command exit 0; command argv SHA-256
  b8f21b23107b0a2a84b42da15b14dba927f7536b2cd6e558f6d36c8d21a3b197.

- 2026-09-17T01:49:21+00:00: Recorded command exit 0; command argv SHA-256
  da580d8d7b6e5b449a7500f33db0bf140ac6f80c8e70d2b73004f2d27241c2d0.

- 2026-09-17T01:49:44+00:00: Published PR #209:
  https://github.com/martin-beck/agent-systems-benchmark/pull/209, base main, exact head
  9fde4d8a6ff1c820fbfa4fc0214c1e36ea7f86d5. Signed commits 20bedf2, daba285, 9fde4d8. Authority
  boundary binds runtime attestation token, validated SandboxLaunchInput/benchmark ResourceLease,
  relay generation/route and pinned sidecar/adapter/supervisor digests; CLI replay rejects missing
  or cassette-mismatched authority. Focused runtime 4/4 and CLI authority-required test pass. fmt,
  workspace clippy, rustdoc, full locked workspace tests pass; formal locked tests pass after one
  isolated Text file busy race (rerun passed); repository policy/signature tests and portability
  manifest validation pass. PR scope excludes supervised cassette lifecycle and asb-tui.

- 2026-09-17T01:49:52+00:00: Recorded command exit 0; command argv SHA-256
  981c8a0ac8bee9b43044f995879acca58b2f6df2f19507aec8117225dc104ad7.

- 2026-09-17T01:50:14+00:00: Verified hosted publication through gh via handoffctl: PR #209 OPEN,
  base main, head feature/ar-1285-runtime-launch-factory, head OID
  9fde4d8a6ff1c820fbfa4fc0214c1e36ea7f86d5. Required checks started at 01:49:25Z: Rust, Repository
  quality, Formal assurance, Fault assurance, Emulated AArch64, Platform evidence; header and AWQ
  shadow checks already SUCCESS. No merge requested.

- 2026-09-17T01:53:36+00:00: Heartbeat by asb_ar1024_lifecycle_router.

- 2026-09-17T01:54:57+00:00: Recorded command exit 1; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T01:55:25+00:00: Recorded command exit 0; command argv SHA-256
  5aef6359fe19c1c029e156b03ef5e2c60dc4369548d3ba378e563862ff9be31e.

- 2026-09-17T01:55:38+00:00: Recorded command exit 0; command argv SHA-256
  857f990d5ceba0b79266ac4f90d4a539844b74fffcead193ea586341b22552ff.

- 2026-09-17T01:56:06+00:00: Recorded command exit 0; command argv SHA-256
  5aef6359fe19c1c029e156b03ef5e2c60dc4369548d3ba378e563862ff9be31e.

- 2026-09-17T01:56:17+00:00: Recorded command exit 0; command argv SHA-256
  857f990d5ceba0b79266ac4f90d4a539844b74fffcead193ea586341b22552ff.

- 2026-09-17T01:56:37+00:00: Review blocker diagnosed: RuntimeLaunchToken previously carried only a
  nonce and could be reused with a different launch context. Added SHA-256 binding over cassette,
  program/args/env, lease class/CPUs, relay handoff, supervisor generation/relay/route and pinned
  command digests; attestation now receives input/lease/cassette and derives this binding. Focused
  runtime suite passes 5/5. Prior exit-1 was the expected handoffctl cargo-fmt cwd/manifest
  invocation failure; rerun with explicit worktree manifest succeeded.

- 2026-09-17T01:57:02+00:00: Recorded command exit 0; command argv SHA-256
  5aef6359fe19c1c029e156b03ef5e2c60dc4369548d3ba378e563862ff9be31e.

- 2026-09-17T01:57:12+00:00: Recorded command exit 0; command argv SHA-256
  857f990d5ceba0b79266ac4f90d4a539844b74fffcead193ea586341b22552ff.

- 2026-09-17T01:57:21+00:00: Recorded command exit 128; command argv SHA-256
  e8c0644b827097cfd0874df38fc3bc648a7b8b12ea8a93200a3c7856d47a83b4.

- 2026-09-17T01:57:30+00:00: Recorded command exit 0; command argv SHA-256
  4628de517f9cb4fd34df6ef57c041e0565394d04dd3bbb18a4812cd68bfb5ce8.

- 2026-09-17T01:57:38+00:00: Recorded command exit 0; command argv SHA-256
  e7360949a1a7f8ce8fc06fb9ba8b97f2064f527e4d374c80eaf780ace78efb3e.
