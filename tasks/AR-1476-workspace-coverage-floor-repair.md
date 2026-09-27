---
{
  "branch": "feature/ar-1476-workspace-coverage-floor-repair",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1200",
    "AR-1379",
    "AR-1472"
  ],
  "id": "AR-1476",
  "next_action": "Promote after validating completed dependencies, then reproduce the 88.05 percent coverage result and add justified tests or exclusions.",
  "owner": "",
  "plan": "../plans/AR-1476-workspace-coverage-floor-repair.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Restore the enforced 90 percent workspace coverage floor blocking exact AR-1474 validation.",
  "task_revision": 2,
  "title": "Repair workspace coverage floor",
  "updated_at": "2026-09-27T04:44:12+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1476-workspace-coverage-floor-repair"
}
---

Successor created from the AR-1474 repository-quality rerun. The repair must
preserve the 90% floor and use behavioral tests or justified source accounting,
not a weakened gate.

- 2026-09-27T04:44:00+00:00: Created after workflow 36292250172 reported
  88.05% workspace coverage (98,414 total lines, 11,761 missed) at exact head
  `56d284c2`.

- 2026-09-27T04:44:12+00:00: Dependencies AR-1200, AR-1379, and AR-1472 are done; promote the
  independent coverage-floor repair.
