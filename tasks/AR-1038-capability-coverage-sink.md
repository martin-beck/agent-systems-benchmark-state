---
{
  "branch": "test/capability-coverage-sink",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T01:35:03+00:00",
  "depends_on": [
    "AR-1023"
  ],
  "id": "AR-1038",
  "next_action": "Repair PR #132 review blockers in the single capability_contract test: closed LLVM_PROFILE_FILE token grammar, default.profraw scanning, actual runtime uniqueness/adversarial coverage, and bounded canonical-parent race handling; then run full gates and republish for immutable review.",
  "observed_branch": "test/capability-coverage-sink",
  "observed_dirty": 1,
  "observed_head": "b65cb4b5e9a9d6d75de967ff4673506218c62b45",
  "owner": "codex-ar1038-coverage-20260911",
  "plan": "../plans/AR-1038.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Prevent sanitized capability child tests from writing default profraw files into the source checkout.",
  "task_revision": 61,
  "title": "Preserve coverage sinks in sanitized CLI child tests",
  "updated_at": "2026-09-10T23:42:18+00:00",
  "worktree_key": "agent-systems-benchmark-capability-coverage-sink"
}
---
## AR-1038

Fix the six `default_*.profraw` files discovered during AR-1013 full coverage without weakening
`env_clear()`. This is an ASB test-harness repair only and owns no standalone TUI or production UI.

- 2026-09-10T22:59:55+00:00: AR-1023 is complete; focused capability test-harness repair is
  dependency-ready.

- 2026-09-10T22:59:58+00:00: Claimed by codex-ar1038-coverage-20260911.

- 2026-09-10T23:01:26+00:00: Recorded command exit 0; command argv SHA-256
  ff96f1201b06672675efd403b806dc7c27fdaac28f0179b14754fde91d4abfb8.

- 2026-09-10T23:03:23+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-10T23:04:06+00:00: Recorded command exit 0; command argv SHA-256
  190f52074d594af56f94d8dee69d460ecc0ba6f773d6d0afeead797fd7ed872d.

- 2026-09-10T23:04:32+00:00: Recorded command exit 0; command argv SHA-256
  256423c8900d6dfa34df9cd63ce7a37fb83bfb6a1ff21374798ee71f3ab21c4d.

- 2026-09-10T23:05:55+00:00: Recorded command exit 1; command argv SHA-256
  b98fa5f31a3776574cfc43aede3198a94d130dcc4f49ded27ed7d0efea649b83.

- 2026-09-10T23:06:35+00:00: Recorded command exit 0; command argv SHA-256
  94a980f40fcbfe6659cf967b318dc33fad47361d16ec87dfa0c880d859eb111a.

- 2026-09-10T23:06:54+00:00: Recorded command exit 0; command argv SHA-256
  256423c8900d6dfa34df9cd63ce7a37fb83bfb6a1ff21374798ee71f3ab21c4d.

- 2026-09-10T23:07:20+00:00: Recorded command exit 0; command argv SHA-256
  e05bd290238ddb252923c16c6ed0a31803232940b7311848859f6f386763703a.

- 2026-09-10T23:08:10+00:00: Recorded command exit 0; command argv SHA-256
  d6b9ab339d7d3c0ad428bd006af6b4ccef78a0452b921c313218a605c6caf3b3.

- 2026-09-10T23:08:49+00:00: Recorded command exit 0; command argv SHA-256
  cd05ff47f8503472ba4ab3e7795b604ca8adc249642416adf741b00044a18204.

- 2026-09-10T23:09:15+00:00: Recorded command exit 0; command argv SHA-256
  1be2447425f5635f4d469b3934662b146f8f11e4b24d9ab6a0ac8d5d7bb68009.

- 2026-09-10T23:10:24+00:00: Recorded command exit 0; command argv SHA-256
  bb57a13e81dc1cf3c9906a1cffdb3764a482037927679d073f09ef7c9db4424c.

