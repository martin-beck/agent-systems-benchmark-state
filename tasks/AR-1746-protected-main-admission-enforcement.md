---
{
  "branch": "repair/ar-1746-protected-main-admission",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1427",
    "AR-1431"
  ],
  "id": "AR-1746",
  "next_action": "Promote and claim after verifying the current GitHub settings/ruleset snapshot; apply and audit the checked-in protected-main contract without changing product source or weakening development review policy.",
  "owner": "",
  "plan": "../plans/AR-1746-protected-main-admission-enforcement.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1746.json",
  "spec_revision": 1,
  "status": "open",
  "summary": "Apply and independently verify ASB's merge-only protected-main settings and active exact-head ruleset so signed local integrations are enforced by GitHub.",
  "task_revision": 2,
  "title": "Enforce protected-main admission for AR-1722 recovery",
  "updated_at": "2026-10-08T16:15:53+00:00",
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
