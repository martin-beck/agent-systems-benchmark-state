---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1817",
  "next_action": "Promote the schema-contract repair, add the documented oracle_gate shape and regression coverage, then independently review and run exact-head coordination CI before merging.",
  "owner": "",
  "plan": "../plans/AR-1817-task-schema-oracle-gate.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1817.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Align the strict ASB task schema with the documented oracle_gate lifecycle field used by existing task records, while retaining rejection of unknown fields.",
  "task_revision": 2,
  "title": "Align task schema with oracle gate contract",
  "updated_at": "2026-10-12T13:20:00+00:00",
  "worktree_key": ""
}
---

# AR-1817 — Align task schema with oracle gate contract

The strict ASB state validation currently rejects the `oracle_gate` field on
AR-1811 and AR-1813 even though the coordinator implementation, task-record
schema, lifecycle validator, and existing durable records support it. Add the
documented bounded `oracle_gate` contract to the ASB project task schema and
regression tests. Preserve strict rejection of unknown task and gate fields;
do not make the schema permissive or alter AR-1816 implementation state.

- 2026-10-12T13:20:00+00:00: Strict validation reproduced two failures: AR-1811 and AR-1813 reject the supported oracle_gate field; task-record schema and lifecycle validator establish the intended contract.
