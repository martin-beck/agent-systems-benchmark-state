---
{
  "branch": "release/ar-1461-first-customer-release-readiness",
  "checkpoint_commit": "36d4bdf35a644a36a8acfdb31078eb7f668a17c4",
  "claim_expires": "2026-09-26T21:56:24+00:00",
  "depends_on": [
    "AR-1456",
    "AR-1460"
  ],
  "id": "AR-1461",
  "next_action": "Create/execute a reviewed release-tooling repair: provide pinned cargo-deny and cargo-audit, establish the documented bundle/tag/publication workflow, then rerun exact-head release gates against 36d4bdf35a644a36a8acfdb31078eb7f668a17c4.",
  "observed_branch": "release/ar-1461-first-customer-release-readiness",
  "observed_dirty": 0,
  "observed_head": "36d4bdf35a644a36a8acfdb31078eb7f668a17c4",
  "owner": "coordinator-ar1461-release",
  "plan": "../plans/AR-1461.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Prepare and publish the first-customer ASB release from the currently qualified main.",
  "task_revision": 25,
  "title": "First-customer release readiness and publication",
  "updated_at": "2026-09-26T19:56:24+00:00",
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
