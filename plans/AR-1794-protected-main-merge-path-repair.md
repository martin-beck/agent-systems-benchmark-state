# AR-1794 plan: protected-main merge-path repair

1. Preserve the AR-1781 GitHub-committer failure and inspect the exact merge
   parents, tree, PR association, and workflow receipt.
2. Exercise `tools/integration/merge_pr.py` from a clean reviewed clone using
   the exact approved base, topic head, and tree. Do not rewrite protected main
   or weaken the provenance policy.
3. Add bounded documentation/tests that make the signed local merge path
   unambiguous and reject web-merge publication in development coordination.
4. Obtain independent exact-head review, run all applicable gates, publish via
   the protected path, and verify every exact-main workflow before closeout.
