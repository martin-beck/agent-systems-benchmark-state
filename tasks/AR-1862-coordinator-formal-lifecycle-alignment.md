---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1862",
  "next_action": "Promote after verifying AR-1861's failed-closed evidence, then align the downstream formal lifecycle runtime/model inventory with the exact upstream AR-0034 vendor contract without weakening gates.",
  "owner": "",
  "plan": "../plans/AR-1862-coordinator-formal-lifecycle-alignment.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Align ASB formal lifecycle runtime/model inventories for Coordinator AR-0034 adoption.",
  "task_revision": 1,
  "title": "Coordinator formal lifecycle inventory alignment",
  "updated_at": "2026-10-13T00:00:00Z",
  "worktree_key": ""
}
---

Narrow compatibility successor routed from AR-1861. The approved upstream
AR-0034 vendor snapshot at signed merge `3b200c9` failed closed during ASB
vendor verification because its runtime lifecycle command inventory contains
`bind-envelope`, `recover-execution`, `change-drift`, and `assumption`, while
ASB's downstream runtime/model inventory is older. This task owns only the
ASB-side formal lifecycle alignment needed for adoption; it does not edit
vendored Coordinator bytes or mutate AR-1826.

