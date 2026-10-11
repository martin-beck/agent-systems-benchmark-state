---
{
  "branch": "feature/ar-1782-verified-asb-workload-installation",
  "checkpoint_commit": "c5154b12fc85bf356ce61d746c56b83d856ff502",
  "claim_expires": "2026-10-11T21:30:00+00:00",
  "depends_on": [
    "AR-1781"
  ],
  "id": "AR-1782",
  "next_action": "PR #584 rebased onto origin/main 24cb72d; exact remote head 96ea497a. Credential-free workload matrix, diagnostic contract, provenance, resolver, and clippy focused gates pass. Poll fresh exact-head CI; do not merge.",
  "observed_branch": "feature/ar-1782-verified-asb-workload-installation",
  "observed_dirty": 0,
  "observed_head": "2ee4626e7784d4f7deb8d1110a8c58257b6dac2e",
  "owner": "ar1782-coordinator-repair",
  "plan": "../plans/AR-1782-verified-asb-workload-installation.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1782.json",
    "spec_revision": 2,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1782.json",
  "spec_revision": 2,
  "status": "in_progress",
  "summary": "Implement dedicated verified remote external workload installation and lifecycle through asb workload.",
  "task_revision": 135,
  "title": "Verified asb workload installation",
  "updated_at": "2026-10-11T19:30:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1782-verified-asb-workload-installation"
}
---

Add `asb workload install <supported-id> [--project PATH]` and `list`, `status`,
`select`, `repair`, `update`, and `remove` lifecycle commands. Install resolves only the
AR-1781 catalog, downloads the official primary-source workload release into a
project-local workload root, verifies immutable identity/proof/license/size and
archive boundaries, performs only declared bounded preparation, validates the
adapter-ready structure, and atomically records a workload receipt.

The command must support all AR-1781 development workload IDs, including
SWE-mini, not merely list them. It must preserve a good prior workload on failed update,
never execute downloaded installer scripts, require root, or mutate global package
manager state. Read-only operations are network-free. Download, integrity,
license, preparation, storage, incompatibility, stale/revoked, and offline cases
must remain separate actionable outcomes. Development operation must not be
blocked by production authorization or hosted-release verification requirements;
the pinned primary-source identity, declared constraints, and bounded preparation
remain mandatory.

- 2026-10-11T13:53:25+00:00: Promote dependency-safe AR-1782 now that AR-1781 is durably done with
  exact-main evidence.

- 2026-10-11T13:53:59+00:00: Claimed by ar1782_workload_install_luna56.

- 2026-10-11T13:54:05+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-10-11T14:00:48+00:00: Heartbeat by ar1782_workload_install_luna56.

- 2026-10-11T14:04:41+00:00: Recorded command exit 0; command argv SHA-256
  e274074a17e0682b5edf79b5caca577a41520ed9ca8daf9342f0433b678582a1.

- 2026-10-11T14:05:07+00:00: Recorded command exit 0; command argv SHA-256
  acc9cf8127a84779f740f6350aa3a1616ba38c8dc1c9797006e2886289fc16e0.

- 2026-10-11T14:05:20+00:00: Recorded command exit 0; command argv SHA-256
  e6e449e9d1f470db7ec6f673f670b5e31f0066cbbd41fd7b2de98c8bdbed15c6.

- 2026-10-11T14:05:31+00:00: Recorded command exit 0; command argv SHA-256
  afb0c01c2d49638af443d2502727e1b5ac6bfd221160d69ddb93f495dd751142.

- 2026-10-11T14:05:54+00:00: Recorded command exit 8; command argv SHA-256
  78f325bde3962aea10f3844ad0018af88b2cf3e001f1e02858b67193c031b6ae.

- 2026-10-11T14:06:26+00:00: PR #584 is open at signed+DCO product head a1090297. Exact-head CI is
  running; header/provenance/AWQ shadow checks pass, remaining required workflows pending.

- 2026-10-11T14:06:30+00:00: Heartbeat by ar1782_workload_install_luna56.

- 2026-10-11T14:06:58+00:00: Recorded command exit 8; command argv SHA-256
  78f325bde3962aea10f3844ad0018af88b2cf3e001f1e02858b67193c031b6ae.

