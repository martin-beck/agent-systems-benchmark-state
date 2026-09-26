---
{
  "branch": "qualification/ar-1460-current-main-first-customer-requalification",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-26T20:57:20+00:00",
  "depends_on": [
    "AR-1456",
    "AR-1458"
  ],
  "id": "AR-1460",
  "next_action": "Run the complete ASB-only first-customer production-like qualification against current protected main 36d4bdf35a644a36a8acfdb31078eb7f668a17c4; release only after local/mock campaign, replay, recovery, cleanup, privacy, full gates, and exact-main evidence pass.",
  "observed_branch": "qualification/ar-1460-current-main-first-customer-requalification",
  "observed_dirty": 0,
  "observed_head": "36d4bdf35a644a36a8acfdb31078eb7f668a17c4",
  "owner": "coordinator-ar1460-current-main",
  "plan": "../plans/AR-1460.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Requalify first-customer readiness after the latest local-mock campaign merge.",
  "task_revision": 18,
  "title": "Current-main first-customer requalification",
  "updated_at": "2026-09-26T19:01:26+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1460-current-main-first-customer-requalification"
}
---

AR-1458 qualified protected main before the later AR-1456 local/mock
multi-agent campaign merge became the current origin/main. This AR repeats the
ASB-only customer-like journey on the exact current main, including explicit
local/mock campaign selection, literature workloads, strict offline replay,
cancellation/restart recovery, cleanup and privacy-safe evidence. It must not
contact a remote provider or modify asb-tui. Any deterministic failure gets a
narrow repair AR; no release claim is made from stale evidence.

- 2026-09-26T18:56:57+00:00: Origin/main advanced to AR-1456 merge 36d4bdf after AR-1458 evidence;
  require fresh first-customer qualification against current main.

- 2026-09-26T18:57:00+00:00: Claimed by coordinator-ar1460-current-main.

- 2026-09-26T18:57:20+00:00: Heartbeat by coordinator-ar1460-current-main.

- 2026-09-26T18:57:23+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-09-26T18:57:38+00:00: Recorded command exit 0; command argv SHA-256
  cb829e9c4e7c7cffe24d5a6161df617fb253eb697a3402baff2975d02e925261.

- 2026-09-26T18:57:52+00:00: Recorded command exit 0; command argv SHA-256
  86076dd52358c5f9c1d448888458be6b162987e95aa5807613dba0718e8f6ac8.

- 2026-09-26T18:58:23+00:00: Recorded command exit 0; command argv SHA-256
  35bc7acc0ab5f9b9f9ad6db99e7bc44fc98bf6022db245c15bf191940263efec.

- 2026-09-26T18:58:38+00:00: Recorded command exit 0; command argv SHA-256
  6562de1aecb54fa6d93ab9c9a1b341d0692a229ce5c7ea06fe0df750c577722c.

- 2026-09-26T18:58:52+00:00: Recorded command exit 0; command argv SHA-256
  0506218d93aba0f897152e511b753bfb435291b4d327af1406574275d323f1e6.

- 2026-09-26T18:59:17+00:00: Recorded command exit 0; command argv SHA-256
  5e3d7817f0afba28e5aaab104bd49513090d0424642bd97634a5373b02bde924.

- 2026-09-26T18:59:35+00:00: Recorded command exit 0; command argv SHA-256
  d668e070629151f918df1cdbc00849848752c2f3d85bdca0a78ae5b794cb3d4a.

- 2026-09-26T18:59:50+00:00: Recorded command exit 0; command argv SHA-256
  2a9339303dd144fa361326d713de072ed50ff2dcfcda3b9fb1bf6fef10b99ae6.

- 2026-09-26T19:00:05+00:00: Recorded command exit 0; command argv SHA-256
  2820e956ea95a29ec25997101b9b4cb478cea6c13c7b2f58da619cdb3784eb07.

- 2026-09-26T19:00:20+00:00: Recorded command exit 0; command argv SHA-256
  65b187fffb8d15b430c4a6abb6c9b57647249f140e8ef8f05b2c79466df6e418.

- 2026-09-26T19:01:11+00:00: Recorded command exit 0; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-26T19:01:26+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.
