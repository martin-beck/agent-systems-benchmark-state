---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1384"
  ],
  "id": "AR-1389",
  "next_action": "Promote after AR-1388 release evidence is reconciled, then bind an isolated worktree and repair the evidenced formal fixture ETXTBSY race without weakening gates.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1389-formal-fixture-exec-race.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Repair the formal online-build fixture race that caused ETXTBSY after AR-1388 merge.",
  "task_revision": 1,
  "title": "Formal fixture executable race repair",
  "updated_at": "2026-09-24T07:06:00+00:00",
  "worktree_key": ""
}
---

This successor owns only the post-merge formal assurance failure recorded by
AR-1388. It must use a fresh isolated worktree and preserve all authority,
privacy, offline, boundedness, and local-mock boundaries.
