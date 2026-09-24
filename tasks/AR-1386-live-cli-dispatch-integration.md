---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1385",
    "AR-1384",
    "AR-1380",
    "AR-1381",
    "AR-1378",
    "AR-1377"
  ],
  "id": "AR-1386",
  "next_action": "Promote after dependency validation; integrate the authenticated runtime live dispatch source into production asb run and sweep with local provider-mock tests and fail-closed egress/teardown checks.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1386-live-cli-dispatch-integration.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Integrate authenticated runtime live dispatch into production asb run and sweep.",
  "task_revision": 1,
  "title": "Production live CLI dispatch integration",
  "updated_at": "2026-09-24T06:32:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1386-live-cli-dispatch-integration"
}
---

This repair consumes the opaque authenticated dispatch source from AR-1385 in
the actual production CLI path. It must preserve runtime-owned authority and
fail-closed network, credential, namespace, launch-token, lease, and teardown
boundaries.

