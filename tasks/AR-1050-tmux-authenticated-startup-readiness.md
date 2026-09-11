---
{
  "branch": "fix/tmux-authenticated-startup-readiness",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T05:44:12+00:00",
  "depends_on": [],
  "id": "AR-1050",
  "next_action": "Publish approved exact head 46145ad63af61d0b6f4549f06c001f33d60f02c1, open PR, require exact-head CI, then merge and run trusted-main qualification only if all green.",
  "owner": "codex-ar1050-tmux-startup-readiness-20260911",
  "plan": "../plans/AR-1050.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Wait for bounded stable authenticated tmux server, session and window readiness after detached creation.",
  "task_revision": 67,
  "title": "Acquire authenticated tmux startup readiness",
  "updated_at": "2026-09-11T03:45:48+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-tmux-authenticated-startup-readiness"
}
---

Trusted-main run 34556679585 at exact merge aacf672c018706ef8a361e1a2dd6c19d890f02d8
passed 19 of 24 terminal tests, while all five live tmux fixtures completed new-session and then
failed the immediate server observation. Add bounded evidence-based startup acquisition with stable
server/session/window identity and retained pane authority. Change no renderer or application code.

- 2026-09-11T03:03:07+00:00: Pre-approved P0 recovery is ready after trusted-main run 34556679585
  exposed asynchronous tmux startup observability.

- 2026-09-11T03:03:09+00:00: Claimed by codex-ar1050-tmux-startup-readiness-20260911.

- 2026-09-11T03:03:21+00:00: Recorded command exit 0; command argv SHA-256
  cba9d7bd2ba40e44aa93d4d92afc64fb942236dfde48fc6a0f4617c06f60c170.

- 2026-09-11T03:06:01+00:00: Heartbeat by codex-ar1050-tmux-startup-readiness-20260911.

- 2026-09-11T03:06:04+00:00: Initial audit complete at exact base aacf672c. First heartbeat
  invocation used an unsupported --note argument and made no state/product change; classified as
  invocation-only. Proceeding with immediate guard, stable startup identity, and pre-option
  revalidation.

- 2026-09-11T03:07:23+00:00: Recorded command exit 1; command argv SHA-256
  11f4f5096b2fdb900cd58e3fd1862b9faa21d054e9cbeb2c32f2392d87748c84.

- 2026-09-11T03:08:20+00:00: Recorded command exit 0; command argv SHA-256
  9053689efe929cbc02a2b35a86211647129553284974b74a059af4957b1e9a5e.

- 2026-09-11T03:08:43+00:00: Recorded command exit 0; command argv SHA-256
  86485ba2da462caed957c3a65cc52df2ef647f14107b5bb47a0d08fe8143016b.

- 2026-09-11T03:09:04+00:00: Recorded command exit 101; command argv SHA-256
  af5e44d787e9208e53cff81da0f5c8bb1ef67ce1efd651d201d21ff5e5b366d4.

- 2026-09-11T03:09:46+00:00: Recorded command exit 1; command argv SHA-256
  e4a53e5adcbc9bfb13af2529123dc8ea806235dbd289b437a5c3ea8d23fe33b9.

- 2026-09-11T03:10:39+00:00: Recorded command exit 0; command argv SHA-256
  2686d5aa5f6feefe46da8cd5d651b7a7ad0f3a9c1c90d89e95a76a71db98cb1d.

- 2026-09-11T03:11:16+00:00: Recorded command exit 0; command argv SHA-256
  7fd8c0fb13aff8b3d8b7a78f1b8eda753278dfebf33959cc06844fe06e9834e1.

- 2026-09-11T03:11:28+00:00: Recorded command exit 0; command argv SHA-256
  af5e44d787e9208e53cff81da0f5c8bb1ef67ce1efd651d201d21ff5e5b366d4.

- 2026-09-11T03:11:43+00:00: Recorded command exit 0; command argv SHA-256
  c66e1c206879289fc5d297fcae4889d890c69df3f2b51ff0b1164760a5869c9c.

