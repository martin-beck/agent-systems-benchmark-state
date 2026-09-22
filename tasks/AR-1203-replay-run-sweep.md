---
{
  "branch": "feature/replay-run-sweep",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0204", "AR-0401", "AR-1202"],
  "id": "AR-1203",
  "next_action": "Replace the hard replay-plan rejection in execute_inner with a validated replay path carrying an exact cassette_sha256, then issue per-attempt ReplayLaunchAuthority and run the workload through the loopback strict-replay sidecar under the scheduler.",
  "owner": "",
  "plan": "../plans/AR-1203.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Remove the run cannot use a replay plan gate so run/sweep execute attempts through the strict-replay sidecar when controls.replay.mode == replay, recording replay-labelled evidence in the run store and supporting concurrency/sweep for replay headroom.",
  "task_revision": 1,
  "title": "Enable replay-mode run/sweep benchmarking",
  "updated_at": "2026-09-22T09:39:55+00:00",
  "worktree_key": "agent-systems-benchmark-replay-run-sweep"
}
---
Enable replay as a first-class benchmark mode: `run`/`sweep` accept a replay plan with an exact
`cassette_sha256` and compatible provider selection, execute attempts through the loopback
strict-replay sidecar exactly like AR-1202 but under the scheduler (concurrency, queue, warmup,
timeout, cancellation), persist replay-labelled evidence, and measure replay headroom without ever
claiming live model quality. Live-mode behavior stays byte-identical. Repository:
`martin-beck/agent-systems-benchmark`.

- 2026-09-22T09:39:55+00:00: Defined from the record/replay/benchmark integration proposal.
  Depends on sweeps/arrival scheduling (AR-0204), the workload suite (AR-0401), and end-to-end
  replay authority (AR-1202). ReplaySettings validation changes are coordinator-fenced.
