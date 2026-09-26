---
{
  "branch": "maintenance/ar-1459-retire-stale-state-prs",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1457"
  ],
  "id": "AR-1459",
  "next_action": "Close stale state PRs #20, #21, and #27 as superseded after confirming their proposed AR metadata is already represented by current state; leave blocked formal PR #25 open and record exact outcomes.",
  "owner": "",
  "plan": "../plans/AR-1459.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "planned",
  "summary": "Retire obsolete state-repository pull requests without changing product or formal gates.",
  "task_revision": 1,
  "title": "Retire stale state-repository pull requests",
  "updated_at": "2026-09-26T20:20:00+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1459-retire-stale-state-prs"
}
---

This maintenance AR reconciles old state-repository proposals whose AR
metadata is already present in the authoritative current state. It may close
only PRs #20, #21, and #27 after read-only verification. It must not merge,
rewrite, or delete evidence; it must leave PR #25 open because its formal
qualification remains blocked on truthful capacity evidence. No ASB product or
asb-tui source changes are in scope.
