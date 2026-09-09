---
{
  "branch": "fix/mini-swe-cancellation-reap-test-isolation",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T01:39:18+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0102",
    "AR-0103",
    "AR-0308",
    "AR-0902"
  ],
  "id": "AR-0909",
  "next_action": "Hold immutable 42fe459 for independent review; publish only after approval and fresh exact-head CI.",
  "observed_branch": "fix/mini-swe-cancellation-reap-test-isolation",
  "observed_dirty": 1,
  "observed_head": "42fe45966a0b213e5d85f8f16604c4885e2a3dba",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0909.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make mini-SWE cancellation/reaping tests deterministic without weakening production lifecycle guarantees.",
  "task_revision": 52,
  "title": "Harden mini-SWE cancellation reap test isolation",
  "updated_at": "2026-09-09T23:37:29+00:00",
  "worktree_key": "agent-systems-benchmark-mini-swe-cancellation-reap-test-isolation"
}
---
## AR-0909

Repair the test-isolation and lifecycle oracle exposed by PR #126 Repository Quality run
34406581994. Under the exact coverage command,
`mini_swe::tests::cancellation_reaps_owned_descendant_group` completed cancellation but observed
the captured `/proc/<pid>` entry after its bounded poll and failed at `mini_swe.rs:1859`; the same
unrelated product range passed ordinary Rust, native, emulated-AArch64 and fault workflows.

No existing AR owns this exact embedded-test defect. AR-0308 and AR-0513 are complete adapter and
replay qualifications; AR-0902 is complete general fault assurance. Preserve the failure as a
coverage-context lifecycle/isolation signal until the exact process identity and state are
classified.

- 2026-09-09T21:57:42+00:00: Dependency audit confirms AR-0101, AR-0102, AR-0103, AR-0308 and
  AR-0902 are durably done. No existing AR owns the exact PR #126 cargo-llvm-cov failure in
  mini_swe::tests::cancellation_reaps_owned_descendant_group. Promote as a focused unclaimed
  embedded-test repair; do not weaken production lifecycle semantics.

- 2026-09-09T22:39:18+00:00: Claimed by quality_20260906.

- 2026-09-09T22:39:46+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-09T22:40:08+00:00: Recorded command exit 0; command argv SHA-256
  b2b1444698fd041bbbe96b9cf2c81d7500a5ca120d1a9e23eb81a078326bb6f8.

- 2026-09-09T22:41:02+00:00: Recorded command exit 1; command argv SHA-256
  31bbd9e4802232293f2efcaf9caf9c04b91079dbf154a255e67485f38be12f17.

- 2026-09-09T22:42:14+00:00: Recorded command exit 0; command argv SHA-256
  c7a24586fe8e492008168de2c71b62a049c6dd784a8ee8290a5bb40f936d8ed5.

- 2026-09-09T22:43:35+00:00: Recorded command exit 0; command argv SHA-256
  44feb74e14d0af356cf531db308694f8a72fdc5209684fa8e7323430684922e8.

- 2026-09-09T22:46:40+00:00: Recorded command exit 0; command argv SHA-256
  33a1ba44dd465d322e5bcfa8b1d75bcdec82f7c0323ae1b63615811f5a1e3060.

- 2026-09-09T22:47:01+00:00: Recorded command exit 1; command argv SHA-256
  5bbeccc32dc72f96b5ccfbb47499567583197b66e196bd76e1d106f2d7ee9559.

- 2026-09-09T22:47:22+00:00: Recorded command exit 0; command argv SHA-256
  6afb5d657d2814e5ce58710055489bfe14d69d7085d9dc4c8845dfbbdebb287b.

- 2026-09-09T22:47:46+00:00: Recorded command exit 101; command argv SHA-256
  5bbeccc32dc72f96b5ccfbb47499567583197b66e196bd76e1d106f2d7ee9559.

- 2026-09-09T22:48:13+00:00: Recorded command exit 0; command argv SHA-256
  533f695e434aa494128ad3b1d5db8dfe9a9fad9ce72c3340a3e21d9ae841a61b.

- 2026-09-09T22:48:37+00:00: Recorded command exit 101; command argv SHA-256
  5bbeccc32dc72f96b5ccfbb47499567583197b66e196bd76e1d106f2d7ee9559.

