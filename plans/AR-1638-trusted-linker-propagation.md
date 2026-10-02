# AR-1638 — Trusted linker-tool propagation

Make the ASB development materializer resolve and propagate validated linker
tools required by Cargo build scripts in the cleared environment. Use explicit
validated tool paths only; do not restore ambient PATH or allow arbitrary
environment inheritance.

Acceptance:

- Reproduce the missing `cc` failure in a disposable clean-room root.
- Resolve validated `cc` and, where required, `ar` paths with ownership, permissions, absolute-path, and bounded parent checks.
- Propagate only explicit `CC`/`AR` values and no ambient PATH.
- Fresh TUI dev install reaches successful materialization; later lifecycle gates remain unchanged.
- Focused/full tests, independent review, hosted checks, and paired qualification pass.
