---
{
  "branch": "fix/main-merge-integrity",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0003"
  ],
  "id": "AR-0897",
  "next_action": "Monitor PR 126 exact-head CI; investigate terminal failures without changing bd6f450.",
  "observed_branch": "fix/main-merge-integrity",
  "observed_dirty": 0,
  "observed_head": "bd6f450ab8777aeb7e055d71aedba8e4cfd375b3",
  "owner": "",
  "plan": "../plans/AR-0897.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Repair the current main merge-boundary failure and enforce a signed DCO-bearing integration path.",
  "task_revision": 41,
  "title": "Restore main merge integrity",
  "updated_at": "2026-09-09T23:41:59+00:00",
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
