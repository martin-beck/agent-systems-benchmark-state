---
{
  "branch": "feature/ar-1300-runtime-cassette-dispatch-seam",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T09:32:34+00:00",
  "depends_on": [
    "AR-1282",
    "AR-1285"
  ],
  "id": "AR-1300",
  "next_action": "Continue bounded monitoring of the four pending exact-head checks; if all pass, perform protected merge and post-merge exact-main verification.",
  "observed_branch": "feature/ar-1300-runtime-cassette-dispatch-seam",
  "observed_dirty": 0,
  "observed_head": "019038378726405eaf05a77269b8541d9a81d912",
  "owner": "ar1300_dispatch",
  "plan": "../plans/AR-1300.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Connect runtime-issued cassette operations to the real strict-replay dispatch path.",
  "task_revision": 84,
  "title": "Runtime-to-replay cassette dispatch seam",
  "updated_at": "2026-09-17T07:38:26+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1300-runtime-cassette-dispatch-seam"
}
---

## AR-1300

Implement the missing ASB-only runtime-to-replay cassette operation seam identified by the
independent review of PRs #197 and #207. The primary replay command must consume a runtime-issued,
authenticated, single-use operation context and perform a real bounded request/response against
the strict-replay service. It must never accept caller-assembled launch authority, fabricate relay
or readiness state, contact a live provider, or fall back when the cassette operation fails.

This is a successor/follow-on implementation slice for the blocked AR-1271, AR-1273, AR-1262 and
AR-1286 evidence. Those records remain historical and must not be revived or treated as source
branches. AR-1282 supplies the authenticated transport and AR-1285 supplies the runtime launch
factory; both are required dependencies. The scope is ASB only: `crates/asb-core`,
`crates/asb-runtime`, `crates/asb-replay`, `crates/asb-cli`, their schemas/docs and credential-free
fixtures/tests. Do not modify asb-tui or coordinator implementation.


- 2026-09-17T07:00:52+00:00: Dependencies AR-1282 and AR-1285 verified done; promote ASB-only
  runtime-to-replay dispatch seam

- 2026-09-17T07:01:32+00:00: Claimed by ar1300_dispatch.

- 2026-09-17T07:01:39+00:00: Recorded command exit 0; command argv SHA-256
  ea07ab3b67665f619b9a1dca7e44f093e0a7340deef748997c47ffda5e5acdda.

- 2026-09-17T07:02:04+00:00: Recorded command exit 0; command argv SHA-256
  1a8de5a310175902c47bab2296114b0ba62bc78073a6a3259b840ed586598472.

- 2026-09-17T07:02:21+00:00: Recorded command exit 0; command argv SHA-256
  dc3aa8e23b2d27a4f64dfa2d2aaba633d9f7eb7a552d995b24593f293ce06b25.

- 2026-09-17T07:02:36+00:00: Recorded command exit 0; command argv SHA-256
  a0e1f3fa60f9cb555044f5c56212713cabe21b943de015c19b5c1a47264d7790.

- 2026-09-17T07:03:55+00:00: Recorded command exit 0; command argv SHA-256
  9436ed4df3eda71a5127f63b07db1e1dcd3bcd92e61f5010c5bde8c9cb82fe2a.

- 2026-09-17T07:04:07+00:00: Recorded command exit 255; command argv SHA-256
  b5ee3857d808cc2b617700d589910a7a1ddc72ba808914702dbe8ba0c08b1a5d.

- 2026-09-17T07:04:16+00:00: Recorded command exit 255; command argv SHA-256
  b5ee3857d808cc2b617700d589910a7a1ddc72ba808914702dbe8ba0c08b1a5d.

- 2026-09-17T07:04:31+00:00: Recorded command exit 0; command argv SHA-256
  e755470626274bcf396a60d89c173e91c4d040d4cb18a875b6197180353117ab.

- 2026-09-17T07:04:42+00:00: Recorded command exit 0; command argv SHA-256
  b5ee3857d808cc2b617700d589910a7a1ddc72ba808914702dbe8ba0c08b1a5d.

- 2026-09-17T07:05:02+00:00: 2026-09-17T07:06:00Z checkpoint: two exit-255 worktree commands were
  environment/coordination invocation failures, not product failures. First attempted git worktree
  removal/add in one chained wrapper; post-reconcile external GitHub API run-list retries failed, so
  the second chained command was not executed. Second attempted product worktree add before deleting
  the stale local branch; git correctly rejected the existing branch. The stale state-repo worktree
  was removed, the stale product branch was deleted through handoffctl, and the protected
  origin/main product worktree was then created successfully at c1b1860. No source mutation or
  external project state was damaged.

