---
{
  "branch": "feature/measurement-selection-plan",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T06:32:03+00:00",
  "depends_on": [
    "AR-0104",
    "AR-1036"
  ],
  "id": "AR-1037",
  "next_action": "After AR-1036, add canonical measurement IDs to validated ASB plans and make collection honor them without any UI code.",
  "observed_branch": "feature/measurement-selection-plan",
  "observed_dirty": 4,
  "observed_head": "1a19b692d724fd5ba1996470daccbfed06171a0a",
  "owner": "codex-root-ar1037-selection-20260911",
  "plan": "../plans/AR-1037.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Carry catalog-backed measurement choices through ASB plan validation, collection and evidence.",
  "task_revision": 18,
  "title": "Add measurement selection to validated run plans",
  "updated_at": "2026-09-11T03:47:42+00:00",
  "worktree_key": "agent-systems-benchmark-measurement-selection-plan"
}
---
## AR-1037

Implement only the ASB runner/control semantics required to make measurement choices real: closed
plan fields, catalog validation, canonical hashing, source gating and evidence provenance. All
search, group tri-state behavior, selection/deselection controls, rendering and help remain
exclusively in `martin-beck/asb-tui` under AR-1014.

- 2026-09-11T03:31:52+00:00: Dependencies AR-0104 and AR-1036 are done; fully green protected-main
  descendant 1a19b692 qualifies the catalog control boundary. Promote ASB-only measurement selection
  semantics with no frontend implementation.

- 2026-09-11T03:32:03+00:00: Claimed by codex-root-ar1037-selection-20260911.

- 2026-09-11T03:32:25+00:00: Recorded command exit 0; command argv SHA-256
  e93ce83471cb6810cbe793116d30cf552be146bcaee414eb9dd68d1b35c47e90.

- 2026-09-11T03:40:05+00:00: Recorded command exit 101; command argv SHA-256
  f8f5cfd8b7ce540eefbcf1ed8593289dcea998c3c67ea623a330a2542845d0e8.

- 2026-09-11T03:40:29+00:00: Recorded command exit 0; command argv SHA-256
  dc4208b7165aebbd5611033bf943ec0ee209e69a0410bd55afd62e8f31008cbd.

- 2026-09-11T03:41:28+00:00: Recorded command exit 1; command argv SHA-256
  0ea6fe112897f4953580feb3bbd086ea218eaea05048e5dfabc08e70b91b8c71.

- 2026-09-11T03:41:41+00:00: Recorded command exit 0; command argv SHA-256
  09c15c70d984c743b03913b5a4a636b645d98c882e9c14f86f69af03ba63b252.

- 2026-09-11T03:41:59+00:00: Recorded command exit 0; command argv SHA-256
  9ccfcfa9c389668cf5c8f871d8115e0a1d8e06c78ef5b3135f5f0f79d08664ab.

- 2026-09-11T03:45:25+00:00: Recorded command exit 101; command argv SHA-256
  476105f72caa4cc95ff415ef324a9ee1e1a12507c57629e7848ad27364dad583.

- 2026-09-11T03:46:13+00:00: Recorded command exit 0; command argv SHA-256
  476105f72caa4cc95ff415ef324a9ee1e1a12507c57629e7848ad27364dad583.

- 2026-09-11T03:46:43+00:00: Recorded command exit 101; command argv SHA-256
  baf579661282d83e638b954ec98e02553246afabb34f1d5c8487dd77135c9272.

- 2026-09-11T03:47:42+00:00: Recorded command exit 0; command argv SHA-256
  09c15c70d984c743b03913b5a4a636b645d98c882e9c14f86f69af03ba63b252.
