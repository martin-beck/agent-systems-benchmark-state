---
{
  "branch": "feature/ar-1440-openrouter-model-refresh-local-measurements",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T15:25:01+00:00",
  "depends_on": [
    "AR-1328",
    "AR-1436",
    "AR-1437"
  ],
  "id": "AR-1440",
  "next_action": "Refresh the dated OpenRouter free-model pin only after a live catalog probe identifies an available zero-cost model; update every profile/config/fixture/doc identity, add positive and negative pin tests, and run a bounded local measurement campaign without adding CI network access or persisting credentials/responses.",
  "observed_branch": "feature/ar-1440-openrouter-model-refresh-local-measurements",
  "observed_dirty": 7,
  "observed_head": "40c5c4118356df0e35d26df6933ddb07d2b4f517",
  "owner": "ar1440-model-refresh-luna56",
  "plan": "../plans/AR-1440.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Refresh the stale OpenRouter free-model pin and qualify local-only benchmark measurements.",
  "task_revision": 9,
  "title": "Refresh OpenRouter model pin and local measurements",
  "updated_at": "2026-09-25T13:25:51+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1440-openrouter-model-refresh-local-measurements"
}
---

Refresh the exact dated OpenRouter free-model identity after the previous
`deepseek/deepseek-chat-v3-0324:free` pin was observed unavailable. The chosen
model must be present in the live `/models` catalog, explicitly marked free,
and recorded with a new dated snapshot identity. Update all Rust profile and
config constants, generated fixtures, schemas/examples, and documentation
without introducing a moving alias or runtime download.

Add a bounded operator-invoked local measurement path that uses the refreshed
profile and the user's zero-budget key only outside CI. It must record only
non-secret digests, status, model identity, bounded timing/token counters and
typed outcomes; never persist keys, prompts, responses, headers or private
paths. Do not add network access to CI and do not claim completion of the
blocked runtime-owned AR-1329 live `asb run` path. Include hostile negative
tests for stale/mismatched model identities and unavailable pins.

- 2026-09-25T13:19:22+00:00: Dependencies AR-1328, AR-1436 and AR-1437 are released; begin exact
  model refresh and operator-only measurements without resuming blocked AR-1329.

- 2026-09-25T13:20:57+00:00: Claimed by ar1440-model-refresh-luna56.

- 2026-09-25T13:21:36+00:00: Recorded command exit 0; command argv SHA-256
  2b8a69c43832ade4c74b8cf69adae82656f18cec0459c3a5f5733a6e6f4b59ad.

- 2026-09-25T13:22:33+00:00: Recorded command exit 0; command argv SHA-256
  693507ce54834382c447255997256e7f7cd98f5c530e53d1133aef292c525a22.

- 2026-09-25T13:25:01+00:00: Heartbeat by ar1440-model-refresh-luna56.
