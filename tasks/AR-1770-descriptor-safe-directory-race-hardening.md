---
{
  "branch": "feature/ar-1770-descriptor-safe-directory-race-hardening",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-10T00:10:31+00:00",
  "depends_on": [
    "AR-1767"
  ],
  "id": "AR-1770",
  "next_action": "Exact-SHA rerun attempts are active: aarch64 37990474021 attempt 7 and formal 37990474025 attempt 6, both at merge dc67390494805693aef21d917319253b2e705da7. Await terminal result; create receipt and release only if both pass.",
  "observed_branch": "feature/ar-1770-descriptor-safe-directory-race-hardening",
  "observed_dirty": 0,
  "observed_head": "6278fcd6720f39de456a791f0c73e6327ff6e25d",
  "owner": "codex-ar1770-descriptor-safe-races",
  "plan": "../plans/AR-1770-descriptor-safe-directory-race-hardening.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "property-or-fuzz",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1770.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1770.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Close remaining directory and atomic-publication replacement races and complete the AR-1767 acceptance matrix.",
  "task_revision": 274,
  "title": "Descriptor-safe directory race hardening and acceptance matrix",
  "updated_at": "2026-10-09T22:16:37+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1770-descriptor-safe-directory-race-hardening"
}
---

Harden the AR-1767 directory preparation and output publication paths against
replacement between validation and effect. Use descriptor-relative or an
equivalent fail-closed design for every command-owned directory ancestor and
for `write_atomic_private` and `publish_recording_campaign`; never follow an
attacker-replaced symlink or publish through an unvalidated ancestor. Preserve
private modes, fsync/atomicity, transaction-owned cleanup, and existing JSON
and diagnostic contracts.

Complete the missing acceptance evidence: deterministic replacement-race and
concurrent-reuse tests; dry-run no-mutation tests; permission/read-only and
rollback tests; path-specific error and human-notice tests for setup/config,
project, tool, plan, run/sweep, report, record/campaign, easy lifecycle, and
TUI routes; and machine-stream privacy checks. Record any platform-specific
implementation boundary explicitly and keep the product offline after install.

- 2026-10-09T19:22:21+00:00: AR-1767 is released done with exact merge and all post-merge gates;
  promote the descriptor-safe race and acceptance-matrix successor.

- 2026-10-09T19:22:30+00:00: Claimed by codex-ar1770-descriptor-safe-races.

- 2026-10-09T19:23:16+00:00: Heartbeat by codex-ar1770-descriptor-safe-races.

- 2026-10-09T19:23:20+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-10-09T19:23:42+00:00: Recorded command exit 0; command argv SHA-256
  b62f4e4a9a8bbb2a2c7126386b0d66111eba17387cebaf68a7f7c625260419c0.

- 2026-10-09T19:24:04+00:00: Recorded command exit 0; command argv SHA-256
  9c1fb2581d699b02c7edf33716968a70f93290ab512054437721c96ca4fa8093.

- 2026-10-09T19:24:06+00:00: Recorded command exit 0; command argv SHA-256
  9c1fb2581d699b02c7edf33716968a70f93290ab512054437721c96ca4fa8093.

- 2026-10-09T19:26:23+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-09T19:26:48+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T19:27:23+00:00: Recorded command exit 101; command argv SHA-256
  73d005d4c4983870f0c5405c6c97dffbf521d57825b14d75dae888988fbdcd03.

- 2026-10-09T19:28:13+00:00: Recorded command exit 101; command argv SHA-256
  73d005d4c4983870f0c5405c6c97dffbf521d57825b14d75dae888988fbdcd03.

- 2026-10-09T19:28:43+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T19:29:06+00:00: Recorded command exit 0; command argv SHA-256
  73d005d4c4983870f0c5405c6c97dffbf521d57825b14d75dae888988fbdcd03.

- 2026-10-09T19:30:01+00:00: Recorded command exit 101; command argv SHA-256
  9c9c28ee85d6728d4e0aadfacd9c56ce020d9e24199e795a870dcd65d1732158.

- 2026-10-09T19:30:26+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T19:30:51+00:00: Recorded command exit 0; command argv SHA-256
  9c9c28ee85d6728d4e0aadfacd9c56ce020d9e24199e795a870dcd65d1732158.

- 2026-10-09T19:31:12+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T19:31:34+00:00: Recorded command exit 1; command argv SHA-256
  dc3363f7c4f58aaf68ba66c9d95e87e4378322324b1d06f02ef51515642b019e.

- 2026-10-09T19:32:00+00:00: Recorded command exit 101; command argv SHA-256
  c64f85e92f4319f5a3e74e135910802ef4e5808bce669c08396bff4a9f271605.

- 2026-10-09T19:32:31+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T19:32:56+00:00: Recorded command exit 101; command argv SHA-256
  d7efc4b5867af3e11acc4adf06c7ef77432dc45f5f69d8d5b2a810794db57cee.

- 2026-10-09T19:33:20+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T19:33:45+00:00: Recorded command exit 0; command argv SHA-256
  d7efc4b5867af3e11acc4adf06c7ef77432dc45f5f69d8d5b2a810794db57cee.

- 2026-10-09T19:34:09+00:00: Heartbeat by codex-ar1770-descriptor-safe-races.

- 2026-10-09T19:34:17+00:00: Recorded command exit 101; command argv SHA-256
  22fc19d872be75a975891ff0abd53f1c305974a409b50c49c5df5d842d033e81.

- 2026-10-09T19:34:52+00:00: Recorded command exit 0; command argv SHA-256
  ef19043205064ea87bec66574bfe246191c9311bc8c404cd8e347d08fbdc44f0.

- 2026-10-09T19:35:30+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T19:35:55+00:00: Recorded command exit 0; command argv SHA-256
  f1e3e8a65e3ee6ff08b55f21651597413fa3014f1fa03f5ba071c63f9074ae66.

- 2026-10-09T19:38:09+00:00: Implementation now uses descriptor-relative rustix
  openat/mkdirat/renameat/unlinkat with O_NOFOLLOW and anchored directory FDs; staged output
  publication and campaign rollback retain parent descriptors. Evidence: cargo check --locked -p
  asb-cli passed; 305 asb-cli unit tests passed; record_campaign focused tests passed;
  directory/publication tests passed; workflow_transcript initially exposed provenance digest drift,
  fixture was updated to the exact new lib.rs digest and workflow_transcript now passes. Next gate
  is lint/docs/full applicable quality.

- 2026-10-09T19:39:15+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T19:39:37+00:00: Recorded command exit 0; command argv SHA-256
  73d005d4c4983870f0c5405c6c97dffbf521d57825b14d75dae888988fbdcd03.

- 2026-10-09T19:40:02+00:00: Recorded command exit 1; command argv SHA-256
  934f167ec5addd91351d48ea8dc774ebfe0bfcc3922ea3dd93b79c46a393bd39.

- 2026-10-09T19:40:36+00:00: Recorded command exit 101; command argv SHA-256
  22fc19d872be75a975891ff0abd53f1c305974a409b50c49c5df5d842d033e81.

