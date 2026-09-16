---
{
  "branch": "feature/remote-enrollment-authz",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T19:24:44+00:00",
  "depends_on": [
    "AR-0813"
  ],
  "id": "AR-0814",
  "next_action": "Implement ASB enrollment protocol, CLI ceremony, identity storage, scoped authorization, rotation, and revocation.",
  "observed_branch": "DETACHED",
  "observed_dirty": 0,
  "observed_head": "0a808a635d85fdc4a43b575e3711ef23b38089e3",
  "owner": "asb_ar0814_enrollment_authz",
  "plan": "../plans/AR-0814.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide the ASB protocol and CLI for explicit remote trust and least-privilege roles.",
  "task_revision": 6,
  "title": "Secure remote enrollment and authorization",
  "updated_at": "2026-09-16T17:25:45+00:00",
  "worktree_key": "agent-systems-benchmark-remote-enrollment-authz"
}
---
## AR-0814

Pair remote TUIs with runners using explicit trust and least-privilege roles.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-10T19:20:00+00:00: Removed TUI implementation from this ASB AR. The standalone asb-tui
  enrollment experience belongs to AR-0817 and consumes this protocol.

- 2026-09-16T17:24:41+00:00: AR-0813 completed with signed transport and post-merge gates; promote
  enrollment/authz implementation.

- 2026-09-16T17:24:44+00:00: Claimed by asb_ar0814_enrollment_authz.

- 2026-09-16T17:25:38+00:00: Recorded command exit 0; command argv SHA-256
  a2ed473f94ce905fc478776983cd071465a36de4319a44489aa21fa5c1167fef.
