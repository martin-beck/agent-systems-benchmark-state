---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1304"
  ],
  "id": "AR-1516",
  "next_action": "Promote after AR-1308 terminates; repair fixture/evidence, rerun.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1516-ar1308-qemu-fixture-evidence-repair.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Repair AR-1308 fixture/evidence for reproducible development runs.",
  "task_revision": 2,
  "title": "AR-1308 QEMU fixture repair",
  "updated_at": "2026-09-29T18:30:11+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1516-ar1308-qemu-fixture-evidence-repair"
}
---

This repair owns fixture correctness and sanitized evidence only. It must not
reinterpret a capacity failure as a model result, weaken formal/publication
qualification, or make reviewed seed material a development prerequisite.

- 2026-09-29T18:30:11+00:00: Completed AR-1304 dependency verified; promote independent AR-1308
  fixture/evidence repair.
