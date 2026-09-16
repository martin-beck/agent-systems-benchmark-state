---
{
  "branch": "fix/gitleaks-revision-config-integrity",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T13:25:29+00:00",
  "depends_on": [
    "AR-0003",
    "AR-0898"
  ],
  "id": "AR-0899",
  "next_action": "Unify Gitleaks revision scoping and protect its configuration with executable negative tests.",
  "owner": "asb_ar0899_gitleaks",
  "plan": "../plans/AR-0899.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Resolve GitHub issue 118 by making local and CI Gitleaks scans deterministic and config changes fail closed.",
  "task_revision": 3,
  "title": "Align and harden Gitleaks execution",
  "updated_at": "2026-09-16T11:25:29+00:00",
  "worktree_key": "agent-systems-benchmark-gitleaks-revision-config-integrity"
}
---
## AR-0899

Resolve [product issue 118](https://github.com/martin-beck/agent-systems-benchmark/issues/118).

Live inspection confirmed the documented local command omits CI's `--log-opts`; the unscoped checkout scanned 320 commits rather than the intended revision set.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-16T11:25:26+00:00: Dependencies AR-0003 and AR-0898 verified done; isolated ASB Gitleaks
  repair is dependency-safe.

- 2026-09-16T11:25:29+00:00: Claimed by asb_ar0899_gitleaks.
