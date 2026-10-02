# AR-1628 — Top-level ASB/TUI launch integration repair

Repair the bootstrap-stage mismatch where the current TUI exited with status 2
after broker/provisioning sockets and terminal handoff were established. The
merged fix skips unsupported lifecycle polls for unavailable development
catalog entries while retaining those choices. The remaining post-bootstrap
15-second top-level progression timeout is tracked separately by AR-1629.

Keep development authentication, signatures, and key management warning-only.
