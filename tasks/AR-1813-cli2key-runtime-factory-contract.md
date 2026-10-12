---
{
  "branch": "feature/ar-1813-cli2key-runtime-factory-contract",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T12:16:18+00:00",
  "depends_on": [
    "AR-1779",
    "AR-1799"
  ],
  "id": "AR-1813",
  "next_action": "PR #607 exact head d5f814896ccfd71bd0fe09028dc94d7fcf4c88ec is under hosted non-TLC checks; TLC check is present only because PR #606 formal-separation merge is still blocked by GitHub review policy. After ordinary checks and independent review, reconcile the formal lane before merge.",
  "observed_branch": "feature/ar-1813-cli2key-runtime-factory-contract",
  "observed_dirty": 0,
  "observed_head": "458ce867b1e973fdf51049cd95ff893fe17d4a40",
  "owner": "ar1810-cli2key-luna56",
  "plan": "../plans/AR-1813-cli2key-runtime-factory-contract.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1813.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1813.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Expose the runtime-owned cli2key receipt contract and opaque factory required for ordinary CLI bootstrap.",
  "task_revision": 12,
  "title": "Expose cli2key runtime factory contract",
  "updated_at": "2026-10-12T10:38:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1813-cli2key-runtime-factory-contract"
}
---

AR-1812 cannot safely implement its ordinary `run`/`sweep` bootstrap because
the production `asb-runtime` factory constructor is private and the generic
AR-1779 receipt lacks the runtime identity/bridge fields. This AR owns only
that runtime-owned API and versioned non-secret receipt contract; it must not
fabricate authority in the CLI or introduce a provider fallback.

- 2026-10-12T10:14:31+00:00: Promoted P0 prerequisite for AR-1812: expose a runtime-owned verified
  cli2key receipt contract and opaque LiveProviderAttemptFactory without CLI authority fabrication
  or provider fallback.

- 2026-10-12T10:14:34+00:00: Claimed by ar1810-cli2key-luna56.

- 2026-10-12T10:14:56+00:00: Bound worktree
  agent-systems-benchmark-ar-1813-cli2key-runtime-factory-contract on branch
  feature/ar-1813-cli2key-runtime-factory-contract.

- 2026-10-12T10:16:18+00:00: Heartbeat by ar1810-cli2key-luna56.

- 2026-10-12T10:21:08+00:00: Recorded exact PR head and the inherited TLC workflow dependency; no
  TLC execution performed locally.

- 2026-10-12T10:34:32+00:00: Recorded command exit 0; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-10-12T10:35:07+00:00: Recorded command exit 0; command argv SHA-256
  297bf0426da2b3a34cc8d291742b5d89c6c71377df2a616c878604996ff250b5.

- 2026-10-12T10:37:41+00:00: Recorded command exit 0; command argv SHA-256
  7b80382008cb01e3ea6fa6e88054b624464f9801b40ed57f947b01892a686ae8.

- 2026-10-12T10:38:00+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.
