---
{
  "branch": "feature/ar-1783-installed-workload-selection-and-execution",
  "checkpoint_commit": "4902eb0d316228c9e566a9ceacfa823613a3a9f7",
  "claim_expires": "2026-10-13T21:37:07+00:00",
  "depends_on": [
    "AR-1763",
    "AR-1764",
    "AR-1782"
  ],
  "id": "AR-1783",
  "next_action": "Do not duplicate AR-1835 control/bootstrap coverage. Preserve d87352ddb511c48b4be1bdbecdd26fb2cf6597a8 as the AR-1783 product checkpoint; after AR-1835 exact-head merge/reconciliation, rerun serialized coverage and accept only if the unchanged 90% floor passes.",
  "observed_branch": "feature/ar-1783-installed-workload-selection-and-execution",
  "observed_dirty": 0,
  "observed_head": "d87352ddb511c48b4be1bdbecdd26fb2cf6597a8",
  "owner": "ar1783-workload-selection-luna",
  "plan": "../plans/AR-1783-installed-workload-selection-and-execution.md",
  "priority": "P0",
  "retry_circuit": {
    "abandoned": [],
    "attempts": [
      {
        "failure": "EXIT",
        "identity": "sha256:e506d6880a64ed5d2d84732d257c1c2c1d606d0748f2a10711707809737ba9a2",
        "progress_digest": "sha256:91f3236fb2308e831080f5a2895e239eab36947398c76808d5f38b096fa60ae5",
        "recorded_at": "2026-10-13T19:37:22+00:00",
        "task_revision": 458,
        "window": 3
      }
    ],
    "hold": null,
    "recoveries": [],
    "reservations": [],
    "schema_version": 1
  },
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "environmental",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1783.json",
    "spec_revision": 2,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1783.json",
  "spec_revision": 2,
  "status": "in_progress",
  "summary": "AR-1835 exact-head fixture now covers the authenticated runtime bootstrap/control seam; AR-1783 remains below 90% until that reviewed change is integrated.",
  "task_revision": 462,
  "title": "Installed workload selection and execution",
  "updated_at": "2026-10-13T19:37:55+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1783-installed-workload-selection-and-execution"
}
---

Make generated project catalogs and run/sweep consume the dedicated `asb workload`
records. Selection validates the installed workload's exact catalog revision,
identity, digest, license/terms compatibility, preparation state, adapter
version, and resource/platform requirements. Execution binds this identity into
the plan/run/record/report/compare evidence and rejects ambient, stale, revoked,
missing, incompatible, or manually substituted workload directories before a run
starts. Cover every AR-1781 workload ID—including SWE-mini—through a fresh
project's install, selection, bounded run and sweep, report, and comparison
journey. Development runs may use a controlled local/development backend where
needed; lack of production authorization or hosted qualification must not block
the suite from this end-to-end path.

- 2026-10-12T20:41:51+00:00: Dependencies AR-1763, AR-1764, and AR-1782 are durably done with
  acceptance evidence; promote for implementation.

- 2026-10-12T20:41:59+00:00: Claimed by ar1783-workload-selection-luna.

- 2026-10-12T20:42:47+00:00: Recorded command exit 0; command argv SHA-256
  91c481d4f1a058d3265e9102b0531d1eefe09cb45e5c1807ecda5e8c8b6b67d5.

- 2026-10-12T20:43:05+00:00: Checkpointed source commit b8fc46907afd281781a49dbd04ccb0aa6337a850.

- 2026-10-12T20:45:12+00:00: Recorded command exit 0; command argv SHA-256
  15bdc813ad2750ae688262967a32a5f5e34493aa64ac096b88091db382829347.

- 2026-10-12T20:45:31+00:00: Recorded command exit 1; command argv SHA-256
  96bc6a20aef6507ede6669f72a95e8e5cd3421bc4c3c176c86eb6c223a216973.

- 2026-10-12T20:45:47+00:00: Recorded command exit 0; command argv SHA-256
  3420e48a388c9ec83c9b28479ca01cf94a2337d61d26e396b712930ea1461a88.

- 2026-10-12T20:45:58+00:00: Recorded command exit 1; command argv SHA-256
  5cffee7c0bfd57b65d9794c05064ec0d1631c677dbb8952d45330ba4d7cf4250.

- 2026-10-12T20:46:23+00:00: Recorded command exit 0; command argv SHA-256
  d6a4561800f8e79160f1f30891a3f07ef4351a4749925c2eb7c421e26b160fb0.

- 2026-10-12T20:46:32+00:00: Recorded command exit 0; command argv SHA-256
  3420e48a388c9ec83c9b28479ca01cf94a2337d61d26e396b712930ea1461a88.

- 2026-10-12T20:47:02+00:00: Recorded command exit 0; command argv SHA-256
  d6a4561800f8e79160f1f30891a3f07ef4351a4749925c2eb7c421e26b160fb0.

- 2026-10-12T20:47:27+00:00: Recorded command exit 0; command argv SHA-256
  fa8b5b71edf3200d321ee3c09e348eccd55c38732142f7ba47f3a35c7d1b1356.

- 2026-10-12T20:48:06+00:00: Recorded command exit 0; command argv SHA-256
  d89c43b28f2a6ac6fb83707b9e20e8397e336513c903c1ccec8e4ccc3ec5d7dc.

- 2026-10-12T20:48:24+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T20:48:27+00:00: Recorded command exit 0; command argv SHA-256
  c8aae51f164559c1c2734b310b508fd66c2e7b4e955a4544d735ff59c4a48832.

- 2026-10-12T20:49:03+00:00: Recorded command exit 0; command argv SHA-256
  3d4cc54827fa0ae5c402321266e4a8e9a84a69a17f7ff27b7a0f0c858d454784.

- 2026-10-12T20:49:19+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-12T20:49:40+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T20:50:02+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-10-12T20:50:13+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T20:51:15+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-10-12T20:51:25+00:00: Recorded command exit 0; command argv SHA-256
  a5e91d8a6e356ba88fd4835c765ebd2411c75eacaa60f98e203295ec257bd3a5.

- 2026-10-12T20:51:39+00:00: Recorded command exit 0; command argv SHA-256
  ce7d45fffe378f17b6453e4e851b9576b579444d490ac31ccb139f845c58245e.

- 2026-10-12T20:51:54+00:00: Recorded command exit 0; command argv SHA-256
  ef19043205064ea87bec66574bfe246191c9311bc8c404cd8e347d08fbdc44f0.

- 2026-10-12T20:52:53+00:00: Recorded command exit 0; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-10-12T20:53:14+00:00: Recorded command exit 0; command argv SHA-256
  b36d15881eb65027724bc584f1b04db05666cd79896b100806e528307c04b65c.

- 2026-10-12T20:54:03+00:00: Recorded command exit 0; command argv SHA-256
  b49a90ee600c1023cee9ee9f9e8a4f9a06c53eef8c48d3932d88e482126c7c01.

- 2026-10-12T20:54:13+00:00: Recorded command exit 0; command argv SHA-256
  fcd17480931a7c27121bea1a4b4cdf0263b22a8542f304a02b7fe3a5e06895df.

- 2026-10-12T20:54:21+00:00: Recorded command exit 0; command argv SHA-256
  77082438719f647bf8d69589a3ecd2c061d48b8f41f8951d6ce69934a4f9550f.

- 2026-10-12T20:54:36+00:00: Checkpointed source commit 60ec53268f51284b6e0d52d4d08080de2c4a70f9.

- 2026-10-12T20:55:34+00:00: Independent read-only review of PR #623 (AR-1686): exact head
  93d75e28a7580ffbd7dbf6e543f5989c6dbe2688 against b8fc46907afd281781a49dbd04ccb0aa6337a850; diff is
  2 files/62 insertions, git diff --check clean; commit SSH signature and DCO pass; receipt runner
  digest matches source, paired ASB/TUI heads are recorded, and no forbidden secret/private-path
  material was found. Verdict: no implementation defect found in the reviewed diff, but not
  merge-ready yet because required exact-head CI remains in progress and AR-1686 is still
  in_progress; recheck all required checks before merge. Receipt lacks a final newline (style-only
  observation).

- 2026-10-12T21:02:59+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T21:03:24+00:00: Recorded command exit 101; command argv SHA-256
  c8aae51f164559c1c2734b310b508fd66c2e7b4e955a4544d735ff59c4a48832.

- 2026-10-12T21:03:48+00:00: Recorded command exit 101; command argv SHA-256
  c8aae51f164559c1c2734b310b508fd66c2e7b4e955a4544d735ff59c4a48832.

