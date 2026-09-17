---
{
  "branch": "feature/ar-1306-authenticated-fault-matrix-qualification",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-18T00:38:20+00:00",
  "depends_on": [
    "AR-1300",
    "AR-1287"
  ],
  "id": "AR-1306",
  "next_action": "CI repair commit 5425bc3891dc9325c4fe455953637e708b851527 is signed/DCO and pushed to PR #222. It selects the first reviewed bubblewrap 0.9.0 package version advertised by apt (allowlist 0.9.0-1ubuntu0.1/0.9.0-1build1), installs the exact version, and verifies dpkg version equality. Local qualified native tests and workspace gates pass. Await refreshed exact-head CI; prior gh checks exit 8 was pending-check status, not a product failure.",
  "observed_branch": "feature/ar-1306-authenticated-fault-matrix-qualification",
  "observed_dirty": 0,
  "observed_head": "5425bc3891dc9325c4fe455953637e708b851527",
  "owner": "codex-ar1306-auth-listener-20260917",
  "plan": "../plans/AR-1306.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify the real authenticated strict-replay service and fault matrix missing from PR #221.",
  "task_revision": 127,
  "title": "Authenticated strict-replay fault-matrix qualification",
  "updated_at": "2026-09-17T22:38:20+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1306-authenticated-fault-matrix-qualification"
}
---

## AR-1306

Implement the narrowly scoped ASB follow-on required by the independent review of PR #221 and
blocked AR-1301. The current fault helper does not prove a real `StrictReplayService`/relay
listener, positive authenticated identity/response parity, or cause-specific provider and
descendant egress denial. This AR owns those missing executable fixtures and their approved KVM
qualification evidence.

AR-1301 is the review predecessor, while AR-1300 and AR-1287 are hard runtime dependencies. The
predecessor is deliberately recorded in this task's scope rather than as a hard dependency to avoid
an impossible AR-1301 -> AR-1306 -> AR-1301 cycle. ASB only: do not change asb-tui, handoffctl,
credentials, live providers, or unrelated coordinator implementation.

Completion requires a real runtime-owned service/listener positive path, exact authenticated
cassette identity and response parity, distinct provider/descendant egress-denial causes, all
remaining lifecycle faults, bounded cleanup, sanitized provenance-bound evidence, signed+DCO
publication, independent review, green exact-head CI, protected merge and post-merge verification.

- 2026-09-17T21:31:46+00:00: Dependencies AR-1300 and AR-1287 are done; promote the real
  authenticated fault-matrix successor.

- 2026-09-17T21:32:09+00:00: Claimed by codex-ar1306-auth-listener-20260917.

- 2026-09-17T21:32:25+00:00: Recorded command exit 0; command argv SHA-256
  14925a15c4fe5ba5963acec8c3090fe2ca9ca1056d727a54d0042009cae057a2.

- 2026-09-17T21:34:09+00:00: Recorded command exit 128; command argv SHA-256
  a1d94ce312c5b430d26e3e641bea256dc176743e4ed993ef53757d7c6561be6f.

- 2026-09-17T21:34:31+00:00: Recorded command exit 0; command argv SHA-256
  c1d752b5a0735f834ef0bd43f0c8229908e54cf34bc2eabb9452d73fd8bd5780.

- 2026-09-17T21:34:45+00:00: Recorded command exit 0; command argv SHA-256
  6f51030fcf3d8503d756059362fedf4ee980de09d8ad5ef62bd0b2948c0e5c2e.

- 2026-09-17T21:35:10+00:00: Recorded command exit 0; command argv SHA-256
  d9cb9225467d2352b997b2d36975ca3ac6aff5ab46113190af547a0a2a0178d1.

- 2026-09-17T21:35:26+00:00: Recorded command exit 1; command argv SHA-256
  a772f749e37282ce900b60b5c7c9909360b075c1dd03702a6f39cb7a7fb5d6c3.

