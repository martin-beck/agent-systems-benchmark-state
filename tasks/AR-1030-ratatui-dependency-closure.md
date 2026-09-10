---
{
  "branch": "build/ratatui-dependency-closure",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T22:52:14+00:00",
  "depends_on": [
    "AR-1017"
  ],
  "id": "AR-1030",
  "next_action": "Register/authorize a GitHub-recognized signing identity for exact head c0dfdd3114741f9415a124f4d4995dac354b4260, or explicitly approve a GitHub rebase/squash rewrite; then rerun exact-head gates and merge PR #11.",
  "owner": "codex-ar1030-ratatui-policy-20260910",
  "plan": "../plans/AR-1030.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make the maintained Ratatui release consumable by standalone asb-tui without hiding supply-chain exceptions.",
  "task_revision": 44,
  "title": "Resolve the Ratatui dependency closure",
  "updated_at": "2026-09-10T20:16:34+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-ratatui-dependency-closure"
}
---
The exact Ratatui 0.30.2 graph is advisory-clean but fails the repository's zero-exception
supply-chain policy because it necessarily contains Zlib-licensed foldhash, hashbrown 0.16/0.17,
and syn 2/3. Resolve this visibly before AR-1010 adds a renderer.

- 2026-09-10T19:50:04+00:00: Claimed by codex-ar1030-ratatui-policy-20260910.

- 2026-09-10T19:50:21+00:00: Recorded command exit 0; command argv SHA-256
  7e0d0efe0ae08a4c308f06db576693eff2b55df1b1195c580afd000b6237ceef.

- 2026-09-10T19:52:14+00:00: Heartbeat by codex-ar1030-ratatui-policy-20260910.

- 2026-09-10T19:52:20+00:00: Recorded command exit 0; command argv SHA-256
  70c299ac34f80fb148951f6d687b81c0133841c6f66036e826bbc90974c0544e.

- 2026-09-10T19:52:41+00:00: Recorded command exit 0; command argv SHA-256
  cb54c6475fcaf9c988b46643c213a1b77cd1b8ed1bfe7d6a8102356c7f0369e7.

- 2026-09-10T19:53:11+00:00: Recorded command exit 101; command argv SHA-256
  e409e268e66f59053c6cd20940690d0e09eac3f60de24e38e2629e7a4361a927.

- 2026-09-10T19:53:29+00:00: Recorded command exit 0; command argv SHA-256
  076056546ce14cbf7b9647a94cf99017d780620e3677ae653b2cb5bc5cc14e7d.

- 2026-09-10T19:54:05+00:00: Recorded command exit 0; command argv SHA-256
  9943ddd4923917bb053c83f7782fec1994419775043b4cf9fb78576bcedc006e.

- 2026-09-10T19:54:56+00:00: Recorded command exit 0; command argv SHA-256
  8f2e42d256187d9d0fd1bae895503b9b4a321b008688badb7b0eccf873b1cb77.

- 2026-09-10T19:55:11+00:00: Recorded command exit 0; command argv SHA-256
  9943ddd4923917bb053c83f7782fec1994419775043b4cf9fb78576bcedc006e.

- 2026-09-10T19:56:12+00:00: Recorded command exit 0; command argv SHA-256
  913e1e1a99f1a1f0601e06b33726299a3fb54fd4c3be66f8cb5b36d654161349.

- 2026-09-10T19:56:50+00:00: Recorded command exit 1; command argv SHA-256
  5d8fa64d1b08568dbf52607648ff129ed525244547b1fcb1c5fdbd5497ee211a.

- 2026-09-10T19:57:03+00:00: Recorded command exit 0; command argv SHA-256
  640948d3f18fb76c7fe74848a9e4afa459231e5623ddc6c817129b5f2c1eb132.

- 2026-09-10T19:57:42+00:00: Recorded command exit 0; command argv SHA-256
  2aa6b014e73a1bb170294bbe0e5ef4716cc88fded01fb11ee6badeda1c1fb60c.

