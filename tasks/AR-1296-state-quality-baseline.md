---
{
  "branch": "repair/ar-1296-state-quality-baseline",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1296",
  "next_action": "Repair explicit tools package identity and add bounded offline upgrade-command coverage until strict mypy and the unchanged 95% coverage gate pass.",
  "observed_branch": "repair/ar-1296-state-quality-baseline",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1296.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Restore strict state-repository mypy and coverage quality gates without weakening thresholds.",
  "task_revision": 2,
  "title": "State quality-gate baseline",
  "updated_at": "2026-09-17T05:18:02+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1296-quality"
}
---

## AR-1296

AR-1295 exposed pre-existing state quality failures: strict mypy cannot resolve
the `tools` package consistently, and coverage is 84% because upgrade command
modules have no tests. This AR owns only package identity and bounded tests; it
must not lower quality thresholds, suppress imports, touch product/asb-tui, or
alter handoffctl semantics without tests.

- 2026-09-17T05:18:02+00:00: Strict mypy and unchanged coverage floor expose deterministic state
  quality gaps; promote independent repair.
