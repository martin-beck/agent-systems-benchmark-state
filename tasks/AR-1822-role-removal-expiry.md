---
{
  "branch": "repair/ar-1822-role-removal-expiry",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T16:36:36+00:00",
  "claim_process": {
    "boot_digest": "sha256:e7865b965cd7fb9a03f25a68c08a4552c90fa89300f35b839e047ca4bb39ff28",
    "pid": 1310543,
    "pid_namespace": "5:4026531836",
    "start_time": 667328298
  },
  "depends_on": [],
  "id": "AR-1822",
  "next_action": "Reconcile current state, promote and claim this repair, then implement and test targeted expired-assignment cleanup without weakening read or admission validation.",
  "owner": "ar1817_schema_contract",
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
  "status": "in_progress",
  "summary": "Allow exact-revision roles.remove cleanup of explicitly named expired assignments while preserving fail-closed reads and admission.",
  "task_revision": 6,
  "title": "Expired role assignment cleanup semantics",
  "updated_at": "2026-10-12T14:36:36+00:00",
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

- 2026-10-12T14:36:12+00:00: dependencies verified; role cleanup repair is next

- 2026-10-12T14:36:14+00:00: Claimed by ar1817_schema_contract.

- 2026-10-12T14:36:19+00:00: Recorded command exit 0; command argv SHA-256
  068e824af8bf3a8aa87247c4898e90c6138107cddcee634b61b3a15d2082d958.

- 2026-10-12T14:36:29+00:00: Implementation branch published for independent review; focused gates
  pass; full suite bounded interruption recorded.

- 2026-10-12T14:36:36+00:00: Claimed by ar1817_schema_contract.