- 2026-09-10T23:11:47+00:00: Recorded command exit 0; command argv SHA-256
  91d8cd78b8270162d184532af519b18d0c1fab235f8d60762b7e90a15ae4e71b.

- 2026-09-10T23:12:19+00:00: Recorded command exit 1; command argv SHA-256
  7c1e23077b971d7348324f0b85d6e0568fbbda4bec35168bd8ab7e19da94e731.

- 2026-09-10T23:12:41+00:00: Recorded command exit 0; command argv SHA-256
  2f7046f502692aa5182ae25d8dc9efe829739e7f5cf0e1ee913600379c51d6cb.

- 2026-09-10T23:12:55+00:00: Recorded command exit 0; command argv SHA-256
  cf0e35e0a89bacf04aa3ead16eba4be578574fa5ae559beb73f282961e46a559.

- 2026-09-10T23:13:22+00:00: Recorded command exit 0; command argv SHA-256
  5025ca94f626015736de9d45d837bfd633592ef08da2b236577b891b333ea0a2.

- 2026-09-10T23:13:50+00:00: Implemented and published PR #132 at signed+DCO head
  6e467bbde40c31bd817d215483ba496e2ecc5df5, tree d94c93a4458866a3c39b722536881787b97ed5cf, base
  58d0da27736d6c22ca7c43f76ade497165b29919. Scope is one test harness file only. Centralized the six
  env-cleared capability children; absence remains valid, while a supplied sink is forwarded exactly
  only if UTF-8, <=4096 bytes, absolute, parent-resolvable outside the checkout,
  parent-traversal-free, per-process (%p), control-free and .profraw-suffixed. Invalid sinks fail
  before spawn, preventing instrumented fallback files. Tests cover absent, empty, relative,
  oversized, control-bearing, shared, wrong-suffix, traversal and checkout-local sinks plus parallel
  canonical/failing children. Focused normal tests pass 9/9. Focused llvm-cov produced 16
  instrumented process profiles only under the external coverage target and zero default_*.profraw
  anywhere in the checkout. Exact-head fmt, workspace clippy -D warnings, full workspace tests with
  serial process tests, rustdoc -D warnings, release build, workspace/critical coverage floors,
  deny, audit, contract consistency, repository policy, diff-check, clean tree and signature/DCO
  pass. Failures classified: initial wrapper lookup exit127 used the product cwd and made no
  mutation; first apply_patch stdin form exited2 before mutation and was replaced by the supported
  patch argument form; one formatted-context patch exited1 without mutation and was reapplied; first
  PR-create quoting exited2 before GitHub mutation and was retried safely; contract consistency
  exited1 because origin/main was not accepted as an exact commit and passed unchanged with exact
  base 58d0da2.

- 2026-09-10T23:13:57+00:00: Recorded command exit 0; command argv SHA-256
  fbc5262f0a32d6002cbe7a2f72989c02904a38dae701a9582f0e84b01ff969ac.

- 2026-09-10T23:14:15+00:00: Recorded command exit 0; command argv SHA-256
  a0172f25db9bb4d9d5e5325764ac8273b42b5a1987ea18be70efadef4e26a853.

- 2026-09-10T23:15:01+00:00: Recorded command exit 0; command argv SHA-256
  e88bed5f434fe162fb90471800dd46cb73eb5e83cb9e61e5953ccc4ec868b7ed.

- 2026-09-10T23:15:30+00:00: Recorded command exit 0; command argv SHA-256
  5f1b4894ccda5d47f2d1eb3f9f1fc5b8860ba3210056855e4d8d391099ff9cd4.

- 2026-09-10T23:15:43+00:00: Recorded command exit 0; command argv SHA-256
  20f1e3269fcfcd0b6985a821cd7965e53282e4ed0ff88decdd2ff2ecd6d7215b.

- 2026-09-10T23:16:49+00:00: Recorded command exit 0; command argv SHA-256
  516813d5ce0bfaa47614fb4314881fe979fb0c04992ba21baf4dc9faf35e86a2.

