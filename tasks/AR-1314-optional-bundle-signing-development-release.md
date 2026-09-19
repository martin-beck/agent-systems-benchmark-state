---
{
  "branch": "feature/ar-1314-optional-bundle-signing",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1314",
  "next_action": "Promote after task review; implement explicit unsigned development/release-bundle mode with checksums, SBOM/provenance, truthful metadata, and fail-closed default verification.",
  "owner": "",
  "plan": "../plans/AR-1314.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Make runtime-bundle signatures optional only through an explicit, truthfully labelled development/release profile.",
  "task_revision": 2,
  "title": "Optional runtime-bundle signing for development and tagged releases",
  "updated_at": "2026-09-19T07:45:37+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1314-optional-bundle-signing"
}
---

# AR-1314

ASB development and tagged-release workflows must be able to publish a runtime bundle without a
detached bundle signature when explicitly selected. This does not remove commit/DCO integrity,
exact content digests, SBOMs, provenance, target checks, or release/tag verification. The default
installer/verifier remains signature-required; unsigned output must be opt-in, clearly labelled,
and rejected as formal qualification evidence.

The implementation must add versioned policy/profile metadata, positive and negative tests,
updated schemas/generated documentation, helpful failure messages, and an offline path. It must
not weaken AR-1307/AR-1308 full-exhaustive formal gates: those continue to require the exact
reviewed signed input bundle and terminal attestation.

- 2026-09-19T07:45:37+00:00: Dependencies are empty; promote explicit unsigned development/release
  profile implementation while preserving formal gates.
