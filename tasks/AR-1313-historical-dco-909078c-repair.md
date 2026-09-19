---
{
  "branch": "repair/ar-1313-historical-dco-909078c",
  "checkpoint_commit": "68afee85219a30a9754c462042b3bc48a19a4ae9",
  "claim_expires": "2026-09-19T10:01:04+00:00",
  "depends_on": [],
  "id": "AR-1313",
  "next_action": "Keep PR #231 unmerged; route one-line workspace coverage deficit to AR-1312, then rerun exact-head checks and signed recovery merge.",
  "observed_branch": "repair/ar-1313-historical-dco-909078c",
  "observed_dirty": 0,
  "observed_head": "8e5598eab3b35a56fb8997bdd73dfd73f89f5cdc",
  "owner": "ar1313-dco-recovery",
  "plan": "../plans/AR-1313.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Forward-only signed DCO recovery candidate published as PR #231.",
  "task_revision": 10,
  "title": "Historical DCO merge-integrity recovery",
  "updated_at": "2026-09-19T08:04:11+00:00",
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

- 2026-09-19T07:49:55+00:00: Heartbeat by ar1313-dco-recovery.

- 2026-09-19T07:56:42+00:00: Heartbeat by ar1313-dco-recovery.

- 2026-09-19T07:57:11+00:00: Prepared empty-tree forward-only SSH-signed commit
  68afee85219a30a9754c462042b3bc48a19a4ae9 on current main 78a8e9fc2144623311e315fcc4e46c2831b0b2c1.
  Historical unsigned merge 909078ced21f36e5a72590c9decf41ac56452212 remains unchanged and
  preserved. Candidate tree equals current main; matching Signed-off-by verified; repository_policy
  --base origin/main --head HEAD passed; merge_pr focused tests passed 9/9. Initial direct unittest
  module invocation failed due operator import form, then signature policy discovery passed 16/16.
  Published PR #231; headers green, remaining exact-head checks in progress. Handoff command
  executed product mutation but state replication reported it requires the main checkout; state
  heartbeat/update recorded from main checkout.

- 2026-09-19T08:01:04+00:00: Heartbeat by ar1313-dco-recovery.

- 2026-09-19T08:04:11+00:00: Repository quality run 35430672372 failed only at cargo llvm-cov
  --locked --workspace --all-targets --fail-under-lines 90. Full TOTAL: 52,704 total lines, 5,271
  missed, displayed 90.00% but exact ratio is 89.9988615665%, so fail-under-lines correctly exited
  1. One additional covered line would reach 90% (5,270 missed => 90.000758%). This is the known
  post-AR-1310 baseline owned by AR-1312, not the empty-tree AR-1313 recovery. Do not weaken
  threshold or merge.
