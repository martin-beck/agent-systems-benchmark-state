# AR-1636 — Trusted rustc path propagation

Make the ASB development materializer resolve and propagate a validated rustc
toolchain executable path alongside the validated rustup home and cargo path.
The cleared child environment must remain bounded, user-owned, and free of
ambient PATH widening. Stable/production trust boundaries and development
non-blocking authentication/signature/key behavior must remain unchanged.

Acceptance:

- Reproduce the missing `rustc -vV` failure in a disposable clean-room root.
- Resolve rustc only from the validated rustup/toolchain root or an explicitly validated private tool override.
- Fresh TUI dev install succeeds, then status/launch/upgrade/restart/remove pass.
- Focused and full ASB tests, independent review, and hosted checks pass.
