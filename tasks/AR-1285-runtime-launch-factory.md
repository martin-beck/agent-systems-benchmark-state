---
{
  "branch": "feature/ar-1285-runtime-launch-factory",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T03:28:19+00:00",
  "depends_on": [
    "AR-1282",
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1285",
  "next_action": "Promote after dependency verification; implement an opaque runtime-owned launch factory and CLI entrypoint boundary.",
  "observed_branch": "feature/ar-1285-runtime-launch-factory",
  "observed_dirty": 3,
  "observed_head": "daba285cdc61b0f2c23be89ef1254b180e58c350",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1285.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide a runtime-owned launch factory for authenticated strict-replay CLI execution.",
  "task_revision": 50,
  "title": "Runtime-owned strict-replay launch factory",
  "updated_at": "2026-09-17T01:44:07+00:00",
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
