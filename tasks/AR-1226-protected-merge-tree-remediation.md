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
  "observed_branch": "repair/ar1226-current-base",
  "observed_dirty": 0,
  "observed_head": "e730645316d68c23b98c2b721f0f59ae5f352d77",
  "owner": "codex-ar1226-merge-remediation-20260917",
  "plan": "../plans/AR-1226.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Remediate the protected-main merge-tree mismatch from stale-base PR merging.",
  "task_revision": 32,
  "title": "Protected merge-tree remediation",
  "updated_at": "2026-09-17T08:40:24+00:00",
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

- 2026-09-17T08:34:42+00:00: Recorded command exit 0; command argv SHA-256
  c7ddf9d2cbf6aa115a07a161b0213442dee448bb51e88fd34f691d0c9951ef66.

- 2026-09-17T08:35:02+00:00: Recorded command exit 1; command argv SHA-256
  5d2cd504736319db618bfd4426a0f6af9853d4b9e261862068c1617b699deb2f.

- 2026-09-17T08:35:26+00:00: Recorded command exit 0; command argv SHA-256
  5d2cd504736319db618bfd4426a0f6af9853d4b9e261862068c1617b699deb2f.

- 2026-09-17T08:35:45+00:00: Recorded command exit 0; command argv SHA-256
  a38e3aa21a724c90e5d8a78ff7c3331127455ae8ea078191b2f9f354c712bd79.

- 2026-09-17T08:36:00+00:00: Recorded command exit 1; command argv SHA-256
  5a9ca183b36d1cb2e14c65b846445612ef9739a8b5603c104f9a7f5298af9270.

- 2026-09-17T08:36:17+00:00: Recorded command exit 0; command argv SHA-256
  2f635509941dabfce89fd224d23ae45faec4299e4362f4a2b944dd2246b21b8a.

- 2026-09-17T08:36:34+00:00: Recorded command exit 0; command argv SHA-256
  d5caf8db00d8a86f895cf4be2ee70e5027326e4c937817453ef2a28d0e61b010.

- 2026-09-17T08:36:58+00:00: Recorded command exit 1; command argv SHA-256
  ba46efa265c35bf5c9feb10fe9cc341f73255f542091bb4c4bc5f214289c3fac.

- 2026-09-17T08:37:14+00:00: Recorded command exit 0; command argv SHA-256
  59ffd7eb3667122222be0a37e6fa6aaddc76c8d5c62c017ed9f8db056325256f.

- 2026-09-17T08:37:31+00:00: Recorded command exit 2; command argv SHA-256
  14dde9a76340a1ac9c31fd7dbe23f13646c4d3e30bea4d483c333fc80b96f7cf.

- 2026-09-17T08:37:47+00:00: Recorded command exit 1; command argv SHA-256
  7d8603dff072055845f7bed8bd0af3a0b9ef87640f26b78357d68f6ba56410bb.

- 2026-09-17T08:38:32+00:00: Recorded command exit 0; command argv SHA-256
  6cd312f4a06a241c5861e8c14b097ad34f74487f5446cafe610ea10372364e0b.

- 2026-09-17T08:38:53+00:00: Recorded command exit 0; command argv SHA-256
  f3d0698c3a1619ce8e52d0dc2578e94b1b1ef57483ae4ea7aa33a2578f5421b3.

- 2026-09-17T08:39:26+00:00: Recorded command exit 0; command argv SHA-256
  0a3ccd6fa55f00057d856e3c5afa7d53baa1328ad0f84a897094f7ab69269a2e.

- 2026-09-17T08:39:49+00:00: Recorded command exit 0; command argv SHA-256
  f2f9d7ab4c4278fd8c4329799525392ad3a810ade035c322f1e3fa826bfa10a3.

- 2026-09-17T08:40:05+00:00: Recorded command exit 0; command argv SHA-256
  617a1c3c9703d25529b97344f496a68c9e846a3f6fce1fa52617fc43182005df.

- 2026-09-17T08:40:24+00:00: Recorded command exit 0; command argv SHA-256
  404fd802617059c348cce3f213bdaae5324017864914c2fa6175425835f6a81c.
