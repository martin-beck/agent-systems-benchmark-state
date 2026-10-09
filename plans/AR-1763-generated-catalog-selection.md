# AR-1763 plan: generated catalogs

1. Map discovered tool capabilities and existing ASB catalog formats into the
   AR-1759 catalog-reference contract.
2. Implement deterministic generation, content-addressed storage, metadata
   persistence, list/show/select, and compatibility validation.
3. Add stale, duplicate, unsupported, digest mismatch, and repeat-generation
   fixtures plus human/JSON CLI tests.
4. Verify no credentials or private host paths enter generated catalogs.
