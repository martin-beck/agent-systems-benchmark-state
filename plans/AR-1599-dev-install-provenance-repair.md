# AR-1599 — development install provenance and toolchain repair

Repair the ASB development-channel materializer so a fresh user can resolve
the current ASB/asb-tui main heads, build in a disposable temporary directory,
and atomically publish the required launcher/runtime files without depending
on `/usr/bin/cargo` or embedding stale checkout identities.  Preserve the
selected `dev` channel as the default and keep stable/nightly/experimental
explicit and fail-closed until their contracts exist.

Dependencies: AR-1563, AR-1564, AR-1568, AR-1588.  Downstream: TUI AR-1599,
ASB AR-1598.

Required evidence: exact source/tree provenance, toolchain discovery from the
trusted environment, bounded clone/build output and cleanup, atomic replacement
with rollback, offline/negative-path tests, signed/DCO PR, independent review,
hosted checks, and post-merge fresh-main verification.  Development fixtures
must remain non-blocking for missing authentication, signatures, and key
management; production validation remains fail-closed.
