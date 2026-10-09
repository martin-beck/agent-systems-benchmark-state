---
{
  "branch": "feature/ar-1761-tool-install-registry",
  "checkpoint_commit": "c34a3d6b52b009d62a513bae6713e748b9dbd1fb",
  "claim_expires": "2026-10-09T18:30:21+00:00",
  "depends_on": [
    "AR-1759",
    "AR-1760"
  ],
  "id": "AR-1761",
  "next_action": "Push exact clean head b95c89d to PR #534; verify exact current base and request fresh independent review/CI. Do not merge until all required checks are green.",
  "observed_branch": "feature/ar-1761-tool-install-registry",
  "observed_dirty": 0,
  "observed_head": "b95c89db086a2eff04f1ada7bf0ce9df7de067b4",
  "owner": "codex-asb-ar1761-tool-install-20261009",
  "plan": "../plans/AR-1761-tool-install-registry.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1761.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1761.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Install supported external ASB tools into a user/project-local root and persist validated records.",
  "task_revision": 138,
  "title": "ASB external-tool installer and registry",
  "updated_at": "2026-10-09T16:34:46+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1761-tool-install-registry"
}
---

Add a clear `asb tool install <id> --kind agent|harness|benchmark|workload|support`
command (with source/version/project and `--json` options) backed by an
extensible, bounded installer registry. It must support the external tools ASB
actually uses, install without root into a user/project-local location, record
the executable/root/source/version/platform/digest/capabilities in the project
config, and give an explicit unsupported-tool diagnostic rather than executing
arbitrary shell. Add status/list/remove or repair behavior only where needed
for idempotence; never store API keys or tokens.

- 2026-10-09T15:40:58+00:00: dependencies AR-1759 and AR-1760 verified accepted/released;
  implementation ready

- 2026-10-09T15:41:04+00:00: Claimed by codex-asb-ar1761-tool-install-20261009.

- 2026-10-09T15:41:15+00:00: Recorded command exit 0; command argv SHA-256
  8781f7f86432da71cf00304d47062d61aa5ed8ccbac43c32fffb341be9c007fd.

- 2026-10-09T15:41:35+00:00: Recorded command exit 0; command argv SHA-256
  c18ed43a4423686964d2b9e91943401cda7e5651ce092cd08b41811163bc1613.

- 2026-10-09T15:41:48+00:00: Recorded command exit 0; command argv SHA-256
  ec48e1d504dbb949df2606165a2406335cb4529dc7cbd9a666569760fe08df68.

- 2026-10-09T15:43:33+00:00: Recorded command exit 1; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T15:43:47+00:00: Recorded command exit 0; command argv SHA-256
  a917c5c96bb0f888caae50bea885d24f8c7158927e33da92e7b5c2eb9571981b.

- 2026-10-09T15:43:57+00:00: Recorded command exit 101; command argv SHA-256
  a37d35e290b63ddfe8627f9bdb0474ef6d3f2654ade91f05cd9a55c3a713fceb.

- 2026-10-09T15:44:27+00:00: Recorded command exit 0; command argv SHA-256
  081af90c8024d255817953c561fd64d176b2fb9188b0198239fe3000831623e8.

- 2026-10-09T15:44:46+00:00: Recorded bounded retry: initial handoffctl cargo check invocation
  failed with exit 101 because wrapper cwd is the state repository and no Cargo.toml was present.
  Repaired by invoking cargo with the product worktree manifest path; cargo check --locked
  --workspace then passed.

- 2026-10-09T15:45:17+00:00: Recorded command exit 0; command argv SHA-256
  e01e5d95dc6ad658cdb3d81caaf78261e9db1f1e205dec5cad0059c1304ba2f1.

- 2026-10-09T15:45:41+00:00: Recorded command exit 0; command argv SHA-256
  a917c5c96bb0f888caae50bea885d24f8c7158927e33da92e7b5c2eb9571981b.

- 2026-10-09T15:45:53+00:00: Recorded command exit 101; command argv SHA-256
  2607424c3654ceee26fa86e853d746acc9c602695281098ece205d223d115425.

