---
{
  "branch": "feature/ar-1356-control-runtime-attestation-primitive",
  "checkpoint_commit": "70f8a3980cb0ed81bfdcb8a203f953467e319a11",
  "claim_expires": "2026-09-23T23:06:43+00:00",
  "depends_on": [
    "AR-1352"
  ],
  "id": "AR-1356",
  "next_action": "Independent review complete; local fmt check, clippy -D warnings, locked workspace tests and doc tests pass. Product commit 70f8a39 is signed+DCO and authority constructors remain private. Publish exact-head PR through coordinator workflow, require all hosted checks and post-merge workflows before release; then advance AR-1355.",
  "observed_branch": "feature/ar-1356-control-runtime-attestation-primitive",
  "observed_dirty": 1,
  "observed_head": "70f8a3980cb0ed81bfdcb8a203f953467e319a11",
  "owner": "codex-asb-runtime-acquisition-successor-luna56",
  "plan": "../plans/AR-1356-control-runtime-attestation-primitive.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Issue runtime-owned live enrollment capability from authenticated control attestation.",
  "task_revision": 36,
  "title": "Control/runtime enrollment attestation primitive",
  "updated_at": "2026-09-23T21:21:07+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1356-control-runtime-attestation-primitive"
}
---

Successor for AR-1355's missing trust primitive. Preserve fail-closed live
dispatch and do not expose caller-supplied launch authority.

- 2026-09-23T21:06:04+00:00: Promote P0 authenticated control/runtime attestation primitive; AR-1355
  documented missing issuer and remains blocked, AR-1329 fail-closed.

- 2026-09-23T21:06:07+00:00: Claimed by codex-asb-runtime-acquisition-successor-luna56.

- 2026-09-23T21:06:43+00:00: Heartbeat by codex-asb-runtime-acquisition-successor-luna56.

- 2026-09-23T21:06:46+00:00: Recorded command exit 0; command argv SHA-256
  e332b91f34b085dd45defe28161e068116b95dc7edbf8ccdf38cfe0761a84e84.

- 2026-09-23T21:07:53+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-23T21:08:07+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T21:08:20+00:00: Recorded command exit 101; command argv SHA-256
  a37d35e290b63ddfe8627f9bdb0474ef6d3f2654ade91f05cd9a55c3a713fceb.

- 2026-09-23T21:08:45+00:00: Recorded command exit 101; command argv SHA-256
  b2260c0b3d96b0ac197158d331e06c29c1209605d3dd985adf153e7fad0ecd31.

- 2026-09-23T21:08:59+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T21:09:13+00:00: Recorded command exit 101; command argv SHA-256
  b2260c0b3d96b0ac197158d331e06c29c1209605d3dd985adf153e7fad0ecd31.

- 2026-09-23T21:09:30+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T21:09:46+00:00: Recorded command exit 0; command argv SHA-256
  b2260c0b3d96b0ac197158d331e06c29c1209605d3dd985adf153e7fad0ecd31.

- 2026-09-23T21:10:12+00:00: Recorded command exit 101; command argv SHA-256
  2110a9961676b5ccc0a82d200c7e3d885d67ce7fb4c0abef421c6af81264370b.

- 2026-09-23T21:10:26+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T21:10:40+00:00: Recorded command exit 0; command argv SHA-256
  2110a9961676b5ccc0a82d200c7e3d885d67ce7fb4c0abef421c6af81264370b.

- 2026-09-23T21:10:55+00:00: Recorded command exit 0; command argv SHA-256
  f0912fec02bbfbc42de1e594c33ee31d8ec9d79fcc3b6f466605c3b8b3d45f20.

- 2026-09-23T21:11:09+00:00: Recorded command exit 0; command argv SHA-256
  48ae495b2b5fa87b94960e175f923719bf2e7c228ec8f3c4902d92d0f444761f.

- 2026-09-23T21:11:22+00:00: Recorded command exit 1; command argv SHA-256
  48ae495b2b5fa87b94960e175f923719bf2e7c228ec8f3c4902d92d0f444761f.

- 2026-09-23T21:11:38+00:00: Implemented bounded control/runtime attestation slice. Added
  CertificateAuthorityV1::issue_metadata endpoint/generation/revocation validation; asb-runtime now
  binds private LiveProviderControlClaims to issued operator/administrator chain and rejects
  malformed digests/private targets. Focused live_service tests pass 11/11; cargo check --offline
  --workspace passes. Product commit is SSH-signed+DCO.

- 2026-09-23T21:12:27+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-23T21:12:49+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-23T21:13:53+00:00: Recorded command exit 0; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-23T21:14:21+00:00: Full applicable local gates passed: cargo fmt --all -- --check; cargo
  clippy --locked --workspace --all-targets -- -D warnings; cargo test --locked --workspace
  including doc tests. Review confirmed no public claims constructors/accessors and no CLI authority
  inputs. No native live evidence was claimed.

- 2026-09-23T21:15:18+00:00: Recorded command exit 0; command argv SHA-256
  6df23ddc4ce94a384cd18137a08d3dbc354461097bfea261cd73f5ac9bc652c5.

- 2026-09-23T21:15:34+00:00: Recorded command exit 0; command argv SHA-256
  2be76a1767f4b3a89fc912bbfa2718067f715b6fad6cbc6b25ead40638ea1226.

- 2026-09-23T21:19:06+00:00: Recorded command exit 0; command argv SHA-256
  a65090b821b6aa82bf73a05e1d9d5eab573cd6a15ce1f143b42c415564492891.

- 2026-09-23T21:20:10+00:00: Recorded command exit 101; command argv SHA-256
  5c8da9b34935360f7399b9d4b260d9a460b442f2f0ca08eddaee6e8f11776ef0.

- 2026-09-23T21:20:41+00:00: Recorded command exit 0; command argv SHA-256
  5c8da9b34935360f7399b9d4b260d9a460b442f2f0ca08eddaee6e8f11776ef0.

- 2026-09-23T21:20:54+00:00: Recorded command exit 0; command argv SHA-256
  18bd4aff9a09c3fb87a532f0a7fcc2d0fe00607e496aacf84775e9e758436f78.

- 2026-09-23T21:21:07+00:00: Recorded command exit 0; command argv SHA-256
  f4937b0f7fb7e5c99a1129b8fb82a8cf16d8092da5da279f468493079d438e69.
