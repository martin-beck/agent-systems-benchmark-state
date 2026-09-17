---
{
  "branch": "repair/ar-1291-superseded-pointers",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1291",
  "next_action": "Claim the state-repair AR, add the verified successor pointers to AR-1052/1054/1056/1058/1061, reconcile and validate AR-1010 dependency readiness.",
  "observed_branch": "repair/ar-1291-superseded-pointers",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1291.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Repair missing successor pointers on superseded dependency tasks.",
  "task_revision": 1,
  "title": "Repair superseded dependency pointers",
  "updated_at": "2026-09-17T04:15:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1291-superseded-pointers"
}
---

AR-1010 cannot pass dependency validation because legacy superseded tasks AR-1052, AR-1054,
AR-1056, AR-1058, and AR-1061 lack explicit `superseded_by` pointers. This state-only repair
records the successor chain already documented in each task's next action. It must not alter
product or handoffctl code.
