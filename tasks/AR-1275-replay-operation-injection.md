---
{
  "branch": "feature/ar-1275-replay-operation-injection",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1237", "AR-1238", "AR-1239"],
  "id": "AR-1275",
  "next_action": "Promote after dependency verification; add the required runtime operation-handle injection point to actual replay dispatch and test real supervised traffic.",
  "observed_branch": "feature/ar-1275-replay-operation-injection",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1275.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Inject runtime-owned operation handles into actual strict-replay dispatch.",
  "title": "Runtime operation injection into replay dispatcher",
  "task_revision": 1,
  "updated_at": "2026-09-17T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1275-operation-injection"
}
---
## AR-1275

Implement the runtime operation injection seam for actual strict-replay dispatch. Preserve AR-1274's
blocked evidence and do not accept metadata-only or caller-fabricated execution.
