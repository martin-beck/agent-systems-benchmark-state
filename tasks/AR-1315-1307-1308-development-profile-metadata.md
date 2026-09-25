---
{
  "branch": "repair/ar-1315-formal-development-profile-wording",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1314"
  ],
  "id": "AR-1315",
  "next_action": "Promote after AR-1314 is done; update AR-1307/AR-1308 wording and validators to permit diagnostic unsigned fixtures while retaining signed full qualification gates.",
  "owner": "",
  "plan": "../plans/AR-1315.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Align formal-runner task metadata with the explicit unsigned development profile.",
  "task_revision": 2,
  "title": "Formal runner development-profile metadata repair",
  "updated_at": "2026-09-25T11:20:35+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1315-formal-development-profile-metadata"
}
---

# AR-1315

After AR-1314 establishes the explicit unsigned development profile, update AR-1307 and AR-1308
task/plan wording and fail-closed preflight diagnostics. Local unsigned fixtures may prepare or
exercise a diagnostic runner, but no such run may be reported as formal qualification, canonical
full attestation, or release evidence. The exact signed input bundle remains mandatory for those
claims.

- 2026-09-25T11:20:35+00:00: Dependency AR-1314 verified done; promote formal development-profile
  metadata repair.
