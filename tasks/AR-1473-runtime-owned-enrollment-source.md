---
{
  "schema_version": 1,
  "id": "AR-1473",
  "title": "Runtime-owned authenticated enrollment source",
  "status": "planned",
  "priority": "P0",
  "summary": "Resolve authenticated control enrollment into an opaque runtime-owned source for normal ASB run and sweep.",
  "next_action": "Promote after validating completed dependencies, then claim the isolated worktree and implement the narrow runtime-owned enrollment source.",
  "task_revision": 1,
  "updated_at": "2026-09-27T03:23:00+00:00",
  "owner": "",
  "claim_expires": "",
  "worktree_key": "agent-systems-benchmark-ar-1473-runtime-owned-enrollment-source",
  "branch": "feature/ar-1473-runtime-owned-enrollment-source",
  "checkpoint_commit": "",
  "plan": "../plans/AR-1473-runtime-owned-enrollment-source.md",
  "depends_on": ["AR-1471", "AR-1472", "AR-1379"]
}
---

Successor created from the AR-1470 and AR-1391 protected-main audits. It owns
only the missing runtime/control enrollment-to-source seam and must preserve
the existing fail-closed authority boundaries.

- 2026-09-27T03:23:00+00:00: Created after AR-1470 re-audit at protected main
  `1e2c5911` confirmed that certificate-chain storage and adapter integration
  exist but no runtime-owned enrollment operation populates the source used by
  normal `run`/`sweep`.
