---
{
  "branch": "codex/ar-1417-interactive-stateful-literature",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-24T21:13:42+00:00",
  "depends_on": [
    "AR-1416",
    "AR-1408"
  ],
  "id": "AR-1417",
  "next_action": "Promote after AR-1416 is released; audit AgentBench and other docs-listed stateful task sources, then implement the bounded local/mock adapter and catalog records.",
  "observed_branch": "codex/ar-1417-interactive-stateful-literature",
  "observed_dirty": 0,
  "observed_head": "0dcc71705eb610e4c3ab6a9f775a9d7b9b25218a",
  "owner": "ar1417-literature-luna56",
  "plan": "../plans/AR-1417.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add selectable interactive and stateful literature workloads beside built-in software-engineering fixtures.",
  "task_revision": 7,
  "title": "Interactive stateful literature workloads",
  "updated_at": "2026-09-24T19:19:12+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1417"
}
---

Live agents, providers, and upstream dataset downloads are never required. Use public
fixtures and a deterministic local or LiteLLM-compatible mock for development and CI.

This AR covers AgentBench's interactive OS/database-style workload boundary and any
additional stateful workload explicitly listed in the product literature docs. Frameworks
and harnesses remain non-workloads unless an independent task protocol and grader are
identified.


- 2026-09-24T19:12:18+00:00: Dependencies AR-1416 and AR-1408 verified done; open interactive
  stateful literature workload implementation.

- 2026-09-24T19:13:02+00:00: Claimed by ar1417-literature-luna56.

- 2026-09-24T19:13:13+00:00: Heartbeat by ar1417-literature-luna56.

- 2026-09-24T19:13:42+00:00: Heartbeat by ar1417-literature-luna56.

- 2026-09-24T19:19:00+00:00: Recorded command exit 0; command argv SHA-256
  654cf640246fd2f864bccfb19908b5bbb230454b66e42fdd6aab8458ba5d1e0d.
