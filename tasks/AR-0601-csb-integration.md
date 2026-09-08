---
{
  "branch": "feature/csb-integration",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0101",
    "AR-0102",
    "AR-0103",
    "AR-0104",
    "AR-0201",
    "AR-0603"
  ],
  "id": "AR-0601",
  "next_action": "Audit bm-runner interfaces and compare subprocess integration with direct execution.",
  "owner": "",
  "plan": "../plans/AR-0601.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "open",
  "summary": "Reuse CSB application execution and monitoring where contracts fit ASB.",
  "task_revision": 3,
  "title": "Prototype optional CSB integration",
  "updated_at": "2026-09-08T09:03:29+00:00",
  "worktree_key": "agent-systems-benchmark-csb-integration"
}
---
## AR-0601

Reuse CSB application execution and monitoring where contracts fit ASB.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-07T04:45:45+00:00: Added required AR-0603 provenance and execution-conformance
  dependency. AR-0601 now owns only the optional high-level orchestration bridge and direct-versus-
  CSB behavior equivalence after that boundary passes.

- 2026-09-08T09:03:29+00:00: All AR-0601 dependencies are durably done; promote isolated optional
  CSB integration as next compatible P2 task.
