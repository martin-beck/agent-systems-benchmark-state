---
{
  "branch": "repair/ar-1746-protected-main-admission",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T18:17:11+00:00",
  "depends_on": [
    "AR-1427",
    "AR-1431"
  ],
  "id": "AR-1746",
  "next_action": "Promote and claim after verifying the current GitHub settings/ruleset snapshot; apply and audit the checked-in protected-main contract without changing product source or weakening development review policy.",
  "observed_branch": "repair/ar-1746-protected-main-admission",
  "observed_dirty": 0,
  "observed_head": "5e8e5b7fdb04a50950e0790d9d66c605e7978606",
  "owner": "ar1746_protected_main_admission_20261008",
  "plan": "../plans/AR-1746-protected-main-admission-enforcement.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1746.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Apply and independently verify ASB's merge-only protected-main settings and active exact-head ruleset so signed local integrations are enforced by GitHub.",
  "task_revision": 6,
  "title": "Enforce protected-main admission for AR-1722 recovery",
  "updated_at": "2026-10-08T16:18:55+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1746-protected-main-admission"
}
---

ASB AR-1722 cannot be truthfully reopened while the repository's external
admission configuration contradicts the checked-in merge-integrity contract.
The current read-only audit reports merge, squash, and rebase enabled, web
signoff disabled, no rulesets, and no classic protection for `main`. Current
ASB product main is otherwise signed, reviewed-tree-equivalent, and hosted
green; this AR therefore owns the bounded external settings repair, not a
product-source rewrite.

Development review remains satisfied by an independent technical worker under
the same GitHub user after exact-head tests. No second account or authorized-
maintainer review is required. Signed commits, matching DCO, exact-tree local
integration, independent technical review, CI, and post-merge evidence remain
mandatory.

- 2026-10-08T16:15:53+00:00: AR-1427 and AR-1431 are done; current live audit confirms the external
  GitHub admission mismatch and no overlapping worker owns repository settings.

- 2026-10-08T16:17:11+00:00: Claimed by ar1746_protected_main_admission_20261008.

- 2026-10-08T16:17:43+00:00: Recorded command exit 0; command argv SHA-256
  94f02abdfe9b939aeb6a1a7498761e025303dd44291c9a4f26c429f01bcdabb9.

- 2026-10-08T16:18:55+00:00: Recorded command exit 1; command argv SHA-256
  e727b346f98e13fb2ad0d88b00531786a3633bbc23d161b0e4aee572bfb9cb4d.
