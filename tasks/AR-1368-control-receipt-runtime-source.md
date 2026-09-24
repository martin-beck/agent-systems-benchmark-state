---
{
  "branch": "feature/ar-1368-control-receipt-runtime-source",
  "checkpoint_commit": "0c6dc52e1f4aa5854f73081711dbd9a5bc1a5d7c",
  "claim_expires": "",
  "depends_on": [
    "AR-1366",
    "AR-1340",
    "AR-1339",
    "AR-1328"
  ],
  "id": "AR-1368",
  "next_action": "Promote and claim the missing runtime-owned ControlClient receipt source, then add the authenticated control operation and production enrollment materialization without exposing authority.",
  "observed_branch": "feature/ar-1368-control-receipt-runtime-source",
  "observed_dirty": 0,
  "observed_head": "0c6dc52e1f4aa5854f73081711dbd9a5bc1a5d7c",
  "owner": "",
  "plan": "../plans/AR-1368-control-receipt-runtime-source.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Provide the authenticated runtime-owned ControlClient receipt source required by AR-1329 production dispatch.",
  "task_revision": 6,
  "title": "Control receipt runtime source",
  "updated_at": "2026-09-24T00:48:17+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1368-control-receipt-runtime-source"
}
---

Narrow successor for the source gap found by AR-1367. Do not touch asb-tui or
allow CLI/config callers to synthesize receipt authority.

- 2026-09-24T00:46:51+00:00: Promote missing authenticated ControlClient receipt source;
  dependencies AR-1366, AR-1340, AR-1339, and AR-1328 are complete.

- 2026-09-24T00:46:53+00:00: Claimed by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-24T00:47:51+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-24T00:48:09+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-24T00:48:17+00:00: Blocked truthfully after authenticated source audit: certificate
  request/response types exist and AR-1366 consumes them, but ControlCall/ControlClient has no
  receipt operation and ControlBackend has no authenticated chain or runtime target/tool/lease/relay
  materialization. No safe product mutation was made. Successor AR-1369 created for durable
  ControlBackend authority materialization; AR-1329 remains fail-closed.
