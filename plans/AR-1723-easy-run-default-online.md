# AR-1723 plan

Implement and qualify the shortest catalog-driven `asb run` path with the
configured live provider as its default. Local mock remains an explicit
`--local-mock` opt-in; live failures are typed and never fall back. Preserve
development warning-only authentication, signature, and key-management rules.

Use the current ASB head, exact provider/model identity, bounded workload,
human-readable default output, and explicit `--json` output. Record a
privacy-safe exact-head receipt and require independent review before merge.
