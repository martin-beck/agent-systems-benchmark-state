# AR-1631 Cross-repository development-channel binding

Bind the ASB command surface and separately published asb-tui to one explicit
release-channel contract. A fresh `dev` install must materialize the selected
TUI source, preserve the channel in lifecycle state, and expose the same
channel in status/launch/help projections. Unsupported channels remain typed
and unavailable; they must not silently fall back.

Development fixtures may use generated credentials and signatures. Missing
authentication, signature validation, and key management are warning-only in
development and must never block this contract.

Acceptance: exact current-main ASB and TUI heads pass paired contract tests,
including channel propagation, persistence, JSON projection, and unavailable
channel diagnostics.
