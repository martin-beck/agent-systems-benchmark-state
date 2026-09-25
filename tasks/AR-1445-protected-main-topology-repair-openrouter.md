---
{
  "branch": "repair/ar-1445-protected-main-topology-repair-openrouter",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T16:03:27+00:00",
  "depends_on": [],
  "id": "AR-1445",
  "next_action": "Create a signed+DCO reviewed descendant PR whose GitHub merge has two parents and preserves the exact current main tree/contract; require exact-head CI and all seven post-merge workflows before closing AR-1440.",
  "observed_branch": "repair/ar-1445-protected-main-topology-repair-openrouter",
  "observed_dirty": 0,
  "observed_head": "10686db7ceb5f023aaef13cd1ed1b6cc58118a55",
  "owner": "ar1445-topology-repair-luna56",
  "plan": "../plans/AR-1445.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair the single-parent protected-main merge produced for the OpenRouter model refresh.",
  "task_revision": 11,
  "title": "Protected-main topology repair for OpenRouter refresh",
  "updated_at": "2026-09-25T14:03:27+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1445-protected-main-topology-repair-openrouter"
}
---

PR #323 changed the OpenRouter free-model pin and added the catalog-bound
operator measurement helper, but its merge commit `84b587ec` has only one
parent. The protected-main repository policy requires a two-parent merge whose
first parent is the exact reviewed base and whose merged tree equals the
reviewed topic tree. Preserve the failed post-merge evidence; do not waive or
weaken that gate.

Create the smallest reviewed descendant change needed to exercise the normal
non-squash protected merge path from the current main tip. Keep the model pin,
selection contract, local-only measurement boundary, and credential/privacy
guarantees unchanged. Require signed+DCO commits, exact-head required checks,
independent review, and all seven exact-main post-merge workflows. After the
repair is green, update and release AR-1440 with both merge-topology and
measurement evidence.

- 2026-09-25T13:59:37+00:00: Post-merge policy run 36144090160 proved PR 323 merged as single-parent
  84b587ec; begin reviewed topology repair without weakening gates.

- 2026-09-25T13:59:47+00:00: Claimed by ar1445-topology-repair-luna56.

- 2026-09-25T14:00:09+00:00: Recorded command exit 0; command argv SHA-256
  e9528bf8d96b5e6e0d3ac7b08a1584c099ecd0a19e62a4d150fdbf1defcf78ae.

- 2026-09-25T14:01:08+00:00: Heartbeat by ar1445-topology-repair-luna56.

- 2026-09-25T14:02:23+00:00: Recorded command exit 0; command argv SHA-256
  8b07a5698a0a16f696959ef182d13fcfe4b28ef67bda04d60c47f22035caf8d9.

- 2026-09-25T14:02:45+00:00: Recorded command exit 0; command argv SHA-256
  a24a8b3d94321101903d50d02906f5a04eac026c5e782c2b70c439ba9ac4e8af.

- 2026-09-25T14:03:07+00:00: Recorded command exit 0; command argv SHA-256
  d7cc2db8c6cffa19a9b0bb23e79987a3a6d13bb553cda1f29de43addf8b6c9b5.

- 2026-09-25T14:03:27+00:00: Heartbeat by ar1445-topology-repair-luna56.
