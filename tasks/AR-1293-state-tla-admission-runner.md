---
{
  "branch": "feature/ar-1293-state-tla-admission",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1293",
  "next_action": "Create a truthful state-repository worktree, audit formal/handoffctl/verify.sh callers, and implement or prove the missing bounded tools/tlc_runner.py interface without touching handoffctl or product code.",
  "observed_branch": "feature/ar-1293-state-tla-admission",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1293.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Repair the state-repository TLA admission runner and truthful worktree metadata.",
  "task_revision": 2,
  "title": "State-scoped TLA admission runner",
  "updated_at": "2026-09-17T04:42:32+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1293-tla-admission"
}
---

## AR-1293

AR-1181 identified a coordination boundary defect: state formal/handoffctl
verification references `tools/tlc_runner.py`, but the task points at an ASB
product worktree and no state runner exists. This successor owns only truthful
state metadata and bounded runner implementation. It must not edit product code,
modify or extract handoffctl, weaken formal verification, or touch asb-tui.

- 2026-09-17T04:42:32+00:00: State-scoped runner successor is independent of product ARs and repairs
  the truthful worktree boundary.
