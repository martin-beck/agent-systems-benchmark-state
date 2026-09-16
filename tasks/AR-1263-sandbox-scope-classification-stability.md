---
{
  "branch": "fix/ar-1263-sandbox-scope-classification",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1238"
  ],
  "id": "AR-1263",
  "next_action": "Post-merge DCO recovery required: protected main ebfa37023e56 merged PR #205 but merge commit lacks Signed-off-by and GitHub RSA key is unverified locally. Preserve feature 0acbc1d and rerun exact-main policy after signed recovery.",
  "observed_branch": "fix/ar-1263-sandbox-scope-classification",
  "observed_dirty": 0,
  "observed_head": "0acbc1d1a8bf43a226fda503fbd76f8afd48eb07",
  "owner": "",
  "plan": "../plans/AR-1263.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Stabilize intermittent sandbox scope classification in the quality gate.",
  "task_revision": 51,
  "title": "Stabilize sandbox scope classification gate",
  "updated_at": "2026-09-16T22:07:50+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1263-sandbox-stability"
}
---

## AR-1263

Repair the existing timing-sensitive sandbox scope classification failure using deterministic,
fail-closed test/runner behavior and preserve the original semantic assertions.

- 2026-09-16T21:16:00+00:00: Created after independent 20-run reproduction found 7 intermittent
  failures at sandbox_boundary.rs line 474, unrelated to AR-1262 source paths.

- 2026-09-16T21:16:17+00:00: Promote independent runner stabilization after 20-run reproduction of
  existing sandbox scope flake.

- 2026-09-16T21:17:51+00:00: Claimed by asb_ar1263_sandbox_stability.

- 2026-09-16T21:17:53+00:00: Recorded command exit 0; command argv SHA-256
  0ed28ab2d231d0b2bd8ef8fcc7c11bb59995fd48770e67cf2eb8a98065389117.

- 2026-09-16T21:18:08+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-16T21:18:30+00:00: Recorded command exit 0; command argv SHA-256
  2c0848fa4854b685365b30913bb16b6313f76405665dd10e56892824a0262cce.

- 2026-09-16T21:18:51+00:00: Recorded command exit 0; command argv SHA-256
  b7b523a9e61c62735a56e239c20311c66f61a633c36f689672f2ec210a68c74e.

- 2026-09-16T21:19:00+00:00: Recorded command exit 0; command argv SHA-256
  588a5eba29d08049941925ddd30e80a35755c500a87d141629914298348aa333.

- 2026-09-16T21:19:12+00:00: Recorded command exit 101; command argv SHA-256
  61fa8c9c7894cf5023248d98df3890ff2b44f74055cd5825304d3829ed41d1e6.

- 2026-09-16T21:19:35+00:00: Recorded command exit 0; command argv SHA-256
  07afeedbd3e1eac300bb221506be20582dfbea6d78f770917c4c73c7029bb4a6.

- 2026-09-16T21:19:56+00:00: Recorded command exit 101; command argv SHA-256
  d8b0a364faaf567170fae33f136fd7e417f1bbbcb8b5cac31feee17ece23c8c1.

- 2026-09-16T21:20:58+00:00: Recorded command exit 0; command argv SHA-256
  07afeedbd3e1eac300bb221506be20582dfbea6d78f770917c4c73c7029bb4a6.

- 2026-09-16T21:21:23+00:00: Recorded command exit 0; command argv SHA-256
  b56f7f6451894de40baddb15b904e7b6d36e64d7aacc62bbc92d85e694e9404d.

- 2026-09-16T21:21:38+00:00: Recorded command exit 0; command argv SHA-256
  469bb9d29322686a4ccdd6c2906a4a77527c1fe134799301a23d497a73733952.

- 2026-09-16T21:21:47+00:00: Recorded command exit 0; command argv SHA-256
  411182929b0e8a88b1f315ea197f8345adfb71b4b0d9f832053a960ca58ca3cc.

- 2026-09-16T21:22:15+00:00: Reproduced with explicit manifest-path command: baseline failed on run
  4/20 at sandbox_boundary.rs:474 because crash launch returned a non-ScopeOwnership result;
  accepted either ScopeOwnership rejection or a returned process that exits nonzero and reaches
  Terminal. Corrected focused test passes 20/20 bounded repeats; signed product commit 0acbc1d.

