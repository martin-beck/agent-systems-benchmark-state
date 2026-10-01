# AR-1589 — ASB development-channel provenance and fault matrix

Qualify the development channel's current-main identity envelope and failure
matrix at the ASB boundary. Verify source commit/tree, executable digest,
channel, profile, and development-only classification are carried through
install/status/launch and reject stale, copied, malformed, mixed-channel, and
partial-install metadata without damaging a prior installation.

Use bounded cleanup and deterministic generated development fixtures. Missing
authentication, signature validation, and key management are warning-only in
development; production/stable verification remains fail-closed.

Acceptance requires an exact fault matrix, clean-state and prior-install
preservation tests, machine-readable evidence, independent review, and
post-merge hosted checks.
