---
{
  "branch": "feature/ar-1813-cli2key-runtime-factory-contract",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1779",
    "AR-1799"
  ],
  "id": "AR-1813",
  "next_action": "Promote and claim; implement the runtime-owned receipt contract and opaque LiveProviderAttemptFactory API needed by AR-1812, then complete review, merge, and post-merge verification.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
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
  "status": "open",
  "summary": "Expose the runtime-owned cli2key receipt contract and opaque factory required for ordinary CLI bootstrap.",
  "task_revision": 2,
  "title": "Expose cli2key runtime factory contract",
  "updated_at": "2026-10-12T10:14:31+00:00",
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
