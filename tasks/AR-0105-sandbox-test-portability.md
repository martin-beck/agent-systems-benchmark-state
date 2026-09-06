---
{
  "branch": "fix/sandbox-test-portability",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T00:04:41+00:00",
  "depends_on": [
    "AR-0103"
  ],
  "id": "AR-0105",
  "next_action": "Release AR-0105 done after repaired exact-main local/hosted/state validation.",
  "observed_branch": "fix/sandbox-test-portability",
  "observed_dirty": 0,
  "observed_head": "23035acde688df67aee86b1373b3b1aa87b3b68d",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-0105.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Remove repository-target assumptions from sandbox lease tests so clean external Cargo targets work.",
  "task_revision": 76,
  "title": "Repair sandbox test target portability",
  "updated_at": "2026-09-06T22:23:38+00:00",
  "worktree_key": "agent-systems-benchmark-sandbox-test-portability"
}
---
## AR-0105

Remove repository-target assumptions from sandbox lease tests so clean external Cargo targets work.

This defect was discovered by AR-0204's exact-tree validation with a fresh external
`CARGO_TARGET_DIR`. The sandbox lease unit fixture derives a repository `target` path and
attempts to create a child without creating its missing parent, producing `ENOENT`. Do not
pre-create or retain a repository target directory to mask the failure.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-06T21:12:10+00:00: Promoted after confirming dependency AR-0103 is durably done; P0
  regression blocks clean external-target full-tree validation and must not be masked by precreating
  repository target directories.

- 2026-09-06T21:14:40+00:00: Claimed by contracts-20260906.

- 2026-09-06T21:14:51+00:00: Recorded command exit 0; command argv SHA-256
  bbce29c67a8524be6da229d8a31c52c3d6291ba6e461557ac0293df07a911720.

- 2026-09-06T21:15:10+00:00: Recorded command exit 101; command argv SHA-256
  9d971526f8ffc1039239ca1a987d496ad8ee068c325e8d745189812a4d433c02.

- 2026-09-06T21:16:36+00:00: Recorded command exit 0; command argv SHA-256
  d7a046c26df871a74ff3ea86b44762fdbb3a81d73dc5c95949cae8cf74d88f11.

- 2026-09-06T21:16:52+00:00: Recorded command exit 0; command argv SHA-256
  9cec9684a58511c4e54662b6a1b70f20cf58a8f71f19e46c562a37d8da6964ef.

- 2026-09-06T21:17:13+00:00: Recorded command exit 0; command argv SHA-256
  77a4167ec9ee7467eca742fcbb87aefbc12ecc58578734426b3bd77ea4ea4141.

- 2026-09-06T21:17:33+00:00: Recorded command exit 101; command argv SHA-256
  46414eb6feafa620f5d84b88b300599506be0f17f11a83e52ec1f661bc751196.

- 2026-09-06T21:17:51+00:00: Recorded command exit 0; command argv SHA-256
  6a2e050bfce0a55aa633ab06c09a432628f93c95e6bfb658c141d331a92520e0.

- 2026-09-06T21:18:08+00:00: Recorded command exit 101; command argv SHA-256
  2f185f7fedd7b24aea88ac1b6206522a66a2b5de11b7d1d8d3078d1ad175bf63.

- 2026-09-06T21:18:22+00:00: Recorded command exit 0; command argv SHA-256
  5d12c87c349772d104fdb43ead9913e4d346bbd337bd01fc621a007f18d1710d.

- 2026-09-06T21:19:01+00:00: Recorded command exit 1; command argv SHA-256
  7ba9030695cbd80ffbab797d62a9beccc5b61333b68c6ea5e7ab01525a5152ad.

- 2026-09-06T21:19:15+00:00: Recorded command exit 0; command argv SHA-256
  f71975b0e0b00a780fed3410ff70f306b8004ce22f8d1aecc438b8adc79fe8e9.

