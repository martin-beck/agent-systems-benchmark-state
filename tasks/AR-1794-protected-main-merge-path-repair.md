---
{
  "branch": "repair/ar-1794-protected-main-merge-path",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1781"
  ],
  "id": "AR-1794",
  "next_action": "Keep open pending a clean signed local merge and green exact-main provenance receipt; do not use GitHub web merge.",
  "observed_branch": "repair/ar-1794-protected-main-merge-path",
  "observed_dirty": 0,
  "observed_head": "198bf86975f64450440e0a30332f732a2233e92e",
  "owner": "",
  "plan": "../plans/AR-1794-protected-main-merge-path-repair.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "hosted",
    "evidence_digest": "sha256:07b6c479de4110138b26e5f5346baa422ee6e92e379be31f47702c92e1b8e536",
    "evidence_ref": "github:martin-beck/agent-systems-benchmark/commit/a89dd44ea978ae6623912ae034fa7e2b40f2dbd0/exact-main-workflows",
    "spec_ref": "specs/AR-1794.json",
    "spec_revision": 1,
    "status": "pass"
  },
  "spec_ref": "specs/AR-1794.json",
  "spec_revision": 1,
  "status": "done",
  "summary": "Repair the protected-main publication path after a GitHub web merge produced a rejected committer identity.",
  "task_revision": 10,
  "title": "Protected-main merge-path repair",
  "updated_at": "2026-10-11T13:51:25+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1794-protected-main-merge-path"
}
---

Repair the merge publication path without weakening portable provenance or
rewriting protected main. The prior AR-1781 merge and failed exact-main run are
inputs, not disposable evidence.

- 2026-10-11T13:22:16+00:00: Claimed by ar1794-protected-merge-repair-luna56.

- 2026-10-11T13:24:53+00:00: Recorded command exit 0; command argv SHA-256
  b2d8d5f1ec56115998d10c70517515e222a8edcd04d514cea0b9a4af8d1021d4.

- 2026-10-11T13:27:15+00:00: Heartbeat by ar1794-protected-merge-repair-luna56.

- 2026-10-11T13:39:00+00:00: Recorded command exit 1; command argv SHA-256
  dc048d5ae1376edccb69d0edfa2e08017a6edcc7434452c85918d74ea1c1a5fa.

- 2026-10-11T13:39:24+00:00: Recorded command exit 0; command argv SHA-256
  44fe5a4fb53c7dd63dedb94e0eff27f7a65de8dc4ec82a0451f4b9d7f146e6e3.

- 2026-10-11T13:39:43+00:00: Recorded command exit 0; command argv SHA-256
  dc048d5ae1376edccb69d0edfa2e08017a6edcc7434452c85918d74ea1c1a5fa.

- 2026-10-11T13:51:18+00:00: Exact-main workflows all passed for signed local merge a89dd44e;
  parents 06514c06/f20f7bf2, reviewed tree 7a5efc6b, SSH signature and DCO verified.

- 2026-10-11T13:51:25+00:00: Closed after PR #580 exact-head review PASS, all required PR checks
  green, signed local merge a89dd44e with exact parents/tree/signature/DCO, and all exact-main
  post-merge workflows green.
