---
{
  "branch": "docs/local-llm-testing-recommendations",
  "checkpoint_commit": "",
  "claim_expires": "",
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
  "owner": "",
  "plan": "../plans/AR-0879.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Research deterministic LLM test doubles and local inference options, document ASB recommendations, and create implementation-ready follow-up ARs.",
  "task_revision": 1,
  "title": "Plan deterministic LLM doubles and local inference",
  "updated_at": "2026-09-09T06:04:31+00:00",
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
