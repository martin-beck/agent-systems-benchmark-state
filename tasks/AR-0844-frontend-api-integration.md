---
{
  "branch": "feature/frontend-api-integration",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T13:46:53+00:00",
  "depends_on": [
    "AR-0840",
    "AR-0841",
    "AR-0842",
    "AR-0843"
  ],
  "id": "AR-0844",
  "next_action": "Integrate independently reviewed frontend API components and qualify standalone runner operation.",
  "observed_branch": "feature/frontend-api-integration",
  "observed_dirty": 0,
  "observed_head": "4523da9629ff09451a0a2d2fe332d80bbb1320de",
  "owner": "replay_20260906",
  "plan": "../plans/AR-0844.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Integrate and qualify the frontend control API as an independent boundary.",
  "task_revision": 4,
  "title": "Integrate frontend control API",
  "updated_at": "2026-09-08T10:47:46+00:00",
  "worktree_key": "agent-systems-benchmark-frontend-api-integration"
}
---
## AR-0844

Integrate the reviewed protocol, transport, lifecycle, and privacy components. Prove the runner
starts and completes without a frontend, frontend restart does not alter runs, reconnect loses no
status, no implicit network listener exists, and exact-head CI/post-merge recovery checks pass.

- 2026-09-08T10:46:22+00:00: All dependencies AR-0840 through AR-0843 are durably done. Promote
  final frontend API integration as the highest-priority safe ready leaf: use a new isolated
  worktree and limit product scope to integration/standalone-runner qualification, with no shared
  Cargo/schema changes and no overlap with active AR-0316 or AR-1005.

- 2026-09-08T10:46:53+00:00: Claimed by replay_20260906.
