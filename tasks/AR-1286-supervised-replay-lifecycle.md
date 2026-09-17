---
{
  "branch": "feature/ar-1286-supervised-replay-lifecycle",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T04:19:17+00:00",
  "depends_on": [
    "AR-1282",
    "AR-1285",
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1286",
  "next_action": "Worktree created at /srv/data/projects/agent-systems-benchmark-ar-1286-supervised-replay-lifecycle from origin/main 2fd9055. Inspect ReplayLaunchContext, SandboxBackend::spawn_launch, and CLI replay authority seam; implement bounded child lifecycle without asb-tui.",
  "observed_branch": "feature/ar-1286-supervised-replay-lifecycle",
  "observed_dirty": 1,
  "observed_head": "2fd90557a4e7be32fab590f47bc501462127c1c1",
  "owner": "asb_ar1286_supervised_replay_lifecycle",
  "plan": "../plans/AR-1286.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Execute strict-replay cassettes through the runtime-owned supervised lifecycle.",
  "task_revision": 8,
  "title": "Supervised strict-replay cassette lifecycle",
  "updated_at": "2026-09-17T02:21:20+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1286-supervised-replay-lifecycle"
}
---

## AR-1286

Implement the next ASB-only lifecycle boundary after the merged AR-1282 transport and AR-1285
launch factory. Preserve all fail-closed authority, egress, cleanup, and no-fallback requirements;
do not touch or claim asb-tui behavior.

- Created as the dependency-safe successor for the supervised cassette lifecycle after AR-1282 and
  AR-1285 completed. Earlier blocked replay lifecycle records remain historical evidence and are
  not implementation inputs.

- 2026-09-17T02:19:11+00:00: Dependencies AR-1282, AR-1285, AR-1237, AR-1238, and AR-1239 are done;
  promote this ASB-only lifecycle successor.

- 2026-09-17T02:19:17+00:00: Claimed by asb_ar1286_supervised_replay_lifecycle.

- 2026-09-17T02:20:12+00:00: Setup checkpoint: declared isolated worktree is clean at exact
  protected main 2fd9055. Initial handoffctl bootstrap from canonical checkout was rejected because
  invocation worktree did not yet match the declared AR worktree; created the declared worktree from
  origin/main, and all subsequent product commands will run there through handoffctl.

- 2026-09-17T02:20:47+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-17T02:21:06+00:00: Recorded command exit 0; command argv SHA-256
  920d4dc14984153ac58c98ec2c07595757e3a94ef557766798bdb312328d8ce3.

- 2026-09-17T02:21:20+00:00: Recorded command exit 0; command argv SHA-256
  b56a340314485ff8f50e5f6d74979c76e51d72077e6eaa02dd388001d918fb1c.
