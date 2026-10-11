---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1699",
    "AR-1700",
    "AR-1723",
    "AR-1724",
    "AR-1733"
  ],
  "id": "AR-1754",
  "next_action": "PR #558 now points to exact signed head 0dcd1472. The hosted Rust failure was a stale workflow provenance digest; it is repaired and the focused workflow-transcript gate passes locally. Independently review the complete diff, then wait for all 15 exact-head checks to reach terminal success. No GitHub Reviews API approval object is required; merge only through the documented signed protected-main procedure.",
  "owner": "",
  "plan": "../plans/AR-1754-default-online-live-workflow.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "hosted",
    "evidence_digest": "sha256:4e56abadaeaa886980ea42a8ae3ef022f5f3f1d36982d0285b7bf9b200168c23",
    "evidence_ref": "quality/AR-1754-default-online-postmerge-receipt.json",
    "spec_ref": "specs/AR-1754.json",
    "spec_revision": 1,
    "status": "pass"
  },
  "spec_ref": "specs/AR-1754.json",
  "spec_revision": 1,
  "status": "done",
  "summary": "Make configured online/live provider execution the default for canonical run, sweep, easy, recording/campaign, and TUI handoff paths while keeping local mock and strict replay explicit alternatives.",
  "task_revision": 111,
  "title": "Make online execution the default across ASB workflows",
  "updated_at": "2026-10-11T03:39:35+00:00",
  "worktree_key": ""
}
---

The user-facing ASB workflow currently requires explicit online/live flags in
several places and makes `asb easy run|sweep` local-mock-only. Define one
consistent development contract: configured online provider execution is the
default, while `--local-mock` is an explicit credential-free alternative and
strict offline replay remains explicit. A live failure must remain a typed
failure; it must never silently fall back to mock or replay.

Cover canonical `run`, `sweep`, `benchmark-live`, `record-live`, recording
campaigns, `asb easy` commands, and the ASB/TUI handoff/configuration contract.
Do not modify the separate asb-tui repository in this AR; publish any required
cross-repository contract and dependency notes in the state plan. Preserve
credential-reference-only configuration, bounded progress, network/cost
warnings, provider/model/agent/workload identity, and all existing fail-closed
production authority checks.

- 2026-10-11T02:17:31+00:00: Dependencies AR-1699, AR-1700, AR-1723, AR-1724, and AR-1733 are
  released/current; promote for canonical online-default integration.

- 2026-10-11T02:17:38+00:00: Claimed by codex-ar1754-online-integration.

- 2026-10-11T02:17:46+00:00: Recorded command exit 0; command argv SHA-256
  904023b98f9c92c714e92042ea44849c3dc5cd79aee9bc2c4f6c2da4145ad191.

- 2026-10-11T02:19:31+00:00: Recorded command exit 101; command argv SHA-256
  56e66b0bd6b13838995dbe88c5b57a45c337007ffea52ed3e4fef3fe9a121b86.

- 2026-10-11T02:20:28+00:00: Recorded command exit 1; command argv SHA-256
  2640793016b9144188de39b32560b8e0bd1213cc844ee2f20b39d5e197ffb7be.

- 2026-10-11T02:20:31+00:00: Recorded command exit 0; command argv SHA-256
  c9b2d9ebecb13115258e662490978a2e2e84bf44fd4af7bd0795c4fe3905f166.

- 2026-10-11T02:21:20+00:00: Recorded command exit 0; command argv SHA-256
  56e66b0bd6b13838995dbe88c5b57a45c337007ffea52ed3e4fef3fe9a121b86.

- 2026-10-11T02:22:17+00:00: Recorded command exit 0; command argv SHA-256
  2b0c9cb4a2554e7e091651501f93c5f0fb1946899b15da96b5bb7ee72971131d.

- 2026-10-11T02:23:10+00:00: Recorded command exit 101; command argv SHA-256
  2640793016b9144188de39b32560b8e0bd1213cc844ee2f20b39d5e197ffb7be.

