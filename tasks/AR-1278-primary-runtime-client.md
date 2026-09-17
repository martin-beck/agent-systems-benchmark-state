---
{
  "branch": "feature/ar-1278-primary-runtime-client",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T02:08:53+00:00",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1278",
  "next_action": "Promote after dependency verification; hand the runtime-issued replay client into primary argument dispatch and prove supervised lifecycle behavior.",
  "observed_branch": "feature/ar-1278-primary-runtime-client",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1278.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Connect the primary replay command to the runtime-issued transport client.",
  "task_revision": 3,
  "title": "Primary replay runtime client handoff",
  "updated_at": "2026-09-17T00:08:53+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1278-primary-runtime-client"
}
---

## AR-1278

Connect the primary argument-level replay command to the runtime-issued transport client. Preserve
AR-1277's blocked evidence and require actual supervised execution and lifecycle proof.

- 2026-09-17T00:08:37+00:00: Dependencies AR-1237, AR-1238, and AR-1239 are done; AR-1277 proves the
  primary dispatcher still does not receive a runtime-issued client.

- 2026-09-17T00:08:53+00:00: Claimed by asb_ar1024_lifecycle_router.
