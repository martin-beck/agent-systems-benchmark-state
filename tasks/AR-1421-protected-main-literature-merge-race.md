---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1417",
    "AR-1398"
  ],
  "id": "AR-1421",
  "next_action": "Promote after AR-1417's product merge is preserved and the failed run 36048870322 is recorded; repair the protected-main merge admission/requalification path without weakening the tree invariant.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1421.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Repair protected-main merge-tree requalification after a literature PR merges onto an advanced main.",
  "title": "Protected-main literature merge race repair",
  "task_revision": 1,
  "updated_at": "2026-09-24T19:36:00+00:00",
  "worktree_key": ""
}
---

The failed post-merge Repository Quality result is preserved as evidence. This AR
must not waive the exact-tree check, add a commit-specific exception, or classify
the merge released before fresh exact-main evidence succeeds.