- 2026-09-17T07:08:33+00:00: Recorded command exit 1; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T07:08:47+00:00: Recorded command exit 0; command argv SHA-256
  dbebc8471cba02b09e566b4d54e6af0038cb179b04e6a3ed264b258e2b7da72d.

- 2026-09-17T07:09:03+00:00: Recorded command exit 101; command argv SHA-256
  b8fe131782d7b5ff45503354b45b542f1505febf4b8de90153d61faac52483ec.

- 2026-09-17T07:09:30+00:00: Recorded command exit 101; command argv SHA-256
  23c7085a71a0f9a3cc31fb96d52835376a1502dcd536434a3c18b4f2143e2921.

- 2026-09-17T07:09:52+00:00: Recorded command exit 0; command argv SHA-256
  dbebc8471cba02b09e566b4d54e6af0038cb179b04e6a3ed264b258e2b7da72d.

- 2026-09-17T07:10:08+00:00: Recorded command exit 101; command argv SHA-256
  23c7085a71a0f9a3cc31fb96d52835376a1502dcd536434a3c18b4f2143e2921.

- 2026-09-17T07:10:27+00:00: Recorded command exit 0; command argv SHA-256
  dbebc8471cba02b09e566b4d54e6af0038cb179b04e6a3ed264b258e2b7da72d.

- 2026-09-17T07:10:57+00:00: Recorded command exit 101; command argv SHA-256
  23c7085a71a0f9a3cc31fb96d52835376a1502dcd536434a3c18b4f2143e2921.

- 2026-09-17T07:11:20+00:00: Recorded command exit 0; command argv SHA-256
  cb861617f98feffcac764026b553d29deb67d8ff4bd7b0c37941fdf231742440.

- 2026-09-17T07:12:02+00:00: 2026-09-17T07:12:00Z checkpoint: the first locked focused compile
  reached product compilation and failed because the new response digest formatted a Sha256 hasher
  instead of its finalized digest (E0277 LowerHex). This was a product compile defect in the new
  code, not an environment failure. Fixed by finalizing the digest; subsequent focused crates
  compiled and tests ran. The later workflow-transcript failure was the expected existing provenance
  fixture drift caused by the intentional CLI source change; updated only its checked-in digest and
  the focused transcript suite is green.

- 2026-09-17T07:12:39+00:00: Recorded command exit 0; command argv SHA-256
  dbebc8471cba02b09e566b4d54e6af0038cb179b04e6a3ed264b258e2b7da72d.

- 2026-09-17T07:13:00+00:00: Recorded command exit 0; command argv SHA-256
  9fc6e752dc210bb6d9a5f0890f02aece00ac398da1d968c933b7bc3c5a455cb9.

- 2026-09-17T07:13:34+00:00: Heartbeat by ar1300_dispatch.

- 2026-09-17T07:13:50+00:00: Recorded command exit 0; command argv SHA-256
  0b4ee7a350c5af6e7fd324202eda88e20b05d63f94cd4a61710d1ea55cbf6e14.

- 2026-09-17T07:14:41+00:00: Recorded command exit 0; command argv SHA-256
  4c4d2ad0336a248cac31003c820b9310c3892043de66a53e6cfb78f4aea25362.

- 2026-09-17T07:15:05+00:00: Recorded command exit 0; command argv SHA-256
  b01c29b022fdaac7e683b951dea91d8fe2dcfc23c5e707b0363225b39e5a6966.

- 2026-09-17T07:15:49+00:00: Recorded command exit 0; command argv SHA-256
  08bf657fbab2259fed880b94b11246aa5d58ba4d35d8a37e20cbb1c3d791bcbc.

- 2026-09-17T07:16:57+00:00: Recorded command exit 0; command argv SHA-256
  dbebc8471cba02b09e566b4d54e6af0038cb179b04e6a3ed264b258e2b7da72d.

- 2026-09-17T07:17:21+00:00: Recorded command exit 0; command argv SHA-256
  9fc6e752dc210bb6d9a5f0890f02aece00ac398da1d968c933b7bc3c5a455cb9.

- 2026-09-17T07:17:36+00:00: Recorded command exit 0; command argv SHA-256
  a3ede631e8a27ca74a59e2b3d914004121bb9785c223e1e203b6881076be8773.

- 2026-09-17T07:17:45+00:00: Recorded command exit 0; command argv SHA-256
  393d7d976b0ad205e7c7088541e7de0be3fa2f1d6fc058f7d6ec0f3cf2e970ec.

- 2026-09-17T07:18:07+00:00: Recorded command exit 0; command argv SHA-256
  3c1b6c2538fbbd9160f5f4ac9f021af278baa782bd2d0c10724ee1d7cd6986f1.

