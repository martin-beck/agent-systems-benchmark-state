---
{
  "branch": "feature/one-line-local-install",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T08:29:58+00:00",
  "depends_on": [
    "AR-0803",
    "AR-0804",
    "AR-0805",
    "AR-0820"
  ],
  "id": "AR-0821",
  "next_action": "Create the missing declared worktree from exact origin/main, then implement and test the guided installation workflow.",
  "owner": "codex-longrun-one-line-install-20260909",
  "plan": "../plans/AR-0821.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Turn a single documented command into a safe guided local ASB and TUI first run.",
  "task_revision": 7,
  "title": "Add guided one-line local installation",
  "updated_at": "2026-09-09T06:30:30+00:00",
  "worktree_key": "agent-systems-benchmark-one-line-install"
}
---

## AR-0821

Turn a single documented command into a safe guided local ASB and TUI first run.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-09T06:29:46+00:00: Dependencies AR-0803, AR-0804, AR-0805, and AR-0820 are released done;
  promote guided one-line installation as the next actionable P1 track. AR-0704 remains
  authorization-gated and AR-0832 remains native-capacity-gated.

- 2026-09-09T06:29:52+00:00: Claimed by codex-longrun-one-line-install-20260909.

- 2026-09-09T06:29:58+00:00: Heartbeat by codex-longrun-one-line-install-20260909.

- 2026-09-09T06:30:11+00:00: Recorded command exit 1; command argv SHA-256
  78d7942e237f6cd1e3138a4ba81d7a545221768e49381e07ac9757d8363bdf9c.

- 2026-09-09T06:30:27+00:00: First worktree observation failed: declared path
  /srv/data/projects/agent-systems-benchmark-one-line-install was absent and no matching live
  worktree was listed. No product mutation occurred; creating the declared isolated worktree is
  required before implementation.

- 2026-09-09T06:30:30+00:00: Recorded command exit 0; command argv SHA-256
  25e5fe5d71720f64e877ee7a599da60d2c9f070238bca30155d0e145bc6c6aed.
