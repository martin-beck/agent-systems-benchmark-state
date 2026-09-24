---
{
  "branch": "feature/ar-1369-control-backend-authority-materialization",
  "checkpoint_commit": "0c6dc52e1f4aa5854f73081711dbd9a5bc1a5d7c",
  "claim_expires": "2026-09-24T02:48:42+00:00",
  "depends_on": [
    "AR-1362",
    "AR-1364",
    "AR-1366"
  ],
  "id": "AR-1369",
  "next_action": "Promote and claim the missing ControlBackend authority materialization, then persist authenticated chain/target/tool/lease/relay state for the receipt source.",
  "observed_branch": "feature/ar-1369-control-backend-authority-materialization",
  "observed_dirty": 0,
  "observed_head": "0c6dc52e1f4aa5854f73081711dbd9a5bc1a5d7c",
  "owner": "codex-asb-runtime-attested-enrollment-luna56",
  "plan": "../plans/AR-1369-control-backend-authority-materialization.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Materialize authenticated live-provider authority in ControlBackend for runtime receipt issuance.",
  "task_revision": 4,
  "title": "ControlBackend authority materialization",
  "updated_at": "2026-09-24T00:48:42+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1369-control-backend-authority-materialization"
}
---

Narrow successor for the missing control-owned source found by AR-1368. Do not
touch asb-tui or synthesize authority from CLI/config input.

- 2026-09-24T00:48:25+00:00: Promote durable ControlBackend authority materialization successor
  after AR-1368 source audit.

- 2026-09-24T00:48:28+00:00: Claimed by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-24T00:48:42+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.
