---
{
  "branch": "feature/ar-1814-ruleset-repair",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T12:23:00+00:00",
  "depends_on": [],
  "id": "AR-1814",
  "next_action": "Re-evaluate PR #606 exact-head mergeability after ruleset repair; merge only with all ordinary checks green, then verify exact-main post-merge workflows and close AR-1814.",
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
  "task_revision": 7,
  "title": "Remove stale TLC development ruleset requirement",
  "updated_at": "2026-10-12T10:24:54+00:00",
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

- 2026-10-12T10:23:40+00:00: Recorded command exit 1; command argv SHA-256
  45c6a9f1981fd6ca38e433afc60e02928e1a0228eee1829a213d8d2aa208d88f.

- 2026-10-12T10:24:22+00:00: Recorded command exit 0; command argv SHA-256
  994b9fc68a8c919ced9d6cb4e417dd22c3735f40f392fe3a980df7c7b54faf29.

- 2026-10-12T10:24:54+00:00: Ruleset 24750310 read before digest
  sha256:dd371da427a5c6b57070dcb85d552c71c1b500164cce39c4ad42bcd8fdc5aaa2; after digest
  sha256:57c08a38ee0feb6a755b04956302a5250e17724d59a2f06b748457a03bc4e5fe. Canonical policy digests
  e0e30afa... -> 3ff248ab.... Mechanical comparison proves only required status TLC and Alloy
  recovery models was removed; no checks added.
