---
{
  "branch": "feature/ar-1280-cross-crate-replay-entrypoint",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T02:13:29+00:00",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1280",
  "next_action": "Promote after dependency verification; implement the cross-crate authenticated replay process entrypoint from protected main.",
  "observed_branch": "feature/ar-1280-cross-crate-replay-entrypoint",
  "observed_dirty": 0,
  "observed_head": "69e8b064d3121a4bae1f672cdae9c0c8672000bc",
  "owner": "asb_ar1280_runtime_cli_entrypoint",
  "plan": "../plans/AR-1280.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Implement the cross-crate runtime process entrypoint for primary strict replay.",
  "task_revision": 6,
  "title": "Cross-crate replay process entrypoint",
  "updated_at": "2026-09-17T00:15:26+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1280-cross-crate-replay-entrypoint"
}
---

## AR-1280

Implement the authenticated cross-crate replay process entrypoint from protected main. Preserve
prior blocked evidence, but do not substitute another audit-only result.

- 2026-09-17T00:13:14+00:00: Dependencies AR-1237, AR-1238, and AR-1239 are done. Prior ARs only
  establish the missing seam; this AR must implement the cross-crate entrypoint from protected main.

- 2026-09-17T00:13:29+00:00: Claimed by asb_ar1280_runtime_cli_entrypoint.

- 2026-09-17T00:13:44+00:00: Recorded command exit 0; command argv SHA-256
  3e33781563a4510d2b29ef626cb1a320e5d8447887a3ad016f11857cb6ea7563.

- 2026-09-17T00:15:26+00:00: Recorded command exit 0; command argv SHA-256
  fef085b0d28dbc6b18c7b98ffd05ceee7c8825b95c169924ce62220ed98ee824.
