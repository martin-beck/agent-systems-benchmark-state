---
{
  "branch": "release/ar-1462-pinned-release-toolchain-bundle-workflow",
  "checkpoint_commit": "36d4bdf35a644a36a8acfdb31078eb7f668a17c4",
  "claim_expires": "",
  "depends_on": [
    "AR-1460"
  ],
  "id": "AR-1462",
  "next_action": "Promote and implement the pinned offline-capable cargo-deny/cargo-audit toolchain and reviewed first-customer bundle/tag workflow, then rerun release readiness against exact protected main.",
  "owner": "",
  "plan": "../plans/AR-1462.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Establish reproducible supply-chain checks and first-customer release bundle publication workflow.",
  "task_revision": 2,
  "title": "Pinned release toolchain and first-customer bundle workflow",
  "updated_at": "2026-09-26T19:17:00+00:00",
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