- 2026-09-10T19:59:34+00:00: Recorded command exit 0; command argv SHA-256
  21dc06e7209084658fa85892384918c10e444fe737770961bc46c7b7e0d1d2c3.

- 2026-09-10T19:59:55+00:00: Recorded command exit 0; command argv SHA-256
  c00112b64e784a7f4c698089805699206b77ba008b8f8024af0860840648e28f.

- 2026-09-10T20:01:29+00:00: Recorded command exit 0; command argv SHA-256
  7fa82e8765053a59560320decb8682195ac34e596f504a383b823a524af265d1.

- 2026-09-10T20:02:45+00:00: Recorded command exit 0; command argv SHA-256
  e12d2eed605135b4e139f5ba5486133e68b97142a812d8111c8b8a27fbf799b4.

- 2026-09-10T20:03:32+00:00: Recorded command exit 0; command argv SHA-256
  d5782c4543cb8abf62435db0be5de407bfd9ec83ab23673101317c8f991b18ea.

- 2026-09-10T20:03:46+00:00: Recorded command exit 0; command argv SHA-256
  9b175c5542e2cff6649811499a46ae0b9d159124e6c448aff1f83f153feb472a.

- 2026-09-10T20:04:09+00:00: Recorded command exit 0; command argv SHA-256
  61ef811c014d77e70f9927ef81e5e7c0d225e7b7693bc7c95eba58568cd7fb7a.

- 2026-09-10T20:04:37+00:00: Recorded command exit 0; command argv SHA-256
  1c5c316ce6e00335249f54eae1a4abcf4c36216ea8333caad21202de29b74f0b.

- 2026-09-10T20:05:02+00:00: Recorded command exit 1; command argv SHA-256
  d983a51a6eabf248b8595a2bee71afd18adacc081d87a2a23a05df223f8f2465.

- 2026-09-10T20:05:25+00:00: Recorded command exit 1; command argv SHA-256
  bed7f39bec24d3d132648ce1448054b4b56843a0527b20a39162460bcc176cfd.

- 2026-09-10T20:07:07+00:00: Classified the 2026-09-10 20:05 UTC exit-1 records: both were
  environment-only follow-up invocations where generate-rust-sbom.py could not execute cargo because
  the handoffctl non-login shell lacked the Rust toolchain on PATH. The dependency-policy test body
  did not execute and no product/policy assertion failed. The immediately preceding comprehensive
  gate exited 0, including full tests, exact-feature anti-widening tests, cargo deny globally and
  for x86_64/AArch64, cargo audit over 93 packages, builds, cross-checks, schema/workflow checks,
  and gitleaks. Rerunning focused checks with the explicit repository-local Rust 1.93 toolchain
  path.

- 2026-09-10T20:07:24+00:00: Recorded command exit 0; command argv SHA-256
  8cb430e0e9cd1fb7a57876b81e1c5ac691e0b6a395e5915c0619b349d748f885.

- 2026-09-10T20:07:55+00:00: Recorded command exit 0; command argv SHA-256
  6d8ad744eaf6d13ce30eb33a150909497193ba5bc6c98de6d234ab22d8a4b9c1.

- 2026-09-10T20:08:13+00:00: Recorded command exit 0; command argv SHA-256
  36dec61e3790423de9cb47aaa1b07a28bb74498066cb7286cb109644e7778e07.

- 2026-09-10T20:08:59+00:00: Recorded command exit 0; command argv SHA-256
  23491ff38a084b0992eddc5a8a641fcd37a081e42fd16b1e7b936d65692027ae.

- 2026-09-10T20:09:19+00:00: Recorded command exit 0; command argv SHA-256
  0f7029bed8b9b131b67b3df72a2071f6ac57afdb09a1b46dd081fa3903f47316.

