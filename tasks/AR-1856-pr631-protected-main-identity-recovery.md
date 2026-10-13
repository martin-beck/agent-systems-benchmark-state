---
{
  "branch": "repair/ar-1856-pr631-protected-main-identity",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1856",
  "next_action": "Inspect current protected-main refs and preserve the immutable PR #631 merge failure before creating a forward-only recovery topic.",
  "owner": "",
  "plan": "../plans/AR-1856-pr631-protected-main-identity-recovery.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {"evidence_class":"hosted","evidence_digest":"","evidence_ref":"","spec_ref":"specs/AR-1856.json","spec_revision":1,"status":"pending"},
  "spec_ref": "specs/AR-1856.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Recover protected-main provenance after PR #631 was GitHub-web-merged with a non-local committer.",
  "task_revision": 1,
  "title": "PR #631 protected-main identity recovery",
  "updated_at": "2026-10-13T16:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1856-pr631-protected-main-identity"
}
---

PR #631 passed exact-head review and CI, but its immutable protected-main merge
`9d2290dc89c9610bb32680f2100759aeba29a06e` was created with committer
`GitHub <noreply@github.com>`. The portable provenance gate correctly rejected
that identity in runs 38413736646 and 38413736253. Preserve the historical
merge and failure; repair only by a forward signed local integration merge.

This AR owns the provenance recovery and post-merge evidence. It does not alter
AR-1850's TUI implementation or AR-1841's Coordinator adoption/state vendor.
