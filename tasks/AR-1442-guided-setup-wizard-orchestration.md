---
{
  "branch": "feature/ar-1442-guided-setup-wizard-orchestration",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T17:20:10+00:00",
  "depends_on": [
    "AR-1441",
    "AR-1316",
    "AR-1328",
    "AR-1436"
  ],
  "id": "AR-1442",
  "next_action": "Promote after dependencies are done; implement the shared catalog-driven first-run and reconfiguration contract for CLI and TUI.",
  "observed_branch": "main",
  "observed_dirty": 7,
  "observed_head": "bd7d10d4a760a84fa42de2b1fa9e97e8ea85ba09",
  "owner": "coordinator-ar1442",
  "plan": "../plans/AR-1442.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Unify first-run and reconfiguration of agents, providers, auth methods, models and defaults in one guided flow.",
  "task_revision": 7,
  "title": "Guided setup wizard orchestration",
  "updated_at": "2026-09-25T15:22:19+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1442"
}
---

The wizard is a first-class product boundary, not a documentation layer. It
must delegate to authoritative ASB catalogs and runtime-owned credential
enrollment and remain safe when the provider is not reachable.

- 2026-09-25T15:20:07+00:00: Dependencies AR-1441, AR-1316, AR-1328 and AR-1436 are released;
  promote the catalog-driven ASB setup/reconfiguration contract while keeping provider reachability
  optional.

- 2026-09-25T15:20:10+00:00: Claimed by coordinator-ar1442.

- 2026-09-25T15:20:47+00:00: Recorded command exit 0; command argv SHA-256
  952c230617030cdb9ac7cccad9580e9e872536ff13620701c6f7dde17602e980.

- 2026-09-25T15:21:20+00:00: Recorded command exit 0; command argv SHA-256
  952c230617030cdb9ac7cccad9580e9e872536ff13620701c6f7dde17602e980.

- 2026-09-25T15:22:19+00:00: Recorded command exit 0; command argv SHA-256
  4437157c2910dd27cf5a92a2d8bf16b93f23354fadb4ffcbcd0bd71ee4100d2c.
