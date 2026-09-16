---
{
  "branch": "fix/main-merge-integrity",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T08:21:12+00:00",
  "depends_on": [
    "AR-0003"
  ],
  "id": "AR-0897",
  "next_action": "Run PR187 exact-head CI/review, then create signed local recovery merge and rerun protected-main policy.",
  "observed_branch": "fix/main-merge-integrity",
  "observed_dirty": 0,
  "observed_head": "bd4f28646e0f1d273fad1dadf3310e0e8338e244",
  "owner": "asb_ar0897_merge_integrity",
  "plan": "../plans/AR-0897.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair the current main merge-boundary failure and enforce a signed DCO-bearing integration path.",
  "task_revision": 179,
  "title": "Restore main merge integrity",
  "updated_at": "2026-09-16T07:51:20+00:00",
  "worktree_key": "agent-systems-benchmark-main-merge-integrity"
}
---
## AR-0897

Restore exact-main commit-policy evidence without rewriting published history and prevent recurrence.

Trigger: GitHub Actions run 34347816992 rejected merge commit `b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b` before later quality gates because it lacks a matching DCO trailer.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-09T20:41:24+00:00: Dependency AR-0003 is done. P0 AR-0897 is the highest-priority ready
  unowned task with no existing branch, PR, worktree, or durable product effect; its
  integration-policy/docs/fixture scope is disjoint from active AR-0907 hosted-platform paths,
  AR-0908 asb-cli test path, and held formal integration.

- 2026-09-09T20:41:27+00:00: Claimed by replay_20260906.

- 2026-09-09T20:42:21+00:00: Recorded command exit 0; command argv SHA-256
  d0a0f89064e7d4fea28001a15ac51ee35d8f2ed68ae6f0d6722c4eb213e169a8.

- 2026-09-09T20:44:18+00:00: Recorded command exit 2; command argv SHA-256
  9af20895a797539e06740c955ffa5cf40a9a5b20fb1e0e5f81f36c31ce463ee6.

- 2026-09-09T20:48:49+00:00: Recorded command exit 1; command argv SHA-256
  f5ecc4c91aac809c00e8acbc140935a1500893198fc1523d0a5da7560d6c7d78.

- 2026-09-09T20:49:34+00:00: Recorded command exit 0; command argv SHA-256
  45f73c2de287a069d87d4ed561a53981f4289820726199a9c453c9ed851eaa6d.

- 2026-09-09T20:50:29+00:00: Recorded command exit 1; command argv SHA-256
  e0255a140754c9592aeb93ac4acf46bed1e5f2b5fc15e68656e6b76b7aedd071.

- 2026-09-09T20:50:54+00:00: Recorded command exit 1; command argv SHA-256
  105e1d5dbed1e3ec25b5727c69547fedde0fdce7d0c52d17674aa229ba0904e3.

- 2026-09-09T20:51:13+00:00: Recorded command exit 0; command argv SHA-256
  47ebf653bcb6b59543159f1c0768206f98863e7d2df785715d08fc200905bd36.

- 2026-09-09T20:53:19+00:00: Recorded command exit 0; command argv SHA-256
  f44ae9c8f9da63233325d3c114869bba3bd0d6c450e64db289f029d168cba277.

- 2026-09-09T20:54:03+00:00: Recorded command exit 0; command argv SHA-256
  45949eccbd799981ce89a55f41d08c8f25717e174da857890f75489700b1b5bc.

- 2026-09-09T20:54:41+00:00: Signed+DCO focused checkpoint fb782963d6df4d0792a22c2c229e8c7f393eff64
  (tree d1487102f2c8e080bfcd55fd8c3e857b0f3628dc, parent b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b)
  is clean with seven owned integration-policy/docs/test paths. It adds an exact base/head/tree
  verifier, signed DCO commit-tree merge with exact parents, remote-ref rechecks and exact
  force-with-lease publication; a fail-closed repository-settings auditor/applicator; policy
  enforcement; historical b6d04a8 identities/limitations; and adversarial fixtures. Focused results:
  Ruff check/format, Python compilation, repository policy, diff-check, and four integration suites
  green. Tests construct and push a signed exact-tree two-parent merge and reject stale/wrong
  identities, unsigned/non-DCO feature commits, and each permissive web-merge/auto-merge setting.
  Historical b6d04a8 tree 579310d1 with parents a4e1a9de/6cf8384b and failed run 34347816992 are
  preserved. Remote settings were audited as currently permissive but not changed before review.

- 2026-09-09T21:02:12+00:00: Recorded command exit 0; command argv SHA-256
  855ef833f25eba2550b413896f9b64c818cc2535c480d0d200e971861bdc1f57.

