---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1405",
  "next_action": "Promote and claim; rebase each applicable open dependency PR onto protected main, repair/test it, and close only superseded or incompatible candidates with evidence.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1405-open-dependency-pr-reconciliation.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Rebase, repair, verify, and truthfully resolve stale open dependency PRs.",
  "task_revision": 1,
  "title": "Open dependency PR reconciliation",
  "updated_at": "2026-09-24T00:00:00+00:00",
  "worktree_key": ""
}
---

This AR does not authorize merging stale or incompatible dependency updates;
all changes remain subject to current exact-head gates.

