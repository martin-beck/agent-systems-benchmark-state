---
{
  "branch": "feature/ssh-remote-bootstrap",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T05:18:58+00:00",
  "depends_on": [
    "AR-0803",
    "AR-0804"
  ],
  "id": "AR-0819",
  "next_action": "Implement OpenSSH host selection, service probing, stdio bridging, and explicit passwordless enrollment.",
  "owner": "replay_20260909",
  "plan": "../plans/AR-0819.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Use configured SSH hosts as the safe default path to a remote runner and help establish dedicated key authentication.",
  "task_revision": 5,
  "title": "Add SSH remote discovery and bootstrap",
  "updated_at": "2026-09-09T03:19:19+00:00",
  "worktree_key": "agent-systems-benchmark-ssh-remote-bootstrap"
}
---
## AR-0819

Use configured SSH hosts as the safe default path to a remote runner and help establish dedicated key authentication.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-09T03:18:52+00:00: Dependencies AR-0803 and AR-0804 are done; promote SSH remote bootstrap
  as the next highest-priority implementable track.

- 2026-09-09T03:18:55+00:00: Claimed by replay_20260909.

- 2026-09-09T03:18:58+00:00: Heartbeat by replay_20260909.

- 2026-09-09T03:19:19+00:00: Recorded command exit 0; command argv SHA-256
  5624c9837a58856e6fa3911d3b5dc8c8d53afbcc1bb42042cfb083f5c1222cd1.
