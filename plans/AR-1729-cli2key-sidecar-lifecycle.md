# AR-1729 — cli2key sidecar and ephemeral-key lifecycle

Add the runtime supervisor, private channel, readiness handshake, endpoint and
executable binding, cancellation, process-group cleanup, and redacted receipt.
Reject non-loopback listeners, substituted executables/configuration, symlinks,
weak permissions, stale readiness, orphaned descendants, and secret-shaped
output. Persist only non-secret references and digests.