- 2026-09-17T07:18:34+00:00: Recorded command exit 0; command argv SHA-256
  c03ba282c60956bb78b11e580cef9581dc9ec4d4af52f9f3a99a0a45745714ca.

- 2026-09-17T07:18:57+00:00: Heartbeat by ar1300_dispatch.

- 2026-09-17T07:19:00+00:00: Signed/DCO implementation checkpoint 405f68f pushed from clean
  protected-origin/main worktree and PR #217 opened. RuntimeLaunchContext now issues a one-shot
  private generation-authenticated operation; CLI serializes the actual cassette request, dispatches
  through StrictReplayService, receives/decodes the cassette response, and emits response
  status/digest. Negative coverage rejects malformed response shapes, credential-bearing operation
  headers, duplicate operation use, handler failure, stale generation, and oversized frames. Focused
  libs 145 tests green, full locked workspace suite green (with only pre-existing environment-gated
  ignores), clippy/rustdoc/release build green. Earlier command failures and compile defect were
  separately checkpointed.

- 2026-09-17T07:19:09+00:00: Recorded command exit 0; command argv SHA-256
  9ceb7f0d8269380f98e3c07da67513c54e2dd1461affec926838bb05c816f0cf.

- 2026-09-17T07:19:34+00:00: Recorded command exit 2; command argv SHA-256
  87bfa4cd10582781dbbfdb9faa1ab143d7866c1dfde145b254b4ee70813ea823.

- 2026-09-17T07:19:57+00:00: Recorded command exit 2; command argv SHA-256
  5097e49ecce8aa5f23d3477a5b7da63377cab7e7a830cbbf760e7e0e11e73e5e.

- 2026-09-17T07:20:36+00:00: 2026-09-17T07:21:00Z checkpoint: two exit-2 records came from
  coordinator command setup, not product gates. First invoked repository_policy.py relative to the
  state checkout, so the script was unavailable; second supplied an unsupported --repo option after
  switching to the absolute product script. No product test failed. A corrected absolute invocation
  then hit the shared coordinator lock timeout while another state transaction was active; no source
  mutation occurred. PR #217 remains open/mergeable at signed head 405f68f; hosted required checks
  are still running, with headers/AWQ already successful. Implementation and local locked gates
  remain green.

- 2026-09-17T07:20:56+00:00: Recorded command exit 0; command argv SHA-256
  160f95d053759a37dbc6ad4a7b0c0ae82909498c93fabcfb2ef148ec0837ff21.

- 2026-09-17T07:21:17+00:00: Recorded command exit 8; command argv SHA-256
  8d51c1a8224c0865fa00e2b7ce60899a553f9c37ff5586fb52271da60170496c.

- 2026-09-17T07:21:37+00:00: Recorded command exit 0; command argv SHA-256
  88c6c6db711ab42df0a768597776003b40cfad6f281ff0a095de21cd0376850a.

- 2026-09-17T07:22:38+00:00: Recorded command exit 8; command argv SHA-256
  8d51c1a8224c0865fa00e2b7ce60899a553f9c37ff5586fb52271da60170496c.

- 2026-09-17T07:22:57+00:00: Recorded command exit 8; command argv SHA-256
  8d51c1a8224c0865fa00e2b7ce60899a553f9c37ff5586fb52271da60170496c.

- 2026-09-17T07:23:59+00:00: 2026-09-17T07:24:00Z checkpoint: repeated exit-8 records from gh
  PR-check polling are external API failures/rate-limit or transient GitHub API unavailability, not
  product gate failures. Polling has been stopped to avoid aggressive retries. Last successful PR
  #217 snapshot: OPEN, MERGEABLE, exact head 405f68f on base c1b1860; headers, AWQ, Kani, Loom,
  platform, retained faults, fuzz, and mutation checks SUCCESS; Rust, formal aggregate,
  emulated-aarch64, and policy/coverage/supply checks remained pending. Local signed/DCO head is
  clean and repository policy passed.

- 2026-09-17T07:24:12+00:00: Heartbeat by ar1300_dispatch.

- 2026-09-17T07:24:15+00:00: Recorded command exit 8; command argv SHA-256
  8d51c1a8224c0865fa00e2b7ce60899a553f9c37ff5586fb52271da60170496c.

- 2026-09-17T07:25:20+00:00: Recorded command exit 0; command argv SHA-256
  68dd7d19eebd7fcb63054636a675fa2ee0902d263799f910c61db4a729e1f026.

- 2026-09-17T07:26:46+00:00: Recorded command exit 101; command argv SHA-256
  9fc6e752dc210bb6d9a5f0890f02aece00ac398da1d968c933b7bc3c5a455cb9.

