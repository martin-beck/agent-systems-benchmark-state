---
{
  "branch": "feature/ar-1347-neutral-live-supervisor-composition",
  "checkpoint_commit": "a336d6744b1a82f36a706ec606b847c92d49cfd3",
  "claim_expires": "2026-09-23T17:37:59+00:00",
  "depends_on": [
    "AR-1327",
    "AR-1328",
    "AR-1339",
    "AR-1340"
  ],
  "id": "AR-1347",
  "next_action": "Define and implement a neutral opaque credential-injection/supervisor composition contract that avoids an asb-runtime to asb-agents dependency cycle; then complete runtime-owned live acquisition with bounded target, lease, namespace, token, relay, credential capability, and teardown tests. Keep AR-1329 fail-closed until merge and post-merge verification.",
  "observed_branch": "feature/ar-1347-neutral-live-supervisor-composition",
  "observed_dirty": 1,
  "observed_head": "a336d6744b1a82f36a706ec606b847c92d49cfd3",
  "owner": "codex-asb-ar1329-live-cli-luna56",
  "plan": "../plans/AR-1347-neutral-live-supervisor-composition.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add the dependency-safe opaque supervisor contract needed for live-provider acquisition.",
  "task_revision": 9,
  "title": "Neutral live-supervisor composition contract",
  "updated_at": "2026-09-23T15:40:52+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1347-neutral-live-supervisor-composition"
}
---

Created from the AR-1346 cross-crate audit. `ResolvedCredential` is private to
`asb-agents`, which already depends on `asb-runtime`; do not expose secret bytes
or introduce a cyclic dependency.

- 2026-09-23T15:37:56+00:00: Promote neutral cross-crate supervisor composition repair from AR-1346
  audit; dependencies complete and AR-1329 remains fail-closed.

- 2026-09-23T15:37:59+00:00: Claimed by codex-asb-ar1329-live-cli-luna56.

- 2026-09-23T15:39:17+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-23T15:39:48+00:00: Recorded command exit 0; command argv SHA-256
  a37d35e290b63ddfe8627f9bdb0474ef6d3f2654ade91f05cd9a55c3a713fceb.

- 2026-09-23T15:40:09+00:00: Recorded command exit 101; command argv SHA-256
  e8beebac0638d83321c84d952814966bbba80dc16ee7dd3d3ead10f3c2b72292.

- 2026-09-23T15:40:33+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-23T15:40:52+00:00: Recorded command exit 101; command argv SHA-256
  e8beebac0638d83321c84d952814966bbba80dc16ee7dd3d3ead10f3c2b72292.