- 2026-10-09T15:46:19+00:00: Recorded command exit 0; command argv SHA-256
  1de8f9ad957f9d922fc8cf742b621ec607aa4aa6d2a7b12e7f0ad69c06e24dd8.

- 2026-10-09T15:46:33+00:00: Focused tool tests first failed with exit 101 because the idempotence
  comparison included the generated record path/kind capability representation differently from the
  persisted record. Diagnosis is in progress; no publication was attempted.

- 2026-10-09T15:46:39+00:00: Recorded command exit 0; command argv SHA-256
  c08b6829368d7782d20a983c1344b00955db57c4e510ac63f32a16ec1bc08693.

- 2026-10-09T15:47:01+00:00: Recorded command exit 0; command argv SHA-256
  a917c5c96bb0f888caae50bea885d24f8c7158927e33da92e7b5c2eb9571981b.

- 2026-10-09T15:47:17+00:00: Recorded command exit 0; command argv SHA-256
  2607424c3654ceee26fa86e853d746acc9c602695281098ece205d223d115425.

- 2026-10-09T15:47:37+00:00: Repaired exit-101 focused test failure: ProjectConfigV1 source
  validation rejected the documented fixture:// source vocabulary. Extended the closed source
  validator to allow fixture:// only; unsupported network schemes and symlink/local-source checks
  remain fail-closed. Focused tool install/list/status/remove tests now pass (5/5).

- 2026-10-09T15:48:11+00:00: Recorded command exit 0; command argv SHA-256
  a917c5c96bb0f888caae50bea885d24f8c7158927e33da92e7b5c2eb9571981b.

- 2026-10-09T15:48:26+00:00: Recorded command exit 0; command argv SHA-256
  2607424c3654ceee26fa86e853d746acc9c602695281098ece205d223d115425.

- 2026-10-09T15:48:47+00:00: Recorded command exit 0; command argv SHA-256
  a917c5c96bb0f888caae50bea885d24f8c7158927e33da92e7b5c2eb9571981b.

- 2026-10-09T15:48:58+00:00: Recorded command exit 0; command argv SHA-256
  56d8695c759a8fa655669ce488499148d7d5f3aa5cd864b645edfddaa37bb475.

- 2026-10-09T15:49:19+00:00: Checkpointed source commit c34a3d6b52b009d62a513bae6713e748b9dbd1fb.

- 2026-10-09T15:49:29+00:00: Recorded command exit 1; command argv SHA-256
  882a2b0d15036ccccb540d14aabe9077fdf6a4b45684ccd1b5e7fecfe60460c8.

- 2026-10-09T15:49:49+00:00: Full-gate attempt failed before running Clippy: cargo fmt received
  --manifest-path after the rustfmt separator and exited 101 because the wrapper cwd is the state
  checkout. No product mutation or publication occurred; retry will pass manifest-path before --.

- 2026-10-09T15:50:07+00:00: Recorded command exit 101; command argv SHA-256
  196a03c6abea2f1ab0074c6b051e942da5ffb3890376e4b7829efa4f18e52d99.

- 2026-10-09T15:50:19+00:00: Clippy gate found two repairable diagnostics in the new installer:
  needless lifetime on tool_kind_map and collapsible nested existing-record check. No warnings were
  suppressed; both will be fixed and the gate rerun.

- 2026-10-09T15:50:42+00:00: Recorded command exit 0; command argv SHA-256
  196a03c6abea2f1ab0074c6b051e942da5ffb3890376e4b7829efa4f18e52d99.

- 2026-10-09T15:50:57+00:00: Recorded command exit 0; command argv SHA-256
  12c5a0c25969608b54243850925121707a01fd86f994ac3fe287fe07838341cf.

- 2026-10-09T15:51:37+00:00: Recorded command exit 101; command argv SHA-256
  224f23823c49769ec0e2e458fdd3da95be1cb852070fa5d2c7fd088f4ad98da0.

- 2026-10-09T15:51:47+00:00: Full workspace tests found one expected contract-test drift after
  adding the tool command: capability_contract expected the old completion list and failed. Updated
  the assertion to include tool; no feature failure or publication occurred.

