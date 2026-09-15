---
{
  "branch": "repair/protected-main-dco-history",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-15T10:06:33+00:00",
  "depends_on": [],
  "id": "AR-1196",
  "next_action": "Repair the protected-main merge/DCO boundary without weakening policy, then rerun exact-main assurance.",
  "owner": "asb_main_policy_repair",
  "plan": "../plans/AR-1196.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Restore a Signed-off-by-bearing protected-main history after the catalog merge.",
  "task_revision": 3,
  "title": "Protected-main DCO history repair",
  "updated_at": "2026-09-15T08:06:33+00:00",
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