- 2026-09-16T21:22:27+00:00: Recorded command exit 0; command argv SHA-256
  22176a1ece3d3591a9b0b37f5f69d0634f08e971734b76eb6394adf265e28d09.

- 2026-09-16T21:23:18+00:00: Recorded command exit 0; command argv SHA-256
  df857b08b8fda6ab47c3349577fb866e3410ae89bf8db8aeed83af9fe807fb91.

- 2026-09-16T21:23:26+00:00: Recorded command exit 0; command argv SHA-256
  60f3b5c634e53f74159d2f4472892f482ce7163a530f376aa614f46f800be17c.

- 2026-09-16T21:23:38+00:00: Recorded command exit 0; command argv SHA-256
  6da5ad75937fcfa80bdf3b52a1f1a416d0de5358bcdc878926afba7ef34dbf12.

- 2026-09-16T21:25:08+00:00: Recorded command exit 0; command argv SHA-256
  b09e6da2efd7d5d756be73baaf752a8d4148bae27ba7011d741da84ca9bd2ceb.

- 2026-09-16T21:25:18+00:00: Recorded command exit 0; command argv SHA-256
  b09e6da2efd7d5d756be73baaf752a8d4148bae27ba7011d741da84ca9bd2ceb.

- 2026-09-16T21:25:28+00:00: Recorded command exit 0; command argv SHA-256
  b09e6da2efd7d5d756be73baaf752a8d4148bae27ba7011d741da84ca9bd2ceb.

- 2026-09-16T21:25:36+00:00: Recorded command exit 0; command argv SHA-256
  b09e6da2efd7d5d756be73baaf752a8d4148bae27ba7011d741da84ca9bd2ceb.

- 2026-09-16T21:25:45+00:00: Recorded command exit 0; command argv SHA-256
  b09e6da2efd7d5d756be73baaf752a8d4148bae27ba7011d741da84ca9bd2ceb.

- 2026-09-16T21:26:00+00:00: Recorded command exit 0; command argv SHA-256
  44ef6490f46b3d4c3286619b080236f19355ff657e774940376c9f8113c854d4.

- 2026-09-16T21:26:08+00:00: Recorded command exit 2; command argv SHA-256
  2df63971444066786059b2349ad8e08594f7c67d1e89e8ff2076dd1868131000.

- 2026-09-16T21:26:21+00:00: Recorded command exit 0; command argv SHA-256
  69cdb5fcb8d75943a26e80217c25076d4461c85ad8a6eba769335b717e81ae81.

- 2026-09-16T21:28:30+00:00: Reconciled generated profraw cleanup: product worktree has no profraw
  files, git status is clean, observed_dirty=0, exact head 0acbc1d1a8bf43a226fda503fbd76f8afd48eb07.
  Full applicable gates: fmt, locked workspace tests, clippy -D warnings, rustdoc, repository
  policy, and signature policy passed. cargo deny and cargo audit are unavailable subcommands in
  this environment; failure-path harness invocation was usage-only because its required --bin-dir
  was not supplied. Focused terminal-crash test passed 20/20 after signed fix. Ready for independent
  review; no PR/merge performed.

- 2026-09-16T21:28:43+00:00: Released ownerless for independent review. Exact clean product head
  0acbc1d1a8bf43a226fda503fbd76f8afd48eb07; signed SSH commit with matching DCO. Focused
  terminal-crash test passed 20/20; fmt, locked workspace tests, clippy -D warnings, rustdoc,
  repository policy, and signature policy passed. cargo deny/audit unavailable; failure-path harness
  requires approved --bin-dir. No PR or merge performed.

- 2026-09-16T21:30:40+00:00: Claimed by asb_ar1263_sandbox_stability.

- 2026-09-16T21:30:48+00:00: Recorded command exit 0; command argv SHA-256
  4265abd6081f4331f78288d264e8df219ed3f8b3c3bd18ec11c93e5667b3daae.

