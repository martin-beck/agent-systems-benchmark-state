---
{
  "branch": "feature/ar-1334-openrouter-conformance-qualification",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-23T10:56:23+00:00",
  "depends_on": [
    "AR-1327",
    "AR-1328"
  ],
  "id": "AR-1334",
  "next_action": "Qualify the pinned free OpenRouter model under the AR-0315 conformance harness and run hostile cases such as credential bleed, endpoint mismatch, rate limits and malformed responses, all failing closed.",
  "observed_branch": "feature/ar-1334-openrouter-conformance-qualification",
  "observed_dirty": 3,
  "observed_head": "96e236cb83477479e244abd7f5014725e7806b88",
  "owner": "codex-asb-ar1334-20260923",
  "plan": "../plans/AR-1334.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify the pinned OpenRouter free model under conformance and hostile fail-closed testing.",
  "task_revision": 8,
  "title": "OpenRouter free-model conformance and hostile qualification",
  "updated_at": "2026-09-23T08:56:35+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1334-openrouter-conformance-qualification"
}
---

Selecting and wiring the OpenRouter profile (AR-1325..AR-1327) and the
per-user free-model configuration (AR-1328) is not enough: the pinned free model
must be proven to conform through the AR-0315 conformance harness and to fail
closed under hostile conditions. This AR qualifies the exact free-model
snapshot over the compatible agent matrix, and runs hostile cases including
absent or bleeding credentials, endpoint identity confusion, rate limiting,
timeouts, streaming and tool-call divergence, and malformed responses. Every
negative case must fail closed with typed errors and no secret or uncertain
provider effect; real provider contact is opt-in and never required for CI.

- 2026-09-23T08:53:51+00:00: Dependencies AR-1327 and AR-1328 are done; prioritize pinned OpenRouter
  conformance and hostile fail-closed qualification.

- 2026-09-23T08:53:57+00:00: Claimed by codex-asb-ar1334-20260923.

- 2026-09-23T08:54:28+00:00: Recorded command exit 0; command argv SHA-256
  d519cb52303fb28e4c29ab2600116fd60c3b0dad7ff03abd245587b56fe2feb6.

- 2026-09-23T08:56:23+00:00: Heartbeat by codex-asb-ar1334-20260923.

- 2026-09-23T08:56:25+00:00: Recorded command exit 1; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.
