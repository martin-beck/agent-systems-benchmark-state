---
{
  "branch": "feature/ar-1378-live-control-adapter",
  "checkpoint_commit": "5f1902c681c9671d332ae662f0516df4d1f688df",
  "claim_expires": "2026-09-24T05:18:13+00:00",
  "depends_on": [
    "AR-1377",
    "AR-1366",
    "AR-1364",
    "AR-1362"
  ],
  "id": "AR-1378",
  "next_action": "PR #275 is published at exact head 5f1902c. Monitor all required checks; repair failures through handoffctl, merge only after independent review and green exact-head CI, then verify seven post-merge workflows.",
  "observed_branch": "feature/ar-1378-live-control-adapter",
  "observed_dirty": 0,
  "observed_head": "5f1902c681c9671d332ae662f0516df4d1f688df",
  "owner": "codex-asb-runtime-receipt-source-luna56",
  "plan": "../plans/AR-1378-live-control-adapter.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Bind authenticated control receipts to runtime-owned live dispatch.",
  "task_revision": 21,
  "title": "Authenticated live control adapter",
  "updated_at": "2026-09-24T03:18:13+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1378-live-control-adapter"
}
---

Successor to the blocked AR-1376 adapter audit. AR-1377 supplies the opaque
chain store; this task supplies only the authenticated control operation seam.

- 2026-09-24T03:08:14+00:00: Done dependencies AR-1377, AR-1366, AR-1364, AR-1362 verified; blocked
  AR-1376 is audit evidence only.

- 2026-09-24T03:08:16+00:00: Claimed by codex-asb-runtime-receipt-source-luna56.

- 2026-09-24T03:08:51+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-24T03:09:05+00:00: Recorded command exit 0; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-09-24T03:09:33+00:00: Heartbeat by codex-asb-runtime-receipt-source-luna56.

- 2026-09-24T03:09:36+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-24T03:10:01+00:00: Recorded command exit 0; command argv SHA-256
  67008938ba404966b828a69fb2cf59c6bfac9b7c63626c02f21fb063dfc4115e.

- 2026-09-24T03:10:27+00:00: Recorded command exit 0; command argv SHA-256
  37394e5771e08f1fcc6f3723ba7793dfbf4780ad0c239116d38abcfed112f8a0.

- 2026-09-24T03:10:47+00:00: Recorded command exit 0; command argv SHA-256
  67739c573b579619ef3e71fb893a396c166af5a2a061ba9f37d5e424ed8b55d4.

- 2026-09-24T03:11:00+00:00: Recorded command exit 0; command argv SHA-256
  fd23175f56422423585f1eecbad1b2f66722c7fe72a4467f792c5d7746773cdc.

- 2026-09-24T03:11:28+00:00: Recorded command exit 0; command argv SHA-256
  78fbb16b3cc348d668a897b869341aa0d0b57e48b7f483f5a8dc66393f21b8f9.

- 2026-09-24T03:11:43+00:00: Added LiveProviderRuntimeBridge::request_control_receipt: it sends
  RuntimeReceipt through authenticated ControlClient, accepts only typed RuntimeReceipt result,
  retrieves the opaque chain from RuntimeCertificateChainStore, and delegates
  nonce/generation/attestation/replay validation. Errors are bounded and privacy-safe. Existing
  bridge tests cover tamper/replay/stale/unavailable; focused command green.

- 2026-09-24T03:12:01+00:00: Recorded command exit 0; command argv SHA-256
  e210942b850b33ddbde4386c19c8f84af2ebdd24a0c9ef886eec60df32f1861c.

- 2026-09-24T03:12:17+00:00: Recorded command exit 0; command argv SHA-256
  78a02e2f11431111256149c8ca3a3ba4586f2d3710e11e6f9cbe0c5fe6efaa55.

- 2026-09-24T03:12:49+00:00: Independent review passed: adapter accepts only typed RuntimeReceipt
  responses from authenticated ControlClient and an opaque chain from RuntimeCertificateChainStore;
  no secrets, paths, certificate bytes, caller identities, or synthetic authority cross the
  boundary. Existing nonce/generation/replay/expiry/tamper checks remain authoritative. PR #275
  published clean with signed+DCO head.

- 2026-09-24T03:18:13+00:00: Heartbeat by codex-asb-runtime-receipt-source-luna56.
