---
{
  "id": "AR-1736",
  "title": "Require model catalogs and execution parity for every backend",
  "priority": "P0",
  "depends_on": ["AR-1733"],
  "plan": "../plans/AR-1736-backend-model-catalog-execution.md",
  "summary": "Make every supported model-bearing backend enumerate selectable models and carry the exact selection through complete run and sweep execution.",
  "status": "planned",
  "next_action": "Promote after AR-1733; inventory the canonical backend registry and implement catalog, selection, run, and sweep parity with exhaustive fixtures.",
  "owner": "",
  "claim_expires": "",
  "checkpoint_commit": "",
  "task_revision": 1,
  "schema_version": 1,
  "spec_ref": "specs/AR-1736.json",
  "spec_revision": 1,
  "updated_at": "2026-10-08T06:30:00+00:00",
  "branch": "",
  "worktree_key": ""
}
---

Establish one mechanically complete contract for every backend ASB advertises.
Each model-bearing backend must enumerate a bounded, generation/digest-bound
model catalog, allow only catalog-backed model selection, and preserve the exact
backend/model identity through plan, normal run, and bounded sweep results.
Backends that are intentionally model-less must declare that fact explicitly
and remain covered by the same registry completeness gate; they may not be
silently omitted. Development fixtures are authoritative for CI. Optional live
checks may add evidence but missing credentials, authentication, signatures, or
key services must not block this development AR.
