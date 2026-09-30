# AR-1561 plan

1. Reproduce and classify missing-module versus real typing failures.
2. Add minimal typed boundaries or precise ignores only where optional modules
   are intentionally absent; preserve runtime fail-closed behavior.
3. Run Ruff, mypy, coordinator tests, coverage and generated-state checks.
4. Verify hosted Coordination verification on the exact repaired main.
