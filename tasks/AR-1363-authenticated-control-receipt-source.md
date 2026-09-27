---
{
  "branch": "feature/ar-1363-authenticated-control-receipt-source",
  "checkpoint_commit": "29d27a91ad6a4eff455f62ae25eb952fec45fcf5",
  "claim_expires": "2026-09-27T03:14:35+00:00",
  "depends_on": [
    "AR-1362"
  ],
  "id": "AR-1363",
  "next_action": "Continue bounded polling of PR #342; merge normally only after all required checks are green and mergeStateStatus is CLEAN.",
  "observed_branch": "feature/ar-1363-authenticated-control-receipt-source",
  "observed_dirty": 0,
  "observed_head": "29d27a91ad6a4eff455f62ae25eb952fec45fcf5",
  "owner": "ar1332_record_replay_luna56",
  "plan": "../plans/AR-1363-authenticated-control-receipt-source.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Deliver authenticated runtime authority receipts through the versioned control boundary without exposing secrets or caller authority.",
  "task_revision": 72,
  "title": "Authenticated control receipt source",
  "updated_at": "2026-09-27T01:16:47+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1363-authenticated-control-receipt-source"
}
---

Successor for blocked AR-1361, explicitly depending on completed AR-1362.
Do not touch asb-tui, reopen stale dependencies, or synthesize authority in CLI.

- 2026-09-24T00:00:00+00:00: Created after AR-1362 delivered the durable
  digest-only runtime authority enrollment contract and all post-merge gates.

- 2026-09-23T23:28:50+00:00: Promote receipt source after AR-1362 completed durable authority
  enrollment and all post-merge gates.

- 2026-09-23T23:28:52+00:00: Claimed by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T23:29:30+00:00: Recorded command exit 0; command argv SHA-256
  277a1936169e354dbe4c6881de500884f7d6e3cf1bd44c494d3e2099e18ee3e0.

- 2026-09-23T23:29:48+00:00: Blocked after exact protected-main audit at e9d4d3d1: ControlBackend
  AuthRecord still contains only provider/endpoint/credential digests, generation, and status. No
  authenticated certificate chain or runtime-owned authority issuer is available to issue
  RuntimeEnrollmentReceiptV1; synthesizing chain or target/tool/lease/relay authority would violate
  fail-closed policy. Create a successor for authenticated certificate-chain
  enrollment/materialization, then resume AR-1363 and downstream AR-1360.

## Current development and CI qualification boundary

The mandatory development and CI qualification path for this AR is a deterministic
local provider/LLM mock (LiteLLM-compatible where practical), including hostile
negative tests and offline replay where applicable. External/live OpenRouter or
other provider reachability is optional supplementary evidence only; it is never a
completion, dependency-readiness, or CI gate. Production egress policy, credential
non-disclosure, runtime-owned authority, namespace/relay attestation, cancellation
and teardown, and fail-closed denial of unapproved external traffic remain required
contracts. Existing live-provider dependency edges describe production integration
ordering only and must not be used to block local qualification or to claim external
reachability.

- 2026-09-27T00:55:24+00:00: AR-1471 now provides authenticated control-to-runtime chain binding;
  resume downstream receipt-source integration without caller authority.

- 2026-09-27T00:55:30+00:00: Claimed by ar1332_record_replay_luna56.

- 2026-09-27T00:56:02+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-27T00:56:21+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-27T00:56:40+00:00: Recorded command exit 0; command argv SHA-256
  d5cae6ce302d8ca5200c4e447362453e14f36935e3149fe0cdd926322eb8e984.

- 2026-09-27T00:56:55+00:00: Recorded command exit 0; command argv SHA-256
  6ed643dd35118b3bc9a612aa209a8cdcd22d115d0c1c932de68957f3c4782365.

- 2026-09-27T00:57:14+00:00: Recorded command exit 0; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-09-27T00:57:34+00:00: Recorded command exit 0; command argv SHA-256
  d5cae6ce302d8ca5200c4e447362453e14f36935e3149fe0cdd926322eb8e984.

