---
{
  "branch": "feature/verifier-integrity",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T06:46:15+00:00",
  "depends_on": [
    "AR-0103",
    "AR-0104",
    "AR-0401"
  ],
  "id": "AR-1002",
  "next_action": "Design the immutable observation and score-revision contract using Inspect and Harbor concepts.",
  "observed_branch": "feature/verifier-integrity",
  "observed_dirty": 0,
  "observed_head": "f42645dd05f17eca5635ca2e82057b703a03a1c3",
  "owner": "replay_20260906",
  "plan": "../plans/AR-1002.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Separate immutable graders from agent work and version scoring independently of execution.",
  "task_revision": 6,
  "title": "Protect verifiers and support offline rescoring",
  "updated_at": "2026-09-08T03:46:15+00:00",
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

- 2026-09-08T00:44:48+00:00: Claimed by replay_20260906.

- 2026-09-08T00:44:57+00:00: Recorded command exit 0; command argv SHA-256
  bdcaa9f19a30302c554a18a1e3bb84e9045c77088ffcbebc5ef28be0f0f65159.

- 2026-09-08T03:46:15+00:00: Heartbeat by replay_20260906.