- 2026-10-11T14:07:43+00:00: Recorded command exit 8; command argv SHA-256
  78f325bde3962aea10f3844ad0018af88b2cf3e001f1e02858b67193c031b6ae.

- 2026-10-11T14:08:05+00:00: Recorded command exit 8; command argv SHA-256
  78f325bde3962aea10f3844ad0018af88b2cf3e001f1e02858b67193c031b6ae.

- 2026-10-11T14:08:46+00:00: Recorded command exit 8; command argv SHA-256
  78f325bde3962aea10f3844ad0018af88b2cf3e001f1e02858b67193c031b6ae.

- 2026-10-11T14:08:49+00:00: Recorded command exit 8; command argv SHA-256
  78f325bde3962aea10f3844ad0018af88b2cf3e001f1e02858b67193c031b6ae.

- 2026-10-11T14:09:50+00:00: Recorded command exit 8; command argv SHA-256
  78f325bde3962aea10f3844ad0018af88b2cf3e001f1e02858b67193c031b6ae.

- 2026-10-11T14:10:45+00:00: Recorded command exit 1; command argv SHA-256
  78f325bde3962aea10f3844ad0018af88b2cf3e001f1e02858b67193c031b6ae.

- 2026-10-11T14:11:09+00:00: Recorded command exit 0; command argv SHA-256
  e8fa5ae4c6687147b213085b0419c35165daa77f6f62165ff84de0a0ca2e56d4.

- 2026-10-11T14:12:41+00:00: Rust checks failed only at diagnostic_contract ordinary producer
  identity; local generated catalog repair passes focused test. Do not push overlapping repair
  before AR-1793 merge.

- 2026-10-11T14:12:45+00:00: Heartbeat by ar1782_workload_install_luna56.

- 2026-10-11T14:31:22+00:00: Recorded command exit 0; command argv SHA-256
  a19f9863e49c2e0fe53777cca6eb65ba80003ffaa6ac29ced611d1a7d816da3e.

- 2026-10-11T14:31:39+00:00: Recorded command exit 0; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-10-11T14:31:50+00:00: Recorded command exit 0; command argv SHA-256
  6b0340b78e00b5e8d62e9973b7e72f6c6de22448e8636894d4001797a91460ec.

- 2026-10-11T14:32:09+00:00: Recorded command exit 0; command argv SHA-256
  e7bd0253a3301d42ef2d00a6221164345479a524c2349ff67e6eca5bfbd24951.

- 2026-10-11T14:32:38+00:00: Recorded command exit 0; command argv SHA-256
  04c7d6439ff8aae8c18a38395591b0d548ab41ade5cfeaa27267e6ac20bbb736.

- 2026-10-11T14:33:06+00:00: Recorded command exit 0; command argv SHA-256
  ac3e505f30fd620a7c294d45f78bcf244146c7ac1be401dd8c78fa01c13f8abb.

- 2026-10-11T14:33:35+00:00: Recorded command exit 8; command argv SHA-256
  78f325bde3962aea10f3844ad0018af88b2cf3e001f1e02858b67193c031b6ae.

- 2026-10-11T14:34:05+00:00: Rebased after AR-1793 merge and pushed generated diagnostic identity
  repair 0c31a205. Fresh PR checks are running; headers/provenance/AWQ shadow pass, remaining checks
  pending.

- 2026-10-11T14:34:47+00:00: Recorded command exit 8; command argv SHA-256
  78f325bde3962aea10f3844ad0018af88b2cf3e001f1e02858b67193c031b6ae.

- 2026-10-11T14:39:20+00:00: Recorded command exit 0; command argv SHA-256
  e7bd0253a3301d42ef2d00a6221164345479a524c2349ff67e6eca5bfbd24951.

- 2026-10-11T14:39:45+00:00: Recorded command exit 0; command argv SHA-256
  2c9d442f017d15b4fd94d96190844d436ce52d408beaa15376675a764087bb7e.