- 2026-09-09T21:05:07+00:00: Recorded command exit 0; command argv SHA-256
  b0f7e748cecec6f5d6b9e821346515a0d6a38ed207de4896d54873db236be93d.

- 2026-09-09T21:06:23+00:00: Recorded command exit 0; command argv SHA-256
  39ef3caf29448a3b1505527d87aa5d83bf1530708163116602df60c4495279e3.

- 2026-09-09T21:07:27+00:00: Recorded command exit 0; command argv SHA-256
  5ce2209b83b30e1eb8ad5c1694f348318609a4df5cea2dc552f3dd2623befded.

- 2026-09-09T21:07:50+00:00: Recorded command exit 0; command argv SHA-256
  58b4c68ed7579a8b9444580f242bc57d5573df2f17e8d74c72d1a03452a62c14.

- 2026-09-09T21:08:31+00:00: Recorded command exit 0; command argv SHA-256
  e1b6b629cb698b127d8b1390535f270a386ddcffdaadcefeb3996249e8166e09.

- 2026-09-09T21:09:50+00:00: Recorded command exit 0; command argv SHA-256
  4da8ad3eae63a19e57d4a37817fd0353e77a5c75aaac1b3b16d8d9c5d8d3fc78.

- 2026-09-09T21:11:46+00:00: Recorded command exit 0; command argv SHA-256
  f95dba75fa3886717ed06342bf8652fcd6952aae23286e4dc3e8f4f1f04790e6.

- 2026-09-09T21:12:54+00:00: Recorded command exit 0; command argv SHA-256
  18650a37139b2565caef06e04b5867f6317c4c226cfd68f9aeace6ec10d0fbb2.

- 2026-09-09T21:13:52+00:00: Recorded command exit 0; command argv SHA-256
  3c082082d70a4823dac1bfbca0113a4cae46077c2cdae8f59d1531a3e27c694b.

- 2026-09-09T21:15:55+00:00: Recorded command exit 0; command argv SHA-256
  4002e49fce166943aa697da211b9eef6a78e63d614277d3a5ef09abbc9123f42.

- 2026-09-09T21:16:23+00:00: Signed repair successor bd6f450ab8777aeb7e055d71aedba8e4cfd375b3 (tree
  201112340e22d217189243f04f611e95eef02536, parent fb782963d6df4d0792a22c2c229e8c7f393eff64, base
  b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b) is clean and limited to the seven owned
  docs/integration-policy/test paths. Review repairs are complete: bounded generic subprocess
  diagnostics with privacy sentinels; immediate target+PR ref reconciliation including
  accepted-after-error; signer principal bound to author/committer and exact DCO identity; atomic
  target/PR reads and post-push recheck; PR drift, target race, GitHub-generated unsigned merge,
  identity spoof, and accepted-but-error hostile tests. Full exact-tree gates pass: Ruff/py_compile
  and 9 integration suites; cargo fmt, Clippy, workspace tests, rustdoc, release build and CLI
  smoke; coverage floors; formal tests, digest-pinned offline TLC/Alloy; mutation sentinels 7/7;
  failure-path, contract and 46 platform tests; actionlint, zizmor, Gitleaks, cargo-deny/audit and
  exact-range repository policy. Pinned Kani plus required false-assertion negative passed in
  recorded exit-0 command 3c082082d70a4823dac1bfbca0113a4cae46077c2cdae8f59d1531a3e27c694b. Final
  immutable check exit 0 confirms both commits SSH-signed/DCO, exact tree/scope, diff-check and
  clean worktree. No publication or remote settings mutation performed.

- 2026-09-09T21:21:10+00:00: Publication was not attempted: approval named
  bd6f450ab877a7eb7e055d71aedba8e4cfd375b3, which git cat-file confirms is absent. The clean
  signed/DCO reviewed object remains bd6f450ab8777aeb7e055d71aedba8e4cfd375b3 with tree
  201112340e22d217189243f04f611e95eef02536. Exact-OID authorization is required because the
  instruction forbade use of a transposed identity.

- 2026-09-09T21:22:16+00:00: Recorded command exit 0; command argv SHA-256
  0ce6e8952e7679e3ea2d53a990325f0c10e50aa3e4ad043ee0d8b6a1c272e5ab.

- 2026-09-09T21:22:43+00:00: Recorded command exit 0; command argv SHA-256
  d29fe530b8b57e464a305e77be8b18b8c68ad815f9e1ebae4a7253a560479fa1.

