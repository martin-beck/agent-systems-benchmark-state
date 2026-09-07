---
{
  "branch": "fix/runner-isolation-hardening",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T09:19:37+00:00",
  "depends_on": [
    "AR-0830",
    "AR-0831"
  ],
  "id": "AR-0836",
  "next_action": "Separate job execution from operator-owned installation, credentials, control state, and diagnostics with a verified immutable boundary.",
  "observed_branch": "fix/runner-isolation-hardening",
  "observed_dirty": 0,
  "observed_head": "a4782cdc467d38996473168cc5d2ccedfae75a25",
  "owner": "quality-20260906",
  "plan": "../plans/AR-0836.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Harden development-host runner isolation against same-UID job tampering and diagnostic leakage.",
  "task_revision": 4,
  "title": "Harden runner isolation and credential boundaries",
  "updated_at": "2026-09-07T07:49:58+00:00",
  "worktree_key": "agent-systems-benchmark-runner-isolation-hardening"
}
---
## AR-0836

Independent audit found that the runner job identity can traverse or modify installation,
credentials, control files, manifests, and diagnostics, and that diagnostics can expose private
paths and session metadata. Harden before any trusted workflow is dispatched.

Acceptance criteria:

- Use separate operator/service and job identities or an equivalent namespace/broker boundary.
- Make complete installation and control state immutable or operator-owned; verify all relevant files.
- Ensure jobs cannot read registration credentials or poison future registrations.
- Bound and redact diagnostics before storage/upload; add leakage and tamper negative tests.
- Qualify interrupted jobs, reset/recovery, and repeated runs with independent security review.

- 2026-09-07T07:49:35+00:00: Dependencies AR-0830 and AR-0831 are durably done; prioritize P0
  remediation of runner identity separation, credential isolation, immutable control state, bounded
  redacted diagnostics, tamper negatives, and interrupted-run recovery before any further trusted
  dispatch.

- 2026-09-07T07:49:37+00:00: Claimed by quality-20260906.
