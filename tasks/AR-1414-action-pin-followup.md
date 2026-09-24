---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-24T18:08:09+00:00",
  "depends_on": [
    "AR-1406"
  ],
  "id": "AR-1414",
  "next_action": "Coordinator must bind branch codex/ar-1414-install-pin-policy and worktree agent-systems-benchmark-ar-1414; then audit PR #235 v2.87.14 exact base/head and policy failure.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "ar1414-install-pin-recovery-luna56",
  "plan": "../plans/AR-1414-action-pin-followup.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify the newer immutable install-action update reopened as PR #235.",
  "task_revision": 5,
  "title": "Follow-up install-action pin qualification",
  "updated_at": "2026-09-24T16:08:57+00:00",
  "worktree_key": ""
}
---

PR #235 currently targets the post-AR-1406 main and updates install-action to
v2.87.14. Do not merge while policy or exact-head checks fail.

- 2026-09-24T16:06:30+00:00: AR-1406 completed; PR #235 reopened for install-action v2.87.14 and
  requires a fresh immutable-pin qualification.

- 2026-09-24T16:08:09+00:00: Claimed by ar1414-install-pin-recovery-luna56.

- 2026-09-24T16:08:25+00:00: Recorded command exit 0; command argv SHA-256
  14569e5566c147a134fa9a8a4c4b2e00e43cb9b4c6e7b05f097c14342245d052.

- 2026-09-24T16:08:57+00:00: Claim succeeded, and handoffctl run exited 0 creating the isolated
  product worktree at the requested branch. However task metadata still has empty branch and
  worktree_key, so product wrapper calls from that worktree are fenced with active task lacks
  declared worktree and branch. No product inspection or mutation performed.