- 2026-10-09T15:51:56+00:00: Recorded command exit 0; command argv SHA-256
  4f3c9574d6c9114953dc0619fbe84dd55c36e97c4f48fff6b047f334d41e7b4c.

- 2026-10-09T15:52:23+00:00: Recorded command exit 101; command argv SHA-256
  224f23823c49769ec0e2e458fdd3da95be1cb852070fa5d2c7fd088f4ad98da0.

- 2026-10-09T15:53:03+00:00: Full workspace tests then found provenance fixture drift after the CLI
  source changed: workflow_transcript failed with the stale cli_source_sha256. Updated only the
  checked-in provenance digest to the exact current lib.rs hash; no behavior bypass or gate
  weakening.

- 2026-10-09T15:53:39+00:00: Recorded command exit 0; command argv SHA-256
  4f4874fc5379a1cb5d8e3eabce9189c6823aac3d3d9fe3893360bb9c1e352a14.

- 2026-10-09T15:53:43+00:00: Recorded command exit 0; command argv SHA-256
  f4ae0486eb145e238580635a490fd0b17013e3bf6e5d9727d1cf4e2823a32f73.

- 2026-10-09T15:54:39+00:00: Recorded command exit 0; command argv SHA-256
  33eb802aab5f68cf0afa5c74694665c81105746e9f87902b0ec0525673b14972.

- 2026-10-09T15:54:58+00:00: Full applicable local gates pass: format check, Clippy with warnings
  denied, workspace tests (including workflow provenance), rustdoc with -D warnings, and locked
  release build. Exact implementation branch is clean at 9bfff7a with signed/DCO commits.

- 2026-10-09T15:55:06+00:00: Recorded command exit 0; command argv SHA-256
  22ba60c5dff3e4a6c5e63eac8a9d101d98606e0c4e95e554b38bda6f9956d065.

- 2026-10-09T15:55:22+00:00: Recorded command exit 0; command argv SHA-256
  6bc71a81c4ea1150dbbd57c6b78d3b4d22542b9e10858d5fa181b1c7bc96c2ab.

- 2026-10-09T15:56:08+00:00: Published PR #534 from clean exact signed head
  9bfff7aa4e2b05cf217cb505678ee0e9ce1259ca. Hosted required checks are in progress; no approval or
  merge has been performed. Independent review remains required before integration.

- 2026-10-09T15:58:52+00:00: Heartbeat by codex-asb-ar1761-tool-install-20261009.

- 2026-10-09T16:08:00+00:00: Recorded command exit 0; command argv SHA-256
  efc0024d8c2da48154d16c336ace72766a6fbf6161d6329400455015bf4520d8.

- 2026-10-09T16:08:26+00:00: Recorded command exit 101; command argv SHA-256
  efc0024d8c2da48154d16c336ace72766a6fbf6161d6329400455015bf4520d8.

- 2026-10-09T16:08:39+00:00: Recorded command exit 0; command argv SHA-256
  2d1e6d6efe7836eba14e23220ef9ad7b99bc6bd01e6d34be58a41cea76bfb747.

- 2026-10-09T16:09:07+00:00: Recorded command exit 0; command argv SHA-256
  824cb7cfbc699838a005b3f55ed44d18f9c1804d40c608d46f7e469b7deb9fb3.

- 2026-10-09T16:11:24+00:00: Recorded command exit 1; command argv SHA-256
  d80365906793d8451a4a3605ec3948f7108fe261100a3640997838ee3778c61b.

- 2026-10-09T16:11:56+00:00: Recorded command exit 0; command argv SHA-256
  3908391941b149d87cd18c760b34fdc3ae214bcacccce9740d77b64a2bbe405d.

- 2026-10-09T16:12:50+00:00: Heartbeat by codex-asb-ar1761-tool-install-20261009.

- 2026-10-09T16:12:57+00:00: Recorded command exit 0; command argv SHA-256
  f660170bbb8ca494c8aaf72dae9adb4f0b31ec4f53306907274ffc6ed80832c0.

- 2026-10-09T16:13:11+00:00: Recorded command exit 1; command argv SHA-256
  0debb00bbb01341575447426575074b9a75508df324587117c8951792c7a3c00.

