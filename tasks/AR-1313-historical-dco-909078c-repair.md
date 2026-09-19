---
{
  "branch": "repair/ar-1313-historical-dco-909078c",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1313",
  "next_action": "Promote after task review; perform a forward-only signed DCO recovery for historical merge 909078c without rewriting published history, then run exact-main policy and post-merge gates.",
  "owner": "",
  "plan": "../plans/AR-1313.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Repair the historical unsigned merge that blocks exact-main policy evidence.",
  "task_revision": 1,
  "title": "Historical DCO merge-integrity recovery",
  "updated_at": "2026-09-19T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1313-historical-dco-909078c"
}
---

# AR-1313

Repository quality rejects historical merge `909078ced21f36e5a72590c9decf41ac56452212`
because it lacks a matching `Signed-off-by`. Repair the protected-main boundary using the
project's forward-only signed recovery pattern. Preserve the published historical object and
tree; never rewrite or mislabel that merge as signed. This AR owns only the ASB repository and
coordination evidence, not asb-tui or Agent Workflow Quality.

Acceptance requires a signed, DCO-bearing recovery that makes the exact current main policy path
green, independent review, exact-head CI, protected merge, and post-merge verification. If the
repository policy cannot be repaired without a separate approved history mechanism, leave this AR
blocked with the exact failure and do not weaken the policy.
