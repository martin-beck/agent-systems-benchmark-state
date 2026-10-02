# AR-1640 — TUI nested-build linker contract

Extend the standalone TUI development materializer to consume the bounded
toolchain contract established by ASB AR-1639. A nested TUI build must work
with private validated `git`, `setsid`, Cargo, compiler, archive, and auxiliary
linker tools while ambient `PATH` remains unavailable.

Acceptance:

- Reproduce the current private-tool/cleared-PATH nested-build failure.
- Propagate or resolve validated absolute `CC`, `AR`, `LD`, Rust linker, and
  target linker flags without inheriting ambient environment.
- Reject relative, missing, writable, symlinked, or untrusted tool overrides.
- Fresh ASB installation followed by nested TUI build succeeds under the
  cleared development environment.
- Focused/full tests, independent review, hosted checks, and exact paired
  lifecycle qualification pass.

Development-only authentication, signatures, and key management remain
warning-only and never block this prototype path.
