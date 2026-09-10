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
  "next_action": "Define and implement signed bundle metadata, digest, license, SBOM, and compatibility verification.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1019.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Verify asb-tui bundles before installation or execution.",
  "task_revision": 2,
  "title": "Verify signed asb-tui extension bundles",
  "updated_at": "2026-09-10T15:17:18+00:00",
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