- 2026-09-17T21:35:46+00:00: Recorded command exit 0; command argv SHA-256
  379b0aaa17109cd9bd7d425c10655c6549ec8983aab554e34bf218cc90d0a7c1.

- 2026-09-17T21:36:10+00:00: Recovered the 21:35:26 exit-1: the initial cargo invocation passed two
  test filters, but cargo test accepts one TESTNAME and rejected the second as an unexpected
  argument. Correct rerun used the single prefix filter native_supervisor_, and passed 3/3:
  authenticated negative matrix, fault matrix, and real cassette HTTP forwarding. No product gate
  failure.

- 2026-09-17T21:36:34+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-17T21:36:52+00:00: Recorded command exit 0; command argv SHA-256
  10772469dd0ddaf5069a4685da5064075f92454b37971ddc36dadc60a7e22e22.

- 2026-09-17T21:37:10+00:00: Recorded command exit 0; command argv SHA-256
  97ee782321facf1df64b14b3500c62b04b8b48c9904b8abb83044328a904f4b2.

- 2026-09-17T21:37:37+00:00: Recorded command exit 0; command argv SHA-256
  e0e814b48e1909b50ccabd4bb0699237298e6f32cf543810dd57274837794bd9.

- 2026-09-17T21:37:52+00:00: Recorded command exit 0; command argv SHA-256
  9ceeabdfd43099b6aecf1259deea68d9d6514939a9b2b2cf5cf11f2969189b6f.

- 2026-09-17T21:38:18+00:00: Implementation candidate 910af9a: fault matrix now uses ReplayRelay
  rather than an unauthenticated raw UnixListener. Focused 3/3, full asb-runtime tests, fmt and
  clippy pass. No asb-tui or handoffctl changes.

- 2026-09-17T21:38:28+00:00: Recorded command exit 0; command argv SHA-256
  19512d543cbca16558243694b400506ff05b53a567fdc394e8f00a631ebcc519.

- 2026-09-17T21:38:51+00:00: Recorded command exit 0; command argv SHA-256
  ef85fb183c77c7e3b1e0160721ea3cfb7744ba74dfae7b503d20709f6c42d3ee.

- 2026-09-17T21:39:48+00:00: Recorded command exit 0; command argv SHA-256
  21bb067315f65c46cd41da23bbb54aaab64ee2308e46515053bbe240e08914a0.

- 2026-09-17T21:40:23+00:00: Recorded command exit 127; command argv SHA-256
  5cdaf45d72ef36a99b39aaa63b92c7a02c7964d16cc57fd77ec472b41780879a.

- 2026-09-17T21:41:01+00:00: Recorded command exit 0; command argv SHA-256
  2222b35d93cfb76ad4c18c76f1d43461b6f70e1b42958891d5abfa84b17eee3c.

- 2026-09-17T21:41:28+00:00: Recorded command exit 0; command argv SHA-256
  d2d4b48386618890ba2aebf7e26cdfcd28b02930dd6ec7bd12524a826acd6501.

- 2026-09-17T21:41:51+00:00: Recorded command exit 0; command argv SHA-256
  3ec9aeb34fd0df436d625673333a87d330c2a13ca70fff36c4c7a2bd2406e4da.

- 2026-09-17T21:42:07+00:00: Recorded command exit 0; command argv SHA-256
  345de5b2da25e9b37d7563eb7df85bd1a31e8c9322cf708237be1d5a076b3001.

- 2026-09-17T21:42:24+00:00: Heartbeat by codex-ar1306-auth-listener-20260917.

- 2026-09-17T21:42:37+00:00: Published PR #222 after clean exact-head review; signed/DCO candidate
  and all local workspace gates passed. Exact-head hosted checks now running.

- 2026-09-17T21:42:49+00:00: Recorded command exit 8; command argv SHA-256
  70f9830c04f328234bb27442bd2464edd9e1aa80f655ba60d4c71b02409306eb.