- 2026-09-09T21:23:04+00:00: Recorded command exit 1; command argv SHA-256
  86a39de25b92b302004a57f3a4201f9588b436d5d105dbe6a8bee03e644aec35.

- 2026-09-09T21:23:26+00:00: Recorded command exit 1; command argv SHA-256
  b4ac5e2b742dfe33c69892a4cf1df9ba11a48aa31f0b86130e870f86490dfbd0.

- 2026-09-09T21:23:48+00:00: Recorded command exit 1; command argv SHA-256
  f52bb0ca7e8b5c6fc0a317acea4ba19f5cb2b3a82e4a92f9924daf1d8c37cdad.

- 2026-09-09T21:24:08+00:00: Recorded command exit 0; command argv SHA-256
  9456b107d1c39179fb03a170bf16f7a2b310d39b167593225e489d05f1bcd50c.

- 2026-09-09T21:24:44+00:00: Published the verified reviewed object
  bd6f450ab8777aeb7e055d71aedba8e4cfd375b3 (tree 201112340e22d217189243f04f611e95eef02536) as PR
  #126 https://github.com/martin-beck/agent-systems-benchmark/pull/126, exact base
  b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b. Remote head identity was re-read and matches exactly.
  Exact-head CI launched: AWQ shadow and header gates passed; Native Ubuntu, Kani, fault, fuzz,
  emulated aarch64, Loom/state, mutation, quality/supply, and Rust were pending at first query.
  TLC/Alloy job 102650889322 in run 34406581823 failed in run_temporal_models.sh immediately after
  the pinned TLA artifact download; the log contains no model diagnostic before exit 1. This is
  provisionally a shared formal acquisition/digest harness failure because the exact seven-path AR
  diff contains no formal/workflow/artifact changes and the same formal gate passed locally with
  pinned cached tools. Candidate remains unchanged; no retry or merge performed.

- 2026-09-09T23:41:59+00:00: Recovered expired claim formerly owned by replay_20260906. Expired
  AR-0897 lease recovered after terminal PR #126 classification; preserve reviewed bd6f450 and
  shared-harness evidence, require fresh claim before mutation.

- 2026-09-10T08:30:14+00:00: Claimed by contracts_20260906.

- 2026-09-10T08:30:39+00:00: Recorded command exit 1; command argv SHA-256
  e434f9b7677c9d0ae8ad7d4e6dabaf53990300b45a98ec912f5718a0737a68cf.

- 2026-09-10T08:31:00+00:00: Recorded command exit 0; command argv SHA-256
  b8ca90ba48a62b054bc3913a824221b202338129d116a96d4e835cad641fda34.

- 2026-09-10T08:31:31+00:00: Terminal PR 126 exact-head evidence at bd6f450/tree 20111234: 10 of 12
  jobs pass, including native Ubuntu, Rust, emulated AArch64, Kani, Loom, fault, fuzz, mutation, AWQ
  and headers. Formal run 34406581823 job 102650889322 fails in the shared temporal acquisition path
  before model diagnostics; AR-0877 owns that boundary. Repository Quality run 34406581994 job
  102650889901 fails only during coverage when
  mini_swe::tests::cancellation_reaps_owned_descendant_group asserts /proc disappearance too early
  (137 passed/1 failed/1 ignored); AR-0909 owns that test-isolation/lifecycle repair. Neither
  failure touches AR-0897 seven-path integration-policy scope. Candidate and PR remain unchanged;
  exact-head acceptance and merge remain blocked pending both serialized repairs.

- 2026-09-10T08:31:42+00:00: Released open without product mutation. PR 126 preserves exact reviewed
  bd6f450/tree 20111234; AR-0897 has no in-scope failure, but acceptance is incomplete until AR-0877
  formal acquisition and AR-0909 cancellation-reaping coverage repairs integrate and fresh
  exact-head CI is all green.

- 2026-09-15T15:18:20+00:00: Claimed by asb_ar0897_merge_integrity.

- 2026-09-15T15:18:59+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-15T15:19:18+00:00: Recorded command exit 0; command argv SHA-256
  561d797a72b76419e4df8eb18b46049ef8005b5bae2d171872e872666666478c.

- 2026-09-15T15:19:27+00:00: Recorded command exit 0; command argv SHA-256
  78bf38bd4489499e0e7e8110ebaef06a4751fd8d341db34f826b3a969aec2539.

- 2026-09-15T15:19:35+00:00: Recorded command exit 0; command argv SHA-256
  955f533ee5362b7454afbb273e290e17ac530113eaf95b9fbb0d3e64f2a772b7.