- 2026-10-09T19:41:05+00:00: Recorded command exit 0; command argv SHA-256
  ef19043205064ea87bec66574bfe246191c9311bc8c404cd8e347d08fbdc44f0.

- 2026-10-09T19:41:29+00:00: After descriptor-safe migration of easy artifacts, project config, plan
  output, and tool installation, full asb-cli unit/integration suite passed except the expected
  provenance digest fixture drift; updated the exact lib.rs digest to
  55263b04cf08a8977a2fd6929697d428ff69314ab3fe9a1ebcaae20d8782d39f. Workflow transcript now passes
  3/3.

- 2026-10-09T19:41:36+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-10-09T19:41:56+00:00: Recorded command exit 0; command argv SHA-256
  565b04b503d6d7bfabfd2845aea0b91208d33abbc73adaaf208c27f9198d6768.

- 2026-10-09T19:42:17+00:00: Recorded command exit 0; command argv SHA-256
  6bb343cc4fa4a52211d35bf4e374f5e8b34ff19b4de08411c9fdbbde962b79ee.

- 2026-10-09T19:42:53+00:00: Recorded command exit 101; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-10-09T19:43:17+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T19:43:42+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-10-09T19:44:13+00:00: Recorded command exit 0; command argv SHA-256
  ef19043205064ea87bec66574bfe246191c9311bc8c404cd8e347d08fbdc44f0.

- 2026-10-09T19:44:35+00:00: Recorded command exit 0; command argv SHA-256
  565b04b503d6d7bfabfd2845aea0b91208d33abbc73adaaf208c27f9198d6768.

- 2026-10-09T19:44:56+00:00: Recorded command exit 0; command argv SHA-256
  4d0b3e11f1752454fffde0ab5a54a207dae56910561bae034638075afc131390.

- 2026-10-09T19:45:24+00:00: Candidate commits: dfa1f435c2aa3614fc60fe1df759c6c3f7358376
  (descriptor-safe implementation, signed DCO) and f5e5f0d91f6c3a6e6a7e6b6fb6df10e730bad0e1 (clippy
  repair, signed DCO). Gates: cargo check -p asb-cli passed; cargo clippy --locked --workspace
  --all-targets -D warnings passed after f5e5f0d; all 305 asb-cli unit/integration suites passed
  before the final clippy-only repair; workflow_transcript 3/3 passed at the current exact source
  digest; diff check clean. The earlier combined cargo filter was an invalid invocation (recorded
  failure), not a product failure.

- 2026-10-09T19:45:35+00:00: Recorded command exit 0; command argv SHA-256
  ff1f2116dd8b8d6abb0c23dd97279588e2251ffcbf0a5de525218cb70e9260e1.

- 2026-10-09T19:46:02+00:00: Recorded command exit 0; command argv SHA-256
  b71b5772c61e10cd4dbf8bf36002097887e27e44d5ab3eb44670b410524b4489.

- 2026-10-09T19:46:30+00:00: Published PR #540:
  https://github.com/martin-beck/agent-systems-benchmark/pull/540. Exact base
  31f52d75f006accc3ac5c372d6d93b6c85ad42bc, head f5e5f0d5a50bd768a7cf80ccf4c84ceb78f3a96e, tree
  8d121f72dde5ddf75b95119c049a61e2e652bba0. Candidate commits
  dfa1f435c2aa3614fc60fe1df759c6c3f7358376 and f5e5f0d5a50bd768a7cf80ccf4c84ceb78f3a96e are
  SSH-signed with matching DCO. Local check, clippy, 305-test asb-cli suite, and 3/3 workflow
  transcript pass; PR body records exact evidence. Independent exact-head review and hosted CI are
  pending.

- 2026-10-09T19:46:36+00:00: Recorded command exit 0; command argv SHA-256
  2f6376756df7813df70388dd319890d417dc9c2c9a811071275872ff7a481f5d.

- 2026-10-09T19:47:24+00:00: Recorded command exit 0; command argv SHA-256
  f0a5e7c3cb0af0df5a8cfe1225796a40c3dabbf8987a21b0c7039f331f8d0f8e.

- 2026-10-09T19:48:19+00:00: Heartbeat by codex-ar1770-descriptor-safe-races.

- 2026-10-09T19:49:36+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T19:50:00+00:00: Recorded command exit 101; command argv SHA-256
  a4b9f2935cd727ed633d22112d7c9815901d3ae417adf537994d4840ac76b3ba.

- 2026-10-09T19:50:24+00:00: Recorded command exit 101; command argv SHA-256
  f57860bf7c63583756bdc88ddba9e63368893ab3ae1596e74515f6fe4dc32b2d.

- 2026-10-09T19:50:50+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T19:51:15+00:00: Recorded command exit 101; command argv SHA-256
  f57860bf7c63583756bdc88ddba9e63368893ab3ae1596e74515f6fe4dc32b2d.

- 2026-10-09T19:51:40+00:00: Recorded command exit 101; command argv SHA-256
  f57860bf7c63583756bdc88ddba9e63368893ab3ae1596e74515f6fe4dc32b2d.

- 2026-10-09T19:52:05+00:00: Recorded command exit 101; command argv SHA-256
  f57860bf7c63583756bdc88ddba9e63368893ab3ae1596e74515f6fe4dc32b2d.

- 2026-10-09T19:52:32+00:00: Recorded command exit 101; command argv SHA-256
  f57860bf7c63583756bdc88ddba9e63368893ab3ae1596e74515f6fe4dc32b2d.

- 2026-10-09T19:52:59+00:00: Recorded command exit 0; command argv SHA-256
  a4b9f2935cd727ed633d22112d7c9815901d3ae417adf537994d4840ac76b3ba.

- 2026-10-09T19:53:27+00:00: Recorded command exit 101; command argv SHA-256
  b2d5f1f7b79c15e9ddfe811d1077b753675005d630b7d6b57381bebf612b3440.

- 2026-10-09T19:53:53+00:00: Recorded command exit 101; command argv SHA-256
  b2d5f1f7b79c15e9ddfe811d1077b753675005d630b7d6b57381bebf612b3440.

- 2026-10-09T19:54:20+00:00: Recorded command exit 101; command argv SHA-256
  b2d5f1f7b79c15e9ddfe811d1077b753675005d630b7d6b57381bebf612b3440.

- 2026-10-09T19:54:59+00:00: Recorded command exit 0; command argv SHA-256
  b2d5f1f7b79c15e9ddfe811d1077b753675005d630b7d6b57381bebf612b3440.

- 2026-10-09T19:55:34+00:00: Recorded command exit 101; command argv SHA-256
  22fc19d872be75a975891ff0abd53f1c305974a409b50c49c5df5d842d033e81.

- 2026-10-09T19:55:58+00:00: Recorded command exit 0; command argv SHA-256
  359d399dbe516e4a6c82de7a61b736b7d34fb7b6e8ffe552245ab234d396de60.

- 2026-10-09T19:56:27+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T19:56:55+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-10-09T19:57:27+00:00: Recorded command exit 0; command argv SHA-256
  22fc19d872be75a975891ff0abd53f1c305974a409b50c49c5df5d842d033e81.

- 2026-10-09T19:57:53+00:00: Recorded command exit 0; command argv SHA-256
  ef19043205064ea87bec66574bfe246191c9311bc8c404cd8e347d08fbdc44f0.

