---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-24T21:13:07+00:00",
  "depends_on": [
    "AR-1416",
    "AR-1408"
  ],
  "id": "AR-1418",
  "next_action": "Promote after AR-1416 is released; audit tau-bench and AgentDojo literature records, then implement separate reliability and safety workload selectors with deterministic mocks.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "ar1418-tool-use-reliability-safety-luna56",
  "plan": "../plans/AR-1418.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add selectable tool-use reliability and safety workloads from the literature with separate metrics.",
  "task_revision": 4,
  "title": "Tool-use reliability and safety workloads",
  "updated_at": "2026-09-24T19:13:07+00:00",
  "worktree_key": ""
}
---

Live providers and backend services are never required. Development and CI use
deterministic public fixtures or a loopback LiteLLM-compatible mock.

Reliability, utility, and policy-violation outcomes must remain separate evidence
dimensions; no aggregate score may hide unsafe or failed tool calls.


- 2026-09-24T19:12:21+00:00: Dependencies AR-1416 and AR-1408 verified done; open tool-use
  reliability and safety workload implementation.

- 2026-09-24T19:12:58+00:00: Claimed by ar1418-tool-use-reliability-safety-luna56.

- 2026-09-24T19:13:07+00:00: Heartbeat by ar1418-tool-use-reliability-safety-luna56.