- 2026-09-11T03:12:50+00:00: Recorded command exit 0; command argv SHA-256
  8e8687aad27cb421813451b30dcaef4715b8689c6041b259926b0dc4a71f4841.

- 2026-09-11T03:13:14+00:00: Recorded command exit 0; command argv SHA-256
  26557d97d0d1776548c1213341aad8dae26ff82cea35e979cd8f229527d56d82.

- 2026-09-11T03:13:43+00:00: Recorded command exit 0; command argv SHA-256
  cfe4545c613f39085dc4339fee017d586bacf818dd5364b64e79c7d0767587d0.

- 2026-09-11T03:14:18+00:00: Recorded command exit 0; command argv SHA-256
  774fe62fa503198a6e2b3a9d8b1ee582a2049d1882c286543e98aeb918dca521.

- 2026-09-11T03:14:40+00:00: Recorded command exit 0; command argv SHA-256
  b4f1f5ce4169a9b2aa9e05b8b064e8de2bd79773612662770e8c8fd125e6c846.

- 2026-09-11T03:14:54+00:00: Recorded command exit 0; command argv SHA-256
  0b979fc794fdc9b025fa3616bfa15b8abec550fe4602c212ecc1a08a4773cabe.

- 2026-09-11T03:15:53+00:00: Recorded command exit 0; command argv SHA-256
  5843a393aefd686e89e6e98b39fd4452371bdaad3d67b69d48b15dd46c26092c.

- 2026-09-11T03:16:21+00:00: Recorded command exit 0; command argv SHA-256
  9a7cc74d9bedee686c709f917462e9e9e285817e531781e4ccc7f687b778f791.

- 2026-09-11T03:16:35+00:00: Recorded command exit 1; command argv SHA-256
  98142ce2eec0e8095948e61c887560edc03b6f4913c9ac628620f346c9867625.

- 2026-09-11T03:17:05+00:00: Recorded command exit 0; command argv SHA-256
  0e3dfa6f6e89f42e94016bc660f903f42c634c7ac93fb691048ffa65f8c682d8.

- 2026-09-11T03:17:39+00:00: Recorded command exit 0; command argv SHA-256
  523a169f4dacd95d5bb98a16513204aea88da4f5354056a152bd59945d02d134.

- 2026-09-11T03:17:53+00:00: Recorded command exit 0; command argv SHA-256
  35000ac4c52c28ee51660797e3dfa9b9a4c41efacacfde6d616df1e647cad40d.

- 2026-09-11T03:19:03+00:00: Recorded command exit 0; command argv SHA-256
  23f3849df54009ebb9a909c8e248923ba37cb5330bca225c8cb55a8da2f79b98.

- 2026-09-11T03:19:24+00:00: Implementation checkpoint: one test-only file. 26/26 serial terminal
  tests passed; five consecutive complete serial suites passed (130 tests) and scoped exact AR-1050
  binary leak audit found 0. Injected observer tests require unavailable then two equal samples,
  reject alternating/one-sample/timeout/mismatched retained authority, and pre-option
  server/session/window/pane transition issues zero option commands. The earlier exit 1 was cargo
  fmt --check reporting only deterministic formatting delta; cargo fmt applied and subsequent
  fmt/test passed.

- 2026-09-11T03:19:39+00:00: Recorded command exit 101; command argv SHA-256
  dcf7241ff465e3a347279082075342a8aaa6614352dc84211ed3751240023d12.

- 2026-09-11T03:19:58+00:00: Recorded command exit 0; command argv SHA-256
  08de3d1e19760d76532da9d6d8985e6699a8fc1d1ec5fe7ab69aa360cdaa5cdb.

- 2026-09-11T03:20:56+00:00: Recorded command exit 0; command argv SHA-256
  dcf7241ff465e3a347279082075342a8aaa6614352dc84211ed3751240023d12.

- 2026-09-11T03:21:20+00:00: Recorded command exit 1; command argv SHA-256
  b1888007d20e4b60e2a5f59148c4d62e38da9102de9686291461f15258d5b92c.

