# AR-1796 plan: concurrent integration liveness

1. Replace stale-base-as-blocked guidance with a retryable integration state.
2. Separate material product changes from generated coordinator projections;
   reuse exact candidate evidence when the reviewed product tree is unchanged.
3. Define one serialized protected-main admission lane that validates the
   merge-result tree, instead of forcing every worker to race rebases.
4. Add an enforceable coordinator/integration implementation AR and tests for
   queueing, retry, liveness, and no duplicate publication.
5. Preserve independent review, signatures, DCO, privacy, merge-result checks,
   and exact-main post-merge assurance.
