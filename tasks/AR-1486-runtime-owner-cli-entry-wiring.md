---
{
  "branch": "feature/ar-1486-runtime-owner-cli-entry-wiring",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1480", "AR-1484", "AR-1485"],
  "id": "AR-1486",
  "next_action": "Promote and claim, then audit the protected-main CLI entry path and implement the bounded runtime-owner wiring slice.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1486-runtime-owner-cli-entry-wiring.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Wire the runtime-owned local/mock process owner into ordinary CLI run and sweep.",
  "task_revision": 1,
  "title": "Runtime-owner CLI entry wiring",
  "updated_at": "2026-09-27T13:18:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1486-cli-owner-wiring"
}
---

Dependency-safe successor for the completed process-owner contract and local
mock lifecycle. This task owns only ordinary ASB CLI run/sweep composition via
the AR-1480 opaque seam; it excludes asb-tui, live providers, and caller-built
authority.

- 2026-09-27T13:18:00+00:00: Created as the next implementation slice after AR-1485; depends on completed AR-1480, AR-1484, and AR-1485.
