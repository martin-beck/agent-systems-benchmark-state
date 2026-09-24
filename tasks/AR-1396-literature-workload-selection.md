---
{
  "branch": "codex/ar-1396-literature-selection",
  "checkpoint_commit": "58bc56f0b793c4f42e83cbe27515d63d22cfda51",
  "claim_expires": "2026-09-24T12:18:05+00:00",
  "depends_on": [
    "AR-1395",
    "AR-1399"
  ],
  "id": "AR-1396",
  "next_action": "PR #288 exact head 58bc56f0b793c4f42e83cbe27515d63d22cfda51; fresh checks pending after CLI fail-closed validation repair. Review remaining OriginalWorkloads seams before merge.",
  "observed_branch": "codex/ar-1396-literature-selection",
  "observed_dirty": 0,
  "observed_head": "58bc56f0b793c4f42e83cbe27515d63d22cfda51",
  "owner": "codex-asb-ar1396-literature-selection-luna56",
  "plan": "../plans/AR-1396-literature-workload-selection.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make qualified literature workload families selectable beside built-in ASB software-engineering fixtures.",
  "task_revision": 49,
  "title": "Literature workload selection",
  "updated_at": "2026-09-24T10:49:35+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1396"
}
---

This AR owns user-facing selection and evidence labeling after the registry and
adapters exist; it does not bypass licensing, acquisition, evaluator, or
platform gates.

- 2026-09-24T10:04:59+00:00: AR-1395 and AR-1399 are done; the registry has 22 validated records.
  Begin explicit catalog/plan/CLI/replay/report selection with fail-closed evidence labels.

- 2026-09-24T10:06:16+00:00: Claimed by codex-asb-ar1396-literature-selection-luna56.

- 2026-09-24T10:08:10+00:00: Recorded command exit 0; command argv SHA-256
  782d0973594bb9e739a49ad1b4fdd8b7152bc89f4d181b8f25550d964ca70250.

- 2026-09-24T10:10:49+00:00: Reclaim from declared product worktree so coordinator branch fence is
  established.

- 2026-09-24T10:10:52+00:00: Claimed by codex-asb-ar1396-literature-selection-luna56.

- 2026-09-24T10:12:29+00:00: Heartbeat by codex-asb-ar1396-literature-selection-luna56.

- 2026-09-24T10:14:10+00:00: Recorded command exit 0; command argv SHA-256
  f31e2b6165f9ecfa584d082799bd098b0b4c64d0da7d2d84a9ac33f064b2932a.

- 2026-09-24T10:15:24+00:00: Recorded command exit 0; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-24T10:15:51+00:00: Recorded command exit 0; command argv SHA-256
  7acbfc5643fcdbb7873911f066ea0978161873ca42a6d1e5ce60fbf5ee666e26.

- 2026-09-24T10:16:06+00:00: Recorded command exit 0; command argv SHA-256
  7e95d847fbc0a65d817802508e657e3c046e6fddef969fd1dd6e6ad176f63746.

- 2026-09-24T10:17:10+00:00: Recorded command exit 0; command argv SHA-256
  d19733f1515bf14d5f84c0ff49a87f41c26f87b52a41f9ce107d7645f7bbf873.

- 2026-09-24T10:17:31+00:00: Recorded command exit 0; command argv SHA-256
  9a16c5c6925e14af2c2b7d42cc2f99cad4f06b6b5760a349cae36197f2c7441e.

- 2026-09-24T10:17:51+00:00: Recorded command exit 8; command argv SHA-256
  8b33846ffb8482b3d5f465aa0701cb9a4e988a887a1d8499ea7c53a946ef5755.

- 2026-09-24T10:18:16+00:00: Published PR #288 from signed+DCO head
  a0024df808f67ab4e1d004adfa39edc9e25de89d. Wrapped focused literature tests passed 7/7; wrapped
  cargo test --locked --workspace passed all non-ignored tests. Exact-head checks are pending except
  AWQ shadow and SPDX/header checks passed.

- 2026-09-24T10:18:29+00:00: Recorded command exit 1; command argv SHA-256
  8b33846ffb8482b3d5f465aa0701cb9a4e988a887a1d8499ea7c53a946ef5755.

- 2026-09-24T10:18:50+00:00: Recorded command exit 0; command argv SHA-256
  1add495fc3328132b1c12d496b9a074a32146965f35790b4b63ab1c1a58ccb49.

- 2026-09-24T10:19:12+00:00: Recorded command exit 0; command argv SHA-256
  20e163e76af3bfb6b98e8d80370559b545afce3b49cbebf845384e8c12635480.

- 2026-09-24T10:19:48+00:00: Heartbeat by codex-asb-ar1396-literature-selection-luna56.

