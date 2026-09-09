---
{
  "branch": "fix/shellcheck-fail-closed",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0003", "AR-0897", "AR-1008"],
  "id": "AR-0898",
  "next_action": "Pin ShellCheck and prove actionlint cannot silently disable its delegated shell analysis.",
  "owner": "",
  "plan": "../plans/AR-0898.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Resolve GitHub issue 117 by installing and explicitly enforcing a digest-pinned ShellCheck.",
  "task_revision": 1,
  "title": "Make ShellCheck fail closed",
  "updated_at": "2026-09-09T13:31:55+00:00",
  "worktree_key": "agent-systems-benchmark-shellcheck-fail-closed"
}
---
## AR-0898

Resolve [product issue 117](https://github.com/martin-beck/agent-systems-benchmark/issues/117).

Live reproduction confirmed that actionlint 1.7.12 exits successfully while reporting its ShellCheck rule disabled when the binary is absent. Explicit ShellCheck 0.11.0 found no current workflow defect.

Implementation has not started. Read the linked plan before claiming.
