---
{
  "branch": "docs/ar-1211-initial-setup",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1210"
  ],
  "id": "AR-1211",
  "next_action": "Implement the syntax-checked tutorial for ASB initialization, first-agent registration, and agent connection setup.",
  "observed_branch": "docs/ar-1211-initial-setup",
  "observed_dirty": 0,
  "observed_head": "6b36fb08e74ddd5a04eacd500ba0a0b25731519d",
  "owner": "",
  "plan": "../plans/AR-1211.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "done",
  "summary": "Teach first-time users to initialize ASB and add the first agent connection.",
  "task_revision": 5,
  "title": "Initial setup and first agent connection tutorial",
  "updated_at": "2026-09-22T14:45:43+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1211"
}
---

Implement the linked tutorial and offline syntax fixtures. Do not run the tutorial commands or
connect to an agent service in CI.

- 2026-09-22T14:45:42+00:00: Dependency AR-1210 done; initial-setup-v1.json contract merged via PR
  #240 and current main green.

- 2026-09-22T14:45:42+00:00: Claimed by asb_tui_tutorial_20260922.

- 2026-09-22T14:45:43+00:00: Verified: initial-setup-v1.json merged via PR #240 (6b36fb0) on main;
  validator test test_initial_setup_tutorial_contract present; exact-main quality green.
