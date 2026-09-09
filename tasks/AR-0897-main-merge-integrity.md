---
{
  "branch": "fix/main-merge-integrity",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T23:41:27+00:00",
  "depends_on": [
    "AR-0003"
  ],
  "id": "AR-0897",
  "next_action": "Restore green exact-main commit-policy evidence and prevent unsigned or non-DCO GitHub-generated merge commits.",
  "owner": "replay_20260906",
  "plan": "../plans/AR-0897.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair the current main merge-boundary failure and enforce a signed DCO-bearing integration path.",
  "task_revision": 4,
  "title": "Restore main merge integrity",
  "updated_at": "2026-09-09T20:42:21+00:00",
  "worktree_key": "agent-systems-benchmark-main-merge-integrity"
}
---
## AR-0897

Restore exact-main commit-policy evidence without rewriting published history and prevent recurrence.

Trigger: GitHub Actions run 34347816992 rejected merge commit `b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b` before later quality gates because it lacks a matching DCO trailer.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-09T20:41:24+00:00: Dependency AR-0003 is done. P0 AR-0897 is the highest-priority ready
  unowned task with no existing branch, PR, worktree, or durable product effect; its
  integration-policy/docs/fixture scope is disjoint from active AR-0907 hosted-platform paths,
  AR-0908 asb-cli test path, and held formal integration.

- 2026-09-09T20:41:27+00:00: Claimed by replay_20260906.

- 2026-09-09T20:42:21+00:00: Recorded command exit 0; command argv SHA-256
  d0a0f89064e7d4fea28001a15ac51ee35d8f2ed68ae6f0d6722c4eb213e169a8.
