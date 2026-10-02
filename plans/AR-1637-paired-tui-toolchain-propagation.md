# AR-1637 — Paired TUI toolchain propagation

Ensure ASB's installed TUI lifecycle passes the validated development toolchain
contract to nested asb-tui materialization without relying on ambient PATH,
RUSTC, or RUSTUP_HOME. Keep environment clearing, private roots, channel
provenance, and production trust boundaries intact.

Acceptance:

- Exact ASB/TUI heads pass nested install, status, launch, restart, upgrade, and remove.
- Only validated development toolchain values cross the broker boundary.
- Human and JSON diagnostics remain consistent and development-only auth/signature/key absence is warning-only.
- Independent review, hosted checks, and final paired qualification pass.
