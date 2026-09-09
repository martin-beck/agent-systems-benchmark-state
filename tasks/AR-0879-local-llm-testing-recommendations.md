---
{
  "branch": "docs/local-llm-testing-recommendations",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T08:14:36+00:00",
  "depends_on": [
    "AR-0312",
    "AR-0313",
    "AR-0315",
    "AR-0501",
    "AR-0502",
    "AR-0503",
    "AR-0504",
    "AR-0505",
    "AR-0871"
  ],
  "id": "AR-0879",
  "next_action": "Obtain independent exact-head review of green product PR 107 at bda6cc8a and state PR 16 at 9de11a52; state global schema remains pre-existingly blocked only by active AR-0878 next_action length.",
  "observed_branch": "docs/local-llm-testing-recommendations",
  "observed_dirty": 0,
  "observed_head": "9686cef457b1355a48c9c814763649f912abce45",
  "owner": "codex-asb-local-llm-research-20260909",
  "plan": "../plans/AR-0879.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Research deterministic LLM test doubles and local inference options, document ASB recommendations, and create implementation-ready follow-up ARs.",
  "task_revision": 45,
  "title": "Plan deterministic LLM doubles and local inference",
  "updated_at": "2026-09-09T07:04:08+00:00",
  "worktree_key": "agent-systems-benchmark-local-llm-testing-recommendations"
}
---
## AR-0879

Research and document how ASB should use deterministic LLM test doubles and local inference without
confusing either with its existing strict recorded-response replay or with qualified live-provider
evidence.

Evaluate pinned public revisions of MockAgents, CopilotKit aimock, larsakerlund llmock, the
piyook/llm-mock naming-adjacent project, Ollama, llama.cpp, vLLM, and LocalAI. Relate their claims
to AgentRR (arXiv:2505.17716), Deterministic Replay for AI Agent Systems (arXiv:2607.16200),
Automated structural testing of LLM-based agents (arXiv:2601.18827), and the empirical
over-mocking warning in arXiv:2602.00409. Inspect ASB AR-0312/0313/0315, AR-0501..0505, and
AR-0869..0874 before recommending work.

Deliver a substantive product research/setup recommendation and full-detail dependency-ordered ARs.
Preserve separate CLI and TUI boundaries, classify synthetic, recorded, and live inference evidence
honestly, and do not implement a simulator, mock server, inference backend, or unshipped UI.

- 2026-09-09T06:14:36+00:00: Claimed by codex-asb-local-llm-research-20260909.

- 2026-09-09T06:14:50+00:00: Recorded command exit 0; command argv SHA-256
  46380aaefebf880dc2aeb08da22adf406054c53db8418039b43a06336b5bb302.

- 2026-09-09T06:20:45+00:00: Recorded command exit 128; command argv SHA-256
  2ee8da51b9eff4ada8a7bffa290d803f1e0efc95f87f479b7acbdb4a7bbecfc5.

- 2026-09-09T06:22:46+00:00: Recorded command exit 128; command argv SHA-256
  2ee8da51b9eff4ada8a7bffa290d803f1e0efc95f87f479b7acbdb4a7bbecfc5.

- 2026-09-09T06:24:30+00:00: Recorded command exit 128; command argv SHA-256
  2ee8da51b9eff4ada8a7bffa290d803f1e0efc95f87f479b7acbdb4a7bbecfc5.

- 2026-09-09T06:26:18+00:00: Recorded command exit 128; command argv SHA-256
  0353447544a786da2037a384b923bbfa7279262de687c0689ee5dd9571de6cf9.

- 2026-09-09T06:27:04+00:00: Recorded command exit 128; command argv SHA-256
  27dff63ec1eb0fd5ff357feea8f2f7455cbc84da04f8bbd2d1c64c794d94b3c8.

- 2026-09-09T06:27:25+00:00: Recorded command exit 128; command argv SHA-256
  752a908eecc8aced640fb8110eaf9db70b6600f95f04d76fe554e0d86f07fd5c.

- 2026-09-09T06:27:50+00:00: Recorded command exit 0; command argv SHA-256
  752a908eecc8aced640fb8110eaf9db70b6600f95f04d76fe554e0d86f07fd5c.

- 2026-09-09T06:28:00+00:00: Recorded command exit 0; command argv SHA-256
  34f20f11235407dae5d98d0dac4fa5f50b16e24018be79ac9f49026203bc123f.

- 2026-09-09T06:28:19+00:00: Recorded command exit 0; command argv SHA-256
  29bb576df3f4a8059e5e307e54faab9eb1ad739bae5a2a9192790e9f9316ddc6.

- 2026-09-09T06:35:22+00:00: Recorded command exit 0; command argv SHA-256
  493f5258e0ea4a912a607b6b496b747dd4c46a866b6d698e83b013afa6b4e5b6.

- 2026-09-09T06:37:00+00:00: Recorded command exit 0; command argv SHA-256
  d08688a95e70a37b8ce9cf5434552634aaf5dc9438923d34bff59eb44fbba2ca.

- 2026-09-09T06:39:18+00:00: Recorded command exit 1; command argv SHA-256
  272f98fac9b70c7c526a9ef38529a7cc5b5b0f3a9fe93fb7debc8cc2abb029da.

