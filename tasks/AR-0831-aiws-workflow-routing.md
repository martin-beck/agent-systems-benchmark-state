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
  "observed_dirty": 0,
  "observed_head": "14ac5ce3bcc272fc81e764a87b5b82128133f00d",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-0831.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Route explicitly trusted ASB CI jobs to qualified development host runners while preserving disposable public-PR isolation.",
  "task_revision": 4,
  "title": "Integrate development host ASB runners with GitHub workflows",
  "updated_at": "2026-09-07T07:27:11+00:00",
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
