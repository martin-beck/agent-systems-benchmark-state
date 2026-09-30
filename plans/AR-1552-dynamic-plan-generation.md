# AR-1552 plan: dynamic workload-backed plan generation

1. Inventory the canonical workload registry, plan schema, measurement catalog,
   and existing fixture builders.
2. Implement a reusable selector/materializer over the canonical supported
   workload inventory; reject unavailable, methodology-only, duplicate, or
   malformed selections.
3. Generate a schema-valid plan with exact workload/scorer/content identities
   and deterministic defaults, without embedding credentials.
4. Add unit and integration tests proving current workloads are discovered and
   a newly registered workload is discoverable without CLI changes.
5. Document the contract and run focused plus workspace tests on an isolated
   product worktree.
