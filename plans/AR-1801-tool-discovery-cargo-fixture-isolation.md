# AR-1801 plan: tool-discovery Cargo fixture isolation

1. Reproduce the full-workspace failure from AR-1772 and identify ambient Cargo
   inheritance or fixture cleanup causing the mismatch.
2. Isolate the version probe with a deterministic pinned fixture while keeping
   native command and bounded-output behavior intact.
3. Add positive and negative tests for unavailable, valid, and malformed probes;
   run focused and full ASB CLI quality gates.
4. Complete independent review, exact-head CI, signed merge, and post-merge
   verification against the AR-1762 dependency.
