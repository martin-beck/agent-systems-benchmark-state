---
{
  "branch": "feature/ar-1316-authenticated-agent-catalog-producer",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-24T19:35:56+00:00",
  "depends_on": [
    "AR-1190",
    "AR-1191",
    "AR-1310",
    "AR-1319"
  ],
  "id": "AR-1316",
  "next_action": "Persist the authenticated catalog snapshot/generation and complete live ASB-to-asb-tui wizard evidence; keep all entries unavailable until a verified release closure exists.",
  "owner": "ar1316-authenticated-agent-catalog-producer-luna56",
  "plan": "../plans/AR-1316.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Publish the verified ASB agent catalog required by the first-run setup wizard.",
  "task_revision": 3,
  "title": "Authenticated agent catalog producer",
  "updated_at": "2026-09-24T17:35:56+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1316-authenticated-agent-catalog-producer"
}
---

ASB now returns a truthful nine-entry authenticated roster through
`ControlCall::AgentCatalog`; every current entry is explicitly unavailable with
`incomplete_provenance`. The remaining work is durable snapshot/generation
persistence and verified release-closure integration. No secrets are exposed.

Progress evidence: ASB PR #245 merged at `027af7ad27da13b359b3f099699c42b03c6f394d`. TUI PR #131 merged at `08fdbbc8f9e2a76f0b1ef06a39af789404c9b2c7` with matching unavailable-entry decoding and digest behavior.

- 2026-09-24T17:35:40+00:00: Claimed by ar1316-authenticated-agent-catalog-producer-luna56.

- 2026-09-24T17:35:56+00:00: Heartbeat by ar1316-authenticated-agent-catalog-producer-luna56.
