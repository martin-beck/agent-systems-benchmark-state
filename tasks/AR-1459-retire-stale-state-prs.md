---
{
  "branch": "maintenance/ar-1459-retire-stale-state-prs",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-26T19:19:00+00:00",
  "depends_on": [
    "AR-1457"
  ],
  "id": "AR-1459",
  "next_action": "Close stale state PRs #20, #21, and #27 as superseded after confirming their proposed AR metadata is already represented by current state; leave blocked formal PR #25 open and record exact outcomes.",
  "owner": "coordinator-ar1459-state-pr-cleanup",
  "plan": "../plans/AR-1459.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Retire obsolete state-repository pull requests without changing product or formal gates.",
  "task_revision": 5,
  "title": "Retire stale state-repository pull requests",
  "updated_at": "2026-09-26T18:49:25+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1459-retire-stale-state-prs"
}
---

This maintenance AR reconciles old state-repository proposals whose AR
metadata is already present in the authoritative current state. It may close
only PRs #20, #21, and #27 after read-only verification. It must not merge,
rewrite, or delete evidence; it must leave PR #25 open because its formal
qualification remains blocked on truthful capacity evidence. No ASB product or
asb-tui source changes are in scope.

- 2026-09-26T18:48:58+00:00: Current state already supersedes metadata in stale PRs #20, #21, and
  #27; promote bounded cleanup while preserving blocked formal PR #25.

- 2026-09-26T18:49:00+00:00: Claimed by coordinator-ar1459-state-pr-cleanup.

- 2026-09-26T18:49:09+00:00: Recorded command exit 0; command argv SHA-256
  ca490c67e611f58bee3455454857377f87dd2ed32e2448780a7cdbb698c4bf56.

- 2026-09-26T18:49:25+00:00: Recorded command exit 0; command argv SHA-256
  58f8018f10338c80b30a370a8c499a9223ef8552b9d1219173ada0882050eb76.