- 2026-10-12T21:03:59+00:00: Recorded command exit 0; command argv SHA-256
  c8aae51f164559c1c2734b310b508fd66c2e7b4e955a4544d735ff59c4a48832.

- 2026-10-12T21:04:10+00:00: Recorded command exit 0; command argv SHA-256
  0ca500d01969eddb76c78415cf9bb0d0161afa9dee001b1e1e5192b0e2bac82f.

- 2026-10-12T21:04:18+00:00: Recorded command exit 0; command argv SHA-256
  2111be5240fe4e6cf926f478089ec83fc93a4f4d2c583611780516356ef070c0.

- 2026-10-12T21:07:27+00:00: Recorded command exit 0; command argv SHA-256
  428457ea9cc6a21bd46c5be6651ba2faccb5b0b07ddc2fd6f96eca730dea5ab7.

- 2026-10-12T21:07:49+00:00: Recorded command exit 0; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-10-12T21:07:54+00:00: Recorded command exit 0; command argv SHA-256
  c2e61a8cf32748be7d24820458d179b7640e90362a58b99bf690cdf7f6613ed1.

- 2026-10-12T21:08:37+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-12T21:08:55+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-10-12T21:09:45+00:00: Recorded command exit 0; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-10-12T21:10:00+00:00: Checkpointed source commit e0474221c5a95e7e091265738b4ba05938767a47.

- 2026-10-12T21:15:30+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T21:19:53+00:00: PR #624 exact head e0474221c5a95e7e091265738b4ba05938767a47 against
  base 74b391348fc5c1361034a14742f6afef747d72db; all required hosted checks are green. Merge remains
  gated on independent review evidence.

- 2026-10-12T21:22:31+00:00: Independent read-only review by ar1783-review-luna of PR #624 exact
  head e0474221c5a95e7e091265738b4ba05938767a47 against base
  74b391348fc5c1361034a14742f6afef747d72db. Diff is 4 files/320 insertions and git diff --check is
  clean. All five topic commits have valid Martin Beck SSH signatures under config/allowed_signers
  and matching Martin Beck DCO trailers; changed text contains no private
  paths/secrets/prompts/transcripts. gh reports all 13 status checks SUCCESS. BLOCKER:
  project_run.rs validate_workload_identity returns Ok when plan workload_id is absent from
  config.workloads, and the added test explicitly accepts not-installed. ProjectExecution::resolve
  validates only the configured selected workload; bind_plan then allows a manually edited plan to
  use an unregistered/built-in workload while an external workload is selected, contrary to the AR
  requirement to reject manually substituted/ambient identities before execution. Need fail-closed
  selection binding and negative test.

- 2026-10-12T21:24:25+00:00: Recorded command exit 0; command argv SHA-256
  c8aae51f164559c1c2734b310b508fd66c2e7b4e955a4544d735ff59c4a48832.

- 2026-10-12T21:24:35+00:00: Recorded command exit 0; command argv SHA-256
  0ca500d01969eddb76c78415cf9bb0d0161afa9dee001b1e1e5192b0e2bac82f.

- 2026-10-12T21:24:58+00:00: Recorded command exit 0; command argv SHA-256
  d89c43b28f2a6ac6fb83707b9e20e8397e336513c903c1ccec8e4ccc3ec5d7dc.

- 2026-10-12T21:25:41+00:00: Recorded command exit 0; command argv SHA-256
  479cee35f596f58876fc7055fd99e64825a1a57e7a1cb7a32506c4754f4b2304.

- 2026-10-12T21:26:16+00:00: Recorded command exit 0; command argv SHA-256
  1c370d6074b72b12c0e0b562e318d930b3628a08d86c31227c66578bebec7737.

- 2026-10-12T21:26:33+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-12T21:26:49+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-10-12T21:27:14+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-10-12T21:27:34+00:00: Recorded command exit 0; command argv SHA-256
  c8aae51f164559c1c2734b310b508fd66c2e7b4e955a4544d735ff59c4a48832.

- 2026-10-12T21:28:21+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-10-12T21:29:15+00:00: Independent read-only review of PR #624 head
  dad6dd8c06a3d126db62abbc73585ae389aec56d against base 74b391348fc5c1361034a14742f6afef747d72db:
  SSH signature and DCO pass; project_run tests 4/4 pass; diff-check clean. BLOCKER: validation only
  checks installed receipt/prepared directory (project_run.rs:171-270), while run_attempt still
  calls built-in prepare_workload(&plan.workload, ...) (lib.rs:10297-10300), and load_and_validate
  still calls describe_workload(&plan.workload) (lib.rs:8404-8413). Thus external installed workload
  is not consumed end-to-end and prepared content is not integrity-bound; acceptance exact
  project-local execution/substitution rejection is unmet. Required exact-head CI not independently
  green/merge-ready.

- 2026-10-12T21:29:46+00:00: Review repair is dependency-safe: implementation branch contains
  fail-closed validation; resume to add diagnostic identity mappings and rerun gates.

- 2026-10-12T21:29:50+00:00: Claimed by ar1783-workload-selection-luna.

- 2026-10-12T21:29:55+00:00: Recorded command exit 101; command argv SHA-256
  d32df0a8f7802e39b9a6743613fff16ac35e4dddba3905aa783a204f77a7e43f.

- 2026-10-12T21:30:18+00:00: Recorded command exit 0; command argv SHA-256
  7a171fe19b6d670019acee3652bcfd90b32baf0f0440f80f4a1204c6de8939e5.

- 2026-10-12T21:31:18+00:00: Recorded command exit 0; command argv SHA-256
  bcce9a7b4de1b97de01a8867a3dd2ffecede717b9a6f675c6e38793c483742fc.

- 2026-10-12T21:32:31+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-12T21:32:35+00:00: Recorded command exit 1; command argv SHA-256
  8ab3067024628d467277120aa301a690ffb6b3665565e7f59ac557a62fa11f00.

- 2026-10-12T21:33:02+00:00: Recorded command exit 0; command argv SHA-256
  7a171fe19b6d670019acee3652bcfd90b32baf0f0440f80f4a1204c6de8939e5.

- 2026-10-12T21:33:07+00:00: Recorded command exit 1; command argv SHA-256
  8ae66ac6337b702f4a8145c24c2df94ddf7c087fd54be25c38aa279187a756da.

- 2026-10-12T21:33:31+00:00: Recorded command exit 101; command argv SHA-256
  797e93acd653188e1550ffc7d6c824ac4b54d5b4841adbb02558798db33872c9.

- 2026-10-12T21:34:02+00:00: Recorded command exit 101; command argv SHA-256
  797e93acd653188e1550ffc7d6c824ac4b54d5b4841adbb02558798db33872c9.

- 2026-10-12T21:34:28+00:00: Recorded command exit 0; command argv SHA-256
  797e93acd653188e1550ffc7d6c824ac4b54d5b4841adbb02558798db33872c9.

- 2026-10-12T21:34:56+00:00: Recorded command exit 0; command argv SHA-256
  e020366c6bbbf55dce62502aa71dd6be3f33097e363bf7714ce98a30596a2207.

- 2026-10-12T21:36:00+00:00: Recorded command exit 101; command argv SHA-256
  bcce9a7b4de1b97de01a8867a3dd2ffecede717b9a6f675c6e38793c483742fc.

- 2026-10-12T21:36:24+00:00: Recorded command exit 0; command argv SHA-256
  b61714ad2b515f73d2b106805bcaac612496dadb8b14b7af894dbb0c1b53784e.

- 2026-10-12T21:36:51+00:00: Recorded command exit 0; command argv SHA-256
  7a171fe19b6d670019acee3652bcfd90b32baf0f0440f80f4a1204c6de8939e5.

- 2026-10-12T21:37:28+00:00: Recorded command exit 0; command argv SHA-256
  fef7ff1571554c58c205e99cdc8d9446c4297c4390a18d3a568eba3dcb3a5b96.

- 2026-10-12T21:39:26+00:00: Recorded command exit 1; command argv SHA-256
  f39eb18490a270c05647dfa9f4c4e7ce1c6d36286bad4f3614cf7c33698a7dba.

- 2026-10-12T21:39:56+00:00: Recorded command exit 0; command argv SHA-256
  797e93acd653188e1550ffc7d6c824ac4b54d5b4841adbb02558798db33872c9.

- 2026-10-12T21:44:10+00:00: Recorded command exit 0; command argv SHA-256
  f92bf6471a6d7c67009de95a487a784d5d4c4adb75b1b06fe24b42ee5cd4f306.

