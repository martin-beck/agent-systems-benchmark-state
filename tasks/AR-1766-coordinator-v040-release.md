---
{
  "branch": "upgrade/ar-1766-coordinator-v040-release",
  "claim_expires": "",
  "depends_on": ["AR-1756"],
  "id": "AR-1766",
  "next_action": "Claim in the isolated state worktree, replace the development vendor with the exact v0.4.0 tag through vendor.py sync, test accept-to-done on disposable Git and SQLite fixtures, independently review, merge and verify post-merge.",
  "owner": "",
  "plan": "../plans/AR-1766-coordinator-v040-release.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1766.json",
  "spec_revision": 1,
  "status": "open",
  "summary": "Replace ASB's development Coordinator snapshot with the exact tagged v0.4.0 release and qualify supported spec acceptance end to end.",
  "task_revision": 1,
  "title": "Adopt tagged Coordinator v0.4.0 in ASB state",
  "updated_at": "2026-10-09T16:11:20+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar1766-v040-release"
}
---

Coordinator v0.4.0 is a lightweight unsigned tag at reviewed commit
712b36ea3d188237cbe8104e70d905094f93a96b. ASB state currently uses
an explicitly development-only Coordinator snapshot at c2692d0. Replace
that snapshot through the upstream tag-bound vendor tool; never patch vendored
bytes. Preserve ASB task history, existing acceptance evidence, and all native
quality and release gates.
