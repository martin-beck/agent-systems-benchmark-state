---
{
  "branch": "feature/ar-1281-supervised-cassette-lifecycle",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1281",
  "next_action": "Promote after dependency verification; implement the complete supervised cassette path and lifecycle fault matrix from protected main.",
  "observed_branch": "feature/ar-1281-supervised-cassette-lifecycle",
  "observed_dirty": 0,
  "observed_head": "69e8b064d3121a4bae1f672cdae9c0c8672000bc",
  "owner": "",
  "plan": "../plans/AR-1281.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Execute primary strict replay through a supervised runtime cassette lifecycle.",
  "task_revision": 6,
  "title": "Supervised cassette lifecycle execution",
  "updated_at": "2026-09-17T00:20:48+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1281-supervised-cassette-lifecycle"
}
---

## AR-1281

Implement complete supervised cassette lifecycle execution from protected main. Preserve prior
blocked evidence while requiring real process invocation and fault-matrix proof.

- 2026-09-17T00:19:58+00:00: Dependencies AR-1237, AR-1238, and AR-1239 are done. Prior ARs
  establish missing seams but remain blocked; this AR must implement complete supervised cassette
  execution from protected main.

- 2026-09-17T00:20:12+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-17T00:20:27+00:00: Recorded command exit 0; command argv SHA-256
  def3ba970665af59e194426813d56cfc98aa56216908781bdf51494a1e3d3d31.

- 2026-09-17T00:20:48+00:00: Released blocked/ownerless after fresh protected-main audit; no product
  mutation. Existing runtime has RunningProcess/SandboxBackend::spawn_launch/SidecarHandoff
  primitives, but asb-cli primary replay remains argument-only and no runtime-issued replay
  client/transport exists on main. Safely implementing supervised cassette request/response requires
  a reviewed cross-crate transport and runtime-to-CLI entrypoint; fabricating one would violate
  fail-closed authority. Consequently provider/descendant egress denial, no fallback,
  cancellation/restart, timeout/crash reaping, cleanup, and malformed/stale/duplicate evidence
  remain blocked.
