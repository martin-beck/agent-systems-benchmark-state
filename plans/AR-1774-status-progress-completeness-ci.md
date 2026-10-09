# AR-1774 plan: status and progress completeness CI

1. Derive command, step, and public-renderer coverage from authoritative types,
   dispatch inventory, and reporter construction rather than a drift-prone list.
2. Add static/mechanical checks rejecting direct public output/status writes,
   missing `-q`, missing output-router use, unregistered steps, invalid tokens,
   and bypassed reporter construction.
3. Add fake-clock and PTY controlled-defect tests for the one-second threshold,
   live updates, terminal cleanup, ETA integrity, terminal resizing, interruption,
   cancellation, errors, warnings, partial results, and broken writers.
4. Add every-route stream tests asserting strict JSON silence on both streams and
   quiet silence, plus terminal color and redirected plain-text behavior.
5. Run a long-operation fixture with deterministic local delays/substeps instead
   of network timing; prove bounded and indeterminate reporting separately.
6. Make the checks required in PR and protected-main CI, document the extension
   workflow, and accept only after independent exact-head/exact-main evidence.