- 2026-10-12T21:44:19+00:00: Recorded command exit 0; command argv SHA-256
  fa8b3a9b3155dfb14dce38a5fa2713e0d88ac24fd74f56936f5a0d172d73fd0f.

- 2026-10-12T21:44:23+00:00: Recorded command exit 0; command argv SHA-256
  fa8b3a9b3155dfb14dce38a5fa2713e0d88ac24fd74f56936f5a0d172d73fd0f.

- 2026-10-12T21:44:32+00:00: Recorded command exit 1; command argv SHA-256
  71f6a49ec8805901790215fdbb7168c494f65cc90c8f7c945dedfc999335141c.

- 2026-10-12T21:44:46+00:00: Recorded command exit 0; command argv SHA-256
  e3aa8fc3a1f52ff212f69a701dedf95ead9bf7c3d938cc6cbe174b741f1aee20.

- 2026-10-12T21:45:52+00:00: Recorded command exit 0; command argv SHA-256
  c872a14396c551e2ca87aea4ce6334ff33807e22d4bd45484db31310eb4789a7.

- 2026-10-12T21:46:11+00:00: Recorded command exit 0; command argv SHA-256
  699f27d06fd6ee26abec6d29a8bd81d8b21f2a07d65cb76848e9cc0fe5b257d7.

- 2026-10-12T21:46:43+00:00: Recorded command exit 0; command argv SHA-256
  797e93acd653188e1550ffc7d6c824ac4b54d5b4841adbb02558798db33872c9.

- 2026-10-12T21:47:07+00:00: Recorded command exit 0; command argv SHA-256
  e3aa8fc3a1f52ff212f69a701dedf95ead9bf7c3d938cc6cbe174b741f1aee20.

- 2026-10-12T21:48:52+00:00: Recorded command exit 0; command argv SHA-256
  bcce9a7b4de1b97de01a8867a3dd2ffecede717b9a6f675c6e38793c483742fc.

- 2026-10-12T21:49:18+00:00: Recorded command exit 0; command argv SHA-256
  f92bf6471a6d7c67009de95a487a784d5d4c4adb75b1b06fe24b42ee5cd4f306.

- 2026-10-12T21:50:32+00:00: Checkpoint: repaired fail-closed project workload binding and
  end-to-end installed workload execution, including record/schema/adapter checks and archive digest
  recomputation. Branch is clean at signed DCO head 4b72fafb37a0eaff47dfda757ee6a9114b75ffb8,
  rebased onto main 356a669e0c6ebbb6cd3675a119cba16fea486283 and pushed to PR #624. Focused tests,
  full workspace cargo test (458 CLI tests plus workspace), fmt, and clippy passed. Coverage rerun
  remains required for final qualification; do not merge until exact-head CI and independent review
  are green.

- 2026-10-12T21:55:22+00:00: Recorded command exit 1; command argv SHA-256
  332efed1c462fae62d8ccada7a29bf10ef00b07b096b7a9231517da174404cab.

- 2026-10-12T21:55:47+00:00: Recorded command exit 0; command argv SHA-256
  a42047c7df8cf4db3c4d48ad7a2fab2477177e8489ca09bfe40b57f2dbe1475d.

- 2026-10-12T21:57:40+00:00: Recorded command exit 0; command argv SHA-256
  e61f9d3beb1ca5641341fcbf3eb64bbd6f2035831028208eafe31c5cd951748e.

- 2026-10-12T21:57:52+00:00: Recorded command exit 1; command argv SHA-256
  5293fd837ebe782e43c7148bfb5782df5bcaef86ad9696624b758f8ec270c275.

- 2026-10-12T21:57:56+00:00: Recorded command exit 0; command argv SHA-256
  fa5f9d69ecacbba56301404d6d90a013078c2c5d12da58d09bca2dffcaf75983.

- 2026-10-12T21:58:12+00:00: Recorded command exit 0; command argv SHA-256
  0bd9bff7dffe484fe4b8432c4f1544b887400c963364a952b9000a38291cf28b.

- 2026-10-12T21:58:52+00:00: Recorded command exit 1; command argv SHA-256
  8ab3067024628d467277120aa301a690ffb6b3665565e7f59ac557a62fa11f00.

- 2026-10-12T21:59:07+00:00: Recorded command exit 0; command argv SHA-256
  f14a8d7c55fe7fbad25ab881daab3d9aed1cb5ee70a744dfe7d02bfda6440534.

- 2026-10-12T22:00:55+00:00: Recovered expired claim formerly owned by
  ar1783-workload-selection-luna. Lease expired during bounded workspace coverage run; recovering
  the same owner to preserve repair work. Coverage reached 88.85% lines after installed-workload
  tests, still below 90% floor; generated profraw will be cleaned and repair continues.

- 2026-10-12T22:00:59+00:00: Claimed by ar1783-workload-selection-luna.

- 2026-10-12T22:01:04+00:00: Recorded command exit 0; command argv SHA-256
  0bd9bff7dffe484fe4b8432c4f1544b887400c963364a952b9000a38291cf28b.

- 2026-10-12T22:01:13+00:00: Recorded command exit 0; command argv SHA-256
  0bd980248a368dc469eec8f9d4b0d8b9053515d297a53e2fc6224caed4b6f45c.

- 2026-10-12T22:01:20+00:00: Recorded command exit 0; command argv SHA-256
  aae918dc56292fd537e53271d05d0e5e6f688c34fd46e8afa057df2b8fc2d450.

- 2026-10-12T22:01:30+00:00: Recorded command exit 0; command argv SHA-256
  8ab3067024628d467277120aa301a690ffb6b3665565e7f59ac557a62fa11f00.

- 2026-10-12T22:01:39+00:00: Recorded command exit 0; command argv SHA-256
  f14a8d7c55fe7fbad25ab881daab3d9aed1cb5ee70a744dfe7d02bfda6440534.

- 2026-10-12T22:01:50+00:00: Recorded command exit 0; command argv SHA-256
  b3d00ffc79d5956edc9fb3b323c005128b35a9d78b32003296a54525894e5df6.

- 2026-10-12T22:02:02+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T22:02:09+00:00: Coverage repair checkpoint: added positive/negative installed-workload
  boundary tests for unsafe roots, tampered ownership, missing owner, file/object bounds, and
  PreparedWorkloadChoice dispatch. Focused package tests and fmt passed. Local workspace llvm-cov
  improved from 88.82% to 88.85% lines but remains below the unchanged 90% floor, so this is not yet
  a passing coverage gate. Signed DCO commit f52131bc971fefa25eb08eec087cad6bcb3b88e6 pushed to PR
  #624; generated profraw removed through handoffctl.

- 2026-10-12T22:04:23+00:00: Recorded command exit 0; command argv SHA-256
  4ae223987b8219093826529fac63e727266e64bbfd4ac65ff73cfd72b944f761.

- 2026-10-12T22:04:36+00:00: Recorded command exit 0; command argv SHA-256
  8ab3067024628d467277120aa301a690ffb6b3665565e7f59ac557a62fa11f00.

- 2026-10-12T22:04:47+00:00: Recorded command exit 0; command argv SHA-256
  cdf6858c9e7234aa01a9f1fe5bf4d8c1b9d4c083f6fe72ecb19a4a2ed741ad5b.

- 2026-10-12T22:04:55+00:00: Recorded command exit 0; command argv SHA-256
  90756ce10e768f3822defffa8861b99ac562e8ca0242bb45a8370132e98a34bd.

- 2026-10-12T22:05:10+00:00: Recorded command exit 101; command argv SHA-256
  d84c0f89dadafdc930a05730874b73a63147c983a84d01ea2b4277a8ea8bcfec.

- 2026-10-12T22:05:27+00:00: Recorded command exit 0; command argv SHA-256
  d84c0f89dadafdc930a05730874b73a63147c983a84d01ea2b4277a8ea8bcfec.

- 2026-10-12T22:05:30+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T22:05:39+00:00: Recorded command exit 1; command argv SHA-256
  8ab3067024628d467277120aa301a690ffb6b3665565e7f59ac557a62fa11f00.

- 2026-10-12T22:05:56+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T22:06:07+00:00: Recorded command exit 0; command argv SHA-256
  cdf6858c9e7234aa01a9f1fe5bf4d8c1b9d4c083f6fe72ecb19a4a2ed741ad5b.

- 2026-10-12T22:06:14+00:00: Recorded command exit 0; command argv SHA-256
  c3d9a24f39cde40b67f59028a2a3a55d70cd0b3ab1d60b366b36cbd35b963234.

