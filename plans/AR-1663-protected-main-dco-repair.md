# AR-1663 — protected-main DCO recognition repair

1. Confirm the dependency records and capture the exact current protected-main
   merge, parents, tree, signature, and DCO failure in a detached isolated
   worktree.
2. Produce a metadata-only signed repair preserving the reviewed product tree
   and required two-parent protected-main topology. Use force-with-lease only
   after confirming the remote head is unchanged and the repair is the exact
   intended replacement.
3. Run the repository's exact protected-main policy and DCO checks, trigger or
   inspect required hosted checks, and record exact SHAs and any blocked hosted
   evidence without weakening development-only nonblocking behavior.
4. Update the ASB coordination receipt and release only after independent
   verification of the state graph, signature, DCO, tree identity, and hosted
   policy.
