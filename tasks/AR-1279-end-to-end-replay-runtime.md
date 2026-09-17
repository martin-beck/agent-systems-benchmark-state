---
{
  "branch": "feature/ar-1279-end-to-end-replay-runtime",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1237", "AR-1238", "AR-1239"],
  "id": "AR-1279",
  "next_action": "Promote after dependency verification; implement transport plus primary runtime-client handoff from protected main and prove full supervised lifecycle.",
  "observed_branch": "feature/ar-1279-end-to-end-replay-runtime",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1279.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Implement end-to-end runtime-owned execution for primary strict replay.",
  "title": "End-to-end primary replay runtime handoff",
  "task_revision": 1,
  "updated_at": "2026-09-17T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1279-end-to-end-replay-runtime"
}
---

## AR-1279

Implement transport and primary runtime-client handoff end to end from protected main. Preserve
AR-1275 through AR-1278 blocked evidence and require real supervised cassette lifecycle proof.