- 2026-09-06T21:19:27+00:00: Recorded command exit 0; command argv SHA-256
  2bfa70e56e0700f1936ea112c39e5f5d79584490104fd381369d35104ecc19ae.

- 2026-09-06T21:20:17+00:00: Recorded command exit 0; command argv SHA-256
  25207b320ad4204782e2db1b7cacc6fa99a74d8a745e25d61895e0601ee06505.

- 2026-09-06T21:21:10+00:00: Recorded command exit 101; command argv SHA-256
  579e494bde30fdd2a65a089c97b4bb11aaed8968fc1b6e507e156f52539ff4a9.

- 2026-09-06T21:21:27+00:00: Recorded command exit 0; command argv SHA-256
  25207b320ad4204782e2db1b7cacc6fa99a74d8a745e25d61895e0601ee06505.

- 2026-09-06T21:21:47+00:00: Original main 9543a32 failure reproduced at sandbox.rs:1329 with fresh
  external CARGO_TARGET_DIR and absent repository target. Signed+DCO fixture-only candidate 2b28fee
  changes only sandbox.rs tests: external-target/temp scratch base, PID plus atomic uniqueness, RAII
  fixture cleanup, and panic-path/no-repository-target regression. Original and negative tests pass
  on three distinct fresh targets with no residuals; one fresh full workspace run passed. A later
  fresh full run exposed a separate order-dependent ENOENT at tests/sandbox_boundary.rs:187 because
  target_root at line 44 still hardcodes repository target and the panic sentinel may execute before
  another test creates it. That path is outside current AR ownership; it was not edited or masked,
  and the empty residual target directory was removed. Clippy typo attempts and exact outcomes are
  retained in wrapper evidence.

- 2026-09-06T21:25:00+00:00: Recorded command exit 0; command argv SHA-256
  b6058f98fd23577b6803e77af4eb661df17e2c37e924329ba58040dfdc78180f.

- 2026-09-06T21:25:26+00:00: Recorded command exit 0; command argv SHA-256
  da3ced52682d53d4280c82d189cc02bdb13d285b39876cd6d29325f514cc0978.

- 2026-09-06T21:25:45+00:00: Recorded command exit 0; command argv SHA-256
  49e3ef9be34e75b475cee10027dfccec505a638f9ba801ab3311d2252174feb9.

- 2026-09-06T21:26:00+00:00: Recorded command exit 0; command argv SHA-256
  d9e737339a202e677bab22a91d963d0110381001448e6e02f3509461ca1931c3.

- 2026-09-06T21:26:09+00:00: Recorded command exit 0; command argv SHA-256
  e0e814b48e1909b50ccabd4bb0699237298e6f32cf543810dd57274837794bd9.

- 2026-09-06T21:26:15+00:00: Recorded command exit 0; command argv SHA-256
  e32967f01c9f082179411bd5e1ecd64d0b001ab7f0e7eb8f5461c28b834d97a1.

- 2026-09-06T21:27:58+00:00: Recorded command exit 0; command argv SHA-256
  7e76f10aa3ba1106ce0960552f070f38c54d80ba2ed83dd774a1c70126649f38.

- 2026-09-06T21:28:11+00:00: Recorded command exit 0; command argv SHA-256
  4f4627b282adf8827827c107a70a6b433626792a6cb0ffe453f207aec1f3e9c0.

- 2026-09-06T21:28:27+00:00: Recorded command exit 0; command argv SHA-256
  10def708b1bb5dfb44cb63a9e1ad314aeed901242bc935a797a894bb7f98bbb2.

