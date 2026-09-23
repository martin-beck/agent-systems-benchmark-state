---
{
  "branch": "feature/ar-1334-openrouter-conformance-qualification",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-23T10:59:22+00:00",
  "depends_on": [
    "AR-1327",
    "AR-1328"
  ],
  "id": "AR-1334",
  "next_action": "Qualify the pinned free OpenRouter model under the AR-0315 conformance harness and run hostile cases such as credential bleed, endpoint mismatch, rate limits and malformed responses, all failing closed.",
  "observed_branch": "feature/ar-1334-openrouter-conformance-qualification",
  "observed_dirty": 4,
  "observed_head": "96e236cb83477479e244abd7f5014725e7806b88",
  "owner": "codex-asb-ar1334-20260923",
  "plan": "../plans/AR-1334.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify the pinned OpenRouter free model under conformance and hostile fail-closed testing.",
  "task_revision": 25,
  "title": "OpenRouter free-model conformance and hostile qualification",
  "updated_at": "2026-09-23T09:02:58+00:00",
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

- 2026-09-23T08:56:42+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T08:57:09+00:00: Recorded command exit 101; command argv SHA-256
  6a2b0d8955ce8b418a058ab810f7b6d4a56db894a1be52931e8c19de22c13ad2.

- 2026-09-23T08:57:34+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T08:57:48+00:00: Recorded command exit 0; command argv SHA-256
  6a2b0d8955ce8b418a058ab810f7b6d4a56db894a1be52931e8c19de22c13ad2.

- 2026-09-23T08:58:10+00:00: Recorded command exit 0; command argv SHA-256
  5c6ecfba14af919ae0f998f584f700ee239ba7e6c78604dcecf69612996e28fa.

- 2026-09-23T08:58:23+00:00: Recorded command exit 0; command argv SHA-256
  5c6ecfba14af919ae0f998f584f700ee239ba7e6c78604dcecf69612996e28fa.

- 2026-09-23T08:59:22+00:00: Heartbeat by codex-asb-ar1334-20260923.

- 2026-09-23T08:59:26+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T08:59:39+00:00: Recorded command exit 0; command argv SHA-256
  6a2b0d8955ce8b418a058ab810f7b6d4a56db894a1be52931e8c19de22c13ad2.

- 2026-09-23T09:00:15+00:00: Recorded command exit 0; command argv SHA-256
  33b60c76c3db4c079281bd7c519d689cf2ea63614f711e2f0ea7e79e6f11f5d8.

- 2026-09-23T09:00:40+00:00: Recorded command exit 101; command argv SHA-256
  4340dcbf253e5e20fd7f5355131da4428901f1f912a4e0ac816826265343c6b5.

- 2026-09-23T09:01:01+00:00: Recorded command exit 101; command argv SHA-256
  4d5c4f48b894bd88f6e9e1bca11ecc1ec69d589dc97b7c51a727caa33f0591f2.

- 2026-09-23T09:01:22+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T09:01:40+00:00: Recorded command exit 0; command argv SHA-256
  4340dcbf253e5e20fd7f5355131da4428901f1f912a4e0ac816826265343c6b5.

- 2026-09-23T09:02:45+00:00: Recorded command exit 0; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-23T09:02:58+00:00: Recorded command exit 0; command argv SHA-256
  40a6e9eb5140b176ab1929e20cfb658ea503e2c16a31725e8308fb53d6ef0466.
