---
{
  "branch": "fix/formal-tla-artifact-availability",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T04:01:25+00:00",
  "depends_on": [
    "AR-0003",
    "AR-0901",
    "AR-0902"
  ],
  "id": "AR-0877",
  "next_action": "Verify an authoritative durable TLA+ 1.8.0 release asset and design the digest-checked online/offline acquisition boundary before implementation.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "replay_20260906",
  "plan": "../plans/AR-0877.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair the formal workflow's unavailable TLA+ artifact pin without weakening provenance or offline verification.",
  "task_revision": 4,
  "title": "Repair formal TLA artifact availability",
  "updated_at": "2026-09-09T01:01:44+00:00",
  "worktree_key": "agent-systems-benchmark-formal-tla-artifact-availability"
}
---
## AR-0877

Replace the TLA+ release-asset URL that returns HTTP 404 with an authoritative, durable,
content-verified acquisition and offline-cache boundary. Preserve all positive and deliberate
mutation formal checks.

Implementation has not started. Read the linked plan before claiming.


- 2026-09-09T01:01:21+00:00: Dependencies AR-0003, AR-0901, and AR-0902 are done; owned formal
  acquisition paths are disjoint from active AR-0806 TUI, AR-0855 state vendor, and AR-0876
  provider-launch scopes. Promote for the blocking TLA+ artifact availability repair.

- 2026-09-09T01:01:25+00:00: Claimed by replay_20260906.

- 2026-09-09T01:01:44+00:00: Recorded command exit 0; command argv SHA-256
  dd885d3beb1c7712be2c40fc7a268651d94964934cea87ee439edf2d698d0f77.
