---
{
  "branch": "feature/asb-tui-compatibility-detection",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1017"],
  "id": "AR-1018",
  "next_action": "Implement platform, architecture, ASB-version, protocol, and terminal capability detection.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1018.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Detect whether an asb-tui bundle is compatible before installation or launch.",
  "task_revision": 1,
  "title": "Add asb-tui compatibility and terminal capability detection",
  "updated_at": "2026-09-10T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-compatibility-detection"
}
---
Detect OS/distribution, architecture, ASB version, protocol version, exact coordinator and
workflow-quality release compatibility, terminal dimensions/features,
SSH/tmux/screen context, and filesystem/runtime requirements. Select only compatible bundles and fail
closed with actionable diagnostics for unsupported combinations.

Acceptance criteria: deterministic machine-readable capability report, resize/channel tests, negative
fixtures for mismatches, privacy-safe diagnostics, and no host identifiers in public artifacts.
