---
{
  "branch": "feature/asb-tui-compatibility-detection",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T15:45:28+00:00",
  "depends_on": [
    "AR-1017"
  ],
  "id": "AR-1018",
  "next_action": "Implement platform, architecture, ASB-version, protocol, and terminal capability detection.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-1018.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Detect whether an asb-tui bundle is compatible before installation or launch.",
  "task_revision": 30,
  "title": "Add asb-tui compatibility and terminal capability detection",
  "updated_at": "2026-09-10T13:00:11+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-compatibility-detection"
}
---
Detect OS/distribution, architecture, ASB version, protocol version, exact coordinator and
workflow-quality release compatibility, terminal dimensions/features,
SSH/tmux/screen context, and filesystem/runtime requirements. Select only compatible bundles and fail
closed with actionable diagnostics for unsupported combinations.

Acceptance criteria: deterministic machine-readable capability report, resize/channel tests, negative
fixtures for mismatches, privacy-safe diagnostics, and no host identifiers in public artifacts.

- 2026-09-10T12:40:02+00:00: AR-1017 is durably done at state 9aa38bcc with public exact-head checks
  and protection verified; AR-1018 is dependency-ready and owns disjoint compatibility detection.

- 2026-09-10T12:40:09+00:00: Claimed by contracts_20260906.

- 2026-09-10T12:40:29+00:00: Recorded command exit 0; command argv SHA-256
  263e132bbd0547042ae890d6380355f5364a45e5528910bdc3a67484dad324a6.

- 2026-09-10T12:45:28+00:00: Heartbeat by contracts_20260906.

- 2026-09-10T12:48:53+00:00: Recorded command exit 0; command argv SHA-256
  420472530e9d05303c33574061da3466b08bd64279b64a0008c4823f781a749a.

- 2026-09-10T12:49:04+00:00: Recorded command exit 101; command argv SHA-256
  59ec19432c7293e890383e067eeb07cf9a2ffae1aa12643fbdd0d792c7fa7fc0.

- 2026-09-10T12:51:21+00:00: Recorded command exit 0; command argv SHA-256
  420472530e9d05303c33574061da3466b08bd64279b64a0008c4823f781a749a.

- 2026-09-10T12:51:32+00:00: Recorded command exit 0; command argv SHA-256
  c9be30c10bf536e6c31fe8e5e3c2dbea49e29970e128dab52c3e4c45b3406367.

- 2026-09-10T12:51:42+00:00: Recorded command exit 0; command argv SHA-256
  4f2ddd9f039f2d8ae863160f907b82991d379b3ba87df7ab44fd95b9335a2491.

- 2026-09-10T12:55:13+00:00: Recorded command exit 0; command argv SHA-256
  420472530e9d05303c33574061da3466b08bd64279b64a0008c4823f781a749a.

- 2026-09-10T12:55:23+00:00: Recorded command exit 0; command argv SHA-256
  6fc8a14fcd761c01f586439ca0091c5ece7e229c7583879466962175a026dcde.

- 2026-09-10T12:55:32+00:00: Recorded command exit 0; command argv SHA-256
  4f2ddd9f039f2d8ae863160f907b82991d379b3ba87df7ab44fd95b9335a2491.

- 2026-09-10T12:55:41+00:00: Recorded command exit 0; command argv SHA-256
  e0396fd60d3a67d470b76f8925a026ebe7b817491604aeeeaecb79ccb38b4797.

- 2026-09-10T12:56:47+00:00: Recorded command exit 0; command argv SHA-256
  51c68dba96c0ef380a9368725f4aeb5819cd8ddf081c7a26a03d9c07cc018064.

- 2026-09-10T12:56:58+00:00: Recorded command exit 0; command argv SHA-256
  4e083eb5b3e77fb3ba1dd4f2ebb048bdf8151a497d2c7e2017cac7521e6d3800.

- 2026-09-10T12:57:15+00:00: Recorded command exit 0; command argv SHA-256
  9f3a2440bff01b4d24d2919beeb6d9737d350456482bee38ad7a277dff3e2e84.

- 2026-09-10T12:57:27+00:00: Recorded command exit 0; command argv SHA-256
  30a140d28210fcc3dccbbac332b10dfcc658d7918ef74ed6db6ced64a261183e.

- 2026-09-10T12:57:37+00:00: Recorded command exit 0; command argv SHA-256
  0edf3596ea0b07b191facdd776911433caa7cd521df6f4a7172e76b95c412cd5.

- 2026-09-10T12:57:45+00:00: Recorded command exit 0; command argv SHA-256
  d769193a8d50b9d7fa9f6f5f77c928dfc84c527a52f3a1e7f77daedcb6eeb9e9.

- 2026-09-10T12:57:55+00:00: Recorded command exit 0; command argv SHA-256
  d1b77cdc839fe95285cefcab486f47433cb3668f860ac98898c4845d9a16b6c5.

- 2026-09-10T12:58:28+00:00: Recorded command exit 0; command argv SHA-256
  1e432592b40c53a69194cff35ccd165f4dac63a22362c50b7e071883b490c17e.

- 2026-09-10T12:58:36+00:00: Recorded command exit 0; command argv SHA-256
  e43205235f188e57cc2535216051ffed3d3a0b6d003e100e2a7967bd140f4962.

- 2026-09-10T12:59:02+00:00: Recorded command exit 0; command argv SHA-256
  18bffdfc42466344d07f3b24f54205227d50df78b1e78174ed11a49c41b4a166.

- 2026-09-10T12:59:24+00:00: Recorded command exit 0; command argv SHA-256
  3828cfb12503069208247b7f6ebdae50f814294ce56ddcab2342a8325206a82d.

- 2026-09-10T12:59:37+00:00: Recorded command exit 0; command argv SHA-256
  ed1b8ab0753de1174529384365d93305c8bba1a8fa0261ee48d3ee4932dd7da2.

- 2026-09-10T12:59:45+00:00: Recorded command exit 0; command argv SHA-256
  0325f233f7b139f84e5a3f3c528b7299e1860d6ddcd06fc03318a6965c16e9c2.

- 2026-09-10T12:59:53+00:00: Recorded command exit 0; command argv SHA-256
  8810c52e3f82557e363f63b0bf2d37c0dd3da2133a4a9342201b571fb591d5d9.

- 2026-09-10T13:00:02+00:00: Recorded command exit 0; command argv SHA-256
  1f46cc71a57b572f7a8840331cf1d4e8093cafe922185fcd01790d9fe57be343.

- 2026-09-10T13:00:11+00:00: Recorded command exit 0; command argv SHA-256
  84e189320995361983fcf56c37a7b816a1cc838b3cd66c49dab3f0b068145df6.
