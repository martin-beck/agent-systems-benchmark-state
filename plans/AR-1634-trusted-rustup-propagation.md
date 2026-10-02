# AR-1634 Trusted development rustup propagation

Repair the ASB development materializer so a trusted user-owned rustup
toolchain can build the current asb-tui after the child environment is cleared.
Resolve and validate a bounded development-only rustup home (with an explicit
override for CI), propagate it to the cargo subprocess, and preserve the
existing trusted parent-chain and workspace-quota checks. Direct untrusted
PATH execution remains rejected.

Cover a fresh install with the current TUI main, then status/upgrade/remove,
using generated local fixtures. Missing authentication, signatures, and key
management remain warning-only and never block development.
