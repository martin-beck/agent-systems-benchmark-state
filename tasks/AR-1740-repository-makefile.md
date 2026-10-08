---
{
  "branch": "feature/ar-1740-repository-makefile",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1740",
  "next_action": "Promote after reviewing the pinned Cargo/toolchain commands and storage boundaries; implement and test the optional repository Makefile with dependency checks and safe build/install/clean/update/test targets.",
  "owner": "",
  "plan": "../plans/AR-1740-repository-makefile.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_ref": "specs/AR-1740.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Add an optional ASB repository Makefile that checks prerequisites and safely wraps build, install, clean, update, and test workflows.",
  "task_revision": 1,
  "title": "Add developer Makefile workflow",
  "updated_at": "2026-10-08T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1740-repository-makefile"
}
---

Developers currently need to remember individual Cargo, Rustup, Git, and quality
commands. Add a repository-root Makefile as an optional convenience layer for
common source workflows. It must check dependencies and explain remediation,
never install packages implicitly, preserve the pinned toolchain and locked
quality gates, and never become a runtime or installed-user dependency.

