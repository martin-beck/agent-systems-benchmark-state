---
{
  "branch": "test/llm-double-conformance-spike",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T10:01:55+00:00",
  "depends_on": [
    "AR-0879"
  ],
  "id": "AR-0888",
  "next_action": "Build the isolated OpenAI and Anthropic conformance spike, execute exact pinned candidates, and publish pass, fail, unsupported, and untested evidence.",
  "observed_branch": "test/llm-double-conformance-spike",
  "observed_dirty": 0,
  "observed_head": "bf66ad4198a2a96fd284765b98a60acdcef12eac",
  "owner": "codex-longrun-llm-double-conformance-20260909",
  "plan": "../plans/AR-0888.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Measure deterministic LLM test doubles against one hostile ASB protocol and isolation suite before selecting any dependency.",
  "task_revision": 7,
  "title": "Spike deterministic LLM double conformance",
  "updated_at": "2026-09-09T08:01:55+00:00",
  "worktree_key": "agent-systems-benchmark-llm-double-conformance-spike"
}
---
## AR-0888

Evaluate MockAgents, CopilotKit aimock, larsakerlund/llmock, and piyook/llm-mock at the revisions in `docs/LOCAL_LLM_TESTING_RECOMMENDATIONS.md`. This conformance spike is not an integration/support claim.

- 2026-09-09T07:59:21+00:00: Dependency AR-0879 is released done; promote deterministic LLM double
  conformance spike. Product-only paths are independent of state workflow track.

- 2026-09-09T07:59:24+00:00: Claimed by codex-longrun-llm-double-conformance-20260909.

- 2026-09-09T07:59:27+00:00: Heartbeat by codex-longrun-llm-double-conformance-20260909.

- 2026-09-09T07:59:30+00:00: Recorded command exit 0; command argv SHA-256
  274f9e39a75fd10d376bf30ef0567423162be4ff90c1b1f2b68f9176438f004c.

- 2026-09-09T08:01:55+00:00: Heartbeat by codex-longrun-llm-double-conformance-20260909.
