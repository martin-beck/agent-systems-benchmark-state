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
  "observed_branch": "feature/ar-1731-cli2key-codex-adapter",
  "observed_dirty": 1,
  "observed_head": "b0d1c9d9f3521c25b65fe8f6e886920c01fc2da4",
  "owner": "codex-asb-ar1731-codex-adapter-20261009",
  "plan": "../plans/AR-1731-cli2key-codex-adapter.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_ref": "specs/AR-1731.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Project the runtime-owned cli2key endpoint, model, and ephemeral client credential into the existing Codex Responses adapter.",
  "task_revision": 17,
  "title": "Connect Codex adapter to cli2key backend",
  "updated_at": "2026-10-09T12:33:20+00:00",
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

- 2026-10-09T12:28:20+00:00: Recorded command exit 0; command argv SHA-256
  7bad499a658562cafcbf80ecb8d6ab0cba4cc26227681233633cb7c87d757c88.

- 2026-10-09T12:29:44+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-09T12:30:09+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T12:30:37+00:00: Recorded command exit 1; command argv SHA-256
  c1afeeaa051f2dcfe4986cbfe004666748d273e72d5ff3922f1404514575847f.

- 2026-10-09T12:31:17+00:00: Recorded command exit 0; command argv SHA-256
  dc14a9b4c3ae63f8a6af806435a94afa39f7b642cec26c66ac98a587569154bf.

- 2026-10-09T12:31:46+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T12:32:07+00:00: Recorded command exit 0; command argv SHA-256
  889ae8d45adaca88ba6a0362b4238042ea80de64bc4f25b3ae8d5af1f979d9c7.

- 2026-10-09T12:32:27+00:00: Recorded command exit 0; command argv SHA-256
  c9d32a02b361b55a7e0c04011f1d71b4e192d19cb368069b1624e1b820a9dc38.

- 2026-10-09T12:32:51+00:00: Recorded command exit 0; command argv SHA-256
  5c75106265a566284fe75fc3aa207b37fb4176303f562f75e29a5a3d7fba6a77.

- 2026-10-09T12:33:20+00:00: Recorded command exit 0; command argv SHA-256
  088b24c762f50a0757e6c661e5f3954c20c2a2c11318582937124be046a41f50.