- 2026-09-15T15:19:44+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-15T15:20:15+00:00: Dependency audit 2026-09-15: AR-0877 is done, but AR-0909 remains open
  (task revision 278; PR #127 exact head c897313524a8d061a078465c5db0512ed366af9d has failing
  TLC/Alloy and Native Ubuntu checks). Existing reviewed AR-0897 PR #126 remains unchanged at
  bd6f450ab8777aeb7e055d71aedba8e4cfd375b3/tree 201112340e22d217189243f04f611e95eef02536. No product
  mutation or publication attempted. After AR-0909 integrates, rebase PR #126 onto current protected
  main, rerun complete gates, independently review exact head, and merge only with green CI.

- 2026-09-16T04:47:00+00:00: Claimed by asb_ar0897_merge_integrity.

- 2026-09-16T04:47:25+00:00: Recorded command exit 0; command argv SHA-256
  d04aa803a9fcb854b247572f9b417fd1935a57ca978bb887d2e7c188e99db043.

- 2026-09-16T04:47:38+00:00: Recorded command exit 1; command argv SHA-256
  b1807e7d793ca7d3bce3d7f29b5001a8c68594ed2dd8c9d679927e51f5638899.

- 2026-09-16T04:47:50+00:00: Recorded command exit 2; command argv SHA-256
  c9f3b02d4f92a2d9f6d5fc8aced1ec2ec155b574de09b6c08d2024bbfe77430d.

- 2026-09-16T04:48:11+00:00: Recorded command exit 0; command argv SHA-256
  81c79b865b4351e74b51e79bfbe1538029dcc4db87124fcd8b8801233ab04720.

- 2026-09-16T04:48:37+00:00: Recorded command exit 1; command argv SHA-256
  599653ddf1d4f426e59237ed38960c082b53d2c79c0f9dd8541f5ee9cb9d35f6.

- 2026-09-16T04:48:56+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T04:49:41+00:00: Recorded command exit 0; command argv SHA-256
  7c8824bdad2aa349d0f4e06c8a45f88849eeca12972176579d78858e87f39ea1.

- 2026-09-16T04:49:59+00:00: Recorded command exit 0; command argv SHA-256
  81c79b865b4351e74b51e79bfbe1538029dcc4db87124fcd8b8801233ab04720.

- 2026-09-16T04:50:33+00:00: Recorded command exit 0; command argv SHA-256
  b87f29537aa7a0ec77b12696102ffda50686417432f0dd31b5afde08a29a40ea.

- 2026-09-16T04:50:46+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T04:50:51+00:00: Recorded command exit 0; command argv SHA-256
  3d8fe1620bda5e98a41432841c9a4893745c2315f3b3d4792f6421374a34c15c.

- 2026-09-16T04:51:05+00:00: Recorded command exit 0; command argv SHA-256
  8b412bd04da5cdde9e241d4738456d6ae7d46f01e8a89905a3af2423f5c93fc7.

- 2026-09-16T04:51:23+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-16T04:51:32+00:00: Recorded command exit 0; command argv SHA-256
  81c79b865b4351e74b51e79bfbe1538029dcc4db87124fcd8b8801233ab04720.

- 2026-09-16T04:51:41+00:00: Recorded command exit 0; command argv SHA-256
  80ac6c490bd948eeac99e4902bbde777cd3b959cac86a66d55e3405dd552a043.

- 2026-09-16T04:51:55+00:00: Recorded command exit 0; command argv SHA-256
  98402b1aa5277af9eb36d4999b1632ce015fc7d0e24fe7e4b0252f3e2e82037f.

- 2026-09-16T04:52:16+00:00: Recorded command exit 101; command argv SHA-256
  d6a0af5332c7364b53ac106c2f6a7b25d05c9e9a7caa9e1bcc71a37c5b633845.

- 2026-09-16T04:52:25+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T04:52:40+00:00: Recorded command exit 0; command argv SHA-256
  d4e23f4ed421370a214c3acd542d3d16f5786dd2de203b0da4a3103f6e4de25b.

- 2026-09-16T04:53:01+00:00: Recorded command exit 0; command argv SHA-256
  4c88914415b7792072af57840949347e378ffe84688c078fd7b79f948e9fa324.

- 2026-09-16T04:53:21+00:00: Rebased signed merge-integrity implementation onto current origin/main
  00f3763; resolved docs/policy conflict, fixed malformed repository_policy block, and committed
  signed/DCO repair aceb191. Focused integration tests 9/9, repository policy, py_compile, cargo
  fmt, and asb-protocol lib 40/40 pass. Full workspace cargo test failed only because /srv/data
  reached no-space-on-device; removed only this worktree target/ build artifact via handoffctl.
  Next: run remaining applicable policy/integration gates, independently review exact clean head,
  publish PR through handoffctl; do not use GitHub web merge.

