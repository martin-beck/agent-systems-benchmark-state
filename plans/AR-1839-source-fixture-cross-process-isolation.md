# AR-1839 plan: cross-process source fixture isolation

1. Read the complete ASB development and quality documentation and reproduce
   the concurrent-process `source_checkout` failure at the reviewed head.
2. Trace fixture repository/staging naming, locks, cleanup, and process
   boundaries; preserve exact source identity and bounded fail-closed errors.
3. Implement the smallest process-safe isolation repair with positive,
   negative, and concurrent regression coverage.
4. Run focused repeated, full workspace, formatting, lint, and applicable
   hosted gates; obtain independent exact-head review.
5. Publish and merge only through the established signed-DCO integration path,
   then verify exact-main workflows and reconcile durable state.