- 2026-10-11T02:24:29+00:00: Recorded command exit 0; command argv SHA-256
  b5bea41b6c623f7c09f1bf24dcae58ebab3c0cdd90ad966bc43a45b44867e12b.

- 2026-10-11T02:24:50+00:00: Recorded command exit 0; command argv SHA-256
  ce21884ced71789f65656793d4d30c9d0e99bbdb220e0cbe03652c5deb5418a5.

- 2026-10-11T02:24:53+00:00: Recorded command exit 0; command argv SHA-256
  d359c8c2c51a46c67222ccd336cda4aa608863df9cc790abedc47759ca8ae2a6.

- 2026-10-11T02:25:12+00:00: Recorded command exit 0; command argv SHA-256
  c75ed860523a165a754ae3874851f69b8742199e109ef5e19da40af2f02bf4fb.

- 2026-10-11T02:25:15+00:00: Recorded command exit 0; command argv SHA-256
  cddfd45995ac3b485d0e12f389dc008a425c1cb747b5c7dab0edb69284483137.

- 2026-10-11T02:25:34+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-11T02:25:38+00:00: Recorded command exit 1; command argv SHA-256
  71423a8987b2a4357131676a137bd93d92c8f2769116fa49a16efd3e972f5f82.

- 2026-10-11T02:25:56+00:00: Recorded command exit 0; command argv SHA-256
  df12ff05ae0928196f2662293dc4f577c012fe72ff368d9692885ca58060d464.

- 2026-10-11T02:26:21+00:00: Recorded command exit 0; command argv SHA-256
  899f1337394fe97b9698fe19f3bd7685bb644ddbf920e6c087c55d632b5cc644.

- 2026-10-11T02:26:42+00:00: Recorded command exit 1; command argv SHA-256
  71423a8987b2a4357131676a137bd93d92c8f2769116fa49a16efd3e972f5f82.

- 2026-10-11T02:27:02+00:00: Recorded command exit 0; command argv SHA-256
  14fc5cce6bc1423f2d47bfbbaa839f23fc7389159b81a481c78ae2e851487ea5.

- 2026-10-11T02:27:23+00:00: Recorded command exit 1; command argv SHA-256
  71423a8987b2a4357131676a137bd93d92c8f2769116fa49a16efd3e972f5f82.

- 2026-10-11T02:27:46+00:00: Recorded command exit 0; command argv SHA-256
  6298def3105d3e0345f7417fe7d0e73ad1cd922e4d68256342ce54665d4b6bc9.

- 2026-10-11T02:27:55+00:00: Recorded command exit 0; command argv SHA-256
  8a9c71d32ea42e1e2f0410318eca9828a886e62b128551a3ecd825655bb04afa.

- 2026-10-11T02:28:04+00:00: Recorded command exit 101; command argv SHA-256
  e6c3c60a7af791e078ffb64c7822f84b111943ab5bb57c21b22e3362bdf94f20.

- 2026-10-11T02:28:39+00:00: Recorded command exit 0; command argv SHA-256
  b68bb4a201585a694b08c56aa10de17e796ce9e2ea14278d1329604174df9f29.

- 2026-10-11T02:29:16+00:00: Recorded command exit 0; command argv SHA-256
  d972377170b70e831ac3d42e98855805e3bd30561640473ce544ffcd9f984be6.

- 2026-10-11T02:29:24+00:00: Recorded command exit 0; command argv SHA-256
  bdf72f3d98e9ffe2ca0f903b5a20e9bd6cba295c4c814f8326904ebaa953dd2c.

- 2026-10-11T02:29:31+00:00: Recorded command exit 0; command argv SHA-256
  62202b9f053f320659448842ffb64a635cd15c95699ad77b6d4488848c63ea47.