- 2026-09-11T03:21:36+00:00: Recorded command exit 0; command argv SHA-256
  455ec7507d230a1c031642caf3294ecfc41c1f97aa8765631345418e852d7456.

- 2026-09-11T03:21:53+00:00: Recorded command exit 1; command argv SHA-256
  b08098166a0a19737a1102104a7cdae58445843fd0b7a8caaead54608b4de927.

- 2026-09-11T03:22:30+00:00: Recorded command exit 0; command argv SHA-256
  8ef87a0fa93cca2090a649132b79a29358e08e06014c5aa13ebbc1bd8dbd29ac.

- 2026-09-11T03:22:46+00:00: Recorded command exit 1; command argv SHA-256
  43e5ca04c7a77474caca99cb111502726917cd2ea40ca8807bd93dfcc33d97ea.

- 2026-09-11T03:23:06+00:00: Recorded command exit 0; command argv SHA-256
  2db936ec7ff82af3caf77e2a3956d3eabe486b6a0e08212263324b353ada266a.

- 2026-09-11T03:23:24+00:00: Recorded command exit 0; command argv SHA-256
  de390170af68b69d5b2f27394433c27b1e9a380aac65d3114f21b1b661be382c.

- 2026-09-11T03:23:45+00:00: Recorded command exit 0; command argv SHA-256
  9f4490d394acc03fdecdf545a2ef571a50207151abf17cbcf127859a49c49b39.

- 2026-09-11T03:24:28+00:00: Recorded command exit 0; command argv SHA-256
  2bf72c23ed925dac00a56939555a81732f81d4d32d2c1c3fb77ad6d8f099f621.

- 2026-09-11T03:24:41+00:00: Recorded command exit 0; command argv SHA-256
  bf313c9cd77e0b797999b9c3d87f568051175e3957ad5d0494e49b45852a6a1d.

- 2026-09-11T03:25:14+00:00: Signed+DCO candidate c465aa6a06395f11bdbf757d92f315b1b89603b7 is clean
  and unpushed. Five serial terminal suites passed (130/130), scoped exact binary leaks 0, full
  coverage-clean passed at 91.44% lines, and all applicable
  Rust/docs/schema/release/supply-chain/shell/workflow/privacy gates passed. Combined supply gate
  exit 1 ended at cargo audit with no diagnostic; immediate identical standalone audit passed, so
  classified transient tool/index execution. Earlier coverage exit 1 was its documented clean-tree
  precondition on the precommit dirty diff; exact clean commit rerun passed.

- 2026-09-11T03:26:04+00:00: Recorded command exit 0; command argv SHA-256
  0c15c887bbb76da525105eadf3fbf7d146b2ac8f9afbfd8837b1707682057c6f.

- 2026-09-11T03:26:23+00:00: Recorded command exit 0; command argv SHA-256
  b7bd69ab126eb48d9e2bc3a2783774db218a13142314436ccab1edf2005ff601.

- 2026-09-11T03:26:35+00:00: Recorded command exit 0; command argv SHA-256
  e1ee139710c75ecef8da8ff683d90981b954f68dd6f58dddf6ef39187a8d6292.

- 2026-09-11T03:27:39+00:00: Recorded command exit 0; command argv SHA-256
  56023cc2b647bc7e970198287aef04347644fe9ed136b8e1d6d59db16018fe8d.

- 2026-09-11T03:28:30+00:00: Recorded command exit 0; command argv SHA-256
  c8d7a953cbcb2631fdf2e20140d1fb3c836163f6f625bc181729ce73cb9f4f39.

- 2026-09-11T03:29:00+00:00: Recorded command exit 0; command argv SHA-256
  1d3a24aa87e1d44451198e4904f2c1fefd7065db22c87ced9295ec281eb61c52.

- 2026-09-11T03:29:38+00:00: Recorded command exit 0; command argv SHA-256
  5c5d9e16d9361e89476afb1165abfc22a4f9be48151540baf60b303635d7f208.