- 2026-09-16T04:54:00+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T04:55:19+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T04:55:56+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T04:56:41+00:00: Recorded command exit 0; command argv SHA-256
  d4e23f4ed421370a214c3acd542d3d16f5786dd2de203b0da4a3103f6e4de25b.

- 2026-09-16T04:56:54+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T04:57:03+00:00: Current clean signed/DCO head aceb191 is rebased onto origin/main
  00f3763. Focused integration 9/9, repository policy, py_compile, cargo fmt, and asb-protocol lib
  40/40 pass. Prior full workspace test failed only with ENOSPC after exhausting /srv/data; removed
  this owned worktree target build artifact (491 MiB) through handoffctl. Next: run Python
  policy/integration and any feasible remaining gates, perform independent exact-head review, then
  publish updated PR126 only after clean exact-tree approval; preserve 00f3763 and do not use GitHub
  web merge.

- 2026-09-16T04:57:33+00:00: Recorded command exit 0; command argv SHA-256
  3d8fe1620bda5e98a41432841c9a4893745c2315f3b3d4792f6421374a34c15c.

- 2026-09-16T04:57:41+00:00: Recorded command exit 0; command argv SHA-256
  81c79b865b4351e74b51e79bfbe1538029dcc4db87124fcd8b8801233ab04720.

- 2026-09-16T04:58:03+00:00: Independent exact-head review of aceb191: clean tree, three signed
  SSH/DCO commits rebased onto 00f3763; merge_pr.py enforces exact full-OID base/head/tree, signed
  DCO two-parent commit, signer identity, atomic remote recheck and force-with-lease;
  repository_settings.py fail-closed audits all web merge/auto-merge modes; adversarial integration
  tests cover stale/wrong identities, unsigned/non-DCO/GitHub-generated heads, signer spoof, races,
  accepted push errors, privacy-bounded diagnostics, and settings mutations. Post-rebase repository
  policy and integration tests 9/9 pass; py_compile and cargo fmt pass; asb-protocol lib 40/40 pass.
  Full workspace test remains environment-blocked by ENOSPC, recorded. Next: obtain independent
  coordinator approval, publish rebased PR126 via exact force-with-lease, await exact-head CI, then
  use local signed merge path only; verify post-merge DCO/policy and reconcile AR.

- 2026-09-16T04:58:24+00:00: Recorded command exit 0; command argv SHA-256
  acd95fcd5d13ea9b5a012c90ffcf5cba476ab3b69a07aaa427d98317fd7ebb62.

- 2026-09-16T04:58:38+00:00: Recorded command exit 1; command argv SHA-256
  a4d87edb00007f72f6f090fc76b3d27add16a975af7ece8a07803f9814d03bed.

- 2026-09-16T04:59:16+00:00: Independent exact-head review approves
  aceb1910b9203572cb2d477d0f94ad92d07e47e1: clean, rebased onto current main 00f3763, all three
  commits SSH-signed/DCO; complete merge_pr/settings/policy diff is scope-correct and adversarial
  integration tests 9/9 plus repository policy, py_compile, cargo fmt, asb-protocol lib 40/40 pass.
  Published PR #126 branch update via exact --force-with-lease against prior bd6f450; PR now exact
  head aceb191/base 00f3763 and open. Exact-head CI run
  35057669012/69115/69146/69149/69102/69117/69083/69116 is pending except AWQ shadow and headers
  pass. Do not merge until every required check is green and protected local signed merge path is
  authorized; next monitor exact-head CI and independently reconcile any failures.

- 2026-09-16T04:59:49+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T05:03:37+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T05:04:56+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T05:05:39+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T05:06:02+00:00: Recorded command exit 0; command argv SHA-256
  70466b9deb0f6bab3206d213d161a64c103c120085423169569443920f051eaf.

- 2026-09-16T05:06:12+00:00: Recorded command exit 0; command argv SHA-256
  99183eccb351ab21d535c4c9323ba009dedc3bc184847f82449b103c4ffc6e1c.

- 2026-09-16T05:06:29+00:00: Recorded command exit 0; command argv SHA-256
  0bbf2aeaa99361a9b7549f23a69da1a9b5765f4d48f8a693451147384f6a9ea7.

- 2026-09-16T05:06:51+00:00: Fixed stale workflow_transcript contract assertion to require
  documented local SSH-signed DCO merge path and reject obsolete gh pr merge --merge wording.
  Focused test passes 1/1. Signed+DCO commit 1ef6469 pushed via exact force-with-lease replacing
  remote aceb191; PR126 exact head is now 1ef6469 and fresh CI is required. Next: monitor all
  exact-head checks, diagnose any failures, and do not merge until all required checks green plus
  independent review.

