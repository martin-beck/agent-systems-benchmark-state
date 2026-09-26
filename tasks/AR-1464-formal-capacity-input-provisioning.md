---
{
  "branch": "repair/ar-1464-formal-capacity-input-provisioning",
  "checkpoint_commit": "ab485f767fbddbd8adfc27b5120f3df0a045b762",
  "claim_expires": "2026-09-26T23:12:57+00:00",
  "depends_on": [],
  "id": "AR-1464",
  "next_action": "Provision and verify the exact signed AR-1307 source bundle, reviewed Ubuntu image, canonical seed and admission lock, 64 GiB overlay and at least 1 GiB available host swap; then hand the immutable inputs to AR-1308.",
  "owner": "coordinator-ar1464-formal-capacity",
  "plan": "../plans/AR-1464.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provision the missing signed formal inputs and disposable capacity required by AR-1308.",
  "task_revision": 5,
  "title": "Formal capacity and signed-input provisioning repair",
  "updated_at": "2026-09-26T21:13:07+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1464-formal-capacity-input-provisioning"
}
---

This P0 repair owns only the missing infrastructure and immutable input
assembly identified by the AR-1308 preflight. It must not weaken AR-1307's
3G memory/3G swap/2-worker/2-core/8G/7200s contract, alter the formal model,
or claim qualification. All source, image, seed, lock, JDK/TLC and runner
artifacts must be digest-pinned, signed or otherwise reviewed under the
existing state policy, stored under `/srv/data/projects`, network-disabled at
execution, and privacy-safe. No ASB product or asb-tui source changes are in
scope.

- 2026-09-26T21:12:00+00:00: Created from AR-1308's terminal preflight:
  28 KiB host swap free, no reviewed Ubuntu image, ~3.5 GiB overlay instead of
  64 GiB, missing exact signed AR-1307 `ab485f767` source/tree, seed and
  canonical admission lock. No VM/TLC run was attempted.

- 2026-09-26T21:12:35+00:00: Provision exact formal inputs and disposable capacity identified by
  AR-1308 preflight.

- 2026-09-26T21:12:38+00:00: Claimed by coordinator-ar1464-formal-capacity.

- 2026-09-26T21:12:57+00:00: Heartbeat by coordinator-ar1464-formal-capacity.

- 2026-09-26T21:13:07+00:00: Recorded command exit 0; command argv SHA-256
  0ed28ab2d231d0b2bd8ef8fcc7c11bb59995fd48770e67cf2eb8a98065389117.
