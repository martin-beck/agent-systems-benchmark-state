---
{
  "branch": "codex/ar-1412-code-generation-controls",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1408",
    "AR-1401"
  ],
  "id": "AR-1412",
  "next_action": "Claim after binding metadata; implement offline-selectable code-generation control adapters.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1412-code-generation-control-adapters.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Recovered an abandoned claim with malformed local-time expiry; branch/worktree are now coordinator-bound before the next claim.",
  "task_revision": 4,
  "title": "Code-generation control workload adapters",
  "updated_at": "2026-09-24T14:27:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1412"
}
---

Live provider/backend connectivity is never required. Development and CI use
bounded local fixtures or LiteLLM-compatible mocks only.

- 2026-09-24T13:38:01+00:00: Dependencies AR-1408 and AR-1401 are done; literature workload family
  adapter is dependency-ready.

- 2026-09-24T14:25:00+00:00: Claimed by ar1412_code_generation_luna56b.

- 2026-09-24T14:27:00+00:00: Coordinator recovery: the prior worker completed without
  binding branch/worktree metadata and its lease encoded local CEST as a +00:00 deadline.
  No owner process or product worktree was present. Claim cleared without product mutation;
  isolated branch codex/ar-1412-code-generation-controls and worktree
  agent-systems-benchmark-ar-1412 are bound for the next claim.