- 2026-10-11T14:40:13+00:00: Recorded command exit 0; command argv SHA-256
  ac3e505f30fd620a7c294d45f78bcf244146c7ac1be401dd8c78fa01c13f8abb.

- 2026-10-11T14:40:45+00:00: Corrected legacy_cli_ar1782_4239 collision: tool_kind callsite is
  reviewed as legacy_cli_ar1777_0028 with MalformedInput; removed duplicate workload identity.
  Focused diagnostic tests and all 379 asb-cli lib tests pass.

- 2026-10-11T14:40:52+00:00: Heartbeat by ar1782_workload_install_luna56.

- 2026-10-11T14:41:00+00:00: Recorded command exit 8; command argv SHA-256
  78f325bde3962aea10f3844ad0018af88b2cf3e001f1e02858b67193c031b6ae.

- 2026-10-11T14:42:02+00:00: Recorded command exit 8; command argv SHA-256
  78f325bde3962aea10f3844ad0018af88b2cf3e001f1e02858b67193c031b6ae.

- 2026-10-11T14:42:33+00:00: Verified origin branch and local HEAD both equal 16c9bbd9. Fresh
  workflow run 381481250xx has no failures; nine required checks remain pending.

- 2026-10-11T14:42:39+00:00: Heartbeat by ar1782_workload_install_luna56.

- 2026-10-11T14:51:01+00:00: Recorded command exit 0; command argv SHA-256
  b97757641a9af30f9ac31e77e95e32904b294391d35779620e8d262127a7ab99.

- 2026-10-11T14:51:25+00:00: Recorded command exit 0; command argv SHA-256
  588ed962a9f7251dcf3409f13fbfc46aa005d8867145f488d9b595c1538ae6d6.

- 2026-10-11T14:51:47+00:00: Recorded command exit 0; command argv SHA-256
  ac3e505f30fd620a7c294d45f78bcf244146c7ac1be401dd8c78fa01c13f8abb.

- 2026-10-11T14:52:32+00:00: Repair d40c5cfd signed+DCO hardens archive safety, mandatory
  digest/proof/license/preparation validation, rollback, hostile lifecycle tests, and refreshes
  provenance/catalog.

- 2026-10-11T14:52:39+00:00: Heartbeat by ar1782_workload_install_luna56.

- 2026-10-11T14:55:47+00:00: Recorded command exit 0; command argv SHA-256
  b97757641a9af30f9ac31e77e95e32904b294391d35779620e8d262127a7ab99.

- 2026-10-11T14:56:15+00:00: Recorded command exit 0; command argv SHA-256
  29704f6ffde8c7b6c360a1f3d6e9cd643daa5af7ce362f9bba27c3951411a9c3.

- 2026-10-11T14:56:48+00:00: Recorded command exit 0; command argv SHA-256
  ac3e505f30fd620a7c294d45f78bcf244146c7ac1be401dd8c78fa01c13f8abb.

- 2026-10-11T14:57:06+00:00: Repaired Rust CI clippy failure at bundle publication and pushed
  9f6e2142; substantive lifecycle safety remains intact.

- 2026-10-11T14:57:11+00:00: Heartbeat by ar1782_workload_install_luna56.

- 2026-10-11T15:06:25+00:00: Heartbeat by ar1782_workload_install_luna56.

- 2026-10-11T15:08:48+00:00: Recorded command exit 0; command argv SHA-256
  b97757641a9af30f9ac31e77e95e32904b294391d35779620e8d262127a7ab99.

- 2026-10-11T15:09:25+00:00: Recorded command exit 0; command argv SHA-256
  481392d227fd6f3e12e572a50ca3aa6a87f0b7953fb1349d17f66f6c32a7ccc4.

- 2026-10-11T15:09:50+00:00: Recorded command exit 0; command argv SHA-256
  ac3e505f30fd620a7c294d45f78bcf244146c7ac1be401dd8c78fa01c13f8abb.

- 2026-10-11T15:10:15+00:00: Coverage gate on 9f6e2142 measured 89.76% hosted despite local 90.02%;
  added focused workload list/status/select/remove/proof-negative matrix without changing
  thresholds.

