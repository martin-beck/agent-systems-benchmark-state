---
{
  "branch": "fix/mini-swe-cancellation-reap-test-isolation",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0101",
    "AR-0102",
    "AR-0103",
    "AR-0308",
    "AR-0902"
  ],
  "id": "AR-0909",
  "next_action": "Reproduce the coverage-only descendant-reap failure and repair only its embedded mini-SWE test boundary.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-0909.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Make mini-SWE cancellation/reaping tests deterministic without weakening production lifecycle guarantees.",
  "task_revision": 1,
  "title": "Harden mini-SWE cancellation reap test isolation",
  "updated_at": "2026-09-09T21:35:00+00:00",
  "worktree_key": "agent-systems-benchmark-mini-swe-cancellation-reap-test-isolation"
}
---
## AR-0909

Repair the test-isolation and lifecycle oracle exposed by PR #126 Repository Quality run
34406581994. Under the exact coverage command,
`mini_swe::tests::cancellation_reaps_owned_descendant_group` completed cancellation but observed
the captured `/proc/<pid>` entry after its bounded poll and failed at `mini_swe.rs:1859`; the same
unrelated product range passed ordinary Rust, native, emulated-AArch64 and fault workflows.

No existing AR owns this exact embedded-test defect. AR-0308 and AR-0513 are complete adapter and
replay qualifications; AR-0902 is complete general fault assurance. Preserve the failure as a
coverage-context lifecycle/isolation signal until the exact process identity and state are
classified.

