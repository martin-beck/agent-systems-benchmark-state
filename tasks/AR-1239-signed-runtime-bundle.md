---
{
  "branch": "feature/ar-1239-signed-runtime-bundle",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1236"],
  "id": "AR-1239",
  "next_action": "Implement asb-bundle-owned manifest/payload wiring for the supervisor and sidecar, then sign and verify the canonical bundle offline.",
  "observed_branch": "feature/ar-1239-signed-runtime-bundle",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1239.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Package and sign the verified loopback supervisor and sidecar runtime payloads.",
  "task_revision": 1,
  "title": "Signed supervisor and sidecar runtime bundle",
  "updated_at": "2026-09-16T08:20:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1239"
}
---

Own only the `asb-bundle` packaging and verification boundary. Do not modify TUI code or take over
AR-1238 runtime launch logic. The bundle must provide immutable, signed payload identities that
SandboxBackend can consume without a mutable `/usr` fallback. Preserve privacy, fail-closed
verification, and unrelated-process safety.
