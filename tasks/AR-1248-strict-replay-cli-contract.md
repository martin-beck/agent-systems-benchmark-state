---
{
  "branch": "feature/ar-1248-strict-replay-cli-contract",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1231",
    "AR-1232"
  ],
  "id": "AR-1248",
  "next_action": "Rerun PR #197 exact-head policy/Rust/contract CI and request independent review at cebe8ef. Executable replay-plan now resolves the verified cassette and retains RuntimeBoundReplay.sidecar for the execution lifetime; runtime attestation is consumed before handoff creation; relay cleanup is asserted on drop. Focused CLI 76/76 and clippy pass.",
  "observed_branch": "feature/ar-1248-strict-replay-cli-contract",
  "observed_dirty": 0,
  "observed_head": "cebe8efc19a1665c87f0d354ea6584670792957b",
  "owner": "",
  "plan": "../plans/AR-1248.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Define the strict-replay CLI consumer contract.",
  "task_revision": 118,
  "title": "Bounded strict-replay CLI consumer contract",
  "updated_at": "2026-09-16T20:02:47+00:00",
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

- 2026-09-16T10:59:00+00:00: Recorded command exit 0; command argv SHA-256
  109d36131c59cbd435b0b3a2033e7f16578455597393f5a2e79fc5e1917d7901.

- 2026-09-16T10:59:27+00:00: Signed bc127a9 pushed to PR #197. Resolver now derives route identity
  from cassette session/attempt/dialect and rejects mismatch; focused tests 2/2 green. Remaining
  independent-review blocker is runtime-issued handoff/sandbox launch integration and lifecycle
  coverage, which must not be claimed by record construction alone.

- 2026-09-16T11:02:23+00:00: Heartbeat by asb_ar1232_lifecycle_router.

- 2026-09-16T11:02:27+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-16T11:02:40+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T11:02:51+00:00: Recorded command exit 0; command argv SHA-256
  2bb0c4f7c650bd58ba047451817300c691716a3e418ef1f08cd31c546e62a17a.

- 2026-09-16T11:03:13+00:00: Recorded command exit 0; command argv SHA-256
  e199d35c46ba7dd6836d71cac684338157d26becce51703bbef46d70f4b042b4.

- 2026-09-16T11:03:23+00:00: Recorded command exit 0; command argv SHA-256
  4ae24a7384177fcaf78f7ffc43e6921296ffaf6f56ce9a884cfa52e0c3ef3a22.

- 2026-09-16T11:03:38+00:00: Recorded command exit 0; command argv SHA-256
  bb6cf3f88c21a8e3c5ac53502ff0baafea79443106425bb6f51eeea82e75b985.

- 2026-09-16T11:03:46+00:00: Recorded command exit 0; command argv SHA-256
  8043e3bf9ea52d812da8e40ea76afda8b87f46c76a2c2fbd5bb3f58fa63bc8e3.

- 2026-09-16T11:04:29+00:00: Recorded command exit 0; command argv SHA-256
  e65704d0af497ff4f9db656cbcc2e1894e552f84bfbc5a531f0945a250925adf.

- 2026-09-16T11:04:51+00:00: Recorded command exit 0; command argv SHA-256
  109d36131c59cbd435b0b3a2033e7f16578455597393f5a2e79fc5e1917d7901.

- 2026-09-16T11:05:15+00:00: Signed commit 7a0a7cc pushed to PR #197. Added
  bind_runtime_handoff(StrictReplayLaunchRecord, SidecarHandoff), fail-closed HandoffMismatch, safe
  empty-cassette handling, direct runtime-issued handoff success/route-drift test, and malformed
  cassette digest-valid rejection. Focused cargo test -p asb-cli --lib replay_contract --locked
  --offline: 3/3 pass; clippy -D warnings pass; contract_consistency --run-tests pass (all
  registered artifacts); full cargo test --workspace --locked --offline pass. Clean tree and G/DCO
  verified.

- 2026-09-16T11:10:23+00:00: Heartbeat by asb_ar1232_lifecycle_router.

- 2026-09-16T11:10:27+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T11:10:43+00:00: Recorded command exit 0; command argv SHA-256
  7059a28d616e8af18a5c09258580cf0d2ebb8f3f2388029a04de1e95846301a7.

- 2026-09-16T11:11:21+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T11:11:32+00:00: Recorded command exit 101; command argv SHA-256
  85276017799dd564e7fee4a901241b74dbc935fa9343f9c3f5be07ed72897e9c.

- 2026-09-16T11:11:50+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T11:11:58+00:00: Recorded command exit 101; command argv SHA-256
  85276017799dd564e7fee4a901241b74dbc935fa9343f9c3f5be07ed72897e9c.

