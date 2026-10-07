---
{
  "id": "AR-1731",
  "title": "Connect Codex adapter to cli2key backend",
  "priority": "P1",
  "depends_on": ["AR-1729", "AR-1730"],
  "plan": "../plans/AR-1731-cli2key-codex-adapter.md",
  "summary": "Project the runtime-owned cli2key endpoint, model, and ephemeral client credential into the existing Codex Responses adapter.",
  "status": "planned",
  "next_action": "Promote after AR-1729 and AR-1730; integrate the Codex adapter with exact launch binding and no fallback.",
  "owner": "",
  "claim_expires": "",
  "checkpoint_commit": "",
  "task_revision": 1,
  "schema_version": 1,
  "spec_ref": "specs/AR-1731.json",
  "spec_revision": 1,
  "updated_at": "2026-10-07T23:21:33+00:00",
  "branch": "",
  "worktree_key": ""
}
---

Update the existing Codex Responses adapter to consume the supervised loopback
endpoint and fresh credential only at the final spawn boundary. Bind the exact
Codex executable/version, selected model, bridge identity, and sidecar
generation. Remove fixture-only credential assumptions for this route without
weakening local-mock or other provider paths. Never fall back to OpenAI,
OpenRouter, ambient Codex defaults, or a different endpoint/model.
