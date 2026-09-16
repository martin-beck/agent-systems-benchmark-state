---
{
  "branch": "feature/ar-1262-runtime-owned-launch-authority",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T23:04:53+00:00",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1262",
  "next_action": "Add direct consumer tests proving authority-backed bridge spawn rejects stale/duplicate/route-digest inputs and retains sidecar through terminal cleanup; then run full gates.",
  "observed_branch": "feature/ar-1262-runtime-owned-launch-authority",
  "observed_dirty": 0,
  "observed_head": "3723fb9b9666bf67139e292c16891e96b3dc2f97",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1262.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Issue runtime-owned authority for supervised strict-replay execution.",
  "task_revision": 34,
  "title": "Runtime-owned strict-replay launch authority",
  "updated_at": "2026-09-16T21:09:12+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1262-runtime-authority"
}
---

## AR-1262

Implement the runtime authority issuer and CLI consumer integration while preserving fail-closed
ownership and bounded lifecycle evidence.

- 2026-09-16T20:58:00+00:00: Created after independent review of AR-1261 confirmed that
  composing runtime authority atomically is required before CLI replay can safely launch.

- 2026-09-16T20:57:39+00:00: Dependencies AR-1237/1238/1239 done; promote runtime-owned launch
  authority successor.

- 2026-09-16T20:57:58+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-16T20:58:45+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T20:58:56+00:00: Recorded command exit 101; command argv SHA-256
  0f9b829a5377a353eea4e06963cc7ee8469fd1884d0955572b76031346c29fd6.

- 2026-09-16T20:59:25+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T20:59:35+00:00: Recorded command exit 0; command argv SHA-256
  0f9b829a5377a353eea4e06963cc7ee8469fd1884d0955572b76031346c29fd6.

- 2026-09-16T20:59:49+00:00: Recorded command exit 0; command argv SHA-256
  1fd26a558e8ddc9805f77c8e5bd0be22c3406605621b83c467722874ebf64fa1.

- 2026-09-16T20:59:58+00:00: Recorded command exit 0; command argv SHA-256
  1d12e96d0f184ea4c43f11299fda3d9ed2ea9f01b32dfe4cf8a4b02e517041b1.

- 2026-09-16T21:00:16+00:00: Signed f691aad adds crates/asb-runtime/src/replay_entrypoint.rs and
  export. ReplayLaunchAuthority issues a validated runtime SidecarHandoff only after namespace
  attestation, retains LoopbackSidecar ownership, and take_once rejects duplicate consumption.
  Focused runtime test passes 1/1; cargo fmt passes; product worktree clean. Initial focused test
  failure was only missing tempfile dev dependency; replaced with bounded std temp root and reran
  green.

- 2026-09-16T21:04:53+00:00: Heartbeat by asb_ar1024_lifecycle_router.

- 2026-09-16T21:05:34+00:00: Recorded command exit 1; command argv SHA-256
  31d26d709d6bb7f1ba84e372fec371f5b93205ddebd7b8d513c9414718061c58.

- 2026-09-16T21:06:03+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T21:06:14+00:00: Recorded command exit 0; command argv SHA-256
  0f9b829a5377a353eea4e06963cc7ee8469fd1884d0955572b76031346c29fd6.

- 2026-09-16T21:06:34+00:00: Recorded command exit 101; command argv SHA-256
  f489a19876782722ed16d09ca01ff72aa074415a2bb4183d7206b5819538e360.

- 2026-09-16T21:06:54+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T21:07:08+00:00: Recorded command exit 0; command argv SHA-256
  f2fbf7f601f8cd667284e96c26e17212d9defb9b0f232227de7a06297380ec36.

- 2026-09-16T21:07:18+00:00: Recorded command exit 0; command argv SHA-256
  fc7fdc918a03f1dc0c713ae6e37e9e7bdd797e02cb27cc93d65fc407db2aef64.

- 2026-09-16T21:07:27+00:00: Recorded command exit 0; command argv SHA-256
  76ca42ba2142d92f0e3c572e909ff46f0ceac6a3806bce9f43a75729c6442f54.

- 2026-09-16T21:07:50+00:00: Signed 007d91d integrates ReplayLaunchAuthority into CLI
  replay_contract: take_launch atomically transfers authenticated handoff, sidecar, backend, launch
  input, lease, and pinned supervisor/sidecar commands; spawn_authorized_replay validates relay
  generation/path and invokes StrictReplayLaunchBridge::spawn. Focused runtime authority test 1/1
  and CLI no-fallback test 1/1 pass; fmt passes. Prior exit-101 was diagnosed as tuple-vs-struct
  resolve_and_bind_runtime mismatch and fixed. Product worktree clean.

- 2026-09-16T21:08:03+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-16T21:08:19+00:00: Recorded command exit 101; command argv SHA-256
  3a905289a80a52faed087e37b801aaabb8129ad2f3b123eb6c22d2468ff04e5d.

- 2026-09-16T21:08:33+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T21:08:48+00:00: Recorded command exit 0; command argv SHA-256
  1a9bf1c057b2db85c3008a7f3844c0ca6a4ee5773ccc48513caa37e3dc22f3a4.

- 2026-09-16T21:08:56+00:00: Recorded command exit 0; command argv SHA-256
  ac07eea5030a5ba4c97a7d01a9a067e8eecfcc171c6cc7530691e9f9ff735616.

- 2026-09-16T21:09:05+00:00: Recorded command exit 0; command argv SHA-256
  5a172d7709e43af3a1577586c584d2ae883a46d7b5cedc3b8fefc0cd45a16faf.
