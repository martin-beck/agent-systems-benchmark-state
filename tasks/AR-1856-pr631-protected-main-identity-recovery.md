---
{
  "branch": "repair/ar-1856-pr631-protected-main-identity",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-13T16:32:14+00:00",
  "depends_on": [],
  "id": "AR-1856",
  "next_action": "Inspect current protected-main refs and preserve the immutable PR #631 merge failure before creating a forward-only recovery topic.",
  "owner": "ar1856-protected-main-repair-luna",
  "plan": "../plans/AR-1856-pr631-protected-main-identity-recovery.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "hosted",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1856.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1856.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Recover protected-main provenance after PR #631 was GitHub-web-merged with a non-local committer.",
  "task_revision": 11,
  "title": "PR #631 protected-main identity recovery",
  "updated_at": "2026-10-13T14:36:25+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1856-pr631-protected-main-identity"
}
---

PR #631 passed exact-head review and CI, but its immutable protected-main merge
`9d2290dc89c9610bb32680f2100759aeba29a06e` was created with committer
`GitHub <noreply@github.com>`. The portable provenance gate correctly rejected
that identity in runs 38413736646 and 38413736253. Preserve the historical
merge and failure; repair only by a forward signed local integration merge.

This AR owns the provenance recovery and post-merge evidence. It does not alter
AR-1850's TUI implementation or AR-1841's Coordinator adoption/state vendor.

- 2026-10-13T14:31:38+00:00: Durable provenance failure evidence supports a narrowly scoped forward
  identity recovery; no AR-1850 or AR-1841 overlap.

- 2026-10-13T14:32:14+00:00: Claimed by ar1856-protected-main-repair-luna.

- 2026-10-13T14:32:26+00:00: Claimed after role admission. Historical merge 9d2290dc and exact
  failures are preserved; proceeding with forward-only local-identity recovery, with no AR-1850 or
  AR-1841 scope.

- 2026-10-13T14:32:57+00:00: Bound worktree
  agent-systems-benchmark-ar-1856-pr631-protected-main-identity on branch
  repair/ar-1856-pr631-protected-main-identity.

- 2026-10-13T14:34:04+00:00: Recorded command exit 0; command argv SHA-256
  6c1e90766ef1400491ebc36eb757646e8c2b13e8895625db43d602a3f0cfd75d.

- 2026-10-13T14:34:34+00:00: Recorded command exit 0; command argv SHA-256
  a42fbd7bb226431de23b1c652a13261b414febb9e2e8c3a53db9e49fbc015e6b.

- 2026-10-13T14:34:57+00:00: Recorded command exit 0; command argv SHA-256
  8f0d1de4fb7d7e7bb26bf3c1033cf0072d42a665b22ef97e23934d857cb491c7.

- 2026-10-13T14:35:40+00:00: Recorded command exit 0; command argv SHA-256
  2b28a4ab52cc20bd97cbb368b1e3ad1d3827b6ab7475a04cf3bf4ff1767a243f.

- 2026-10-13T14:36:08+00:00: Recorded command exit 0; command argv SHA-256
  c5747f4860b679d178ba3457c6b769a74405293a56a443a20a394feb07f910ce.

- 2026-10-13T14:36:25+00:00: Recorded command exit 0; command argv SHA-256
  c5747f4860b679d178ba3457c6b769a74405293a56a443a20a394feb07f910ce.
