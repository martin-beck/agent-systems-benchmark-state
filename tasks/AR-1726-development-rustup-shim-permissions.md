---
{
  "branch": "repair/ar-1726-development-rustup-shim-permissions",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T00:42:10+00:00",
  "depends_on": [
    "AR-1634",
    "AR-1636",
    "AR-1637"
  ],
  "id": "AR-1726",
  "next_action": "Promote after dependency verification; implement the bounded development-only permission exception, focused hostile-path tests, and exact paired installed lifecycle qualification.",
  "observed_branch": "repair/ar-1726-development-rustup-shim-permissions",
  "observed_dirty": 1,
  "observed_head": "f535e3cb327b99b35bae2ddae9f0086b3c211303",
  "owner": "codex-ar1726-rustup",
  "plan": "../plans/AR-1726-development-rustup-shim-permissions.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1726.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Make development asb tui installation accept a conventional user-owned 0775 rustup shim path with an explicit warning while preserving hard stable and production trust boundaries.",
  "task_revision": 9,
  "title": "Allow user-owned group-writable rustup shim in development",
  "updated_at": "2026-10-07T22:45:34+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1726-development-rustup-shim-permissions"
}
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

- 2026-10-07T22:37:38+00:00: Dependencies AR-1634, AR-1636, and AR-1637 are done. User authorized
  the bounded development-only 0775 rustup shim exception; promote implementation and paired
  qualification.

- 2026-10-07T22:42:10+00:00: Claimed by codex-ar1726-rustup.

- 2026-10-07T22:42:29+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-10-07T22:42:54+00:00: Recorded command exit 0; command argv SHA-256
  ad5023ea3aab7e906a3bd6149245b11179886f084e63677dbcbd7ea34b00dfa9.

- 2026-10-07T22:45:02+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-07T22:45:34+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.
