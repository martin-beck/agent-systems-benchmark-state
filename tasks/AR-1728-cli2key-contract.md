---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T05:36:09+00:00",
  "depends_on": [],
  "id": "AR-1728",
  "next_action": "Claim in an isolated ASB worktree; evaluate and pin a bridge, freeze the contract, and prove bounded Responses compatibility without persisting secrets.",
  "owner": "codex-ar1728-cli2key-contract-20261009",
  "plan": "../plans/AR-1728-cli2key-contract.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_ref": "specs/AR-1728.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Define cli2key as a development-only loopback Codex OAuth bridge with an ephemeral local client key, then select and pin a qualifying implementation.",
  "task_revision": 22,
  "title": "Freeze development cli2key contract and bridge",
  "updated_at": "2026-10-09T02:54:20+00:00",
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

- 2026-10-07T23:26:53+00:00: AR series design is published and validated; AR-1728 is intentionally
  unclaimed and ready for an isolated implementation worker.

- 2026-10-08T04:14:00+00:00: Claimed by codex-root-backend-model-ar-20261008.

- 2026-10-08T04:14:27+00:00: Recorded command exit 0; command argv SHA-256
  62f60907ed531f3b3a2376c238de8ef0fde175599c671cd06cf910e6c20f4413.

- 2026-10-08T04:15:05+00:00: Recorded command exit 0; command argv SHA-256
  55f87efa3ecf8614a4b0779a8bb686a63224999d23c26c93472b16d1bc33fef4.

- 2026-10-08T04:15:35+00:00: Added dependent AR-1736 with task, plan, and spec for canonical
  registry-driven model enumeration, selection, and exact identity propagation through full run and
  bounded sweep for every supported backend; deterministic development fixtures are sufficient and
  optional live credentials are nonblocking. AR-1728 implementation scope remains unchanged and
  ready.

- 2026-10-08T04:23:01+00:00: Claimed by codex-root-ar1737-register-20261008.

- 2026-10-08T04:23:17+00:00: Recorded command exit 0; command argv SHA-256
  3b99812bddb2cedfe5525fb0d93cc2ec1e7e620a897fe835f83e4ba372ee7d0a.

- 2026-10-08T04:23:48+00:00: Recorded command exit 0; command argv SHA-256
  38e9ccad05daa61830e1e28e4d9a5a94ddef7eed77e7956404a98c51623aaeea.

- 2026-10-08T04:24:21+00:00: Registered dependent ASB repair AR-1737 from exact AR-1575 evidence. It
  repairs the env-cleared validated linker/search-root handoff without restoring ambient PATH,
  retains reproducible remapping, and requires source-built install/upgrade/bare-launch
  qualification. AR-1728 remains unchanged and ready.

- 2026-10-08T09:22:59+00:00: Claimed by codex-backend-discovery-contract-20261008.

- 2026-10-08T09:24:35+00:00: No supplemental AR created: coordinator review confirmed AR-1736
  already preserves the required strict enumeration and full run/sweep contract; the attempted
  wrapped edit failed on the coordinator lock before any file mutation.

- 2026-10-09T02:36:09+00:00: Claimed by codex-ar1728-cli2key-contract-20261009.

- 2026-10-09T02:36:19+00:00: Recorded command exit 0; command argv SHA-256
  bf36bfe9ad14dc3de9999bf713e52ca5565dc82bea504d546e94f18538a6d291.

- 2026-10-09T02:42:22+00:00: Recorded command exit 0; command argv SHA-256
  1569e159a63e02bdb0179499d54e36c0f9ae53916fa370aa77af026c2b2d0220.

- 2026-10-09T02:43:45+00:00: Recorded command exit 0; command argv SHA-256
  485ff207ab6878b97aa6494d8672f892a95e591d895117860dad5c05728ba428.

- 2026-10-09T02:51:58+00:00: Recorded command exit 0; command argv SHA-256
  318f389cf7b43d1a2902400455c545617b56ccc53e9f6f31a3444156bbb38b6c.

- 2026-10-09T02:53:56+00:00: Recorded command exit 0; command argv SHA-256
  2107afe5f836d61bf812fd12027fa2f176ae3dbfdebe28a45b906d8c3f8db2e2.

- 2026-10-09T02:54:20+00:00: Recorded command exit 0; command argv SHA-256
  c845c39e39039d122163b303df11f4de061cc280a5a97680d2457065f608d080.
