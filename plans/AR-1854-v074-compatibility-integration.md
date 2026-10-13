# AR-1854 plan: v0.7.4 compatibility integration

Integrate the exact reviewed heads of AR-1851, AR-1852 and AR-1853 after all
three are merged, then qualify the resulting tree with the repository's strict
and formal gates.

1. Verify the three merged commits, signatures, DCO trailers and trees.
2. Reproduce the standalone cross-repair failures on the integrated tree and
   confirm each is resolved by the owning repair without changing thresholds.
3. Run the locked full suite, coverage, strict state-consistency and formal
   model/implementation gates on the exact integrated head.
4. Record independent exact-head review, required CI, merge and post-merge
   evidence; retain any remaining baseline failure as a blocker.

Dependencies: AR-1851, AR-1852 and AR-1853.
