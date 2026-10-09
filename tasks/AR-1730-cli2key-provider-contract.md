---
{
  "branch": "feature/ar-1730-cli2key-provider-contract",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T09:40:34+00:00",
  "depends_on": [
    "AR-1728"
  ],
  "id": "AR-1730",
  "next_action": "Promote after AR-1728; add protocol, control, catalog, selection, and launch contracts with fixture coverage.",
  "observed_branch": "feature/ar-1730-cli2key-provider-contract",
  "observed_dirty": 2,
  "observed_head": "30286af46920b34096d3a48153e728f7319358a4",
  "owner": "codex-ar1730-cli2key-provider-20261009",
  "plan": "../plans/AR-1730-cli2key-provider-contract.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_ref": "specs/AR-1730.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Add a development cli2key provider profile, catalog and launch identity for loopback Responses without overstating official OpenAI support.",
  "task_revision": 12,
  "title": "Add cli2key provider and selection contracts",
  "updated_at": "2026-10-09T07:43:46+00:00",
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