- 2026-10-09T16:13:27+00:00: Recorded command exit 101; command argv SHA-256
  2607424c3654ceee26fa86e853d746acc9c602695281098ece205d223d115425.

- 2026-10-09T16:13:53+00:00: Recorded command exit 0; command argv SHA-256
  a917c5c96bb0f888caae50bea885d24f8c7158927e33da92e7b5c2eb9571981b.

- 2026-10-09T16:14:12+00:00: Recorded command exit 101; command argv SHA-256
  2607424c3654ceee26fa86e853d746acc9c602695281098ece205d223d115425.

- 2026-10-09T16:14:31+00:00: Recorded command exit 0; command argv SHA-256
  a917c5c96bb0f888caae50bea885d24f8c7158927e33da92e7b5c2eb9571981b.

- 2026-10-09T16:14:40+00:00: Recorded command exit 0; command argv SHA-256
  2607424c3654ceee26fa86e853d746acc9c602695281098ece205d223d115425.

- 2026-10-09T16:14:55+00:00: Recorded command exit 0; command argv SHA-256
  1178411481f18b826842d37a3b9a5ab5a571c081b00edfbecbf0bba4703c92b4.

- 2026-10-09T16:15:12+00:00: PR #534 repository-quality run 37955302155 failed its unchanged 90%
  workspace line-coverage floor at 88.18% (131495 lines, 15541 missed); floor was not weakened.
  Repaired with signed DCO commit 22d8de5 adding positive and negative tool installer
  parser/source/conflict/status/config branch coverage; focused 6-test suite passes.

- 2026-10-09T16:15:40+00:00: Recorded command exit 101; command argv SHA-256
  1f32d821ac2a92b7218d30afafdfa184d4a057db7d34e8f1eb937c776dbcda2a.

- 2026-10-09T16:15:49+00:00: Recorded command exit 0; command argv SHA-256
  b8149b3191ace2123d57711b6849cef3bda7cc953e8b01d2c7079e833470bb3c.

- 2026-10-09T16:16:43+00:00: Recorded command exit 0; command argv SHA-256
  1f32d821ac2a92b7218d30afafdfa184d4a057db7d34e8f1eb937c776dbcda2a.

- 2026-10-09T16:16:53+00:00: Recorded command exit 2; command argv SHA-256
  428457ea9cc6a21bd46c5be6651ba2faccb5b0b07ddc2fd6f96eca730dea5ab7.

- 2026-10-09T16:18:23+00:00: Recorded command exit 0; command argv SHA-256
  92195fe1416227cda697bf350b319e1b2468404b7845794d2e1518621ffa6a91.

- 2026-10-09T16:18:36+00:00: Recorded command exit 0; command argv SHA-256
  f660170bbb8ca494c8aaf72dae9adb4f0b31ec4f53306907274ffc6ed80832c0.

- 2026-10-09T16:18:45+00:00: Heartbeat by codex-asb-ar1761-tool-install-20261009.

- 2026-10-09T16:18:54+00:00: Coverage repair validated locally: full workspace quality, clippy,
  tests, rustdoc, release build all pass; check_coverage.py passes unchanged 90% workspace line
  floor (workspace 90.39% lines; critical packages all above 95%). New signed+DCO head is 644085e
  after provenance refresh. Generated profraw files were removed from the checkout.

- 2026-10-09T16:19:00+00:00: Recorded command exit 0; command argv SHA-256
  a301b4dd020ecbd9133885963264b8daa5f92c08e4a01bd45bdb67d93ba062bd.

- 2026-10-09T16:19:16+00:00: Recorded command exit 0; command argv SHA-256
  bbf6437efaaf991a4ca0ea750b9285a4812442bd08a4c916387c1daeaccf1e7b.

- 2026-10-09T16:19:32+00:00: Remote PR #534 verified clean exact head
  644085ecd2f3758aa3482b8a60d4e2ddf099f0c1 against base ea5e52bfe843969c493f22146f66ccfa2415159a
  after handoffctl push. PR is OPEN, non-draft, reviewDecision empty, and statusCheckRollup
  currently empty while GitHub schedules checks.

