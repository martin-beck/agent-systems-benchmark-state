---
{
  "branch": "",
  "checkpoint_commit": "73b5fd1d14fa0343a7f3cc6d73acc91187d46333",
  "claim_expires": "2026-09-27T12:10:22+00:00",
  "depends_on": [
    "AR-1423",
    "AR-1425"
  ],
  "id": "AR-1426",
  "next_action": "Run full workspace/docs/privacy gates, independent review, then publish signed PR.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1426-evolving-literature-window-refresh.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Refresh evolving literature benchmark windows without stale or incomparable results.",
  "task_revision": 11,
  "title": "Evolving literature workload window refresh",
  "updated_at": "2026-09-27T10:10:22+00:00",
  "worktree_key": ""
}
---

This AR keeps time-windowed and continuously refreshed literature workloads
selectable without treating a mutable source as a stable benchmark. It never
requires live providers or upstream downloads during development or CI.

- 2026-09-24: Added after the literature audit identified stale-window risk for
  LiveCodeBench and SWE-rebench. Existing built-in and stable literature IDs are
  unaffected; every refresh is a new content-addressed identity.

- 2026-09-27T10:05:16+00:00: AR-1423 and AR-1425 are released done; promote the dependency-ready
  offline refresh-manifest implementation.

- 2026-09-27T10:05:18+00:00: Claimed by ar1332-record-replay-luna56.

- 2026-09-27T10:05:29+00:00: Recorded command exit 0; command argv SHA-256
  1d96b88e0f9d8fc7de759f6c96696434c0868b7259e3dae18a69288d99e85bf1.

- 2026-09-27T10:07:11+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T10:07:21+00:00: Recorded command exit 0; command argv SHA-256
  83c84b7ac070d1aac6e30d26c8e7594032ea08b02fde5ebba86c365365ccd50f.

- 2026-09-27T10:08:00+00:00: Recorded command exit 101; command argv SHA-256
  7c50f518ef4f65f5fc0220fd26969854e2f8a8796393c29f5376716d6c2d793a.

- 2026-09-27T10:08:57+00:00: Recorded command exit 0; command argv SHA-256
  013aecd2ab27d39f6fd6e04aac60832985368c7c4d7bbf9e4477a1d59b2bc05a.

- 2026-09-27T10:09:45+00:00: Recorded command exit 0; command argv SHA-256
  dee750d0a840ceafafe8ca38552c64951e15258468c0e24c7c53a2d274663b85.

- 2026-09-27T10:10:14+00:00: Implementation checkpoint: added strict RefreshManifestV1 and
  RefreshManifestInput to asb-workloads. Manifest content-addresses
  source/dataset/window/cutoff/split/evaluator/image/SBOM/license/evidence fields; unknown fields,
  invalid digests, unsupported workloads, incomplete evidence, tampering, and cross-window/evaluator
  comparisons fail closed. Four positive/negative unit tests pass; full asb-workloads lib 39/39
  passes; fmt and clippy pass. The earlier exit-101 was product-related clippy denial
  (too-many-arguments, manual-flatten, collapsible-if) in the new module; fixed by constructor input
  struct, iterator flatten, and rerun success. Docs/WORKLOADS.md records the contract. Signed+DCO
  head 73b5fd1.

- 2026-09-27T10:10:22+00:00: Heartbeat by ar1332-record-replay-luna56.
