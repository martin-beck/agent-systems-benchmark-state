---
{
  "branch": "repair/ar-1312-post-merge-coverage-floor",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-19T10:09:52+00:00",
  "depends_on": [],
  "id": "AR-1312",
  "next_action": "Coverage reproduction failed in cargo llvm-cov workspace summary at 08:13:54: three asb-cli capability-contract tests found checkout default_*.profraw files and exited 101; add coverage-mode target sink, clean generated profiles, rerun focused/full coverage and record results.",
  "observed_branch": "repair/ar-1312-post-merge-coverage-floor",
  "observed_dirty": 1,
  "observed_head": "78a8e9fc2144623311e315fcc4e46c2831b0b2c1",
  "owner": "ar1312_coverage_worker",
  "plan": "../plans/AR-1312.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair the post-merge workspace coverage deficit without weakening the 90% floor.",
  "task_revision": 25,
  "title": "Post-merge workspace coverage floor repair",
  "updated_at": "2026-09-19T08:16:22+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1312-post-merge-coverage-floor"
}
---

# AR-1312: Post-merge workspace coverage floor repair

The AR-1310 implementation is merged, but required post-merge policy run
35393146183 failed at the existing workspace line-coverage floor: 89.99% at
merge commit 17a1530e620608a4d53b6d92ba48c642400778e2. This planned successor
must add meaningful tests for the uncovered paths and preserve the threshold.

- 2026-09-19T08:06:30+00:00: Dependency deadlock repaired by signed coordinator metadata revision.
  AR-1310 remains preserved as the merged implementation/evidence reference, but cannot be a hard
  prerequisite because its post-merge coverage failure is exactly the defect AR-1312 must repair.
  AR-1312 is now independent and remains subject to the unchanged 90% gate, exact-head CI, review,
  merge, and post-merge verification. No product or quality gate was weakened.

- 2026-09-19T08:06:48+00:00: Dependency deadlock corrected: independent coverage repair authorized;
  AR-1310 remains evidence, 90% floor unchanged.

- 2026-09-19T08:07:32+00:00: Claimed by ar1312_coverage_worker.

- 2026-09-19T08:08:14+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-09-19T08:08:34+00:00: Recorded command exit 0; command argv SHA-256
  6d7daaf3fa2b2dc1024fe94ff2ede47dd0833d1533a23e4d2f6e4e24d2e61efe.

- 2026-09-19T08:09:13+00:00: Recorded command exit 0; command argv SHA-256
  89e813dd5e87fb9fa61317b31519c167193e2ed92aae9afbb51338842792e20f.

- 2026-09-19T08:09:25+00:00: Recorded command exit 0; command argv SHA-256
  926389567d132c5fb6c96283f5498ee582d330de87cee2c36c7ced16ffb32d5a.

- 2026-09-19T08:09:52+00:00: Heartbeat by ar1312_coverage_worker.

- 2026-09-19T08:10:55+00:00: Recorded command exit 0; command argv SHA-256
  428457ea9cc6a21bd46c5be6651ba2faccb5b0b07ddc2fd6f96eca730dea5ab7.

- 2026-09-19T08:12:02+00:00: Recorded command exit 101; command argv SHA-256
  d33d9cb53d548745a8c3c0ee69405438b3271a287c7d7be0c8849c52919f6429.

- 2026-09-19T08:12:22+00:00: Recorded command exit 0; command argv SHA-256
  bf2f26579cb832a14ffb91a77e677429b2c16438251397559f808bb19112042a.

- 2026-09-19T08:13:54+00:00: Recorded command exit 2; command argv SHA-256
  39f5bf37659926d3938e4cdf34374f4888ec5484d09a3fb3d70311438a424134.

- 2026-09-19T08:14:17+00:00: Recorded command exit 0; command argv SHA-256
  bd4441f41964b199f749ae1a76207f14951f318de514790cde9d082946a018bc.

- 2026-09-19T08:14:42+00:00: Recorded exact failure: cargo llvm-cov --locked --workspace
  --all-targets --summary-only --fail-under-lines 90 exited 101 because capability_contract tests
  detected generated crates/asb-cli/default_*.profraw files. No gate or floor change.

- 2026-09-19T08:14:49+00:00: Recorded command exit 0; command argv SHA-256
  c24f010114290ca19c2736656870bcc6df571c0bd7e9626977009cda287f837f.

- 2026-09-19T08:15:23+00:00: Recorded command exit 101; command argv SHA-256
  bebe50790cfd409aeecd081e27469feeff22ba0c42d18f547f896c530479f8b6.

- 2026-09-19T08:15:42+00:00: Recorded command exit 0; command argv SHA-256
  47b0c98f95bbd342b82c944e71cb49272c14eaf651373744429cab3f5db6c4d6.

- 2026-09-19T08:16:05+00:00: Recorded command exit 0; command argv SHA-256
  af57729e1d567d245c5c927c571997a153a4a5ca57d8d0313518c99258415e11.

- 2026-09-19T08:16:22+00:00: Recorded command exit 0; command argv SHA-256
  c24f010114290ca19c2736656870bcc6df571c0bd7e9626977009cda287f837f.
