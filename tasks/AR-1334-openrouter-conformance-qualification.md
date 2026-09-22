---
{
  "branch": "feature/ar-1334-openrouter-conformance-qualification",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1327",
    "AR-1328"
  ],
  "id": "AR-1334",
  "next_action": "Qualify the pinned free OpenRouter model under the AR-0315 conformance harness and run hostile cases such as credential bleed, endpoint mismatch, rate limits and malformed responses, all failing closed.",
  "owner": "",
  "plan": "../plans/AR-1334.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Qualify the pinned OpenRouter free model under conformance and hostile fail-closed testing.",
  "task_revision": 1,
  "title": "OpenRouter free-model conformance and hostile qualification",
  "updated_at": "2026-09-22T13:39:37+00:00",
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
