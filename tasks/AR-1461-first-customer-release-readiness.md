---
{
  "branch": "release/ar-1461-first-customer-release-readiness",
  "checkpoint_commit": "0a85123785c3e5e293fee02df757f494ac3423fe",
  "claim_expires": "",
  "depends_on": [
    "AR-1456",
    "AR-1460"
  ],
  "id": "AR-1461",
  "next_action": "Release done after public tag/release and fresh consumption verification.",
  "observed_branch": "release/ar-1461-first-customer-release-readiness",
  "observed_dirty": 0,
  "observed_head": "0a85123785c3e5e293fee02df757f494ac3423fe",
  "owner": "",
  "plan": "../plans/AR-1461.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "done",
  "summary": "Prepare and publish the first-customer ASB release from the currently qualified main.",
  "task_revision": 46,
  "title": "First-customer release readiness and publication",
  "updated_at": "2026-09-26T20:06:23+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1461-first-customer-release-readiness"
}
---

This AR is the release boundary after current-main first-customer
qualification. It must consume the exact qualified protected-main commit,
preserve the credential-free local/mock and offline boundaries, build a
reproducible bundle, run the established source, privacy, formal, supply-chain
and artifact checks, and publish only through the documented release workflow.
External signing authority is optional where the established workflow permits;
no gate may be weakened. No asb-tui or remote-provider dependency is added.

- 2026-09-26T19:05:18+00:00: Current-main AR-1460 qualification is green at exact 36d4bdf; audit
  established release workflow before publication.

- 2026-09-26T19:05:21+00:00: Claimed by coordinator-ar1461-release.

- 2026-09-26T19:05:58+00:00: Recorded command exit 0; command argv SHA-256
  2e1ae39a626814ee52afd37ca2ad04ed38a36a8d0c3ab1e0e3e1efe3babcd4da.

- 2026-09-26T19:06:12+00:00: Recorded command exit 0; command argv SHA-256
  503f8680998a0b610210a032ce25132adb2d806d47bfeb5181f8624d310b94a1.

- 2026-09-26T19:06:27+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-26T19:06:41+00:00: Recorded command exit 0; command argv SHA-256
  46f8c01f5323975f73b1b628f98d287169d9bbd7a137f3fb2ea8d74866b73ae0.

- 2026-09-26T19:06:56+00:00: Recorded command exit 0; command argv SHA-256
  3cd539291028cf3e190c8520e041b7026e3fad2df0f23ea046d3fb1a68744a13.

- 2026-09-26T19:07:11+00:00: Recorded command exit 0; command argv SHA-256
  319fa6a2ff85ba92e6b7fbedb2e9935dc855ff3c6734d3a86c8dba770f7adac6.

- 2026-09-26T19:07:25+00:00: Recorded command exit 0; command argv SHA-256
  d3d0a5840f55c6090b3ba9ae9591a2d4bca2c94f541f98d1b3079388e69435d6.

- 2026-09-26T19:07:40+00:00: Recorded command exit 0; command argv SHA-256
  7f39d268c3b258e661a6d6cf9a8a0e6aeff271c169af85098b8b7b7832cc9221.

- 2026-09-26T19:07:55+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-26T19:08:25+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-26T19:08:39+00:00: Recorded command exit 101; command argv SHA-256
  09106a58846d62b60a8b096e311be2bf71836cd7e41e5bfbac061fcad43c19de.

- 2026-09-26T19:08:54+00:00: Recorded command exit 101; command argv SHA-256
  2dfec79f126030b62fbf4b28a4ddf3e75532e2e8952409edff46cfecb7874f6a.

- 2026-09-26T19:10:25+00:00: Recorded command exit 0; command argv SHA-256
  428457ea9cc6a21bd46c5be6651ba2faccb5b0b07ddc2fd6f96eca730dea5ab7.

- 2026-09-26T19:10:46+00:00: Recorded command exit 0; command argv SHA-256
  8f020a8266d9eda8e0ed704996e99736ad1cf29c0294cefaaa456dc2d9fb4d92.

- 2026-09-26T19:11:32+00:00: Recorded command exit 0; command argv SHA-256
  b49a90ee600c1023cee9ee9f9e8a4f9a06c53eef8c48d3932d88e482126c7c01.

- 2026-09-26T19:11:48+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-26T19:12:03+00:00: Recorded command exit 0; command argv SHA-256
  6840d2f0cea6f9cf6ffce81b9b1b74dcdddaff8701fc6cc1705c309033813254.

- 2026-09-26T19:12:29+00:00: Release audit against exact qualified main
  36d4bdf35a644a36a8acfdb31078eb7f668a17c4 completed in clean isolated worktree. Version is
  workspace 0.1.0; no release tags exist, no release workflow exists under .github/workflows, and no
  checked-in release/bundle/SBOM/provenance packaging tool was found. Deterministic gates passed:
  cargo fmt --all -- --check; cargo clippy --locked --workspace --all-targets -- -D warnings; cargo
  coverage script completed with required test matrix and coverage report; env RUSTDOCFLAGS=-D
  warnings cargo doc --locked --workspace --no-deps; cargo build --locked --workspace --release.
  Required supply-chain gates are unavailable: cargo deny --locked check exits 101 with cargo error
  no such command deny; cargo audit --deny warnings exits 101 with cargo error no such command
  audit. No publication, tag, force update, remote provider contact, or asb-tui change. Publication
  is fail-closed. A narrowly scoped repair AR is required for pinned tool installation plus reviewed
  release/bundle/tag workflow; handoffctl exposes no task-create command, so no task file was
  fabricated.

