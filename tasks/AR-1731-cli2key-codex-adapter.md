---
{
  "branch": "feature/ar-1731-cli2key-codex-adapter",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1729",
    "AR-1730"
  ],
  "id": "AR-1731",
  "next_action": "AR-1758 is repairing failed post-merge provenance for b3cb9b2; remain in progress and unaccepted until supported repair PR and exact-main checks are green.",
  "observed_branch": "feature/ar-1731-cli2key-codex-adapter",
  "observed_dirty": 0,
  "observed_head": "6386e066b37a99692e3343f6162d648a8cb506f0",
  "owner": "",
  "plan": "../plans/AR-1731-cli2key-codex-adapter.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "hosted",
    "evidence_digest": "sha256:0c1145e3541052c6e17abd834e8a298a1a9955d6cdfcc17cadf27e127bdd567a",
    "evidence_ref": "quality/AR-1731-cli2key-postmerge-receipt.json",
    "spec_ref": "specs/AR-1731.json",
    "spec_revision": 1,
    "status": "pass"
  },
  "spec_ref": "specs/AR-1731.json",
  "spec_revision": 1,
  "status": "done",
  "summary": "Project the runtime-owned cli2key endpoint, model, and ephemeral client credential into the existing Codex Responses adapter.",
  "task_revision": 51,
  "title": "Connect Codex adapter to cli2key backend",
  "updated_at": "2026-10-09T13:14:40+00:00",
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

- 2026-10-09T12:33:46+00:00: Recorded command exit 0; command argv SHA-256
  feec1ff0d170bea958888980a584bf60d26be6fe6d151c8cb522689379b4e121.

- 2026-10-09T12:37:13+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T12:37:35+00:00: Recorded command exit 0; command argv SHA-256
  889ae8d45adaca88ba6a0362b4238042ea80de64bc4f25b3ae8d5af1f979d9c7.

- 2026-10-09T12:37:56+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T12:38:18+00:00: Recorded command exit 0; command argv SHA-256
  889ae8d45adaca88ba6a0362b4238042ea80de64bc4f25b3ae8d5af1f979d9c7.

- 2026-10-09T12:38:38+00:00: Recorded command exit 1; command argv SHA-256
  2dc9da94c01b508a18bfeec79540b63c1bd9330ef6c4731f1cf6d076ec7d1e89.

- 2026-10-09T12:38:59+00:00: Recorded command exit 0; command argv SHA-256
  5cd40abcf6946f845077d5906bd9a4ea92e68131ae9008a39db703f8e8208a38.

- 2026-10-09T12:39:30+00:00: Recorded command exit 0; command argv SHA-256
  d4714147e4627290987b0ad5fb08eeec1f40613aae45136a217a0ee5f540cf82.

- 2026-10-09T12:39:52+00:00: Recorded command exit 0; command argv SHA-256
  2dc9da94c01b508a18bfeec79540b63c1bd9330ef6c4731f1cf6d076ec7d1e89.

- 2026-10-09T12:40:19+00:00: Recorded command exit 0; command argv SHA-256
  5cd40abcf6946f845077d5906bd9a4ea92e68131ae9008a39db703f8e8208a38.

- 2026-10-09T12:43:13+00:00: Recorded command exit 0; command argv SHA-256
  395302625f1e72e0b4d832ace51ac9b6e3d33f870ee042f07565de4ad943f209.

- 2026-10-09T12:45:23+00:00: Implementation and focused hostile tests are complete; independent
  review comment recorded. Awaiting remaining exact-head hosted checks before merge.

- 2026-10-09T12:48:55+00:00: Heartbeat by codex-asb-ar1731-codex-adapter-20261009.

- 2026-10-09T12:51:02+00:00: Recorded command exit 1; command argv SHA-256
  c427c665cfcca147b37c7574b24aaf182ad05b0acdb6fe675130205b377a179a.

- 2026-10-09T12:51:22+00:00: Recorded command exit 0; command argv SHA-256
  0789a820bb332a1618be9b6e49c28a355623a50ba472f3e88c7da8ee8d917a91.

- 2026-10-09T12:51:44+00:00: Recorded command exit 0; command argv SHA-256
  6519f66b604455db836b86f37038b9b9681da58d342b62f505a934b5ceefa063.

- 2026-10-09T12:52:00+00:00: Recorded command exit 0; command argv SHA-256
  86fe1eb2831a03f5193ff71c1c4910f745328707338a5567bd5872980adcc742.

- 2026-10-09T12:52:19+00:00: Recorded command exit 0; command argv SHA-256
  ad72fab36bef1a5c17965449c9cc7bc2a4f676f1d189bd1cccd6e1410d41ba57.

- 2026-10-09T12:52:30+00:00: Recorded command exit 1; command argv SHA-256
  86fe1eb2831a03f5193ff71c1c4910f745328707338a5567bd5872980adcc742.

- 2026-10-09T12:52:43+00:00: Recorded command exit 0; command argv SHA-256
  6bc3bd030f48a910b945844c2bd388e3f8af532eb13e85341f326d6c0d9e6789.

- 2026-10-09T12:52:51+00:00: Recorded command exit 0; command argv SHA-256
  ad72fab36bef1a5c17965449c9cc7bc2a4f676f1d189bd1cccd6e1410d41ba57.

- 2026-10-09T12:53:08+00:00: Recorded command exit 0; command argv SHA-256
  d8fc0b5fa92a22e7678073c8ce8b9a87ad62d419553053de6e1c615681493aeb.

- 2026-10-09T12:53:18+00:00: Recorded command exit 0; command argv SHA-256
  b1d58ad6001d910de334c5b748986327acf6f6c541293c699c66a5348f4ab19d.

- 2026-10-09T12:53:48+00:00: Recorded command exit 0; command argv SHA-256
  91709d2f584a4df3bb736ca9e119fe481b7e8eefde96632282ce2e0d69cd6dea.

- 2026-10-09T12:53:57+00:00: Recorded command exit 0; command argv SHA-256
  226d41708803c478f18884d9df572ab90d83666a75458b85b98ecbc8c2eb9c47.

- 2026-10-09T12:54:05+00:00: Recorded command exit 0; command argv SHA-256
  ffd2c2087ea8d4d5936a68173743a8fba699a09882c490f525737dd2bf2fa977.

- 2026-10-09T12:54:36+00:00: Recorded command exit 0; command argv SHA-256
  bac5d7b3843f6fd01b1cb89819cc1a7fec08c5ea266e78359b30684dd859efa7.

- 2026-10-09T12:54:44+00:00: Recorded command exit 0; command argv SHA-256
  349ee71932d584214b91c2ef504d19b22a2480355a5f74b332b5f760cc1aa109.

- 2026-10-09T12:54:54+00:00: Recorded command exit 0; command argv SHA-256
  ffd2c2087ea8d4d5936a68173743a8fba699a09882c490f525737dd2bf2fa977.

- 2026-10-09T12:55:37+00:00: Post-merge portable provenance failed because locally constructed merge
  b3cb9b2 omitted Signed-off-by. AR-1758 records the failure and supported no-history-rewrite repair
  path.

- 2026-10-09T13:14:37+00:00: Accepted implementation PR #527 and repaired exact-main publication
  021ca1c39ff0199aa2c193026783712bc73bc51b; focused hostile tests, independent review, and all
  required exact-main workflows are successful.

- 2026-10-09T13:14:40+00:00: Completed Codex cli2key adapter integration and non-rewriting
  protected-main provenance repair.
