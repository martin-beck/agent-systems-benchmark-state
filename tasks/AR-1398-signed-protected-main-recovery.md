---
{
  "branch": "repair/ar-1398-signed-protected-main-recovery",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1337"
  ],
  "id": "AR-1398",
  "next_action": "Promote after the integration queue is quiescent; create a signed+DCO descendant preserving PR #286 merge 123ba915 tree/parents, run independent review and all exact-main gates, then close the three affected repair records with fresh evidence.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1398-signed-protected-main-recovery.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Restore signed+DCO protected-main evidence after an unsigned GitHub-generated repair merge.",
  "task_revision": 1,
  "title": "Signed protected-main recovery",
  "updated_at": "2026-09-24T10:00:00+00:00",
  "worktree_key": ""
}
---

# AR-1398

This is an integration/publication repair only. It must not change workload
semantics, OpenRouter behavior, native-evidence policy, or asb-tui. External
providers are never required for development evidence.
