---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1858"],
  "id": "AR-1859",
  "next_action": "Promote after validating the AR-1858 terminal evidence and bind the exact v0.7.0 formal worktree.",
  "owner": "",
  "plan": "../plans/AR-1859-formal-work-root-validation.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {"evidence_class": "mechanical", "evidence_digest": "", "evidence_ref": "", "spec_ref": "specs/AR-1859.json", "spec_revision": 1, "status": "pending"},
  "spec_ref": "specs/AR-1859.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Reject non-absolute TLC work roots before formal execution.",
  "task_revision": 1,
  "title": "v0.7.0 formal work-root validation",
  "updated_at": "2026-10-13T16:30:00+00:00",
  "worktree_key": ""
}
---

Successor to AR-1858. AR-1858 full guarded run reached 95% coverage but failed three workflow tests: relative-tlc, ../hostile-tlc, and relative/with space each returned rc1 from missing tlc2.TLC instead of required rc64. Preserve formal gates and PR #145 unmerged.
