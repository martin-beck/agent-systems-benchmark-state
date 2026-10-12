---
{
  "branch": "feature/ar-1782-verified-asb-workload-installation",
  "checkpoint_commit": "c5154b12fc85bf356ce61d746c56b83d856ff502",
  "claim_expires": "",
  "depends_on": [
    "AR-1781"
  ],
  "id": "AR-1782",
  "next_action": "Recreate a clean integration worktree at exact merge 7ce484612db043831e4acb995839455f512197c0; rerun cargo test --locked --workspace through handoffctl, verify HEAD and cleanliness, then record result before release.",
  "observed_branch": "feature/ar-1782-verified-asb-workload-installation",
  "observed_dirty": 0,
  "observed_head": "3be3029d7a1d927b86b4ae938abfc939d8339009",
  "owner": "",
  "plan": "../plans/AR-1782-verified-asb-workload-installation.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "environmental",
    "evidence_digest": "sha256:965d865fd1afadeb545c34aac7d9efb6fbed9f3203c0695c0e3f68178702e3e9",
    "evidence_ref": "evidence/AR-1782-post-merge-receipt.txt",
    "spec_ref": "specs/AR-1782.json",
    "spec_revision": 2,
    "status": "pass"
  },
  "spec_ref": "specs/AR-1782.json",
  "spec_revision": 2,
  "status": "done",
  "summary": "Implement dedicated verified remote external workload installation and lifecycle through asb workload.",
  "task_revision": 253,
  "title": "Verified asb workload installation",
  "updated_at": "2026-10-11T20:57:31+00:00",
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

- 2026-10-11T19:30:05+00:00: Repair commits e2b6c96a and 2ee4626e close path confinement, evaluator
  layout, license, and diagnostic-contract gaps; worker tests and clippy passed. Coordinator now
  owns exact-head review and CI transition.

- 2026-10-11T19:31:10+00:00: Heartbeat by ar1782-coordinator-repair.

- 2026-10-11T19:31:13+00:00: Fresh CI at 2ee4626e failed only because
  docs/examples/asb-cli-workflow-v1.provenance.json retains the pre-repair lib.rs digest; this is a
  version-coupled fixture repair, not a gate bypass.

- 2026-10-11T19:31:32+00:00: Recorded command exit 0; command argv SHA-256
  79330f4930c0b2862f387bc03e8f654452ee893b5e4e4b0b5c975164a14b11f5.

- 2026-10-11T19:31:50+00:00: Recorded command exit 0; command argv SHA-256
  ef19043205064ea87bec66574bfe246191c9311bc8c404cd8e347d08fbdc44f0.

- 2026-10-11T19:32:09+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-11T19:32:30+00:00: Recorded command exit 0; command argv SHA-256
  a5e91d8a6e356ba88fd4835c765ebd2411c75eacaa60f98e203295ec257bd3a5.

- 2026-10-11T19:32:57+00:00: Recorded command exit 0; command argv SHA-256
  43ea9928318902aa9759fb71da6ab8f4065ad9187c052d4dbcfab10689b865dc.

- 2026-10-11T19:33:03+00:00: Recorded command exit 0; command argv SHA-256
  4f8df750c52059d8635553b027b488846a11042048be7fbf9b169d768cc9b33c.

- 2026-10-11T19:33:05+00:00: Recorded command exit 0; command argv SHA-256
  7e98eb9e102fb5d7990fdbc762db8b81b0736b84bd704ca74b2362608b3609fb.

- 2026-10-11T19:33:26+00:00: Heartbeat by ar1782-coordinator-repair.

- 2026-10-11T19:33:26+00:00: Provenance fixture refreshed to exact lib.rs digest 212ecc...; focused
  provenance tests, formatting, diff checks, SSH signature, and DCO verified.

- 2026-10-11T19:33:31+00:00: Recorded command exit 0; command argv SHA-256
  d32df0a8f7802e39b9a6743613fff16ac35e4dddba3905aa783a204f77a7e43f.

