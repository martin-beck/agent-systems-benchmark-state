---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1423", "AR-1430", "AR-1420", "AR-1416"],
  "id": "AR-1424",
  "next_action": "Promote after AR-1423, AR-1430, AR-1420, and AR-1416 are released; implement the complete local-mock literature selector and campaign matrix.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1424-all-literature-selector-campaign.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Make all locally executable literature workloads selectable and campaignable beside built-in fixtures.",
  "task_revision": 1,
  "title": "Complete literature selector and local campaign matrix",
  "updated_at": "2026-09-24T20:00:00+00:00",
  "worktree_key": ""
}
---

Development and CI use deterministic local fixtures or a loopback
LiteLLM-compatible mock only. External provider connectivity and upstream
dataset downloads are never requirements for this AR.
