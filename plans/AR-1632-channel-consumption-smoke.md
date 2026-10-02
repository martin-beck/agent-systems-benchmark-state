# AR-1632 Clean-room development-channel consumption smoke

Using the AR-1631 contract, execute a disposable fresh-clone journey that
installs the default `dev` channel, starts the TUI, persists the selected
channel across restart, upgrades from a pinned older dev revision, and reports
bounded rollback/tamper diagnostics. Verify the same journey through human
output and opt-in `--json` projections.

No live provider or production key chain is required: generated development
fixtures and local/mock execution are valid, and absent authentication,
signatures, or key management must never block the prototype.