- 2026-09-27T00:57:48+00:00: Recorded command exit 0; command argv SHA-256
  7dfa8e4180973619ad63008ca55c1cdb60a77d1e72bc16077bde392345beacad.

- 2026-09-27T00:58:07+00:00: Recorded command exit 0; command argv SHA-256
  f622264bbf42f560d7e8b73f6d8cf8db8852eac2e0b1f6910b643b5283d645e0.

- 2026-09-27T00:58:27+00:00: Recorded command exit 0; command argv SHA-256
  1e4694571d528fd054e88a6bf4bc34032c9d9bfe0b1b4ebe8e4648db31fb86a6.

- 2026-09-27T00:58:42+00:00: Recorded command exit 0; command argv SHA-256
  30f4d1c3c5ec954a7b6703d587f3f00af18ebc0ebbbdf413a51588828e26072a.

- 2026-09-27T00:58:57+00:00: Recorded command exit 0; command argv SHA-256
  954f2523cfdb49c58b89567fd8ca110735e6235f5e74d791c610c2dbfe379cbf.

- 2026-09-27T00:59:11+00:00: Recorded command exit 0; command argv SHA-256
  5db8a9f3275ebe83006ec30df58bc50ee0d99f066fe2bc3cca1efa2e067a8045.

- 2026-09-27T00:59:32+00:00: Recorded command exit 0; command argv SHA-256
  45b57a304295a0681a2e4535b23f13625690f70fe7196f64bc62e32c4894ee59.

- 2026-09-27T00:59:47+00:00: Recorded command exit 0; command argv SHA-256
  7178b635232ea4b1b2db99de68cb2db38cb2bb75f265af9443b4e3b114ff3950.

- 2026-09-27T01:00:06+00:00: Recorded command exit 0; command argv SHA-256
  460e90e667a2b39bfe26831312583135670124d9720cd7a6cd684839737b5ffd.

- 2026-09-27T01:00:26+00:00: Recorded command exit 0; command argv SHA-256
  ca25836fc60cc0de22aa986920715042509237ad93b6633692800a0ebff37a4e.

- 2026-09-27T01:00:41+00:00: Recorded command exit 0; command argv SHA-256
  5acdd3e42493c3f8771fcfa67af92cfb70989ce84126ec9f76d4293251df924f.

- 2026-09-27T01:01:04+00:00: Recorded command exit 0; command argv SHA-256
  65b4518df45df6d303e2f8e4d505976579ea07c661336f48452be361be767023.

- 2026-09-27T01:01:30+00:00: Recorded command exit 0; command argv SHA-256
  f82987cdb9691659ea9387d7eea5014340bff0727540ca9ae8277de42f405f6b.

- 2026-09-27T01:01:45+00:00: Recorded command exit 0; command argv SHA-256
  e12145ef78560361b2bee18614a779289bd3b061b396a2fd8f0d05dbbddb6ba0.

- 2026-09-27T01:02:09+00:00: Recorded command exit 0; command argv SHA-256
  e9ec0caaacbc4b9d99e3f596e0f2e2a174d3ab463869c97b3b94df68e8579b38.

- 2026-09-27T01:02:24+00:00: Recorded command exit 0; command argv SHA-256
  8bfb00fb17231f67ee6be0af406901c4376273925110ee64542167a8a386dcd6.

- 2026-09-27T01:03:03+00:00: Recorded command exit 2; command argv SHA-256
  7367b176485dc3e36e7c3e93b16ff14b4ffe3f53437f55644cd491e478708ccc.

- 2026-09-27T01:03:54+00:00: Recorded command exit 0; command argv SHA-256
  53fb0fe436e38a1b861fb7a6de9d1f618dc013e15b3fbf14b22760bbfb45c82e.

- 2026-09-27T01:04:14+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-27T01:04:34+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-27T01:05:21+00:00: Recorded command exit 0; command argv SHA-256
  f84b9bb94cb0d3f389581d2e3ff412632aeb6577236c2420a4963c7705978ea4.