- 2026-09-11T03:29:56+00:00: Recorded command exit 1; command argv SHA-256
  af593997eea1919b66a6a98852b3ccad3aa202641c023fe2c02e3c539213d52f.

- 2026-09-11T03:30:14+00:00: Recorded command exit 101; command argv SHA-256
  698033a1d39a083f38c48f8f6e63363ccbd3f4e426f71ccbe25b27a67644e23e.

- 2026-09-11T03:30:37+00:00: Recorded command exit 0; command argv SHA-256
  230e903031c3550c7091faa1c153528fd03e48b50b4b2b97d51686e4f8b0a36f.

- 2026-09-11T03:30:51+00:00: Recorded command exit 101; command argv SHA-256
  af593997eea1919b66a6a98852b3ccad3aa202641c023fe2c02e3c539213d52f.

- 2026-09-11T03:31:11+00:00: Recorded command exit 0; command argv SHA-256
  777e11819b30d2ebeb0a523f7c9e10e7373a217f5e32a261ddcc3cc3fbfee279.

- 2026-09-11T03:31:41+00:00: Recorded command exit 0; command argv SHA-256
  af593997eea1919b66a6a98852b3ccad3aa202641c023fe2c02e3c539213d52f.

- 2026-09-11T03:31:56+00:00: Recorded command exit 0; command argv SHA-256
  7e0586a811cb5dc5006774c46e1c7226fad275782b0e8f31207c0ea3ebd8ff6d.

- 2026-09-11T03:33:01+00:00: Recorded command exit 0; command argv SHA-256
  4513aaa67289121d7838ad7745091919f696fd2f994ae7fb71b1505b4067b6c5.

- 2026-09-11T03:33:38+00:00: Recorded command exit 0; command argv SHA-256
  2bf72c23ed925dac00a56939555a81732f81d4d32d2c1c3fb77ad6d8f099f621.

- 2026-09-11T03:34:17+00:00: Obsolete c465aa6/dfdcecf were blocked by two live-fixture guard
  invariants. Exact 46145ad repairs both: malformed output enters guarded finisher immediately;
  authenticated startup is stored inside the guard and the real option path can only derive
  authority from that guard. No-pane guard proves zero observer/option calls and exact server
  cleanup. Final five serial suites passed (130/130), exact binary leaks 0, fmt/clippy and
  coverage-clean full suite passed at 91.44%. Compile exits 101 while adding the guard field were
  code-local missing-pattern and large-enum lint findings; repaired with exhaustive pattern and
  boxed retained tuple, then rerun green.

- 2026-09-11T03:41:11+00:00: Recorded command exit 0; command argv SHA-256
  0ac211a990d74c1be636dfdc9132b23efde5d70e8627140f51e276cda087e1ab.

- 2026-09-11T03:42:13+00:00: Recorded command exit 0; command argv SHA-256
  d98dfba1b5881e33e4de556acd5d22cb51ca1213217e5b329a931c06c64919df.

- 2026-09-11T03:44:12+00:00: Heartbeat by codex-ar1050-tmux-startup-readiness-20260911.

- 2026-09-11T03:44:24+00:00: Independent immutable review APPROVED exact signed+DCO head
  46145ad63af61d0b6f4549f06c001f33d60f02c1, tree b64bd9d15a985deb43373ebff8140a3bfa2a8cef. Resume
  governed delivery without source mutation.

- 2026-09-11T03:45:08+00:00: Recorded command exit 0; command argv SHA-256
  daa1eef0769700492f01c420be8be4ebf9e7f446659a89654bddea45ea0195a7.

- 2026-09-11T03:45:34+00:00: Recorded command exit 0; command argv SHA-256
  f2bd3312ab652dff1d48fd1dc2c183bad68cfc2ce31a7e6b7246788e05ac3428.

- 2026-09-11T03:45:48+00:00: Recorded command exit 0; command argv SHA-256
  71f3776bcfff7ef81a8715dd00dfb89e4fd6324eebd9161a719380c6f91fd569.
