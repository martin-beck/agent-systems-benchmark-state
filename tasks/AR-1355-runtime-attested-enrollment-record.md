---
{
  "branch": "feature/ar-1355-runtime-attested-enrollment-record",
  "checkpoint_commit": "d83a85926f2c4c42317617f4f6b7b3c9a3195874",
  "claim_expires": "2026-09-23T23:02:15+00:00",
  "depends_on": [
    "AR-1352"
  ],
  "id": "AR-1355",
  "next_action": "Implement the runtime/control-owned attested enrollment-record transport, validate target/tool/lease/relay authority inside asb-runtime, mint opaque handles, then consume them in asb run/sweep with positive and negative tests.",
  "observed_branch": "feature/ar-1355-runtime-attested-enrollment-record",
  "observed_dirty": 0,
  "observed_head": "d83a85926f2c4c42317617f4f6b7b3c9a3195874",
  "owner": "codex-asb-runtime-acquisition-successor-luna56",
  "plan": "../plans/AR-1355-runtime-attested-enrollment-record.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Transport runtime-attested enrollment authority without exposing it to the CLI.",
  "task_revision": 3,
  "title": "Runtime-attested enrollment record transport",
  "updated_at": "2026-09-23T21:02:15+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1355-runtime-attested-enrollment-record"
}
---

Successor for AR-1354's exact architectural blocker. The enrollment source
must be runtime/control-owned and attested; do not add caller-supplied public
constructors or synthetic authority. AR-1329 remains fail-closed until merge.

- 2026-09-23T21:02:13+00:00: Promote P0 runtime-attested enrollment record transport; AR-1354
  blocker is recorded and preserved.

- 2026-09-23T21:02:15+00:00: Claimed by codex-asb-runtime-acquisition-successor-luna56.
