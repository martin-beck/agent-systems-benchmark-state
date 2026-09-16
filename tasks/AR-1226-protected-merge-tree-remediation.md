---
{
  "branch": "repair/protected-merge-tree-policy",
  "checkpoint_commit": "ef82484fa78dd31c0d7b5ad48e2dc51a93ec1339",
  "claim_expires": "",
  "depends_on": [
    "AR-1200"
  ],
  "id": "AR-1226",
  "next_action": "Reproduce the protected-main merge-tree mismatch and requalify a current-main topic tree without weakening policy.",
  "owner": "",
  "plan": "../plans/AR-1226.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Remediate the protected-main merge-tree mismatch from stale-base PR merging.",
  "task_revision": 2,
  "title": "Protected merge-tree remediation",
  "updated_at": "2026-09-16T06:27:38+00:00",
  "worktree_key": "agent-systems-benchmark-protected-merge-tree-remediation"
}
---

ASB PR #175 was merged at `ef82484fa78dd31c0d7b5ad48e2dc51a93ec1339` after PR #174, while its
reviewed topic branch still descended from the pre-#174 main. Post-merge Repository quality run
`34955354581` failed closed with `protected-main merge tree differs from the reviewed topic tree`
for range `d354a5127c8d065de64432fb443200612df10f6d..ef82484fa78dd31c0d7b5ad48e2dc51a93ec1339`.
All other post-merge assurance runs succeeded. This task owns the reproduction and a corrected,
current-main requalification; it must not mark the merge usable until policy assurance passes.

- 2026-09-16T06:27:38+00:00: Promote P0 ASB-only protected merge-tree remediation; dependency
  AR-1200 is complete.
