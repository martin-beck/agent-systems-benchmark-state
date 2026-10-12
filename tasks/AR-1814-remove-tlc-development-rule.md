---
{
  "branch": "feature/ar-1814-ruleset-repair",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T12:23:00+00:00",
  "depends_on": [],
  "id": "AR-1814",
  "next_action": "Promote and claim; inspect ruleset 24750310, remove only the stale TLC/Alloy required status, verify the minimal diff, then complete PR #606 merge and post-merge verification.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "ar1773-catalog-repair-luna56",
  "plan": "../plans/AR-1814-remove-tlc-development-rule.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "mechanical",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1814.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1814.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Remove the stale TLC development status requirement while preserving all native gates and final-delivery formal assurance.",
  "task_revision": 4,
  "title": "Remove stale TLC development ruleset requirement",
  "updated_at": "2026-10-12T10:23:34+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1814-ruleset-repair"
}
---

The protected-main ruleset still requires `TLC and Alloy recovery models`,
which contradicts the completed development/formal workflow separation in
AR-1811. This repair owns only the minimal ruleset edit and the exact evidence
needed to unblock ordinary development merges; it does not bypass or weaken
the remaining required checks.

- 2026-10-12T10:22:51+00:00: Promoted P0 ruleset repair: remove only stale TLC/Alloy development
  requirement after AR-1811 formal separation, preserving all other native gates and final-delivery
  formal assurance.

- 2026-10-12T10:23:00+00:00: Claimed by ar1773-catalog-repair-luna56.

- 2026-10-12T10:23:34+00:00: Bound worktree agent-systems-benchmark-ar-1814-ruleset-repair on branch
  feature/ar-1814-ruleset-repair.
