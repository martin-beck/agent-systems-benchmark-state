# AR-1560 plan

1. Reproduce the exact Ruff-format failure.
2. Apply only the pinned formatter's deterministic rewrite.
3. Run Ruff, mypy, coordinator tests and generated-state checks.
4. Verify hosted Coordination verification on the exact repaired main.
