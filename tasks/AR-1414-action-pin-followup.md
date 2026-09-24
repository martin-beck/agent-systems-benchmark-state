---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1406"],
  "id": "AR-1414",
  "next_action": "Promote after AR-1406; audit PR #235 for the v2.87.14 immutable release pin, repair policy/check failures, and merge only after exact-head review and all required checks pass.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1414-action-pin-followup.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "planned",
  "summary": "Qualify the newer immutable install-action update reopened as PR #235.",
  "task_revision": 1,
  "title": "Follow-up install-action pin qualification",
  "updated_at": "2026-09-24T00:00:00+00:00",
  "worktree_key": ""
}
---

PR #235 currently targets the post-AR-1406 main and updates install-action to
v2.87.14. Do not merge while policy or exact-head checks fail.
