---
{
  "branch": "feature/ar-1496-runtime-owned-provider-capture-control",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1151", "AR-1330", "AR-1433", "AR-1447", "AR-1450", "AR-1455"],
  "id": "AR-1496",
  "title": "Runtime-owned provider capture and control activation",
  "next_action": "Promote after AR-1151, AR-1330, AR-1433, AR-1447, AR-1450 and AR-1455 are verified; implement the real tuple capture/reconciliation and offline activation path over the existing control contracts.",
  "owner": "",
  "plan": "../plans/AR-1496.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Complete runtime-owned provider capture, tuple cassette reconciliation and verified offline activation required by the setup wizard.",
  "task_revision": 1,
  "updated_at": "2026-09-28T14:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1496-runtime-owned-provider-capture-control"
}
---

This is the implementation successor explicitly required by blocked AR-1160.
It is local/mock-first and does not reopen optional production live-provider
execution or alter AR-1160's historical evidence.