- 2026-09-17T21:43:39+00:00: Recorded command exit 8; command argv SHA-256
  70f9830c04f328234bb27442bd2464edd9e1aa80f655ba60d4c71b02409306eb.

- 2026-09-17T21:43:54+00:00: Recorded command exit 8; command argv SHA-256
  70f9830c04f328234bb27442bd2464edd9e1aa80f655ba60d4c71b02409306eb.

- 2026-09-17T21:44:05+00:00: Exact-head CI monitored: 6 checks passed, 6 remain pending, no
  failures. PR is clean and unchanged at signed candidate head.

- 2026-09-17T21:44:15+00:00: Recorded command exit 0; command argv SHA-256
  3e4db653e5225bc40a001949e7ffcf89be0311192c38d74ed08e0edf578ddc6f.

- 2026-09-17T21:49:46+00:00: Recorded command exit 0; command argv SHA-256
  70f9830c04f328234bb27442bd2464edd9e1aa80f655ba60d4c71b02409306eb.

- 2026-09-17T21:50:07+00:00: Monitored PR #222 exact-head checks to terminal: all 12 passed,
  including emulated-aarch64. No reviewer approval yet; merge remains blocked pending independent
  review.

- 2026-09-17T21:54:32+00:00: Independent acceptance review: BLOCK. The one-file diff removes raw
  UnixListener, but the fault matrix still does not exercise a service/listener positive path;
  existing separate positive test does not bind matrix cases. Provider/descendant egress cases only
  assert nonzero exit, so unrelated failure could satisfy them. All 12 hosted checks are green, but
  this is a substantive acceptance gap; do not merge.

- 2026-09-17T21:55:58+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-17T21:56:48+00:00: Heartbeat by codex-ar1306-auth-listener-20260917.

- 2026-09-17T21:56:54+00:00: Recorded command exit 1; command argv SHA-256
  413d8cfd8985157151fc7fe5325e3a83caa44052436e65b6a51ca5cecf1bec69.

- 2026-09-17T21:57:20+00:00: Recorded exact repair-tool failures: apply_patch invocation via
  handoffctl had no stdin (exit 2); Python subprocess wrapper had syntax error from escaped newlines
  (exit 1). Working tree remains at signed 910af9a; no source mutation occurred.

- 2026-09-17T21:57:35+00:00: Recorded command exit 0; command argv SHA-256
  7ffaca487c8c23bde2f0805b3e20381b5d056946fefa174c76d596424982dc27.

- 2026-09-17T21:58:05+00:00: Recorded command exit 0; command argv SHA-256
  08a7a3e36743fed63d32305d5ff41c121406a2f7acb002ea97634373b46b442c.

- 2026-09-17T21:58:33+00:00: Recorded command exit 0; command argv SHA-256
  58dbe59a808992086bab07b3b2cf79c6db23ba4d00aadbc811addab1176a458b.

- 2026-09-17T21:58:48+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T21:58:58+00:00: Recorded command exit 0; command argv SHA-256
  264fcedabcf0d93cdabd2200bdda093ee9401500fb70f47a7ef269009f979713.

- 2026-09-17T21:59:20+00:00: Recorded command exit 0; command argv SHA-256
  2d59387dc86f926c7f5f779a537514d92accf52f6e22c573ffbec0cfbb8a213b.

- 2026-09-17T21:59:43+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T21:59:56+00:00: Recorded command exit 0; command argv SHA-256
  264fcedabcf0d93cdabd2200bdda093ee9401500fb70f47a7ef269009f979713.

- 2026-09-17T22:00:25+00:00: Recorded command exit 0; command argv SHA-256
  98efca768b52d536e88927e34a74e1680abe536b6074d4427a39eecf843117b4.

- 2026-09-17T22:00:37+00:00: Heartbeat by codex-ar1306-auth-listener-20260917.