- 2026-10-12T22:06:22+00:00: Recorded command exit 0; command argv SHA-256
  0bd9bff7dffe484fe4b8432c4f1544b887400c963364a952b9000a38291cf28b.

- 2026-10-12T22:06:33+00:00: Recorded command exit 0; command argv SHA-256
  b3d00ffc79d5956edc9fb3b323c005128b35a9d78b32003296a54525894e5df6.

- 2026-10-12T22:06:48+00:00: Coverage repair batch pushed: signed DCO commits 78dba6fd and d46a9dee
  add end-to-end installed run_attempt success plus installed source missing/escaping/preparation
  rejection coverage. Focused tests and formatting pass; branch clean and generated profraw removed
  through handoffctl. Full workspace coverage is next gate; prior result was 88.85%, below the hard
  90% floor.

- 2026-10-12T22:08:15+00:00: Recorded command exit 101; command argv SHA-256
  e61f9d3beb1ca5641341fcbf3eb64bbd6f2035831028208eafe31c5cd951748e.

- 2026-10-12T22:08:33+00:00: Recorded command exit 0; command argv SHA-256
  1ea9c554525c377525cb395946fcb6f0fbfa813f7cb172b8b0789fbcc73c38d2.

- 2026-10-12T22:08:42+00:00: Recorded command exit 0; command argv SHA-256
  e7a227184db71e87b92664e97f614287cdf72bf087ef3722af29bba69e633da6.

- 2026-10-12T22:10:04+00:00: Recorded command exit 0; command argv SHA-256
  e61f9d3beb1ca5641341fcbf3eb64bbd6f2035831028208eafe31c5cd951748e.

- 2026-10-12T22:10:17+00:00: Recorded command exit 0; command argv SHA-256
  0bd9bff7dffe484fe4b8432c4f1544b887400c963364a952b9000a38291cf28b.

- 2026-10-12T22:10:29+00:00: Recorded command exit 0; command argv SHA-256
  b3d00ffc79d5956edc9fb3b323c005128b35a9d78b32003296a54525894e5df6.

- 2026-10-12T22:10:42+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T22:10:47+00:00: Full workspace llvm-cov completed all tests (460 CLI tests plus
  workspace) but failed unchanged 90% line floor: 88.88% lines, 84.63% functions, 90.27% regions.
  This is a genuine gate failure despite installed workload success/source negative coverage.
  Provenance digest was refreshed and signed head 280b39de pushed to PR #624. Generated profraw
  artifacts removed through handoffctl; branch clean.

- 2026-10-12T22:11:24+00:00: Recorded command exit 0; command argv SHA-256
  76bea8d1f2fc78aa9f7ab9c51ae71a986073970b4713a9319ad9cc83de308c9a.

- 2026-10-12T22:11:38+00:00: Recorded command exit 1; command argv SHA-256
  8ab3067024628d467277120aa301a690ffb6b3665565e7f59ac557a62fa11f00.

- 2026-10-12T22:11:49+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T22:11:58+00:00: Recorded command exit 0; command argv SHA-256
  7cec78d3e28752faa02e03923a6e53b6b7a3794cfe12e3b74ce42c844403abf8.

- 2026-10-12T22:12:05+00:00: Recorded command exit 0; command argv SHA-256
  200b71cca781d167a90781c014e935d34c551be6edb350eb6441ee5d7a3651fc.

- 2026-10-12T22:13:36+00:00: Recorded command exit 0; command argv SHA-256
  e61f9d3beb1ca5641341fcbf3eb64bbd6f2035831028208eafe31c5cd951748e.

- 2026-10-12T22:13:50+00:00: Recorded command exit 0; command argv SHA-256
  0bd9bff7dffe484fe4b8432c4f1544b887400c963364a952b9000a38291cf28b.

- 2026-10-12T22:14:03+00:00: Recorded command exit 0; command argv SHA-256
  b3d00ffc79d5956edc9fb3b323c005128b35a9d78b32003296a54525894e5df6.

- 2026-10-12T22:14:15+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T22:14:20+00:00: Coverage batch adds source-builder compile/publish, failed-build,
  ambiguous-output, stable-failure-code tests in addition to installed workload run/source tests.
  Full workspace tests completed; llvm-cov result 89.04% lines, 84.70% functions, 90.41% regions.
  Generated profraw removed through handoffctl; clean signed head 32f42827 pushed to PR #624. This
  remains a genuine coverage blocker.

- 2026-10-12T22:14:27+00:00: Independent read-only audit of exact signed head
  280b39de1dcf85478a8f64ebdd217aa0df2672e6. Full serialized cargo llvm-cov --locked --workspace
  --all-targets completed all tests; aggregate report is 88.89% regions (17,473 missed of 157,286),
  90.28% lines, 84.63% functions, so the repository quality floor records a genuine 90% gate deficit
  despite installed-workload tests. New installed-workload behavior is exercised: project_run.rs
  86.46% lines; asb-workloads/src/lib.rs 96.42% lines. Remaining AR-specific uncovered behavior
  seams include project_run.rs validate_workload_identity missing project-root/config load, escaping
  path, non-directory/symlink prepared/archive, unreadable archive, digest mismatch, and missing
  receipt branches; lib.rs installed_workload_source missing
  root/config/record/non-external/escape/preparation branches plus InstalledPreparedWorkload copy
  failure mapping. These add only a small amount. To cross the unchanged floor without exclusions,
  target behavior-driven public seams with the largest baseline gaps: asb-cli/src/lib.rs (85.97%
  lines; 3,128 missed regions) for public run/sweep/setup/replay/diagnostic routes and failure
  outcomes; asb-cli/src/control.rs (88.21% lines; 1,860 missed regions) for durable
  lifecycle/authority/capture failure transitions; asb-cli/src/tui.rs (83.50% lines; 2,160 missed
  regions) for wizard/broker lifecycle negative journeys; then asb-runtime launch_factory/sandbox
  and asb-agents provider/auth boundaries. Do not approve or merge while the hard coverage gate is
  red.

- 2026-10-12T22:14:49+00:00: Recorded command exit 101; command argv SHA-256
  76bea8d1f2fc78aa9f7ab9c51ae71a986073970b4713a9319ad9cc83de308c9a.

- 2026-10-12T22:15:17+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T22:15:27+00:00: Recorded command exit 0; command argv SHA-256
  76bea8d1f2fc78aa9f7ab9c51ae71a986073970b4713a9319ad9cc83de308c9a.

- 2026-10-12T22:15:39+00:00: Recorded command exit 1; command argv SHA-256
  8ab3067024628d467277120aa301a690ffb6b3665565e7f59ac557a62fa11f00.

- 2026-10-12T22:15:51+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T22:16:11+00:00: Recorded command exit 0; command argv SHA-256
  7cec78d3e28752faa02e03923a6e53b6b7a3794cfe12e3b74ce42c844403abf8.

- 2026-10-12T22:16:36+00:00: Recorded command exit 0; command argv SHA-256
  57e481616da2e954fe2c522540db85efbf1ec5d882fd9e696446690771286f24.

- 2026-10-12T22:17:52+00:00: Dependency-safe PR audit found PR #624 remote head
  32f42827367dbfedcb21304e80234336445ab683 differs from observed state head c2f3759f9962; current
  durable evidence records 89.04% lines and a genuine hard coverage-gate deficit. No merge
  authorization.

- 2026-10-12T22:18:36+00:00: Recorded command exit 0; command argv SHA-256
  e61f9d3beb1ca5641341fcbf3eb64bbd6f2035831028208eafe31c5cd951748e.

- 2026-10-12T22:18:46+00:00: Recorded command exit 0; command argv SHA-256
  0bd9bff7dffe484fe4b8432c4f1544b887400c963364a952b9000a38291cf28b.

- 2026-10-12T22:18:58+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T22:19:08+00:00: Full workspace llvm-cov completed 464 CLI tests and workspace suites.
  Latest result: 89.05% lines, 84.71% functions, 90.43% regions, hard 90% line floor still fails.
  Source-builder preflight negative tests pass; generated profraw removed through handoffctl. New
  signed product commit c2f3759f is local only and not pushed because coverage is not qualifying.

- 2026-10-12T22:19:40+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T22:19:48+00:00: Recorded command exit 101; command argv SHA-256
  271113781cc5be8e8a2160bd41e97aca82a07f164bb84ce885b3336c61975e2c.

- 2026-10-12T22:20:13+00:00: Recorded command exit 101; command argv SHA-256
  b4f3fe410552c10d5c9045c448bd9f3142cdff89e43064d7fad731f5b270b04b.

