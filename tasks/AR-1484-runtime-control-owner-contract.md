---
{
  "branch": "feature/ar-1484-runtime-control-owner-contract",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1472", "AR-1473", "AR-1480"],
  "id": "AR-1484",
  "next_action": "Promote and claim, then inspect protocol/runtime identifiers and add the smallest stable owner contract with local/mock/replay tests.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1484-runtime-control-owner-contract.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Define stable runtime/control process-owner lifecycle and opaque handoff contract.",
  "task_revision": 1,
  "title": "Runtime/control process-owner contract",
  "updated_at": "2026-09-27T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1484-runtime-control-owner-contract"
}
---

Design/contract slice for the process owner required by AR-1483. It is
provider-free and ASB-only; it must not modify asb-tui or accept caller-built
authority.

