---
{
  "branch": "repair/ar-1836-tui-qualification-determinism",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-13T21:38:15+00:00",
  "depends_on": [
    "AR-1835"
  ],
  "id": "AR-1836",
  "next_action": "Promote after AR-1835 dependency resolution; reproduce the two hosted failures with complete workflow metadata, identify the owning workflow/asb-tui seam, and implement only a deterministic qualification repair without weakening the gate.",
  "observed_branch": "repair/ar-1837-pr627-protected-main-identity",
  "observed_dirty": 0,
  "observed_head": "6ea3648e483f25179c3112b54ed7c348e141cad4",
  "owner": "ar1836-tui-qual-luna",
  "plan": "../plans/AR-1836-cross-repo-tui-qualification-determinism.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1836.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Repair the deterministic cross-repository Exact TUI inherited-fd/PTY qualification seam exposed by AR-1835 without weakening its assertions.",
  "task_revision": 6,
  "title": "Cross-repository Exact TUI qualification determinism",
  "updated_at": "2026-10-13T19:39:38+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1837-pr627-protected-main-identity"
}
---

AR-1835/PR #627 exact head `06565d3de95aa72fa67bf2fde73078753acfd49b` is
blocked by the required Exact TUI inherited-fd and PTY journey. Hosted jobs
115063830052 and 115065450191 both failed at `crates/asb-cli/src/tui.rs:6127`
with `Run Control did not dispatch offline default after readiness`, followed
by the test unwrap at line 6182. The PR changes only `control.rs` and the
generated diagnostic catalog; it does not touch `tui.rs`.

The exact ignored test passed locally through handoffctl with the complete
workflow inputs (`ASB_TUI_BINARY`, expected digest, source commit, and source
tree). An incomplete local invocation failed closed on missing source metadata,
confirming the harness inputs are required. This AR owns only the workflow or
cross-repository contract seam and must not alter unrelated TUI behavior,
waive the check, serialize it away, or accept mutable/unverified binaries.

- 2026-10-13: Created as a narrow P0 successor dependent on AR-1835 after two
  identical hosted failures versus a complete-metadata local pass; PR #627
  remains merge-blocked.

- 2026-10-13: Dependency audit: handoffctl promotion is fail-closed unless
  every dependency is `done` (or an explicitly completed supersession chain).
  AR-1835 remains `in_progress` while PR #627 has a terminal-failed required
  check, so AR-1836 must remain planned and ownerless; do not claim or start a
  replacement worker before AR-1835 reaches a dependency-satisfying state.

- 2026-10-13T19:37:30+00:00: AR-1835 is now done with signed protected-main merge and post-merge
  receipt; promote dependency-ready qualification repair.

- 2026-10-13T19:38:00+00:00: Claimed by ar1836-tui-qual-luna.

- 2026-10-13T19:38:15+00:00: Heartbeat by ar1836-tui-qual-luna.

- 2026-10-13T19:38:49+00:00: Bound worktree
  agent-systems-benchmark-ar-1837-pr627-protected-main-identity on branch
  repair/ar-1836-tui-qualification-determinism.
