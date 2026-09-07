---
{
  "branch": "fix/runner-isolation-hardening",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0830", "AR-0831"],
  "id": "AR-0836",
  "next_action": "Separate job execution from operator-owned installation, credentials, control state, and diagnostics with a verified immutable boundary.",
  "owner": "",
  "plan": "../plans/AR-0836.md",
  "priority": "P0",
  "schema_version": 1,
  "task_revision": 1,
  "status": "planned",
  "summary": "Harden development-host runner isolation against same-UID job tampering and diagnostic leakage.",
  "title": "Harden runner isolation and credential boundaries",
  "updated_at": "2026-09-07T00:00:00+00:00",
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
