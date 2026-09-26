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
  "task_revision": 16,
  "title": "Formal capacity and signed-input provisioning repair",
  "updated_at": "2026-09-26T21:17:14+00:00",
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

- 2026-09-26T21:13:26+00:00: Recorded command exit 0; command argv SHA-256
  a00daeb04eb8457c6b09b676f90fc96bb4017684b9666da4725e7e35499bd0eb.

- 2026-09-26T21:13:55+00:00: Recorded command exit 0; command argv SHA-256
  3d44ce891bef75d3f0b3972757ae869f385dedb01af176785cc5ff7240f3fd60.

- 2026-09-26T21:14:27+00:00: Recorded command exit 1; command argv SHA-256
  bb69a5e9071fd175408272dbfa67d57cac62c2168d12c8b707dae4d7e7145ce6.

- 2026-09-26T21:14:50+00:00: Recorded command exit 0; command argv SHA-256
  33efe247a4bde9723519d8b7359efa610e6ecb9d46b2885eeb9ddd9c8987975f.

- 2026-09-26T21:15:21+00:00: Recorded command exit 0; command argv SHA-256
  7f9bb8faedaf9a95b9bb54c73d552e7e205c2c405b568b22d87e6ec80d3ad26a.

- 2026-09-26T21:15:43+00:00: Recorded command exit 0; command argv SHA-256
  c4a16d26ad0679a4763593e416880695e694f9ecf9cb4414563f264d06a1ecd6.

- 2026-09-26T21:16:09+00:00: Recorded command exit 0; command argv SHA-256
  60f7d69654174c108c13adbcb29074f615dc58ec8ae54d87f5c104a3cb9741c9.

- 2026-09-26T21:16:24+00:00: Recorded command exit 0; command argv SHA-256
  2aa51383a66d6ad1b5229b2b6d9fb31a33f2ce0945fffb1b73d57e8c94da9406.

- 2026-09-26T21:16:38+00:00: Recorded command exit 0; command argv SHA-256
  669118dc240b84f3fc329b4a30399c9c855cc438ec5a9e2b02688ce0cd9e9bcd.

- 2026-09-26T21:16:54+00:00: Recorded command exit 1; command argv SHA-256
  ce42c369f0d189d31e740fe7870a183a2a0eb1a8fd293d7834aa3cf3d899b95b.

- 2026-09-26T21:17:14+00:00: Recorded command exit 0; command argv SHA-256
  5a9454aaa6303c1757c6d354a0442a5e03b8f5c9623365a3542d92a9243daa50.