- 2026-10-09T19:58:57+00:00: Recorded command exit 0; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-10-09T19:59:23+00:00: Heartbeat by codex-ar1770-descriptor-safe-races.

- 2026-10-09T19:59:32+00:00: Recorded command exit 0; command argv SHA-256
  7a0e67dc3e878fb24cce372a44169db0bde15d77f6a828dc262f5b7efb820860.

- 2026-10-09T20:00:00+00:00: Recorded command exit 0; command argv SHA-256
  552166c9ac60990d7da4c4377891dd9f24d1fe3078878b4988c7cd929836c7ae.

- 2026-10-09T20:00:31+00:00: Recorded command exit 0; command argv SHA-256
  309637164a3518a96cb52b8afa977f0809dc26141ba775d82424b475beac799a.

- 2026-10-09T20:00:58+00:00: P1 review repair complete and pushed as signed DCO commit 1e9629b6.
  Descriptor-relative no-follow preparation now covers attempt-private directories, prompt creation,
  built-in and literature fixture roots, nested initial files, and reset setup. Gates: workspace
  test command completed with all reported suites passing; second full CLI run 305/305 plus
  integrations, workload 39+4, clippy, check, workflow transcript 3/3. PR #540 is blocked pending
  fresh independent review and exact-head CI.

- 2026-10-09T20:01:54+00:00: Recorded command exit 0; command argv SHA-256
  5295ed44100d9f156af80a476d84f16767a0453a84c950720e3720da310a8789.

- 2026-10-09T20:02:20+00:00: Recorded command exit 0; command argv SHA-256
  d1928a0428ed96490242781988ee150464f7c85a6ce0890b08d016fac47cdc02.

- 2026-10-09T20:02:45+00:00: Recorded command exit 0; command argv SHA-256
  258a7d9a220dbeec1ddce80d38091eb2df0296fd7fd209c14b109dbc7bf29d4e.

- 2026-10-09T20:03:12+00:00: Recorded command exit 0; command argv SHA-256
  ddbb5502f0d424795dabf150da7be015ab94ddbaabe138dce1d4d5c038935f17.

- 2026-10-09T20:03:38+00:00: CI header gate repaired with signed DCO commit 44667bc adding the exact
  required source header to the new descriptor-safe helper. Product branch is attached, clean, and
  pushed. Prior local gates remain: workspace suites reported passing, CLI 305/305 plus
  integrations, workload 39+4, clippy, check, workflow transcript 3/3. PR #540 remains blocked
  pending fresh independent review and exact-head CI.

- 2026-10-09T20:03:45+00:00: Recorded command exit 0; command argv SHA-256
  ece73a2088f3b722bcdc9b3162b2ef9d0d11f671db2e6586d36c829fe1b392ec.

- 2026-10-09T20:05:09+00:00: Heartbeat by codex-ar1770-descriptor-safe-races.

- 2026-10-09T20:05:16+00:00: Recorded command exit 0; command argv SHA-256
  5295ed44100d9f156af80a476d84f16767a0453a84c950720e3720da310a8789.

- 2026-10-09T20:06:12+00:00: Recorded command exit 1; command argv SHA-256
  029e3a866d46267ac9d491a0e344965dc5a925c630beac6a3a75b3bdde26b0ee.

- 2026-10-09T20:06:37+00:00: Recorded command exit 0; command argv SHA-256
  929c3c62caf71b33c87bee4f404aff8cc18d9a4b2f3571feb1a87828dc87b9d9.

- 2026-10-09T20:07:04+00:00: Recorded command exit 101; command argv SHA-256
  896a7ce6bd6967d4040a5d23d876c009a73eff28eb1422286034add3d9ebd1dc.

- 2026-10-09T20:07:35+00:00: Recorded command exit 0; command argv SHA-256
  896a7ce6bd6967d4040a5d23d876c009a73eff28eb1422286034add3d9ebd1dc.

- 2026-10-09T20:08:06+00:00: Recorded command exit 0; command argv SHA-256
  929c3c62caf71b33c87bee4f404aff8cc18d9a4b2f3571feb1a87828dc87b9d9.

- 2026-10-09T20:08:31+00:00: Recorded command exit 0; command argv SHA-256
  8e7743f38aaae5a2182a6795026b710b42cf091824baa8b6011e09e4225825e4.

- 2026-10-09T20:08:55+00:00: Recorded command exit 0; command argv SHA-256
  54c74c93c73307f948b2d9ee72b1eecb9fd888cced2565be3d72f5b215102b1f.

- 2026-10-09T20:09:24+00:00: Recorded command exit 0; command argv SHA-256
  36953103c91b07879f8be1417b9426308d1456d591718d27e53ad411ac3ec4a4.

- 2026-10-09T20:09:50+00:00: Recorded command exit 0; command argv SHA-256
  24e6d5497393b0ee210f591b758575cf69cafeedbece7685f4b7e724fa592056.

- 2026-10-09T20:10:16+00:00: Recorded command exit 0; command argv SHA-256
  49569ac76b842bcefbf3af3e7d6dfc88fd655bf5bf8ee90f82efc582d43a9bcc.

- 2026-10-09T20:10:39+00:00: Recorded command exit 0; command argv SHA-256
  24b47f17502ab8fce069704907c25fa4790546879a76e4e2f114754dca3db2eb.

- 2026-10-09T20:11:03+00:00: Recorded command exit 0; command argv SHA-256
  ddbb5502f0d424795dabf150da7be015ab94ddbaabe138dce1d4d5c038935f17.

- 2026-10-09T20:11:28+00:00: Review repair pushed as signed DCO commit bf522fa. Descriptor setup now
  rolls back newly-created directories on fchmod/open failures and reopens concurrent AlreadyExists
  winners with no-follow validation; a concurrent hostile-path regression test was added. Added
  CLI_ROUTE_ACCEPTANCE_MATRIX.md documenting setup/config, project/tool, plan, run/sweep, report,
  record/campaign, easy, TUI, dry-run, read-only, rollback, and JSON/human stream evidence with
  existing test mappings. Focused safe_fs, route integration, workflow transcript, clippy, header,
  and check gates pass; PR #540 awaits fresh independent review and exact-head CI.

- 2026-10-09T20:11:34+00:00: Recorded command exit 0; command argv SHA-256
  ece73a2088f3b722bcdc9b3162b2ef9d0d11f671db2e6586d36c829fe1b392ec.

- 2026-10-09T20:11:58+00:00: Recorded command exit 1; command argv SHA-256
  6a36b57f52c086ad481e5f433c475b707dbb9dcfe8de737aed0c16543a74c88f.

- 2026-10-09T20:12:34+00:00: Recorded command exit 0; command argv SHA-256
  929c3c62caf71b33c87bee4f404aff8cc18d9a4b2f3571feb1a87828dc87b9d9.

- 2026-10-09T20:13:00+00:00: Recorded command exit 101; command argv SHA-256
  c5b2d44f3107c3e94a25e4c3474395063e2376fc5c369822ffa74b3b9ae4ba92.

