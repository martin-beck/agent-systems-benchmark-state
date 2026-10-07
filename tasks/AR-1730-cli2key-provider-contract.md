---
{
  "id": "AR-1730",
  "title": "Add cli2key provider and selection contracts",
  "priority": "P1",
  "depends_on": ["AR-1728"],
  "plan": "../plans/AR-1730-cli2key-provider-contract.md",
  "summary": "Add a development cli2key provider profile, catalog and launch identity for loopback Responses without overstating official OpenAI support.",
  "status": "planned",
  "next_action": "Promote after AR-1728; add protocol, control, catalog, selection, and launch contracts with fixture coverage.",
  "owner": "",
  "claim_expires": "",
  "checkpoint_commit": "",
  "task_revision": 1,
  "schema_version": 1,
  "spec_ref": "specs/AR-1730.json",
  "spec_revision": 1,
  "updated_at": "2026-10-07T23:21:33+00:00",
  "branch": "",
  "worktree_key": ""
}
---

Add a `cli2key` development provider identity using OpenAI Responses over a
loopback endpoint. Bind selections to catalog generation, discovered model,
bridge/runtime/executable identity, and an opaque invocation credential
reference. Initially advertise only Codex; every additional agent requires its
own independent adapter proof. Do not alias this profile to the official
`openai` provider or inherit production readiness claims.
