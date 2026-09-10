---
{
  "branch": "feature/asb-tui-compatibility-detection",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T15:45:28+00:00",
  "depends_on": [
    "AR-1017"
  ],
  "id": "AR-1018",
  "next_action": "Implement platform, architecture, ASB-version, protocol, and terminal capability detection.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-1018.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Detect whether an asb-tui bundle is compatible before installation or launch.",
  "task_revision": 9,
  "title": "Add asb-tui compatibility and terminal capability detection",
  "updated_at": "2026-09-10T12:51:32+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-compatibility-detection"
}
---
Detect OS/distribution, architecture, ASB version, protocol version, exact coordinator and
workflow-quality release compatibility, terminal dimensions/features,
SSH/tmux/screen context, and filesystem/runtime requirements. Select only compatible bundles and fail
closed with actionable diagnostics for unsupported combinations.

Acceptance criteria: deterministic machine-readable capability report, resize/channel tests, negative
fixtures for mismatches, privacy-safe diagnostics, and no host identifiers in public artifacts.

- 2026-09-10T12:40:02+00:00: AR-1017 is durably done at state 9aa38bcc with public exact-head checks
  and protection verified; AR-1018 is dependency-ready and owns disjoint compatibility detection.

- 2026-09-10T12:40:09+00:00: Claimed by contracts_20260906.

- 2026-09-10T12:40:29+00:00: Recorded command exit 0; command argv SHA-256
  263e132bbd0547042ae890d6380355f5364a45e5528910bdc3a67484dad324a6.

- 2026-09-10T12:45:28+00:00: Heartbeat by contracts_20260906.

- 2026-09-10T12:48:53+00:00: Recorded command exit 0; command argv SHA-256
  420472530e9d05303c33574061da3466b08bd64279b64a0008c4823f781a749a.

- 2026-09-10T12:49:04+00:00: Recorded command exit 101; command argv SHA-256
  59ec19432c7293e890383e067eeb07cf9a2ffae1aa12643fbdd0d792c7fa7fc0.

- 2026-09-10T12:51:21+00:00: Recorded command exit 0; command argv SHA-256
  420472530e9d05303c33574061da3466b08bd64279b64a0008c4823f781a749a.

- 2026-09-10T12:51:32+00:00: Recorded command exit 0; command argv SHA-256
  c9be30c10bf536e6c31fe8e5e3c2dbea49e29970e128dab52c3e4c45b3406367.
