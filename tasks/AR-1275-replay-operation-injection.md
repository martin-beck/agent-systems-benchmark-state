---
{
  "branch": "feature/ar-1275-replay-operation-injection",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T01:48:01+00:00",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1275",
  "next_action": "Bind runtime-issued operation handle into the primary argument-level replay command; add supervised cassette response/egress/cancel/restart/timeout/crash/cleanup evidence.",
  "observed_branch": "feature/ar-1275-replay-operation-injection",
  "observed_dirty": 0,
  "observed_head": "2ff7b8df88f747afb08f36f15c224a2c4bdacca1",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1275.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Inject runtime-owned operation handles into actual strict-replay dispatch.",
  "task_revision": 26,
  "title": "Runtime operation injection into replay dispatcher",
  "updated_at": "2026-09-16T23:55:51+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1275-operation-injection"
}
---
## AR-1275

Implement the runtime operation injection seam for actual strict-replay dispatch. Preserve AR-1274's
blocked evidence and do not accept metadata-only or caller-fabricated execution.

- 2026-09-16T23:47:42+00:00: Dependencies AR-1237, AR-1238, and AR-1239 are done; AR-1274 proves the
  actual replay dispatcher still lacks a runtime-issued operation-handle injection point.

- 2026-09-16T23:48:01+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-16T23:49:22+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T23:50:24+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T23:50:42+00:00: Recorded command exit 101; command argv SHA-256
  988929bf75a80adca4e95673c46f16fae49b7c92330988b33c5d7eee2d3af51a.

- 2026-09-16T23:51:25+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T23:51:39+00:00: Recorded command exit 101; command argv SHA-256
  988929bf75a80adca4e95673c46f16fae49b7c92330988b33c5d7eee2d3af51a.

- 2026-09-16T23:52:01+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-16T23:52:13+00:00: Recorded command exit 0; command argv SHA-256
  988929bf75a80adca4e95673c46f16fae49b7c92330988b33c5d7eee2d3af51a.

- 2026-09-16T23:52:37+00:00: Recorded command exit 0; command argv SHA-256
  9b3d971b262b08d7aa6927fcfb61f2d24dd7c6480aed5a116a30ff1dd09270c5.

- 2026-09-16T23:52:46+00:00: Recorded command exit 0; command argv SHA-256
  9b3d971b262b08d7aa6927fcfb61f2d24dd7c6480aed5a116a30ff1dd09270c5.

- 2026-09-16T23:53:06+00:00: Recorded command exit 0; command argv SHA-256
  749aa28ab02ba530afa628f17e3594f872428624ec1fcea0da1cf069bc0804a4.

- 2026-09-16T23:53:17+00:00: Recorded command exit 0; command argv SHA-256
  140d1177ffbb9949e68e4ab9f3d792caf05271e1102e70605ffcd6c9c135d293.

- 2026-09-16T23:53:57+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-16T23:54:21+00:00: Recorded command exit 0; command argv SHA-256
  ef19043205064ea87bec66574bfe246191c9311bc8c404cd8e347d08fbdc44f0.

- 2026-09-16T23:54:36+00:00: Recorded command exit 0; command argv SHA-256
  a5e91d8a6e356ba88fd4835c765ebd2411c75eacaa60f98e203295ec257bd3a5.

- 2026-09-16T23:54:45+00:00: Recorded command exit 0; command argv SHA-256
  e3bbe49c6449de3f1b25d671198ae1b47d11faa50b409cdb5da21861a162ff4e.

- 2026-09-16T23:55:29+00:00: Recorded command exit 0; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-16T23:55:51+00:00: Signed head 2ff7b8d adds runtime ReplayOperationHandle,
  dependency-neutral request/response envelopes, and CLI dispatch_with_runtime_operation adapter
  with positive response and stale/no-fallback tests. Focused CLI adapter 2/2 and core/runtime tests
  pass. Full locked workspace suite passes after fixing workflow_transcript provenance drift caused
  by new lib.rs export (old digest b024... replaced with actual 430f...). Tree clean. Acceptance
  remains incomplete because primary argument-only replay dispatch still cannot obtain
  runtime-issued handle and no real supervised lifecycle/egress fixtures exist.
