---
{
  "branch": "fix/hosted-runner-evidence-classification",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T19:25:36+00:00",
  "depends_on": [
    "AR-0702",
    "AR-0848"
  ],
  "id": "AR-0907",
  "next_action": "Add a closed hosted-portability schema and conditional workflow boundary while preserving exact native qualification and its 24.04.4 evidence.",
  "observed_branch": "fix/hosted-runner-evidence-classification",
  "observed_dirty": 7,
  "observed_head": "b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0907.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Separate rolling hosted portability checks from immutable native qualification evidence.",
  "task_revision": 16,
  "title": "Classify hosted runner evidence without weakening native qualification",
  "updated_at": "2026-09-09T17:11:46+00:00",
  "worktree_key": "agent-systems-benchmark-hosted-runner-evidence"
}
---
## AR-0907

Repair the native-platform workflow boundary exposed by the rolling `ubuntu-24.04` hosted image.
Keep AR-0848's exact Ubuntu 24.04.4 native qualification immutable and fail closed while allowing
the hosted runner to report a separately named, non-qualification portability result when its
patch release has advanced.

- 2026-09-09T16:25:32+00:00: Dependencies AR-0702 and AR-0848 are done. The focused
  hosted-portability schema/workflow fence is disjoint from preserved AR-0877/AR-0906 candidates and
  keeps exact native qualification immutable.

- 2026-09-09T16:25:36+00:00: Claimed by quality_20260906.

- 2026-09-09T17:01:56+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-09-09T17:02:19+00:00: Recorded command exit 0; command argv SHA-256
  e4e034d4fe6a0cbcf1b8f2a5b85ed359ee43f7f7fdd8579c0483c523e8b29e8d.

- 2026-09-09T17:02:50+00:00: Recorded command exit 0; command argv SHA-256
  f1b21bc4b1375b43be257a40b139b7b4cc1b1254f16619601de5d42a67c68ed9.

- 2026-09-09T17:06:06+00:00: Recorded command exit 0; command argv SHA-256
  0594fdb22df731bf29f15cdaa373cbe4520119c9851ee20d67a0e0aff2c10158.

- 2026-09-09T17:08:03+00:00: Recorded command exit 0; command argv SHA-256
  effefcb8fba57c2643d3f1fb8ca081872939baf26756d7f7e061c06ba5516227.

- 2026-09-09T17:09:34+00:00: Recorded command exit 1; command argv SHA-256
  a2dfd636fd11a3d4b4fc083d87939e5be5f64d2716d14dbfd1c279574430b0df.

- 2026-09-09T17:11:03+00:00: Recorded command exit 0; command argv SHA-256
  e6da57bcc0d0010e9cfac4ba8776cb05e211ab26ebd48477b1e35988ac60a52a.

- 2026-09-09T17:11:24+00:00: Recorded command exit 1; command argv SHA-256
  69e28ec24d7ef5afadde96b2adcaf023dfe1cd1c91192d3317d988115dd8eba6.

- 2026-09-09T17:11:46+00:00: Recorded command exit 1; command argv SHA-256
  67b373ac3aad4f612afb5c38c6ac7202744c9d848af58ca3383abcf94750a7fa.
