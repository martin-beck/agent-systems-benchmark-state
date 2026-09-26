---
{
  "branch": "release/ar-1462-pinned-release-toolchain-bundle-workflow",
  "checkpoint_commit": "36d4bdf35a644a36a8acfdb31078eb7f668a17c4",
  "claim_expires": "2026-09-26T21:23:18+00:00",
  "depends_on": [
    "AR-1460"
  ],
  "id": "AR-1462",
  "next_action": "Promote and implement the pinned offline-capable cargo-deny/cargo-audit toolchain and reviewed first-customer bundle/tag workflow, then rerun release readiness against exact protected main.",
  "observed_branch": "release/ar-1462-pinned-release-toolchain-bundle-workflow",
  "observed_dirty": 0,
  "observed_head": "f64f943c73574ea7a8144ca4ec45fb3570dee63e",
  "owner": "coordinator-ar1462-release-tooling",
  "plan": "../plans/AR-1462.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Establish reproducible supply-chain checks and first-customer release bundle publication workflow.",
  "task_revision": 18,
  "title": "Pinned release toolchain and first-customer bundle workflow",
  "updated_at": "2026-09-26T19:24:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1462-pinned-release-toolchain-bundle-workflow"
}
---

This P0 repair AR addresses the exact release-readiness failures recorded by
AR-1461. It must add a reproducible, pinned and offline-capable way to run the
required cargo-deny and cargo-audit checks, plus a reviewed first-customer
release workflow that derives its version/tag, checksums, SBOM/provenance and
bundle manifest from one clean exact commit. The workflow must be fail-closed,
credential-free by default, and must not require a remote provider, native
ARM host, asb-tui source, or external signing authority. An unsigned bundle is
permitted where the established release policy says signing is optional, but
all integrity, provenance, privacy and exact-head checks remain mandatory.

- 2026-09-26T19:20:00+00:00: Created from AR-1461's exact blocker: cargo-deny and
  cargo-audit are absent, and no checked-in release/tag/bundle/SBOM/provenance
  workflow exists. AR-1460's exact protected-main qualification is the input.

- 2026-09-26T19:17:00+00:00: AR-1460 is done; AR-1461 identified the release-tooling blocker;
  promote bounded P0 repair.

- 2026-09-26T19:17:03+00:00: Claimed by coordinator-ar1462-release-tooling.

- 2026-09-26T19:17:35+00:00: Recorded command exit 0; command argv SHA-256
  032da1cbce6ee6ab9b84a18cde263eec8332a57d995e1c47d0fe0c574ab0955f.

- 2026-09-26T19:19:06+00:00: Recorded command exit 0; command argv SHA-256
  d548db58f4ae0860bb692ee6d4196e355223f305ba6cbbc6da2cf15f21cc1454.

- 2026-09-26T19:19:21+00:00: Recorded command exit 0; command argv SHA-256
  d04aa803a9fcb854b247572f9b417fd1935a57ca978bb887d2e7c188e99db043.

- 2026-09-26T19:20:06+00:00: Recorded command exit 1; command argv SHA-256
  0783c4ca231a8c433c4fc4883db0fdec7edf10d94ee0a829627bc64f82738587.

- 2026-09-26T19:20:23+00:00: Recorded command exit 1; command argv SHA-256
  2b8344c1a8344c07788a5a55bb876d13fe3167bb202e50b5621728afa367641f.

- 2026-09-26T19:20:41+00:00: Recorded command exit 0; command argv SHA-256
  882450e35df46d21d00fe38c6e4dd55a42f6d722d854dccce7f39306335e4104.

- 2026-09-26T19:20:57+00:00: Recorded command exit 0; command argv SHA-256
  3111209c79dd189eada14700ee56edcabe74337ee74490b00dc4917b7bdc14f0.

- 2026-09-26T19:21:22+00:00: Recorded command exit 0; command argv SHA-256
  2b8344c1a8344c07788a5a55bb876d13fe3167bb202e50b5621728afa367641f.

- 2026-09-26T19:22:45+00:00: Recorded command exit 0; command argv SHA-256
  8920d3af11aaa0d16797d120a5b2a95755788ebd7343fe5cd03127681263a9d5.

- 2026-09-26T19:23:18+00:00: Heartbeat by coordinator-ar1462-release-tooling.

- 2026-09-26T19:24:00+00:00: Recorded command exit 0; command argv SHA-256
  37eadbd7126ccb695c8136e9133304ee20ae50023cb486664605c871c3af495b.