- 2026-10-11T19:34:02+00:00: Recorded command exit 0; command argv SHA-256
  e99fa3526731594bb874afc38873d168af47ae1a7a2b2f28a3ba0ab45ec23c25.

- 2026-10-11T19:34:23+00:00: Recorded command exit 0; command argv SHA-256
  eb8648d78be9d44db5631385c3fcbaaeaac0114989924fef6dc1415045ce0bfa.

- 2026-10-11T19:41:25+00:00: Heartbeat by ar1782-coordinator-repair.

- 2026-10-11T19:41:25+00:00: Policy gate failed on hosted workspace line coverage 89.96%; no
  threshold or exclusion change authorized. Start focused headroom repair.

- 2026-10-11T19:41:37+00:00: Recorded command exit 1; command argv SHA-256
  9021062b2f94c8237a275d55c1d58d4b68f814009d1e64c0331cc2e79485dbf5.

- 2026-10-11T19:42:02+00:00: Heartbeat by ar1782-coordinator-repair.

- 2026-10-11T19:42:22+00:00: Recorded command exit 0; command argv SHA-256
  55dcada8241e128ea43fad98b16914d286accd7b1ae8800223abfe72d4b7663f.

- 2026-10-11T19:43:07+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-11T19:43:13+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-11T19:43:22+00:00: Recorded command exit 101; command argv SHA-256
  7478958eb316c743a73bd43b84218eeabe587096e7a49efafbd15511f621999a.

- 2026-10-11T19:43:30+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-11T19:43:37+00:00: Recorded command exit 0; command argv SHA-256
  7478958eb316c743a73bd43b84218eeabe587096e7a49efafbd15511f621999a.

- 2026-10-11T19:45:05+00:00: Recorded command exit 101; command argv SHA-256
  11aa7892ee38d3a937558ce5f68e38a693ff8b89e160ec2c02b25ddf17ea330b.

- 2026-10-11T19:45:40+00:00: Recorded command exit 101; command argv SHA-256
  bbce46d2ff93648e7eb1884aa7b67c4b6fc4c41a4baf56000d9f1186d564d857.

- 2026-10-11T19:46:02+00:00: Recorded command exit 0; command argv SHA-256
  7109951d44fa989265b6b6481cadfc8b40676ae39f4e04b8e1126fe99b431b01.

- 2026-10-11T19:47:03+00:00: Recorded command exit 101; command argv SHA-256
  11aa7892ee38d3a937558ce5f68e38a693ff8b89e160ec2c02b25ddf17ea330b.

- 2026-10-11T19:47:27+00:00: Recorded command exit 0; command argv SHA-256
  9ff4e40d0a608a041abbfd1d435a9e4d565a2c8931e342870e1969854466c867.

- 2026-10-11T19:47:35+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-11T19:47:43+00:00: Recorded command exit 0; command argv SHA-256
  b97757641a9af30f9ac31e77e95e32904b294391d35779620e8d262127a7ab99.

- 2026-10-11T19:47:48+00:00: Recorded command exit 0; command argv SHA-256
  1a7e5d90dafbd72b5558a734390990d47e5418d247bc8a648ebfd7ce6ec138d2.

- 2026-10-11T19:47:56+00:00: Recorded command exit 0; command argv SHA-256
  4f8df750c52059d8635553b027b488846a11042048be7fbf9b169d768cc9b33c.

- 2026-10-11T19:48:29+00:00: Heartbeat by ar1782-coordinator-repair.

- 2026-10-11T19:48:30+00:00: Headroom repair added project-bound lifecycle coverage and refreshed
  diagnostic/provenance fixtures; signed exact head independently verified. Final clean coverage
  measurement is the remaining gate.

- 2026-10-11T19:48:59+00:00: Recorded command exit 0; command argv SHA-256
  0595a130fcc91554f444c68fea9ef76dbfed8d5b1eaeca807ca3bed0c813cd47.