- 2026-10-12T22:20:22+00:00: Recorded command exit 0; command argv SHA-256
  b4f3fe410552c10d5c9045c448bd9f3142cdff89e43064d7fad731f5b270b04b.

- 2026-10-12T22:20:31+00:00: Recorded command exit 0; command argv SHA-256
  a67cc126738b65de5daa299ffa5f436afdb087680cbcb27352e00dd23363ec85.

- 2026-10-12T22:20:36+00:00: Recorded command exit 1; command argv SHA-256
  8ab3067024628d467277120aa301a690ffb6b3665565e7f59ac557a62fa11f00.

- 2026-10-12T22:20:43+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T22:21:04+00:00: Recorded command exit 1; command argv SHA-256
  8ab3067024628d467277120aa301a690ffb6b3665565e7f59ac557a62fa11f00.

- 2026-10-12T22:21:14+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T22:21:26+00:00: Recorded command exit 1; command argv SHA-256
  8499a5275f7f8914dfb36bfcf3b1e1d6e9c418d5d06d07caa7180b20e396d736.

- 2026-10-12T22:21:39+00:00: Recorded command exit 0; command argv SHA-256
  e774070ed47b8b4d482195d8b1d99c3f5917c058c0db71c81099e4073212cc88.

- 2026-10-12T22:21:48+00:00: Recorded command exit 0; command argv SHA-256
  856041d6364daafac03e6dea99f3718964ed9ed63a166cfd5b70b86d831bc589.

- 2026-10-12T22:21:57+00:00: Recorded command exit 0; command argv SHA-256
  45ca30b6d20fee5877cea3a87e949f34e4c5bdbc904fcf0e9c5afae3685992a6.

- 2026-10-12T22:22:04+00:00: Recorded command exit 0; command argv SHA-256
  a610666abff1c28ba2e509ed9ed74bf758577161e7e609f88d51aa0c371529ce.

- 2026-10-12T22:23:20+00:00: Recorded command exit 101; command argv SHA-256
  e61f9d3beb1ca5641341fcbf3eb64bbd6f2035831028208eafe31c5cd951748e.

- 2026-10-12T22:23:25+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T22:23:52+00:00: Recorded command exit 0; command argv SHA-256
  5a1a01cebecc8d6f8ffd690cf3f00a65fe9a114daae16edb806547898c37b926.

- 2026-10-12T22:24:21+00:00: Recorded command exit 0; command argv SHA-256
  63a234eae117a6b91114d670288356c269d58f3720b8b34ed63aa491aa873c4a.

- 2026-10-12T22:24:31+00:00: Recorded command exit 0; command argv SHA-256
  adc26d95075a188f8d76eb784e907811e2f9f8d1af1445130845d5ffc2a00c9b.

- 2026-10-12T22:25:13+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T22:26:48+00:00: Recorded command exit 0; command argv SHA-256
  e61f9d3beb1ca5641341fcbf3eb64bbd6f2035831028208eafe31c5cd951748e.

- 2026-10-12T22:26:58+00:00: Recorded command exit 1; command argv SHA-256
  120cec179feab07f4868f83ec4a3af8dfaba17df4ab6fa2feef85a40c9b8cf89.

- 2026-10-12T22:27:09+00:00: Recorded command exit 0; command argv SHA-256
  2789ac8386194e35eaa534ffdc8e1ad90e962bc992d1cd27fc7f3f65eb2d0458.

- 2026-10-12T22:27:22+00:00: Recorded command exit 0; command argv SHA-256
  80ca5428992be15b15ccff44645a59ab40fad43ae4cc0e46b9943c576349df7e.

- 2026-10-12T22:27:36+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T22:27:43+00:00: Checkpoint: commits 9315abdd (control artifact tests), d0d3674c
  (diagnostic identity refresh), c2f3759f source-builder preflight are local and signed/DCO. Focused
  control and diagnostic-contract tests pass. Full workspace llvm-cov completed all tests but
  reports 89.07% lines (104306/121? total report: 157541 lines, 17218 missed), 84.72% functions,
  90.45% regions; no push/review/merge attempted. Generated profraw cleaned after run. Failure from
  prior run was stale diagnostic catalog identities; repaired and focused test now green.

- 2026-10-12T22:28:09+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T22:28:20+00:00: Recorded command exit 0; command argv SHA-256
  d0d6a496a815d2406b57c29750f16d0dac2280b031da5d5a6e0dc27af4f66096.

- 2026-10-12T22:28:31+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T22:28:33+00:00: Recorded command exit 0; command argv SHA-256
  d4b0b843a013d941a33c6bb891f5036f5c4fd1725ae5ca2ab487ff247011c8fd.

- 2026-10-12T22:28:39+00:00: Recorded command exit 0; command argv SHA-256
  62a2e3746f15fbc07e488b62e2dbdac4cc8e68409e625447d93ed1efa76038c1.

- 2026-10-12T22:30:35+00:00: Recorded command exit 0; command argv SHA-256
  e61f9d3beb1ca5641341fcbf3eb64bbd6f2035831028208eafe31c5cd951748e.

- 2026-10-12T22:30:47+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T22:30:54+00:00: Latest bounded batch commit 6490d4df7f85b15b02fe15aa6a5c442c34905125 is
  SSH-signed (G) and DCO-trailered. New TUI status identity/routing/terminal-value tests pass. Full
  workspace run completed 467 CLI tests and all suites; exact total 89.08% lines (104339 covered of
  121? report total 157589 with 17213 missed), 84.73% functions, 90.46% regions. Generated profraw
  removed; branch clean. No push/review/merge until floor is met.

- 2026-10-12T22:31:01+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T22:31:40+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T22:31:52+00:00: Recorded command exit 0; command argv SHA-256
  442a9bd6d6159be981d083d96c2b7d4adcb72ca1a5cf7b5fad475c4afda8510c.

- 2026-10-12T22:32:05+00:00: Recorded command exit 0; command argv SHA-256
  ec33d80a5a0c1c5f4195f645ae49822bb7daca329ee8c788738a14e8117cc171.

- 2026-10-12T22:32:12+00:00: Recorded command exit 0; command argv SHA-256
  c082b27b00848ec679355b840bac1b8cb883010f8feb36a4f4f52ecfe1e7f01c.

- 2026-10-12T22:32:45+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T22:33:49+00:00: Recorded command exit 0; command argv SHA-256
  e61f9d3beb1ca5641341fcbf3eb64bbd6f2035831028208eafe31c5cd951748e.

- 2026-10-12T22:34:01+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T22:34:08+00:00: Exact local head c92ea3cdfbac32edb84062d238b54e3cdad3b108 is SSH-signed
  (G) with DCO. Added project setup/layout validation tests covering missing/file/outside/symlink
  roots; focused test passes. Full workspace llvm-cov completed all suites: 89.10% lines (104363
  covered, 9935 missed of 157645), 84.76% functions, 90.48% regions. Generated profraw removed.
  Worktree clean; no push/review/merge.

- 2026-10-12T22:34:33+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T22:34:41+00:00: Recorded command exit 0; command argv SHA-256
  30a33dbd4b9c5228da76d62f7ebfe20b73b63196f031a5edc3c02f9b215554d8.

- 2026-10-12T22:34:50+00:00: Recorded command exit 0; command argv SHA-256
  4c8c3bae40eda2cd9049cc04b9ebd81a215cd7510f01ea90b42e57bc3e11059e.

- 2026-10-12T22:34:58+00:00: Recorded command exit 0; command argv SHA-256
  a8744db3be929908232d8018c8152ac558405fc8a3fefae2098576c41edc471e.

- 2026-10-12T22:36:13+00:00: Recorded command exit 101; command argv SHA-256
  e61f9d3beb1ca5641341fcbf3eb64bbd6f2035831028208eafe31c5cd951748e.

- 2026-10-12T22:37:07+00:00: Recorded command exit 0; command argv SHA-256
  73c7d0dd14a9bfbe756e42df0cf611291c3209d4e7af71a43dd375d6895e8c6a.

- 2026-10-12T22:37:49+00:00: Recorded command exit 101; command argv SHA-256
  eae454637d710aee0249d959d55da04577299675647f8325c267571f71a884a3.

- 2026-10-12T22:39:18+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T22:40:07+00:00: Recorded command exit 0; command argv SHA-256
  b48802db5d60864fea266a175aab6561f162cad0de4217481cf349d287ea912d.

