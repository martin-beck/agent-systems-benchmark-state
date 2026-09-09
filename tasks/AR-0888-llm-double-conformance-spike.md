---
{
  "branch": "test/llm-double-conformance-spike", "checkpoint_commit": "", "claim_expires": "", "depends_on": ["AR-0879"],
  "id": "AR-0888", "next_action": "Build the isolated OpenAI and Anthropic conformance spike, execute exact pinned candidates, and publish pass, fail, unsupported, and untested evidence.",
  "owner": "", "plan": "../plans/AR-0888.md", "priority": "P1", "schema_version": 1, "status": "planned",
  "summary": "Measure deterministic LLM test doubles against one hostile ASB protocol and isolation suite before selecting any dependency.",
  "task_revision": 1, "title": "Spike deterministic LLM double conformance", "updated_at": "2026-09-09T06:30:00+00:00",
  "worktree_key": "agent-systems-benchmark-llm-double-conformance-spike"
}
---
## AR-0888

Evaluate MockAgents, CopilotKit aimock, larsakerlund/llmock, and piyook/llm-mock at the revisions in `docs/LOCAL_LLM_TESTING_RECOMMENDATIONS.md`. This conformance spike is not an integration/support claim.