- 2026-09-10T23:18:20+00:00: Recorded command exit 0; command argv SHA-256
  422d0fa5fa3688a316bb455b111224bf9471d21e0cf3f89c4f1c1322e5250305.

- 2026-09-10T23:18:45+00:00: Recorded command exit 0; command argv SHA-256
  fbc5262f0a32d6002cbe7a2f72989c02904a38dae701a9582f0e84b01ff969ac.

- 2026-09-10T23:19:23+00:00: PR #132 advanced by normal signed+DCO merge of current main, without
  force: exact remote head 51e18c62287816c7877925234ba37c0eb043f023, tree
  e35af4ee18030bead6b165aa561345f712a4ed34, GitHub base 0c65159d70ee728e21c7936663a90bea49ab0366.
  The initial exact-head Platform Evidence failure was correctly classified as source identity not
  immutable because main advanced after branch creation and the workflow base was no longer an
  ancestor; merging current main repaired ancestry and the replacement Platform Evidence check
  passed. Scope diff against current base remains only capability_contract.rs. Exact-head fmt,
  workspace clippy, focused 9/9, full workspace tests, rustdoc, contract consistency, repository
  policy and full serial coverage pass; protocol lines 96.44%, replay lines 97.64%, zero checkout
  default profiles. Live replacement CI currently 9/12 success and 3 running.

- 2026-09-10T23:20:08+00:00: Recorded command exit 1; command argv SHA-256
  09c4f4f6b0a3b806e820b29a804c5412c212affd90bf5bf3d9d0cbe3f2d01ce0.

- 2026-09-10T23:20:25+00:00: Recorded command exit 0; command argv SHA-256
  0b0a2eb4df9cd68e8af5a729056ffd7ae3c5bebe56af73f5274aa870e0cded09.

- 2026-09-10T23:22:20+00:00: Recorded command exit 0; command argv SHA-256
  7cda31780e54019c7de181010bc509f4bd00b0b9acdc6c08f1be7a37ff36c6c0.

- 2026-09-10T23:23:07+00:00: Recorded command exit 0; command argv SHA-256
  c211c9015ae5f8ce3ae826f7ca36930d9de66028685b9a762ddc23bcb54f2bf0.

- 2026-09-10T23:23:34+00:00: Recorded command exit 0; command argv SHA-256
  49b3d39a7a12d23fd92bacd2f6e3a09cc3ba853ef2209d3b18a4ba89076ffce3.

- 2026-09-10T23:23:56+00:00: Recorded command exit 0; command argv SHA-256
  20f1e3269fcfcd0b6985a821cd7965e53282e4ed0ff88decdd2ff2ecd6d7215b.

- 2026-09-10T23:25:35+00:00: CI repair successor b65cb4b5e9a9d6d75de967ff4673506218c62b45 (tree
  ed1c1847687f5a73216169af242ad2c71d234dad) is signed+DCO and pushed to PR #132. Exact hosted
  cargo-llvm-cov behavior is an absolute per-process .profraw path inside the checkout's ignored
  target subtree, not always an external root. The validator now permits only that isolated
  workspace target subtree or a resolved external directory; source paths, parent traversal,
  symlinked ancestors, relative/empty/oversized/control-bearing/shared/non-profraw values still fail
  before spawn. Added the exact hosted %p-%32m target fixture plus source-escape and symlink
  negatives. With CARGO_TARGET_DIR deliberately unset, focused normal and llvm-cov tests pass 9/9
  and the checkout-wide scan finds zero default_*.profraw. Prior exact 51e18c full
  workspace/coverage gates passed; replacement b65cb4b exact-head CI is running. The superseded
  quality failure is classified as a real validator incompatibility with cargo-llvm-cov's workspace
  target sink and was repaired, not retried unchanged. One later wrapper post-check exit1 occurred
  only because unrelated AR-1010 lease expired after product verification; AR-1010 recovery and
  doctor live now pass.

- 2026-09-10T23:26:13+00:00: Recorded command exit 2; command argv SHA-256
  34e318bc0346a81292b1c1eede34dd59f5b50fad1bb40035af6dc33fc8cf5478.

