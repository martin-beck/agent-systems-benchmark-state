---
{
  "branch": "feature/ar-1280-cross-crate-replay-entrypoint",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1237", "AR-1238", "AR-1239"],
  "id": "AR-1280",
  "next_action": "Promote after dependency verification; implement the cross-crate authenticated replay process entrypoint from protected main.",
  "observed_branch": "feature/ar-1280-cross-crate-replay-entrypoint",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1280.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Implement the cross-crate runtime process entrypoint for primary strict replay.",
  "title": "Cross-crate replay process entrypoint",
  "task_revision": 1,
  "updated_at": "2026-09-17T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1280-cross-crate-replay-entrypoint"
}
---

## AR-1280

Implement the authenticated cross-crate replay process entrypoint from protected main. Preserve
prior blocked evidence, but do not substitute another audit-only result.
