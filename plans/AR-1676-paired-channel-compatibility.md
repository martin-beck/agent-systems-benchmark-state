# AR-1676 — Paired ASB/TUI channel compatibility matrix

Run the same channel cases through the ASB CLI/router and standalone TUI:
omitted channel (default `dev`), explicit `dev`, future channel names, restart
persistence, upgrade, rollback, remove, malformed manifest, and unavailable
channel. Record exact ASB/TUI heads and manifest digests in a durable receipt.

The runner must assert identical typed diagnostics and human/JSON semantics,
while treating development-only credential and authenticity warnings as
non-blocking.
