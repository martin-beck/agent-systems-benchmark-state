---
{
  "branch": "feature/ar-1437-local-record-replay-campaign",
  "checkpoint_commit": "a7d041bdca739f29b2e09d60f7d50924fbe6cf74",
  "claim_expires": "2026-09-25T03:27:52+00:00",
  "depends_on": [
    "AR-1436",
    "AR-1328"
  ],
  "id": "AR-1437",
  "next_action": "Run focused/full offline gates, independent exact-head review, then publish PR.",
  "observed_branch": "feature/ar-1437-local-record-replay-campaign",
  "observed_dirty": 2,
  "observed_head": "18a0df9b4312e49196c1c8202b48a183ed83b073",
  "owner": "codex-asb-ar1437-local-record-luna56",
  "plan": "../plans/AR-1437-local-record-replay-campaign.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify deterministic local record/replay and campaign journeys over the runtime mock.",
  "task_revision": 10,
  "title": "Local record/replay campaign qualification",
  "updated_at": "2026-09-25T01:31:32+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1437-local-record-replay-campaign"
}
---

Local-only successor to AR-1436. Use only completed AR-1436 and AR-1328 as
hard dependencies. AR-1330, AR-1331, AR-1332, and AR-1333 remain future/live
references; AR-1329 and AR-1338 remain untouched. No live provider capture or
authority is resumed.

The implementation must use the deterministic runtime-owned local mock,
preserve offline/default denial and production egress boundaries, emit bounded
digest-only evidence, and add positive plus hostile tests for record/replay or
campaign qualification. Require focused/full/review/PR/seven post-merge gates.

- 2026-09-25T01:27:49+00:00: Promote local-only record/replay campaign successor. Completed
  dependencies AR-1436 and AR-1328 are done; AR-1330/1331/1332/1333 remain future/live references
  and AR-1329/1338 remain untouched. Preserve offline/default denial and no live provider authority.

- 2026-09-25T01:27:52+00:00: Claimed by codex-asb-ar1437-local-record-luna56.

- 2026-09-25T01:28:00+00:00: Recorded command exit 0; command argv SHA-256
  796ef0e547da4a0a8917d2b28477bfd5b901b97bc40a404ac48e361aabe02249.

- 2026-09-25T01:29:24+00:00: Recorded command exit 1; command argv SHA-256
  d6c60d6497992ce859262bfb988a61353f99892a4eb3cdbd8d771ad8e064b538.

- 2026-09-25T01:30:00+00:00: Recorded command exit 0; command argv SHA-256
  c9ee46ef8a96e739304c9e2c58592afc92894b3d6ae6bc27e969acc8e8c4b624.

- 2026-09-25T01:30:45+00:00: Implementation committed/pushed as signed+DCO a7d041b. Added explicit
  `asb easy record-campaign MANIFEST.json --local-mock` over existing bounded record-campaign
  sealing, with hostile live/config option rejection, positive campaign test, docs, and final CLI
  provenance digest. No provider capture, live authority, or replay fallback added.

- 2026-09-25T01:31:32+00:00: Recorded command exit 0; command argv SHA-256
  9499c0c9f7493c93690381ad0802155d6eee0d2965f70d5d086e271f050d0188.
