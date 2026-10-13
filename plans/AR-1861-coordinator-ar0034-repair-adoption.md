# AR-1861 plan: Coordinator AR-0034 legacy-binding repair adoption

Adopt the exact upstream Coordinator repair delivered by AR-0034. The repair
clears only an exact retained `worktree_key` on an open, unowned task with an
empty branch, allowing ASB AR-1826 to bind its reviewed branch without bypassing
the existing `bind-worktree` safety fence.

1. Verify upstream AR-0034 evidence: PR #1293 exact head `0bc30d4`, signed
   local integration merge `3b200c9`, green required checks, and post-merge
   focused positive/negative tests.
2. Use the approved Coordinator vendor/provenance tool from an isolated state
   worktree; never edit vendored coordinator bytes manually.
3. Run vendor, schema, generated-view, privacy, state, formal, and live-doctor
   gates, preserving all existing coverage and authority fences.
4. Independently review and publish the state adoption through signed DCO
   commits, exact-head CI, merge, and post-merge verification.
5. Reconcile AR-1826 only after adoption is merged: claim it, invoke the
   exact-key repair transition, bind the reviewed branch/worktree, and
   requalify the product head against current ASB main.

This is state/coordinator adoption only. It does not implement setup-config
product behavior and does not replace AR-1826 ownership.
