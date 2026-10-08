---
{
  "branch": "repair/ar-1748-portable-main-provenance",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T20:27:25+00:00",
  "depends_on": [
    "AR-1427",
    "AR-1431"
  ],
  "id": "AR-1748",
  "next_action": "Implement a generally available required CI provenance check and capability-aware ruleset admission, then independently review, merge, verify post-merge CI, and perform one bounded live settings apply with two consecutive audits.",
  "observed_branch": "repair/ar-1748-portable-main-provenance",
  "observed_dirty": 0,
  "observed_head": "2f52ecbaf79ae8316e0c2a42ad4c4a79dae5d9eb",
  "owner": "ar1748_portable_main_provenance_20261008",
  "plan": "../plans/AR-1748-protected-main-portable-provenance.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1748.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Replace the unavailable Enterprise-only commit-metadata ruleset with a required portable provenance check while preserving Web Flow rejection and atomic protected-main admission.",
  "task_revision": 9,
  "title": "Portable protected-main provenance and capability admission",
  "updated_at": "2026-10-08T17:33:15+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1748-portable-main-provenance"
}
---

AR-1746 merged bounded settings diagnostics and passed every exact-main
post-merge workflow, but its single live ruleset creation attempt was rejected
atomically with HTTP 422. Two audits prove that no repository setting or
ruleset was partially changed. Read-only diagnosis identifies the requested
`committer_email_pattern` restriction as an Enterprise-organization metadata
feature, while ASB is a public user-owned GitHub Free repository. Core public
rulesets are available and repository administration is working.

This successor must preserve the actual admission predicate. It may not remove
the metadata rule and then claim Web Flow rejection is enforced: GitHub Web
Flow commits can be GitHub-signed and web signoff supplies DCO but does not
prove the reviewed local merge path. Instead, add a mandatory portable CI
provenance check that rejects Web Flow/noreply commits and validates the exact
signed-DCO merge identity, require that check in the generally available core
ruleset, and make the settings tool capability-aware before any mutation.

Development integration requires an independent technical worker but permits
the same GitHub account; it does not require a second account, production
credentials, a verified release, or an Enterprise upgrade. If the portable
contract cannot be expressed and observed on the current repository, fail
closed with an exact typed blocker rather than weakening it.

- 2026-10-08T17:24:52+00:00: Promoted after AR-1746 atomic rejection diagnosis: implement portable
  Web Flow provenance enforcement and capability-aware core ruleset admission without weakening
  development policy.

- 2026-10-08T17:27:25+00:00: Claimed by ar1748_portable_main_provenance_20261008.

- 2026-10-08T17:27:34+00:00: Recorded command exit 0; command argv SHA-256
  b7023a6f6301c30be2548d060b4866d61bffe515b6b2c81f33dc2fb25c858b10.

- 2026-10-08T17:30:20+00:00: Recorded command exit 0; command argv SHA-256
  3a8b5522600b1ac244d11f78d2a060d1a8e60b8ba3477ef6aa7586d54d5a5d8c.

- 2026-10-08T17:31:33+00:00: Recorded command exit 1; command argv SHA-256
  1933e16a4a920a306a9d32682500f1537f49a615d94c6d095dcc6c288fa88e6f.

- 2026-10-08T17:32:11+00:00: Recorded command exit 0; command argv SHA-256
  2c04dad3bf114734e4dadc332f2895b056f1a1c0391d5f3afe4b112cf60dd603.

- 2026-10-08T17:33:15+00:00: Recorded command exit 0; command argv SHA-256
  89271759062811bdecd44b61893fc6c5e9f84d22e32c3680c24a59f1830bca23.
