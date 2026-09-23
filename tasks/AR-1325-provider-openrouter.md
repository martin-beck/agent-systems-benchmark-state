---
{
  "branch": "feature/ar-1325-provider-openrouter",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-23T08:04:34+00:00",
  "depends_on": [
    "AR-0310",
    "AR-0318"
  ],
  "id": "AR-1325",
  "next_action": "Repair PR #249 history so every commit uses configured allowed SSH key SHA256:a36V6yPvRZyxnQ2113tiA/MlHt7mPfJEXAGByBXVkuE, then rerun exact-head policy and dependent PR checks.",
  "observed_branch": "feature/ar-1325-provider-openrouter",
  "observed_dirty": 0,
  "observed_head": "85eece9f6915c51a55ec54457dc214d743f5db00",
  "owner": "coordinator-openrouter-audit",
  "plan": "../plans/AR-1325.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Define one pinned credential-free OpenRouter provider profile for compatible ASB agent adapters.",
  "task_revision": 31,
  "title": "Support a shared OpenRouter provider",
  "updated_at": "2026-09-23T06:08:39+00:00",
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

- 2026-09-23T06:00:37+00:00: Claimed by coordinator-openrouter-audit.

- 2026-09-23T06:00:49+00:00: PR #249 exact-head f47e3728a9721ea268a730abef0f953bd2956613 is
  UNSTABLE: Repository quality fails because commit is signed by unlisted
  SHA256:xZFt+Xw6eb2sqyimnU8KqX/DawY5wKZFb1b4g7nKisU. No merge authorized.

- 2026-09-23T06:04:09+00:00: Released coordinator audit claim so a dedicated worker can repair the
  signed-history blocker; preserved exact PR failure evidence in next_action.

- 2026-09-23T06:04:34+00:00: Claimed by coordinator-openrouter-audit.

- 2026-09-23T06:04:44+00:00: Recorded command exit 128; command argv SHA-256
  d815d2d0fd19ccf2a6217ead997857fa773d1a5a528814161ecc34c43cf12390.

- 2026-09-23T06:05:21+00:00: Recorded command exit 128; command argv SHA-256
  baa948977eb7dac4d28c12c998a8e7a1cf72b36b1baf4e9ef03bc75749b403a5.

- 2026-09-23T06:05:33+00:00: Recorded command exit 128; command argv SHA-256
  f3aaef49bba53992737bac2a744e12e1aab7ab8ac60bdfee48145262151bbb58.

- 2026-09-23T06:05:55+00:00: Recorded command exit 0; command argv SHA-256
  fe0152892fc4e958afca852964e0a4727ca3796302eec45eebca2caaad7cf763.

- 2026-09-23T06:06:08+00:00: Recorded command exit 0; command argv SHA-256
  ba80366854db66aae4c495a502b1867aca4342f316fbb8d8d6e4d175b32f6e5e.

- 2026-09-23T06:06:39+00:00: Recorded command exit 0; command argv SHA-256
  3e91760620132cceae0c66e75cf85300904d38d92aa2b5fca5ac05bf2f1be229.

- 2026-09-23T06:06:57+00:00: Recorded command exit 0; command argv SHA-256
  d36922dc9be3f297e183a33373146ac56d994c7618ef3d954ae31d7c94b42eb4.

- 2026-09-23T06:07:10+00:00: Recorded command exit 0; command argv SHA-256
  7969b77f0447c5089381f9076096a8b20569f26b74b3fb65c36c1e81882456a7.

- 2026-09-23T06:07:25+00:00: Recorded command exit 0; command argv SHA-256
  6523bb46c12c928c4f9eb0ae5637d2c6cb7368e256745f771f33e5b8600e1e0a.

- 2026-09-23T06:07:46+00:00: Recorded command exit 0; command argv SHA-256
  f115b7f28dff6f8ffd22409db4459345c65bf80c88fdc3ea04c48fc2b605aeec.

- 2026-09-23T06:07:58+00:00: Recorded command exit 101; command argv SHA-256
  b895a4dd97883268a2693c049e9aa326a7b2b00873117a5922595ad4ac43b9cb.

- 2026-09-23T06:08:13+00:00: Recorded command exit 101; command argv SHA-256
  17daefe6c3e330ad2269d09a10ccf028ebb5ca4e4fa56fe902f82601d55e6cd2.

- 2026-09-23T06:08:39+00:00: Recorded command exit 0; command argv SHA-256
  480a48ebf4d3b29c9e896b8f162a4359ef1b24e1229b6e8c74b995619346e0ef.