- 2026-09-27T01:05:36+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-09-27T01:05:55+00:00: Recorded command exit 0; command argv SHA-256
  6120de36aaf3f41dd6cadb792c3fccfa2bc059e1af956c26b16aabbc0ee7bbd5.

- 2026-09-27T01:06:15+00:00: Recorded command exit 0; command argv SHA-256
  0c3a5150207f73fcd896f8d69bcd72b4bab205cdeca8aa41f1a41b6ef0ed74a8.

- 2026-09-27T01:06:30+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-27T01:07:23+00:00: Recorded command exit 0; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-27T01:07:39+00:00: Heartbeat by ar1332_record_replay_luna56.

- 2026-09-27T01:08:00+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-27T01:08:25+00:00: Recorded command exit 0; command argv SHA-256
  83eea80a9d087ff8892cb2661bf0e6f7ab62f8c8288f14697126e2ebaafdf975.

- 2026-09-27T01:09:13+00:00: Recorded command exit 0; command argv SHA-256
  b49a90ee600c1023cee9ee9f9e8a4f9a06c53eef8c48d3932d88e482126c7c01.

- 2026-09-27T01:09:28+00:00: Rebased clean declared worktree onto protected main
  cb9bce4dd99194ba44f65655d7f7e2e21fc8b408. Implemented narrow control receipt-source hardening in
  crates/asb-cli/src/control.rs: RuntimeReceipt requests validate schema/provider/generation/nonce
  before authority lookup; constructed response validates exact request/chain/receipt binding before
  emission. Added hostile malformed-request test. No asb-tui/live-provider changes. Signed+DCO
  commit 29d27a91 verified; focused control/runtime/CLI tests pass (including new negative), full
  workspace tests pass, clippy -D warnings pass, rustdoc -D warnings pass, release workspace build
  pass. One initial clippy attempt hit shared coordinator LOCK_TIMEOUT and was retried successfully;
  initial patch heredoc failed due wrapper escaping and was corrected via base64 apply_patch.

- 2026-09-27T01:09:38+00:00: Recorded command exit 0; command argv SHA-256
  7dfa8e4180973619ad63008ca55c1cdb60a77d1e72bc16077bde392345beacad.

- 2026-09-27T01:09:52+00:00: Recorded command exit 0; command argv SHA-256
  17b5bfc2e8d47126c0508a5c457b6c51a374b2cea4dc6b250e438259560e45e3.

- 2026-09-27T01:10:07+00:00: Recorded command exit 0; command argv SHA-256
  3fc92b56d32c59905cf6327b6a7568d863fa0d58809b9254829a33fcba3135b8.

- 2026-09-27T01:10:23+00:00: Recorded command exit 0; command argv SHA-256
  0eccf9c4708ea8758b8c812cdc7ae0be9141503d1a82e72f3998b8770fa49280.

- 2026-09-27T01:10:46+00:00: Recorded command exit 0; command argv SHA-256
  97a0727b26ebf199589e74bac771bad1976be53dc99ef324d2121079512946ad.

- 2026-09-27T01:11:08+00:00: Recorded command exit 0; command argv SHA-256
  392299657f25cad912887aef5926e1acf02d126faaf70e1ce738633681cb0b2f.

- 2026-09-27T01:11:29+00:00: Recorded command exit 0; command argv SHA-256
  001cc326119bd8281c9d2a12fde3dd3a3a6aadc0b95b65e833da8ce413346aae.

- 2026-09-27T01:11:47+00:00: Heartbeat by ar1332_record_replay_luna56.

- 2026-09-27T01:11:54+00:00: Recorded command exit 0; command argv SHA-256
  001cc326119bd8281c9d2a12fde3dd3a3a6aadc0b95b65e833da8ce413346aae.

