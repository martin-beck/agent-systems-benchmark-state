---
{
  "branch": "fix/formal-tla-artifact-availability",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0003", "AR-0901", "AR-0902"],
  "id": "AR-0877",
  "next_action": "Verify an authoritative durable TLA+ 1.8.0 release asset and design the digest-checked online/offline acquisition boundary before implementation.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-0877.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Repair the formal workflow's unavailable TLA+ artifact pin without weakening provenance or offline verification.",
  "task_revision": 1,
  "title": "Repair formal TLA artifact availability",
  "updated_at": "2026-09-09T00:53:00+00:00",
  "worktree_key": "agent-systems-benchmark-formal-tla-artifact-availability"
}
---
## AR-0877

Replace the TLA+ release-asset URL that returns HTTP 404 with an authoritative, durable,
content-verified acquisition and offline-cache boundary. Preserve all positive and deliberate
mutation formal checks.

Implementation has not started. Read the linked plan before claiming.