- 2026-09-16T05:07:10+00:00: Recorded command exit 0; command argv SHA-256
  166117133f6d109ce2b623bf811ff78f1c5e2554b53a4b1ef9c3e6ce37d4e76e.

- 2026-09-16T05:07:20+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T05:07:35+00:00: Recorded command exit 0; command argv SHA-256
  70466b9deb0f6bab3206d213d161a64c103c120085423169569443920f051eaf.

- 2026-09-16T05:07:47+00:00: Recorded command exit 0; command argv SHA-256
  10d0ce84606bff721a40d40c3f5a866cfbfb024b375e66d6cfdc1ca007a62be0.

- 2026-09-16T05:07:59+00:00: Recorded command exit 0; command argv SHA-256
  bac23c0a21bcb53fd4c3c71072fd6ac38aaf90ebc3c25e60e1598062d2d58c24.

- 2026-09-16T05:08:15+00:00: PR126 run 35058203094 failed only cargo fmt on workflow_transcript.rs;
  gh log identified exact rustfmt wrapping. Ran cargo fmt via handoffctl, signed+DCO commit 44ca04d,
  pushed with exact lease replacing 1ef6469. Worktree clean, diff-check and focused
  workflow_transcript test previously pass. Fresh exact-head CI now required for 44ca04d; next
  monitor and diagnose only exact-head failures, no merge until all checks green.

- 2026-09-16T05:08:50+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T05:09:53+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T05:15:17+00:00: Recorded command exit 0; command argv SHA-256
  d7b5fe8cb72b938368838d1d28f52d045b841d11afaeeeb2a2230ede7e0a4076.

- 2026-09-16T05:15:35+00:00: Recorded command exit 2; command argv SHA-256
  e87963d45e503d5120c3656dfe9916d89f6a7a85af5e462012c7de69354a7549.

- 2026-09-16T05:16:46+00:00: Recorded command exit 0; command argv SHA-256
  610023d463f090d8ac4c4ad1195040d33079c61d9137ca7c094db7b0bbffcf04.

- 2026-09-16T05:17:04+00:00: Recorded command exit 0; command argv SHA-256
  21e1e3146706dff9f9eae3d0f1c278e5ab673211a8a888837bc51f6887bfd4c8.

- 2026-09-16T05:17:24+00:00: Recorded command exit 0; command argv SHA-256
  a5debc524d30d23c4210c91fe59fcea2cb2280e0cf2234cdde8dbff6efa49518.

- 2026-09-16T05:17:33+00:00: Recorded command exit 0; command argv SHA-256
  723daf2a2a944265e29eaae50d957222e4b32bc224a07c01b38e4a6ab0d5483c.

- 2026-09-16T05:18:46+00:00: Recorded command exit 0; command argv SHA-256
  cc3c64720994ba85b78d7bdaa8481735529439c6eb82d73dd49cd77a0e3a66ac.

- 2026-09-16T05:19:05+00:00: Recorded command exit 0; command argv SHA-256
  af57b6026ff65d6e8b480c4cd7b5667deb2efb20413e2b06fa5e1de637c7013f.

- 2026-09-16T05:19:13+00:00: Recorded command exit 0; command argv SHA-256
  abf7c7f5e6a1f19b4a041254d9fb63d20e568f9974ad231d6d962b0f98ceed9c.

- 2026-09-16T05:19:25+00:00: Recorded command exit 0; command argv SHA-256
  48512ab7d64c6444287ccce2ee7eaea405c6e12962f747cb4c2b31fa5a837c90.

- 2026-09-16T05:20:02+00:00: Recorded command exit 0; command argv SHA-256
  50f86da0acc5c134ffdcc62e499d523174ee0f05cebf5108c1d7a0c7addacec9.

- 2026-09-16T05:20:12+00:00: Recorded command exit 0; command argv SHA-256
  8384c47f3a8ea60f1b7374681501d45cb79764b04aa77ee3c752e86f45f8ba06.

- 2026-09-16T05:20:28+00:00: Recorded command exit 0; command argv SHA-256
  39ebbcca4c6855b468511dc51bcf90e4811b105271b4f5810fa9f081c88b4fca.

- 2026-09-16T05:20:47+00:00: Recorded command exit 0; command argv SHA-256
  ef4ec9599381a7fe5546b4c5a9666cf94842a093998cc2a4b6c10646ba384a89.

