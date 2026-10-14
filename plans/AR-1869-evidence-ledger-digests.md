# AR-1869 plan: evidence-ledger digests

1. Verify the two failing ledgers and compute the exact current candidate digest.
2. Update only each ledger's candidate digest and matching mechanical step fields.
3. Run focused task-spec, schema, generated-view, and strict consistency gates.
4. Publish through signed review and exact-head CI; preserve all predicates and evidence references.
