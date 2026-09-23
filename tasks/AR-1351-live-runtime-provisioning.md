---
{
  "branch": "feature/ar-1351-live-runtime-provisioning",
  "checkpoint_commit": "d069f3eeacae914bec5d33dfbb575cd7e4281b2c",
  "claim_expires": null,
  "depends_on": ["AR-1339", "AR-1340", "AR-1347", "AR-1350"],
  "id": "AR-1351",
  "next_action": "Implement the private runtime-owned host provisioning service for pinned backend/gate, authenticated egress handoff, and observed namespace; keep AR-1349 and AR-1329 downstream and fail-closed.",
  "observed_branch": "feature/ar-1351-live-runtime-provisioning",
  "observed_dirty": 0,
  "observed_head": "d069f3eeacae914bec5d33dfbb091b945e7de933960006",
  "owner": null,
  "plan": "../plans/AR-1351-live-runtime-provisioning.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Add the private host/runtime provisioning seam for live acquisition.",
  "task_revision": 1,
  "title": "Runtime-owned live provisioning",
  "updated_at": "2026-09-23T20:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1351-live-runtime-provisioning"
}
---

Successor repair recorded from AR-1349's constructor audit. Existing relay,
namespace, and launch-factory APIs require authority-bearing host inputs that
the production CLI cannot safely obtain. AR-1351 supplies that missing private
runtime boundary; AR-1349 remains fail-closed until it is merged and verified.
