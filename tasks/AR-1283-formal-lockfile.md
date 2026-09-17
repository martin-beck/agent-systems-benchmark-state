---
{
  "branch": "feature/ar-1283-formal-lockfile",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0003"
  ],
  "id": "AR-1283",
  "next_action": "Promote after dependency verification; regenerate and verify formal/Cargo.lock so hosted --locked formal tests do not attempt updates.",
  "observed_branch": "feature/ar-1283-formal-lockfile",
  "observed_dirty": 0,
  "observed_head": "69e8b064d3121a4bae1f672cdae9c0c8672000bc",
  "owner": "",
  "plan": "../plans/AR-1283.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Repair formal workspace lockfile drift that fails the locked CI gate.",
  "task_revision": 7,
  "title": "Formal lockfile CI drift repair",
  "updated_at": "2026-09-17T00:49:39+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1283-formal-lockfile"
}
---

## AR-1283

Repair formal lockfile drift without weakening locked CI or changing formal behavior.

- 2026-09-17T00:46:57+00:00: PR #208 Loom failed before tests because formal/Cargo.lock is stale
  under cargo test --locked; repair the lockfile without weakening the gate.

- 2026-09-17T00:47:11+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-17T00:47:43+00:00: Recorded command exit 0; command argv SHA-256
  5c8da9b34935360f7399b9d4b260d9a460b442f2f0ca08eddaee6e8f11776ef0.

- 2026-09-17T00:49:13+00:00: Heartbeat by asb_ar1024_lifecycle_router.

- 2026-09-17T00:49:39+00:00: Diagnosis: clean fresh origin/main head
  69e8b064d3121a4bae1f672cdae9c0c8672000bc has no formal/Cargo.lock diff. The authoritative
  handoffctl-wrapped cargo test --locked --manifest-path formal/Cargo.toml completed exit 0; formal
  suites passed: unit 2/2, control_models 4/4, loom_ownership 2/2, production_trace 3/3,
  recovery_models 5/5, recovery_production 2/2, state_models 6/6, tla_artifact_acquisition 9/9,
  tla_image_identity 5/5, tla_source_build 4/4, toolchain_pins 1/1. Stale-lock failure is specific
  to PR #208 path-dependency changes and must be repaired on that exact feature head by its owner;
  no safe scoped mutation exists on unchanged main. Worktree clean, no product mutation. Next
  action: PR #208 owner regenerates formal/Cargo.lock and reruns locked formal gate.
