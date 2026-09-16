---
{
  "branch": "feature/ar-1260-runtime-owned-strict-replay-integration",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T22:35:56+00:00",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1260",
  "next_action": "Run clippy -D warnings, rustdoc, policy/privacy/signature gates on exact head 9e4a1c0; then request independent review. Runtime native lifecycle/egress execution remains delegated to existing runtime tests and must not be claimed as CLI evidence.",
  "observed_branch": "feature/ar-1260-runtime-owned-strict-replay-integration",
  "observed_dirty": 0,
  "observed_head": "9e4a1c095e1f736011699edb4ab216e876e77251",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1260.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Integrate strict replay with runtime-owned attestation and supervised sandbox execution.",
  "task_revision": 29,
  "title": "Runtime-owned strict-replay integration",
  "updated_at": "2026-09-16T20:38:02+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1260-runtime"
}
---

## AR-1260

Implement the runtime-owned strict-replay handoff described in the plan. Preserve the reviewed
AR-1248 CLI contract and fail closed whenever runtime authority or supervised launch context is
missing, stale, duplicated, or mismatched.

- 2026-09-16T20:25:00+00:00: Created as the coordinator successor to AR-1248 after independent
  review confirmed that CLI-created readiness cannot replace runtime-issued namespace authority.

- 2026-09-16T20:27:04+00:00: Dependencies AR-1237, AR-1238, AR-1239 independently done; promote
  runtime-owned strict-replay integration.

- 2026-09-16T20:27:18+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-16T20:27:37+00:00: Recorded command exit 0; command argv SHA-256
  463a2b3478e4c4c507ddcb3a04a8ee990994c543356db5c621784f31dd43d354.

- 2026-09-16T20:28:20+00:00: Recorded command exit 0; command argv SHA-256
  df3f51288a439e254d63ec6692caf22033d5b5f9dbb9294e1c455f7eec83d16d.

- 2026-09-16T20:29:35+00:00: Recorded command exit 0; command argv SHA-256
  f489a19876782722ed16d09ca01ff72aa074415a2bb4183d7206b5819538e360.

- 2026-09-16T20:29:53+00:00: Recorded command exit 0; command argv SHA-256
  2fafaf13de7ad1f582cb78062779f8ef8b07c9c2aa001644a68701b7edb217cd.

- 2026-09-16T20:33:25+00:00: Heartbeat by asb_ar1024_lifecycle_router.

- 2026-09-16T20:33:57+00:00: Recorded command exit 0; command argv SHA-256
  f489a19876782722ed16d09ca01ff72aa074415a2bb4183d7206b5819538e360.

- 2026-09-16T20:34:08+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-16T20:34:21+00:00: Recorded command exit 0; command argv SHA-256
  bb6cf3f88c21a8e3c5ac53502ff0baafea79443106425bb6f51eeea82e75b985.

- 2026-09-16T20:34:30+00:00: Recorded command exit 0; command argv SHA-256
  70f41644d1eddef2d300c219a0492d66bebd04428bf28e2452bfc5b811c321eb.

- 2026-09-16T20:35:19+00:00: Recorded command exit 0; command argv SHA-256
  e65704d0af497ff4f9db656cbcc2e1894e552f84bfbc5a531f0945a250925adf.

- 2026-09-16T20:35:47+00:00: Signed 317a756 adds spawn_runtime_replay: runtime SandboxBackend,
  SandboxLaunchInput, ResourceLease, pinned supervisor/sidecar are required; deny policy, relay
  generation/path are checked before StrictReplayLaunchBridge::spawn, and RunningRuntimeReplay
  retains sidecar ownership. Focused asb-cli lib tests pass 76/76; cargo fmt --all -- --check
  passes; cargo test --workspace --locked --offline passes (exit 0, including native sandbox 11/11
  and schema/policy fixtures). Worktree clean.

- 2026-09-16T20:35:56+00:00: Heartbeat by asb_ar1024_lifecycle_router.

- 2026-09-16T20:36:36+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-16T20:36:50+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T20:37:00+00:00: Recorded command exit 0; command argv SHA-256
  f2fbf7f601f8cd667284e96c26e17212d9defb9b0f232227de7a06297380ec36.

- 2026-09-16T20:37:13+00:00: Recorded command exit 0; command argv SHA-256
  bb6cf3f88c21a8e3c5ac53502ff0baafea79443106425bb6f51eeea82e75b985.

- 2026-09-16T20:37:23+00:00: Recorded command exit 0; command argv SHA-256
  ab528c0548b21c47a8d72103202a48967d17e5c56e1156bc208322047859e6af.

- 2026-09-16T20:37:41+00:00: Signed 9e4a1c0 adds a direct no-fallback test: spawn_runtime_replay
  rejects a missing authenticated relay before child creation, with deny policy and runtime launch
  inputs otherwise valid. Focused test passes 1/1; cargo fmt passes. Product worktree is clean.

- 2026-09-16T20:38:02+00:00: Recorded command exit 0; command argv SHA-256
  3a905289a80a52faed087e37b801aaabb8129ad2f3b123eb6c22d2468ff04e5d.
