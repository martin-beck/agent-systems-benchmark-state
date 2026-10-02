# AR-1670 — exact Coordinator authority vendoring closure

Compare the ASB state checkout with the signed Coordinator v0.3.53 release,
restore the required authority adapters, role registry, lifecycle/rollback
stores, and upgrade dependencies byte-for-byte, and reconcile the allowlist and
provenance. Validate source headers, immutable vendor hashes, mypy, Ruff,
schema checks, and live coordinator doctor evidence.
