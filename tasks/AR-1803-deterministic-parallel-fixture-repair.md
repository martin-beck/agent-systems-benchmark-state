---
{
  "branch": "feature/ar-1803-deterministic-parallel-fixture-repair",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1762"],
  "id": "AR-1803",
  "next_action": "Reproduce and isolate AR-1801 parallel-load fixture failures before implementation.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1803-deterministic-parallel-fixture-repair.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "environmental",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1803.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1803.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Repair nondeterministic parallel provider-selection and comparison fixtures blocking AR-1801 full gates.",
  "task_revision": 1,
  "title": "Deterministic parallel fixture repair",
  "updated_at": "2026-10-12T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1803-deterministic-parallel-fixture-repair"
}
---

Created from AR-1801 exact-head full-gate evidence. Two complete `asb-cli`
runs failed under parallel load with distinct provider/comparison assertions:
`left 6/right 0` at `crates/asb-cli/src/lib.rs:16076` and `:16161`; focused
reruns passed. AR-1801 remains unaccepted until this repair or an equivalent
deterministic root-cause fix makes the full gate green. The dependency is
AR-1762 (done) so this repair can proceed independently while preserving AR-1801
as the affected successor linkage and evidence source.
