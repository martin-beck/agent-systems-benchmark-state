# AR-1601 — development-channel publication and provenance qualification

Qualify the protected-main development channel as the single current-main
source for the TUI installer.  The default channel must be `dev`; future
channels remain explicit choices and unsupported channels must return typed,
human-readable diagnostics with `--json` available.  The published result must
retain exact ASB/TUI commit, tree, and executable identities and must not expose
credentials.

Dependencies: ASB AR-1600, ASB AR-1599, and asb-tui AR-1588.  This is a
cross-repository qualification gate, not a replacement for either implementation.

Required evidence: disposable fresh-clone install, exact source/tree/digest
provenance, default-dev and explicit-channel negative cases, status/doctor
validation, cleanup, independent review, hosted checks, and post-merge
verification.  Development-only missing authentication, signatures, and key
management remain warning-only; stable/production paths remain fail-closed.