- 2026-09-10T23:26:47+00:00: Recorded command exit 0; command argv SHA-256
  6970754ed152dec27c3c47194bd043648175fedda2abfc3203a6649fcdf8a1e1.

- 2026-09-10T23:27:07+00:00: Recorded command exit 0; command argv SHA-256
  dd2d52c31c1974687cb9c30562215dbaab7ab5e8ec1337c85cc3da9ba64530b2.

- 2026-09-10T23:29:27+00:00: Final immutable PR #132 head b65cb4b5e9a9d6d75de967ff4673506218c62b45
  tree ed1c1847687f5a73216169af242ad2c71d234dad has all 12 exact-head GitHub checks terminal
  SUCCESS, including repository quality and emulated aarch64. The task plan is aligned in signed+DCO
  state commit 2237ecac to permit exact cargo-llvm-cov absolute sinks beneath ignored workspace
  target as well as validated external roots, while retaining source-path, root-default, traversal
  and symlink rejection. No merge or production/UI/TUI change was made.

- 2026-09-10T23:29:38+00:00: Implementation is frozen at PR #132 exact head
  b65cb4b5e9a9d6d75de967ff4673506218c62b45 tree ed1c1847687f5a73216169af242ad2c71d234dad with all 12
  checks terminal green. Await independent immutable review and coordinated protected merge; no
  self-merge.

- 2026-09-10T23:35:03+00:00: Claimed by codex-ar1038-coverage-20260911.

- 2026-09-10T23:36:11+00:00: Reclaimed frozen b65cb4b after reading full repository
  guidance/task/plan. Initial audit confirms contains(%p) accepts escaped/unsupported/repeated
  runtime substitutions and artifact scan misses default.profraw. Invalid read-only handoffctl show
  invocation exited 2 due to nonexistent subcommand and made no mutation. Repair remains one
  test-file only; no production or UI scope.

- 2026-09-10T23:38:45+00:00: Recorded command exit 0; command argv SHA-256
  febfa975120aa7c91ba5976dddcbcfed57bf0d3762f8b668bd8bb89bf5a130ae.

- 2026-09-10T23:39:46+00:00: Recorded command exit 1; command argv SHA-256
  88e23ece9a299de8f9a9c5d1c7fd9e89c7b8a9cc0288b1b37409afee164a6db4.

- 2026-09-10T23:40:01+00:00: Recorded command exit 0; command argv SHA-256
  0507b6ac502eed2c1ebe7a8f77407f669b671267d002a7b933eaf713b9654982.

- 2026-09-10T23:40:12+00:00: Recorded command exit 0; command argv SHA-256
  8a98ab3bfb8b881741a947ee916ce754fcd1965033e013fb677920cc79777eb6.

- 2026-09-10T23:40:48+00:00: Recorded command exit 0; command argv SHA-256
  31e68b7bc1d87c938c88c60cb7644bddf4e6ae4b10988e8fd52b3457390489bb.

- 2026-09-10T23:41:17+00:00: Recorded command exit 0; command argv SHA-256
  16704ade09b27959f564c5e6ead65b701c052ecf1cae9cca923e1f0037d10979.

- 2026-09-10T23:41:27+00:00: Recorded command exit 0; command argv SHA-256
  cc8d69428acd0eca33b9fb995efc9e769af949d004c0d30eb3cd1d641d31f9d3.

- 2026-09-10T23:41:43+00:00: Recorded command exit 0; command argv SHA-256
  8a98ab3bfb8b881741a947ee916ce754fcd1965033e013fb677920cc79777eb6.

- 2026-09-10T23:42:02+00:00: Recorded command exit 101; command argv SHA-256
  85736cc6e7d6c65211af710d2f6ff89ce5d0d910514a930cfa93b8a40c1ec7ea.

- 2026-09-10T23:42:18+00:00: Recorded command exit 0; command argv SHA-256
  9ced583eaeee1fff56ffa93e5b3ff3c67b1089c8911230b1f8cda2d17f5ce0e8.
