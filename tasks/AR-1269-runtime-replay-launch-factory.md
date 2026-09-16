---
{
  "branch": "feature/ar-1269-runtime-replay-launch-factory",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1237", "AR-1238", "AR-1239"],
  "id": "AR-1269",
  "next_action": "Promote after dependency verification; implement the runtime-owned authenticated launch-bundle factory and real supervised replay fixtures.",
  "observed_branch": "feature/ar-1269-runtime-replay-launch-factory",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1269.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Create runtime-owned launch bundles for supervised strict replay.",
  "task_revision": 1,
  "title": "Runtime-owned replay launch-bundle factory",
  "updated_at": "2026-09-16T23:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1269-runtime-launch-factory"
}
---
## AR-1269

Implement the missing runtime launch-bundle factory required for real supervised replay. Preserve
AR-1268's blocked transport evidence and never move launch authority into the CLI.
