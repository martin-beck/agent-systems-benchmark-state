---
{
  "branch": "repair/ar-1292-tla-provenance",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T06:36:32+00:00",
  "depends_on": [],
  "id": "AR-1292",
  "next_action": "Audit the pinned TLA+ v1.8.0 asset provenance and decide whether a minimal hash-bound fixture update is independently justified; otherwise retain the fail-closed blocker.",
  "observed_branch": "repair/ar-1292-tla-provenance",
  "observed_dirty": 0,
  "observed_head": "c1b1860786e844adb69b8f74e39af290592a89c8",
  "owner": "asb_ar1292_tla_provenance",
  "plan": "../plans/AR-1292.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair or formally retain the pinned TLA+ artifact provenance mismatch blocking formal assurance.",
  "task_revision": 8,
  "title": "Pinned TLA+ artifact provenance repair",
  "updated_at": "2026-09-17T04:38:08+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1292-tla-provenance"
}
---

## AR-1292

PR #119 / AR-0704 is blocked before model execution because the downloaded
official TLA+ v1.8.0 asset has the expected size but does not match the pinned
SHA-256. This AR owns only evidence-led provenance repair or confirmation that
the external release remains unverifiable. It must not weaken or bypass formal
verification, alter native-capacity behavior, or touch asb-tui.

- 2026-09-17T04:34:39+00:00: Dependencies are external-provenance scoped; promote independent audit
  without weakening AR-0704 formal gate.

- 2026-09-17T04:35:18+00:00: Claimed by asb_ar1292_tla_provenance.

- 2026-09-17T04:36:32+00:00: Heartbeat by asb_ar1292_tla_provenance.

- 2026-09-17T04:36:35+00:00: Recorded command exit 0; command argv SHA-256
  146cc60c9b79021ba3ecc84c5e1163b9db4328738be7e71ebdf4f275ec94bb8e.

- 2026-09-17T04:37:37+00:00: Recorded command exit 0; command argv SHA-256
  770e0083dc32f22b0ecb13f98a20aa485bf3558c5eae2ef406000553f522d11e.

- 2026-09-17T04:38:08+00:00: Recorded command exit 0; command argv SHA-256
  d7ea8da35895297f9eebdcf26d7bd88efec48b1765744a58fc7ae71666de9147.