- 2026-10-09T20:13:27+00:00: Recorded command exit 0; command argv SHA-256
  c5b2d44f3107c3e94a25e4c3474395063e2376fc5c369822ffa74b3b9ae4ba92.

- 2026-10-09T20:13:53+00:00: Recorded command exit 0; command argv SHA-256
  7a940098069d50979f60c9313e922e11e04880f495207d63ee5f57a178d5abcc.

- 2026-10-09T20:14:19+00:00: Recorded command exit 0; command argv SHA-256
  f45526ce7dcf732dffb560a9a086b6a65864766503ab7df0cb0e635e546553b7.

- 2026-10-09T20:14:48+00:00: Recorded command exit 101; command argv SHA-256
  382245ea3e511b956eb56ec1dae1b90e40bc15d2bf983cf01b0c5080a02d5605.

- 2026-10-09T20:15:30+00:00: Recorded command exit 0; command argv SHA-256
  9dd213801f55b5196bb569ee7e0633e751373c8757398b76769a11d0faeb2460.

- 2026-10-09T20:15:58+00:00: Recorded command exit 0; command argv SHA-256
  30ad26f600430a1991b20e0d8d7f37852237b82e804e250862dfb7b404efb6a9.

- 2026-10-09T20:16:22+00:00: Recorded command exit 0; command argv SHA-256
  884d7ae6f1f145c2095b5fb2d7d5f6ad26a344e929744012425150c5453c1f1d.

- 2026-10-09T20:16:46+00:00: Recorded command exit 0; command argv SHA-256
  5295ed44100d9f156af80a476d84f16767a0453a84c950720e3720da310a8789.

- 2026-10-09T20:17:09+00:00: Recorded command exit 0; command argv SHA-256
  f40ae087386324ad4734256e24c07c1b903513747c399d96320546fc594361bf.

- 2026-10-09T20:17:36+00:00: Recorded command exit 0; command argv SHA-256
  ddbb5502f0d424795dabf150da7be015ab94ddbaabe138dce1d4d5c038935f17.

- 2026-10-09T20:18:01+00:00: Heartbeat by codex-ar1770-descriptor-safe-races.

- 2026-10-09T20:18:08+00:00: Review repair pushed as signed DCO commit c207894. safe_fs now rolls
  back accumulated directories when current descriptor cloning or fchmod fails; prepare_child
  reopens concurrent AlreadyExists winners with no-follow validation; focused tests now cover
  concurrent reuse and file-parent no-mutation. CLI_ROUTE_ACCEPTANCE_MATRIX documents route-specific
  human/JSON, dry-run, read-only, permission-shaped, rollback, and TUI evidence. Exact-head CI Loom
  failure was reproduced locally: formal/Cargo.lock lacked the new rustix dependency introduced by
  this AR; regenerated lock passed the full formal test suite offline (all reported tests green).
  Fresh CI is required.

- 2026-10-09T20:18:14+00:00: Recorded command exit 0; command argv SHA-256
  8f6fbc3e647390707f716e2638d244cc72ffa2132a5112d19131566eb6b65089.

- 2026-10-09T20:19:08+00:00: Recorded command exit 0; command argv SHA-256
  d70d9b1655befe4adb1c757f1717cc4a408db3fe446b3044f43fce7e44c20383.

- 2026-10-09T20:19:42+00:00: Recorded command exit 0; command argv SHA-256
  929c3c62caf71b33c87bee4f404aff8cc18d9a4b2f3571feb1a87828dc87b9d9.

- 2026-10-09T20:20:06+00:00: Recorded command exit 0; command argv SHA-256
  896a7ce6bd6967d4040a5d23d876c009a73eff28eb1422286034add3d9ebd1dc.

- 2026-10-09T20:20:37+00:00: Recorded command exit 0; command argv SHA-256
  929c3c62caf71b33c87bee4f404aff8cc18d9a4b2f3571feb1a87828dc87b9d9.

- 2026-10-09T20:21:02+00:00: Recorded command exit 0; command argv SHA-256
  c5b2d44f3107c3e94a25e4c3474395063e2376fc5c369822ffa74b3b9ae4ba92.

- 2026-10-09T20:21:30+00:00: Recorded command exit 0; command argv SHA-256
  382245ea3e511b956eb56ec1dae1b90e40bc15d2bf983cf01b0c5080a02d5605.

- 2026-10-09T20:21:55+00:00: Recorded command exit 0; command argv SHA-256
  24e6d5497393b0ee210f591b758575cf69cafeedbece7685f4b7e724fa592056.

- 2026-10-09T20:22:26+00:00: Recorded command exit 0; command argv SHA-256
  5c29502c780c3ccbe7ef8d3fcf02e4fa18e940eb701451c23c61b575bf6e0ba9.

- 2026-10-09T20:22:49+00:00: Recorded command exit 0; command argv SHA-256
  65e660803a615e8d376ef798909e07b83080c3db46a5a31ea4489d7d20be85ef.

- 2026-10-09T20:23:12+00:00: Recorded command exit 0; command argv SHA-256
  5295ed44100d9f156af80a476d84f16767a0453a84c950720e3720da310a8789.

- 2026-10-09T20:23:36+00:00: Recorded command exit 0; command argv SHA-256
  04cf3118b76b43945cb9c0399eba62a83ccac57aa529fa34e0605ad394d58805.

- 2026-10-09T20:24:01+00:00: Recorded command exit 0; command argv SHA-256
  ddbb5502f0d424795dabf150da7be015ab94ddbaabe138dce1d4d5c038935f17.

- 2026-10-09T20:24:27+00:00: Nested transaction repair pushed as signed DCO commit 73aae7b.
  write_initial now collects created directory descriptors and rolls them back in reverse order on
  later preparation/write failure; pre-existing directories remain untouched. Added focused nested
  rollback test. Formal lock refresh remains included and the previously failing Loom gate passed
  locally with --locked after the refresh. Prior workload 42 tests, route integration (human 14,
  guide 6, TUI 5, transcript 3), clippy, and check gates pass. PR #540 awaits fresh review and
  exact-head CI.

- 2026-10-09T20:24:33+00:00: Recorded command exit 0; command argv SHA-256
  8f6fbc3e647390707f716e2638d244cc72ffa2132a5112d19131566eb6b65089.

- 2026-10-09T20:25:25+00:00: Recorded command exit 0; command argv SHA-256
  b64c0a0a89c98c7925e2cc730ecf2c5896219f27227c5fc55245757465c0effc.

- 2026-10-09T20:25:48+00:00: Recorded command exit 0; command argv SHA-256
  5295ed44100d9f156af80a476d84f16767a0453a84c950720e3720da310a8789.

- 2026-10-09T20:26:12+00:00: Recorded command exit 0; command argv SHA-256
  e372fc0cd40c98f1afa9b91c6fd2d081d22b8201b00c23518b955e1fe0cbd871.

- 2026-10-09T20:26:36+00:00: Recorded command exit 0; command argv SHA-256
  65a63c45a54d0b885f544ca1d4f554875192d37fc8598166d88f5542d2fba9ca.

- 2026-10-09T20:27:00+00:00: Recorded command exit 0; command argv SHA-256
  595f4ba905b8c05db4b80eef8493cd71af22fc30ef7d059f3b118bf2c6a6dcc9.

