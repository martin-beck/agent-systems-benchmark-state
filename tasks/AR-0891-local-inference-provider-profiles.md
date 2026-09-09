---
{
  "branch": "feat/local-inference-provider-profiles",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T11:41:25+00:00",
  "depends_on": [
    "AR-0879",
    "AR-0312",
    "AR-0313",
    "AR-0315"
  ],
  "id": "AR-0891",
  "next_action": "Create and push a signed no-ff merge object from the claimed feature worktree (worktree-fence-safe), then verify GitHub marks PR #114 merged and run post-merge exact-main checks.",
  "observed_branch": "feat/local-inference-provider-profiles",
  "observed_dirty": 0,
  "observed_head": "eed49592617a0a712482d4a341ae7b1f802fe04f",
  "owner": "codex-longrun-local-inference-profiles-20260909",
  "plan": "../plans/AR-0891.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Extend ASB local inference through evidence-backed profiles rather than one speculative adapter task per server.",
  "task_revision": 114,
  "title": "Qualify local inference provider profiles",
  "updated_at": "2026-09-09T09:42:09+00:00",
  "worktree_key": "agent-systems-benchmark-local-inference-provider-profiles"
}
---
## AR-0891

Use exact Ollama, llama.cpp, vLLM and LocalAI sources in `docs/LOCAL_LLM_TESTING_RECOMMENDATIONS.md`; qualify only profiles filling an ASB need.

- 2026-09-09T08:33:38+00:00: Dependencies AR-0879, AR-0312, AR-0313, and AR-0315 are released done;
  promote grouped local inference provider profiles. AR-0890 remains unclaimable until AR-0888
  selects a qualifying executable candidate.

- 2026-09-09T08:33:41+00:00: Claimed by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T08:33:44+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T08:33:47+00:00: Recorded command exit 0; command argv SHA-256
  c9938d78e9318920e75494dd836f1fdec89a162bd75e309dc02b597001ca51c3.

- 2026-09-09T08:36:17+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T08:36:19+00:00: Recorded command exit 0; command argv SHA-256
  38f607d45df87159b5d45c6b3f81b10a23f9e07e54cb16b9642f814bf3595426.

- 2026-09-09T08:40:14+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T08:40:16+00:00: Recorded command exit 1; command argv SHA-256
  eae2353e008b14765573c3a727caea6abc0d5a6f5a41d96dae7cc21edbb18a64.

- 2026-09-09T08:40:52+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T08:40:55+00:00: Recorded command exit 1; command argv SHA-256
  eae2353e008b14765573c3a727caea6abc0d5a6f5a41d96dae7cc21edbb18a64.

- 2026-09-09T08:41:13+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T08:41:17+00:00: Recorded command exit 0; command argv SHA-256
  ab1fa736790ffddd7b0f2e0b666555ce6c819ae6c665d808e1e872a15ca39bf5.

- 2026-09-09T08:41:43+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T08:41:59+00:00: Milestone: added tools/local-inference-profiles/profiles-v1.json plus
  fail-closed validator, hostile tests, and documentation. All four grouped profiles are explicitly
  unqualified/non-selectable because complete model/tokenizer/runtime/hardware/repeated-trial
  evidence is not yet present; no runtime support was overclaimed. Focused tests, Ruff, strict mypy,
  canonical digest, and diff-check pass.

- 2026-09-09T08:42:23+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T08:43:04+00:00: Recorded command exit 0; command argv SHA-256
  e0df5bf2a62e0de12285f5969115c8cfc0331e1d14c3177b3be78432a8efeaf6.

- 2026-09-09T08:43:31+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T08:43:34+00:00: Recorded command exit 0; command argv SHA-256
  080185c8d968f46cd7789481e03e62a98a54caa380b72f69e34df33b923365fa.

- 2026-09-09T08:43:48+00:00: Recorded command exit 0; command argv SHA-256
  0c3ad7ec952af1ec139144d42f8370f2479a6d8daa65fc6194c0e2b4a4837aae.

- 2026-09-09T08:44:04+00:00: Recorded command exit 0; command argv SHA-256
  d015d3f8d98882deda8500e152b07ee32a07c6348cbcd0288313ff4d01d8b0d0.

- 2026-09-09T08:44:20+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T08:44:24+00:00: Recorded command exit 0; command argv SHA-256
  f0652f39c24417e411e4fe62ba100e4254077ab1303484e4e5fb6697340a8d7a.

