---
{
  "branch": "repair/ar-1822-role-removal-expiry",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T17:07:38+00:00",
  "claim_process": {
    "boot_digest": "sha256:e7865b965cd7fb9a03f25a68c08a4552c90fa89300f35b839e047ca4bb39ff28",
    "pid": 1742966,
    "pid_namespace": "5:4026531836",
    "start_time": 667514458
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
  "task_revision": 3,
  "title": "Expired role assignment cleanup semantics",
  "updated_at": "2026-10-12T15:07:38+00:00",
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

- 2026-10-12T15:07:35+00:00: dependencies verified; current-main v6 successor after AR-1823
  publication

- 2026-10-12T15:07:38+00:00: Claimed by ar1817_schema_contract.
