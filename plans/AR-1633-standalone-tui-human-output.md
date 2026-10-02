# AR-1633 Standalone TUI human-output parity

Make direct asb-tui lifecycle commands human-readable by default, with
explicit `--json` (or the established opt-in JSON spelling) for machine
consumers. Install, status, launch, upgrade, remove, doctor, and failure
diagnostics must use the same bounded channel/provenance vocabulary as the ASB
router. Existing JSON callers remain compatible.

Development-only missing authentication, signatures, and key management must
be visible warnings and never block the prototype.
