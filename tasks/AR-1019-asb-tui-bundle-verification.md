---
{
  "branch": "feature/asb-tui-bundle-verification",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T18:17:21+00:00",
  "depends_on": [
    "AR-1017",
    "AR-1018"
  ],
  "id": "AR-1019",
  "next_action": "Implement production bounded HTTPS range transport and identity-safe verified cache; add manifest schemas and full fault/coverage gates.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-1019.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Verify asb-tui bundles before installation or execution.",
  "task_revision": 4,
  "title": "Verify signed asb-tui extension bundles",
  "updated_at": "2026-09-10T15:29:52+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-bundle-verification"
}
---
Specify signed release metadata containing immutable source/build references for the TUI,
agent-workflow-coordinator, and agent-workflow-quality, checksums, architecture, ASB/protocol
compatibility, license report, and SBOM. Verify signatures, digests, size, provenance,
license policy, and compatibility before any extraction or execution; reject mutable URLs and partial
downloads. Support bounded retry, resumable transfer, and verified-cache reuse.

Acceptance criteria: valid/tampered/expired/mismatched fixtures, offline verification, redacted errors,
artifact-quota-safe retention, and reproducible verification tests.

- 2026-09-10T15:17:18+00:00: AR-1017 and AR-1018 are complete. Public asb-tui main
  a7ca8e07f177fc6a647b3297df624137cfb85e86 has exact hosted and trusted local validation; signed
  bundle verification may begin.

- 2026-09-10T15:17:21+00:00: Claimed by contracts_20260906.

- 2026-09-10T15:29:52+00:00: Signed+DCO checkpoint e15ea19a62c7db03389ee2a1d83ec2799af85163/tree
  1d0ec10d9bde036338b2da29972a7182287efe81 on exact public main a7ca8e07. Closed bundle manifest
  validates expiry, immutable versioned release URLs, source commit/tree, exact ASB/protocol/tooling
  compatibility, five required artifact kinds, per-artifact 256 MiB and aggregate 512 MiB quotas,
  lowercase SHA-256, and fixed privacy-safe failures. Detached SSH signature verification precedes
  parsing against the pinned signer. Bounded range retrieval retries at most three consecutive
  failures, resumes offsets, rejects overlong/short/tampered content, and reuses only
  size-and-digest-valid cache bytes. License allowlist, required package coverage, SPDX 2.3
  membership, and reproducible GitHub provenance bind back to the signed manifest. Real offline
  signed/tampered fixture plus mutable, expired, mismatched, incomplete, corrupt-cache, retry and
  semantic-policy tests pass. Full 51 tests, fmt, Clippy -D warnings and rustdoc pass. Initial cargo
  commands failed only because wrapper PATH omits cargo/cargo-fmt; pinned absolute Rust 1.93
  toolchain corrected it. Generated target was removed with cargo clean; worktree is clean.
  Production transport/cache, schemas, docs, fault expansion, coverage and complete gates remain.
