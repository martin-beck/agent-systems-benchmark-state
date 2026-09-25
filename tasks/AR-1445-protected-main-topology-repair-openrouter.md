---
{
  "branch": "repair/ar-1445-protected-main-topology-repair-openrouter",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1445",
  "next_action": "Create a signed+DCO reviewed descendant PR whose GitHub merge has two parents and preserves the exact current main tree/contract; require exact-head CI and all seven post-merge workflows before closing AR-1440.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1445.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Repair the single-parent protected-main merge produced for the OpenRouter model refresh.",
  "task_revision": 1,
  "title": "Protected-main topology repair for OpenRouter refresh",
  "updated_at": "2026-09-25T00:00:00+00:00",
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
