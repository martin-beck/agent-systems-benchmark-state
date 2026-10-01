# AR-1611 — integrated dev-channel TUI install and launch

Implement and qualify the ASB-owned `asb tui install` path against the current
dev-channel main heads. It must clone/build in a disposable temporary location,
verify the selected source identity, atomically publish the executable and
manifest, preserve the previous install on failure, and launch through the
existing trusted router. Default output is human-readable; `--json` is opt-in.

Acceptance requires a fresh-user install, repeat install/upgrade, interrupted
build rollback, status/doctor, and launch transcript with exact source and
binary digests. Development auth/signature/key material is warning-only.
