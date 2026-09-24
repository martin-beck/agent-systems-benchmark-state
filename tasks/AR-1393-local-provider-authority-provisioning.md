---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1388",
    "AR-1385",
    "AR-1373",
    "AR-1366",
    "AR-1341",
    "AR-1342",
    "AR-1339",
    "AR-1340"
  ],
  "id": "AR-1393",
  "next_action": "Promote after dependencies are verified, then bind an isolated worktree and implement runtime-owned local-provider authority provisioning with offline mock tests.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1393-local-provider-authority-provisioning.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Provision a runtime-owned loopback mock authority so development never requires external provider access.",
  "task_revision": 1,
  "title": "Local provider authority provisioning",
  "updated_at": "2026-09-24T07:48:00+00:00",
  "worktree_key": ""
}
---

This successor is the safe local-provider path required by the user policy. It
must not touch asb-tui, expose private authority, or weaken external-provider
or production egress gates.
