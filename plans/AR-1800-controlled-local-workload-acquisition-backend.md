# AR-1800 plan: controlled local workload acquisition backend

1. Define a repository-owned credential-free fixture archive server or equivalent
   bounded acquisition seam that maps each AR-1781 development workload ID to a
   pinned archive and evaluator entrypoint without changing production sources.
2. Add positive and hostile tests for catalog identity, digest/revision binding,
   offline-after-install, stale/revoked/mismatched records, interrupted
   acquisition, update/repair/remove, and acquisition-versus-benchmark failures.
3. Run the public `asb workload install`, selection, run, sweep, report, and
   compare journey for every AR-1781 development workload, including SWE-mini,
   using only the controlled backend and bounded local/mock execution.
4. Publish privacy-safe identity evidence and exact-main hosted qualification;
   then resume AR-1780 for the final every-ID acceptance.
