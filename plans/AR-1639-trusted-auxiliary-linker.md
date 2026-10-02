# AR-1639 — Trusted auxiliary linker resolution

Complete the cleared development linker contract when GCC needs auxiliary
tools such as `ld`, without restoring ambient PATH. Resolve or stage a bounded,
validated auxiliary linker configuration (for example an explicit `-B` root or
trusted wrapper) and preserve private ownership, stable behavior, and typed
development diagnostics.

Acceptance:

- Reproduce the exact `collect2: cannot find 'ld'` failure under empty PATH.
- Select a safe, explicit auxiliary-linker solution using validated absolute
  paths and no arbitrary environment inheritance.
- Fresh TUI dev installation succeeds through materialization under the cleared environment.
- Focused/full tests, independent review, hosted checks, and paired lifecycle qualification pass.