- 2026-10-09T20:27:23+00:00: Recorded command exit 0; command argv SHA-256
  5e505b205b031405b8efd0a20fac9684867106cb124b4fad158d0104a762b7f8.

- 2026-10-09T20:28:16+00:00: Recorded command exit 1; command argv SHA-256
  fafbbf756dac80daee41c6b9644e9df553da55e35471092a906c80001fe53085.

- 2026-10-09T20:28:39+00:00: Recorded command exit 0; command argv SHA-256
  96221c33afe9e533d3b135c51b63a0078c4ed4a76feeeb0eb57bbadc976bb2ca.

- 2026-10-09T20:29:05+00:00: Recorded command exit 0; command argv SHA-256
  f24dafa9a9f9477b07be7cf723c09279185f623e38aa98b41ee8bc00d334738d.

- 2026-10-09T20:29:32+00:00: Recorded command exit 0; command argv SHA-256
  bc7c4cb05101e491c31fab90703b658a190bdde85602aeb0e60357374c7d26b6.

- 2026-10-09T20:29:58+00:00: Recorded command exit 0; command argv SHA-256
  e59efea554e1dd613fe7eb1e017277cf1f57ea35d31cd617fcb2675e68f584bf.

- 2026-10-09T20:30:23+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-09T20:30:46+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T20:31:10+00:00: Recorded command exit 101; command argv SHA-256
  b2d5f1f7b79c15e9ddfe811d1077b753675005d630b7d6b57381bebf612b3440.

- 2026-10-09T20:31:13+00:00: Recorded command exit 0; command argv SHA-256
  98a29db3d26fadd902355310e52e00a17d60046a3fb589ce243f828e4f22c17e.

- 2026-10-09T20:31:33+00:00: Recorded command exit 0; command argv SHA-256
  6e540fb46c96de4bae6a73debe8684f9e319a747678b509b5f635f2a3e011da1.

- 2026-10-09T20:32:02+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T20:32:28+00:00: Recorded command exit 0; command argv SHA-256
  b2d5f1f7b79c15e9ddfe811d1077b753675005d630b7d6b57381bebf612b3440.

- 2026-10-09T20:32:49+00:00: Recorded command exit 0; command argv SHA-256
  5b086372be5112b80ac4e4fc73365e52c82a74f0ab16403178927cc62e8ff609.

- 2026-10-09T20:33:14+00:00: Recorded command exit 0; command argv SHA-256
  4adfac04596170086056d040d01fae0542c561c0985de87545cea8e51b35fa3e.

- 2026-10-09T20:33:37+00:00: Recorded command exit 0; command argv SHA-256
  9c1fb2581d699b02c7edf33716968a70f93290ab512054437721c96ca4fa8093.

- 2026-10-09T20:34:01+00:00: Recorded command exit 1; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T20:34:06+00:00: Recorded command exit 0; command argv SHA-256
  9e10832acf4b934699cc822b584d2221fdcba749ddfdbcd6804b50dc06ee6eac.

- 2026-10-09T20:34:27+00:00: Recorded command exit 0; command argv SHA-256
  c5b2d44f3107c3e94a25e4c3474395063e2376fc5c369822ffa74b3b9ae4ba92.

- 2026-10-09T20:34:49+00:00: Recorded command exit 0; command argv SHA-256
  9c1fb2581d699b02c7edf33716968a70f93290ab512054437721c96ca4fa8093.

- 2026-10-09T20:35:15+00:00: Recorded command exit 0; command argv SHA-256
  5c29502c780c3ccbe7ef8d3fcf02e4fa18e940eb701451c23c61b575bf6e0ba9.

- 2026-10-09T20:35:57+00:00: Recorded command exit 0; command argv SHA-256
  538114a9cfc89fab6d5527885783276e97dcccc254c42f9b2c7de7a24e8f4b44.

- 2026-10-09T20:36:52+00:00: Recorded command exit 0; command argv SHA-256
  74ff85f9c7ae2deca8d01f5a7a961d6014c4906bfd091463fe2e5acbc5a4af0d.

- 2026-10-09T20:38:29+00:00: Heartbeat by codex-ar1770-descriptor-safe-races.

- 2026-10-09T20:39:24+00:00: Recorded command exit 0; command argv SHA-256
  32ee42a28fd2c30c78edd3266506d5ebc9bdbd38eeb8ea910ddee6f58fb9a926.

- 2026-10-09T20:39:53+00:00: Recorded command exit 2; command argv SHA-256
  1f231342cadc74457e55cac3de261446fded7dca26af5ad075d5260635407761.

- 2026-10-09T20:40:41+00:00: Recorded command exit 0; command argv SHA-256
  865a18748d2f5e80c45baaf367aecf4dba2a0ec796eb926d2b14faff409aa811.

- 2026-10-09T20:42:51+00:00: Recorded command exit 0; command argv SHA-256
  cad09ec92df43665693e362faf8bd52f24d198a2d3a93cca4304a21ac20ecd58.

- 2026-10-09T20:43:46+00:00: Recorded command exit 0; command argv SHA-256
  9c1fb2581d699b02c7edf33716968a70f93290ab512054437721c96ca4fa8093.

- 2026-10-09T20:44:08+00:00: Recorded command exit 0; command argv SHA-256
  5295ed44100d9f156af80a476d84f16767a0453a84c950720e3720da310a8789.

- 2026-10-09T20:44:44+00:00: Recorded command exit 0; command argv SHA-256
  d1928a0428ed96490242781988ee150464f7c85a6ce0890b08d016fac47cdc02.

- 2026-10-09T20:45:14+00:00: Recorded command exit 0; command argv SHA-256
  1f22999b0c13f110259db6e366315c1f389f331061fb492ac7e174b9511efd15.

- 2026-10-09T20:45:49+00:00: Recorded command exit 0; command argv SHA-256
  ddbb5502f0d424795dabf150da7be015ab94ddbaabe138dce1d4d5c038935f17.

- 2026-10-09T20:46:47+00:00: Recorded command exit 0; command argv SHA-256
  32ee42a28fd2c30c78edd3266506d5ebc9bdbd38eeb8ea910ddee6f58fb9a926.

- 2026-10-09T20:47:47+00:00: Repaired transaction rollback to track and remove files before
  directories, preserving pre-existing workspace content. Added deterministic collision test.
  Workload tests: 43 unit, 4 public API, 5 validity, 2 doc tests passed. Workspace clippy --locked
  --all-targets -D warnings passed. Signed+DCO commit 6278fcd pushed to PR #540; awaiting fresh
  independent review and exact-head CI.

- 2026-10-09T20:48:13+00:00: Recorded command exit 8; command argv SHA-256
  d7997a49278d5bfbd9b65554614ae7ddc66dbf251579f5fcc74587ba8371a3fe.

- 2026-10-09T20:49:21+00:00: Recorded command exit 8; command argv SHA-256
  d7997a49278d5bfbd9b65554614ae7ddc66dbf251579f5fcc74587ba8371a3fe.

- 2026-10-09T20:49:24+00:00: Recorded command exit 8; command argv SHA-256
  d7997a49278d5bfbd9b65554614ae7ddc66dbf251579f5fcc74587ba8371a3fe.

