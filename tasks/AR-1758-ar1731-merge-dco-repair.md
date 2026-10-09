---
{
  "branch": "repair/ar-1758-merge-dco",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T14:55:12+00:00",
  "depends_on": [],
  "id": "AR-1758",
  "next_action": "Promote and claim; preserve the failed merge evidence, use the documented repair path, and publish only through a reviewed PR with signed+DCO exact-main verification.",
  "owner": "codex-asb-ar1758-merge-dco-repair-20261009",
  "plan": "../plans/AR-1758-ar1731-merge-dco-repair.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1758.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Restore a compliant protected-main publication after the AR-1731 local merge lacked a DCO trailer, without rewriting published history or weakening gates.",
  "task_revision": 6,
  "title": "Repair AR-1731 protected-main merge provenance",
  "updated_at": "2026-10-09T12:56:40+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1758-merge-dco"
}
---

AR-1731's signed local two-parent merge `b3cb9b2` preserved the reviewed tree and
parents but omitted its matching `Signed-off-by` trailer, so protected-main
portable provenance failed. This repair must preserve that historical evidence,
must not force-update or rewrite `main`, and must use a reviewed repair PR and
the repository's documented merge-integrity tooling. AR-1731 remains unaccepted
until the repaired exact-main workflows are green.

- 2026-10-09T12:55:09+00:00: Created to repair the observed AR-1731 protected-main merge/DCO
  publication mismatch without rewriting history; dependency cycle removed.

- 2026-10-09T12:55:12+00:00: Claimed by codex-asb-ar1758-merge-dco-repair-20261009.

- 2026-10-09T12:56:40+00:00: Recorded command exit 0; command argv SHA-256
  bac5d7b3843f6fd01b1cb89819cc1a7fec08c5ea266e78359b30684dd859efa7.