- 2026-10-12T22:41:17+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T22:41:25+00:00: Latest signed/DCO local commit 6dbe4066 adds safe_fs invalid-name,
  existing-entry, write-new collision, and absolute-path boundary tests; focused test passes. Full
  workspace llvm-cov with RUST_TEST_THREADS=1 completed all suites and reports 89.10% lines (104386
  covered, 9936 missed of 157712), 84.78% functions, 90.48% regions. An earlier parallel run exited
  101 without a durable failure diagnostic; deterministic single-thread rerun completed with
  coverage result. Profraw removed and worktree clean. No push/review/merge.

- 2026-10-12T22:41:42+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T22:41:59+00:00: Recorded command exit 101; command argv SHA-256
  18d4a02a28f1f79ce864e9ea7e15934f164a9b1608e1a555daa17922c1af5941.

- 2026-10-12T22:42:11+00:00: Recorded command exit 101; command argv SHA-256
  18d4a02a28f1f79ce864e9ea7e15934f164a9b1608e1a555daa17922c1af5941.

- 2026-10-12T22:42:33+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T22:42:41+00:00: Recorded command exit 0; command argv SHA-256
  18d4a02a28f1f79ce864e9ea7e15934f164a9b1608e1a555daa17922c1af5941.

- 2026-10-12T22:42:52+00:00: Recorded command exit 0; command argv SHA-256
  5347a27d72ccf9123de3e6e55a44aa7f3fbca61806f07d3b647ac9a22afeb16d.

- 2026-10-12T22:42:59+00:00: Recorded command exit 0; command argv SHA-256
  60cdc8e68b31f9b2c24ccbcbeb68f1fdc9d7639a476d5f883ee01ba82d1e01ca.

- 2026-10-12T22:45:50+00:00: Recorded command exit 0; command argv SHA-256
  b48802db5d60864fea266a175aab6561f162cad0de4217481cf349d287ea912d.

- 2026-10-12T22:46:06+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T22:46:13+00:00: Latest signed/DCO local commit 1865585e adds runtime tests for
  canonical/private root validation and pinned-command digest mismatch. Focused runtime test passes.
  Serialized full workspace llvm-cov completed all suites and reports 89.11% lines (104410 covered,
  9930 missed of 157780), 84.78% functions, 90.49% regions; floor failure is solely below 90% line
  threshold. Profraw removed, worktree clean, no push/review/merge.

- 2026-10-12T22:46:37+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T22:46:46+00:00: Recorded command exit 0; command argv SHA-256
  5a747be35840f483c38d0b04d9b09fc1ced9bc7a3a24cb10f0c79e4e1953307c.

- 2026-10-12T22:46:56+00:00: Recorded command exit 0; command argv SHA-256
  a2aa508794155722dc3093ca13701def6e95aca3ce40cd97886638d3b062934d.

- 2026-10-12T22:47:03+00:00: Recorded command exit 0; command argv SHA-256
  ad350cfdd3ad441c4f9e48ea364ca36f7852e23d898f3486a07a1d09c6e64408.

- 2026-10-12T22:50:20+00:00: Recorded command exit 0; command argv SHA-256
  b48802db5d60864fea266a175aab6561f162cad0de4217481cf349d287ea912d.

- 2026-10-12T22:50:27+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T22:50:34+00:00: Latest signed/DCO local commit b0d076bc adds sandbox LLVM profile
  override and environment-key boundary coverage; focused test passes. Deterministic serialized full
  workspace llvm-cov completed all suites and reports 89.11% lines (104421 covered, 9927 missed of
  157803), 84.78% functions, 90.49% regions; floor remains unmet. Profraw removed, worktree clean,
  no push/review/merge.

- 2026-10-12T22:51:26+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T22:51:38+00:00: Recorded command exit 0; command argv SHA-256
  760906ecb72cabfa1c71711a248e8241f0842e9fd7d7188965c3ccc0c0f87c98.

- 2026-10-12T22:51:47+00:00: Recorded command exit 101; command argv SHA-256
  b73abb55fa7f9dc051adc063b94ee19431ce0fc80b16f2e8128676c71af61291.

- 2026-10-12T22:52:03+00:00: Recorded command exit 0; command argv SHA-256
  b73abb55fa7f9dc051adc063b94ee19431ce0fc80b16f2e8128676c71af61291.

- 2026-10-12T22:52:13+00:00: Recorded command exit 0; command argv SHA-256
  45ca30b6d20fee5877cea3a87e949f34e4c5bdbc904fcf0e9c5afae3685992a6.

- 2026-10-12T22:52:19+00:00: Recorded command exit 0; command argv SHA-256
  1b25f5db6a988688c6e468e88b42b965df5de5ba67702ef653dfba0523e06b87.

- 2026-10-12T22:54:20+00:00: Recorded command exit 101; command argv SHA-256
  b48802db5d60864fea266a175aab6561f162cad0de4217481cf349d287ea912d.

- 2026-10-12T22:54:29+00:00: Recorded command exit 101; command argv SHA-256
  797e93acd653188e1550ffc7d6c824ac4b54d5b4841adbb02558798db33872c9.

- 2026-10-12T22:54:51+00:00: Recorded command exit 0; command argv SHA-256
  797e93acd653188e1550ffc7d6c824ac4b54d5b4841adbb02558798db33872c9.

- 2026-10-12T22:55:02+00:00: Recorded command exit 0; command argv SHA-256
  63a234eae117a6b91114d670288356c269d58f3720b8b34ed63aa491aa873c4a.

- 2026-10-12T22:55:09+00:00: Recorded command exit 0; command argv SHA-256
  4ba29877df715a3e067b851b2f8c1ad5479f1f63e8fa4327549733dddab3ee6c.

- 2026-10-12T22:57:08+00:00: Recorded command exit 101; command argv SHA-256
  b48802db5d60864fea266a175aab6561f162cad0de4217481cf349d287ea912d.

- 2026-10-12T22:57:20+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T22:57:27+00:00: Latest signed/DCO product commits: 0d50540e (control state and endpoint
  tests), 410f08c1 (diagnostic identity refresh). Focused control and diagnostic-contract tests
  pass. Serialized full workspace llvm-cov completed suites; 89.11% lines (coverage gate remains
  nonzero because fixed 90% floor is unmet), 84.78% functions, 90.49% regions. Profraw removed,
  worktree clean, no push/review/merge.

- 2026-10-12T22:57:40+00:00: Recorded command exit 1; command argv SHA-256
  913192cfa7ce9d37612f68d8a89f5cc71682e1a6e3f77ebb736f0a51a283e7cf.

- 2026-10-12T22:58:01+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T22:58:13+00:00: Recorded command exit 0; command argv SHA-256
  84162f7809084dc164bf4e7cb112865bec2ee05e0b9a7b865ef64c0ac83030fb.

- 2026-10-12T22:58:24+00:00: Recorded command exit 0; command argv SHA-256
  d4b0b843a013d941a33c6bb891f5036f5c4fd1725ae5ca2ab487ff247011c8fd.

- 2026-10-12T22:58:34+00:00: Recorded command exit 0; command argv SHA-256
  e7febebd1db0e8162b43a5e11895c7ce17c78ac33e2f982ecdc57d00ee4f59b7.

- 2026-10-12T23:01:10+00:00: Recorded command exit 0; command argv SHA-256
  b48802db5d60864fea266a175aab6561f162cad0de4217481cf349d287ea912d.

- 2026-10-12T23:01:22+00:00: Recorded command exit 0; command argv SHA-256
  913192cfa7ce9d37612f68d8a89f5cc71682e1a6e3f77ebb736f0a51a283e7cf.

- 2026-10-12T23:01:44+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T23:02:19+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T23:02:28+00:00: Recorded command exit 0; command argv SHA-256
  1016167bf964fa6bd057312b03a3146e764d3ee4c531c8e906b873688057b839.

- 2026-10-12T23:02:38+00:00: Recorded command exit 0; command argv SHA-256
  d44b98afbbd64e32da19b691aa894d9a8bf4653cf63adbe66cf8bd1d024d8f90.

- 2026-10-12T23:02:47+00:00: Recorded command exit 0; command argv SHA-256
  839fb353c063a6c03cb5458f3c4cdde4d148454faf7fe2d1b233aa425a413494.

- 2026-10-12T23:05:44+00:00: Recorded command exit 0; command argv SHA-256
  b48802db5d60864fea266a175aab6561f162cad0de4217481cf349d287ea912d.

- 2026-10-12T23:05:57+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T23:06:04+00:00: Latest signed/DCO product commit e272b744 adds actual
  asb_loopback_supervisor argument, spawn, and supervise success/failure/deadline tests (no
  duplicated production parser). Focused binary tests pass. Serialized full workspace llvm-cov
  completed all suites: 89.19% lines (104496 covered, 9855 missed of 157982), 84.97% functions,
  90.57% regions. Profraw artifacts removed; worktree clean. No push/review/merge.

