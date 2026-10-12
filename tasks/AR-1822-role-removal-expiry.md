---
{
  "branch": "repair/ar-1822-role-removal-expiry",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1822",
  "next_action": "Reconcile current state, promote and claim this repair, then implement and test targeted expired-assignment cleanup without weakening read or admission validation.",
  "owner": "",
  "plan": "../plans/AR-1822-role-removal-expiry.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1822.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1822.json",
  "spec_revision": 1,
  "status": "open",
  "summary": "Allow exact-revision roles.remove cleanup of explicitly named expired assignments while preserving fail-closed reads and admission.",
  "task_revision": 2,
  "title": "Expired role assignment cleanup semantics",
  "updated_at": "2026-10-12T14:45:53+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1822-role-removal-expiry"
}
---

AR-1820 cannot safely clear stale role assignments because the current removal
path validates every assignment with admission-time expiry semantics. This
repair separates explicit, exact-revision administrative cleanup from reads and
admission: removal may delete only the named structurally valid assignment,
including an expired one, while list/check/doctor/admission remain fail-closed.
No runtime authority is broadened and no role state is edited outside the
transactional command.

- 2026-10-12T14:45:53+00:00: dependencies verified; fresh current-main successor for
  strict-consistency repair
