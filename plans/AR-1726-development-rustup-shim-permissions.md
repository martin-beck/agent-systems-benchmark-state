# AR-1726 Development rustup shim permission compatibility

Repair the development-only `asb tui install` toolchain resolver so a conventional
user-owned rustup layout remains usable when `~/.cargo` and `~/.cargo/bin` are
group-writable but not world-writable. Preserve strict stable and production
trust policy.

## Scope

- Resolve the default toolchain from the bounded validated rustup home.
- Accept group-write only for current-user-owned development shim ancestors and
  emit a stable warning in human and JSON responses.
- Continue rejecting world-writable, non-user-owned, symlinked-parent, escaping,
  missing, malformed, or substituted Cargo/rustc paths.
- Add focused resolver, rustc propagation, warning, race/substitution, and
  negative tests.
- Qualify exact paired `asb tui install`, `status`, bare `asb tui`, upgrade, and
  removal against current ASB and asb-tui heads.

## Integration

Use the existing development resolver and lifecycle. Do not add an ambient PATH
fallback, a second installer, or a stable/production policy exception. Require
independent exact-head review, protected merge, and terminal-green post-merge CI.