- 2026-10-11T02:29:43+00:00: Recorded command exit 0; command argv SHA-256
  70743d2f466e120aa382787de0a4e1e13ccec192978d4a2c77b4cb437e5652a8.

- 2026-10-11T02:29:58+00:00: Recorded command exit 0; command argv SHA-256
  cde28356e41ef2731532cbb9e97314b094f95b9838b287252d85503913314b3d.

- 2026-10-11T02:30:10+00:00: Heartbeat by codex-ar1754-online-integration.

- 2026-10-11T02:30:54+00:00: Published PR #558 for configured/provider-selection online-default
  routing and explicit --local-mock alternatives. Focused asb-cli tests pass 342/342; exact-head CI
  is pending.

- 2026-10-11T02:31:17+00:00: Recorded command exit 0; command argv SHA-256
  bfcd8377481dd678156d8333e623b11e47d40938e533ed787ff1d70de31bde9f.

- 2026-10-11T02:31:26+00:00: Recorded command exit 0; command argv SHA-256
  1414247d14c7a1648e2b5b9bb041e7da83a1044a2eb327fcbed41b1f8dce9cad.

- 2026-10-11T02:31:34+00:00: Recorded command exit 0; command argv SHA-256
  91a5ff998aa74996084f8bb3be42b0f6e26651f0bf4b2c04e34613c24dfceb55.

- 2026-10-11T02:31:42+00:00: Recorded command exit 0; command argv SHA-256
  d1d08a52fc114878aa75f329e3896cc0d93dafe70c96fb2a2d8314a60dfe53f2.

- 2026-10-11T02:31:53+00:00: Recorded command exit 0; command argv SHA-256
  8a9c71d32ea42e1e2f0410318eca9828a886e62b128551a3ecd825655bb04afa.

- 2026-10-11T02:32:33+00:00: Recorded command exit 0; command argv SHA-256
  b68bb4a201585a694b08c56aa10de17e796ce9e2ea14278d1329604174df9f29.

- 2026-10-11T02:32:37+00:00: Recorded command exit 0; command argv SHA-256
  bdf72f3d98e9ffe2ca0f903b5a20e9bd6cba295c4c814f8326904ebaa953dd2c.

- 2026-10-11T02:32:48+00:00: Recorded command exit 0; command argv SHA-256
  2682824cac520368a97bc56f4d94739482ddbe374b8d07901f8981b7199f14c5.

- 2026-10-11T02:32:59+00:00: Recorded command exit 0; command argv SHA-256
  adb32bf6a74b6b627f01047b0737454d216f0735b258693015fde95a32b063ce.

- 2026-10-11T02:33:30+00:00: Heartbeat by codex-ar1754-online-integration.

- 2026-10-11T02:33:33+00:00: Added default-online direct/easy record-live with explicit --local-mock
  override; cargo fmt and focused asb-cli tests pass 342/342. PR #558 was force-with-lease updated
  to c943c276; exact-head CI restarted.

- 2026-10-11T02:36:46+00:00: Heartbeat by codex-ar1754-online-integration.

- 2026-10-11T02:38:54+00:00: Recorded command exit 0; command argv SHA-256
  920839c6cb028a0862c32cfc1537be086f9f88ab2cd1804bf4cb07beccf9de07.

- 2026-10-11T02:39:14+00:00: Recorded command exit 101; command argv SHA-256
  3624c529276fa502511125892b0aefc0f540282eb8821b4a89c0b5f35987763d.

- 2026-10-11T02:39:32+00:00: Recorded command exit 0; command argv SHA-256
  13fdc8b56a0c965b955af689e5b7a20635a4bc1edf24d69a6cfed905ec54c75d.

- 2026-10-11T02:39:46+00:00: Recorded command exit 101; command argv SHA-256
  3624c529276fa502511125892b0aefc0f540282eb8821b4a89c0b5f35987763d.

- 2026-10-11T02:40:50+00:00: Recorded command exit 0; command argv SHA-256
  c1883c824df8c90318eb76c049345d83e0ab2bcb8d23aba826932c643b2a2e01.

