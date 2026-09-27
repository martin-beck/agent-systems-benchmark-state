---
{
  "branch": "release/ar-1493-release-authority-enrollment-handoff",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-27T18:52:55+00:00",
  "depends_on": [
    "AR-1461",
    "AR-1462",
    "AR-1491",
    "AR-1492"
  ],
  "id": "AR-1493",
  "next_action": "Promote and claim after the state commit; audit AR-1492 handoff and implement only repository-side enrollment/verification checks and docs.",
  "observed_branch": "release/ar-1493-release-authority-enrollment-handoff",
  "observed_dirty": 0,
  "observed_head": "5f4e286f051d09bc9706085ca21f68459fc10eb4",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1493-release-authority-enrollment-handoff.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Define and validate the external release-authority enrollment and signed-bundle verification handoff.",
  "task_revision": 6,
  "title": "Release-authority enrollment handoff",
  "updated_at": "2026-09-27T16:53:25+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1493-release-authority-enrollment-handoff"
}
---

AR-1490 is blocked because the authorized external signed customer package and
release authority are absent. AR-1493 makes the safe operator handoff exact
without fabricating authority or turning the AR-1491 non-production fixture
into release evidence.

- Required public handoff identities: SSHSIG namespace
  `asb-runtime-bundle-v1`, externally supplied principal, allowed-signers
  contract, trusted `ssh-keygen` path and SHA-256.
- Required verification: detached signature over exact `manifest.json` bytes,
  exact target identity, complete inventory/SBOM/provenance/checksum validation,
  and bounded offline verifier invocation.
- Forbidden substitutions: generated keys, placeholder principals, unsigned
  release claims, live providers, network access, credentials, private paths,
  or raw signature material in state.

The next action after promotion is to audit the existing AR-1492 output and add
only deterministic repository-side checks/docs. If the external authority
inputs remain absent, release AR-1493 blocked with those exact missing inputs
and preserve AR-1490 as the customer-release blocker.

- 2026-09-27T16:52:40+00:00: Dependencies AR-1461, AR-1462, AR-1491, and AR-1492 are complete.
  Promote the repository-side release-authority enrollment/verification handoff while preserving
  AR-1490 external signed-package blocker.

- 2026-09-27T16:52:46+00:00: Claimed by ar1332-record-replay-luna56.

- 2026-09-27T16:52:55+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T16:53:13+00:00: Recorded command exit 0; command argv SHA-256
  cc7868e69d843cc7770dfabaea600e67a6d6e3ed3f397db89d2e989706c70f92.