- 2026-10-09T20:50:32+00:00: Recorded command exit 8; command argv SHA-256
  d7997a49278d5bfbd9b65554614ae7ddc66dbf251579f5fcc74587ba8371a3fe.

- 2026-10-09T20:50:36+00:00: Recorded command exit 8; command argv SHA-256
  d7997a49278d5bfbd9b65554614ae7ddc66dbf251579f5fcc74587ba8371a3fe.

- 2026-10-09T20:50:57+00:00: Recorded command exit 0; command argv SHA-256
  65cb2bd9b06064f7c29ba6bb270860a399b2b24adb8b0d4e474bfd76ab42af24.

- 2026-10-09T20:51:20+00:00: Heartbeat by codex-ar1770-descriptor-safe-races.

- 2026-10-09T20:51:28+00:00: Recorded command exit 0; command argv SHA-256
  5533a04d3907771a4e90d81c996b536017a98257f39d24d0ea31c92b5d808f9c.

- 2026-10-09T20:52:37+00:00: Recorded command exit 0; command argv SHA-256
  c6ce863cd1962ac0abc5e5db54aac7bb75f2d92e53781c597878fc729e130918.

- 2026-10-09T20:52:58+00:00: Recorded command exit 0; command argv SHA-256
  c6ce863cd1962ac0abc5e5db54aac7bb75f2d92e53781c597878fc729e130918.

- 2026-10-09T20:53:03+00:00: Recorded command exit 0; command argv SHA-256
  fbd01e241027bb3bb76d1f9c1a079323be83bccb42141eff57e16f661b03fd60.

- 2026-10-09T20:53:21+00:00: Heartbeat by codex-ar1770-descriptor-safe-races.

- 2026-10-09T20:54:31+00:00: Recorded command exit 0; command argv SHA-256
  c6ce863cd1962ac0abc5e5db54aac7bb75f2d92e53781c597878fc729e130918.

- 2026-10-09T20:54:52+00:00: Recorded command exit 0; command argv SHA-256
  c6ce863cd1962ac0abc5e5db54aac7bb75f2d92e53781c597878fc729e130918.

- 2026-10-09T20:54:56+00:00: Recorded command exit 8; command argv SHA-256
  d7997a49278d5bfbd9b65554614ae7ddc66dbf251579f5fcc74587ba8371a3fe.

- 2026-10-09T20:55:16+00:00: Recorded command exit 0; command argv SHA-256
  90ac15a8fabec06646f61c28d6b866b3323225447bee7c88d21903efe0b42687.

- 2026-10-09T20:55:41+00:00: Recorded command exit 0; command argv SHA-256
  c78f584ca50d93140dae138f01e4464513a005db0469409cda25a863465adef8.

- 2026-10-09T20:56:51+00:00: Recorded command exit 0; command argv SHA-256
  5295ed44100d9f156af80a476d84f16767a0453a84c950720e3720da310a8789.

- 2026-10-09T20:57:13+00:00: Recorded command exit 0; command argv SHA-256
  d644dae88c988c415b11b76b1f0d42d392198f7b619641c8025bb8000d52b542.

- 2026-10-09T20:57:16+00:00: Recorded command exit 0; command argv SHA-256
  9c1fb2581d699b02c7edf33716968a70f93290ab512054437721c96ca4fa8093.

- 2026-10-09T20:57:35+00:00: Recorded command exit 0; command argv SHA-256
  d7997a49278d5bfbd9b65554614ae7ddc66dbf251579f5fcc74587ba8371a3fe.

- 2026-10-09T20:58:01+00:00: Recorded command exit 0; command argv SHA-256
  00673ceafc4991383e9c55b562afefbb5e6c256adc34821b158b8ecf41cba3a5.

- 2026-10-09T20:58:51+00:00: Recorded command exit 0; command argv SHA-256
  eba58bad0622ac42c806f8c2a84672cf818476a566a154b7bdfdb0686b1a2f10.

- 2026-10-09T20:59:03+00:00: Recorded command exit 0; command argv SHA-256
  0bc7de4ee90a1c4e12186a0500fdf89ed306fdf7e76b3749f8adad6f5917f833.

- 2026-10-09T21:00:02+00:00: Recorded command exit 0; command argv SHA-256
  e33622dcf99b60a4bb3498cd8b921eabc91cb1cd9d46bea181072007afd84554.

- 2026-10-09T21:00:17+00:00: Recorded command exit 0; command argv SHA-256
  0b62ec675b1f55aca990c7e340a9d78b915bb6a149a8be5725e96d2662f986f0.

- 2026-10-09T21:01:07+00:00: Recorded command exit 0; command argv SHA-256
  e33622dcf99b60a4bb3498cd8b921eabc91cb1cd9d46bea181072007afd84554.

- 2026-10-09T21:01:20+00:00: Recorded command exit 0; command argv SHA-256
  4ee18d0130afaecad599272e86a66a7e5cdf32a16e316908ddb094e55fc5bfd2.

- 2026-10-09T21:02:19+00:00: Recorded command exit 0; command argv SHA-256
  e33622dcf99b60a4bb3498cd8b921eabc91cb1cd9d46bea181072007afd84554.

- 2026-10-09T21:02:33+00:00: Recorded command exit 0; command argv SHA-256
  800b365901e7d7a29c6686d9583aa02322405d354016378c8aa1777baa2ca9cd.

- 2026-10-09T21:02:45+00:00: Recorded command exit 0; command argv SHA-256
  d2ed91a35389fb91f453fb9ebfd44b20ebf20e13dd66080320395d649012b656.

- 2026-10-09T21:02:59+00:00: Recorded command exit 0; command argv SHA-256
  8f75401ee035fd0a7288da3a93a157b7c9559dcd7b104b4a2d003b0df4178bb0.

- 2026-10-09T21:03:11+00:00: Recorded command exit 0; command argv SHA-256
  6867b3bf0d23254c75c80cc08c25069b7effa6b4a2dcdfe53c8c196347fdb944.

- 2026-10-09T21:04:25+00:00: Recorded command exit 0; command argv SHA-256
  d7997a49278d5bfbd9b65554614ae7ddc66dbf251579f5fcc74587ba8371a3fe.

- 2026-10-09T21:04:37+00:00: Recorded command exit 0; command argv SHA-256
  e33622dcf99b60a4bb3498cd8b921eabc91cb1cd9d46bea181072007afd84554.

- 2026-10-09T21:04:50+00:00: Recorded command exit 0; command argv SHA-256
  0bc7de4ee90a1c4e12186a0500fdf89ed306fdf7e76b3749f8adad6f5917f833.

- 2026-10-09T21:05:02+00:00: Recorded command exit 0; command argv SHA-256
  4ee18d0130afaecad599272e86a66a7e5cdf32a16e316908ddb094e55fc5bfd2.

- 2026-10-09T21:05:14+00:00: Heartbeat by codex-ar1770-descriptor-safe-races.

- 2026-10-09T21:05:52+00:00: Recorded command exit 0; command argv SHA-256
  e33622dcf99b60a4bb3498cd8b921eabc91cb1cd9d46bea181072007afd84554.

