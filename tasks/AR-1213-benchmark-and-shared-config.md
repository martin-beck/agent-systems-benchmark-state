---
{
  "branch": "docs/ar-1213-benchmark-shared-config",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-24T22:04:08+00:00",
  "depends_on": [
    "AR-1212"
  ],
  "id": "AR-1213",
  "next_action": "Implement syntax-checked tutorials for one benchmark run and atomic shared configuration across selected agents.",
  "observed_branch": "docs/ar-1213-benchmark-shared-config",
  "observed_dirty": 4,
  "observed_head": "eafe1514be33392675ead33a6302336809dd021d",
  "owner": "ar1213-cli-tutorial-luna56",
  "plan": "../plans/AR-1213.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Teach benchmark execution and extending agents with one shared configuration.",
  "task_revision": 6,
  "title": "Benchmark run and shared-agent configuration tutorials",
  "updated_at": "2026-09-24T20:07:19+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1213"
}
---

Implement the linked tutorials and offline syntax/result fixtures. CI must not perform a benchmark
run or contact an agent.

- 2026-09-24T20:02:16+00:00: AR-1212 is durably done; promote the benchmark run and shared-agent CLI
  tutorial AR.

- 2026-09-24T20:04:08+00:00: Claimed by ar1213-cli-tutorial-luna56.
