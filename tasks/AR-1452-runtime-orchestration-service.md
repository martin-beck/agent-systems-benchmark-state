---
{
  "branch": "feature/ar-1452-runtime-orchestration-service",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1357",
    "AR-1433",
    "AR-1448",
    "AR-1451"
  ],
  "id": "AR-1452",
  "next_action": "Promote after AR-1451 is reviewed and merged; add the asb-orchestrator crate without exposing caller-built authority.",
  "owner": "",
  "plan": "../plans/AR-1452.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Implement one service-owned authority for admission, attempts, resources, and teardown.",
  "task_revision": 2,
  "title": "Implement the runtime-owned ASB orchestration service",
  "updated_at": "2026-09-25T18:12:22+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1452-runtime-orchestration-service"
}
---

Implement the central service. The mandatory path is local deterministic mock
and strict replay; real-provider connectivity remains optional and fail-closed
until the service can prove the complete authority chain.

- 2026-09-25T18:12:22+00:00: AR-1451 architecture and authority contract merged and post-merge
  verified at 071167d; local mock/replay implementation can proceed against verified AR-1448 without
  waiting on optional AR-1450 replay hardening.
