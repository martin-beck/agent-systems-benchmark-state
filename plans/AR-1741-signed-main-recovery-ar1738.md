# AR-1741: Signed protected-main recovery for AR-1738

## Objective

Restore exact-main merge-integrity evidence after the preserved GitHub-generated
merge `2f7387e` for AR-1738/PR #504, without rewriting or force-updating
published history.

## Dependencies and scope

This is an independent publication-recovery task; it does not create a
dependency cycle with AR-1738. AR-1738 remains open until this recovery and its
post-merge evidence are complete. AR-1740 is a separate incident and is not
included.

Owned paths are the isolated recovery worktree, signed recovery commit/merge,
and bounded recovery evidence. Do not change ASB product behavior.

## Work sequence

1. Preserve `2f7387e` and record its exact parents, tree, GitHub committer, and
   failed protected-main policy run.
2. Create a minimal forward-only signed+DCO descendant based on `2f7387e` in a
   fresh reviewed PR; do not rewrite or force-update `main`.
3. Independently review the exact recovery tree and use
   `tools/integration/merge_pr.py` to construct the signed two-parent merge
   with an exact target lease.
4. Verify the descendant signature, matching DCO, exact parents/tree, exact-main
   policy, and all required post-merge workflows.

## Definition of done

The historical GitHub merge remains preserved, a signed local-integration
descendant is on protected `main`, exact-main policy and required post-merge
checks are green, and AR-1738 can be released with durable evidence.
