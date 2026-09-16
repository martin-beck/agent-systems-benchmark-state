---
{
  "branch": "feature/ar-1248-strict-replay-cli-contract",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T12:50:51+00:00",
  "depends_on": [
    "AR-1231",
    "AR-1232"
  ],
  "id": "AR-1248",
  "next_action": "Review blocks merge: integrate resolver with runtime-issued SidecarHandoff/SandboxLaunchInput seam or narrow acceptance with coordinator; cross-validate cassette route/dialect and add malformed/executor lifecycle tests before new signed head.",
  "observed_branch": "feature/ar-1248-strict-replay-cli-contract",
  "observed_dirty": 0,
  "observed_head": "bc127a9d87fb893bbf8b52102d318507cc92d2c3",
  "owner": "asb_ar1232_lifecycle_router",
  "plan": "../plans/AR-1248.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Define the strict-replay CLI consumer contract.",
  "task_revision": 72,
  "title": "Bounded strict-replay CLI consumer contract",
  "updated_at": "2026-09-16T10:58:47+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1248"
}
---

Implement only the linked AR-1248 plan using the ASB development documentation and handoffctl.
Preserve zero-runtime-dependency, offline-after-install, provider-egress denial, and all native,
formal, privacy, signature, DCO, and exact-tree gates.

- 2026-09-16T10:33:49+00:00: Dependencies AR-1231 and AR-1232 are durably done on protected main;
  strict replay CLI consumer gap is concrete and dependency-ready.

- 2026-09-16T10:34:06+00:00: Claimed by asb_ar1232_lifecycle_router.

- 2026-09-16T10:34:37+00:00: Heartbeat by asb_ar1232_lifecycle_router.

- 2026-09-16T10:35:47+00:00: Heartbeat by asb_ar1232_lifecycle_router.

- 2026-09-16T10:37:41+00:00: Recorded command exit 101; command argv SHA-256
  2bb0c4f7c650bd58ba047451817300c691716a3e418ef1f08cd31c546e62a17a.

- 2026-09-16T10:38:05+00:00: Recorded command exit 101; command argv SHA-256
  2bb0c4f7c650bd58ba047451817300c691716a3e418ef1f08cd31c546e62a17a.

- 2026-09-16T10:38:27+00:00: Recorded command exit 0; command argv SHA-256
  69487790cd46864562a51f207e108eea84da8519a17023da666d53127f8fc1e6.

- 2026-09-16T10:38:45+00:00: Recorded command exit 0; command argv SHA-256
  2bb0c4f7c650bd58ba047451817300c691716a3e418ef1f08cd31c546e62a17a.

- 2026-09-16T10:39:38+00:00: Recorded command exit 0; command argv SHA-256
  5cd7f7ecbd072b19f8bcf922677100f3be60e4ce8a4254b8d6fd3e991baa2b30.

- 2026-09-16T10:40:08+00:00: Heartbeat by asb_ar1232_lifecycle_router.

- 2026-09-16T10:40:11+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-16T10:40:42+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T10:41:00+00:00: Recorded command exit 0; command argv SHA-256
  2bb0c4f7c650bd58ba047451817300c691716a3e418ef1f08cd31c546e62a17a.

- 2026-09-16T10:41:26+00:00: Recorded command exit 0; command argv SHA-256
  e199d35c46ba7dd6836d71cac684338157d26becce51703bbef46d70f4b042b4.

- 2026-09-16T10:41:47+00:00: Recorded command exit 0; command argv SHA-256
  7adfa5f47f2d88e04500f07dc00da634ef9b56c7337415589d392c96b685c882.

- 2026-09-16T10:41:57+00:00: Recorded command exit 0; command argv SHA-256
  86b0d1dd71b4402f8180c78ddf5c60ead0d27e36ce1372707ea4c99ae0cb36e4.

