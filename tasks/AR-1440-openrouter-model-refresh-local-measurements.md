---
{
  "branch": "feature/ar-1440-openrouter-model-refresh-local-measurements",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T15:32:39+00:00",
  "depends_on": [
    "AR-1328",
    "AR-1436",
    "AR-1437"
  ],
  "id": "AR-1440",
  "next_action": "Refresh the dated free-model pin from a live catalog; update every identity and test; retain provider-catalog/provider-plan as the sole provider/model/agent selection authority with stale and mixed-selection rejection; run bounded operator-only local measurements without CI network or persisted credentials/prompts/responses; publish exact-head evidence.",
  "observed_branch": "feature/ar-1440-openrouter-model-refresh-local-measurements",
  "observed_dirty": 0,
  "observed_head": "f2d4999ef09e3ebe3da720209a36954e6090f4b9",
  "owner": "ar1440-model-refresh-luna56",
  "plan": "../plans/AR-1440.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Refresh the stale OpenRouter free-model pin and qualify local-only benchmark measurements.",
  "task_revision": 19,
  "title": "Refresh OpenRouter model pin and local measurements",
  "updated_at": "2026-09-25T13:33:02+00:00",
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

- 2026-09-25T13:26:24+00:00: Recorded command exit 0; command argv SHA-256
  e4cf7907c5843af9e8e4d812ac349bfbe43737f1e85e65137977b0ab471c76cf.

- 2026-09-25T13:27:38+00:00: Scope extended to make provider, model, and selected agent changes
  catalog-driven and easy to regenerate without a second registry.

- 2026-09-25T13:27:48+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-25T13:28:14+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-25T13:28:29+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-25T13:32:24+00:00: Recorded command exit 0; command argv SHA-256
  700f2c3ed4d924e8ae40935ce8ed769768ac8d3ede69f00b7a8471468ea13ee7.

- 2026-09-25T13:32:39+00:00: Heartbeat by ar1440-model-refresh-luna56.

- 2026-09-25T13:33:02+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.
