---
{
  "branch": "repair/protected-main-dco-history",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-15T10:07:50+00:00",
  "depends_on": [],
  "id": "AR-1196",
  "next_action": "Await independent review and all exact-head PR #171 checks; integration must use local signed merge/push, not GitHub web merge. Current main remains 817a40b.",
  "owner": "asb_main_policy_repair",
  "plan": "../plans/AR-1196.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Restore a Signed-off-by-bearing protected-main history after the catalog merge.",
  "task_revision": 5,
  "title": "Protected-main DCO history repair",
  "updated_at": "2026-09-15T08:08:09+00:00",
  "worktree_key": "agent-systems-benchmark-protected-main-dco-repair"
}
---

Repair the exact ASB main history introduced by catalog integration commit
`327f15eefcdef9c78d60b46b2f2dbe557f23f7b0`, which lacks the required Signed-off-by trailer.
Use the repository-approved reversible history-repair path or a protected merge mechanism that
creates a DCO-bearing boundary. Preserve all feature content, signatures, branch protection and
policy checks; never bypass the gate or misclassify the failed post-merge run.

- 2026-09-15T08:06:31+00:00: Promote planned AR for live policy audit and signed merge-candidate
  preparation; no merge/release.

- 2026-09-15T08:06:33+00:00: Claimed by asb_main_policy_repair.

- 2026-09-15T08:07:50+00:00: Heartbeat by asb_main_policy_repair.

- 2026-09-15T08:08:09+00:00: Prepared and pushed PR #171 from signed local merge candidate
  200edbbbc3f06663484682b2d917de39f192b284. Parents are 817a40bfbd7c906092ec10c8036fe0386152a544 and
  catalog head 78ae48b71ccc85dfa3de8e35e12f8a0ea66f53a8; tree
  519879aa13507f2eb46eb174d404cea7f505525c. SSH ED25519 signature and exact DCO verified. Local
  repository policy passed; signature/failure-path tests 16 passed plus 2 subtests. No merge/release
  performed.
