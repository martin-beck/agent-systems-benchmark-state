# AR-1615 — live ASB–TUI control handshake and lifecycle repair

Repair and qualify the real ASB–TUI control handoff after the immutable
development bundle is installable. The installed TUI must negotiate the exact
control/catalog contract and expose record, seal, reopen, replay, compare,
retry, cancel, stale-session, and remove behavior through the live route, not
only fixture or source-level tests.

Development fixtures and generated identities are permitted and missing
production authentication, signatures, or key management must remain visible
non-blocking warnings. Protocol mismatches, stale handles, or unavailable
services must be typed, fail-closed, and explain the next action.

Required evidence: exact paired heads and protocol digest, live PTY/control
transcript, positive lifecycle path, retry/cancel/stale/remove negatives,
offline activation, no-secret output, independent review, hosted checks, and
exact-main post-merge verification.
