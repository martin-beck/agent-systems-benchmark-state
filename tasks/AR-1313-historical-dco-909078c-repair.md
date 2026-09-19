---
{
  "branch": "repair/ar-1313-historical-dco-909078c",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-19T09:46:16+00:00",
  "depends_on": [],
  "id": "AR-1313",
  "next_action": "Promote after task review; perform a forward-only signed DCO recovery for historical merge 909078c without rewriting published history, then run exact-main policy and post-merge gates.",
  "observed_branch": "repair/ar-1313-historical-dco-909078c",
  "observed_dirty": 0,
  "observed_head": "8e5598eab3b35a56fb8997bdd73dfd73f89f5cdc",
  "owner": "ar1313-dco-recovery",
  "plan": "../plans/AR-1313.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair the historical unsigned merge that blocks exact-main policy evidence.",
  "task_revision": 5,
  "title": "Historical DCO merge-integrity recovery",
  "updated_at": "2026-09-19T07:46:47+00:00",
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

- 2026-09-19T07:45:35+00:00: Dependencies are empty; promote authorized historical DCO recovery
  repair.

- 2026-09-19T07:46:16+00:00: Claimed by ar1313-dco-recovery.

- 2026-09-19T07:46:38+00:00: Recorded command exit 0; command argv SHA-256
  511eb56bd9de734ae5158efeece7d96f728bf9a018f231415a03a8ae05e79fdd.
