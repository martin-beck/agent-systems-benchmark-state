---
{
  "branch": "feature/ar-1731-cli2key-codex-adapter",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T14:27:00+00:00",
  "depends_on": [
    "AR-1729",
    "AR-1730"
  ],
  "id": "AR-1731",
  "next_action": "Promote after AR-1729 and AR-1730; integrate the Codex adapter with exact launch binding and no fallback.",
  "owner": "codex-asb-ar1731-codex-adapter-20261009",
  "plan": "../plans/AR-1731-cli2key-codex-adapter.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_ref": "specs/AR-1731.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Project the runtime-owned cli2key endpoint, model, and ephemeral client credential into the existing Codex Responses adapter.",
  "task_revision": 5,
  "title": "Connect Codex adapter to cli2key backend",
  "updated_at": "2026-10-09T12:27:39+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1731-cli2key-adapter"
}
---

Update the existing Codex Responses adapter to consume the supervised loopback
endpoint and fresh credential only at the final spawn boundary. Bind the exact
Codex executable/version, selected model, bridge identity, and sidecar
generation. Remove fixture-only credential assumptions for this route without
weakening local-mock or other provider paths. Never fall back to OpenAI,
OpenRouter, ambient Codex defaults, or a different endpoint/model.

- 2026-10-09T12:26:56+00:00: Dependencies AR-1729 and AR-1730 are now accepted and done with exact
  hosted merge evidence; ready for implementation.

- 2026-10-09T12:27:00+00:00: Claimed by codex-asb-ar1731-codex-adapter-20261009.

- 2026-10-09T12:27:39+00:00: Recorded command exit 0; command argv SHA-256
  105da586cac1b3bcaa99b9e44f9a3f5ee37cf82223894f67446c0df22697e3f0.