- 2026-10-12T23:07:06+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T23:07:14+00:00: Recorded command exit 101; command argv SHA-256
  2a994f4af435ddc208dc9a9073e933c656545d9b0077180abd9947455022da12.

- 2026-10-12T23:07:26+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T23:07:34+00:00: Recorded command exit 0; command argv SHA-256
  2a994f4af435ddc208dc9a9073e933c656545d9b0077180abd9947455022da12.

- 2026-10-12T23:07:45+00:00: Recorded command exit 0; command argv SHA-256
  6a9890c5734f8fd58583fc318375afc75e19ea8ecdd2eaa5997b08bd05988930.

- 2026-10-12T23:07:52+00:00: Recorded command exit 0; command argv SHA-256
  77d1e571ce68e80c9207f9ebe312f0a244d22cfd32de4d706443bc9510f69aff.

- 2026-10-12T23:10:21+00:00: Recorded command exit 0; command argv SHA-256
  b48802db5d60864fea266a175aab6561f162cad0de4217481cf349d287ea912d.

- 2026-10-12T23:10:33+00:00: Recorded command exit 0; command argv SHA-256
  21070f2de444d4c99f04c5185ce0e2ec530bfc3a1677ed3672239b6bccec64a5.

- 2026-10-12T23:11:10+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T23:11:18+00:00: bb291c71 is SSH-signed with DCO. Focused asb-runtime loopback_sidecar
  tests: 8 passed. Full serialized workspace suite passed; coverage gate failed only at fixed floor:
  104547/117? report total 158063 lines, 89.21%; 9828 missed, 85.01% functions, 90.60% regions.
  Generated profraw removed; worktree clean; no push/review/merge.

- 2026-10-12T23:11:30+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T23:11:39+00:00: Recorded command exit 1; command argv SHA-256
  c165e96b1cd24e9d5f392c4c8456327c6489ed3066d93a30ecece348948f8a9c.

- 2026-10-12T23:11:49+00:00: Recorded command exit 0; command argv SHA-256
  56eea118a4ea76bee946f16aa2336c202417a979849f394e1398442ff25aba13.

- 2026-10-12T23:11:56+00:00: Recorded command exit 0; command argv SHA-256
  79a477c5fe799635bac59f9fe0ba0927f3aba5d0a520aa43a00cd614edada03d.

- 2026-10-12T23:12:10+00:00: Recorded command exit 0; command argv SHA-256
  a2aa508794155722dc3093ca13701def6e95aca3ce40cd97886638d3b062934d.

- 2026-10-12T23:12:17+00:00: Recorded command exit 0; command argv SHA-256
  e07c2b551db232b517051f544329a8504df291b0393dfec469d6c67e7cd58ab6.

- 2026-10-12T23:15:28+00:00: Recorded command exit 0; command argv SHA-256
  b48802db5d60864fea266a175aab6561f162cad0de4217481cf349d287ea912d.

- 2026-10-12T23:15:40+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T23:15:46+00:00: Full serialized workspace tests passed; fixed 90% line floor is the
  sole failure. Exact report total 158107 lines, 104563 covered, 9822 missed; generated profraw
  removed; worktree clean; no push/review/merge.

- 2026-10-12T23:16:02+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T23:16:12+00:00: Recorded command exit 0; command argv SHA-256
  9c3df1eeb2b67a1d241d716b7bc1d1c37d21b92a3d4f4ba7854b96c909267d9c.

- 2026-10-12T23:16:22+00:00: Recorded command exit 0; command argv SHA-256
  5347a27d72ccf9123de3e6e55a44aa7f3fbca61806f07d3b647ac9a22afeb16d.

- 2026-10-12T23:16:30+00:00: Recorded command exit 0; command argv SHA-256
  9d89a2e439a85fa248537e7ac9e812bbcc4e0ed11e847981f2750bc4f2e91b57.

- 2026-10-12T23:16:42+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T23:16:49+00:00: Focused development_fixture_runs_owned_authority_without_native_tools
  passed. Latest report top missed clusters were launch_factory.rs (201 lines), sandbox.rs (197),
  live_service.rs (215); no unchanged coverage rerun. Worktree clean after signed commit; no
  push/review/merge below 90%.

- 2026-10-12T23:17:08+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T23:17:19+00:00: Recorded command exit 101; command argv SHA-256
  7dd9a655994a8c73db81396f006820ad848c503119fc08b6745018d6f817786e.

- 2026-10-12T23:17:32+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T23:17:40+00:00: Recorded command exit 0; command argv SHA-256
  7dd9a655994a8c73db81396f006820ad848c503119fc08b6745018d6f817786e.

- 2026-10-12T23:17:49+00:00: Recorded command exit 0; command argv SHA-256
  5347a27d72ccf9123de3e6e55a44aa7f3fbca61806f07d3b647ac9a22afeb16d.

- 2026-10-12T23:17:57+00:00: Recorded command exit 0; command argv SHA-256
  bb97be84dfe06e0d8c14525902b0cdbe8f7117534dbbbdbd45291ed1ec2b29d6.

- 2026-10-12T23:20:30+00:00: Recorded command exit 0; command argv SHA-256
  b48802db5d60864fea266a175aab6561f162cad0de4217481cf349d287ea912d.

- 2026-10-12T23:20:45+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T23:20:51+00:00: Focused live_factory_rejects_zero_nonce_and_namespace_substitution
  passed. Full serialized workspace tests passed; hard 90% line floor remains sole failure. Exact
  report total 158180 lines, 104595 covered, 9800 missed; generated profraw removed; worktree clean;
  no push/review/merge.

- 2026-10-12T23:21:13+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T23:21:22+00:00: Recorded command exit 101; command argv SHA-256
  6482a0402bc9e33d8d56da0d7c577641151456136acd37536658715d65746a25.

- 2026-10-12T23:21:34+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T23:21:42+00:00: Recorded command exit 0; command argv SHA-256
  6482a0402bc9e33d8d56da0d7c577641151456136acd37536658715d65746a25.

- 2026-10-12T23:21:53+00:00: Recorded command exit 0; command argv SHA-256
  5a3226f4ec6b2673edadf257299924b32159bdff258e218f369b52811eaea749.

- 2026-10-12T23:22:00+00:00: Recorded command exit 0; command argv SHA-256
  a3ac7de5d22913e4537b34962628c85158534d5ceee58207786feee60f7fb7c7.

- 2026-10-12T23:24:17+00:00: Recorded command exit 0; command argv SHA-256
  b48802db5d60864fea266a175aab6561f162cad0de4217481cf349d287ea912d.

- 2026-10-12T23:24:30+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T23:24:35+00:00: Focused local_mock_backend_defaults_and_public_identity_are_stable
  passed. Full serialized workspace suite passed; fixed 90% line floor remains sole failure. Exact
  report total 158220 lines, 104612 covered, 9790 missed; generated profraw removed; worktree clean;
  no push/review/merge.

- 2026-10-12T23:24:51+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T23:25:02+00:00: Recorded command exit 101; command argv SHA-256
  35da53039aa093d28c8c605010e94bd365ce078dae20283b89af24420c160778.

- 2026-10-12T23:25:17+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T23:25:25+00:00: Recorded command exit 0; command argv SHA-256
  35da53039aa093d28c8c605010e94bd365ce078dae20283b89af24420c160778.

- 2026-10-12T23:25:35+00:00: Recorded command exit 0; command argv SHA-256
  a2aa508794155722dc3093ca13701def6e95aca3ce40cd97886638d3b062934d.

- 2026-10-12T23:25:42+00:00: Recorded command exit 0; command argv SHA-256
  3071e0ca04336cd452769e17306a12c25c7424ca5696b5a217f439489cd6abac.

- 2026-10-12T23:28:02+00:00: Recorded command exit 0; command argv SHA-256
  b48802db5d60864fea266a175aab6561f162cad0de4217481cf349d287ea912d.

- 2026-10-12T23:28:15+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T23:28:21+00:00: Focused development_spawn_exposes_bounded_process_lifecycle_and_cleanup
  passed. Full serialized workspace tests passed; fixed 90% line floor remains sole failure. Exact
  report total 158276 lines, 104641 covered, 9771 missed; generated profraw removed; worktree clean;
  no push/review/merge.

- 2026-10-12T23:29:18+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T23:29:28+00:00: Recorded command exit 0; command argv SHA-256
  68c221e0653ef90cdf61da5334074863988c118a966aefdb5aededc54b34dc63.

