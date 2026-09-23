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
  "observed_branch": "feature/ar-1325-provider-openrouter",
  "observed_dirty": 0,
  "observed_head": "f47e3728a9721ea268a730abef0f953bd2956613",
  "owner": "",
  "plan": "../plans/AR-1325.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Define one pinned credential-free OpenRouter provider profile for compatible ASB agent adapters.",
  "task_revision": 13,
  "title": "Support a shared OpenRouter provider",
  "updated_at": "2026-09-23T05:56:45+00:00",
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

- 2026-09-22T14:56:54+00:00: Recorded command exit 0; command argv SHA-256
  a32158e9fbac5b12b9647f35c59f6fefdf63543e6af84c126967456c9b52cf19.

- 2026-09-22T14:57:14+00:00: Recorded command exit 0; command argv SHA-256
  0b92c53b7b9ca737e3cbdf694ed0bf2de40458a4cac4bbd44969ff14326ad8eb.

- 2026-09-22T14:57:44+00:00: Heartbeat by ar1325-openrouter.

- 2026-09-23T05:56:45+00:00: Recovered expired claim formerly owned by ar1325-openrouter. Recovered
  expired claim after verifying no active AR-1325 worker process; existing PR #249 remains under
  review.
