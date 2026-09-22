---
{
  "branch": "feature/record-replay-workflow",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1201", "AR-1203", "AR-0401"],
  "id": "AR-1204",
  "next_action": "Define the default workload x agent matrix for the in-tree fixtures, execute the plan to live record to seal to offline replay run to report to compare journey per tuple, and wire record-campaign with per-tuple cost estimates and duplicate fencing.",
  "owner": "",
  "plan": "../plans/AR-1204.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Deliver the complete user journey for the specific in-tree workloads: plan, live record (OpenRouter free model), seal, offline replay run, report, compare, with campaign coverage and cost estimates for the free tier.",
  "task_revision": 1,
  "title": "Integrate the record-live to replay-offline benchmark workflow",
  "updated_at": "2026-09-22T09:39:55+00:00",
  "worktree_key": "agent-systems-benchmark-record-replay-workflow"
}
---
Deliver the complete integrated user journey over the in-tree workload fixtures: plan, live record
against the pinned OpenRouter free model, seal the redacted replay-verified cassette, offline
replay-mode run, report, and compare under documented comparable rules. The default matrix is
workload subset (bug-fix, feature-addition, build-repair, refactoring) times selected agents with
one OpenRouter free-model profile; `record-campaign` fences duplicate paid work via `attempt_id`.
Repository: `martin-beck/agent-systems-benchmark`.

- 2026-09-22T09:39:55+00:00: Defined from the record/replay/benchmark integration proposal.
  Depends on live capture (AR-1201), replay-mode run/sweep (AR-1203), and the workload suite
  (AR-0401). Documented rules treat redaction, truncation, profile identity and pacing as hard
  boundaries, not deltas.
