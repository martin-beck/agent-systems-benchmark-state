# AR-1856 plan: PR #631 protected-main identity recovery

1. Preserve merge `9d2290dc89c9610bb32680f2100759aeba29a06e`, its exact
   failure, parents, tree, reviewed PR #631 head, and current protected-main tip;
   never rewrite or force-update main.
2. Create the smallest forward-only metadata recovery topic from current main,
   preserving the exact ASB product tree and AR-1850's launcher ownership.
3. Run repository policy, signature, DCO, privacy, focused and full applicable
   gates; obtain independent exact-head review and terminal-success CI.
4. Publish only a signed local two-parent merge through
   `tools/integration/merge_pr.py --push`, then verify the local integration
   committer, exact tree/parents, and every exact-main workflow.
5. Record the immutable historical failure and repaired receipt, coordinate the
   resulting post-merge verification with AR-1850, and do not modify AR-1841.