- 2026-10-09T21:07:10+00:00: Recorded command exit 0; command argv SHA-256
  e33622dcf99b60a4bb3498cd8b921eabc91cb1cd9d46bea181072007afd84554.

- 2026-10-09T21:07:22+00:00: Recorded command exit 0; command argv SHA-256
  4ee18d0130afaecad599272e86a66a7e5cdf32a16e316908ddb094e55fc5bfd2.

- 2026-10-09T21:07:35+00:00: Post-merge monitoring: success Hosted 37990474147, Credential-free
  37990474163, Broker 37990474279, Fault 37990474124, Huawei 37990474076, Provenance 37990474221;
  dependency-update runs 37990589932/90306/94951/95917/96242 success. Formal 37990474025 and aarch64
  37990474021 first attempts and reruns both report Docker toomanyrequests before any product test.
  No release/receipt yet; preserve failures as infrastructure evidence.

- 2026-10-09T21:08:28+00:00: Recorded command exit 0; command argv SHA-256
  e33622dcf99b60a4bb3498cd8b921eabc91cb1cd9d46bea181072007afd84554.

- 2026-10-09T21:08:43+00:00: Recorded command exit 0; command argv SHA-256
  d2ed91a35389fb91f453fb9ebfd44b20ebf20e13dd66080320395d649012b656.

- 2026-10-09T21:08:55+00:00: Recorded command exit 0; command argv SHA-256
  8f75401ee035fd0a7288da3a93a157b7c9559dcd7b104b4a2d003b0df4178bb0.

- 2026-10-09T21:09:52+00:00: Recorded command exit 0; command argv SHA-256
  e33622dcf99b60a4bb3498cd8b921eabc91cb1cd9d46bea181072007afd84554.

- 2026-10-09T21:10:07+00:00: Post-merge exact-main green: Hosted 37990474147, Credential-free
  37990474163, Broker 37990474279, Fault 37990474124, Repository quality 37990474230, Rust
  37990474203, Huawei 37990474076, Provenance 37990474221. Formal 37990474025 and aarch64
  37990474021 were rerun three times; every failure is Docker toomanyrequests before product
  execution. Do not accept/release until terminal-success rerun.

- 2026-10-09T21:11:16+00:00: Heartbeat by codex-ar1770-descriptor-safe-races.

- 2026-10-09T21:13:28+00:00: Heartbeat by codex-ar1770-descriptor-safe-races.

- 2026-10-09T21:14:36+00:00: Recorded command exit 0; command argv SHA-256
  d2ed91a35389fb91f453fb9ebfd44b20ebf20e13dd66080320395d649012b656.

- 2026-10-09T21:14:48+00:00: Recorded command exit 0; command argv SHA-256
  8f75401ee035fd0a7288da3a93a157b7c9559dcd7b104b4a2d003b0df4178bb0.

- 2026-10-09T21:15:48+00:00: Recorded command exit 0; command argv SHA-256
  e33622dcf99b60a4bb3498cd8b921eabc91cb1cd9d46bea181072007afd84554.

- 2026-10-09T21:16:11+00:00: Recorded command exit 1; command argv SHA-256
  359610079857d765ce43ab5919f8b4dab938e4383d11bd6480bacce1d5f299f7.

- 2026-10-09T21:16:37+00:00: Recorded command exit 0; command argv SHA-256
  695963dbbb0c6e3fcf58f5dc1817be18aa56955c8956743a6a6703f5b85a77b8.

- 2026-10-09T21:16:48+00:00: Recorded command exit 0; command argv SHA-256
  daa6674575ae2db61ad49b6ef6f7b18190e5ca212a55929c0b29843267e349b5.

- 2026-10-09T21:17:02+00:00: Recorded command exit 0; command argv SHA-256
  bbc04ac32d21be48fa45c28843978287e837c9838e65f099fc2cbb3171b7dc21.

- 2026-10-09T21:17:19+00:00: Recorded command exit 0; command argv SHA-256
  71b45802288689777e3000b13abaf093cb9595600f1d4ba50b18d12a1b4d8205.

- 2026-10-09T21:17:27+00:00: Recorded command exit 0; command argv SHA-256
  19b098aae75fc16f603881afc50c20b0eb6e526d6a101290fa9cf373deefb31c.

- 2026-10-09T21:18:21+00:00: Recorded command exit 0; command argv SHA-256
  01d85f6ddebe2ccceaad851546d7c48c0029d847a34876361cab3ac2b599e455.

- 2026-10-09T21:18:32+00:00: Recorded command exit 0; command argv SHA-256
  130cf376fd8a330352ddec59a41be65bdb50617ef97b0d50b98a1b7bdb6cc3bb.

- 2026-10-09T21:18:45+00:00: Recorded command exit 0; command argv SHA-256
  bc58ce008af482ad248cd596278da6682bab5534462c5e88790a2589d5d731a9.

- 2026-10-09T21:19:01+00:00: Recorded command exit 0; command argv SHA-256
  3957a4d49b398428e1e0375fada530c81002ebfef580a1e1d8b37784ff63aba5.

- 2026-10-09T21:19:17+00:00: Verified main still points exactly to
  dc67390494805693aef21d917319253b2e705da7. Dispatch runs headSha exactly matches merge: aarch64
  37992462857 failed Docker Hub toomanyrequests; formal 37992484669 had Kani/Loom success but TLC
  container auth timeout. Original and rerun IDs retained: aarch64 37990474021, formal 37990474025.
  Receipt/accept/release remain prohibited.

- 2026-10-09T21:21:31+00:00: Heartbeat by codex-ar1770-descriptor-safe-races.

- 2026-10-09T21:26:53+00:00: Heartbeat by codex-ar1770-descriptor-safe-races.

- 2026-10-09T21:29:04+00:00: Recorded command exit 0; command argv SHA-256
  daa6674575ae2db61ad49b6ef6f7b18190e5ca212a55929c0b29843267e349b5.

- 2026-10-09T21:29:21+00:00: Recorded command exit 0; command argv SHA-256
  bbc04ac32d21be48fa45c28843978287e837c9838e65f099fc2cbb3171b7dc21.

- 2026-10-09T21:29:38+00:00: Recorded command exit 0; command argv SHA-256
  1472065d100c8aede46ac425c099811a29a9459698bc6d6cd1de83c8ddd6b4c3.

- 2026-10-09T21:29:50+00:00: Recorded command exit 0; command argv SHA-256
  962c84a488dea12804ff3b54301216973f38627e3b1317b61489abc75ea7224b.

- 2026-10-09T21:30:52+00:00: Recorded command exit 0; command argv SHA-256
  c50e05809426e370c7ee454bd0cda2ebd2e12caaaade7c2e42a8bba57ef1ca47.

- 2026-10-09T21:31:10+00:00: Recorded command exit 0; command argv SHA-256
  0ddefc57572926c3f1e80b49ead2907a6cd5d9fab552c7d568316b93f7c4de33.

- 2026-10-09T21:31:30+00:00: Recorded command exit 0; command argv SHA-256
  dffdf5c4d34b76eb36319f0f64b02fd8c1d612bab6baa1e05ecc9bc8919be943.