- 2026-09-09T22:49:12+00:00: Recorded command exit 0; command argv SHA-256
  dc61c3ad2c31ac63e35ac6061b0a196062b3e7b8923de1cafb6235383f9fcacf.

- 2026-09-09T22:49:36+00:00: Recorded command exit 101; command argv SHA-256
  5bbeccc32dc72f96b5ccfbb47499567583197b66e196bd76e1d106f2d7ee9559.

- 2026-09-09T22:50:14+00:00: Recorded command exit 0; command argv SHA-256
  f9fb9088f1be8961eab6c2e19687154ab4af25c87e7f1911399fdf6a53de2bb8.

- 2026-09-09T22:50:34+00:00: Recorded command exit 0; command argv SHA-256
  5bbeccc32dc72f96b5ccfbb47499567583197b66e196bd76e1d106f2d7ee9559.

- 2026-09-09T22:51:16+00:00: Recorded command exit 0; command argv SHA-256
  4e0b1f490c029d9e677e28c069471c9b87dab0506e5cec26434a6eded6d1b4c8.

- 2026-09-09T22:51:42+00:00: Claimed at state 0c9a8345; declared worktree is b6d04a8 with one dirty
  owned path. Original PR126 failure did not reproduce: focused llvm-cov and the exact full coverage
  gate passed. Test-only repair now binds PID, start time, process group and session; distinguishes
  missing, reused, zombie, runnable and changed ownership; rejects malformed/oversized PID and proc
  evidence; preserves terminal Cancelled and production bytes. Focused identity and instrumented
  cancellation tests pass after correcting two test-fixture mistakes.

- 2026-09-09T23:13:18+00:00: Recorded command exit 0; command argv SHA-256
  712bff4bdbfc6f17c00ce6d2d81a55fbf0aa0751e938b77502be0d9d55b41972.

- 2026-09-09T23:15:15+00:00: Recorded command exit 0; command argv SHA-256
  4c41c0205a9e6ed923c84149107450d30d7d3de0a7d5769b4a482b27e33793c0.

- 2026-09-09T23:15:42+00:00: Recorded command exit 0; command argv SHA-256
  c71a9e2675e30698dccd83227e89b2b78375ca3c705ba5076b76de305047f2b0.

- 2026-09-09T23:16:04+00:00: Recorded command exit 0; command argv SHA-256
  6afb5d657d2814e5ce58710055489bfe14d69d7085d9dc4c8845dfbbdebb287b.

- 2026-09-09T23:16:32+00:00: Recorded command exit 0; command argv SHA-256
  07396ce66fc3c27a066bad9b4c4dece4565a8485e06b120967e2313477e5f600.

- 2026-09-09T23:17:25+00:00: Recorded command exit 0; command argv SHA-256
  90db167b6894671a6e224fd66ed15bd7142e983fb7d3960f78e055b36c34f969.

- 2026-09-09T23:17:49+00:00: Recorded command exit 101; command argv SHA-256
  29e10a0406c7ef24ad8bd75b7c8b9ba88b1a003a3d998719640dd668298fb931.

- 2026-09-09T23:18:09+00:00: Recorded command exit 0; command argv SHA-256
  07396ce66fc3c27a066bad9b4c4dece4565a8485e06b120967e2313477e5f600.

- 2026-09-09T23:19:42+00:00: Recorded command exit 0; command argv SHA-256
  19d2e66f76219e2264bd633f21c0501c077df4e372b2bdaa1380e9c89e3ed043.

- 2026-09-09T23:20:00+00:00: Recorded command exit 0; command argv SHA-256
  d27fac5dbe52c30f9128ec74b03daaae148d841d56fe016652b2f8ccf20df0c3.

- 2026-09-09T23:20:41+00:00: Recorded command exit 0; command argv SHA-256
  5990b44b353f13e1a914a644e182719911bb6fc50c8baf71e6cce5a01c61cee7.

- 2026-09-09T23:20:57+00:00: Recorded command exit 0; command argv SHA-256
  19d2e66f76219e2264bd633f21c0501c077df4e372b2bdaa1380e9c89e3ed043.

