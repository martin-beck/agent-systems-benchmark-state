---
{
  "branch": "feature/ar-1325-provider-openrouter",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-22T18:24:48+00:00",
  "depends_on": [
    "AR-0310",
    "AR-0318"
  ],
  "id": "AR-1325",
  "next_action": "Pin the OpenRouter endpoint identity, dated model snapshot, transport bounds and OPENROUTER_API_KEY credential reference, then implement the credential-free provider profile with fail-closed validation.",
  "observed_branch": "feature/ar-1325-provider-openrouter",
  "observed_dirty": 3,
  "observed_head": "a4934fca0b528ac90d09fb537936584f5af0f75e",
  "owner": "ar1325-openrouter",
  "plan": "../plans/AR-1325.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Define one pinned credential-free OpenRouter provider profile for compatible ASB agent adapters.",
  "task_revision": 8,
  "title": "Support a shared OpenRouter provider",
  "updated_at": "2026-09-22T14:47:33+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1325-provider-openrouter"
}
---

OpenRouter exposes an OpenAI-compatible API, but the closed ASB provider catalog
only advertises `openai` (selectable) and `ollama` (unavailable), and the launch
projection pins api.openai.com. This AR defines the missing OpenRouter provider
profile on the reviewed AR-0310 common contract: endpoint identity for
https://openrouter.ai/api/v1, a dated model snapshot instead of a moving alias,
explicit transport bounds, and the credential-free `OPENROUTER_API_KEY`
reference boundary from AR-0318. No credential value enters the profile, and
unsupported or lossy translations fail closed.

- 2026-09-22T14:10:08+00:00: Dependencies AR-0310 and AR-0318 are done; promote the OpenRouter
  provider profile for parallel implementation.

- 2026-09-22T14:10:18+00:00: Claimed by ar1325-openrouter.

- 2026-09-22T14:24:48+00:00: Heartbeat by ar1325-openrouter.

- 2026-09-22T14:45:45+00:00: Recorded command exit 101; command argv SHA-256
  681994a9b7b368ece8b133aae9b6f6ac982dd6a4869c3ca5fb59dcb9ad68604a.

- 2026-09-22T14:47:33+00:00: Recorded command exit 101; command argv SHA-256
  681994a9b7b368ece8b133aae9b6f6ac982dd6a4869c3ca5fb59dcb9ad68604a.
