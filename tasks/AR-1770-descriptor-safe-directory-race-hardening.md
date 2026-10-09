---
{
  "branch": "feature/ar-1770-descriptor-safe-directory-race-hardening",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T20:29:23+00:00",
  "depends_on": [
    "AR-1767"
  ],
  "id": "AR-1770",
  "next_action": "Independent reviewer must inspect PR #540 exact head f5e5f0d5a50bd768a7cf80ccf4c84ceb78f3a96e and tree 8d121f72dde5ddf75b95119c049a61e2e652bba0; then wait for exact-head CI.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
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
  "task_revision": 75,
  "title": "Descriptor-safe directory race hardening and acceptance matrix",
  "updated_at": "2026-10-09T20:00:00+00:00",
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
