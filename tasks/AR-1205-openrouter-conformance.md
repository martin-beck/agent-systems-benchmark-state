---
{
  "branch": "feature/openrouter-conformance",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1200", "AR-1203", "AR-1204"],
  "id": "AR-1205",
  "next_action": "Build the credential-free synthetic loopback suite for the OpenRouter dialect, then run live-record to network-denied-replay journeys per supported agent and record free-model availability and rate limits as explicit evidence limits.",
  "owner": "",
  "plan": "../plans/AR-1205.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Prove each supported agent against the pinned OpenRouter free model through a credential-free loopback conformance suite and native loopback live-record to network-denied-replay journeys, and record free-model availability/limits.",
  "task_revision": 1,
  "title": "OpenRouter free-model live/replay conformance and parity evidence",
  "updated_at": "2026-09-22T09:39:55+00:00",
  "worktree_key": "agent-systems-benchmark-openrouter-conformance"
}
---
Prove the pinned OpenRouter free-model profile per supported agent: a credential-free synthetic
loopback conformance suite for the OpenAI-compatible dialect (Chat Completions/Responses buffered
and SSE, tools, causal IDs, retries, errors), then for each agent one native loopback live-record
journey followed by a network-denied strict replay with trajectory/grader parity. Free-model
availability, rate limits and latency variability are recorded as explicit evidence limits; replay
never claims fresh-model quality. Gemini stays unsupported for the OpenAI-compatible profile.
Repository: `martin-beck/agent-systems-benchmark`.

- 2026-09-22T09:39:55+00:00: Defined from the record/replay/benchmark integration proposal.
  Depends on the pinned OpenRouter profile (AR-1200), replay-mode run/sweep (AR-1203), and the
  integrated workflow (AR-1204).
