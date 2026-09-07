---
{
  "branch": "feature/development-host-workflow-routing",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T10:26:51+00:00",
  "depends_on": [
    "AR-0003",
    "AR-0830"
  ],
  "id": "AR-0831",
  "next_action": "Define trusted-job labels and update ASB workflows without routing public pull-request code to persistent development host capacity.",
  "observed_branch": "feature/development-host-workflow-routing",
  "observed_dirty": 4,
  "observed_head": "14ac5ce3bcc272fc81e764a87b5b82128133f00d",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-0831.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Route explicitly trusted ASB CI jobs to qualified development host runners while preserving disposable public-PR isolation.",
  "task_revision": 8,
  "title": "Integrate development host ASB runners with GitHub workflows",
  "updated_at": "2026-09-07T07:29:32+00:00",
  "worktree_key": "agent-systems-benchmark-development-host-workflow-routing"
}
---
## AR-0831

Route explicitly trusted ASB CI jobs to qualified development host runners while preserving disposable
public pull-request isolation.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-07T07:26:49+00:00: AR-0003 and AR-0830 are durably done; workflow/actionlint/policy
  ownership is free after the AR-0830 merge, and routing remains limited to trusted manual/protected
  events with disposable PR equivalents.

- 2026-09-07T07:26:51+00:00: Claimed by contracts-20260906.

- 2026-09-07T07:27:13+00:00: Recorded command exit 0; command argv SHA-256
  789d951d350d0a21c46d5e5b54369bbca81c249264d811442011fa43887d16ea.

- 2026-09-07T07:29:20+00:00: Recorded command exit 0; command argv SHA-256
  3724c9d7e41c9dff9e46c2388af57eb2c8952b0701c4f275f76d588eef7d2292.

- 2026-09-07T07:29:32+00:00: Recorded command exit 0; command argv SHA-256
  ed60df3b901474f580fc7b404c8de2cdd185b8f37b32885a24fcd35323367f95.
