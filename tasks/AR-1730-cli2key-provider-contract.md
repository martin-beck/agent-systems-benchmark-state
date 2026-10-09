---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T09:38:53+00:00",
  "depends_on": [
    "AR-1728"
  ],
  "id": "AR-1730",
  "next_action": "Promote after AR-1728; add protocol, control, catalog, selection, and launch contracts with fixture coverage.",
  "owner": "codex-ar1730-cli2key-provider-20261009",
  "plan": "../plans/AR-1730-cli2key-provider-contract.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_ref": "specs/AR-1730.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Add a development cli2key provider profile, catalog and launch identity for loopback Responses without overstating official OpenAI support.",
  "task_revision": 3,
  "title": "Add cli2key provider and selection contracts",
  "updated_at": "2026-10-09T07:38:53+00:00",
  "worktree_key": ""
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
