---
{
  "branch": "feature/asb-tui-bundle-verification",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1017",
    "AR-1018"
  ],
  "id": "AR-1019",
  "next_action": "Publish exact clean 67839598 after final privacy review; open focused PR and require exact-head hosted CI before merge.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1019.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "done",
  "summary": "Verify asb-tui bundles before installation or execution.",
  "task_revision": 6,
  "title": "Verify signed asb-tui extension bundles",
  "updated_at": "2026-09-10T15:53:28+00:00",
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

- 2026-09-10T15:50:06+00:00: Candidate 67839598f7908232b67d4f482475d883908230b0/tree
  a5c8f0e743395dc742cea52fdf0bd0735d629b8b, exact base public main a7ca8e07, is clean with five
  SSH-signed exact-DCO commits. Review repairs added immutable version/commit/tree/build-digest
  closure for asb-tui, coordinator v0.3.5 and quality v0.23.0; sole pinned signer enforcement
  rejects appended keys; persistent partial state resumes across invocations but is never treated as
  verified; partials clear after digest failure or successful content-addressed insertion.
  Production HTTPS ranges and retained-directory owner-private cache are implemented. Full
  exact-head gates pass: 54 Rust tests, fmt, locked Clippy -D warnings, rustdoc -D warnings, release
  build, deny/audit, closed schema fixture validation, shell/workflow/Zizmor, full five-commit
  Gitleaks/privacy, ASB isolation 16 tests plus 2 doctests, and clean llvm-cov 90.74% lines/88.34%
  regions. Initial isolation exit 127 was only wrapper cargo PATH omission; pinned Rust 1.93 PATH
  rerun passed. No branch publication yet.

- 2026-09-10T15:53:28+00:00: Completed public AR-1019. Five SSH-signed exact-DCO source commits
  through 67839598f7908232b67d4f482475d883908230b0/tree a5c8f0e743395dc742cea52fdf0bd0735d629b8b
  passed complete local gates and public PR 5 exact-head hosted run 34498301671. Normal protected
  squash merge produced GitHub-verified exact-DCO main 990517eda77d4d42ff51ca5d1da03b56e7b8cdda with
  identical reviewed tree. Exact-main hosted run 34498444488 and trusted local runner 34498444539
  succeeded; signed-commit protection was restored immediately. Delivered signed closed manifest,
  immutable three-component source/tree/build identities, exact compatibility, artifact
  quotas/digests, license/SPDX/provenance policy, HTTPS range retry, persistent process-restart
  resume, retained-directory owner-private verified cache, offline signed/tampered fixtures, fixed
  privacy-safe failures, schema/docs, 54 tests, ASB isolation 16 plus 2 doctests, and 90.74% line
  coverage. No release artifact was claimed or executed.
