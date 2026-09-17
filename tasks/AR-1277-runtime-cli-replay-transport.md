---
{
  "branch": "feature/ar-1277-runtime-cli-replay-transport",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T01:59:50+00:00",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1277",
  "next_action": "Promote after dependency verification; implement the authenticated runtime-to-CLI replay transport boundary and executable lifecycle tests.",
  "observed_branch": "feature/ar-1277-runtime-cli-replay-transport",
  "observed_dirty": 0,
  "observed_head": "69e8b064d3121a4bae1f672cdae9c0c8672000bc",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1277.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide a runtime-issued transport channel for primary strict replay.",
  "task_revision": 4,
  "title": "Runtime-to-CLI replay transport boundary",
  "updated_at": "2026-09-17T00:00:17+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1277-runtime-cli-replay-transport"
}
---

## AR-1277

Implement the authenticated runtime-to-CLI transport required by the primary replay command.
Preserve AR-1276's blocked evidence and require actual supervised execution.

- 2026-09-16T23:59:37+00:00: Dependencies AR-1237, AR-1238, and AR-1239 are done; AR-1276 proves the
  primary CLI lacks any runtime-context or service channel, so a transport boundary is required.

- 2026-09-16T23:59:50+00:00: Claimed by asb_ar1024_lifecycle_router.