- 2026-10-11T19:49:17+00:00: Recorded command exit 101; command argv SHA-256
  11aa7892ee38d3a937558ce5f68e38a693ff8b89e160ec2c02b25ddf17ea330b.

- 2026-10-11T19:49:46+00:00: Recorded command exit 0; command argv SHA-256
  0595a130fcc91554f444c68fea9ef76dbfed8d5b1eaeca807ca3bed0c813cd47.

- 2026-10-11T19:50:05+00:00: Recorded command exit 0; command argv SHA-256
  0f95a7f9172e2a97212e5dbb24d9696c5ff9cf610903dc5271d64450a1d5a9a6.

- 2026-10-11T19:51:20+00:00: Recorded command exit 0; command argv SHA-256
  11aa7892ee38d3a937558ce5f68e38a693ff8b89e160ec2c02b25ddf17ea330b.

- 2026-10-11T19:51:53+00:00: Recorded command exit 0; command argv SHA-256
  0595a130fcc91554f444c68fea9ef76dbfed8d5b1eaeca807ca3bed0c813cd47.

- 2026-10-11T19:52:11+00:00: Recorded command exit 0; command argv SHA-256
  0f95a7f9172e2a97212e5dbb24d9696c5ff9cf610903dc5271d64450a1d5a9a6.

- 2026-10-11T19:52:51+00:00: Heartbeat by ar1782-coordinator-repair.

- 2026-10-11T19:52:52+00:00: Clean full workspace llvm-cov completed at 90.22% lines against
  unchanged 90% floor; all tests and coverage gate passed. No source changes in verification run.

- 2026-10-11T19:56:15+00:00: Heartbeat by ar1782-coordinator-repair.

- 2026-10-11T19:56:15+00:00: Hosted policy gate reproducibly reports 89.97% (101063/101195), so
  merge remains blocked. Assign second headroom repair; all other observed checks have no product
  failure.

- 2026-10-11T19:59:10+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-11T19:59:12+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-11T19:59:28+00:00: Recorded command exit 1; command argv SHA-256
  ff20aea9b0bc559883aed2887b24e8d705857cfb012bd868bb645248a13560ba.

- 2026-10-11T20:00:47+00:00: Recorded command exit 101; command argv SHA-256
  5d64c193216d1be2aaeff68aecf69caf97aa349d2c5ff4deeb8ff3b6b4a136b7.

- 2026-10-11T20:01:57+00:00: Recorded command exit 0; command argv SHA-256
  15dea97d5832a35e57334c39b8e3b1b4553a2a41dd475a3bab3ec9f09aadcae8.

- 2026-10-11T20:02:16+00:00: Recorded command exit 101; command argv SHA-256
  c5e03b9da0e4360b9f35add581a1b1d30ff45fad3132e5c5c47cf4c52c195149.

- 2026-10-11T20:02:50+00:00: Recorded command exit 0; command argv SHA-256
  c5e03b9da0e4360b9f35add581a1b1d30ff45fad3132e5c5c47cf4c52c195149.

- 2026-10-11T20:03:13+00:00: Recorded command exit 0; command argv SHA-256
  83760dfa21a399b77e0bf8951c77dab0e2814121bb1d4b2d7fa767808d9b921c.

- 2026-10-11T20:03:16+00:00: Recorded command exit 0; command argv SHA-256
  cf220e791468443b5f7b6ed8baa0ffa18999fac69cd8802c26dc5e10e221d21b.

- 2026-10-11T20:03:22+00:00: Recorded command exit 0; command argv SHA-256
  d32df0a8f7802e39b9a6743613fff16ac35e4dddba3905aa783a204f77a7e43f.

- 2026-10-11T20:04:28+00:00: Recorded command exit 101; command argv SHA-256
  11aa7892ee38d3a937558ce5f68e38a693ff8b89e160ec2c02b25ddf17ea330b.

- 2026-10-11T20:04:42+00:00: Recorded command exit 0; command argv SHA-256
  ef19043205064ea87bec66574bfe246191c9311bc8c404cd8e347d08fbdc44f0.