- 2026-09-24T10:29:16+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-24T10:29:35+00:00: Recorded command exit 0; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-09-24T10:30:04+00:00: Recorded command exit 0; command argv SHA-256
  75eddc3cdc5cc090f8aa5fbd0cc3031cd0f66f69204b14ec22d94222d94e9778.

- 2026-09-24T10:30:32+00:00: Recorded command exit 8; command argv SHA-256
  8b33846ffb8482b3d5f465aa0701cb9a4e988a887a1d8499ea7c53a946ef5755.

- 2026-09-24T10:31:03+00:00: Rebased PR #288 onto signed recovery main b63394 and force-with-lease
  pushed signed+DCO head e1e532ea1d4e2eceff6fa8d55c8df4ec2e8400ea. Fresh exact-head checks started;
  AWQ shadow and SPDX/header checks passed, remaining checks pending.

- 2026-09-24T10:31:31+00:00: Recorded command exit 8; command argv SHA-256
  8b33846ffb8482b3d5f465aa0701cb9a4e988a887a1d8499ea7c53a946ef5755.

- 2026-09-24T10:32:13+00:00: Recorded command exit 8; command argv SHA-256
  8b33846ffb8482b3d5f465aa0701cb9a4e988a887a1d8499ea7c53a946ef5755.

- 2026-09-24T10:32:57+00:00: Recorded command exit 8; command argv SHA-256
  8b33846ffb8482b3d5f465aa0701cb9a4e988a887a1d8499ea7c53a946ef5755.

- 2026-09-24T10:33:34+00:00: Recorded command exit 8; command argv SHA-256
  8b33846ffb8482b3d5f465aa0701cb9a4e988a887a1d8499ea7c53a946ef5755.

- 2026-09-24T10:34:28+00:00: Recorded command exit 8; command argv SHA-256
  8b33846ffb8482b3d5f465aa0701cb9a4e988a887a1d8499ea7c53a946ef5755.

- 2026-09-24T10:34:44+00:00: Recorded command exit 8; command argv SHA-256
  8b33846ffb8482b3d5f465aa0701cb9a4e988a887a1d8499ea7c53a946ef5755.

- 2026-09-24T10:34:58+00:00: Heartbeat by codex-asb-ar1396-literature-selection-luna56.

- 2026-09-24T10:35:25+00:00: Recorded command exit 8; command argv SHA-256
  8b33846ffb8482b3d5f465aa0701cb9a4e988a887a1d8499ea7c53a946ef5755.

- 2026-09-24T10:36:15+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-24T10:36:37+00:00: Recorded command exit 101; command argv SHA-256
  10a701b2424e5ed226b0455eb01ce19376ff98a24fb81ec0200c779f16f8a3dc.

- 2026-09-24T10:37:07+00:00: Recorded command exit 0; command argv SHA-256
  d2c1f2da93c56080e89172c6bdbea13dfb310792273bd34989003d5a60853c10.

- 2026-09-24T10:37:22+00:00: Recorded command exit 0; command argv SHA-256
  565b04b503d6d7bfabfd2845aea0b91208d33abbc73adaaf208c27f9198d6768.

- 2026-09-24T10:37:37+00:00: Recorded command exit 0; command argv SHA-256
  8cc40e1067b6f94a34d719fa3c47b359814c0c87950fa3cfc405a37f30115cda.

- 2026-09-24T10:37:53+00:00: Recorded command exit 0; command argv SHA-256
  525718d87c89898bbd0a02c059b5d0442ffcbfecfd2ff08e02ac213df258c8c6.

- 2026-09-24T10:38:37+00:00: CLI validation now consults combined catalog: registry literature IDs
  are explicitly rejected as evaluator-unavailable before preparation, while built-in behavior is
  unchanged. Updated workflow provenance digest. Wrapped workflow_transcript tests pass 3/3; prior
  wrapped cargo test -p asb-cli failure was exact provenance drift (old cli_source_sha256), repaired
  in 58bc56f.

- 2026-09-24T10:48:05+00:00: Heartbeat by codex-asb-ar1396-literature-selection-luna56.

- 2026-09-24T10:48:27+00:00: Recorded command exit 1; command argv SHA-256
  523f3b52061b439c10a3601c7e683cf449add10867aa8c0e3ea47d595ed72a82.

- 2026-09-24T10:49:10+00:00: Recorded command exit 0; command argv SHA-256
  89977560b196c07e8f67e7675d5ab5fd808c5f12f310fe5f9f1f6e0e181cca53.

- 2026-09-24T10:49:35+00:00: Recorded command exit 0; command argv SHA-256
  3757a148b4f12f0aad34a62b5a1e6b87941a90f8182dd325cbc813b868df33a8.
