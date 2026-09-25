---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1405"
  ],
  "id": "AR-1407",
  "next_action": "Promote after AR-1405; reproduce the sha2 0.11 compile/MSRV failure and either repair it with digest-parity evidence or preserve the supersession.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1407-sha2-compatibility.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "open",
  "summary": "Qualify or repair the closed sha2 0.11 dependency update without weakening crypto or MSRV contracts.",
  "task_revision": 2,
  "title": "sha2 compatibility repair",
  "updated_at": "2026-09-25T11:38:03+00:00",
  "worktree_key": ""
}
---

The current protected cryptographic implementation remains authoritative until
compatibility and digest parity are proven.


- 2026-09-25T11:38:03+00:00: AR-1405 is complete at merged f213b296 with seven green post-merge
  workflows; promote bounded sha2 compatibility qualification
