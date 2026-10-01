# AR-1592 — ASB control catalog compatibility

Implement the ASB-side common control contract consumed by the released
asb-tui development bootstrap: `BenchmarkCatalog` followed by
`MeasurementCatalog` at the negotiated version. Keep the change bounded to
protocol/schema validation, backend catalog publication, and compatibility
tests; do not claim the cross-repository journey until AR-1590 reruns it.

Required evidence:

- exact protocol version/call/result definitions and canonical validation;
- deterministic development catalogs with identity, revision, and digest;
- real `ControlBackend` responses and ordered request tests;
- unsupported-version and downgrade negatives;
- no authentication/signature/key-management blocking in development mode;
- exact signed/DCO PR, independent review, and green hosted checks.

Dependencies: AR-1576. Downstream: AR-1590.