- 2026-09-09T08:44:43+00:00: Recorded command exit 0; command argv SHA-256
  5c87af4465969aba263da212af6c31baf456620d7c9592797a518920e4109c34.

- 2026-09-09T08:45:22+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T08:46:08+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T08:47:17+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T08:49:15+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T08:49:18+00:00: Verified PR #111 exact head 772c6277c99354e8685aee73fafa2c957a3eb9c8:
  all 14 required checks passed, including both Rust runners, emulated aarch64, policy/supply chain,
  fault/fuzz/mutation, formal, headers, and AWQ shadow evidence. Local focused and full Rust gates
  also passed.

- 2026-09-09T08:49:46+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T08:49:51+00:00: Recorded command exit 0; command argv SHA-256
  08d2813a11a229929c0450cc842a05b0c3671da0a0fd872c74d7741288d1f80c.

- 2026-09-09T08:50:15+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T08:51:40+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T08:53:12+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T08:54:32+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T08:57:06+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T08:57:09+00:00: Recorded command exit 1; command argv SHA-256
  8c8103c22bf212a8e93e36540a1bfaced814ed74893809a694f8e0a32e0d8303.

- 2026-09-09T08:57:28+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T08:57:35+00:00: Recorded command exit 0; command argv SHA-256
  f7f76ec70b6e516cec16e651a90dccf2374239ecb75d0bdf6526a16a95f1d083.

- 2026-09-09T08:57:59+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T08:58:06+00:00: Recorded command exit 0; command argv SHA-256
  cc2ac50fa5a7d91eaaca3c915ea78fa2ac6a954383f79d07a02d753e9a4213ab.

- 2026-09-09T08:58:42+00:00: Recorded command exit 0; command argv SHA-256
  396bfd08062e790096a38c253b812946ea3b244df44731659a0d28bd6e576610.

- 2026-09-09T08:58:58+00:00: Recorded command exit 0; command argv SHA-256
  2712e0edc4690ae6f924c587a70fe3d366077aa1019465967f92d9a16bc4da89.

- 2026-09-09T08:59:17+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T08:59:22+00:00: Recorded command exit 0; command argv SHA-256
  20ff7ac6b7a4d470d9af9e971441d3ae6616a138242552f83279944325883aa6.

- 2026-09-09T08:59:40+00:00: Recorded command exit 0; command argv SHA-256
  a9f67aa3815c044481122199f86a356b9316345b6a8509426a928220c8865ad0.

- 2026-09-09T09:00:03+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:01:31+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:02:53+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:05:00+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:05:54+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:05:58+00:00: PR #113 exact-head CI is fully green: all 14 checks passed, including
  emulated aarch64, both Rust runners, policy/supply chain, fault/fuzz/mutation, formal, headers,
  and AWQ shadow.

- 2026-09-09T09:06:12+00:00: Recorded command exit 0; command argv SHA-256
  566fa5285348b71d6e713bbeda965b018085284c0ac0593b60d0b670513e9ce9.

- 2026-09-09T09:06:37+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:08:04+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:10:24+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:12:52+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:12:54+00:00: Post-merge exact-main verification for merge
  cd350831486d22f39e77e04daf2206625f7e4119 is fully green across all six workflows. The ignored
  native Ollama read-only probe passed exact binary, server, and model pins; manifest records this
  partial evidence but AR-0891 remains in progress because tokenizer and repeated-variability
  evidence are missing and no other engine has a qualified artifact.

- 2026-09-09T09:14:43+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:15:08+00:00: Recorded command exit 0; command argv SHA-256
  bba3b92764534f67209703cee821de159280f34afd9f0f6233eae18345ae20f0.

- 2026-09-09T09:15:28+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:15:31+00:00: Recorded command exit 0; command argv SHA-256
  d13aac54c6f2c50ec11eb710812a7365073a9e7f9151c9960dd396eb241c367d.

- 2026-09-09T09:17:19+00:00: Recorded command exit 1; command argv SHA-256
  ffdd53803189288ea2917aba0fb2a4a047970c6500eedfbdc6c136d4fd055799.

- 2026-09-09T09:17:50+00:00: Recorded command exit 1; command argv SHA-256
  ffdd53803189288ea2917aba0fb2a4a047970c6500eedfbdc6c136d4fd055799.

