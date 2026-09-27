---
{
  "schema_version": 1,
  "id": "AR-1476",
  "title": "Repair workspace coverage floor",
  "status": "planned",
  "priority": "P0",
  "summary": "Restore the enforced 90 percent workspace coverage floor blocking exact AR-1474 validation.",
  "next_action": "Promote after validating completed dependencies, then reproduce the 88.05 percent coverage result and add justified tests or exclusions.",
  "task_revision": 1,
  "updated_at": "2026-09-27T04:44:00+00:00",
  "owner": "",
  "claim_expires": "",
  "worktree_key": "agent-systems-benchmark-ar-1476-workspace-coverage-floor-repair",
  "branch": "feature/ar-1476-workspace-coverage-floor-repair",
  "checkpoint_commit": "",
  "plan": "../plans/AR-1476-workspace-coverage-floor-repair.md",
  "depends_on": ["AR-1200", "AR-1379", "AR-1472"]
}
---

Successor created from the AR-1474 repository-quality rerun. The repair must
preserve the 90% floor and use behavioral tests or justified source accounting,
not a weakened gate.

- 2026-09-27T04:44:00+00:00: Created after workflow 36292250172 reported
  88.05% workspace coverage (98,414 total lines, 11,761 missed) at exact head
  `56d284c2`.