- 2026-09-16T10:42:30+00:00: Signed commit 37a9c2b adds StrictReplayPlanV1 resolver with explicit
  bounded artifact root, symlink/traversal/size/digest/malformed rejection, authenticated
  StrictReplayLaunchRecord construction, schema/fixture/catalog/docs, and positive/negative tests.
  Focused unit tests 2/2 and clippy -D warnings pass; initial locked test failure was missing
  Cargo.lock entries, fixed by offline cargo check and rerun green. Worktree clean.

- 2026-09-16T10:42:55+00:00: Recorded command exit 0; command argv SHA-256
  4ae24a7384177fcaf78f7ffc43e6921296ffaf6f56ce9a884cfa52e0c3ef3a22.

- 2026-09-16T10:43:28+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T10:43:38+00:00: Recorded command exit 0; command argv SHA-256
  2bb0c4f7c650bd58ba047451817300c691716a3e418ef1f08cd31c546e62a17a.

- 2026-09-16T10:43:52+00:00: Recorded command exit 0; command argv SHA-256
  bb6cf3f88c21a8e3c5ac53502ff0baafea79443106425bb6f51eeea82e75b985.

- 2026-09-16T10:44:01+00:00: Recorded command exit 0; command argv SHA-256
  b0d4b6f53dc5fc9c746c248454e3bcceb4f4000c11ced3206a82309d83272144.

- 2026-09-16T10:44:24+00:00: Independent review gap fixed in signed eac5232: explicit symlink,
  unknown egress deserialization, and oversized artifact rejection tests. Focused replay-contract
  tests remain 2/2 green; worktree clean.

- 2026-09-16T10:44:36+00:00: Recorded command exit 0; command argv SHA-256
  9e079f6e1c4242860e970aae23083791b47dd4a5386aae23d4066c61128e44e5.

- 2026-09-16T10:44:59+00:00: Recorded command exit 0; command argv SHA-256
  1adb6576bf82757e355b703435b8236b4d15ae8b7104b4eb56d0a87cf3e6b9c8.

- 2026-09-16T10:45:39+00:00: Recorded command exit 101; command argv SHA-256
  e65704d0af497ff4f9db656cbcc2e1894e552f84bfbc5a531f0945a250925adf.

- 2026-09-16T10:46:08+00:00: Recorded command exit 0; command argv SHA-256
  a8194f3965983e5bb8eac8aaf23f2cf7ecd510b5517db3c36ec902746864e86e.

- 2026-09-16T10:46:26+00:00: Recorded command exit 0; command argv SHA-256
  a5e91d8a6e356ba88fd4835c765ebd2411c75eacaa60f98e203295ec257bd3a5.

- 2026-09-16T10:46:37+00:00: Recorded command exit 0; command argv SHA-256
  ce7d45fffe378f17b6453e4e851b9576b579444d490ac31ccb139f845c58245e.

- 2026-09-16T10:47:01+00:00: Recorded command exit 0; command argv SHA-256
  109d36131c59cbd435b0b3a2033e7f16578455597393f5a2e79fc5e1917d7901.

- 2026-09-16T10:47:18+00:00: Recorded command exit 8; command argv SHA-256
  457dad11b37c52ae4a46a832d7a082caacae43e9439a5c72cb55c17e0435bbed.

- 2026-09-16T10:47:43+00:00: Workflow provenance digest failure from full gate was diagnosed and
  fixed in signed 8896cad; focused workflow_transcript 3/3 passes. PR #197 updated from eac5232 to
  8896cad. Contract consistency, focused replay tests 2/2, clippy, and prior full workspace reached
  only this stale-fixture failure.

- 2026-09-16T10:48:21+00:00: Recorded command exit 0; command argv SHA-256
  e65704d0af497ff4f9db656cbcc2e1894e552f84bfbc5a531f0945a250925adf.

- 2026-09-16T10:48:32+00:00: Recorded command exit 8; command argv SHA-256
  457dad11b37c52ae4a46a832d7a082caacae43e9439a5c72cb55c17e0435bbed.

- 2026-09-16T10:49:29+00:00: Recorded command exit 8; command argv SHA-256
  457dad11b37c52ae4a46a832d7a082caacae43e9439a5c72cb55c17e0435bbed.

