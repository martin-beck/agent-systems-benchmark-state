# AR-1802 plan: controlled workload matrix and fixture authority

1. Restrict fixture acquisition to an explicit development-only authority and
   preserve production/network and catalog identity boundaries.
2. Add positive and hostile tests for archive size, URL/catalog digest, revision,
   evaluator mismatch, missing/unsafe fixtures, and acquisition-vs-benchmark
   failure separation.
3. Qualify every AR-1781 development workload through install, select, run,
   sweep, report, and compare, then repeat the post-setup journey offline.
4. Record bounded privacy-safe evidence, obtain independent review, exact-head
   CI, signed merge, and post-merge verification before AR-1800 acceptance.
