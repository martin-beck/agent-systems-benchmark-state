---
{
  "branch": "fix/ar-1245-postmerge-dco-evidence",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1242", "AR-1243"],
  "id": "AR-1245",
  "next_action": "Implement a narrowly scoped forward-only repair for the known PR-192 merge DCO failure and verify protected-main quality.",
  "observed_branch": "fix/ar-1245-postmerge-dco-evidence",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1245.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Repair protected-main post-merge DCO evidence without rewriting published history.",
  "task_revision": 1,
  "title": "Post-merge DCO admission evidence",
  "updated_at": "2026-09-16T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1245"
}
---

Implement only AR-1245. Preserve the published merge commit and use the repository's documented
development and handoffctl workflow. Do not weaken future signed/DCO admission or touch runtime,
bundle, or TUI code.
