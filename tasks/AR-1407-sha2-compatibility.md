---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1405"],
  "id": "AR-1407",
  "next_action": "Promote after AR-1405; reproduce the sha2 0.11 compile/MSRV failure and either repair it with digest-parity evidence or preserve the supersession.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1407-sha2-compatibility.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "planned",
  "summary": "Qualify or repair the closed sha2 0.11 dependency update without weakening crypto or MSRV contracts.",
  "task_revision": 1,
  "title": "sha2 compatibility repair",
  "updated_at": "2026-09-24T00:00:00+00:00",
  "worktree_key": ""
}
---

The current protected cryptographic implementation remains authoritative until
compatibility and digest parity are proven.

