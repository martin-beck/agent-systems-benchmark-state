---
{
  "branch": "feature/ar-1814-ruleset-repair",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1814",
  "next_action": "Monitor exact-main post-merge workflows for signed merge 5a6c5477; after all terminal success, accept/release AR-1814 with ruleset before/after receipt and doctor evidence.",
  "observed_branch": "feature/ar-1814-ruleset-repair",
  "observed_dirty": 0,
  "observed_head": "07c590e712df11e555228abf1b9de4add3510d4f",
  "owner": "",
  "plan": "../plans/AR-1814-remove-tlc-development-rule.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "mechanical",
    "evidence_digest": "sha256:2595fc33eda6071001fadbbda6d93b5a24bd5d352f55f0548d376896db0091c9",
    "evidence_ref": "main/5a6c5477cd171606da3aaa0cae9950453ea8dc5c",
    "spec_ref": "specs/AR-1814.json",
    "spec_revision": 1,
    "status": "pass"
  },
  "spec_ref": "specs/AR-1814.json",
  "spec_revision": 1,
  "status": "done",
  "summary": "Remove the stale TLC development status requirement while preserving all native gates and final-delivery formal assurance.",
  "task_revision": 12,
  "title": "Remove stale TLC development ruleset requirement",
  "updated_at": "2026-10-12T10:38:25+00:00",
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

- 2026-10-12T10:25:11+00:00: Recorded command exit 0; command argv SHA-256
  9b45075adf806d00827a705d18eb8c380a615a255dfcc7c53d3aa32ff9bb1164.

- 2026-10-12T10:25:26+00:00: Ruleset minimal repair applied and verified; PR #606 merged via signed
  exact-tree merge 5a6c5477cd171606da3aaa0cae9950453ea8dc5c (base 07c590e7, topic d9972679, tree
  7cf7d050). Post-merge workflows queued/running; no TLC was run.

- 2026-10-12T10:38:16+00:00: Ruleset 24750310 before/after digests recorded; exact comparison proves
  only TLC and Alloy recovery models was removed. PR #606 merged as signed 5a6c5477. All exact-main
  post-merge workflows terminal success, including Development formal assurance without TLC.

- 2026-10-12T10:38:25+00:00: Completed minimal ruleset repair. Before full ruleset digest
  sha256:dd371da427a5c6b57070dcb85d552c71c1b500164cce39c4ad42bcd8fdc5aaa2; after full digest
  sha256:57c08a38ee0feb6a755b04956302a5250e17724d59a2f06b748457a03bc4e5fe; canonical policy
  e0e30afa6076eee0da773e7fb2627127a4515fe45f87ae2f47478d1e5aa627a8 ->
  3ff248abfde816df42ef76f77d3526e58dbf957ff3f2bfcd157b1127113e53eb. Only TLC/Alloy status removed.
  PR #606 merged signed as 5a6c5477; all 11 post-merge workflows terminal success, Development
  formal assurance retained Kani/Loom and no TLC.
