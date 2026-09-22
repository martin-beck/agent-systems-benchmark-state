---
{
  "branch": "feature/ar-1325-provider-openrouter",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0310",
    "AR-0318"
  ],
  "id": "AR-1325",
  "next_action": "Pin the OpenRouter endpoint identity, dated model snapshot, transport bounds and OPENROUTER_API_KEY credential reference, then implement the credential-free provider profile with fail-closed validation.",
  "owner": "",
  "plan": "../plans/AR-1325.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Define one pinned credential-free OpenRouter provider profile for compatible ASB agent adapters.",
  "task_revision": 2,
  "title": "Support a shared OpenRouter provider",
  "updated_at": "2026-09-22T14:10:08+00:00",
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