- 2026-09-09T06:39:51+00:00: Recorded command exit 1; command argv SHA-256
  ba05b898783840258aaabeaa131f72f2663b41d7a5adcd86b8f11b41efb90e66.

- 2026-09-09T06:40:49+00:00: Recorded command exit 128; command argv SHA-256
  8b961b1bb027c76345934c44bc313fd428bea1e37f6c96c9544b591b8f65faeb.

- 2026-09-09T06:41:31+00:00: Recorded command exit 0; command argv SHA-256
  ef31c67c7156650c8ee4ae46507c4b20105091135bb38296e54d36ae9146e9fe.

- 2026-09-09T06:41:40+00:00: Recorded command exit 0; command argv SHA-256
  0cceecc1ec1fb1d57bb825ecd268c9adb15b8c5e4060636bdf23a60bc04a15b6.

- 2026-09-09T06:42:07+00:00: Recorded command exit 127; command argv SHA-256
  ffbbec096b58302b36ca233a2e81e683fa2da5696d28caf082e2e125875c9dd8.

- 2026-09-09T06:42:31+00:00: Recorded command exit 127; command argv SHA-256
  e46d608b65da66c7ea501f1151682b9ca42eb606ba899799e586466c17ce8ed2.

- 2026-09-09T06:45:06+00:00: Recorded command exit 0; command argv SHA-256
  dea051a96767a228ffeb04d1ba903ba11e8ff939405b69ba9803610c2db9aa5f.

- 2026-09-09T06:45:51+00:00: Recorded command exit 0; command argv SHA-256
  9e07d8412edd3bf459a806670755426be99598fba0e28a265e40a48b8fe2cd45.

- 2026-09-09T06:46:16+00:00: Recorded command exit 0; command argv SHA-256
  4d6844c1090027d720b663a83bf7f7dba65a5d60672e1ef77735c883b48cf961.

- 2026-09-09T06:47:04+00:00: Recorded command exit 0; command argv SHA-256
  228739c55b289075b83e63985f5c813cab3e512cd170621057a31b3b0f0db0ec.

- 2026-09-09T06:47:31+00:00: Recorded command exit 0; command argv SHA-256
  9dad03488ec45dfac20e11271ba37d37feffd22b1aa8e9002241a486b45f24bb.

- 2026-09-09T06:47:53+00:00: Recorded command exit 0; command argv SHA-256
  5bc8238dbd2a270c86e8d16f6bae9fc221ed8f5198fe637b856f6a437f2d85c5.

- 2026-09-09T06:49:29+00:00: Recorded command exit 127; command argv SHA-256
  61477b4e8bb42a5de99864396ca557548411aa32178701f11a7cfb05efe0dbc1.

- 2026-09-09T06:50:15+00:00: Recorded command exit 0; command argv SHA-256
  7c12437c2acd8eb95e026e7de09fa9cf2a26062740dba024b7277bdb84e61f28.

- 2026-09-09T06:50:41+00:00: Recorded command exit 0; command argv SHA-256
  fda0a277abc2d1d78ee348f00eddf16e40b5646be238d2724ce5049d78d544eb.

- 2026-09-09T06:51:09+00:00: Recorded command exit 0; command argv SHA-256
  0262fbc7a1219f534d30e9a689d6f9d527b94bedd29711b7466986b91ce686ca.

- 2026-09-09T06:52:02+00:00: Recorded command exit 0; command argv SHA-256
  6cc9caa4acf5ace049f21adac5750efdaef67cb18df1795fc3e044caebe85e26.

- 2026-09-09T06:53:04+00:00: Published the researched recommendation and AR-0880..AR-0886. Product
  full local gates pass; state targeted schema and full non-schema gates pass. GitHub SSH signatures
  remain unknown_key pending account registration.

- 2026-09-09T06:54:22+00:00: All fourteen product hosted jobs are terminal SUCCESS at exact head
  bda6cc8a, including emulated AArch64. State path-triggered AWQ shadow is SUCCESS at 9de11a52;
  targeted schema and full non-schema gates pass.

- 2026-09-09T06:55:27+00:00: Recorded command exit 1; command argv SHA-256
  c377f6f23e8191ac628092cf69be4594e4f4cad0d689771b259aba09c7fa026c.

- 2026-09-09T07:02:10+00:00: Recorded command exit 0; command argv SHA-256
  4975bb01ed0ba1a945e33da4521d9ecc0076bf2d12f4068cf14cda4f2f3d4c74.

- 2026-09-09T07:02:49+00:00: Recorded command exit 128; command argv SHA-256
  dfc0117aa5b8995632a80e7e151a1f91274cacd77363e2f89ed388bb59e2dd71.

- 2026-09-09T07:03:08+00:00: Recorded command exit 128; command argv SHA-256
  dfc0117aa5b8995632a80e7e151a1f91274cacd77363e2f89ed388bb59e2dd71.

- 2026-09-09T07:04:01+00:00: Recorded command exit 0; command argv SHA-256
  dfc0117aa5b8995632a80e7e151a1f91274cacd77363e2f89ed388bb59e2dd71.

- 2026-09-09T07:04:08+00:00: Recorded command exit 0; command argv SHA-256
  e783066d5f3dd62781e7c178718029f817108f92eff0575b02275ada1de93f80.
