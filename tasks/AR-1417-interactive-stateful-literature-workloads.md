---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1416",
    "AR-1408"
  ],
  "id": "AR-1417",
  "next_action": "Promote after AR-1416 is released; audit AgentBench and other docs-listed stateful task sources, then implement the bounded local/mock adapter and catalog records.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1417.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Add selectable interactive and stateful literature workloads beside built-in software-engineering fixtures.",
  "task_revision": 1,
  "title": "Interactive stateful literature workloads",
  "updated_at": "2026-09-24T19:10:00+00:00",
  "worktree_key": ""
}
---

Live agents, providers, and upstream dataset downloads are never required. Use public
fixtures and a deterministic local or LiteLLM-compatible mock for development and CI.

This AR covers AgentBench's interactive OS/database-style workload boundary and any
additional stateful workload explicitly listed in the product literature docs. Frameworks
and harnesses remain non-workloads unless an independent task protocol and grader are
identified.