- 2026-10-12T23:29:36+00:00: Recorded command exit 0; command argv SHA-256
  5a3226f4ec6b2673edadf257299924b32159bdff258e218f369b52811eaea749.

- 2026-10-12T23:29:43+00:00: Recorded command exit 0; command argv SHA-256
  e515f0421041b7476050792d0ce2640dac6b60427394d308a55ab100a6fa754d.

- 2026-10-12T23:32:41+00:00: Recorded command exit 0; command argv SHA-256
  b48802db5d60864fea266a175aab6561f162cad0de4217481cf349d287ea912d.

- 2026-10-12T23:32:52+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T23:32:57+00:00: Focused
  authority_resolver_persist_failure_is_typed_and_lifecycle_is_idempotent passed. Full serialized
  workspace tests passed; fixed 90% line floor remains sole failure. Exact report total 158336
  lines, 104671 covered, 9776 missed; generated profraw removed; worktree clean; no
  push/review/merge.

- 2026-10-12T23:33:18+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T23:33:28+00:00: Recorded command exit 101; command argv SHA-256
  6bb4e335a580aab66a692d538e9ea8728c11bbc39973b408a87122609acc035e.

- 2026-10-12T23:33:41+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T23:33:49+00:00: Recorded command exit 101; command argv SHA-256
  6bb4e335a580aab66a692d538e9ea8728c11bbc39973b408a87122609acc035e.

- 2026-10-12T23:36:33+00:00: Recorded command exit 0; command argv SHA-256
  b48802db5d60864fea266a175aab6561f162cad0de4217481cf349d287ea912d.

- 2026-10-12T23:36:43+00:00: Recorded command exit 0; command argv SHA-256
  421ce1b4471964250b3c71c8c954e2a67cb6f28d425c787eb3e7348c2d97d3f0.

- 2026-10-12T23:37:13+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T23:37:18+00:00: Bounded report pass after signed 94521496: exact total 158336 lines,
  104671 covered, 9774 missed. Dominant uncovered blocks: live_service 1854-1880, 1888-1927,
  1931-1970; sandbox 766-837; launch_factory 701-721 and 798-837. Focused prior test passed; full
  serialized suite passed; profraw removed; worktree clean; no publication below gate.

- 2026-10-12T23:38:11+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T23:38:20+00:00: Recorded command exit 101; command argv SHA-256
  23bfe013b1134f1849c245cd4c9fca19f9b321c8994c0a1cdf995caf36cdd44a.

- 2026-10-12T23:38:36+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T23:38:43+00:00: Recorded command exit 101; command argv SHA-256
  23bfe013b1134f1849c245cd4c9fca19f9b321c8994c0a1cdf995caf36cdd44a.

- 2026-10-12T23:38:55+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T23:39:03+00:00: Recorded command exit 101; command argv SHA-256
  23bfe013b1134f1849c245cd4c9fca19f9b321c8994c0a1cdf995caf36cdd44a.

- 2026-10-12T23:39:20+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T23:39:28+00:00: Recorded command exit 101; command argv SHA-256
  23bfe013b1134f1849c245cd4c9fca19f9b321c8994c0a1cdf995caf36cdd44a.

- 2026-10-12T23:39:41+00:00: Recorded command exit 0; command argv SHA-256
  f28e8da641834bffd14347e708a06c6b6a9645bc46edf5bdcc8b2be400eaefae.

- 2026-10-12T23:40:19+00:00: Recorded command exit 101; command argv SHA-256
  23bfe013b1134f1849c245cd4c9fca19f9b321c8994c0a1cdf995caf36cdd44a.

- 2026-10-12T23:41:06+00:00: Recorded command exit 101; command argv SHA-256
  760958eaafc6a50b2e4366ec95d254d4d33c1b9811e12427939e2ac4c7c1fdc0.

- 2026-10-12T23:41:21+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-12T23:41:27+00:00: No product changes from the failed fixture attempt; all temporary edits
  removed. Worktree clean, generated profraw removed. Existing public control endpoint tests are in
  crates/asb-control/tests/endpoint.rs, but runtime cannot currently reuse their private fixtures.
  Narrow repair candidate: expose a bounded test-only ControlServer fixture API or add an
  asb-runtime integration fixture; separately provision containerized bwrap/systemd runner. No
  push/review/merge below 90%.

- 2026-10-12T23:43:13+00:00: Recorded command exit 0; command argv SHA-256
  81656827fb76aee22b81f0a0af3e6b3438da65d0727d76385005b27ac615c6d1.

- 2026-10-12T23:43:38+00:00: Recorded command exit 0; command argv SHA-256
  37a8f2d06ff45172c4bb64cc908971056a01f7a1d2a787ec66ef894f89a2b855.

- 2026-10-12T23:43:59+00:00: Recorded command exit 0; command argv SHA-256
  802d229a2d65bf2cd6af4c0f9216ffbad7832cef6795e4263825646a9fc5e7c3.

- 2026-10-12T23:46:50+00:00: Recorded command exit 0; command argv SHA-256
  428457ea9cc6a21bd46c5be6651ba2faccb5b0b07ddc2fd6f96eca730dea5ab7.

- 2026-10-12T23:47:05+00:00: Recorded command exit 0; command argv SHA-256
  d15aed147f5d76f3e7dfcb58d63d3636fefe99f216bbb9bf53deb082aa2e0198.

- 2026-10-12T23:47:25+00:00: Recorded command exit 0; command argv SHA-256
  6ea4f0c78fa5e3c788788ee271924d8fec809d9dc937aeb1a7b37c5aa8409acf.

- 2026-10-12T23:47:29+00:00: Recorded command exit 0; command argv SHA-256
  98895f7181ffe4619810c653239e3d3ad51bc2ceb2cb67ee51c29275f8683e51.

- 2026-10-12T23:47:58+00:00: Focused qualified_runtime_backend_executes_and_reaps_child passed 1/1
  through canonical handoffctl. Serialized tools/quality/check_coverage.py completed all workspace
  suites; latest durable aggregate remains 89.28% lines, 85.11% functions, 90.66% regions, below the
  fixed 90% line floor. Profraw artifacts were removed through handoffctl and product worktree is
  clean at d87352dd. No review/PR/merge should proceed while the coverage gate remains unmet.

- 2026-10-12T23:48:03+00:00: Checkpointed source commit d87352ddb511c48b4be1bdbecdd26fb2cf6597a8.

- 2026-10-13T00:36:51+00:00: Coordinator recovery: no matching worker process/session is live;
  release stale active lease while preserving checkpoint d87352d, branch/head, and coverage evidence
  for replacement Luna worker.

- 2026-10-13T00:38:12+00:00: Claimed by ar1783-workload-selection-luna.

- 2026-10-13T00:38:24+00:00: Checkpointed source commit 4902eb0d316228c9e566a9ceacfa823613a3a9f7.

- 2026-10-13T00:38:29+00:00: Recorded command exit 0; command argv SHA-256
  05423f546638fa0266e03f759296fdc2689e698f112d4b7b172bb75e95f5dca1.

- 2026-10-13T00:38:31+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-13T00:39:03+00:00: Overlap audit: AR-1835 head 06565d3d adds
  unix_runtime_bootstrap_uses_kernel_session_and_rejects_stale_replay, covering authenticated
  ControlClient/server bootstrap, stale replay and cancellation. This is the exact
  live_service/control bootstrap seam identified by AR-1783; no distinct AR-1783 production contract
  remains to implement. No retry of the hanging control fixture; await reviewed AR-1835 integration,
  then rerun one bounded serialized coverage command.

- 2026-10-13T00:39:07+00:00: Heartbeat by ar1783-workload-selection-luna.

- 2026-10-13T00:42:41+00:00: Worker overlap audit complete: no product gap distinct from AR-1835;
  preserve checkpoint and defer serialized coverage rerun until AR-1835 exact-head gate resolves.

- 2026-10-13T19:37:07+00:00: Claimed by ar1783-workload-selection-luna.

- 2026-10-13T19:37:19+00:00: Reserved retry circuit launch slot; expired_slots_cleaned=0.

- 2026-10-13T19:37:22+00:00: Recorded retryable failure 1/3.

- 2026-10-13T19:37:25+00:00: Recorded command exit 1; command argv SHA-256
  8da9301c3b436d1d2430be4cf7a9ec902b7262bb7e8f28de6f839d0fd0e2560c.

- 2026-10-13T19:37:52+00:00: Reserved retry circuit launch slot; expired_slots_cleaned=0.

- 2026-10-13T19:37:55+00:00: Released retry circuit launch slot.
