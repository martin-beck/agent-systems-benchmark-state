---
{
  "branch": "feature/ar-1435-local-mock-cli-wiring",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T01:54:20+00:00",
  "depends_on": [
    "AR-1434"
  ],
  "id": "AR-1435",
  "next_action": "Run focused CLI/runtime tests and full locked workspace gates, then review exact diff and publish signed+DCO PR.",
  "owner": "codex-asb-ar1435-local-mock-luna56",
  "plan": "../plans/AR-1435-local-mock-cli-wiring.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Wire deterministic local mock attempts into asb run and sweep configuration qualification.",
  "task_revision": 8,
  "title": "Local mock CLI wiring",
  "updated_at": "2026-09-24T23:54:22+00:00",
  "worktree_key": ""
}
---

Local-only successor to AR-1434. AR-1329 and AR-1432 remain blocked and are
not resumed. This task may exercise only the deterministic runtime-owned mock;
it must not contact OpenRouter or any external provider, mint
`LiveProviderAttempt`, or weaken production egress and default-denial gates.

- 2026-09-24T23:48:43+00:00: AR-1434 is durably done. Promote this sole-dependency local-only CLI
  wiring successor; preserve AR-1329 and AR-1432 blocked, production egress/default denial
  unchanged, and require focused/full/review/PR/seven post-merge gates.

- 2026-09-24T23:48:49+00:00: Claimed by codex-asb-ar1435-local-mock-luna56.

- 2026-09-24T23:48:58+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-09-24T23:49:12+00:00: Recorded command exit 0; command argv SHA-256
  92a0994e27638ae1f7a4c0badbc162e4aa04d283750035404bef41042d45731a.

- 2026-09-24T23:49:34+00:00: Claimed and isolated worktree created from exact protected main merge
  4736db727b13140364b8acd32cf77b7b375eeb17; bind declared branch before product changes.

- 2026-09-24T23:54:20+00:00: Heartbeat by codex-asb-ar1435-local-mock-luna56.

- 2026-09-24T23:54:22+00:00: Implementation begun in bound isolated worktree. Config-backed asb run
  and asb sweep --use-config now execute deterministic LocalProviderMockBackend attempts per
  scheduler admission; no LiveProviderAttempt conversion or external provider path. Focused config
  run/sweep test, five runtime local_mock tests, clippy, fmt, and diff-check pass. A first focused
  assertion exposed scheduler input zero versus mock identity zero rejection; corrected by mapping
  mock attempt identity to input_id + 1 while preserving scheduler evidence.
