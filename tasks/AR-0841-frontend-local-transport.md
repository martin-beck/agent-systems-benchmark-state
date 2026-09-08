---
{
  "branch": "feature/frontend-local-transport",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0840",
    "AR-0104"
  ],
  "id": "AR-0841",
  "next_action": "Implement bounded owner-only Unix-socket transport with peer checks and fail-closed framing.",
  "owner": "",
  "plan": "../plans/AR-0841.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Implement the local frontend control transport and authorization boundary.",
  "task_revision": 2,
  "title": "Implement frontend local transport",
  "updated_at": "2026-09-08T06:52:53+00:00",
  "worktree_key": "agent-systems-benchmark-frontend-local-transport"
}
---
## AR-0841

Implement length-prefixed JSON-RPC over an owner-only Unix socket with peer-credential checks,
bounded frames, deadlines, backpressure, and fail-closed protocol mismatch behavior. Do not bind
TCP implicitly.

- 2026-09-08T06:52:53+00:00: Promoted after AR-0840 PR #54 merged and dependency AR-0104 verified
  done; local transport implementation is path-disjoint and ready for a dedicated worker.
