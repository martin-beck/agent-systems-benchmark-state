---
{
  "branch": "repair/protected-main-dco-history",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1196",
  "next_action": "Reconcile PR #170 merge against main; do not merge duplicates until exact remote head and post-merge checks are verified.",
  "observed_head": "98acd6d5f5a206b351a54689e7817dd43af406ca",
  "owner": "",
  "plan": "../plans/AR-1196.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "done",
  "summary": "Restore a Signed-off-by-bearing protected-main history after the catalog merge.",
  "task_revision": 9,
  "title": "Protected-main DCO history repair",
  "updated_at": "2026-09-15T08:27:09+00:00",
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

- 2026-09-15T08:10:04+00:00: Live update: PR #170 is now reported MERGED with GitHub-generated merge
  commit 748c16ba67b9cff5a08558784dd183d020a1f2d4 (parents 817a40b and 78ae48b, tree 519879aa). Its
  body includes DCO but committer is GitHub; local main ref query still returns 817a40b, so
  publication/ref reconciliation is pending. PR #171 remains open with signed local candidate
  200edbb; its platform job failed source identity because the PR workflow used synthetic base
  748c16b. Do not merge #171 until refs and exact-main status reconcile.

- 2026-09-15T08:10:42+00:00: Heartbeat by asb_main_policy_repair.

- 2026-09-15T08:10:52+00:00: Additional live evidence: PR #172 opened at 08:09:11 with exact catalog
  topic and DCO body; PR #170 reports merged at 08:07:04 but origin/main remains
  817a40bfbd7c906092ec10c8036fe0386152a544 and no main PushEvent followed. PR #171 hosted platform
  check failed because workflow BASE_COMMIT resolved synthetic merge 748c16ba, reporting source
  identity not immutable; this is a workflow/ref interaction, not candidate source failure. No
  merge/release by this worker.

- 2026-09-15T08:27:09+00:00: Completed: repaired ASB main through GitHub Web Flow DCO-bearing merge
  4f855514c5086e1a933ba1e5a4f41db135dbf0a8; exact main post-merge assurance is green.
