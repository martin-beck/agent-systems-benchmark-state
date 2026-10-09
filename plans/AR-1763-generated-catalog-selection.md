# AR-1763 plan: generated catalogs

1. Start only after AR-1769 makes fine-grained, actionable human diagnostic
   coverage a required gate for every new public command and failure/warning.
2. Map discovered tool capabilities and existing ASB catalog formats into the
   AR-1759 catalog-reference contract.
3. Implement deterministic generation, content-addressed storage, metadata
   persistence, list/show/select, and compatibility validation.
4. Add stale, duplicate, unsupported, digest mismatch, and repeat-generation
   fixtures plus human/JSON CLI tests.
5. Verify no credentials or private host paths enter generated catalogs.
