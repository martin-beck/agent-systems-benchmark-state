---
{
  "branch": "repair/ar-1799-tui-install-rustup-invalid",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T15:23:22+00:00",
  "depends_on": [
    "AR-1738",
    "AR-1636"
  ],
  "id": "AR-1799",
  "next_action": "Reproduce the installed-entrypoint failure on the exact current ASB main head, then repair the failing rustup/rustc path and add regression coverage.",
  "observed_branch": "repair/ar-1799-tui-install-rustup-invalid",
  "observed_dirty": 0,
  "observed_head": "a0a978f134959943c54362e84032a6232c606105",
  "owner": "codex-ar1799-tui-install-rustup-invalid-20261012",
  "plan": "../plans/AR-1799-tui-install-rustup-invalid-repair.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "environmental",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1799.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1799.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Repair the remaining current-main asb tui install trusted_tool_invalid failure for development rustup/rustc layouts and qualify the real installed entrypoint.",
  "task_revision": 4,
  "title": "Repair asb tui install rustup/rustc trusted-tool rejection",
  "updated_at": "2026-10-12T13:25:41+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1799-tui-install-rustup-invalid"
}
---

The merged permission compatibility repairs are not sufficient if the actual
`asb tui install` entrypoint still returns `trusted_tool_invalid`. Reproduce
that exact failure against current protected ASB main using a disposable HOME,
the conventional rustup shim/toolchain layout, and the affected permission or
ownership variants. Trace the typed error to its real validator, repair the
development-only path without weakening stable/production trust boundaries, and
make permission/ownership findings warning-only as already specified for
development. Preserve hard failures for path traversal, symlink substitution,
malformed settings, missing tools, and toolchain pairing races.

The acceptance target is the installed-entrypoint journey (`asb tui install`,
then status/launch or the documented no-provider qualification), not only an
isolated preflight helper. No API key, signature, or key-management artifact
may block development qualification or enter durable state.

- 2026-10-12T13:23:02+00:00: Open P0 repair for the reproduced user-visible asb tui install
  trusted_tool_invalid failure.

- 2026-10-12T13:23:22+00:00: Claimed by codex-ar1799-tui-install-rustup-invalid-20261012.
