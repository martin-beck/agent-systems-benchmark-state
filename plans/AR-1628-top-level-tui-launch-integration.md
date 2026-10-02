# AR-1628 — Top-level ASB/TUI launch integration repair

Repair the exact current-main mismatch where `asb tui launch --channel dev`
successfully establishes broker/provisioning sockets and terminal handoff but
the current TUI exits with status 2 immediately after terminal initialization.
Trace the typed control context and render-policy transition across the
top-level route, add an exact paired integration test using current protected
heads, and rerun the complete AR-1615 lifecycle journey. Keep development
authentication, signatures, and key management warning-only.
