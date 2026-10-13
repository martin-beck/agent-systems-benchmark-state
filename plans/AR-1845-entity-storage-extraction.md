# AR-1845 plan: entity and storage extraction

1. Enumerate the concrete entities used by setup, catalog discovery,
   configuration, selection, plan compilation, validation, execution, process
   launch, recording/replay, results, reporting, and comparison.
2. Extend the generated registry with storage kind and lifecycle metadata for
   files, structured documents, environment variables, argv/options, runtime
   messages, catalogs, cassettes, and result artifacts.
3. Instrument or derive field-to-entity reads, writes, transforms, and
   validations from the implementation. Keep API keys as references/digests and
   redact values and sensitive host paths.
4. Exercise deterministic fixtures through the complete lifecycle and assert
   that every model field has an explainable entity relation.
5. Preserve the existing explicit-config and development safety contracts and
   obtain independent review.