- 2026-09-17T22:00:40+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T22:00:59+00:00: Recorded command exit 101; command argv SHA-256
  379b0aaa17109cd9bd7d425c10655c6549ec8983aab554e34bf218cc90d0a7c1.

- 2026-09-17T22:02:05+00:00: Recorded command exit 0; command argv SHA-256
  ed4d9a6d1ae94745336418dd89e3c6a61a8dc3d5a67df07cae85a9bbe058e96f.

- 2026-09-17T22:02:17+00:00: Recorded command exit 0; command argv SHA-256
  ada345b6e35c79db802dc47b92799ac83818d106c63a6d3367a9a8fec05a44ca.

- 2026-09-17T22:02:27+00:00: Heartbeat by codex-ar1306-auth-listener-20260917.

- 2026-09-17T22:02:32+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T22:02:42+00:00: Recorded command exit 0; command argv SHA-256
  264fcedabcf0d93cdabd2200bdda093ee9401500fb70f47a7ef269009f979713.

- 2026-09-17T22:03:08+00:00: Repair progress: initial inserted call was accidentally added to every
  native-test fallback branch, causing exit 101 in the full native prefix run; inspected with rg,
  removed all unintended insertions, retained the call only inside the fault-matrix test. Focused
  fault-matrix test then passed 1/1. Diff check clean.

- 2026-09-17T22:03:18+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-17T22:03:36+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-17T22:04:16+00:00: Recorded command exit 0; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-17T22:04:38+00:00: Recorded command exit 0; command argv SHA-256
  e0e814b48e1909b50ccabd4bb0699237298e6f32cf543810dd57274837794bd9.

- 2026-09-17T22:05:00+00:00: Recorded command exit 0; command argv SHA-256
  b32d7f6d27223df1388736c47cfbf3be6867d979652e18c16b75a17facee42f1.

- 2026-09-17T22:05:19+00:00: Recorded command exit 0; command argv SHA-256
  518a4780082fdca5a8bec45d401a548a8ac7fb8bb46f5c129a80fea618cfd017.

- 2026-09-17T22:05:51+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-17T22:06:04+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-17T22:06:45+00:00: Recorded final repair gates: focused fault matrix 1/1 and full
  workspace test pass; fmt/clippy/docs pass. Release build command reached coordinator lock timeout,
  not a product/build failure; concurrent AR-1293 handoff remains active.

- 2026-09-17T22:06:51+00:00: Recorded command exit 0; command argv SHA-256
  b49a90ee600c1023cee9ee9f9e8a4f9a06c53eef8c48d3932d88e482126c7c01.

- 2026-09-17T22:07:14+00:00: Retry after coordinator lock cleared: cargo build --locked --workspace
  --release passed. All local applicable gates are now terminal green; candidate remains clean and
  exact pushed head 1ab79c1.

- 2026-09-17T22:07:24+00:00: Recorded command exit 0; command argv SHA-256
  2ecfdcc7e27414489284329df38d69ab14433a1d3d6b3c64d2c96238dc75e7bd.

- 2026-09-17T22:08:11+00:00: Recorded command exit 8; command argv SHA-256
  70f9830c04f328234bb27442bd2464edd9e1aa80f655ba60d4c71b02409306eb.

- 2026-09-17T22:08:30+00:00: Recorded command exit 8; command argv SHA-256
  70f9830c04f328234bb27442bd2464edd9e1aa80f655ba60d4c71b02409306eb.

- 2026-09-17T22:08:49+00:00: Refreshed PR #222 after repair: exact head 1ab79c1; AWQ, fault, formal
  Kani/Loom/TLC, headers, platform, fuzz and mutation checks pass. Policy/supply, Rust, and
  emulated-aarch64 are still running. Merge remains blocked.

