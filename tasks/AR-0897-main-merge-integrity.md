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
  "observed_branch": "fix/main-merge-integrity",
  "observed_dirty": 5,
  "observed_head": "b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b",
  "owner": "replay_20260906",
  "plan": "../plans/AR-0897.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair the current main merge-boundary failure and enforce a signed DCO-bearing integration path.",
  "task_revision": 12,
  "title": "Restore main merge integrity",
  "updated_at": "2026-09-09T20:51:13+00:00",
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

- 2026-09-09T20:44:18+00:00: Recorded command exit 2; command argv SHA-256
  9af20895a797539e06740c955ffa5cf40a9a5b20fb1e0e5f81f36c31ce463ee6.

- 2026-09-09T20:48:49+00:00: Recorded command exit 1; command argv SHA-256
  f5ecc4c91aac809c00e8acbc140935a1500893198fc1523d0a5da7560d6c7d78.

- 2026-09-09T20:49:34+00:00: Recorded command exit 0; command argv SHA-256
  45f73c2de287a069d87d4ed561a53981f4289820726199a9c453c9ed851eaa6d.

- 2026-09-09T20:50:29+00:00: Recorded command exit 1; command argv SHA-256
  e0255a140754c9592aeb93ac4acf46bed1e5f2b5fc15e68656e6b76b7aedd071.

- 2026-09-09T20:50:54+00:00: Recorded command exit 1; command argv SHA-256
  105e1d5dbed1e3ec25b5727c69547fedde0fdce7d0c52d17674aa229ba0904e3.

- 2026-09-09T20:51:13+00:00: Recorded command exit 0; command argv SHA-256
  47ebf653bcb6b59543159f1c0768206f98863e7d2df785715d08fc200905bd36.
