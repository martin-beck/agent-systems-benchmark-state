---
{
  "branch": "feature/ar-1248-strict-replay-cli-contract",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T21:16:46+00:00",
  "depends_on": [
    "AR-1231",
    "AR-1232"
  ],
  "id": "AR-1248",
  "next_action": "Await a runtime-owned successor that supplies independently attested namespace capability plus supervised SandboxLaunchInput/ResourceLease. Then wire replay_plan through StrictReplayLaunchBridge::spawn and add real request/response, egress-denial, cancellation/restart/cleanup and no-fallback tests. Preserve PR #197 head 7d9c2ee and its green CI; do not fabricate namespace readiness in CLI.",
  "observed_branch": "feature/ar-1248-strict-replay-cli-contract",
  "observed_dirty": 0,
  "observed_head": "7d9c2ee2e08b9d61cb03837236918575405fb5c2",
  "owner": "coordinator-successor-creation",
  "plan": "../plans/AR-1248.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Define the strict-replay CLI consumer contract.",
  "task_revision": 153,
  "title": "Bounded strict-replay CLI consumer contract",
  "updated_at": "2026-09-16T20:46:48+00:00",
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

- 2026-09-16T20:02:49+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-16T20:03:13+00:00: Recorded command exit 0; command argv SHA-256
  f489a19876782722ed16d09ca01ff72aa074415a2bb4183d7206b5819538e360.

- 2026-09-16T20:04:04+00:00: Recorded command exit 0; command argv SHA-256
  4b2f8f087bf217cebb690fc5079fb08ab8bab2944d87ea71b4f286ec9130b722.

- 2026-09-16T20:04:35+00:00: Recorded command exit 101; command argv SHA-256
  95c14b9abf735939b9e9324b41bf3e083d79848364d781f329a36049529e8387.

- 2026-09-16T20:06:09+00:00: Recorded command exit 101; command argv SHA-256
  8f82fb17898790624dbd122514be33159123f346dc6b64572124225911961878.

- 2026-09-16T20:06:54+00:00: Recorded command exit 0; command argv SHA-256
  95c14b9abf735939b9e9324b41bf3e083d79848364d781f329a36049529e8387.

- 2026-09-16T20:07:48+00:00: Recorded command exit 0; command argv SHA-256
  f64fe7b41b29315c3ef437fc62cbea67fcb63999b3a4acdc251cdbc1a664ae38.

- 2026-09-16T20:08:08+00:00: Recorded command exit 0; command argv SHA-256
  a5e91d8a6e356ba88fd4835c765ebd2411c75eacaa60f98e203295ec257bd3a5.

- 2026-09-16T20:08:16+00:00: Recorded command exit 0; command argv SHA-256
  43ea9928318902aa9759fb71da6ab8f4065ad9187c052d4dbcfab10689b865dc.

- 2026-09-16T20:08:38+00:00: Recorded command exit 0; command argv SHA-256
  95c14b9abf735939b9e9324b41bf3e083d79848364d781f329a36049529e8387.

- 2026-09-16T20:09:11+00:00: Recorded command exit 0; command argv SHA-256
  3bd05d41ad1e7e81a241742cb8f9bc4068ab10db15e7786209352d8936230537.

- 2026-09-16T20:09:33+00:00: Diagnosed PR #197 failures: workflow_transcript provenance assertion
  used a stale 63-character cli_source_sha256. Updated only
  docs/examples/asb-cli-workflow-v1.provenance.json to the exact 64-character digest for
  crates/asb-cli/src/lib.rs. Signed+DCO commit 7d9c2ee pushed; focused transcript tests 3/3 pass,
  full locked offline workspace test gate passes, git signature verifies, and worktree is clean.
  Prior runtime attestation/replay-supervision review blocker remains distinct and unresolved; no
  merge requested.

- 2026-09-16T20:10:12+00:00: Heartbeat by asb_ar1024_lifecycle_router.

- 2026-09-16T20:12:20+00:00: Independent review blocker recorded: replay_plan creates
  LoopbackSidecar with literal attestation and does not invoke StrictReplayLaunchBridge::spawn,
  SandboxBackend, ResourceLease, or supervised child execution. Therefore end-to-end cassette
  request/response, provider-egress denial, cancellation/cleanup, restart and no-fallback evidence
  remain unproven. Do not merge; retain exact-head CI monitoring and route runtime integration to
  the approved runtime capability successor if outside this CLI contract.

- 2026-09-16T20:20:27+00:00: Terminal exact-head CI recorded for PR #197 head 7d9c2ee: AArch64
  portability run 35144819641, Formal assurance run 35144819644, Repository quality run 35144819653,
  Rust verification run 35144819699, plus AWQ 35144819681, Fault assurance 35144819716, Platform
  evidence 35144819659, and headers 35144819652 all concluded SUCCESS. Independent review still
  blocks publication because replay_plan does not invoke supervised runtime child launch or prove
  end-to-end transport lifecycle.

- 2026-09-16T20:20:30+00:00: Released ownerless/open after terminal exact-head CI success.
  Runtime-supervision integration remains the explicit next action; PR #197 must not merge until
  independent review clears supervised child transport, egress denial, cancellation/restart/cleanup
  and no-fallback evidence.

- 2026-09-16T20:21:38+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-16T20:21:48+00:00: Recorded command exit 0; command argv SHA-256
  7ff9f66199d2a3b292f342dc948a1ca42fe8b8eaf5af3227964d3e7c23db0f27.

- 2026-09-16T20:22:24+00:00: Scope audit complete: AR-1248 acceptance names SidecarHandoff/sandbox
  launch input, but current runtime APIs require a runtime-issued namespace capability and
  supervised launch context absent from the CLI. replay_contract.rs calls attest_with_commands(true,
  ...) and only constructs/returns a bridge; replay_plan never invokes
  StrictReplayLaunchBridge::spawn, SandboxBackend or ResourceLease. Implementing those in CLI would
  duplicate/forge runtime authority. Required repair is a dependency-linked runtime successor; no
  product mutation made.

- 2026-09-16T20:22:27+00:00: Released ownerless/open after scope audit. CLI contract and provenance
  repair remain clean with PR #197 exact head 7d9c2ee and green required CI; runtime-owned
  attestation/supervised child launch is explicitly delegated to the successor capability before
  further AR-1248 work.

- 2026-09-16T20:26:24+00:00: Claimed by coordinator-successor-creation.

- 2026-09-16T20:26:32+00:00: Recorded command exit 0; command argv SHA-256
  9f559a9ce801ac827cebd8cfb5690f76c26e68a992eb3343e484aceaa713ee96.

- 2026-09-16T20:26:45+00:00: Created coordinator successor AR-1260 for runtime-owned attestation and
  supervised strict-replay integration; preserve exact reviewed head 7d9c2ee and do not merge until
  successor evidence passes.

- 2026-09-16T20:45:03+00:00: Claimed by coordinator-successor-creation.

- 2026-09-16T20:45:06+00:00: Recorded command exit 128; command argv SHA-256
  fb29cf57dd905e88fd2cffdea26ab8d181e453e100e967f2742d15deeb7501c4.

- 2026-09-16T20:45:14+00:00: Coordinator added AR-1261 successor for runtime-to-CLI authority
  entrypoint; preserve reviewed AR-1248 exact head and green CI.

- 2026-09-16T20:45:55+00:00: Claimed by coordinator-successor-creation.

- 2026-09-16T20:45:57+00:00: Recorded command exit 0; command argv SHA-256
  fb29cf57dd905e88fd2cffdea26ab8d181e453e100e967f2742d15deeb7501c4.

- 2026-09-16T20:46:06+00:00: Added AR-1261 successor for runtime-to-CLI authority entrypoint in ASB
  state; preserve AR-1248 reviewed head.

- 2026-09-16T20:46:46+00:00: Claimed by coordinator-successor-creation.

- 2026-09-16T20:46:48+00:00: Recorded command exit 0; command argv SHA-256
  acb3db6bed7adf8787c06d9033986f094b5500c9f2a11c9e4628e484c810b236.