- 2026-09-17T22:12:08+00:00: Recorded command exit 0; command argv SHA-256
  4c345b083c3cb179787e2bc6cf7774a49180922905ae155836ba464d831f3d20.

- 2026-09-17T22:12:19+00:00: Recorded command exit 1; command argv SHA-256
  4a970b1310bdc5493582ff36d9aca0be5db403612d27aa509e526b7ada008792.

- 2026-09-17T22:12:39+00:00: Recorded command exit 0; command argv SHA-256
  dbbd6d8e16e831c8a2faf199560bec71a787e7a2a612ae1ac4cc896fe627b9a7.

- 2026-09-17T22:13:02+00:00: Recorded command exit 0; command argv SHA-256
  a779418d60419a8537dad511a0dae57737e6b9e5a365369028c319f8381dfb40.

- 2026-09-17T22:13:14+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T22:13:28+00:00: Recorded command exit 0; command argv SHA-256
  83f80a67b973715dbb71d7da066f6fd427c879f3dbb903051a53203e07f10336.

- 2026-09-17T22:13:54+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T22:14:04+00:00: Recorded command exit 101; command argv SHA-256
  379b0aaa17109cd9bd7d425c10655c6549ec8983aab554e34bf218cc90d0a7c1.

- 2026-09-17T22:14:39+00:00: Recorded command exit 0; command argv SHA-256
  1d1b84ff4348c506aa5e3fa945f0fe275510b866ce4a87ea318a354e34d52cbe.

- 2026-09-17T22:15:11+00:00: Recorded command exit 0; command argv SHA-256
  f08225d4b5f051d285659a15e52b0947e96596941db8baa468ddf0c5a5c734ff.

- 2026-09-17T22:15:21+00:00: Recorded command exit 0; command argv SHA-256
  ca0a37348fb024b3b6ee58b14c6dad7747d7073622c39d3abaa488bb0f4d4af4.

- 2026-09-17T22:15:47+00:00: Recorded command exit 0; command argv SHA-256
  a04d2faa0a82b28ac636feb473d02e13295032ab064fe3ca3ee28572f4633917.

- 2026-09-17T22:15:57+00:00: Recorded command exit 0; command argv SHA-256
  874a4263380f1ca541aff474c0337fa537439e5ffd4d42c085d93c85f1f1fa72.

- 2026-09-17T22:16:34+00:00: Recorded command exit 0; command argv SHA-256
  1d1b84ff4348c506aa5e3fa945f0fe275510b866ce4a87ea318a354e34d52cbe.

- 2026-09-17T22:16:54+00:00: Independent review follow-up: generic tests intentionally skip
  native-only fixtures, but approved native-platform workflow binds ASB_REQUIRE_NATIVE_SANDBOX=1 in
  its sandbox command, executing the full matrix and failing closed if capability is unavailable.
  Temporary local assertion was removed to avoid breaking non-native hosted jobs. Multiple handoff
  commands hit transient coordinator LOCK_TIMEOUT; no product diff remains.

- 2026-09-17T22:17:08+00:00: Recorded command exit 0; command argv SHA-256
  1d1b84ff4348c506aa5e3fa945f0fe275510b866ce4a87ea318a354e34d52cbe.

- 2026-09-17T22:19:59+00:00: Heartbeat by codex-ar1306-auth-listener-20260917.

- 2026-09-17T22:20:19+00:00: Recorded command exit 0; command argv SHA-256
  f26a78103e962e78c4636d718872d26497fb5a4c2f009ff3c9c3ab4ac25ce073.

- 2026-09-17T22:20:31+00:00: Recorded command exit 0; command argv SHA-256
  217799b7ce32b340be4b92f7f1cc287e2cd93428f0e43504749a1a058a12c44a.

- 2026-09-17T22:20:47+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T22:21:03+00:00: Recorded command exit 0; command argv SHA-256
  11f32d1cddb3fba391f91a3ec36198a60aa1ee3efee888529d62809c5fd236d9.

