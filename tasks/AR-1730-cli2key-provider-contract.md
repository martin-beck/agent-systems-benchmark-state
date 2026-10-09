---
{
  "branch": "feature/ar-1730-cli2key-provider-contract",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T09:27:10+00:00",
  "depends_on": [
    "AR-1728"
  ],
  "id": "AR-1730",
  "next_action": "Promote after AR-1728; add protocol, control, catalog, selection, and launch contracts with fixture coverage.",
  "observed_branch": "feature/ar-1730-cli2key-provider-contract",
  "observed_dirty": 0,
  "observed_head": "918000a5c4f5b1e6821d257f32b279663c6903d1",
  "owner": "codex-ar1730-cli2key-provider-20261009",
  "plan": "../plans/AR-1730-cli2key-provider-contract.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_ref": "specs/AR-1730.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Add a development cli2key provider profile, catalog and launch identity for loopback Responses without overstating official OpenAI support.",
  "task_revision": 39,
  "title": "Add cli2key provider and selection contracts",
  "updated_at": "2026-10-09T07:57:13+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1730-cli2key-provider-contract"
}
---

Add a `cli2key` development provider identity using OpenAI Responses over a
loopback endpoint. Bind selections to catalog generation, discovered model,
bridge/runtime/executable identity, and an opaque invocation credential
reference. Initially advertise only Codex; every additional agent requires its
own independent adapter proof. Do not alias this profile to the official
`openai` provider or inherit production readiness claims.

- 2026-10-09T07:38:48+00:00: dependencies verified for cli2key provider contract

- 2026-10-09T07:38:53+00:00: Claimed by codex-ar1730-cli2key-provider-20261009.

- 2026-10-09T07:40:34+00:00: Heartbeat by codex-ar1730-cli2key-provider-20261009.

- 2026-10-09T07:40:50+00:00: Recorded command exit 0; command argv SHA-256
  54bf945203015a35ad2709fffcd6495c30d93a8babd0574604ee6c08111410b2.

- 2026-10-09T07:41:39+00:00: Recorded command exit 1; command argv SHA-256
  469c1f5852ba1a32fb01da328becabc02206e98d6c7a1be3bc037d8958c46163.

- 2026-10-09T07:42:18+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T07:42:58+00:00: Recorded command exit 101; command argv SHA-256
  470062534e2fb3cddc51b93c58a7dbb4f98427f836daee1a23873539d7e165e7.

- 2026-10-09T07:43:20+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T07:43:46+00:00: Recorded command exit 0; command argv SHA-256
  470062534e2fb3cddc51b93c58a7dbb4f98427f836daee1a23873539d7e165e7.

- 2026-10-09T07:43:52+00:00: Recorded command exit 0; command argv SHA-256
  d7fa61afbcc69b5d5af1715ab33a4d7b2885341aced9b0b5bd765a78ee21a338.

- 2026-10-09T07:44:34+00:00: Recorded command exit 0; command argv SHA-256
  71653f268ce8b04c4ec69ac706e0ba7233fd5cbd234b1b7dbd3f393e35f533b7.

- 2026-10-09T07:44:58+00:00: Recorded command exit 0; command argv SHA-256
  a1c219d0a50169c05c2f5f1bc4c9105819d774eb17b55e22b6bc623d8080292e.

- 2026-10-09T07:45:26+00:00: Recorded command exit 1; command argv SHA-256
  2f5b29a617104e6561278f0b490380f3fc95bd67042ad51939ba3d844fb57587.

- 2026-10-09T07:45:57+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T07:46:18+00:00: Recorded command exit 0; command argv SHA-256
  d29c2864f8ed045daa373f49509c25be583bec59c55fc4afdb09eb2dc2c90d80.

- 2026-10-09T07:46:33+00:00: Recorded command exit 0; command argv SHA-256
  3c18d58ce25356aacb8da4488cb5f03a74d34c2e3c3c8f8d41b46737bff825eb.

- 2026-10-09T07:46:39+00:00: Recorded command exit 1; command argv SHA-256
  3c18d58ce25356aacb8da4488cb5f03a74d34c2e3c3c8f8d41b46737bff825eb.

- 2026-10-09T07:47:11+00:00: Recorded command exit 0; command argv SHA-256
  39cf5398131881d6bebfeb6940a170dba53287cbad205a984f34c80a6dbe58e7.

- 2026-10-09T07:47:36+00:00: Recorded command exit 8; command argv SHA-256
  2f5b29a617104e6561278f0b490380f3fc95bd67042ad51939ba3d844fb57587.

- 2026-10-09T07:48:12+00:00: Recorded command exit 8; command argv SHA-256
  2f5b29a617104e6561278f0b490380f3fc95bd67042ad51939ba3d844fb57587.

- 2026-10-09T07:48:42+00:00: Recorded command exit 8; command argv SHA-256
  2f5b29a617104e6561278f0b490380f3fc95bd67042ad51939ba3d844fb57587.

- 2026-10-09T07:49:08+00:00: Recorded command exit 8; command argv SHA-256
  2f5b29a617104e6561278f0b490380f3fc95bd67042ad51939ba3d844fb57587.

- 2026-10-09T07:49:33+00:00: Recorded command exit 8; command argv SHA-256
  2f5b29a617104e6561278f0b490380f3fc95bd67042ad51939ba3d844fb57587.

- 2026-10-09T07:51:34+00:00: Contract boundary clarification: runtime may generate a fresh local
  cli2key client key when configured key material is absent or invalid; generated key material must
  never enter catalog, selection, launch identity, manifests, logs, argv, state, or evidence. Public
  contract carries only an opaque invocation credential-reference identity.

- 2026-10-09T07:51:42+00:00: Recorded command exit 8; command argv SHA-256
  2f5b29a617104e6561278f0b490380f3fc95bd67042ad51939ba3d844fb57587.

- 2026-10-09T07:52:08+00:00: Heartbeat by codex-ar1730-cli2key-provider-20261009.

- 2026-10-09T07:53:48+00:00: Heartbeat by codex-ar1730-cli2key-provider-20261009.

- 2026-10-09T07:53:52+00:00: Recorded command exit 1; command argv SHA-256
  2f5b29a617104e6561278f0b490380f3fc95bd67042ad51939ba3d844fb57587.

- 2026-10-09T07:54:19+00:00: Recorded command exit 8; command argv SHA-256
  2f5b29a617104e6561278f0b490380f3fc95bd67042ad51939ba3d844fb57587.

- 2026-10-09T07:54:43+00:00: Recorded command exit 8; command argv SHA-256
  2f5b29a617104e6561278f0b490380f3fc95bd67042ad51939ba3d844fb57587.

- 2026-10-09T07:55:02+00:00: Heartbeat by codex-ar1730-cli2key-provider-20261009.

- 2026-10-09T07:57:10+00:00: Heartbeat by codex-ar1730-cli2key-provider-20261009.

- 2026-10-09T07:57:13+00:00: Recorded command exit 0; command argv SHA-256
  9d0a97f0f94fdb5b13f586ee9648d24b11ef695793ab3988544ff0626c57a8af.
