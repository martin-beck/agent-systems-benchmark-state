# AR-1626 — ASB/TUI control-loop PTY repair

Repair the exact-main development launch failure found by AR-1615. Keep the
direct TUI PTY path and the ASB broker/control child loop separately tested;
make private XDG/socket roots bounded and launchable without requiring
production authentication, signatures, or key management. Add positive and
negative tests for launch, polling, shutdown, and socket-path diagnostics,
then rerun the paired lifecycle qualification without weakening gates.
