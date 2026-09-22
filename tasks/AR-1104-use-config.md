---
{
  "branch": "feature/use-config",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0876",
    "AR-1101",
    "AR-1102",
    "AR-1103"
  ],
  "id": "AR-1104",
  "next_action": "Wire the UserConfigV1 file into plan, run and sweep as --use-config after the wizard and resolution path exist.",
  "observed_branch": "feature/use-config",
  "observed_dirty": 0,
  "observed_head": "e77850353011a7f87a6b1e525d68723e24a56c25",
  "owner": "",
  "plan": "../plans/AR-1104.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Integrate UserConfigV1 into plan, run and sweep as --use-config.",
  "task_revision": 2,
  "title": "Integrate --use-config into plan, run and sweep",
  "updated_at": "2026-09-22T10:16:40+00:00",
  "worktree_key": "agent-systems-benchmark-use-config"
}
---
Add `--use-config <config.toml>` to `plan`, `run` and `sweep` so the resolved per-agent effective
provider/model from UserConfigV1 feeds the existing digest-pinned selection path without changing
the selection contract. Repository: `martin-beck/agent-systems-benchmark`.

- 2026-09-13T09:57:00+00:00: Frozen scope for parallel setup-wizard series AR-1100..AR-1106.
  No network or credential value is required; config resolution reuses AR-1101 translation and the
  existing fail-closed selection validation.
