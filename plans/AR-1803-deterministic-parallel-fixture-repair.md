# AR-1803 plan: deterministic parallel fixture repair

1. Reproduce the AR-1801 full-gate failures under the exact signed head and
   retain the command, assertion, and parallel-load evidence.
2. Identify shared fixture, environment, temporary-root, or process ownership
   state causing the `left 6/right 0` outcomes in provider-selection and
   comparison tests.
3. Add the smallest bounded credential-free isolation repair with positive and
   negative tests; preserve public contracts and fail closed on setup errors.
4. Run focused affected tests repeatedly, then the full `asb-cli` and workspace
   gates under parallel execution. Publish through independent review, exact-
   head CI, and protected merge only when every gate is green.