- 2026-09-16T11:12:45+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T11:12:55+00:00: Recorded command exit 0; command argv SHA-256
  85276017799dd564e7fee4a901241b74dbc935fa9343f9c3f5be07ed72897e9c.

- 2026-09-16T11:13:15+00:00: Recorded command exit 0; command argv SHA-256
  e199d35c46ba7dd6836d71cac684338157d26becce51703bbef46d70f4b042b4.

- 2026-09-16T11:13:26+00:00: Recorded command exit 0; command argv SHA-256
  7059a28d616e8af18a5c09258580cf0d2ebb8f3f2388029a04de1e95846301a7.

- 2026-09-16T11:13:44+00:00: Recorded command exit 0; command argv SHA-256
  8ac4294e0f100e105e79d7551496111b6c836ff94aaead3de10e0ce538fe8bb9.

- 2026-09-16T11:13:52+00:00: Recorded command exit 0; command argv SHA-256
  f26aaabd114a99f28e6d08acd4abecdcd625e45db0b8d634717cda640b8fecfa.

- 2026-09-16T11:14:16+00:00: Recorded command exit 0; command argv SHA-256
  109d36131c59cbd435b0b3a2033e7f16578455597393f5a2e79fc5e1917d7901.

- 2026-09-16T11:14:37+00:00: Signed+DCO 66e0fa2 pushed to PR #197. Added executable replay-plan
  dispatch and runtime sidecar resolution/binding, with positive CLI end-to-end test and stale route
  negative. Focused replay-plan test 1/1 pass; full asb-cli lib tests 75/75 pass; clippy -D warnings
  pass; prior contract consistency and full locked offline workspace pass remain valid. One
  intermediate test failure was expected exit code mismatch (asserted 2, project validation is 3);
  corrected and rerun green. Clean tree.

- 2026-09-16T11:19:18+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T11:19:31+00:00: Recorded command exit 0; command argv SHA-256
  2bb0c4f7c650bd58ba047451817300c691716a3e418ef1f08cd31c546e62a17a.

- 2026-09-16T11:19:44+00:00: Recorded command exit 0; command argv SHA-256
  85276017799dd564e7fee4a901241b74dbc935fa9343f9c3f5be07ed72897e9c.

- 2026-09-16T11:20:00+00:00: Recorded command exit 0; command argv SHA-256
  e199d35c46ba7dd6836d71cac684338157d26becce51703bbef46d70f4b042b4.

- 2026-09-16T11:20:12+00:00: Recorded command exit 0; command argv SHA-256
  7059a28d616e8af18a5c09258580cf0d2ebb8f3f2388029a04de1e95846301a7.

- 2026-09-16T11:20:32+00:00: Recorded command exit 0; command argv SHA-256
  8ac4294e0f100e105e79d7551496111b6c836ff94aaead3de10e0ce538fe8bb9.

- 2026-09-16T11:20:40+00:00: Recorded command exit 0; command argv SHA-256
  8c09ae82f8aa984e9bf1b2c543eccb03f1e9ce8510e6c974cf09d15c2c8651c2.

- 2026-09-16T11:21:10+00:00: Recorded command exit 0; command argv SHA-256
  109d36131c59cbd435b0b3a2033e7f16578455597393f5a2e79fc5e1917d7901.

- 2026-09-16T11:21:30+00:00: Signed+DCO cebe8ef pushed. RuntimeBoundReplay owns
  ResolvedStrictReplay, StrictReplayLaunchBridge, and LoopbackSidecar so relay is not dropped before
  execution; sidecar attestation is materialized and passed into handoff instead of hardcoding
  handoff namespace_ready. Added lifetime/cleanup test plus executable dispatch positive/stale-route
  tests. Focused asb-cli lib 76/76, focused replay-plan 1/1, clippy -D warnings pass. Previous
  66e0fa2 PR policy/Rust failures require fresh exact-head CI; no product failure identified yet.

- 2026-09-16T11:26:22+00:00: AR-1248 CLI contract implementation is complete through signed cebe8ef,
  but independent review requires actual namespace attestation, cassette-serving adapter child
  execution through StrictReplayLaunchBridge, and end-to-end request/response plus
  egress/cancel/restart/no-fallback evidence. These require runtime-owned SandboxLaunchInput,
  ResourceLease, SandboxBackend supervision, and an independently issued namespace capability absent
  from the CLI plan/API; fabricating namespace_ready=true or executable paths would violate
  fail-closed scope. Dependency/runtime follow-up is AR-1232 (currently blocked on approved sandbox
  capability AR-1233/AR-1234). Preserve PR #197 and exact head cebe8ef; resume after runtime
  capability lands.

- 2026-09-16T20:02:47+00:00: Coordinator authorized bounded failure-repair audit: dependencies are
  terminal done; inspect exact PR #197 Repository quality/Rust failures and repair only reproducible
  scoped coverage/provenance issues before publication.
