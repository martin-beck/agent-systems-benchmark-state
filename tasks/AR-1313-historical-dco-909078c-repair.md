---
{
  "branch": "repair/ar-1313-historical-dco-909078c",
  "checkpoint_commit": "3420355d8a0855aea696775cfe85cc628773c842",
  "claim_expires": "2026-09-24T13:31:37+00:00",
  "depends_on": [],
  "id": "AR-1313",
  "next_action": "All PR #290 exact-head checks are green; obtain independent review, then run signed merge_pr.py against exact base e41d4df/head 3420355/tree e1120e9 and verify seven post-merge workflows.",
  "observed_branch": "repair/ar-1313-historical-dco-909078c",
  "observed_dirty": 0,
  "observed_head": "3420355d8a0855aea696775cfe85cc628773c842",
  "owner": "ar1313_recovery_luna56",
  "plan": "../plans/AR-1313.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Forward-only signed DCO recovery candidate published as PR #231.",
  "task_revision": 27,
  "title": "Historical DCO merge-integrity recovery",
  "updated_at": "2026-09-24T11:31:48+00:00",
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

- 2026-09-19T08:04:14+00:00: Blocked by exact hosted Repository quality run 35430672372: 52,704
  total lines, 5,271 missed; exact 89.9988615665% below unchanged 90% floor despite rounded 90.00%.
  One covered line is sufficient, and repair belongs to existing AR-1312. Preserve PR #231 at signed
  head 68afee85219a30a9754c462042b3bc48a19a4ae9, base 78a8e9fc2144623311e315fcc4e46c2831b0b2c1; do
  not merge until AR-1312 repairs coverage and all exact-head/post-merge gates are green. Historical
  merge 909078c remains preserved; no gate weakening.

- 2026-09-24T11:15:15+00:00: AR-1312 coverage repair is done and current main represents the old
  recovery tree; refresh PR #231 against current main and revalidate whether signed recovery is
  still required.

- 2026-09-24T11:17:43+00:00: Claimed by ar1313_recovery_luna56.

- 2026-09-24T11:18:35+00:00: Heartbeat by ar1313_recovery_luna56.

- 2026-09-24T11:20:08+00:00: Recorded command exit 0; command argv SHA-256
  a979daf9c86f1cc8b8b2629aaa380ada763680578704964da33a301a563e2558.

- 2026-09-24T11:20:23+00:00: Recorded command exit 0; command argv SHA-256
  3f139868c4559048fc72c83f8764f95381ce053413923cff9380ca121c8921ec.

- 2026-09-24T11:20:41+00:00: Heartbeat by ar1313_recovery_luna56.

- 2026-09-24T11:20:52+00:00: Recorded command exit 0; command argv SHA-256
  fc216a16f6653c07f61e1f04f494ac4b2c5a9240ed8b94b452f47cf0b026ad3a.

- 2026-09-24T11:21:41+00:00: Current protected main e41d4df was audited: historical unsigned merge
  909078c remains an ancestor, old PR #231 head 68afee8 is not an ancestor and is stale. Created
  current-main empty signed+DCO recovery 3420355d; tree equals e41d4df, signature and DCO verified,
  repository_policy --base origin/main --head HEAD passed, and merge_pr focused tests passed 11/11.
  No history rewrite or gate weakening.

- 2026-09-24T11:21:50+00:00: Recorded command exit 0; command argv SHA-256
  8c593b651bedbbe2f5d1bc6dbe6dfe678a271993ff0d51dd317b7fcda2e962d1.

- 2026-09-24T11:22:45+00:00: Heartbeat by ar1313_recovery_luna56.

- 2026-09-24T11:22:55+00:00: PR #290 created after stale PR #231 was proven based on old 78a8e9f.
  Exact base e41d4df and head 3420355; initial checks are running. The handoffctl PR command
  completed remotely but state lock timed out afterward; this update reconciles the durable
  evidence.

- 2026-09-24T11:26:46+00:00: Heartbeat by ar1313_recovery_luna56.

- 2026-09-24T11:31:37+00:00: Heartbeat by ar1313_recovery_luna56.

- 2026-09-24T11:31:48+00:00: PR #290 exact-head checks all passed: AWQ shadow, headers, Rust,
  emulated aarch64, repository quality (coverage and defect fixtures), fault, formal, hosted. No
  source diff; tree remains exactly e1120e9 (same as base). Independent review is still required
  before signed integration merge.
