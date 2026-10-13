# AR-1857 plan: restore full-gate coverage floor

Raise the terminal full-suite branch-aware coverage from the observed 94% to
the required 95% without lowering the threshold or changing formal/resource
gates. Preserve PR #145 unmerged until the repair is reviewed and green.

1. Identify uncovered first-party paths from the exact 94% artifact.
2. Add narrow positive and negative tests for those paths.
3. Run focused, full, coverage, formal, independent review, and exact-head CI.
4. Publish only through signed DCO workflow; do not alter AR-1841/AR-1849 scope.
