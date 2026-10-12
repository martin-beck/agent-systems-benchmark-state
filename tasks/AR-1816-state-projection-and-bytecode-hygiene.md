---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T14:40:50+00:00",
  "depends_on": [],
  "id": "AR-1816",
  "next_action": "Implement a lock-aware, atomic reconciliation path and bytecode-safe coordinator execution, then qualify recovery under concurrent state activity.",
  "owner": "ar1816_projection_hygiene",
  "plan": "../plans/AR-1816-state-projection-and-bytecode-hygiene.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1816.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Repair recurring stale ASB coordinator projections and generated Python bytecode that breaches the state-file size guard.",
  "task_revision": 3,
  "title": "Coordinator projection and bytecode hygiene recovery",
  "updated_at": "2026-10-12T12:40:50+00:00",
  "worktree_key": ""
}
---

# AR-1816 — Coordinator projection and bytecode hygiene recovery

Repair the ASB coordinator-state failure mode where `handoffctl doctor --live`
reports stale generated `PROJECT_STATE.md` and `WORKTREES.md`, and where Python
execution writes `tools/__pycache__/handoffctl*.pyc` large enough to violate the
state-file size guard. This is a coordinator repair, not a product-output or
channel-implementation task; AR-1674 remains the owner of the ASB project
channel contract.

The implementation must keep generated views derived-only. It must serialize
or retry reconciliation safely around the existing coordinator lock, publish a
matched projection set atomically, and make all supported coordinator entry
points bytecode-safe without relying on every caller remembering an environment
variable. Existing developer workflows must retain explicit typed lock-timeout
diagnostics rather than silently racing or treating a partial render as valid.

Acceptance requires deterministic unit/fault tests for lock contention,
interrupted rendering, stale projection detection/recovery, and bytecode
suppression or redirection; an integration test must demonstrate clean
`reconcile`, `snapshot`, and `doctor --live` from a configured primary state
checkout while concurrent mutation is either serialized or clearly rejected.
No generated projection may be edited manually, and no tracked/untracked
bytecode, credentials, or host-private runtime configuration may enter commits.

- 2026-10-12T12:40:20+00:00: dependencies verified; begin projection and bytecode hygiene repair

- 2026-10-12T12:40:50+00:00: Claimed by ar1816_projection_hygiene.
