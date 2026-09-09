---
{
  "branch": "fix/gitleaks-revision-config-integrity",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0003", "AR-0898"],
  "id": "AR-0899",
  "next_action": "Unify Gitleaks revision scoping and protect its configuration with executable negative tests.",
  "owner": "",
  "plan": "../plans/AR-0899.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Resolve GitHub issue 118 by making local and CI Gitleaks scans deterministic and config changes fail closed.",
  "task_revision": 1,
  "title": "Align and harden Gitleaks execution",
  "updated_at": "2026-09-09T13:31:55+00:00",
  "worktree_key": "agent-systems-benchmark-gitleaks-revision-config-integrity"
}
---
## AR-0899

Resolve [product issue 118](https://github.com/martin-beck/agent-systems-benchmark/issues/118).

Live inspection confirmed the documented local command omits CI's `--log-opts`; the unscoped checkout scanned 320 commits rather than the intended revision set.

Implementation has not started. Read the linked plan before claiming.