- 2026-09-06T21:28:43+00:00: Expanded two-fixture candidate d71321c is signed+DCO on exact product
  main 9543a32 and changes only sandbox unit/integration test fixtures. Both original ENOENT paths
  now derive collision-resistant PID/atomic scratch names from external CARGO_TARGET_DIR or temp
  fallback; unit overlap uses RAII directory cleanup, integration panic sentinel creates and cleans
  its own root, and host isolation sentinel remains outside the sandbox workspace without
  repository-target assumptions. Unit originals/negative passed three distinct fresh targets;
  integration sentinel/staging passed three distinct fresh targets in alternating order; two
  separate cargo test processes passed concurrently against one fresh target; full exact-tree gate
  on another initially nonexistent external target passed with repository target absent before/after
  and zero scratch/sentinel residue. Workspace fmt/clippy/tests/docs/release, formal suite,
  audit/deny, coverage, workflow analyzers, Gitleaks, repository/DCO policy, controlled failure
  fixtures and platform validation all passed. Coverage: sandbox.rs 95.30% regions, 98.92%
  functions, 97.61% lines; workspace 93.41% regions, 96.59% lines.
  Candidate/tree/signature/DCO/diff/privacy/scope clean. Earlier second ENOENT and two mechanical
  borrow corrections remain preserved in evidence.

- 2026-09-06T21:38:34+00:00: Recorded command exit 0; command argv SHA-256
  1e99e8551d531d93db923cc939be3d861761e8275e5ec25889386c7069a2f374.

- 2026-09-06T21:39:55+00:00: Recorded command exit 0; command argv SHA-256
  bb6cfba6a1e26dcaa86995a8fccdaaa4ee23d9db129d3d4153d287f2da589212.

- 2026-09-06T21:40:19+00:00: Recorded command exit 0; command argv SHA-256
  e4c840476a7bd1cd28463c8e76e662a781fb4592afb992a666359c859cc6ca8b.

- 2026-09-06T21:40:54+00:00: Recorded command exit 0; command argv SHA-256
  a434470327ac5f7ecd6ee1a918677ec4b1e5e2495a3d49e81f66f6a2d44c8d51.

- 2026-09-06T21:42:01+00:00: Recorded command exit 0; command argv SHA-256
  948072f92946cc85b89e1ee05ef4fb02bb05eccb0cb8f7c3f48399eeec48b6f5.

- 2026-09-06T21:42:16+00:00: Recorded command exit 0; command argv SHA-256
  e32967f01c9f082179411bd5e1ecd64d0b001ab7f0e7eb8f5461c28b834d97a1.

- 2026-09-06T21:42:44+00:00: Recorded command exit 0; command argv SHA-256
  2108a363d79d8ffb21edfb7c8af6fc0bd06cb3fdb0dfed5186208e0e9e8aae4b.

- 2026-09-06T21:43:47+00:00: Recorded command exit 0; command argv SHA-256
  20dabe80042a53ab0e3e4cf470282dd2ac99394e1f8fdcbdbd41f50de20a07b2.

- 2026-09-06T21:44:51+00:00: Recorded command exit 0; command argv SHA-256
  75e37f33803399650f2f9d78068fab2b781b353b9366e762303722a20dc0811b.

- 2026-09-06T21:45:17+00:00: Independent review correctly blocked d71321c: relative CARGO_TARGET_DIR
  was classified without resolving against current_dir, and raw/manual fixture cleanup could retain
  residue after panic. Repaired signed+DCO candidate 250f398 is based exactly on b7e9078 and changes
  only sandbox.rs cfg(test) fixtures plus sandbox_boundary.rs. Relative target values now normalize
  against captured current_dir; all unit/integration roots are unique PID+atomic RAII guards;
  caught-panic regressions prove file and directory removal. Real relative external target, three
  distinct fresh absolute targets, both execution orders, and concurrent processes passed with
  repository target absent and zero scratch residue. Exact-tree external-target workspace
  fmt/clippy/tests/docs/release, native tests, formal suite, audit/deny, coverage,
  actionlint/zizmor/Gitleaks, repository/DCO policy, failure fixtures and platform validation
  passed. Coverage is sandbox.rs 97.56% lines and workspace 96.80% lines. Tree, diff-check, SSH
  signature, DCO, privacy and two-file scope are clean; no publication before immutable re-review.

