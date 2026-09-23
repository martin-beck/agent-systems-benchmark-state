---
{
  "branch": "feature/ar-1340-attested-live-relay-handoff",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-23T11:59:44+00:00",
  "depends_on": [
    "AR-1339"
  ],
  "id": "AR-1340",
  "next_action": "Promote after AR-1339 is done; implement the attested namespace-bound relay handoff and descendant-egress denial evidence for AR-1329 to consume.",
  "owner": "codex-asb-ar1340-20260923",
  "plan": "../plans/AR-1340.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Bind the live provider relay to an attested child namespace and integrate it without weakening offline or replay denial.",
  "task_revision": 4,
  "title": "Attested live-relay namespace and child handoff",
  "updated_at": "2026-09-23T09:59:44+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1340-attested-live-relay-handoff"
}
---

AR-1339 supplies a bounded runtime relay primitive, but AR-1329 still lacks the
runtime-owned namespace and child handoff that makes the relay authoritative.
This AR provisions an attested private loopback or Unix endpoint inside the
approved live child namespace, keeps the live relay capability distinct from
`NetworkPolicy::Deny`, proves denial for children and descendants, and then
wires the guarded capability into `asb run` and `asb sweep --live-provider`.
Offline/default and strict-replay paths must remain network-denied and must not
receive the live capability. No API key or other credential may appear in
public coordination state or runtime evidence.

- 2026-09-23T09:58:42+00:00: AR-1339 is done at protected main 229941f; promote namespace-bound
  handoff work before final AR-1329 CLI integration.

- 2026-09-23T09:59:01+00:00: Claimed by codex-asb-ar1340-20260923.

- 2026-09-23T09:59:44+00:00: Heartbeat by codex-asb-ar1340-20260923.
