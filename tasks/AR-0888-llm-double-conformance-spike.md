---
{
  "branch": "test/llm-double-conformance-spike",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T10:05:19+00:00",
  "depends_on": [
    "AR-0879"
  ],
  "id": "AR-0888",
  "next_action": "Build the isolated OpenAI and Anthropic conformance spike, execute exact pinned candidates, and publish pass, fail, unsupported, and untested evidence.",
  "observed_branch": "test/llm-double-conformance-spike",
  "observed_dirty": 0,
  "observed_head": "78e6a51ce99ed407db8bbfe2487a1f20f0c27f2b",
  "owner": "codex-longrun-llm-double-conformance-20260909",
  "plan": "../plans/AR-0888.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Measure deterministic LLM test doubles against one hostile ASB protocol and isolation suite before selecting any dependency.",
  "task_revision": 19,
  "title": "Spike deterministic LLM double conformance",
  "updated_at": "2026-09-09T08:05:19+00:00",
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

- 2026-09-09T08:02:10+00:00: Implemented isolated standard-library AR-0888 spike: immutable
  candidate manifest, OpenAI Chat/Responses and Anthropic Messages buffered/SSE fixtures,
  rate-limit/truncation/unmatched faults, deterministic repeat hashes, loopback-only/no-credential
  privacy checks, explicit untested candidate matrix, and focused tests. unittest (3), Ruff, strict
  mypy, and diff-check pass.

- 2026-09-09T08:02:24+00:00: Recorded command exit 0; command argv SHA-256
  5104cb17e012db427a6f20aec347ad52d6a32510981321d293c2e642860bc6d8.

- 2026-09-09T08:02:44+00:00: Recorded command exit 0; command argv SHA-256
  db5921f9f78f010369b8e77437a3bd7d873d5b53e31af4aba4631dc0d4ca0433.

- 2026-09-09T08:03:00+00:00: Heartbeat by codex-longrun-llm-double-conformance-20260909.

- 2026-09-09T08:03:04+00:00: Recorded command exit 8; command argv SHA-256
  c22d02b809c14b27042704f4577f4912d5ff9d1a8d8d7bae5823bfc7adc9633b.

- 2026-09-09T08:03:56+00:00: Heartbeat by codex-longrun-llm-double-conformance-20260909.

- 2026-09-09T08:04:01+00:00: Recorded command exit 8; command argv SHA-256
  c22d02b809c14b27042704f4577f4912d5ff9d1a8d8d7bae5823bfc7adc9633b.

- 2026-09-09T08:04:12+00:00: Heartbeat by codex-longrun-llm-double-conformance-20260909.

- 2026-09-09T08:04:56+00:00: Heartbeat by codex-longrun-llm-double-conformance-20260909.

- 2026-09-09T08:05:00+00:00: Recorded command exit 8; command argv SHA-256
  c22d02b809c14b27042704f4577f4912d5ff9d1a8d8d7bae5823bfc7adc9633b.

- 2026-09-09T08:05:19+00:00: Heartbeat by codex-longrun-llm-double-conformance-20260909.