- 2026-10-11T20:05:52+00:00: Recorded command exit 0; command argv SHA-256
  11aa7892ee38d3a937558ce5f68e38a693ff8b89e160ec2c02b25ddf17ea330b.

- 2026-10-11T20:05:59+00:00: Recorded command exit 0; command argv SHA-256
  565b04b503d6d7bfabfd2845aea0b91208d33abbc73adaaf208c27f9198d6768.

- 2026-10-11T20:06:05+00:00: Recorded command exit 0; command argv SHA-256
  0b96e10e29c6e70d787de4d0497366e66f47eed6083250a7ef07c77a8218677b.

- 2026-10-11T20:06:14+00:00: Recorded command exit 0; command argv SHA-256
  4f8df750c52059d8635553b027b488846a11042048be7fbf9b169d768cc9b33c.

- 2026-10-11T20:06:41+00:00: Heartbeat by ar1782-coordinator-repair.

- 2026-10-11T20:06:42+00:00: Second headroom repair added gzip archive and literature endpoint
  tests; clean workspace coverage is 90.23%, all focused gates pass, and signed exact head is
  d16375681b952934909d5ecbdd13e3d5ec361c4d.

- 2026-10-11T20:15:48+00:00: Heartbeat by ar1782-coordinator-repair.

- 2026-10-11T20:15:48+00:00: Hosted policy gate remains the sole failure at 89.99%; no
  floor/exclusion change authorized. Start final larger headroom repair.

- 2026-10-11T20:22:59+00:00: Heartbeat by ar1782-coordinator-repair.

- 2026-10-11T20:22:59+00:00: Final headroom repair added archive/lifecycle safety tests;
  hosted-equivalent coverage is 90.26%, signed exact head d6bddcabab5cfd1063a5f31c01c505f02f4b5d1a
  is clean. Fresh independent review required.

- 2026-10-11T20:24:09+00:00: Heartbeat by ar1782-coordinator-repair.

- 2026-10-11T20:24:09+00:00: Independent review blocked only on provenance drift: actual lib.rs
  SHA-256 1348bbd2... differs from recorded f0373063... after headroom tests. No source or gate
  defect found.

- 2026-10-11T20:24:14+00:00: Heartbeat by ar1782-coordinator-repair.

- 2026-10-11T20:24:16+00:00: Recorded command exit 0; command argv SHA-256
  b10a47fbbca97caa7dfa47da6f422ac333e03694b0df1729a7c0d044d44193bf.

- 2026-10-11T20:24:37+00:00: Recorded command exit 0; command argv SHA-256
  ef19043205064ea87bec66574bfe246191c9311bc8c404cd8e347d08fbdc44f0.

- 2026-10-11T20:25:05+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-11T20:25:15+00:00: Recorded command exit 0; command argv SHA-256
  a5e91d8a6e356ba88fd4835c765ebd2411c75eacaa60f98e203295ec257bd3a5.

- 2026-10-11T20:25:21+00:00: Recorded command exit 0; command argv SHA-256
  43ea9928318902aa9759fb71da6ab8f4065ad9187c052d4dbcfab10689b865dc.

- 2026-10-11T20:25:30+00:00: Recorded command exit 0; command argv SHA-256
  4f8df750c52059d8635553b027b488846a11042048be7fbf9b169d768cc9b33c.

- 2026-10-11T20:26:07+00:00: Heartbeat by ar1782-coordinator-repair.

- 2026-10-11T20:26:07+00:00: Provenance repair commit 3be3029d is SSH-signed+DCO, exact digest
  1348bbd2..., focused workflow transcript tests pass, and worktree is clean.

- 2026-10-11T20:37:07+00:00: Recorded command exit 0; command argv SHA-256
  5fd28450679fe0f026a4ece8457988112387518f7a55ba64de3246fcc7473b0f.

- 2026-10-11T20:37:30+00:00: Recorded command exit 0; command argv SHA-256
  fa5670793b16622fbc369fe99f679444b8ea527528c6564deb271d26604d921e.