- 2026-10-11T15:10:18+00:00: Heartbeat by ar1782_workload_install_luna56.

- 2026-10-11T15:17:34+00:00: Recorded command exit 0; command argv SHA-256
  b97757641a9af30f9ac31e77e95e32904b294391d35779620e8d262127a7ab99.

- 2026-10-11T15:17:57+00:00: Recorded command exit 0; command argv SHA-256
  c3e80ee2208cc946a4a235e95c2df8f5111af748a93440e2e623ae79fef5587b.

- 2026-10-11T15:18:23+00:00: Recorded command exit 0; command argv SHA-256
  ac3e505f30fd620a7c294d45f78bcf244146c7ac1be401dd8c78fa01c13f8abb.

- 2026-10-11T15:18:48+00:00: Hosted coverage was 89.87%; success-path matrix now exercises installed
  record lifecycle and should clear unchanged 90% floor.

- 2026-10-11T15:18:51+00:00: Heartbeat by ar1782_workload_install_luna56.

- 2026-10-11T15:27:28+00:00: Recorded command exit 0; command argv SHA-256
  b97757641a9af30f9ac31e77e95e32904b294391d35779620e8d262127a7ab99.

- 2026-10-11T15:27:50+00:00: Recorded command exit 0; command argv SHA-256
  5ac8ecedc20e29ce923c325ac0b7f43f43812197039a08c1e984d8ed1d2edee9.

- 2026-10-11T15:28:14+00:00: Recorded command exit 0; command argv SHA-256
  ac3e505f30fd620a7c294d45f78bcf244146c7ac1be401dd8c78fa01c13f8abb.

- 2026-10-11T15:28:39+00:00: Hosted coverage was 89.89%; this repair adds remaining deterministic
  lifecycle/archive branches without changing thresholds.

- 2026-10-11T15:28:46+00:00: Heartbeat by ar1782_workload_install_luna56.

- 2026-10-11T15:42:28+00:00: Recorded command exit 0; command argv SHA-256
  522eda7c168ca7a6c603a7ae6df4310ac3a3a5b64a26e26063a09057d30ada95.

- 2026-10-11T15:42:52+00:00: Recorded command exit 0; command argv SHA-256
  59fa108a1b1071492739ee55523bf641a76f9ae98bb60c3e5ed0f3730c486358.

- 2026-10-11T15:43:17+00:00: Recorded command exit 0; command argv SHA-256
  293c2148a179cf191174557f643f16f9891d390fd73eaa6feadfba1fcb474444.

- 2026-10-11T15:43:59+00:00: Repaired substantive lifecycle and hosted PTY race blockers; push
  complete, awaiting fresh hosted checks.

- 2026-10-11T15:45:17+00:00: Heartbeat by ar1782_workload_install_luna56.

- 2026-10-11T15:50:29+00:00: Recorded command exit 0; command argv SHA-256
  5f57a7529df044ee1fbff4e20904785ff10c9115905a7ca26ff2a8943ac2186c.

- 2026-10-11T15:50:55+00:00: Recorded command exit 0; command argv SHA-256
  55d545e10cfdca0eb19e12b08e575de457d8ca76e5905242ea2aa891e5dbb159.

- 2026-10-11T15:51:15+00:00: Recorded command exit 0; command argv SHA-256
  293c2148a179cf191174557f643f16f9891d390fd73eaa6feadfba1fcb474444.

- 2026-10-11T15:51:43+00:00: Repaired generated diagnostic identity catalog after exact hosted
  failure; fresh CI required.

- 2026-10-11T15:52:16+00:00: Observed exact pushed head 8371090f and renewed test evidence after
  catalog repair.

- 2026-10-11T15:52:21+00:00: Heartbeat by ar1782_workload_install_luna56.

- 2026-10-11T15:52:29+00:00: Checkpointed source commit 8371090f1446f7191739a80415db7860911b62ef.

- 2026-10-11T16:00:02+00:00: Recorded command exit 0; command argv SHA-256
  6ccdbe3547ec7043b3d36864e5b445013277e5f9b9e624f957c4f0617b256c5f.

