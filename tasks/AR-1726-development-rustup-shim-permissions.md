---
{"id":"AR-1726","title":"Allow user-owned group-writable rustup shim in development","priority":"P0","depends_on":["AR-1634","AR-1636","AR-1637"],"plan":"../plans/AR-1726-development-rustup-shim-permissions.md","summary":"Make development asb tui installation accept a conventional user-owned 0775 rustup shim path with an explicit warning while preserving hard stable and production trust boundaries.","status":"planned","next_action":"Promote after dependency verification; implement the bounded development-only permission exception, focused hostile-path tests, and exact paired installed lifecycle qualification.","owner":"","claim_expires":"","checkpoint_commit":"","worktree_key":"agent-systems-benchmark-ar-1726-development-rustup-shim-permissions","branch":"repair/ar-1726-development-rustup-shim-permissions","observed_branch":"","observed_head":"","observed_dirty":0,"schema_version":1,"spec_ref":"specs/AR-1726.json","spec_revision":1,"task_revision":1,"updated_at":"2026-10-08T00:45:00+02:00"}
---

This is a development-only compatibility repair. The current host has a regular,
current-user-owned Rust 1.93 Cargo/rustc toolchain beneath a conventional rustup
shim, while `~/.cargo` and `~/.cargo/bin` are mode 0775. The user explicitly
authorized that layout for development execution.

Accept only current-user-owned group-writable shim ancestors and surface a
development warning. World-writable, non-user-owned, symlinked-parent, escaping,
missing, malformed, or substituted paths remain hard failures. Stable and
production installation policy is unchanged.

Completion requires focused positive and hostile-path tests, exact paired
ASB/asb-tui install/status/bare-launch/upgrade/remove evidence, independent
review, protected merge, and terminal-green post-merge CI.
