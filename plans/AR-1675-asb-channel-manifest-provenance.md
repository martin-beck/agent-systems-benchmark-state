# AR-1675 — ASB channel manifest and current-main provenance

Define the small, versioned channel manifest consumed by ASB and asb-tui. It
must identify channel, repository, resolved commit, source/build digest, and
development-only status. The dev resolver must point to the current configured
main head and reject stale, malformed, or mismatched manifests with typed
diagnostics.

Acceptance includes deterministic fixtures for valid dev, stale head, digest
mismatch, unavailable stable/nightly/experimental channels, and redacted
human/JSON projections.
