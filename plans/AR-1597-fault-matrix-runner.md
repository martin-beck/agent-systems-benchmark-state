# AR-1597 — fault matrix and deterministic runner

Create the approved runner and fault matrix for setup, provider connection,
recording, replay, benchmark, comparison, cancellation, stale-generation,
missing-auth, missing-signature, and cleanup cases. The runner must emit
human-readable evidence by default and machine-readable evidence only with
`--json`.

Dependencies: AR-1596. Downstream: paired TUI AR-1596 and final qualification.

Required evidence: isolated runner, matrix manifest, bounded timeouts,
failure classification, cleanup assertions, exact-head receipts, signed/DCO
PR, independent review, and hosted checks.
