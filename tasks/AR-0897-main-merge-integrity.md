---
{
  "branch": "fix/main-merge-integrity",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0003"],
  "id": "AR-0897",
  "next_action": "Restore green exact-main commit-policy evidence and prevent unsigned or non-DCO GitHub-generated merge commits.",
  "owner": "",
  "plan": "../plans/AR-0897.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Repair the current main merge-boundary failure and enforce a signed DCO-bearing integration path.",
  "task_revision": 1,
  "title": "Restore main merge integrity",
  "updated_at": "2026-09-09T13:31:55+00:00",
  "worktree_key": "agent-systems-benchmark-main-merge-integrity"
}
---
## AR-0897

Restore exact-main commit-policy evidence without rewriting published history and prevent recurrence.

Trigger: GitHub Actions run 34347816992 rejected merge commit `b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b` before later quality gates because it lacks a matching DCO trailer.

Implementation has not started. Read the linked plan before claiming.