- 2026-09-16T05:20:58+00:00: Recorded command exit 0; command argv SHA-256
  7998575a69d7d9771aee1068635e431e10a5864ce5d035fa6a513ce92fe72a35.

- 2026-09-16T05:21:16+00:00: Recorded command exit 0; command argv SHA-256
  533125954338c9d427822c988167a333101210c95ee7c4e2add7f18d1d9ce243.

- 2026-09-16T05:21:32+00:00: Recorded command exit 0; command argv SHA-256
  faec54e70b826dc65f95ca9120eeaa0565c3e631b30fe02645cbed6b1310c418.

- 2026-09-16T05:22:05+00:00: Post-merge run 35058879898 failed because protected-main policy still
  required GitHub Web Flow committer, although local signed merge 7d43c1e is valid. Added signed+DCO
  repair e559888 on top of 7d43c1e: protected-main now verifies allowed SSH signer for local merges
  while retaining historical GitHub Web Flow verification; local policy and focused transcript test
  pass. Published repair PR #185 (head e559888, base 7d43c1e) through handoffctl. PR185 exact-head
  CI: AWQ shadow and source headers green; remaining required checks pending. Next monitor PR185,
  diagnose failures, merge only through local signed path, then rerun post-merge assurance.

- 2026-09-16T05:22:26+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T05:24:27+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T05:24:52+00:00: Lease renewed. Independent exact-head review of PR185 e559888 (base
  7d43c1e) approves one-file policy repair: signed/DCO, diff-check clean, retains historical GitHub
  Web Flow verification while accepting allowed SSH-signed local protected-main merges; local
  protected-main policy and focused transcript test pass. PR185 checks: Loom, platform, retained
  faults, fuzz, mutation, Kani, TLC/Alloy, AWQ, headers green; Rust, emulated AArch64, and
  policy/coverage/supply chain still pending. Next: monitor exact-head checks; after all green,
  merge PR185 using local signed merge_pr path and verify resulting exact-main/post-merge policy.

- 2026-09-16T05:28:59+00:00: Recorded command exit 1; command argv SHA-256
  d7e4e5212ee834d96a9c32dec1456a48e2eb919f5379f5a421383c36d18dc6d6.

- 2026-09-16T05:29:23+00:00: Recorded command exit 0; command argv SHA-256
  3cd876866c0e5f77f12cfe11197aee2d64011b09d5e6dc5a6acc60e03e6fe709.

- 2026-09-16T05:29:41+00:00: Recorded command exit 0; command argv SHA-256
  af7f3198a884ec9cc47dd15b3f4c28f6426b4e6a4c5960690107183e380b54ad.

- 2026-09-16T05:29:50+00:00: Recorded command exit 0; command argv SHA-256
  2686d97084f20cb72cf673a70dd377d0a897674a788497feef8bd5e3e0d08124.

- 2026-09-16T05:30:02+00:00: Recorded command exit 0; command argv SHA-256
  a50d0aa952e7d6ed5c9be79c5a6d15410e94779593ac9b7a0634d8f82402a618.

- 2026-09-16T05:30:22+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T05:30:33+00:00: PR185 policy failure diagnosed:
  test_wrong_committer_and_dco_fail_closed used a GPG-signed disallowed-key fixture, so signature
  validation preceded intended committer assertion. Repair df5a519 adds explicit authorized
  LOCAL_COMMITTER check; unauthorized committer now fails with committer error, while separate
  wrong-signer negatives remain. Full test_signature_policy passes 16/16; commit SSH-signed/DCO and
  pushed via exact lease, PR185 exact head df5a519. Next monitor fresh exact-head CI; if all 12
  green, independently review and merge locally signed, then verify post-merge main policy/DCO.

- 2026-09-16T05:30:36+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T05:31:29+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T05:32:30+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T05:33:34+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T05:33:36+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T05:34:25+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T05:37:34+00:00: Recorded command exit 0; command argv SHA-256
  578dc5947a799e7961e67c671bc0d0fcde13e9f356d223a3154987e117a8bca6.

- 2026-09-16T05:37:56+00:00: Recorded command exit 0; command argv SHA-256
  5a99dbe8fb99aeb92666922cfa400eeb34e79bdbcdd5d93dba0e88d2724bf156.

- 2026-09-16T05:38:15+00:00: Recorded command exit 0; command argv SHA-256
  21e1e3146706dff9f9eae3d0f1c278e5ab673211a8a888837bc51f6887bfd4c8.

- 2026-09-16T05:38:25+00:00: Recorded command exit 1; command argv SHA-256
  572f3af57350c306d1572fac85cc621c00f7bb36e0e1252cb534789d8477f8da.

