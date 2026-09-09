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
  "next_action": "Research pinned public LLM test doubles, replay literature, and local inference servers; publish an ASB-specific recommendation and dependency-ordered implementation ARs without adding runtime integration.",
  "observed_branch": "docs/local-llm-testing-recommendations",
  "observed_dirty": 2,
  "observed_head": "ca6e75916a8c9831b9107377cd48d731463c272a",
  "owner": "codex-asb-local-llm-research-20260909",
  "plan": "../plans/AR-0879.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Research deterministic LLM test doubles and local inference options, document ASB recommendations, and create implementation-ready follow-up ARs.",
  "task_revision": 20,
  "title": "Plan deterministic LLM doubles and local inference",
  "updated_at": "2026-09-09T06:41:31+00:00",
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
