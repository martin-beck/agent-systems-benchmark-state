---
{
  "branch": "feature/ar-1307-portable-tlc-runner-repair",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T23:55:11+00:00",
  "depends_on": [
    "AR-1302"
  ],
  "id": "AR-1307",
  "next_action": "Bounded canonical runner repair is implemented; run Ruff/format/mypy/full state suite, inspect remaining provenance/privacy gates, then qualify fresh exact-head portable and required tiers.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-ar1307-runner-20260917",
  "plan": "../plans/AR-1307.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair and publish a canonical, bounded portable TLC runner for AR-1293.",
  "task_revision": 14,
  "title": "Portable TLC runner repair and qualification",
  "updated_at": "2026-09-17T22:03:58+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1307-portable-tlc-runner-repair"
}
---

## AR-1307

AR-1302's initial portable runner is not publishable: it directly invokes TLC,
does not use the canonical admission/attestation path, has incomplete
provenance and unbounded subprocess handling, and does not match the AR-1293
tier contracts. Repair it as a state-repository-only successor and produce
fresh exact-head qualification evidence. Do not touch ASB product, asb-tui,
handoffctl, external root-owned locks, or native-ARM-only requirements.

The predecessor AR-1302 is complete and is independently audited by this AR;
AR-1293 remains blocked until the repaired runner is merged and handed off.
See `../plans/AR-1307.md` for the complete scope, gates, evidence contract,
and protected publication sequence.

- 2026-09-17T23:55:00+00:00: Created as the repair successor after independent exact-head review
  found AR-1302's runner bypassed canonical admission/attestation and lacked required bounded
  execution, profile alignment, provenance, and clean publication evidence. Depends only on done
  AR-1302 so it can unblock blocked AR-1293 without a dependency cycle.

- 2026-09-17T21:53:43+00:00: Predecessor AR-1302 done; successor repair required by independent
  audit; dependencies verified.

- 2026-09-17T21:53:50+00:00: Claimed by codex-ar1307-runner-20260917.

- 2026-09-17T21:54:54+00:00: Heartbeat by codex-ar1307-runner-20260917.

- 2026-09-17T21:55:11+00:00: Heartbeat by codex-ar1307-runner-20260917.

- 2026-09-17T21:56:28+00:00: Recorded command exit 0; command argv SHA-256
  7814f4f5ae3f66be7fe59901f822afa0e2407e90e469a939a2123119a6df97c4.

- 2026-09-17T21:57:50+00:00: Recorded command exit 0; command argv SHA-256
  ceeaba81699fff9952c2220fe54bc01c6111a06d65ee6be972c52bc35a7881a9.

- 2026-09-17T22:00:13+00:00: Recorded command exit 0; command argv SHA-256
  ceeaba81699fff9952c2220fe54bc01c6111a06d65ee6be972c52bc35a7881a9.

- 2026-09-17T22:01:59+00:00: Recorded command exit 0; command argv SHA-256
  ceeaba81699fff9952c2220fe54bc01c6111a06d65ee6be972c52bc35a7881a9.

- 2026-09-17T22:02:41+00:00: Repair progress: imported the reviewed canonical runner/profile chain,
  moved default runtime paths under /srv/data/projects, added bounded argv-only process-group
  execution with output sinks and timeout classification, bound source/input/runner/artifact
  provenance, restricted attestation paths, and removed UUID privacy findings. Focused tlc runner
  suite 24/24 passes.

- 2026-09-17T22:02:54+00:00: Recorded command exit 1; command argv SHA-256
  647c7d343dc9cf1ef1dd6fc2acfc7e6c91186e61e088c40d3bcce31d2d94f1da.

- 2026-09-17T22:03:27+00:00: Recorded command exit 1; command argv SHA-256
  647c7d343dc9cf1ef1dd6fc2acfc7e6c91186e61e088c40d3bcce31d2d94f1da.

- 2026-09-17T22:03:45+00:00: Recorded command exit 0; command argv SHA-256
  647c7d343dc9cf1ef1dd6fc2acfc7e6c91186e61e088c40d3bcce31d2d94f1da.

- 2026-09-17T22:03:58+00:00: Recorded command exit 1; command argv SHA-256
  35451d934feac81f54c673dffd03f08b9f39bdca932e02bb60d02fe7b9510d85.
