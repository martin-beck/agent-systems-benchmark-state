---
{
  "schema_version": 1,
  "id": "AR-1452",
  "title": "Implement the runtime-owned ASB orchestration service",
  "status": "planned",
  "priority": "P0",
  "summary": "Implement one service-owned authority for admission, attempts, resources, and teardown.",
  "next_action": "Promote after AR-1451 is reviewed and merged; add the asb-orchestrator crate without exposing caller-built authority.",
  "task_revision": 1,
  "updated_at": "2026-09-25T17:29:20+00:00",
  "owner": "",
  "claim_expires": "",
  "worktree_key": "agent-systems-benchmark-ar-1452-runtime-orchestration-service",
  "branch": "feature/ar-1452-runtime-orchestration-service",
  "checkpoint_commit": "",
  "plan": "../plans/AR-1452.md",
  "depends_on": ["AR-1451", "AR-1450"]
}
---

Implement the central service. The mandatory path is local deterministic mock
and strict replay; real-provider connectivity remains optional and fail-closed
until the service can prove the complete authority chain.

