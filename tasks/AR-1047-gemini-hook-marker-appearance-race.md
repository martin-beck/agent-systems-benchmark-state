---
{
  "branch": "fix/gemini-hook-marker-appearance-race",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T03:59:36+00:00",
  "depends_on": [],
  "id": "AR-1047",
  "next_action": "PR #139 exact 661d52c/tree 3931f7cb is independently approved and 12/12 exact-head green; await explicit root authorization and exact multiline protected merge recipe.",
  "observed_branch": "fix/gemini-hook-marker-appearance-race",
  "observed_dirty": 0,
  "observed_head": "661d52c614c5cfa28859d71131fbc8158b68bc2d",
  "owner": "codex-ar1047-gemini-marker-race-20260911",
  "plan": "../plans/AR-1047.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Treat a regular marker published between absent open and fallback lstat as pending for descriptor validation on the next poll.",
  "task_revision": 30,
  "title": "Close the Gemini hook-marker appearance race",
  "updated_at": "2026-09-11T02:17:57+00:00",
  "worktree_key": "agent-systems-benchmark-gemini-hook-marker-appearance-race"
}
---

Three AArch64 runs failed different Gemini fixtures with `HookUnavailable`, including serialized
PR #138 run `34552034116`. Repair only the race where a valid regular marker appears after
`open(O_NOFOLLOW)` reports `NotFound` but before fallback lstat. A regular appearance is `Pending`
and must be reopened and fully validated on the next poll; symlink and non-regular appearances
remain `Invalid`. Add an exact deterministic interposition test and preserve all existing checks.

- 2026-09-11T01:59:34+00:00: Root approved the exact one-file marker-appearance interleaving plan as
  written.

- 2026-09-11T01:59:36+00:00: Claimed by codex-ar1047-gemini-marker-race-20260911.

- 2026-09-11T01:59:47+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-09-11T01:59:56+00:00: Recorded command exit 0; command argv SHA-256
  cb829e9c4e7c7cffe24d5a6161df617fb253eb697a3402baff2975d02e925261.

- 2026-09-11T02:00:04+00:00: Recorded command exit 0; command argv SHA-256
  fcafd29cc68cb7dbd13e99fe2391391b29bf9302ac0c501b264c59c4834ca48e.

- 2026-09-11T02:00:29+00:00: Recorded command exit 0; command argv SHA-256
  43f59574834ad539779c2727cb24b7d5704fc0bdd73bb76e68d8a0d322781699.

- 2026-09-11T02:01:46+00:00: Recorded command exit 0; command argv SHA-256
  eab0eb51b6437f5b683d21ce60a8436b66728ad9f49f727b18d018281022025a.

- 2026-09-11T02:02:22+00:00: Recorded command exit 0; command argv SHA-256
  7d1f2c18f58bddea4de2fddfa84218fd7a05ae7904c2b196873aff8ac0874071.

- 2026-09-11T02:04:49+00:00: Recorded command exit 0; command argv SHA-256
  a9234b0594253e4774881e3692319fe510ca6b843ab86c61b4923d2863e308d3.

- 2026-09-11T02:06:19+00:00: Recorded command exit 0; command argv SHA-256
  4796e8088a88927375b021860f912b67fd9a20b124199a5a466ce4fc17b1b322.

- 2026-09-11T02:06:40+00:00: Recorded command exit 0; command argv SHA-256
  548676ec12f29b1f0d808147e73bb42b4e018a0800eaabc52a0b7f1a47d2bdb0.

- 2026-09-11T02:06:50+00:00: Recorded command exit 0; command argv SHA-256
  0c925fdf5306d3bb8e267dbb4fde0c4e47b63bdcdca2eea227337fa850297039.

- 2026-09-11T02:07:02+00:00: Recorded command exit 0; command argv SHA-256
  cf7469fa56d890bc336466eb6467036f7d465f4b89d18cde2cc62e15ecd8b657.

- 2026-09-11T02:07:21+00:00: Recorded command exit 0; command argv SHA-256
  345999de03cd6797d9bcc9fb09e6f991d08b13ece6cf4b6e46cce4e9de5ee4b0.

- 2026-09-11T02:07:46+00:00: Frozen clean one-file signed+DCO successor
  661d52c614c5cfa28859d71131fbc8158b68bc2d, tree 3931f7cb300f1138a1fb2be7493991c03647c1c5, parent
  exact main 2ecb876b82a91a8103926b298c42ad49ce8dd143. Exact interposition uses bounded rendezvous
  after O_NOFOLLOW open NotFound and before lstat: valid atomic rename returns Pending then
  descriptor-validated Ready; dangling symlink returns Invalid. Exact test 100/100 and full
  serialized Gemini module 20/20. Full fmt, clippy, workspace tests, rustdoc, release, deny, audit,
  coverage, contract, actionlint, zizmor, gitleaks, controlled failures, signature, artifact,
  manifests and 57 platform tests pass. Earlier exit 1 fmt check was a mechanical layout finding
  before tests; 0-test exact filters were invalid evidence due omitted gemini::tests:: prefix and
  were corrected to 1/1 each.

- 2026-09-11T02:09:43+00:00: Recorded command exit 0; command argv SHA-256
  0e7d5419f9cb1c6faa517b04b489ecd4b87d4e135912302a508d3157f564e3db.

- 2026-09-11T02:09:53+00:00: Recorded command exit 0; command argv SHA-256
  d4daa54cbb19b0447840c6f49e799fffa45b0cb63326a663b273eab88bdf22f1.

- 2026-09-11T02:10:19+00:00: Recorded command exit 0; command argv SHA-256
  3979ecc44022bf1dae73bab38afa4063fcef04ee190a5c66c840b4983a54abc3.

- 2026-09-11T02:10:56+00:00: Recorded command exit 8; command argv SHA-256
  eb2fc0ac66f5cefb1d734155f65266ab3b95a8afe2adb889d2de53deefad341a.

- 2026-09-11T02:13:18+00:00: Recorded command exit 8; command argv SHA-256
  eb2fc0ac66f5cefb1d734155f65266ab3b95a8afe2adb889d2de53deefad341a.

- 2026-09-11T02:15:38+00:00: Recorded command exit 0; command argv SHA-256
  eb2fc0ac66f5cefb1d734155f65266ab3b95a8afe2adb889d2de53deefad341a.

- 2026-09-11T02:16:00+00:00: PR #139 exact-head CI is terminal 12/12 green. Emulated AArch64 run
  34553546358/job 103121253796 passed in 5m27s; Repository quality 34553546334 and Rust 34553546331
  pass, with all formal/fault/platform/header/AWQ checks passing. Remote PR remains base
  2ecb876/head 661d52c/tree 3931f7cb. No merge performed.

- 2026-09-11T02:16:24+00:00: Recorded command exit 0; command argv SHA-256
  ccdad4e176aad6671671a63d8e75ebcb37cbabab6dfd07245b02b01a304d6242.

- 2026-09-11T02:17:18+00:00: Recorded command exit 0; command argv SHA-256
  93e3086ab41f37983ccb47b626f9b38beffe3ee4c150845b7ac518034d6092bd.

- 2026-09-11T02:17:41+00:00: Recorded command exit 0; command argv SHA-256
  1830c43eb0accbf62689dfb084ca118485aece04c54ec54ad06b92b8141197fa.

- 2026-09-11T02:17:57+00:00: Recorded command exit 0; command argv SHA-256
  1dac593b3f627da0b5b2643bfe8fefb4a1adc7ea89a6ad275f70066b1c825b50.