- 2026-09-06T21:56:25+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-06T21:57:03+00:00: Recorded command exit 0; command argv SHA-256
  5bc442c64572d74ee06342f32ba83db6cc8381549dfbb1f90b221ccb0ebf3110.

- 2026-09-06T21:57:40+00:00: Recorded command exit 0; command argv SHA-256
  c816df3192169f0e3f1cf007576df74382b86c40b59ce67675241aed1606786c.

- 2026-09-06T21:57:55+00:00: Recorded command exit 0; command argv SHA-256
  948072f92946cc85b89e1ee05ef4fb02bb05eccb0cb8f7c3f48399eeec48b6f5.

- 2026-09-06T21:58:02+00:00: Recorded command exit 0; command argv SHA-256
  e32967f01c9f082179411bd5e1ecd64d0b001ab7f0e7eb8f5461c28b834d97a1.

- 2026-09-06T21:58:51+00:00: Recorded command exit 0; command argv SHA-256
  fe719da954644cbaa0a4bc43f88eed7117790ad14ae171142af9d37b2c65316e.

- 2026-09-06T22:00:07+00:00: Recorded command exit 0; command argv SHA-256
  67ff76791b5c03096c92c1d776cbcebfcf745dd1c64b45a61a17e957c079a8f2.

- 2026-09-06T22:00:43+00:00: Recorded command exit 0; command argv SHA-256
  f96889c02fe189aa2dbcb667913fbde238d7843645344aa3e1cb6198bf12cfa8.

- 2026-09-06T22:01:07+00:00: Second immutable review correctly blocked 250f398: merely making
  relative CARGO_TARGET_DIR absolute remained vulnerable to lexical foo/../target and symlink
  aliases that could resolve into the repository target while bypassing prefix classification.
  Successor eea3d20 lexically removes dot components and canonicalizes the deepest existing prefix
  so symlinks plus nonexistent suffixes resolve semantically before fixture use/classification.
  Negative regressions cover an existing relative alias and symlink alias resolving to repository
  target without creating it; positive regression covers a relative external target. RAII cleanup
  remains across all roots. Actual relative external run, three distinct fresh absolute targets,
  reverse ordering, concurrent processes, staging, original ENOENT tests and zero residue passed.
  Fresh external exact-tree workspace fmt/clippy/tests/docs/release, native sandbox, formal,
  audit/deny, coverage, workflow analyzers, Gitleaks, repository/DCO policy, failure fixtures and
  platforms passed. Coverage sandbox.rs 97.39% lines, workspace 96.77%. Candidate is one SSH-signed
  exact-DCO commit on b7e9078, clean two-file test-only scope, repository target absent; no
  publication before re-review.

- 2026-09-06T22:04:41+00:00: Heartbeat by contracts-20260906.

- 2026-09-06T22:10:24+00:00: Coordinator independently approved immutable candidate eea3d20 after
  verifying exact one-commit ancestry on b7e9078, SSH signature, DCO, two-file test-only
  scope/diff-check, RAII cleanup, relative-dot normalization, deepest-existing-prefix symlink
  handling, uniqueness and acceptance evidence; no production, Cargo or schema changes.
  Prepublication recheck confirms clean tree, repository target absent, exact origin/main b7e9078,
  no existing remote feature ref or PR, valid signature/DCO, Gitleaks clean and repository policy
  pass.

- 2026-09-06T22:10:38+00:00: Recorded command exit 0; command argv SHA-256
  03cf37fa29f3b008bcf13d35ae6db0de79b500cae9bd62ca5e4f9308b7c87e37.

- 2026-09-06T22:11:01+00:00: Recorded command exit 0; command argv SHA-256
  c257275056c670bf40c7998f4acd0782bfb2fa11d20f4b4d6f8a59e6c97839b2.

