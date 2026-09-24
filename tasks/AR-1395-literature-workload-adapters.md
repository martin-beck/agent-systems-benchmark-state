---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1394"
  ],
  "id": "AR-1395",
  "next_action": "Promote after AR-1394 is done, then implement family adapters and deterministic offline fixtures behind the workload lifecycle contract.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1395-literature-workload-adapters.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Normalize approved literature tasks through bounded, non-vendored ASB workload adapters.",
  "title": "Literature workload adapter boundary",
  "task_revision": 1,
  "updated_at": "2026-09-24T07:58:00+00:00",
  "worktree_key": ""
}
---

Adapters must preserve source semantics and never turn provenance-only entries
into executable or qualified workloads.
