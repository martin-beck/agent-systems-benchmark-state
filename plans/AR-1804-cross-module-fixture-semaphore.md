# AR-1804 plan: cross-module fixture semaphore

1. Reproduce AR-1801/AR-1803 failures under the repository’s default parallel
   Cargo test harness and inventory every process-backed fixture module.
2. Design one test-only, bounded, cross-module admission primitive that limits
   child-process and mutable-fixture concurrency without changing runtime
   authority, production behavior, or public contracts.
3. Add positive and hostile contention tests for queue bounds, cancellation,
   timeout, cleanup, semaphore exhaustion, and no leaked descendants/roots.
4. Run focused, default parallel `asb-cli`, and workspace gates repeatedly;
   publish via independent review, exact-head CI, signed merge, and post-merge
   verification before releasing AR-1801.