- 2026-09-17T07:27:28+00:00: Recorded command exit 0; command argv SHA-256
  dbebc8471cba02b09e566b4d54e6af0038cb179b04e6a3ed264b258e2b7da72d.

- 2026-09-17T07:27:52+00:00: Recorded command exit 0; command argv SHA-256
  9fc6e752dc210bb6d9a5f0890f02aece00ac398da1d968c933b7bc3c5a455cb9.

- 2026-09-17T07:28:37+00:00: Recorded command exit 0; command argv SHA-256
  abcf6e707b55922b0195a6df3a00bf51b7264d49ec362d131db32f1ee1696a07.

- 2026-09-17T07:28:47+00:00: Recorded command exit 0; command argv SHA-256
  95c2b2d6ec4cc79c439e58f80c1348047c24b4beecb6485f08e3f42301b4c22c.

- 2026-09-17T07:29:05+00:00: Recorded command exit 0; command argv SHA-256
  2bee46e5b0f44dd0d4b42ff3e382fd4a1e30bca68b2130f7e45c3d02e173a3cd.

- 2026-09-17T07:29:29+00:00: Heartbeat by ar1300_dispatch.

- 2026-09-17T07:29:31+00:00: Added signed/DCO test commit 0190383 to prove a consumed runtime launch
  context can issue exactly one operation; focused runtime/replay/CLI libraries pass after the
  addition. Pushed PR #217 head 0190383, so the previously green 405f68f checks are intentionally
  stale and must be rerun at the new exact head. No source or worktree dirt remains.

- 2026-09-17T07:30:04+00:00: Recorded command exit 8; command argv SHA-256
  8d51c1a8224c0865fa00e2b7ce60899a553f9c37ff5586fb52271da60170496c.

- 2026-09-17T07:31:51+00:00: Recorded command exit 8; command argv SHA-256
  8d51c1a8224c0865fa00e2b7ce60899a553f9c37ff5586fb52271da60170496c.

- 2026-09-17T07:32:12+00:00: Recorded command exit 8; command argv SHA-256
  8d51c1a8224c0865fa00e2b7ce60899a553f9c37ff5586fb52271da60170496c.

- 2026-09-17T07:32:34+00:00: Heartbeat by ar1300_dispatch.

- 2026-09-17T07:32:37+00:00: Exact-head PR #217 at 0190383 now has headers, AWQ, fuzz, Kani,
  mutation, platform, retained faults, and Loom checks SUCCESS. Rust, formal aggregate,
  emulated-aarch64, and policy/coverage/supply checks remain pending. Independent local review
  confirms both topic commits are SSH-signed+DCO, repository policy passes, worktree is clean, and
  the branch is based on protected origin/main c1b1860.

- 2026-09-17T07:34:23+00:00: Recorded command exit 8; command argv SHA-256
  8d51c1a8224c0865fa00e2b7ce60899a553f9c37ff5586fb52271da60170496c.

- 2026-09-17T07:35:05+00:00: Recorded command exit 8; command argv SHA-256
  8d51c1a8224c0865fa00e2b7ce60899a553f9c37ff5586fb52271da60170496c.

- 2026-09-17T07:36:22+00:00: Recorded command exit 0; command argv SHA-256
  8d51c1a8224c0865fa00e2b7ce60899a553f9c37ff5586fb52271da60170496c.

- 2026-09-17T07:36:33+00:00: Recorded command exit 0; command argv SHA-256
  8d51c1a8224c0865fa00e2b7ce60899a553f9c37ff5586fb52271da60170496c.

- 2026-09-17T07:37:08+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-09-17T07:37:17+00:00: Recorded command exit 0; command argv SHA-256
  cb829e9c4e7c7cffe24d5a6161df617fb253eb697a3402baff2975d02e925261.

- 2026-09-17T07:37:27+00:00: Recorded command exit 0; command argv SHA-256
  498a45511d836b8214c57806462d9d61c14b46c202d428e6d973320febf2d11c.

- 2026-09-17T07:37:46+00:00: Recorded command exit 0; command argv SHA-256
  9f51a4f2c7fbf167ac1e03b024a9704622858850aa102f1e25bb78c9992eba9a.

- 2026-09-17T07:38:01+00:00: Recorded command exit 0; command argv SHA-256
  eef2bbfce3dc6fcc97911f75907a7543bb91c6c618b189c42029409d0e300c11.

- 2026-09-17T07:38:17+00:00: Recorded command exit 1; command argv SHA-256
  dc57a5c552050c2670ce8251d4a349b0cf325ec929044ed1d4aeed3cf529888d.

- 2026-09-17T07:38:26+00:00: Recorded command exit 0; command argv SHA-256
  217993b69dd9a04d3fde05dfb8d3036764ffb4c2ac2ad19147f5efed0b44b4a3.
