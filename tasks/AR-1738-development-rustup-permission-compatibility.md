---
{
  "branch": "repair/ar-1738-development-rustup-permission-compatibility",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1726", "AR-1734"],
  "id": "AR-1738",
  "next_action": "Claim an isolated worktree, reproduce current-main trusted_tool_invalid for RUSTUP_HOME, implement warning-only development permission/ownership handling, and requalify the exact paired lifecycle without changing stable or production policy.",
  "owner": "",
  "plan": "../plans/AR-1738-development-rustup-permission-compatibility.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1738.json",
  "spec_revision": 1,
  "status": "open",
  "summary": "Allow development rustup shim and RUSTUP_HOME permission/ownership findings with warnings instead of trusted_tool_invalid, while preserving path-shape and stable/production boundaries.",
  "task_revision": 1,
  "title": "Repair permissive development rustup permission acceptance",
  "updated_at": "2026-10-08T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1738-development-rustup-permission-compatibility"
}
---

The current-main development installer still reports `trusted_tool_invalid`
when the rustup shim or `RUSTUP_HOME` has permission/ownership properties that
are safe enough for this explicitly local development path. For this AR,
permission and ownership findings are warning-only in development, including
world-writable and non-user-owned fixtures as requested. Keep absolute,
non-escaping, non-malformed, and non-symlink path-shape validation; do not
weaken stable or production installation policy.

