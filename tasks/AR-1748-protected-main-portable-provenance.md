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
  "observed_dirty": 9,
  "observed_head": "2f52ecbaf79ae8316e0c2a42ad4c4a79dae5d9eb",
  "owner": "ar1748_portable_main_provenance_20261008",
  "plan": "../plans/AR-1748-protected-main-portable-provenance.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1748.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Replace the unavailable Enterprise-only commit-metadata ruleset with a required portable provenance check while preserving Web Flow rejection and atomic protected-main admission.",
  "task_revision": 22,
  "title": "Portable protected-main provenance and capability admission",
  "updated_at": "2026-10-08T17:41:35+00:00",
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

- 2026-10-08T17:34:18+00:00: Recorded command exit 0; command argv SHA-256
  d63e90f8ae54457d339f9b47686f46eba967265df5d7642f02d6501a1414dda7.

- 2026-10-08T17:35:29+00:00: Recorded command exit 0; command argv SHA-256
  3800c82124d3a3bd5076f14ef9f4015d941c14d433b648213f7e7f98b22f7194.

- 2026-10-08T17:36:23+00:00: Recorded command exit 0; command argv SHA-256
  01776cc343dc72841b6be96cc94385211af3f567a39ee755aa05cfdd729a120c.

- 2026-10-08T17:37:22+00:00: Recorded command exit 0; command argv SHA-256
  e715f1e7710a316d80a9064a93f4026cf086ee34e28008219a961375550ec482.

- 2026-10-08T17:38:29+00:00: Recorded command exit 0; command argv SHA-256
  43deabf539411468532103a845b08e52516b30a6e20b99d1145432b4963a4496.

- 2026-10-08T17:39:39+00:00: Recorded command exit 1; command argv SHA-256
  46b0463d9ed539cd84e65e997ecb9d9571e8df343ebc30e4c851d07dfe5625fc.

- 2026-10-08T17:40:23+00:00: Recorded command exit 0; command argv SHA-256
  2bbc8f4f0f4125bfc994cf95057cc8a4fa60bb76c8ebc5127a77d018f2935779.

- 2026-10-08T17:41:03+00:00: Recorded command exit 0; command argv SHA-256
  22cb95ff0d85fc0440379c12418996e08dab806f5bae5a4292a987d567092e52.