- 2026-09-17T22:21:19+00:00: Recorded command exit 0; command argv SHA-256
  1d1b84ff4348c506aa5e3fa945f0fe275510b866ce4a87ea318a354e34d52cbe.

- 2026-09-17T22:21:29+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-17T22:21:38+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-17T22:22:17+00:00: Recorded command exit 0; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-17T22:22:40+00:00: Recorded command exit 0; command argv SHA-256
  17bde1235c1e28283e717a7182c469f7a9737a26477e9b47569ab058e19eab22.

- 2026-09-17T22:23:00+00:00: Recorded command exit 0; command argv SHA-256
  518a4780082fdca5a8bec45d401a548a8ac7fb8bb46f5c129a80fea618cfd017.

- 2026-09-17T22:23:26+00:00: Implemented reviewed response-parity repair. Qualified native
  supervisor tests passed 3/3 under ASB_REQUIRE_NATIVE_SANDBOX=1; full locked workspace tests, fmt
  and clippy passed. Signed/DCO commit a6c0a03 pushed to PR #222. Merge remains blocked pending
  CI/review.

- 2026-09-17T22:24:34+00:00: Heartbeat by codex-ar1306-auth-listener-20260917.

- 2026-09-17T22:27:28+00:00: Heartbeat by codex-ar1306-auth-listener-20260917.

- 2026-09-17T22:31:06+00:00: Heartbeat by codex-ar1306-auth-listener-20260917.

- 2026-09-17T22:33:57+00:00: Recorded command exit 255; command argv SHA-256
  8e480616f29b12d3c93efccc85ecd913855efd304739a85360a9eca9d55ace35.

- 2026-09-17T22:34:15+00:00: Heartbeat by codex-ar1306-auth-listener-20260917.

- 2026-09-17T22:34:28+00:00: Recorded command exit 0; command argv SHA-256
  80fb552622829785aebd6fbc1488651efd3012cef1eea45aa7d42e52f99e2943.

- 2026-09-17T22:35:05+00:00: Recorded command exit 0; command argv SHA-256
  52ccc7b4947d71fdfb377353fdecfb772424c13801465395cb7e2c8eeeb0bf4e.

- 2026-09-17T22:35:15+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-09-17T22:35:30+00:00: Recorded command exit 0; command argv SHA-256
  0b64b502877b692e6ec06c09c401731abae2491470ebdf27c39ddce877313941.

- 2026-09-17T22:35:40+00:00: Recorded command exit 0; command argv SHA-256
  379b0aaa17109cd9bd7d425c10655c6549ec8983aab554e34bf218cc90d0a7c1.

- 2026-09-17T22:35:48+00:00: Recorded command exit 0; command argv SHA-256
  f306fe83743deefb79f10799d61620e40bf7487b2915531cfb01a2fc7c9453a0.

- 2026-09-17T22:36:06+00:00: Recorded command exit 0; command argv SHA-256
  518a4780082fdca5a8bec45d401a548a8ac7fb8bb46f5c129a80fea618cfd017.

- 2026-09-17T22:36:32+00:00: Recorded hosted platform prerequisite failure: ubuntu-24.04 apt could
  not locate pinned bubblewrap 0.9.0-1ubuntu0.1 (apt exit 100). Repaired workflow with reviewed
  0.9.0 allowlist/candidate selection and post-install exact version check; no network/host
  isolation changes. Signed commit 5425bc3 pushed to PR #222.

- 2026-09-17T22:36:47+00:00: Recorded command exit 0; command argv SHA-256
  82164eb7b9c75c42df4a72e4a85c068fc91bda8dbb22d5cf39f7bd21bbd034e6.

- 2026-09-17T22:37:06+00:00: Heartbeat by codex-ar1306-auth-listener-20260917.

- 2026-09-17T22:38:20+00:00: Heartbeat by codex-ar1306-auth-listener-20260917.
