# AR-1849 plan: formal admission environment repair

Repair the hosted formal workflow so every command that can execute TLC,
including the full unittest step, receives the runner-private admission queue
and lock. Preserve the formal model, resource bounds, and fail-closed runner.

1. Add workflow-wide private `TLC_ADMISSION_QUEUE` and `TLC_ADMISSION_LOCK`.
2. Add positive and negative tests proving the private absolute lock contract.
3. Run focused and full state gates, independently review, and publish a PR.
4. Requalify dependent AR-1841 only after exact-head CI is terminal green.
