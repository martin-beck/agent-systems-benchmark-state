---
{
  "branch": "repair/ar-1747-coordinator-unblock-vendor",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T18:17:08+00:00",
  "depends_on": [],
  "id": "AR-1747",
  "next_action": "Promote and claim; synchronize the reviewed upstream Coordinator development identity that adds provenance-checked unblock, then qualify the complete ASB state vendor closure and blocked-task transition fixtures.",
  "owner": "codex-asb-ar1747-vendor-20261008",
  "plan": "../plans/AR-1747-coordinator-unblock-vendor-adoption.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1747.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Adopt the official Coordinator development unblock capability in ASB state so AR-1722 can be reopened through a supported provenance-checked transition.",
  "task_revision": 3,
  "title": "Adopt Coordinator unblock support for AR-1722",
  "updated_at": "2026-10-08T16:17:08+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1747-coordinator-unblock-vendor"
}
---

ASB state currently vendors Coordinator v0.3.57, whose `resume` command accepts
only a valid pause snapshot. AR-1722 is externally blocked and has no pause
snapshot, so it cannot be reopened safely with the installed command set.
Upstream development commit `e863b57edc7f7a21b2aff2c7b45ce226e12637d2`
(tree `eee603591b917eeca244425559d7c67bb88a7268`) contains the independently
reviewed provenance-checked `unblock` transition and its complete formal vendor
closure. This AR owns exact adoption and downstream qualification; it must not
fabricate a pause, edit AR-1722 directly, or change ASB product runtime code.

- 2026-10-08T16:15:59+00:00: Official upstream Coordinator e863b57 already contains the reviewed
  unblock repair; exact downstream development vendor adoption is dependency-ready and path-isolated
  from AR-1746.

- 2026-10-08T16:17:08+00:00: Claimed by codex-asb-ar1747-vendor-20261008.
