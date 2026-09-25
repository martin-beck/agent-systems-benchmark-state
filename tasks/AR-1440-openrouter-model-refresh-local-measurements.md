---
{
  "branch": "feature/ar-1440-openrouter-model-refresh-local-measurements",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1328",
    "AR-1436",
    "AR-1437"
  ],
  "id": "AR-1440",
  "next_action": "Refresh the dated OpenRouter free-model pin only after a live catalog probe identifies an available zero-cost model; update every profile/config/fixture/doc identity, add positive and negative pin tests, and run a bounded local measurement campaign without adding CI network access or persisting credentials/responses.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1440.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Refresh the stale OpenRouter free-model pin and qualify local-only benchmark measurements.",
  "task_revision": 2,
  "title": "Refresh OpenRouter model pin and local measurements",
  "updated_at": "2026-09-25T13:19:22+00:00",
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
