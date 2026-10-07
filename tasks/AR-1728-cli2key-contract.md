---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-07T23:55:27+00:00",
  "depends_on": [],
  "id": "AR-1728",
  "next_action": "Claim in an isolated ASB worktree; evaluate and pin a bridge, freeze the contract, and prove bounded Responses compatibility without persisting secrets.",
  "owner": "codex-cli2key-planning",
  "plan": "../plans/AR-1728-cli2key-contract.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_ref": "specs/AR-1728.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Define cli2key as a development-only loopback Codex OAuth bridge with an ephemeral local client key, then select and pin a qualifying implementation.",
  "task_revision": 4,
  "title": "Freeze development cli2key contract and bridge",
  "updated_at": "2026-10-07T23:26:17+00:00",
  "worktree_key": ""
}
---

Define the ASB `cli2key` development mode before implementation. A Codex CLI
login does not grant ASB an official OpenAI Platform API key. The fresh key in
this mode is instead a random downstream client credential for a loopback-only
proxy whose upstream authentication is a user-approved Codex OAuth session.

Select a pinned, license-compatible bridge and exact version/digest. Prove a
bounded `/v1/models` discovery and one `/v1/responses` request. Prefer a bridge
that imports an existing Codex login into its own private store through a
documented interface; ASB must not parse or copy `~/.codex/auth.json` ad hoc.
Record no tokens, key values, prompts, provider bodies, or private paths.

The contract must explicitly prohibit treating Codex `app-server` as a raw
provider for other agents: that would create nested-agent execution and
invalidate normal benchmark comparability. This mode is development-only,
unofficial, opt-in, and provides no production or provider-authority claim.

- 2026-10-07T23:25:27+00:00: Claimed by codex-cli2key-planning.

- 2026-10-07T23:25:40+00:00: Recorded command exit 0; command argv SHA-256
  c7d567b158342cc9f29aecfdc7c3c115d73a8e8d03cf56ae6636dda76ebfc1e8.

- 2026-10-07T23:26:17+00:00: Recorded command exit 0; command argv SHA-256
  657ceb20b632c8bae94d629eab17b3a147b52e6905374e2680a1d1592cbf09b6.
