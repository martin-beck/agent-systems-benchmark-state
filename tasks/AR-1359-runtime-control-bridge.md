---
{
  "branch": "feature/ar-1359-runtime-control-bridge",
  "checkpoint_commit": "f5119103248ff448bea4ab0bfc4581ed43743d7d",
  "claim_expires": "2026-09-24T00:44:03+00:00",
  "depends_on": [
    "AR-1357"
  ],
  "id": "AR-1359",
  "next_action": "PR #266 exact head f511910 is published. Monitor every exact-head required check, repair any failures without weakening gates, then merge only after all green and independent review.",
  "observed_branch": "feature/ar-1359-runtime-control-bridge",
  "observed_dirty": 0,
  "observed_head": "f5119103248ff448bea4ab0bfc4581ed43743d7d",
  "owner": "codex-asb-runtime-attested-enrollment-luna56",
  "plan": "../plans/AR-1359-runtime-control-bridge.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Bridge authenticated control enrollment into runtime-owned opaque live authority.",
  "task_revision": 26,
  "title": "Runtime/control enrollment bridge",
  "updated_at": "2026-09-23T22:44:03+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1359-runtime-control-bridge"
}
---

Successor for AR-1358's cross-crate architectural blocker. Preserve AR-1329
fail-closed behavior and do not touch asb-tui.

- 2026-09-24T00:40:00+00:00: Created after audit found no safe control/runtime
  bridge capable of issuing the merged runtime enrollment record to asb-cli.

- 2026-09-23T22:28:17+00:00: AR-1357 is done; promote the runtime-owned control bridge required by
  blocked AR-1358.

- 2026-09-23T22:28:20+00:00: Claimed by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T22:28:27+00:00: Recorded command exit 0; command argv SHA-256
  4c0706e50abf7d121dcd89426b0b89020f8675977c744726e971f75b0d0e0363.

- 2026-09-23T22:29:03+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T22:30:21+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T22:31:33+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-23T22:31:51+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T22:32:22+00:00: Recorded command exit 0; command argv SHA-256
  840fef93f52f8ecccfc52112d87ec726d91f86870935a18999f2dcaf059b1567.

- 2026-09-23T22:32:51+00:00: Recorded command exit 0; command argv SHA-256
  5ecc83bfcb02954567c903f622ae821bfdf2e6e1e5cdc2b2db80e01f23692506.

- 2026-09-23T22:33:28+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-23T22:34:25+00:00: Recorded command exit 0; command argv SHA-256
  b36d15881eb65027724bc584f1b04db05666cd79896b100806e528307c04b65c.

- 2026-09-23T22:34:39+00:00: Recorded command exit 0; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-23T22:34:55+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T22:35:02+00:00: Recorded command exit 0; command argv SHA-256
  928f94f912f52fad0d749b7d88488bcc0ee958c31e9b017b830db7e0679e951b.

- 2026-09-23T22:35:16+00:00: Recorded command exit 0; command argv SHA-256
  0bf5c49482b3146cd561f8793a704d552f416a0abe7e19089cc45734f08f2fd6.

- 2026-09-23T22:35:32+00:00: Recorded command exit 0; command argv SHA-256
  436fd8c71eeaf5a288b68647e2e7db846b02b36791ca2422dde7b1ed94ee9497.

- 2026-09-23T22:36:17+00:00: Implemented concrete bridge: asb-control issues bounded secret-free
  RuntimeEnrollmentReceiptV1 bound to validated certificate chain, provider/public target, digests,
  generation, freshness and deterministic nonce; private/link-local targets rejected. asb-runtime
  LiveProviderRuntimeBridge validates receipt against opaque IssuedCertificateChainV1, constructs
  private claims/attestation, consumes one-shot ledger, and returns only a secret-free enrollment
  record. Positive/tamper/replay/path-free tests pass; focused control/runtime tests, clippy
  workspace, full workspace tests, and rustdoc -D warnings pass. Commit f511910 is SSH-signed+DCO
  and pushed.

- 2026-09-23T22:36:34+00:00: Recorded command exit 0; command argv SHA-256
  20ce11e0e7800ae7906b34c64e08db4517d0a8adc68c8cdcfc3b1947f5dace33.

- 2026-09-23T22:37:19+00:00: Published PR #266 at exact head f511910 through handoffctl. All
  required hosted checks started; AWQ and headers already pass. No merge action taken while checks
  run.

- 2026-09-23T22:39:25+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T22:41:57+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T22:44:03+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.