- 2026-09-09T09:18:15+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:18:18+00:00: Recorded command exit 0; command argv SHA-256
  ffdd53803189288ea2917aba0fb2a4a047970c6500eedfbdc6c136d4fd055799.

- 2026-09-09T09:19:50+00:00: Recorded command exit 0; command argv SHA-256
  c92feb1d27aeca3afe7504d041a6f83e3e4872951d83d2d1ff7b1857faff83d2.

- 2026-09-09T09:20:08+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:20:11+00:00: Recorded command exit 0; command argv SHA-256
  65f971df3ee08f59359d125c98938b466e1bafd579fed25be4e51e6e1014ce48.

- 2026-09-09T09:20:31+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:20:38+00:00: Recorded command exit 0; command argv SHA-256
  a48def94002962738ee445a87a5d7429fac56ad78ee623d569c6de9d12b6b5e1.

- 2026-09-09T09:21:05+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:22:34+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:24:04+00:00: CI failure preempted feature work: PR #114 policy/coverage/supply-chain
  run 34334165543 failed only in Gitleaks. Local exact-range reproduction identified generic-api-key
  false positive at profiles-v1.json:77 on the public tokenizer_sha256 content digest; no credential
  was present. Added a narrowly path/field-scoped .gitleaks.toml allowlist and local exact-range
  scan now reports no leaks. Do not merge until a new exact-head CI run is green.

- 2026-09-09T09:24:19+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:24:22+00:00: Recorded command exit 0; command argv SHA-256
  1355ed50976c326cc3ced73ad382b6e7b2d4a33e2f55f69d6e0d21d00b1d668f.

- 2026-09-09T09:24:39+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:24:45+00:00: Recorded command exit 0; command argv SHA-256
  20ff7ac6b7a4d470d9af9e971441d3ae6616a138242552f83279944325883aa6.

- 2026-09-09T09:25:08+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:26:35+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:28:01+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:29:32+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:31:22+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:31:24+00:00: Repaired policy CI failure with a narrowly scoped .gitleaks.toml
  exception for the public tokenizer_sha256 content digest. Exact-range Gitleaks reports no leaks,
  and all 14 PR #114 checks are now green.

- 2026-09-09T09:31:38+00:00: Recorded command exit 1; command argv SHA-256
  caf1c177859eab71cef1d212133a9be19e9dadf21ee14d7b68242be6bb437cc7.

- 2026-09-09T09:32:28+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:32:42+00:00: Merge command was safely prevented because origin/main advanced to
  2a85872285e6de374e7ea48e3b062e4134bec49e2 via independently merged PR #112 while PR #114 was
  running. Product main remains clean at cd350831; no mutation occurred. Rebase the feature branch
  before merging.

- 2026-09-09T09:33:06+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:33:11+00:00: Recorded command exit 0; command argv SHA-256
  62a33f21fb9d280b697ca7e6147a77688011cc469ff41b85a73f7ea0ea3b2298.

- 2026-09-09T09:33:37+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:35:06+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:36:32+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:38:03+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:39:46+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:39:48+00:00: Rebased PR #114 after concurrent PR #112 advanced main. Exact-head CI
  on eed49592617a0a712482d4a341ae7b1f802fe04f is fully green across all 14 checks; the prior
  Gitleaks false positive remains repaired by the narrow allowlist.

- 2026-09-09T09:40:08+00:00: Recorded command exit 1; command argv SHA-256
  660b6fe3aa50a94de9218235e8434fee0f2bf498738215506bd695a8bb7af256.

- 2026-09-09T09:41:25+00:00: Heartbeat by codex-longrun-local-inference-profiles-20260909.

- 2026-09-09T09:41:29+00:00: The normal main-worktree merge command exited 1 because upstream
  worktree fencing correctly rejects a claimed AR-0891 worker mutating the separate product-main
  worktree. Main remains clean at cd350831 and origin/main is 2a858722; use a signed commit-tree
  merge/push from the declared feature worktree with an exact main-ref lease.

- 2026-09-09T09:41:42+00:00: Recorded command exit 1; command argv SHA-256
  10a777f2b9edd1bf5835c16fd35d008345afbc63034638c6bce108599d810cad.

- 2026-09-09T09:42:09+00:00: Recorded command exit 0; command argv SHA-256
  804e64de4dbb4745a8e13864573f8f74c5a2e3ad603ad5146cd0a8b4f2014d96.
