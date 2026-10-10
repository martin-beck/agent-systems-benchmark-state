# AR-1779 plan: default usable tool-install command

1. Replace required source/version/kind input for supported IDs with catalog
   resolution; retain explicit development/import syntax separately.
2. Orchestrate verified reuse, prebuilt retrieval, source fallback, project
   dependency materialization, atomic registration, and adapter smoke check.
3. Add idempotent status/repair/update/remove behavior with no download or build
   on inspection and complete receipt/provenance visibility.
4. Render clear status/progress and source/build choice through the shared output
   facilities while preserving JSON/quiet/privacy contracts.
5. Run fresh-project supported-tool install journeys on deterministic
   local primary-source fixtures and at least one opt-in official-source path;
   prove every failure leaves no false usable record.
