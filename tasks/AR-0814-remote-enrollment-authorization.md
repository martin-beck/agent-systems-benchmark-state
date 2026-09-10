---
{
  "branch": "feature/remote-enrollment-authz",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0813"],
  "id": "AR-0814",
  "next_action": "Implement ASB enrollment protocol, CLI ceremony, identity storage, scoped authorization, rotation, and revocation.",
  "owner": "",
  "plan": "../plans/AR-0814.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Provide the ASB protocol and CLI for explicit remote trust and least-privilege roles.",
  "task_revision": 2,
  "title": "Secure remote enrollment and authorization",
  "updated_at": "2026-09-10T19:20:00+00:00",
  "worktree_key": "agent-systems-benchmark-remote-enrollment-authz"
}
---
## AR-0814

Pair remote TUIs with runners using explicit trust and least-privilege roles.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-10T19:20:00+00:00: Removed TUI implementation from this ASB AR. The standalone asb-tui
  enrollment experience belongs to AR-0817 and consumes this protocol.