- 2026-10-11T16:00:32+00:00: Recorded command exit 0; command argv SHA-256
  ab85ba62e941cd127c434cceafd4b252903ec696e4fd787751f48d7f48f6cbea.

- 2026-10-11T16:01:00+00:00: Recorded command exit 0; command argv SHA-256
  293c2148a179cf191174557f643f16f9891d390fd73eaa6feadfba1fcb474444.

- 2026-10-11T16:01:37+00:00: Repaired exact provenance fixture digest after hosted Rust failure;
  pushed c5154b12.

- 2026-10-11T16:01:44+00:00: Heartbeat by ar1782_workload_install_luna56.

- 2026-10-11T16:01:51+00:00: Checkpointed source commit c5154b12fc85bf356ce61d746c56b83d856ff502.

- 2026-10-11T16:11:30+00:00: Recorded command exit 0; command argv SHA-256
  ff59affe15aef98b4f88f136d4ccb9f578abba05496d6e0417ba7ae678abf20b.

- 2026-10-11T16:11:54+00:00: Recorded command exit 0; command argv SHA-256
  2f7f3b099f794b9d0c035d54de704dbce0db4099fd52ebc980e102698e26913c.

- 2026-10-11T16:12:20+00:00: Recorded command exit 0; command argv SHA-256
  293c2148a179cf191174557f643f16f9891d390fd73eaa6feadfba1fcb474444.

- 2026-10-11T16:12:47+00:00: Pushed lifecycle/output/coverage repair after hosted 89.87% floor
  failure; lease renewal required.

- 2026-10-11T16:12:52+00:00: Heartbeat by ar1782_workload_install_luna56.

- 2026-10-11T16:14:04+00:00: Reconciled durable task to signed+DCO product head 4b79404a. Repair
  implements bounded acquisition helper, human default/JSON opt-in, distinct install/update/repair
  preconditions, offline repair/stale detection, and focused lifecycle coverage; pending hosted
  gates.

- 2026-10-11T16:14:08+00:00: Heartbeat by ar1782_workload_install_luna56.

- 2026-10-11T16:18:29+00:00: Recorded command exit 128; command argv SHA-256
  e7bd0253a3301d42ef2d00a6221164345479a524c2349ff67e6eca5bfbd24951.

- 2026-10-11T16:18:52+00:00: Recorded command exit 0; command argv SHA-256
  5f57a7529df044ee1fbff4e20904785ff10c9115905a7ca26ff2a8943ac2186c.

- 2026-10-11T16:19:25+00:00: Recorded command exit 0; command argv SHA-256
  5f57a7529df044ee1fbff4e20904785ff10c9115905a7ca26ff2a8943ac2186c.

- 2026-10-11T16:19:49+00:00: Recorded command exit 0; command argv SHA-256
  01f1912a5e878df266e7185d8d4e6335b829832e630f8d783a183439212a6471.

- 2026-10-11T16:20:17+00:00: Recorded command exit 0; command argv SHA-256
  293c2148a179cf191174557f643f16f9891d390fd73eaa6feadfba1fcb474444.

- 2026-10-11T16:21:33+00:00: Repaired hosted Rust and credential-free catalog mismatch by removing
  duplicate lib.rs:4143 identity; signed+DCO commit 35fef02b pushed. Full credential-free lib suite
  passes 384/384 locally.

- 2026-10-11T16:21:38+00:00: Heartbeat by ar1782_workload_install_luna56.

- 2026-10-11T16:37:43+00:00: Recorded command exit 0; command argv SHA-256
  ff59affe15aef98b4f88f136d4ccb9f578abba05496d6e0417ba7ae678abf20b.

- 2026-10-11T16:38:07+00:00: Recorded command exit 0; command argv SHA-256
  c43c3bac5e275330f9eb9b0d9044b9c671dc163d3869caa4d181e9427a795e22.

- 2026-10-11T16:38:30+00:00: Recorded command exit 0; command argv SHA-256
  293c2148a179cf191174557f643f16f9891d390fd73eaa6feadfba1fcb474444.

