---
{
  "branch": "repair/protected-merge-tree-policy",
  "checkpoint_commit": "ef82484fa78dd31c0d7b5ad48e2dc51a93ec1339",
  "claim_expires": "2026-09-17T10:31:51+00:00",
  "depends_on": [
    "AR-1200"
  ],
  "id": "AR-1226",
  "next_action": "Historical reproduction confirms policy rejects ef82484 before merge-tree comparison because its RSA/GPG signature is not in the allowed SSH trust set. Current clean branch is fd7daa4; create a signed-DCO current-main topic repair, then rerun policy and exact-head gates.",
  "observed_branch": "repair/protected-merge-tree-policy",
  "observed_dirty": 0,
  "observed_head": "fd7daa43549edd67b60076aa6b1eee333061b438",
  "owner": "codex-ar1226-merge-remediation-20260917",
  "plan": "../plans/AR-1226.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Remediate the protected-main merge-tree mismatch from stale-base PR merging.",
  "task_revision": 11,
  "title": "Protected merge-tree remediation",
  "updated_at": "2026-09-17T08:33:23+00:00",
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

- 2026-09-16T06:27:41+00:00: Claimed by asb_ar1232_lifecycle_router.

- 2026-09-16T06:28:15+00:00: Recorded command exit 1; command argv SHA-256
  a4698354b467f618b4915a4e2e6f48a8c7929dae3caa22bbfa85b4e6b9650b60.

- 2026-09-16T06:28:40+00:00: Exact handoffctl reproduction command repository_policy --base
  d354a5127c8d065de64432fb443200612df10f6d --head ef82484fa78dd31c0d7b5ad48e2dc51a93ec1339 failed
  closed: ef82484 lacks an allowed SSH signature; log reports RSA key B5690EEEBB952194 unavailable.
  This is the protected merge-boundary failure, not a product test failure. Worktree
  repair/protected-merge-tree-policy is clean at origin/main fd7daa4.

- 2026-09-16T06:28:50+00:00: Released blocked/ownerless after exact reproduction. repository_policy
  on historical range d354a512..ef82484 fails before merge-tree comparison because ef82484 has an
  unavailable RSA/GPG signature, not an allowed SSH signature. Protected history must not be
  rewritten; requires coordinator-owned forward-only signed-DCO successor/attestation before
  requalification.

- 2026-09-17T08:31:48+00:00: Resume for forward-only current-main protected-merge admission
  remediation; historical merges remain unchanged.

- 2026-09-17T08:31:51+00:00: Claimed by codex-ar1226-merge-remediation-20260917.

- 2026-09-17T08:33:08+00:00: Recorded command exit 0; command argv SHA-256
  a8ad273dd5c2b276d41497f156f8eebb77a964c8bfe6b5811f6be6f9211313fa.

- 2026-09-17T08:33:23+00:00: Recorded command exit 0; command argv SHA-256
  8b167f7b5231a040d3ab55d03be111969472dcb856f803ba82b2ee4e94bd5453.
