---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1421"],
  "id": "AR-1427",
  "next_action": "Promote and reproduce PR #310 merge f511645 versus reviewed topic 9d97e168; repair exact protected-main merge-tree requalification, then rerun AR-1215 post-merge evidence.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1427-protected-main-merge-tree-requalification.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Repair exact protected-main merge-tree requalification after sequential tutorial merges.",
  "title": "Protected-main merge-tree requalification repair",
  "task_revision": 1,
  "updated_at": "2026-09-24T00:00:00+00:00",
  "worktree_key": ""
}
---

This repair preserves the exact-tree policy while making sequential protected
main merges safe. The AR-1215 failure run `36060277237` remains immutable
incident evidence; no gate is waived.

- 2026-09-24: Added after Repository Quality rejected merge `f511645` because
  the protected merge tree differed from reviewed topic tree `9d97e168`.
