---
{
  "branch": "feature/ar-1344-runtime-cli-acquisition-contract",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-23T14:53:22+00:00",
  "depends_on": [
    "AR-1339",
    "AR-1340",
    "AR-1342"
  ],
  "id": "AR-1344",
  "next_action": "Promote after dependencies are verified; implement the runtime-owned per-attempt CLI acquisition API and wire run/sweep without weakening live-provider fail-closed behavior.",
  "observed_branch": "feature/ar-1344-runtime-cli-acquisition-contract",
  "observed_dirty": 1,
  "observed_head": "ce2c2db068b05092f0f63291e0d94d4dbc9cda9c",
  "owner": "codex-asb-ar1344-cli-acquisition-20260923",
  "plan": "../plans/AR-1344-runtime-cli-acquisition-contract.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add the runtime-owned API and CLI integration needed for safe live-provider attempts.",
  "task_revision": 16,
  "title": "Runtime-owned CLI live acquisition contract",
  "updated_at": "2026-09-23T12:55:25+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1344-runtime-cli-acquisition-contract"
}
---

Created from the AR-1329/AR-1343 audit. The bounded relay is available at
`ce2c2db068b05092f0f63291e0d94d4dbc9cda9c`, but the CLI still has no supported
runtime acquisition seam. Keep `spawn_verified_agent` fail-closed until this
contract and its tests are merged and verified.

- 2026-09-23T12:48:42+00:00: Dependencies AR-1339, AR-1340 and AR-1342 are done; promote the
  runtime-owned CLI acquisition contract to unblock AR-1329 without weakening fail-closed policy.

- 2026-09-23T12:49:01+00:00: Claimed by codex-asb-ar1344-cli-acquisition-20260923.

- 2026-09-23T12:51:36+00:00: Heartbeat by codex-asb-ar1344-cli-acquisition-20260923.

- 2026-09-23T12:51:39+00:00: Heartbeat by codex-asb-ar1344-cli-acquisition-20260923.

- 2026-09-23T12:51:41+00:00: Recorded command exit 0; command argv SHA-256
  0ed28ab2d231d0b2bd8ef8fcc7c11bb59995fd48770e67cf2eb8a98065389117.

- 2026-09-23T12:52:03+00:00: Recorded command exit 0; command argv SHA-256
  498ccf248bc166cd8940e579a67ad12e0a07199783062cc3019459f7d310c063.

- 2026-09-23T12:52:17+00:00: Recorded command exit 0; command argv SHA-256
  226bdfa5da4828ff864f3126c00791871661e174da732206e614e2d05843f279.

- 2026-09-23T12:52:30+00:00: Recorded command exit 0; command argv SHA-256
  64e91b86b06d7063344ceb73ae416c58ad2b4352ab0ffeb981b2e3c176ec279c.

- 2026-09-23T12:52:43+00:00: Recorded command exit 0; command argv SHA-256
  e97ef49f6318174d14e9065600b2c65e961302ae81d9280e2033ccf6a24ee585.

- 2026-09-23T12:52:57+00:00: Recorded command exit 0; command argv SHA-256
  06c540c688f38ee91064fecc195e0368937aa75c041bbd3ab833e7f007f6d217.

- 2026-09-23T12:53:22+00:00: Heartbeat by codex-asb-ar1344-cli-acquisition-20260923.

- 2026-09-23T12:55:05+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-23T12:55:25+00:00: Recorded command exit 0; command argv SHA-256
  fd3302a5f725a05b03fb15853ad3dcc3b516ee6915f463c994e7d35647d86a25.