- 2026-10-09T21:31:46+00:00: Recorded command exit 0; command argv SHA-256
  022f5769a70a8a6fe6b52869062dea97441659a4388bdf22aa522761c720a3c5.

- 2026-10-09T21:32:00+00:00: Exact merge main and all successful gates retained. Attempts: original
  aarch64 37990474021 and formal 37990474025; reruns remained Docker toomanyrequests; exact-head
  workflow_dispatch aarch64 37992462857 and 37993714381, formal 37992484669 and 37993742442, all
  exact headSha dc67390494805693aef21d917319253b2e705da7. Aarch64 dispatches fail Docker Ubuntu
  image pull rate limit. Formal dispatches pass Kani/Loom but TLC fails Docker eclipse-temurin image
  pull/rate limit. No product test failure, no receipt/accept/release yet.

- 2026-10-09T21:34:20+00:00: Recorded command exit 0; command argv SHA-256
  ba90b93c23d8097dec8e1868478dbbdf66a7412b6c2b0bc0f6a64ab8274619a0.

- 2026-10-09T21:34:40+00:00: Recorded command exit 0; command argv SHA-256
  31316435a94f60e21d6298469f789d4f23d43e7a22154e37c53fcd38164b24f8.

- 2026-10-09T21:35:05+00:00: Recorded command exit 0; command argv SHA-256
  e33622dcf99b60a4bb3498cd8b921eabc91cb1cd9d46bea181072007afd84554.

- 2026-10-09T21:36:20+00:00: Recorded command exit 0; command argv SHA-256
  2b0e3ebbafc3d0abac33830b2817cb2f32d9469e17e1c9bfdb5a82e88143a947.

- 2026-10-09T21:36:36+00:00: Heartbeat by codex-ar1770-descriptor-safe-races.

- 2026-10-09T21:36:44+00:00: Latest exact-SHA workflow_dispatch attempts: aarch64 37993714381 and
  formal 37993742442 both headSha dc67390494805693aef21d917319253b2e705da7; aarch64 failed Docker
  Ubuntu pull toomanyrequests, formal failed Docker eclipse-temurin pull toomanyrequests while
  Kani/Loom passed. Original and prior retries remain 37990474021/37990474025,
  37992462857/37992484669. All non-container post-merge gates are green. No receipt, accept,
  release, or gate weakening performed.

- 2026-10-09T22:07:15+00:00: Recovered expired claim formerly owned by
  codex-ar1770-descriptor-safe-races. Replacement Terra worker recovered expired lease; preserving
  existing owner and merged exact-head evidence while awaiting hosted registry recovery.

- 2026-10-09T22:07:29+00:00: Claimed by codex-ar1770-descriptor-safe-races.

- 2026-10-09T22:07:35+00:00: Recorded command exit 0; command argv SHA-256
  84b1fd15ac68be1450067e676ab0c584df59ec11e1d184423e0b2e1f2fd13fa8.

- 2026-10-09T22:08:18+00:00: Recorded command exit 0; command argv SHA-256
  022f5769a70a8a6fe6b52869062dea97441659a4388bdf22aa522761c720a3c5.

- 2026-10-09T22:08:29+00:00: Recorded command exit 0; command argv SHA-256
  dffdf5c4d34b76eb36319f0f64b02fd8c1d612bab6baa1e05ecc9bc8919be943.

- 2026-10-09T22:08:59+00:00: Recorded command exit 1; command argv SHA-256
  359610079857d765ce43ab5919f8b4dab938e4383d11bd6480bacce1d5f299f7.

- 2026-10-09T22:09:26+00:00: Recorded command exit 0; command argv SHA-256
  d2ed91a35389fb91f453fb9ebfd44b20ebf20e13dd66080320395d649012b656.

- 2026-10-09T22:09:40+00:00: Recorded command exit 0; command argv SHA-256
  8f75401ee035fd0a7288da3a93a157b7c9559dcd7b104b4a2d003b0df4178bb0.

- 2026-10-09T22:09:49+00:00: Recorded command exit 0; command argv SHA-256
  abea52f29c7661cf6d220dd98709236ffcaf1fd59982a3005527feacb975ba67.

- 2026-10-09T22:09:58+00:00: Recorded command exit 0; command argv SHA-256
  885c3a98ad9f1a3012dd5dbb6f9cf055ad50e2a9fca1847eff3e9e64c5110de3.

- 2026-10-09T22:10:03+00:00: Recorded command exit 0; command argv SHA-256
  885c3a98ad9f1a3012dd5dbb6f9cf055ad50e2a9fca1847eff3e9e64c5110de3.

- 2026-10-09T22:10:28+00:00: Recovered expired claim, reconciled/doctor green, and started
  exact-head reruns after documented Docker registry failures.

- 2026-10-09T22:10:31+00:00: Heartbeat by codex-ar1770-descriptor-safe-races.

- 2026-10-09T22:12:01+00:00: Recorded command exit 0; command argv SHA-256
  ef5be44ad77cd4f2be1affed17adf9408130b7527c6a0a521a5d643fb9ca1c9a.

- 2026-10-09T22:12:10+00:00: Recorded command exit 0; command argv SHA-256
  cb909219d9cee80ad08aafd48d62f9533848070544be0b98a0bee6efb76e5ee1.

- 2026-10-09T22:13:09+00:00: Recorded command exit 0; command argv SHA-256
  ef5be44ad77cd4f2be1affed17adf9408130b7527c6a0a521a5d643fb9ca1c9a.

- 2026-10-09T22:13:18+00:00: Recorded command exit 0; command argv SHA-256
  cb909219d9cee80ad08aafd48d62f9533848070544be0b98a0bee6efb76e5ee1.

- 2026-10-09T22:13:25+00:00: Recorded command exit 0; command argv SHA-256
  64100aa9fba76409c5f2f3f87b8d0bdf0a3b9191505607bafcd1011ad5d02d07.

- 2026-10-09T22:14:12+00:00: Recorded command exit 0; command argv SHA-256
  cab19fb108daae02bd5a92b7c8183ced00ab0ca312ef7fc9dcddeab64f1808c2.

- 2026-10-09T22:14:22+00:00: Recorded command exit 0; command argv SHA-256
  cab19fb108daae02bd5a92b7c8183ced00ab0ca312ef7fc9dcddeab64f1808c2.

- 2026-10-09T22:14:33+00:00: Recorded command exit 0; command argv SHA-256
  99a35385fa612a3ec6ab7f60c22d2a31fe4baef4895cd6216006d8df0ce3c597.

- 2026-10-09T22:15:44+00:00: Recorded command exit 0; command argv SHA-256
  ae0da9dbcbf83bebea3022bf372cf9708db090b761b7213258d0f0ec00bc8c13.

- 2026-10-09T22:15:48+00:00: Recorded command exit 124; command argv SHA-256
  4e8944c4649c8dab56914deed25a2d4e9056fede16054b02d815b64d4b56ab02.

- 2026-10-09T22:16:37+00:00: Recorded command exit 0; command argv SHA-256
  ef5be44ad77cd4f2be1affed17adf9408130b7527c6a0a521a5d643fb9ca1c9a.
