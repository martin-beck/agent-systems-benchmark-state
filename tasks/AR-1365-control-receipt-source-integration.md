---
{
  "branch": "feature/ar-1365-control-receipt-source-integration",
  "checkpoint_commit": "aa537f6a07ac3476a8c4d6443a8df3c42a1aebc1",
  "claim_expires": "2026-09-24T02:10:34+00:00",
  "depends_on": [
    "AR-1362",
    "AR-1364"
  ],
  "id": "AR-1365",
  "next_action": "PR #269 merged as aa537f6a07ac3476a8c4d6443a8df3c42a1aebc1. Monitor seven post-merge workflows for exact merge SHA; release only after every workflow is terminal success.",
  "observed_branch": "feature/ar-1365-control-receipt-source-integration",
  "observed_dirty": 0,
  "observed_head": "6959cc1810265e026a9af40602752fdca4dc1e18",
  "owner": "codex-asb-runtime-attested-enrollment-luna56",
  "plan": "../plans/AR-1365-control-receipt-source-integration.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Integrate authenticated chain and authority enrollment into the versioned control receipt source.",
  "task_revision": 26,
  "title": "Control receipt source integration",
  "updated_at": "2026-09-24T00:10:34+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1365-control-receipt-source-integration"
}
---

Successor for blocked AR-1363, explicitly depending on completed AR-1362 and
AR-1364. Do not touch asb-tui or synthesize authority from CLI/config input.

- 2026-09-24T00:00:00+00:00: Created after AR-1364 supplied authenticated
  chain enrollment materialization and all post-merge workflows passed.

- 2026-09-23T23:54:21+00:00: Promote receipt-source integration after AR-1362 and AR-1364 completed
  authority and chain primitives with all post-merge gates.

- 2026-09-23T23:54:24+00:00: Claimed by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T23:55:36+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T23:56:04+00:00: Recorded command exit 0; command argv SHA-256
  d9dd06c9e77766238089b3c04fcddb575442cf1887a2ccc06521948ea874e7cc.

- 2026-09-23T23:56:18+00:00: Recorded command exit 0; command argv SHA-256
  907b1b1f743859290d1b107a1971b1dbf4bfaf02a4014ca1961d94cfbbf81467.

- 2026-09-23T23:56:31+00:00: Recorded command exit 0; command argv SHA-256
  6e8cb2a64901eb1a329d88fa73bfb5df82ce60a90a4732207a42bf5678ac2e6b.

- 2026-09-23T23:56:48+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T23:56:52+00:00: Recorded command exit 0; command argv SHA-256
  d9fa5fa9d6b1edd0744be1b0aa7351347516f8475fbf10364d8f42e7873456ab.

- 2026-09-23T23:57:20+00:00: Recorded command exit 0; command argv SHA-256
  b2f7111306aa7c03c56215bdb77e1811ed87e0363612681320219865a955e4c7.

- 2026-09-23T23:58:16+00:00: Implemented bounded RuntimeReceiptRequestV1 and
  RuntimeReceiptResponseV1 contracts in asb-control: strict schema, provider/generation/nonce
  validation, request-response binding, secret/path-free receipt fields, and positive/negative
  tests. Full asb-control tests 66+26+7+4 plus docs pass; workspace clippy -D warnings and fmt pass.
  Signed+DCO product commit 6959cc1810265e026a9af40602752fdca4dc1e18.

- 2026-09-23T23:58:29+00:00: Recorded command exit 0; command argv SHA-256
  d476a77a088a79e5e0444c8d52b3a20ff98ee0ea30280dc07949d5fda250e9a1.

- 2026-09-23T23:58:44+00:00: Recorded command exit 0; command argv SHA-256
  acf118b8a8f0abcd5b5c44edf87ecdfcd415c54f7605f3eb12c0a48b148645f7.

- 2026-09-24T00:00:09+00:00: Publication verified: clean SSH-signed+DCO commit
  6959cc1810265e026a9af40602752fdca4dc1e18 is pushed and PR #269 is open at the exact head.

- 2026-09-24T00:00:12+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-24T00:02:08+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-24T00:03:09+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-24T00:05:04+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-24T00:06:02+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-24T00:07:06+00:00: Recorded command exit 0; command argv SHA-256
  3ac7933f60057b62db960dd03ad6259ab646e726fde5455eae4953c5614758ba.

- 2026-09-24T00:07:45+00:00: Protected merge verified: PR #269 exact head
  6959cc1810265e026a9af40602752fdca4dc1e18 merged at aa537f6a07ac3476a8c4d6443a8df3c42a1aebc1 after
  all 12 required checks passed and final signature/DCO/diff review.

- 2026-09-24T00:07:56+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-24T00:09:37+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-24T00:10:34+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.