- 2026-10-11T16:38:55+00:00: Pushed signed+DCO e9b6ceac for all independent-review blockers and
  coverage margin. Source tarball path handling and exercism repositories[] are catalog-bound;
  repair revalidates retained evidence and reconstructs prepared state.

- 2026-10-11T16:39:00+00:00: Heartbeat by ar1782_workload_install_luna56.

- 2026-10-11T16:48:17+00:00: Recorded command exit 0; command argv SHA-256
  ff59affe15aef98b4f88f136d4ccb9f578abba05496d6e0417ba7ae678abf20b.

- 2026-10-11T16:48:40+00:00: Recorded command exit 0; command argv SHA-256
  1acef21545e70189b7ae3a0de2c092a26fd9990bbf73e05204247448c37d6c6e.

- 2026-10-11T16:49:04+00:00: Recorded command exit 0; command argv SHA-256
  293c2148a179cf191174557f643f16f9891d390fd73eaa6feadfba1fcb474444.

- 2026-10-11T16:49:29+00:00: Pushed signed+DCO 55d0f1dd with additional repair missing-bundle,
  malformed-receipt, archive rebuild, stale prepared replacement, and human output tests;
  regenerated diagnostic catalog and provenance digest.

- 2026-10-11T16:49:34+00:00: Heartbeat by ar1782_workload_install_luna56.

- 2026-10-11T17:09:27+00:00: Recorded command exit 0; command argv SHA-256
  ff59affe15aef98b4f88f136d4ccb9f578abba05496d6e0417ba7ae678abf20b.

- 2026-10-11T17:09:48+00:00: Recorded command exit 0; command argv SHA-256
  a1079a7e907fc7f264c34e4ac5da5c72b4726750537377aa0aa0548da2c7367b.

- 2026-10-11T17:10:09+00:00: Recorded command exit 0; command argv SHA-256
  293c2148a179cf191174557f643f16f9891d390fd73eaa6feadfba1fcb474444.

- 2026-10-11T17:10:39+00:00: Pushed signed+DCO fdb1e4bc with verified-workload source-shape,
  archive-safety, and repair-proof coverage tests; local full quality gate passed at 90.17%
  workspace lines after PTY rerun.

- 2026-10-11T17:11:02+00:00: Heartbeat by ar1782_workload_install_luna56.

- 2026-10-11T17:15:18+00:00: Recorded command exit 0; command argv SHA-256
  ff59affe15aef98b4f88f136d4ccb9f578abba05496d6e0417ba7ae678abf20b.

- 2026-10-11T17:15:38+00:00: Recorded command exit 0; command argv SHA-256
  7a0a43a0391813ef0f78627009729f69d143c8b919b35095009c3a84ce2b50b4.

- 2026-10-11T17:16:00+00:00: Recorded command exit 0; command argv SHA-256
  293c2148a179cf191174557f643f16f9891d390fd73eaa6feadfba1fcb474444.

- 2026-10-11T17:16:26+00:00: Heartbeat by ar1782_workload_install_luna56.

- 2026-10-11T17:20:30+00:00: Recorded command exit 0; command argv SHA-256
  ff59affe15aef98b4f88f136d4ccb9f578abba05496d6e0417ba7ae678abf20b.

- 2026-10-11T17:20:51+00:00: Recorded command exit 0; command argv SHA-256
  5566a3a77299c54c6e918b1b11718cda49823c4a2fc104aff30a9db44d5cf04a.

- 2026-10-11T17:21:13+00:00: Recorded command exit 0; command argv SHA-256
  293c2148a179cf191174557f643f16f9891d390fd73eaa6feadfba1fcb474444.

- 2026-10-11T17:28:19+00:00: Heartbeat by ar1782_workload_install_luna56.

- 2026-10-11T17:28:26+00:00: Rebase completed with signed repair 96ea497a; preserved arXiv v1
  bounded validation and credential-free network deny boundary.

- 2026-10-11T19:29:04+00:00: Recovered expired claim formerly owned by
  ar1782_workload_install_luna56. Coordinator recovery: lease expired; preserve recorded PR evidence
  and await fresh exact-head validation.

- 2026-10-11T19:30:00+00:00: Claimed by ar1782-coordinator-repair.
