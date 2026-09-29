---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1302"],
  "id": "AR-1515",
  "next_action": "Promote after AR-1307; reproduce, repair, and rerun gates.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1515-ar1307-runner-ci-oom-repair.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Repair runner OOM/admission failure without widening its contract.",
  "task_revision": 1,
  "title": "AR-1307 runner CI repair",
  "updated_at": "2026-09-29T18:25:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1515-ar1307-runner-ci-oom-repair"
}
---

This repair is intentionally separate from AR-1307's historical qualification
record. It owns diagnosis and implementation of the remaining runner/CI failure;
it does not weaken formal gates or turn a development result into publication
evidence. Generated disposable seeds are sufficient for development tests.