- 2026-10-11T20:37:36+00:00: Recorded command exit 0; command argv SHA-256
  c97b034a991260112173af8a7610cc6dd21420b5ad53eecb15cb182da223c8fa.

- 2026-10-11T20:37:46+00:00: Recorded command exit 1; command argv SHA-256
  713c54e4549793b8533c11f13312f71c0275c27222e61a45ec3d67267fc55d51.

- 2026-10-11T20:37:59+00:00: Recorded command exit 0; command argv SHA-256
  45cd3a6588bbaf54a4e107b912c9bf1e8ae98d1d086587bf3525d7a8c61359b4.

- 2026-10-11T20:38:14+00:00: Heartbeat by ar1782-coordinator-repair.

- 2026-10-11T20:38:14+00:00: PR #584 merged through signed exact-tree two-parent merge 7ce4846 (base
  24cb72d, reviewed head 3be3029d, tree 842ebc25). Ten post-merge workflows are in progress; do not
  release yet.

- 2026-10-11T20:50:26+00:00: Recorded command exit 0; command argv SHA-256
  c3e3e42ed6378cde65b6e9bc375fc62ca59e70e785d1f0da4c57b4a3a331ca85.

- 2026-10-11T20:51:08+00:00: Heartbeat by ar1782-coordinator-repair.

- 2026-10-11T20:51:14+00:00: All 10 exact-main workflows are terminal-success. The attempted
  post-merge workspace run ended, but its integration worktree was at pre-merge base 24cb72d, so it
  is invalid evidence; AR remains in progress.

- 2026-10-11T20:51:59+00:00: Recorded command exit 0; command argv SHA-256
  8835ca6afa124b5f0cfd058e18f654c75cfea93cbe35cb3c57d7948687d35db1.

- 2026-10-11T20:52:14+00:00: Recorded command exit 0; command argv SHA-256
  ba24acbef326ec8e9d32a20b23bfddb0dd2065f6246d9f7ae97d747bd72e60d0.

- 2026-10-11T20:52:24+00:00: Recorded command exit 0; command argv SHA-256
  1172e94c0a9b2ad3427bfc988a1f8c38426761909bf198baba8529e4224c8779.

- 2026-10-11T20:52:35+00:00: Recorded command exit 0; command argv SHA-256
  0840177781a306f9cac27df908d14e7b5801294074d8c0421041db9a4a0e19c4.

- 2026-10-11T20:54:14+00:00: Recorded command exit 0; command argv SHA-256
  5158ce0410fcd0ea3ce87276a5bb4bf6fb074f7f17c67aae96f9561c9f58459d.

- 2026-10-11T20:54:29+00:00: Recorded command exit 0; command argv SHA-256
  6b58f28136c1c504956244d600801fee5cc8b7b8ff6c84e8ecc3b2e561241830.

- 2026-10-11T20:55:45+00:00: Heartbeat by ar1782-coordinator-repair.

- 2026-10-11T20:57:14+00:00: Recorded command exit 0; command argv SHA-256
  f6afff9379f09b79fd401f28971c62953b4b1993932538a5908401c783a0e0b9.

- 2026-10-11T20:57:16+00:00: Recorded command exit 0; command argv SHA-256
  8ee7e06cbf2fce8c635b1fa102e13e1c933ff90ceb67105832e260738a46d084.

- 2026-10-11T20:57:29+00:00: Independent post-merge acceptance: exact merge, full workspace test,
  all post-merge workflows, signature/DCO, clean worktree, and live doctor verified.

- 2026-10-11T20:57:31+00:00: PR #584 merged at 7ce484612db043831e4acb995839455f512197c0 with exact
  reviewed head 3be3029d7a1d927b86b4ae938abfc939d8339009; exact merge signature/DCO, full locked
  workspace test, 10/10 post-merge workflows, clean worktree, and doctor verified; acceptance
  receipt recorded.