- 2026-09-16T10:49:38+00:00: Recorded command exit 8; command argv SHA-256
  457dad11b37c52ae4a46a832d7a082caacae43e9439a5c72cb55c17e0435bbed.

- 2026-09-16T10:50:24+00:00: Recorded command exit 8; command argv SHA-256
  457dad11b37c52ae4a46a832d7a082caacae43e9439a5c72cb55c17e0435bbed.

- 2026-09-16T10:50:32+00:00: Recorded command exit 8; command argv SHA-256
  457dad11b37c52ae4a46a832d7a082caacae43e9439a5c72cb55c17e0435bbed.

- 2026-09-16T10:50:51+00:00: Heartbeat by asb_ar1232_lifecycle_router.

- 2026-09-16T10:51:14+00:00: Exact-head review rechecked: 10 scoped ASB files, no asb-tui changes,
  all three feature commits SSH-signed/DCO, diff-check clean, repository policy passed. Full locked
  offline workspace test passed after refreshing workflow provenance; PR #197 currently has 8
  completed green checks and 4 required lanes in progress.

- 2026-09-16T10:52:11+00:00: Recorded command exit 8; command argv SHA-256
  457dad11b37c52ae4a46a832d7a082caacae43e9439a5c72cb55c17e0435bbed.

- 2026-09-16T10:52:13+00:00: Recorded command exit 8; command argv SHA-256
  457dad11b37c52ae4a46a832d7a082caacae43e9439a5c72cb55c17e0435bbed.

- 2026-09-16T10:53:15+00:00: Recorded command exit 8; command argv SHA-256
  457dad11b37c52ae4a46a832d7a082caacae43e9439a5c72cb55c17e0435bbed.

- 2026-09-16T10:53:25+00:00: Recorded command exit 8; command argv SHA-256
  457dad11b37c52ae4a46a832d7a082caacae43e9439a5c72cb55c17e0435bbed.

- 2026-09-16T10:54:14+00:00: Recorded command exit 0; command argv SHA-256
  457dad11b37c52ae4a46a832d7a082caacae43e9439a5c72cb55c17e0435bbed.

- 2026-09-16T10:54:31+00:00: Recorded command exit 0; command argv SHA-256
  457dad11b37c52ae4a46a832d7a082caacae43e9439a5c72cb55c17e0435bbed.

- 2026-09-16T10:54:55+00:00: All 12 PR #197 CI checks are green at 8896cad, but independent review
  correctly identifies implementation gaps: resolver emits StrictReplayLaunchRecord only, does not
  construct runtime-issued SidecarHandoff/SandboxLaunchInput or supervised launch; route/provider
  dialect are not cassette-cross-validated; missing malformed cassette and executor
  lifecycle/egress/cancel/restart/no-fallback coverage. Do not merge until repaired or formally
  narrowed.

- 2026-09-16T10:55:50+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T10:56:07+00:00: Recorded command exit 101; command argv SHA-256
  2bb0c4f7c650bd58ba047451817300c691716a3e418ef1f08cd31c546e62a17a.

- 2026-09-16T10:56:34+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T10:56:54+00:00: Recorded command exit 0; command argv SHA-256
  2bb0c4f7c650bd58ba047451817300c691716a3e418ef1f08cd31c546e62a17a.

- 2026-09-16T10:57:06+00:00: Recorded command exit 0; command argv SHA-256
  ff954a573a552b3113c874db1fdd5ac4e98fb8a3477c20c22e06af7b07ff82fc.

- 2026-09-16T10:57:14+00:00: Recorded command exit 0; command argv SHA-256
  a98bcb963e3e8f10830e5d2875a53ea5949d457cda1b9f4abdd68883832ad21b.

- 2026-09-16T10:58:11+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T10:58:22+00:00: Recorded command exit 0; command argv SHA-256
  2bb0c4f7c650bd58ba047451817300c691716a3e418ef1f08cd31c546e62a17a.

- 2026-09-16T10:58:40+00:00: Recorded command exit 0; command argv SHA-256
  713749287af15dc46bdd0589bcc67c928ca3f92f50d6198922411436fb97efa2.
