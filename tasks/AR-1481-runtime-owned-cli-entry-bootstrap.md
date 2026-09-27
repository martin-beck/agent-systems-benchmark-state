---
{
  "branch": "feature/ar-1481-runtime-owned-cli-entry-bootstrap",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1472", "AR-1473", "AR-1480"],
  "id": "AR-1481",
  "next_action": "Promote and claim, then inspect the protected-main entrypoint and runtime/control bootstrap inputs.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1481-runtime-owned-cli-entry-bootstrap.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Wire runtime-owned authenticated dispatch into the ordinary CLI entry path.",
  "task_revision": 1,
  "title": "Runtime-owned CLI entry bootstrap",
  "updated_at": "2026-09-27T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1481-runtime-owned-cli-entry-bootstrap"
}
---

Narrow successor to the stale/circular AR-1374 and AR-1375 chain. It owns
only process-entry composition over the completed AR-1472, AR-1473, and
AR-1480 opaque-source contracts. It must not touch asb-tui, require a live
provider, accept caller-built authority, or weaken fail-closed boundaries.