- 2026-10-09T16:19:39+00:00: Heartbeat by codex-asb-ar1761-tool-install-20261009.

- 2026-10-09T16:19:47+00:00: Recorded command exit 1; command argv SHA-256
  d34f24cd2d9e2ec4c4bef5dca888ec312a5b26e36ca5fefd23b0dcf954f2d1d9.

- 2026-10-09T16:20:33+00:00: Heartbeat by codex-asb-ar1761-tool-install-20261009.

- 2026-10-09T16:20:40+00:00: Recorded command exit 1; command argv SHA-256
  d34f24cd2d9e2ec4c4bef5dca888ec312a5b26e36ca5fefd23b0dcf954f2d1d9.

- 2026-10-09T16:22:17+00:00: Heartbeat by codex-asb-ar1761-tool-install-20261009.

- 2026-10-09T16:22:20+00:00: Recorded command exit 0; command argv SHA-256
  b5bea41b6c623f7c09f1bf24dcae58ebab3c0cdd90ad966bc43a45b44867e12b.

- 2026-10-09T16:22:33+00:00: Independent review of exact PR #534 head
  644085ecd2f3758aa3482b8a60d4e2ddf099f0c1: complete diff/docs/contracts reviewed; cargo fmt check,
  focused tool tests (6/6), clippy -D warnings, and diff check pass. However, a blocking path-safety
  finding remains: tool_install checks destination.exists() and reads bytes before checking symlink
  metadata, so an existing .asb/tools/<id>/tool symlink to matching bytes is accepted and persisted.
  Reproduced in a disposable fixture: install exited 0 and retained the symlink target. This
  violates the documented symlink/path-safe contract and must be repaired by rejecting destination
  symlinks (and safely validating the destination inode/type) before any digest comparison. No
  approval or merge recommendation.

- 2026-10-09T16:24:10+00:00: Heartbeat by codex-asb-ar1761-tool-install-20261009.

- 2026-10-09T16:24:33+00:00: Recorded command exit 0; command argv SHA-256
  a917c5c96bb0f888caae50bea885d24f8c7158927e33da92e7b5c2eb9571981b.

- 2026-10-09T16:24:45+00:00: Recorded command exit 0; command argv SHA-256
  2607424c3654ceee26fa86e853d746acc9c602695281098ece205d223d115425.

- 2026-10-09T16:24:58+00:00: Recorded command exit 0; command argv SHA-256
  c32e71f606a1b2be814e9a98750e329dca7c591ad50ff98aa4ea184f18974ede.

- 2026-10-09T16:25:12+00:00: Recorded command exit 0; command argv SHA-256
  5cdb732b0f4d851fdd6495659bcc2ce53959cfeccd4b036916c4e6efc5dbae7b.

- 2026-10-09T16:25:24+00:00: Recorded command exit 0; command argv SHA-256
  9747de804a661239fdf4185a7ee6fe3e1d5201cd1b14e4d73c4982b9f2975a8f.

- 2026-10-09T16:25:43+00:00: Recorded command exit 1; command argv SHA-256
  7f6e958dc25903677768417a8fc57b0457c385bb3005fc77b8cc053ff84c6e02.

- 2026-10-09T16:26:16+00:00: Recorded command exit 0; command argv SHA-256
  0bd80b3e4e6943dc8a34b48e3e4366e9ace6ae904bc357fa703d6cca0c4708cf.

- 2026-10-09T16:27:00+00:00: Recorded command exit 101; command argv SHA-256
  1f32d821ac2a92b7218d30afafdfa184d4a057db7d34e8f1eb937c776dbcda2a.

- 2026-10-09T16:27:31+00:00: Recorded command exit 0; command argv SHA-256
  a917c5c96bb0f888caae50bea885d24f8c7158927e33da92e7b5c2eb9571981b.

- 2026-10-09T16:27:44+00:00: Recorded command exit 101; command argv SHA-256
  2607424c3654ceee26fa86e853d746acc9c602695281098ece205d223d115425.