- 2026-09-26T19:12:37+00:00: AR-1461 publication blocked truthfully. Exact qualified main
  36d4bdf35a644a36a8acfdb31078eb7f668a17c4 is clean and deterministic
  build/format/Clippy/coverage/rustdoc/release-build gates pass, but required cargo-deny and
  cargo-audit commands are absent (both exit 101), and repository lacks release tags, release
  workflow, and checked-in bundle/SBOM/provenance packaging workflow. No release or tag was
  published. Next action is a reviewed repair AR providing pinned supply-chain tools and an
  established signed bundle/tag/publication workflow; no task file fabricated because handoffctl has
  no create-task command.

- 2026-09-26T19:56:21+00:00: AR-1462 is complete at merge 0a85123785c3e5e293fee02df757f494ac3423fe;
  resume release readiness against the new exact protected main.

- 2026-09-26T19:56:24+00:00: Claimed by coordinator-ar1461-release.

- 2026-09-26T19:57:17+00:00: Heartbeat by coordinator-ar1461-release.

- 2026-09-26T19:57:47+00:00: Recorded command exit 0; command argv SHA-256
  fcf1954a04d485ba664fba058eced39b72923d23b45b447e9ef00ef3354257a1.

- 2026-09-26T19:58:10+00:00: Recorded command exit 0; command argv SHA-256
  1d1590ab3fa34fec84e7fd22fa7515f49785cbce475eb627a87bee7bf63e0622.

- 2026-09-26T19:58:33+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-26T19:58:51+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-26T20:00:01+00:00: Recorded command exit 0; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-26T20:00:21+00:00: Recorded command exit 0; command argv SHA-256
  ab86a6c31434a53260d930880fc61b83fa040b6cd7a01b15358d80f5f29ece93.

- 2026-09-26T20:01:50+00:00: Recorded command exit 0; command argv SHA-256
  428457ea9cc6a21bd46c5be6651ba2faccb5b0b07ddc2fd6f96eca730dea5ab7.

- 2026-09-26T20:02:13+00:00: Recorded command exit 0; command argv SHA-256
  81ad157c486731536a45fa7a20fbb42154329d2498e9c7a41962ac746c2736bf.

- 2026-09-26T20:02:37+00:00: Recorded command exit 1; command argv SHA-256
  3118fb8f38fb2ed906058ada8bf8bf17c1ef05af0c00dfefc03f1790fc4a8b3c.

- 2026-09-26T20:02:52+00:00: Recorded command exit 0; command argv SHA-256
  f723e06cd8ad3fed4761a0991ef7f469f74c10de5ed74332332a735dd605deac.

- 2026-09-26T20:03:12+00:00: Recorded command exit 0; command argv SHA-256
  66171b019b13f4cc7a97b253232d6fbc544aa3dd6e21e55381e2b2bb0cdb50e4.

- 2026-09-26T20:03:39+00:00: Recorded command exit 0; command argv SHA-256
  ce534ff49cf0112fad16a76e9edb5dbe635062981ae8552f273480414b6bcdab.

- 2026-09-26T20:03:55+00:00: Recorded command exit 0; command argv SHA-256
  1d38644262f9661a3d15437b8a99ee8baa5fe3005dd85c60f6a3558d78474ae2.

- 2026-09-26T20:04:21+00:00: Recorded command exit 0; command argv SHA-256
  55f28a0d69566e96cb23147cf5c4d405aca682ea53f28463644d29904b9d4c64.

- 2026-09-26T20:04:43+00:00: Recorded command exit 0; command argv SHA-256
  83728393c37b5bb9a3ae0abbc62bb44dd94d2f4389fe4fcb40127eb67942a080.

- 2026-09-26T20:05:08+00:00: Recorded command exit 0; command argv SHA-256
  20aa68ebbcbd4a269ab626288dce452e56f64d27a973f17e18436324287c684f.

- 2026-09-26T20:05:37+00:00: Recorded command exit 0; command argv SHA-256
  af0ee60cbe5953bea27e0c28608c49b341f193a0e9f4ada9f451ac91b0887ce0.

- 2026-09-26T20:06:11+00:00: Resumed against exact protected origin/main
  0a85123785c3e5e293fee02df757f494ac3423fe after AR-1462. Full gates passed: cargo fmt --all --
  --check; cargo clippy --locked --workspace --all-targets -- -D warnings; cargo test --locked
  --workspace; RUSTDOCFLAGS=-D warnings cargo doc --locked --workspace --no-deps; cargo build
  --locked --workspace --release; coverage (all required matrix/floors); source-header policy;
  pinned offline cargo-deny 0.20.2 and cargo-audit 0.22.2 with exact digests. Generated
  unsigned-release bundle manifest with SPDX/CycloneDX SBOM, provenance, and SHA256SUMS; archive
  SHA256 a4eaebdf422c5fa57f0bca182502416cc8c68aa08faf7588c622e953906c36ed. Created and pushed tag
  v0.1.0 at exact main, published non-draft GitHub release
  https://github.com/martin-beck/agent-systems-benchmark/releases/tag/v0.1.0, and freshly
  downloaded/extracted asset with all checksums and source_revision/profile assertions passing. No
  remote provider or asb-tui changes. One chained privacy command false-alarmed on intentional
  provenance key credentials:none; corrected absolute-path privacy scan passed. Historical exit-101
  records remain the pre-AR-1462 missing-tool evidence.

- 2026-09-26T20:06:23+00:00: AR-1461 complete: exact-main 0a85123785c3e5e293fee02df757f494ac3423fe
  qualified, tag v0.1.0 and public release published, archive
  a4eaebdf422c5fa57f0bca182502416cc8c68aa08faf7588c622e953906c36ed freshly consumed with
  checksum/SBOM/source-revision verification.
