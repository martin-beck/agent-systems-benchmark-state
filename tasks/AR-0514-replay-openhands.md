---
{
  "branch": "feature/replay-openhands",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T09:00:09+00:00",
  "depends_on": [
    "AR-0309",
    "AR-0503",
    "AR-0504",
    "AR-0401"
  ],
  "id": "AR-0514",
  "next_action": "Prove credential-free record/replay conformance for OpenHands with network denial and malformed/tool/cancel negatives.",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-0514.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify replay conformance for OpenHands.",
  "task_revision": 3,
  "title": "Qualify OpenHands replay",
  "updated_at": "2026-09-08T07:00:09+00:00",
  "worktree_key": "agent-systems-benchmark-replay-openhands"
}
---
## AR-0514

Qualify OpenHands record/replay, network denial, parity, retries, tool calls, cancellation, and malformed-record failures.

- 2026-09-08T07:00:07+00:00: AR-0309 is durably done at 52f884b; AR-0503, AR-0504 and AR-0401
  verified done. Promoted highest-priority ready OpenHands replay qualification.

- 2026-09-08T07:00:09+00:00: Claimed by contracts_20260906.