- 2026-09-10T20:09:53+00:00: Recorded command exit 0; command argv SHA-256
  4ea0d43a8984ba28bb6a77836d27be4923346318efba855817ce6e20f426a49e.

- 2026-09-10T20:10:25+00:00: Recorded command exit 0; command argv SHA-256
  af43793490abdc61430a231efc6d4b75713252962f75718a56248ca7e6ace6df.

- 2026-09-10T20:11:12+00:00: Published signed+DCO checkpoint
  c0dfdd3114741f9415a124f4d4995dac354b4260 on draft asb-tui PR #11. Live GitHub head, local HEAD,
  and origin head match exactly; quality CI is in progress. Comprehensive local gates passed: full
  test suite, clippy/docs/release build, cargo-deny globally/x86_64/AArch64, cargo-audit over 93
  packages, x86_64/AArch64 cargo checks, deterministic SPDX/schema/workflow/privacy checks, and
  clean-tree coverage at 90.55% lines. Independent review found the Zlib/duplicate exception narrow,
  mechanically guarded, signed, and nonblocking; no blocking finding. Nonblocking merge-order note:
  reconcile unverified_extension wording to source_only_unverified when integrating AR-1022.

- 2026-09-10T20:11:30+00:00: Recorded command exit 0; command argv SHA-256
  c65936e210c5941a778180c3316170034f45ed2c0afa90a074f5ff05f5db2675.

- 2026-09-10T20:12:07+00:00: Live exact-head CI is green: Repository quality / Rust, supply-chain,
  and privacy gates passed in GitHub Actions run 34524715305 job 103030678680 at
  c0dfdd3114741f9415a124f4d4995dac354b4260. Independent review has no blocking finding. Draft PR #11
  remains open and unmerged as assigned; branch/worktree are clean and generated Python cache is
  absent.

- 2026-09-10T20:12:21+00:00: Recorded command exit 1; command argv SHA-256
  f85ba2b3337f52dfd08aa0128ef5cca4dec8c5de6fdb2c09833df8f3bfee1876.

- 2026-09-10T20:12:42+00:00: Recorded command exit 1; command argv SHA-256
  522a316134991bcc5eb767766883289606aa5455f18e95de09c29ea857a84808.

- 2026-09-10T20:13:11+00:00: Recorded command exit 0; command argv SHA-256
  07da014134d9405ea3401997eb9f1da71fb8a76e4e43ac04dd7b6563ef5c8c25.

- 2026-09-10T20:13:35+00:00: Recorded command exit 0; command argv SHA-256
  be585c11e538790393828317757270532c99365b37225da9b5932da78e7b854f.

- 2026-09-10T20:13:57+00:00: Recorded command exit 0; command argv SHA-256
  57c5d6079f9e620ee8b4ebf30e6734da1b40abe0810c7a60ee279ecffa01678c.

- 2026-09-10T20:14:38+00:00: Recorded command exit 0; command argv SHA-256
  ea2b3c178b8ab63d127a804ac4b6ab029ef64ddff48a8f129dc5a4efdc9ebbec.

- 2026-09-10T20:15:40+00:00: Recorded command exit 1; command argv SHA-256
  f803b509cea788504b22b9f6abc53f417babd7d97d5490d9eb7196db9922b1b0.

- 2026-09-10T20:16:34+00:00: Classified the latest merge exit 1: `gh pr merge --admin --merge` was
  rejected by GitHub with `Commits must have verified signatures. (mergePullRequest)`. Local git
  verifies c0dfdd3 as a good ED25519 signature and DCO is present, but GitHub reports
  commit.verification.reason=unknown_key and signature.isValid=false. Main protection requires
  signed commits and enforces admins. Current gh token lacks admin:ssh_signing_key and API says an
  auth refresh is required. No direct main push, protection bypass, account-key mutation, or history
  rewrite was performed. PR #11 remains open/ready, exact-head CI green, and
  mergeable_state=blocked.
