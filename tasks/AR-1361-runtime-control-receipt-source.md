---
{
  "branch": "feature/ar-1361-runtime-control-receipt-source",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-24T01:03:18+00:00",
  "depends_on": [
    "AR-1359"
  ],
  "id": "AR-1361",
  "next_action": "Promote after AR-1359 is done, then add an authenticated control receipt source and runtime-owned dispatch factory without exposing authority to CLI.",
  "observed_branch": "feature/ar-1361-runtime-control-receipt-source",
  "observed_dirty": 0,
  "observed_head": "be9af3d6fb22818e95f51b9640b10c5eb6e043f3",
  "owner": "codex-asb-runtime-attested-enrollment-luna56",
  "plan": "../plans/AR-1361-runtime-control-receipt-source.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide authenticated control receipt delivery and runtime-owned dispatch composition for CLI consumers.",
  "task_revision": 4,
  "title": "Runtime control receipt source",
  "updated_at": "2026-09-23T23:03:47+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1361-runtime-control-receipt-source"
}
---

Successor for blocked AR-1360. Do not touch asb-tui or let the CLI construct
provider target, policy, tool, lease, relay, namespace, credential, or token
authority.

- 2026-09-24T00:00:00+00:00: Created after AR-1360 audit found that the merged
  receipt ingestion bridge has no authenticated ControlClient source and no
  runtime-owned cross-crate dispatch factory. AR-1360 remains blocked.

- 2026-09-23T23:03:15+00:00: Promote missing authenticated control receipt source and runtime-owned
  dispatch factory; dependency AR-1359 is merged and fully verified.

- 2026-09-23T23:03:18+00:00: Claimed by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T23:03:47+00:00: Recorded command exit 0; command argv SHA-256
  7a064b06d86f07bff0c3c51b85a1ba223dcae4dab0490c3fcddd167240a05bbe.