- 2026-10-11T02:41:06+00:00: Recorded command exit 101; command argv SHA-256
  3624c529276fa502511125892b0aefc0f540282eb8821b4a89c0b5f35987763d.

- 2026-10-11T02:41:55+00:00: Recorded command exit 0; command argv SHA-256
  983cd897bd83c5fb73a4faca63e6306220ab7f1607ee7dc861ecb72ef4b6bc6c.

- 2026-10-11T02:42:10+00:00: Recorded command exit 101; command argv SHA-256
  3624c529276fa502511125892b0aefc0f540282eb8821b4a89c0b5f35987763d.

- 2026-10-11T02:43:13+00:00: Recorded command exit 0; command argv SHA-256
  3ce443d2dd618e9cfdb83081511bda8c5401bbbecceec79beef6d9bf19b1c185.

- 2026-10-11T02:44:02+00:00: Recorded command exit 0; command argv SHA-256
  5b3cbeadbe0801c723718018e0dbaaba6628283c4d4841041f7b1d912f280c59.

- 2026-10-11T02:44:33+00:00: Recorded command exit 0; command argv SHA-256
  024f7af5ef34e4a75ed4d40981c1ccedd976339f904663fc9df39a6792118b31.

- 2026-10-11T02:45:04+00:00: Recorded command exit 0; command argv SHA-256
  a6aee793f3649ad159f0c89901c2dd69f5794a018ee1d97dedf3595935f9328c.

- 2026-10-11T02:45:32+00:00: Recorded command exit 0; command argv SHA-256
  f508bfe46b5947bbe2c0db38b5c22231793287d1d21a442ac0f1c7c214eca1c4.

- 2026-10-11T02:46:08+00:00: Recorded command exit 0; command argv SHA-256
  7a7a69557d0cb3c41f27e87818c2938a17f0cacfe40cc8c4ba174b719ac082eb.

- 2026-10-11T02:46:23+00:00: Recorded command exit 101; command argv SHA-256
  3624c529276fa502511125892b0aefc0f540282eb8821b4a89c0b5f35987763d.

- 2026-10-11T02:47:14+00:00: Recorded command exit 0; command argv SHA-256
  0634d2ad699142c5a159d8ac396f205c26c4965d0e68668a134552247be163a1.

- 2026-10-11T02:47:30+00:00: Recorded command exit 0; command argv SHA-256
  3624c529276fa502511125892b0aefc0f540282eb8821b4a89c0b5f35987763d.

- 2026-10-11T02:47:49+00:00: Recorded command exit 0; command argv SHA-256
  adb32bf6a74b6b627f01047b0737454d216f0735b258693015fde95a32b063ce.

- 2026-10-11T02:48:32+00:00: Recorded command exit 0; command argv SHA-256
  ff7887e46b72480a870664579ce906aa6ea87d2bc18f40a3688a31267ec0430c.

- 2026-10-11T02:51:34+00:00: Heartbeat by codex-ar1754-online-integration.

- 2026-10-11T02:53:54+00:00: Recorded command exit 0; command argv SHA-256
  34a498a39080b61d1953aa1ef8e8bf64c0d434d57e075ed0194818ef8502be40.

- 2026-10-11T02:54:09+00:00: Recorded command exit 0; command argv SHA-256
  adb32bf6a74b6b627f01047b0737454d216f0735b258693015fde95a32b063ce.

- 2026-10-11T02:54:21+00:00: Recorded command exit 101; command argv SHA-256
  17da061e935d708c69338970a19c2b356a255e39bbcdb3414557fce521542cc7.

- 2026-10-11T02:54:33+00:00: Recorded command exit 1; command argv SHA-256
  9f1ca677b34e4cce155e01d17d49a33fb753a7b0b7d19d2a5684946e36654ce3.

