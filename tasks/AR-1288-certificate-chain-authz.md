---
{
  "branch": "feature/ar-1288-certificate-chain-authz",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T04:38:57+00:00",
  "depends_on": [
    "AR-0813"
  ],
  "id": "AR-1288",
  "next_action": "Promote after schema and dependency validation; then claim the isolated worktree and implement the AR-0814 certificate issuance and chain-validation successor.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "2fd90557a4e7be32fab590f47bc501462127c1c1",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1288.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Implement runtime-owned certificate issuance and trust-chain validation required by AR-0814.",
  "task_revision": 3,
  "title": "Runtime certificate issuance and chain validation",
  "updated_at": "2026-09-17T02:38:57+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1288-certificate-chain-authz"
}
---
## AR-1288

AR-0814 completed the versioned remote authorization and pairing boundary but identified
certificate issuance, chain validation and trusted route/ancestor authority as a separate gap.
This ASB-only successor supplies that missing cryptographic boundary. It must preserve offline,
fail-closed operation and must not add frontend or TUI behavior.

The implementation owns only the runtime/control certificate and identity boundary, its CLI
argument contract, schemas/docs and tests. It must be based on protected main after AR-0813 and
must not reuse unmerged strict-replay or asb-tui branches.

- 2026-09-17T02:38:44+00:00: Successor for AR-0814 certificate issuance/chain validation gap;
  depends only on completed AR-0813.

- 2026-09-17T02:38:57+00:00: Claimed by asb_ar1024_lifecycle_router.
