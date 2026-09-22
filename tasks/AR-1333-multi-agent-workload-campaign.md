---
{
  "branch": "feature/ar-1333-multi-agent-workload-campaign",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1329",
    "AR-1332"
  ],
  "id": "AR-1333",
  "next_action": "Add the benchmark campaign mode that runs the compatible agent matrix against the workload suite under one pinned free model, with per-tuple records, sealed cassettes and strict offline replay.",
  "owner": "",
  "plan": "../plans/AR-1333.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Run the multi-agent by workload benchmark campaign with per-tuple evidence and offline replay.",
  "task_revision": 1,
  "title": "Multi-agent by workload benchmark campaign",
  "updated_at": "2026-09-22T13:39:37+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1333-multi-agent-workload-campaign"
}
---

The single-run and capture/replay pieces deliver evidence per execution, but
benchmarking different agents under specific workloads requires a campaign that
drives the whole matrix. This AR adds a campaign mode that, for every selected
agent and workload tuple, executes the agent under the pinned OpenRouter
free-model selection, captures and seals each cassette, and produces a per-tuple
record with the agent, workload, model, digest, result and replay outcome. The
campaign persists intent before provider effects, reconciles interrupted tuples
to stale without repeating paid work, and supports offline replay of the sealed
matrix for reproducible comparison.
