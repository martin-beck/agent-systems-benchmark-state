---
{
  "branch": "feature/verifier-integrity",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0103",
    "AR-0104",
    "AR-0401"
  ],
  "id": "AR-1002",
  "next_action": "Design the immutable observation and score-revision contract using Inspect and Harbor concepts.",
  "owner": "",
  "plan": "../plans/AR-1002.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Separate immutable graders from agent work and version scoring independently of execution.",
  "task_revision": 2,
  "title": "Protect verifiers and support offline rescoring",
  "updated_at": "2026-09-08T00:44:45+00:00",
  "worktree_key": "agent-systems-benchmark-verifier-integrity"
}
---
## AR-1002

Separate immutable graders from agent work and version scoring independently of execution.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-08T00:44:45+00:00: Dependencies AR-0103, AR-0104, and AR-0401 are durably done. Selected
  highest-priority safe dependency-ready P1 leaf aligned with workload integrity; owned
  asb-workloads grader, asb-store observation, and asb-analysis scoring paths are disjoint from
  active AR-0505 replay integration, AR-0840 frontend protocol, and AR-0848 native-capacity
  evidence. Declared branch, worktree, remote ref, and related processes are absent.