- 2026-10-11T02:54:51+00:00: Recorded command exit 0; command argv SHA-256
  78bb3e74248e492f9e71ff8acae2986da41643ca7f8a4d71dc1ba263b74d9e1b.

- 2026-10-11T02:55:07+00:00: Recorded command exit 101; command argv SHA-256
  17da061e935d708c69338970a19c2b356a255e39bbcdb3414557fce521542cc7.

- 2026-10-11T02:55:41+00:00: Recorded command exit 1; command argv SHA-256
  1f0ca0e7b3f03b2d19cb32679530d9d56bb9d19de5e7f5e47dc231acbecb93a6.

- 2026-10-11T02:56:16+00:00: Recorded command exit 1; command argv SHA-256
  b726f0f2613f8ca52df4e3f51cebe1946f8b112a3a0bbfc77fdd0dcfffb848e4.

- 2026-10-11T02:56:43+00:00: Recorded command exit 0; command argv SHA-256
  f50c881f230c23386449dec6166b462a5dca2fe2dc3b2b46cd73aeac1c711ed2.

- 2026-10-11T02:56:56+00:00: Recorded command exit 0; command argv SHA-256
  8a9c71d32ea42e1e2f0410318eca9828a886e62b128551a3ecd825655bb04afa.

- 2026-10-11T02:57:16+00:00: Recorded command exit 0; command argv SHA-256
  17da061e935d708c69338970a19c2b356a255e39bbcdb3414557fce521542cc7.

- 2026-10-11T02:57:26+00:00: Recorded command exit 0; command argv SHA-256
  adb32bf6a74b6b627f01047b0737454d216f0735b258693015fde95a32b063ce.

- 2026-10-11T02:58:58+00:00: Heartbeat by codex-ar1754-online-integration.

- 2026-10-11T03:03:15+00:00: Recorded command exit 0; command argv SHA-256
  b6c346a4d9a82e6bc8ad75a5601f22f6915e12354e98fff512a4e89a44d4d97b.

- 2026-10-11T03:03:34+00:00: Recorded command exit 101; command argv SHA-256
  3624c529276fa502511125892b0aefc0f540282eb8821b4a89c0b5f35987763d.

- 2026-10-11T03:03:37+00:00: Recorded command exit 0; command argv SHA-256
  adb32bf6a74b6b627f01047b0737454d216f0735b258693015fde95a32b063ce.

- 2026-10-11T03:05:56+00:00: Recorded command exit 101; command argv SHA-256
  3624c529276fa502511125892b0aefc0f540282eb8821b4a89c0b5f35987763d.

- 2026-10-11T03:06:37+00:00: Recorded command exit 0; command argv SHA-256
  74c60c0d24f82e1cd4f22cdc012d6654cbfc63f16a0437486a58ec509a44f24b.

- 2026-10-11T03:06:55+00:00: Recorded command exit 0; command argv SHA-256
  3624c529276fa502511125892b0aefc0f540282eb8821b4a89c0b5f35987763d.

- 2026-10-11T03:07:41+00:00: Heartbeat by codex-ar1754-online-integration.

- 2026-10-11T03:07:50+00:00: Recorded command exit 0; command argv SHA-256
  adb32bf6a74b6b627f01047b0737454d216f0735b258693015fde95a32b063ce.

- 2026-10-11T03:08:10+00:00: Repaired diagnostic catalog for the configured local-mock error
  producer; focused diagnostic, guide, and 342 asb-cli library tests pass locally. Force-with-lease
  pushed exact signed DCO head fffa180a.

- 2026-10-11T03:11:15+00:00: Heartbeat by codex-ar1754-online-integration.

- 2026-10-11T03:12:21+00:00: Heartbeat by codex-ar1754-online-integration.

- 2026-10-11T03:12:44+00:00: Recorded command exit 0; command argv SHA-256
  228f6d6d968a7ad61bbc8eabef26a8e2e32a7c698edc95521761008e67688d82.

