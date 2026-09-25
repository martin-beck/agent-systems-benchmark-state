---
{
  "branch": "feature/ar-1452-runtime-orchestration-service",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T21:12:29+00:00",
  "depends_on": [
    "AR-1357",
    "AR-1433",
    "AR-1448",
    "AR-1451"
  ],
  "id": "AR-1452",
  "next_action": "Promote after AR-1451 is reviewed and merged; add the asb-orchestrator crate without exposing caller-built authority.",
  "owner": "coordinator-orchestrator-impl",
  "plan": "../plans/AR-1452.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Implement one service-owned authority for admission, attempts, resources, and teardown.",
  "task_revision": 5,
  "title": "Implement the runtime-owned ASB orchestration service",
  "updated_at": "2026-09-25T18:12:56+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1452-runtime-orchestration-service"
}
---

Implement the central service. The mandatory path is local deterministic mock
and strict replay; real-provider connectivity remains optional and fail-closed
until the service can prove the complete authority chain.

- 2026-09-25T18:12:22+00:00: AR-1451 architecture and authority contract merged and post-merge
  verified at 071167d; local mock/replay implementation can proceed against verified AR-1448 without
  waiting on optional AR-1450 replay hardening.

- 2026-09-25T18:12:29+00:00: Claimed by coordinator-orchestrator-impl.

- 2026-09-25T18:12:41+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-09-25T18:12:56+00:00: Recorded command exit 0; command argv SHA-256
  83f1caf095bb9901547b520f2fde199f94671ba108891640af8e229104fbb942.
