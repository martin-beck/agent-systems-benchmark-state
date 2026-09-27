---
{
  "branch": "release/ar-1492-customer-bundle-signing-handoff",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-27T18:13:26+00:00",
  "depends_on": [
    "AR-1461",
    "AR-1462",
    "AR-1491"
  ],
  "id": "AR-1492",
  "next_action": "Promote and claim, then stage a deterministic customer bundle and document the external signature handoff/validation boundary.",
  "observed_branch": "release/ar-1492-customer-bundle-signing-handoff",
  "observed_dirty": 0,
  "observed_head": "b048fef92f4bdb4eedd5379d645f4288a4b6ab20",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1492-customer-bundle-signing-handoff.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Stage a deterministic customer bundle and provide an explicit external signing handoff and verifier.",
  "task_revision": 8,
  "title": "Customer bundle signing handoff",
  "updated_at": "2026-09-27T16:15:51+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1492-customer-bundle-signing-handoff"
}
---

AR-1490 is blocked on missing external release package and signing authority.
This bounded successor prepares everything that can be produced autonomously,
without fabricating a signature or claiming customer acceptance.

- Stage the exact deterministic runtime bundle input tree, manifest, checksums,
  SBOM, provenance, and verifier invocation from the pinned source.
- Emit a concise external-signing handoff specifying the expected SSHSIG
  namespace, principal, allowed-signers input, and post-signature validation.
- Keep all outputs credential-free and bounded; do not retain private paths or
  secret material and do not contact a provider.

The resulting staging artifact is not a release and cannot satisfy AR-1490
until an authorized external signer supplies and independently validates the
detached signature.

- 2026-09-27T16:13:21+00:00: Dependencies complete; prepare deterministic customer bundle staging
  and explicit external signing handoff without fabricating release authority.

- 2026-09-27T16:13:23+00:00: Claimed by ar1332-record-replay-luna56.

- 2026-09-27T16:13:26+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T16:13:35+00:00: Recorded command exit 0; command argv SHA-256
  1be3df8ac8a124a6199760f3e1a120392451859acb9b8a94d858d5fd026f1c18.

- 2026-09-27T16:13:57+00:00: Recorded command exit 2; command argv SHA-256
  f246114e63922b80b23a8b6c53b5df63c9e3ff55bb234723023a02aa6e259d82.

- 2026-09-27T16:15:51+00:00: Recorded command exit 0; command argv SHA-256
  e501325c2f00e14e73d45ed23a843b3da31b59f73801b77c791316dc6a8bd116.
