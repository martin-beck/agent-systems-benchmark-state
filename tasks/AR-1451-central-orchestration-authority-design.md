---
{
  "branch": "feature/ar-1451-central-orchestration-authority-design",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T19:32:06+00:00",
  "depends_on": [
    "AR-1341",
    "AR-1357",
    "AR-1433",
    "AR-1448"
  ],
  "id": "AR-1451",
  "next_action": "Promote after reconciling AR-1450 and review the authority matrix, schemas, lifecycle, threat model, and migration design.",
  "owner": "coordinator-orchestration",
  "plan": "../plans/AR-1451.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Freeze one runtime-owned orchestration authority for every ASB run and attempt.",
  "task_revision": 3,
  "title": "Central orchestration authority contract and ASB redesign",
  "updated_at": "2026-09-25T17:32:06+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1451-central-orchestration-authority-design"
}
---

Define and independently review the central runtime-owned orchestration
authority described in the plan. This is an architecture/design AR; it must not
paper over missing runtime primitives with caller-supplied constructors or live
provider access.


- 2026-09-25T17:31:58+00:00: Foundational orchestration authority design is dependency-ready; begin
  reviewed contract and migration design.

- 2026-09-25T17:32:06+00:00: Claimed by coordinator-orchestration.
