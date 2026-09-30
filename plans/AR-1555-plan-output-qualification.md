# AR-1555 plan: plan and output workflow qualification

1. Review the exact merged heads from AR-1552 through AR-1554.
2. Execute a clean local/mock journey using a catalog-selected workload.
3. Execute the same journey with `--json` and machine-validate every response.
4. Test a synthetic catalog extension and confirm plan creation discovers it.
5. Run workspace/quality gates, update docs and durable receipts, then close
   only with exact-head review and hosted checks.