- 2026-09-27T01:12:14+00:00: Recorded command exit 0; command argv SHA-256
  001cc326119bd8281c9d2a12fde3dd3a3a6aadc0b95b65e833da8ce413346aae.

- 2026-09-27T01:12:33+00:00: Recorded command exit 0; command argv SHA-256
  001cc326119bd8281c9d2a12fde3dd3a3a6aadc0b95b65e833da8ce413346aae.

- 2026-09-27T01:12:52+00:00: Heartbeat by ar1332_record_replay_luna56.

- 2026-09-27T01:12:58+00:00: Recorded command exit 0; command argv SHA-256
  0400894a8fb04528b541596044b098cf3fa6c69097907f04a4516b92624960dd.

- 2026-09-27T01:13:19+00:00: Recorded command exit 0; command argv SHA-256
  001cc326119bd8281c9d2a12fde3dd3a3a6aadc0b95b65e833da8ce413346aae.

- 2026-09-27T01:13:39+00:00: Recorded command exit 0; command argv SHA-256
  0400894a8fb04528b541596044b098cf3fa6c69097907f04a4516b92624960dd.

- 2026-09-27T01:14:11+00:00: PR #342 is OPEN at exact head 29d27a91ad6a4eff455f62ae25eb952fec45fcf5,
  base cb9bce4dd99194ba44f65655d7f7e2e21fc8b408, mergeStateStatus UNSTABLE while jobs run. Required
  rollup observed: Huawei MIT source headers SUCCESS; Hosted portability and native qualification
  IN_PROGRESS; Fault assurance retained faults SUCCESS, bounded fuzz IN_PROGRESS, matcher/SLO
  mutation IN_PROGRESS; Formal assurance Kani SUCCESS, Loom SUCCESS, TLC/Alloy IN_PROGRESS; Rust
  verification IN_PROGRESS; Repository quality IN_PROGRESS. AWQ shadow SUCCESS. No failures;
  continue polling.

- 2026-09-27T01:14:17+00:00: Recorded command exit 0; command argv SHA-256
  0400894a8fb04528b541596044b098cf3fa6c69097907f04a4516b92624960dd.

- 2026-09-27T01:14:35+00:00: Heartbeat by ar1332_record_replay_luna56.

- 2026-09-27T01:14:42+00:00: Recorded command exit 0; command argv SHA-256
  0400894a8fb04528b541596044b098cf3fa6c69097907f04a4516b92624960dd.

- 2026-09-27T01:15:00+00:00: Recorded command exit 0; command argv SHA-256
  0400894a8fb04528b541596044b098cf3fa6c69097907f04a4516b92624960dd.

- 2026-09-27T01:15:21+00:00: Recorded command exit 0; command argv SHA-256
  0400894a8fb04528b541596044b098cf3fa6c69097907f04a4516b92624960dd.

- 2026-09-27T01:15:40+00:00: Recorded command exit 0; command argv SHA-256
  ff5c276a21f226ef04953d2240055e1f91c5bbfcedbdad514a4ef0d6e92d815e.

- 2026-09-27T01:15:59+00:00: Recorded command exit 0; command argv SHA-256
  0400894a8fb04528b541596044b098cf3fa6c69097907f04a4516b92624960dd.

- 2026-09-27T01:16:19+00:00: Recorded command exit 0; command argv SHA-256
  0400894a8fb04528b541596044b098cf3fa6c69097907f04a4516b92624960dd.

- 2026-09-27T01:16:47+00:00: Bounded polling at 2026-09-27T01:16Z: PR #342 exact head 29d27a91;
  mergeStateStatus UNSTABLE. Completed SUCCESS: Huawei 36284742897, Hosted 36284742907, Fault
  retained 36284742879, Formal TLC/Kani/Loom 36284742887, AWQ shadow 36284742871. Still IN_PROGRESS:
  Emulated AArch64 36284742939, Repository quality 36284742895, Rust verification 36284742908. Fault
  fuzz and mutation and Formal models are all SUCCESS. No failure or hang evidence; continue bounded
  polling with heartbeat.
