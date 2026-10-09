---
{
  "id": "AR-1758",
  "title": "Repair AR-1731 protected-main merge provenance",
  "priority": "P0",
  "depends_on": [],
  "plan": "../plans/AR-1758-ar1731-merge-dco-repair.md",
  "summary": "Restore a compliant protected-main publication after the AR-1731 local merge lacked a DCO trailer, without rewriting published history or weakening gates.",
  "status": "planned",
  "next_action": "Promote and claim; preserve the failed merge evidence, use the documented repair path, and publish only through a reviewed PR with signed+DCO exact-main verification.",
  "owner": "",
  "claim_expires": "",
  "checkpoint_commit": "",
  "task_revision": 2,
  "schema_version": 1,
  "spec_ref": "specs/AR-1758.json",
  "spec_revision": 1,
  "updated_at": "2026-10-09T12:59:00+00:00",
  "branch": "",
  "worktree_key": ""
}
---

AR-1731's signed local two-parent merge `b3cb9b2` preserved the reviewed tree and
parents but omitted its matching `Signed-off-by` trailer, so protected-main
portable provenance failed. This repair must preserve that historical evidence,
must not force-update or rewrite `main`, and must use a reviewed repair PR and
the repository's documented merge-integrity tooling. AR-1731 remains unaccepted
until the repaired exact-main workflows are green.