- 2026-09-16T05:38:51+00:00: Recorded command exit 0; command argv SHA-256
  447a866193c76d0890729affb149af888690bfa8588e22ce8894c3a7a24f92d9.

- 2026-09-16T05:39:08+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T05:39:14+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T05:39:25+00:00: PR185 merged through local signed merge_pr path as protected-main
  fd7daa43549edd67b60076aa6b1eee333061b438. Remote main verification: exact parents 7d43c1e and
  df5a519, exact reviewed tree 5335d2d3, valid allowed SSH signature Martin Beck, matching DCO;
  check_dco against 7d43c1e..fd7daa4 passes. Post-merge assurance for exact fd7daa4: headers and
  hosted portability green; Formal, Rust, emulated AArch64, Fault, and Repository quality runs
  35060286406/418/408/384/401 remain in progress. Earlier invalid DCO range using unfetched second
  parent was diagnosed and corrected. Next monitor all post-merge workflows to terminal; do not
  release AR until each passes.

- 2026-09-16T05:40:21+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T05:41:16+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T05:43:18+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T05:43:51+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T05:45:49+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T05:45:53+00:00: Recorded command exit 0; command argv SHA-256
  dd082f3fa8aca86148d0676b4354ad2aa66d764382d03f1d7196d175f250751c.

- 2026-09-16T05:46:09+00:00: Post-merge exact-main AArch64 run 35060286408 failed in existing
  goose::tests::diagnostic_and_symlink_fail_closed: symlink diagnostic fixture returned Ok
  GooseOutcome(status=Failed, exit_code=127) rather than expected diagnostic error, indicating
  emulated-userspace fixture execution mismatch (likely /bin/sh/fixture launch), not a production
  policy failure. No gate weakened or skipped. Created planned repair AR-1235 with scope limited to
  deterministic Goose fixture portability; dependencies AR-0003, no owner/claim yet. AR-0897 remains
  open pending AR-1235 repair and all post-merge workflows.

- 2026-09-16T05:46:45+00:00: Recorded command exit 0; command argv SHA-256
  537113ef79a064c4a53fa1defe4c4407c7e787c49f5deb0c9d66a234025b1b20.

- 2026-09-16T05:46:54+00:00: Recorded command exit 0; command argv SHA-256
  b3429a8fc9d44e7e10ae361fc06719551bafb33fdbb7de5e9736743b33161347.

- 2026-09-16T05:47:11+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T07:47:34+00:00: Recovered expired claim formerly owned by asb_ar0897_merge_integrity.
  Lease expired at 2026-09-16T07:47:11Z; no matching worker process or heartbeat since 05:47:11Z.
  Preserve PR126 and merge 1c07e907 evidence; reassign signed-DCO protected-main repair for AR-0859
  post-merge policy recovery.

- 2026-09-16T07:47:53+00:00: Claimed by asb_ar0897_merge_integrity.

- 2026-09-16T07:47:56+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T07:48:58+00:00: Recorded command exit 1; command argv SHA-256
  bbd10b63d1155fe8f31187073b2cf951ed28370ca8650289b9b155e72c05d084.

- 2026-09-16T07:49:26+00:00: Recorded command exit 0; command argv SHA-256
  93255dda5d7909f6ba07762fb48dd99c731a15d52f5a1965d88568186f2cfcc5.

- 2026-09-16T07:49:47+00:00: Recorded command exit 0; command argv SHA-256
  232bc8b88bf735de114a7053bfb16692e5baf2034832f866a0ab805dbb529ab4.

- 2026-09-16T07:50:05+00:00: Recorded command exit 0; command argv SHA-256
  01dabd394078f8bed576a0afabdf28ecb397a7d5f6a1f8baf572c4c13f2c1d34.

- 2026-09-16T07:50:34+00:00: Recorded command exit 0; command argv SHA-256
  49178688076588ddf281b25479ae71730ad3115387c262a9a8a8873503fe8c83.

- 2026-09-16T07:50:56+00:00: Recorded command exit 0; command argv SHA-256
  a09512083acb4e4c8848e2c251757e5ddd3b734969f4a835acd7645d7175a586.

- 2026-09-16T07:51:12+00:00: Heartbeat by asb_ar0897_merge_integrity.

- 2026-09-16T07:51:20+00:00: Recovered AR-0897 after expiry. Protected-main run 35069013257 rejected
  published merge 1c07e907 for missing DCO. Added bounded historical evidence to MERGE_INTEGRITY.md
  in signed DCO head bd4f286 rebased onto main 1c07e90, force-with-lease pushed, and opened PR187.
  No history rewritten.