- 2026-10-09T16:27:58+00:00: Recorded command exit 0; command argv SHA-256
  a917c5c96bb0f888caae50bea885d24f8c7158927e33da92e7b5c2eb9571981b.

- 2026-10-09T16:28:11+00:00: Recorded command exit 0; command argv SHA-256
  2607424c3654ceee26fa86e853d746acc9c602695281098ece205d223d115425.

- 2026-10-09T16:28:22+00:00: Recorded command exit 0; command argv SHA-256
  85234b62dca6d94a419aca9b10f8cb6db6eec9cb98a00c6a0dd9ef1a8303001f.

- 2026-10-09T16:28:57+00:00: Recorded command exit 101; command argv SHA-256
  1f32d821ac2a92b7218d30afafdfa184d4a057db7d34e8f1eb937c776dbcda2a.

- 2026-10-09T16:29:12+00:00: Recorded command exit 101; command argv SHA-256
  f4f0dd6b02d0c6c1b997d17a4b74b14c2188895e1a48284e5b01370af8fbdf4b.

- 2026-10-09T16:29:28+00:00: Recorded command exit 2; command argv SHA-256
  8025304f2eec020a68048051a895bdc817ee225246ec1474f976e393e745df02.

- 2026-10-09T16:29:54+00:00: Recorded command exit 0; command argv SHA-256
  a917c5c96bb0f888caae50bea885d24f8c7158927e33da92e7b5c2eb9571981b.

- 2026-10-09T16:30:21+00:00: Heartbeat by codex-asb-ar1761-tool-install-20261009.

- 2026-10-09T16:30:33+00:00: Recorded command exit 0; command argv SHA-256
  43c45257a7de28c04cf0c4019d183ca3920bc44cd8582652567f03380dbb27f8.

- 2026-10-09T16:30:39+00:00: Recorded command exit 101; command argv SHA-256
  369436ccf7999ac35333abf2860dd00480bfe023cc55e434ee9047afda9ebbf7.

- 2026-10-09T16:30:51+00:00: Recorded command exit 0; command argv SHA-256
  369436ccf7999ac35333abf2860dd00480bfe023cc55e434ee9047afda9ebbf7.

- 2026-10-09T16:31:00+00:00: Recorded command exit 0; command argv SHA-256
  2f4bca528f56592c5c112d12eeb9cb509c1cb08df74c8cb006769b13c0536abe.

- 2026-10-09T16:32:17+00:00: Recorded command exit 0; command argv SHA-256
  1f32d821ac2a92b7218d30afafdfa184d4a057db7d34e8f1eb937c776dbcda2a.

- 2026-10-09T16:33:55+00:00: Recorded command exit 0; command argv SHA-256
  92195fe1416227cda697bf350b319e1b2468404b7845794d2e1518621ffa6a91.

- 2026-10-09T16:34:09+00:00: Recorded command exit 0; command argv SHA-256
  f660170bbb8ca494c8aaf72dae9adb4f0b31ec4f53306907274ffc6ed80832c0.

- 2026-10-09T16:34:22+00:00: Independent review repair complete. Signed+DCO 6ca69c7 rejects existing
  tool destination symlinks before any digest/read and requires regular-file metadata; regression
  test proves matching-byte symlink target is untouched. Current base f361cfc was merged in
  signed+DCO 200c5e3. Main reconciliation required signed+DCO a983e2b/b95c89d to register tool in
  human command classifier and golden contracts. Focused 7 installer tests plus all 14 human CLI
  tests pass. Full format/clippy/workspace tests/rustdoc/release build pass. Coverage passes
  unchanged floors: workspace 90.54% lines, asb-core 99.61%, asb-protocol 96.49%, asb-replay 95.88%.
  Removed generated profraw files.

- 2026-10-09T16:34:32+00:00: Recorded command exit 0; command argv SHA-256
  a301b4dd020ecbd9133885963264b8daa5f92c08e4a01bd45bdb67d93ba062bd.

- 2026-10-09T16:34:46+00:00: Recorded command exit 0; command argv SHA-256
  5208d5eddf4d44c41ad0deac967c1d67667705e97bd74985c07c03aaeba32053.