- 2026-10-11T03:13:17+00:00: Recorded command exit 101; command argv SHA-256
  7209c9fc590e00c4b2405af8daf70bb85eab24fe01fd193b956a7d07de2593c6.

- 2026-10-11T03:13:32+00:00: Recorded command exit 0; command argv SHA-256
  31e6cdc547c91e05aa5539b68951aa0f6de2820e12a138674d521c243192bed6.

- 2026-10-11T03:13:43+00:00: Recorded command exit 0; command argv SHA-256
  7209c9fc590e00c4b2405af8daf70bb85eab24fe01fd193b956a7d07de2593c6.

- 2026-10-11T03:13:56+00:00: Recorded command exit 0; command argv SHA-256
  adb32bf6a74b6b627f01047b0737454d216f0735b258693015fde95a32b063ce.

- 2026-10-11T03:14:09+00:00: Repaired the workflow provenance JSON digest after hosted Rust
  identified the exact lib.rs hash drift; workflow_transcript now passes locally. Pushed signed DCO
  head 0dcd1472; exact-head CI restarted.

- 2026-10-11T03:16:44+00:00: Heartbeat by codex-ar1754-online-integration.

- 2026-10-11T03:19:08+00:00: Heartbeat by codex-ar1754-online-integration.

- 2026-10-11T03:22:36+00:00: Heartbeat by codex-ar1754-online-integration.

- 2026-10-11T03:24:49+00:00: Heartbeat by codex-ar1754-online-integration.

- 2026-10-11T03:26:12+00:00: Recorded command exit 1; command argv SHA-256
  a15c1bbba6cd082a760db158367ddd00613923853ddaff9707dd9f1cfd66e7d4.

- 2026-10-11T03:26:23+00:00: Recorded command exit 1; command argv SHA-256
  725d1c2ac5d7dc2dafde1df16f79729918b5f5f68e76a15230eaa28723cc5f10.

- 2026-10-11T03:26:42+00:00: Recorded command exit 0; command argv SHA-256
  5480a89855609b29d989b3f69d03ce52d2480c4b27b07d6b20001efd5ac3b7f7.

- 2026-10-11T03:27:17+00:00: Recorded command exit 0; command argv SHA-256
  6d16e6aebcca106db9f65cd86dddbab2262d6752382fcfea3f46e184a6532f2d.

- 2026-10-11T03:28:35+00:00: Heartbeat by codex-ar1754-online-integration.

- 2026-10-11T03:31:57+00:00: Heartbeat by codex-ar1754-online-integration.

- 2026-10-11T03:34:12+00:00: Heartbeat by codex-ar1754-online-integration.

- 2026-10-11T03:37:29+00:00: Recorded command exit 1; command argv SHA-256
  ea0e4e4411f3a714e37ebaadc87b6e8b65326f09254841248b9a42b5adc999a5.

- 2026-10-11T03:38:38+00:00: Recorded command exit 0; command argv SHA-256
  042d9c4664ec2c65f715e0868dd0de198713fe2408b7969fb8160079ade9bb05.

- 2026-10-11T03:39:04+00:00: Recorded command exit 0; command argv SHA-256
  914dca83ea7fdafd2a4ca76b1e9171206ff2f8787f8d1f1f29b3574c052cdb36.

- 2026-10-11T03:39:30+00:00: Accepted after signed merge 8e4dc926, all ten exact-main workflows
  succeeded, protected-main provenance rerun succeeded after merged-PR association propagation, and
  fresh exact-main policy plus workflow-transcript, diagnostic, guide, and 342-test library
  verification passed. No GitHub Reviews API approval object required.

- 2026-10-11T03:39:35+00:00: Released AR-1754 after accepted post-merge receipt for merge 8e4dc926;
  exact-main workflows and fresh local verification are terminal-success. The only transient
  provenance failure was rerun successfully after GitHub association propagation. No GitHub Reviews
  API approval object was required.