- 2026-09-16T21:31:03+00:00: Released ownerless for independent review after re-review approval.
  Product exact clean signed head 0acbc1d1a8bf43a226fda503fbd76f8afd48eb07; generated WORKTREES
  projection now records dirty=0. Focused terminal-crash test 20/20; locked fmt/workspace
  tests/clippy/rustdoc/repository policy/signature policy passed. cargo deny/audit unavailable and
  failure-path harness requires approved --bin-dir. No PR or merge performed.

- 2026-09-16T21:31:30+00:00: Claimed by asb_ar1263_sandbox_stability.

- 2026-09-16T21:31:33+00:00: Recorded command exit 1; command argv SHA-256
  63e7735b1cf93d516bd28a6de8c145f496982c358be7e0b8d55b3bca269bf77c.

- 2026-09-16T21:31:51+00:00: Recorded command exit 0; command argv SHA-256
  d5504eff25c890686c9c1da77bd447bf24431004d4371c4f86929f421396b9c0.

- 2026-09-16T21:32:01+00:00: Recorded command exit 1; command argv SHA-256
  63e7735b1cf93d516bd28a6de8c145f496982c358be7e0b8d55b3bca269bf77c.

- 2026-09-16T21:32:30+00:00: Recorded command exit 0; command argv SHA-256
  3900bb0b3b5cf41df797659940ce9737a74182cea680ebe0e42c37e1e2d587b0.

- 2026-09-16T21:32:58+00:00: Publication corrected by running gh from the declared product worktree:
  PR #205 opened at https://github.com/martin-beck/agent-systems-benchmark/pull/205. Exact base
  0a808a635d85fdc4a43b575e3711ef23b38089e3, head 0acbc1d1a8bf43a226fda503fbd76f8afd48eb07,
  mergeable. Hosted checks run 35152955071 (AArch64), 35152955085 (fault/fuzz), 35152955083
  (formal), 35152955236 (platform), 35152955119 (policy), 35152955173 (Rust); header and AWQ checks
  already passed. Keep PR open pending all required terminal success.

- 2026-09-16T21:33:08+00:00: Released ownerless while PR #205 hosted checks run. Exact head
  0acbc1d1a8bf43a226fda503fbd76f8afd48eb07/base 0a808a635d85fdc4a43b575e3711ef23b38089e3, PR
  https://github.com/martin-beck/agent-systems-benchmark/pull/205. Header/AWQ checks passed;
  AArch64, fault/fuzz, formal, platform, policy, and Rust checks were in progress at release.
  Independent review approved publication. No merge performed.

- 2026-09-16T21:40:52+00:00: Claimed by asb_ar1263_sandbox_stability.

- 2026-09-16T21:40:55+00:00: Recorded command exit 1; command argv SHA-256
  3b8302eb10498874768b6c592f3a5b800f20907950f9b9e8039306670a4ae168.

- 2026-09-16T21:41:15+00:00: Recorded command exit 0; command argv SHA-256
  9d059121b792b7fd062dd5f32e2b1614e61c9331ae019c331150f1fdeca7c490.

- 2026-09-16T21:41:53+00:00: Post-merge verification: PR #205 merged at
  ebfa37023e56269b8299254b535be60f3cf1d186 with parents 0a808a635d85fdc4a43b575e3711ef23b38089e3 and
  0acbc1d1a8bf43a226fda503fbd76f8afd48eb07. Feature head and all 12 exact-head hosted checks were
  green. Protected-main merge commit is GitHub-authored and has no Signed-off-by trailer; git show
  --show-signature reports RSA B5690EEEBB952194 but local key unavailable. AR remains not done
  pending signed forward-only recovery and exact-main policy/post-merge gates.

- 2026-09-16T21:42:01+00:00: Blocked after protected-main merge
  ebfa37023e56269b8299254b535be60f3cf1d186: GitHub merge commit lacks Signed-off-by; local RSA
  signature key unavailable. Feature commit 0acbc1d and all 12 exact-head checks are preserved
  green. Requires signed forward-only protected-main recovery plus exact-main policy/post-merge
  verification; AR is not complete.

- 2026-09-16T22:07:50+00:00: AR-1264 signed forward-only recovery 69e8b064 resolved the
  protected-main DCO blocker; reopen AR-1263 for closure verification against exact signed main and
  terminal post-merge evidence.
