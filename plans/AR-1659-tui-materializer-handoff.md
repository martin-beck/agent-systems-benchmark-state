# AR-1659 — atomic TUI materializer and launch handoff

Provide the ASB-owned runner for `asb tui install`: clone the selected channel,
build the exact TUI revision in a temporary directory, validate its manifest,
atomically install it, and launch it with the versioned control handoff.
Exercise failure cleanup, rollback, remove, and incompatible-manifest diagnostics.

The development runner may use generated fixtures and warning-only identity,
signature, and key-management status.
