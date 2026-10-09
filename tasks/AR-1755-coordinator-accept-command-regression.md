---
{
  "id": "AR-1755",
  "title": "Restore coordinator acceptance command after v0.3.59 upgrade",
  "priority": "P0",
  "depends_on": ["AR-1753"],
  "plan": "../plans/AR-1755-coordinator-accept-command-regression.md",
  "summary": "Restore the downstream handoffctl accept workflow removed by the v0.3.59 vendor upgrade so validated spec acceptance can be recorded without manual metadata edits.",
  "status": "planned",
  "next_action": "Promote after AR-1753 and restore the downstream acceptance command with focused positive and negative coverage.",
  "owner": "",
  "claim_expires": "",
  "checkpoint_commit": "",
  "task_revision": 1,
  "schema_version": 1,
  "spec_ref": "specs/AR-1755.json",
  "spec_revision": 1,
  "updated_at": "2026-10-09T10:00:00+00:00",
  "branch": "",
  "worktree_key": ""
}
---

Restore only the ASB-state-owned `handoffctl accept` command removed during the
Coordinator v0.3.59 vendor upgrade. Do not modify vendored bytes. The command
must validate ownership, active status, exact revision, task spec identity,
evidence class, evidence reference, and digest before setting `spec_acceptance`.
Preserve fail-closed done admission and add documentation and regression tests.
