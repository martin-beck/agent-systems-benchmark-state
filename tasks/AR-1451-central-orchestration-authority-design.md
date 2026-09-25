---
{
  "schema_version": 1,
  "id": "AR-1451",
  "title": "Central orchestration authority contract and ASB redesign",
  "status": "planned",
  "priority": "P0",
  "summary": "Freeze one runtime-owned orchestration authority for every ASB run and attempt.",
  "next_action": "Promote after reconciling AR-1450 and review the authority matrix, schemas, lifecycle, threat model, and migration design.",
  "task_revision": 1,
  "updated_at": "2026-09-25T17:29:20+00:00",
  "owner": "",
  "claim_expires": "",
  "worktree_key": "agent-systems-benchmark-ar-1451-central-orchestration-authority-design",
  "branch": "feature/ar-1451-central-orchestration-authority-design",
  "checkpoint_commit": "",
  "plan": "../plans/AR-1451.md",
  "depends_on": ["AR-1341", "AR-1357", "AR-1433", "AR-1448"]
}
---

Define and independently review the central runtime-owned orchestration
authority described in the plan. This is an architecture/design AR; it must not
paper over missing runtime primitives with caller-supplied constructors or live
provider access.