- 2026-09-06T22:12:46+00:00: Published immutable reviewed head eea3d20 and opened product PR #18. PR
  base is exact b7e9078, head exact eea3d20, mergeable, and all exact-head hosted checks passed:
  Rust verification run 34063259371 on ubuntu-24.04 x86_64 and ubuntu-24.04-arm; formal assurance
  run 34063259403 with Kani plus Loom/state models on x86_64/aarch64; repository quality run
  34063259528. PR URL https://github.com/martin-beck/agent-systems-benchmark/pull/18. No merge or
  release by worker.

- 2026-09-06T22:14:01+00:00: Recorded command exit 0; command argv SHA-256
  9878ff66f6f1167f0b183658c048fcf00bc8b82458a9d12b8c29b1a743690a11.

- 2026-09-06T22:16:41+00:00: Recorded command exit 0; command argv SHA-256
  91c481d4f1a058d3265e9102b0531d1eefe09cb45e5c1807ecda5e8c8b6b67d5.

- 2026-09-06T22:17:06+00:00: Recorded command exit 0; command argv SHA-256
  6666c5dc9937172206b2b480a2695d3024cc09358b12ac8a1d7578f49e24494a.

- 2026-09-06T22:18:05+00:00: PR #18 durably merged exact reviewed eea3d20 into b7e9078 as 7f308cc.
  Exact-main fresh external postmerge tests passed 23 runtime unit plus 10 sandbox boundary/native
  tests with repository target absent and zero residue; live doctor passed. Hosted formal run
  34063408520 passed. Hosted Rust run 34063408544 failed DCO on x86_64/aarch64 and quality run
  34063408539 failed repository policy: GitHub-authored merge identity is martin-beck
  <martin.beck2@gmx.de>, while required trailer is Martin Beck <martin.beck2@gmx.de>, so
  matching-author DCO fails; local keyring also cannot authenticate GitHub web-flow RSA signature.
  Correcting already-pushed main requires coordinator authorization for a controlled signed+DCO
  history repair or another explicit policy decision. AR remains in_progress and unreleased.

- 2026-09-06T22:19:10+00:00: Recorded command exit 0; command argv SHA-256
  db38e63e11537c4f9e408a4903247311605359e6e3115aff1b7b0313b69d86dd.

- 2026-09-06T22:19:40+00:00: Recorded command exit 0; command argv SHA-256
  989ec720da246333a316e049ead7d77b7bc03791c0b28a850435b7b64a762b02.

- 2026-09-06T22:20:00+00:00: Recorded command exit 0; command argv SHA-256
  fc9c65171bc651829043353e4aa4f1482c4e7fbf5f10df614d4c167b98e70962.

- 2026-09-06T22:20:44+00:00: Recorded command exit 0; command argv SHA-256
  6b3bdabc9badb169002f8c9ab95cb4054b95807434d7fe6c3295a129e602bc5b.

- 2026-09-06T22:21:15+00:00: Recorded command exit 0; command argv SHA-256
  63decf41da24151df0534576916e24fbfe41287300039395372e2abe8a653da5.

- 2026-09-06T22:23:38+00:00: Authorized narrow history repair replaced only bad GitHub merge 7f308cc
  with 23035ac using identical tree abdfa181, exact parents b7e9078 then reviewed eea3d20, Martin
  Beck author/committer, SSH signature and exact DCO. Explicit remote lease required main still
  equal 7f308cc and force-updated only that ref. Local postmerge fresh external target had already
  passed 23 runtime unit and 10 sandbox boundary/native tests with zero residue; replacement tree is
  byte-identical. Forced-push event Rust 34063685524 and quality 34063685602 were non-product
  failures because discarded 7f308cc was unreachable to checkout range logic. Clean
  workflow-dispatch exact-main reruns passed: Rust 34063766870 x86_64/aarch64, quality 34063737973;
  formal push run 34063685531 passed Kani and x86_64/aarch64 Loom/state models. Local/remote/origin
  main equal 23035ac, signature/DCO pass, worktree clean, live doctor green.