- 2026-09-09T23:22:08+00:00: Recorded command exit 0; command argv SHA-256
  ad9ca3234afcd4c872e24741b755ebedb1a0960e077b4e256300a1ac073110e0.

- 2026-09-09T23:26:11+00:00: Recorded command exit 0; command argv SHA-256
  509e9e6163ad26e364cc096e9efe443cb230a217748f41a0921661c011a92e5d.

- 2026-09-09T23:26:33+00:00: Recorded command exit 0; command argv SHA-256
  5b1b7d9b61bb7091f15a22cbe72fea398a55302fff046aba82ee8af852150804.

- 2026-09-09T23:27:10+00:00: Recorded command exit 0; command argv SHA-256
  1ae1b2cc5f97f8e0e786b03f93532a5b84d83b3b81e24c891e6ef489dcfabd45.

- 2026-09-09T23:27:37+00:00: Recorded command exit 1; command argv SHA-256
  6c78b5a337ffdea2f480c3ff3a1325aa5d59c9f97cf2dca5d9cc986bbb371ca7.

- 2026-09-09T23:28:00+00:00: Recorded command exit 101; command argv SHA-256
  208473cc16338589df10819db9f7c95a2a27a81f10fd091d71b5d983816ad6eb.

- 2026-09-09T23:28:18+00:00: Recorded command exit 0; command argv SHA-256
  8bc7f5492d6a673472dfc8a18a838d67fcab21ddffd933f2530b2e07d0227fae.

- 2026-09-09T23:28:44+00:00: Recorded command exit 0; command argv SHA-256
  0c36c774112f8ca37d23b923c055ebb1c60370160fa05444193008256071a6c7.

- 2026-09-09T23:29:17+00:00: Recorded command exit 0; command argv SHA-256
  d7f400b27af74ab097c8330517338740a81d88683b694ef960786995dcf10605.

- 2026-09-09T23:29:39+00:00: Recorded command exit 0; command argv SHA-256
  dc46ea147bf73c5bfe729414765d050309a11af85efa09c4346a4ae383b779d0.

- 2026-09-09T23:30:17+00:00: Immutable candidate 42fe45966a0b213e5d85f8f16604c4885e2a3dba, tree
  806d27e116595f5f3c9417a55c6b6e3f331942a2, exact parent b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b is
  clean, one-path embedded cfg(test) scope, SSH-signed and DCO-valid. Original PR126 coverage
  failure remained unreproduced under exact full coverage. Final evidence: mini_swe 22/22;
  cancellation 20 serial plus 16 concurrent; private-root symlink/unsafe-mode/replacement and
  malformed/oversized/reused/non-owned identity negatives green; full workspace fmt, clippy -D
  warnings, tests, rustdoc, release and exact coverage green; contract/failure/artifact/platform
  4+7+4+4+2+5+17+6+46 green; repository policy, actionlint, zizmor, Gitleaks, cargo-deny and
  cargo-audit green. A temporary added session-leader assertion correctly failed because production
  owns the descendant process group but does not create a new session; it was reverted before the
  candidate, while session identity remains captured and immutable. Linux proc evidence does not
  claim ASB reaps a zombie owned by another reaper.

- 2026-09-09T23:33:12+00:00: Recorded command exit 0; command argv SHA-256
  c309cb22f5024a888edba1b227bb1fd2fc47f53c4995fc2a1b54189d23684996.

- 2026-09-09T23:35:35+00:00: Recorded command exit 0; command argv SHA-256
  05cc81acdb629462fde08cca0a8fab85adbda823b74ad5350c32b7b86a345061.

- 2026-09-09T23:36:25+00:00: Recorded command exit 0; command argv SHA-256
  2fe136f4ccc6582673ccf9a053e85162c8a4d3fea5da990d34ebc4f82efac835.

- 2026-09-09T23:37:04+00:00: Recorded command exit 1; command argv SHA-256
  54c206b639bd15f1853fc77226c3107284b17094d104d8e3bb3061a8060ecf88.

- 2026-09-09T23:37:29+00:00: Recorded command exit 0; command argv SHA-256
  59bae973c90cbd4096e9ad08b7f34b92381108fd456011186547b0426d86c2bc.
