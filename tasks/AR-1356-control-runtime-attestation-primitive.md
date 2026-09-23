---
{
  "branch": "feature/ar-1356-control-runtime-attestation-primitive",
  "checkpoint_commit": "726f4ccd1a20ce4e9bbf4abf819a1f0e3446fb15",
  "claim_expires": "2026-09-23T23:06:07+00:00",
  "depends_on": [
    "AR-1352"
  ],
  "id": "AR-1356",
  "next_action": "Reuse authenticated asb-control enrollment/certificate contracts to define and verify a bounded control-to-runtime attestation, then issue the opaque runtime capability needed by AR-1355.",
  "observed_branch": "feature/ar-1356-control-runtime-attestation-primitive",
  "observed_dirty": 0,
  "observed_head": "726f4ccd1a20ce4e9bbf4abf819a1f0e3446fb15",
  "owner": "codex-asb-runtime-acquisition-successor-luna56",
  "plan": "../plans/AR-1356-control-runtime-attestation-primitive.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Issue runtime-owned live enrollment capability from authenticated control attestation.",
  "task_revision": 3,
  "title": "Control/runtime enrollment attestation primitive",
  "updated_at": "2026-09-23T21:06:07+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1356-control-runtime-attestation-primitive"
}
---

Successor for AR-1355's missing trust primitive. Preserve fail-closed live
dispatch and do not expose caller-supplied launch authority.

- 2026-09-23T21:06:04+00:00: Promote P0 authenticated control/runtime attestation primitive; AR-1355
  documented missing issuer and remains blocked, AR-1329 fail-closed.

- 2026-09-23T21:06:07+00:00: Claimed by codex-asb-runtime-acquisition-successor-luna56.
