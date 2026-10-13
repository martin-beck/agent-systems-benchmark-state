# AR-1844 plan: data-model registry

1. Inventory the ASB Rust types and enums that define setup configuration,
   selections, plans, catalogs, credentials, execution, recording, results,
   reporting, and comparison.
2. Add one versioned introspection/registry contract derived from those types;
   each field records logical name, entity, owner, sensitivity, and allowed
   value kind while redacting API-key material and host secrets.
3. Generate the registry from the implementation or its authoritative schema,
   not from a second manually maintained field list. Add a completeness test.
4. Expose a stable machine-readable artifact for later storage and command-flow
   extraction, with human-readable names suitable for graph labels.
5. Run focused schema, privacy, and drift tests and obtain independent review.
