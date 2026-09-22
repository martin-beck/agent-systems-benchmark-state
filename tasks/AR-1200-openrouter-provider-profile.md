---
{
  "branch": "feature/openrouter-provider",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0310", "AR-0313", "AR-0318", "AR-0320"],
  "id": "AR-1200",
  "next_action": "Record availability evidence for a specific :free OpenRouter model identifier and freeze it in a const snapshot, then implement OpenRouterProfile mirroring OpenAiProfile.",
  "owner": "",
  "plan": "../plans/AR-1200.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Add a pinned OpenRouter provider profile (OpenAI-compatible endpoint, one frozen :free model snapshot) with the environment credential boundary and exact adapter translations, exposed through the provider catalog and AllAgentsProviderSelection.",
  "task_revision": 1,
  "title": "Pin the OpenRouter provider profile (free model) and credential boundary",
  "updated_at": "2026-09-22T09:39:55+00:00",
  "worktree_key": "agent-systems-benchmark-openrouter-provider"
}
---
Add the pinned OpenRouter provider profile: OpenAI-compatible base `https://openrouter.ai/v1`,
one frozen `:free` model snapshot with recorded availability evidence, the `OPENROUTER_API_KEY`
environment credential boundary, and exact per-adapter request translations reusing the existing
`ProviderProfileAdapter`/`bind_provider_profile` and `verify_effective_request` fail-closed path.
Repository: `martin-beck/agent-systems-benchmark`.

- 2026-09-22T09:39:55+00:00: Defined from the record/replay/benchmark integration proposal.
  Depends on the provider-profile contract (AR-0310), all-agents selection (AR-0313), and the
  credential reference/resolver integration (AR-0318, AR-0320). Gemini stays unsupported for the
  OpenAI-compatible profile.
