---
{
  "branch": "codex/ar-1415-literature-selector-total-coverage",
  "checkpoint_commit": "c533734a486a8c3a8c854c1fce395b915986d874",
  "claim_expires": "2026-09-24T20:10:53+00:00",
  "depends_on": [
    "AR-1410",
    "AR-1414"
  ],
  "id": "AR-1415",
  "next_action": "Rerun exact failed post-merge workflow 36038241138 after three green isolated Goose reproductions; wait all seven terminal SUCCESS, verify main, then release.",
  "observed_branch": "codex/ar-1415-literature-selector-total-coverage",
  "observed_dirty": 0,
  "observed_head": "bc0cfaff9cc126cb4f3dbadfc9a6284750dba0bc",
  "owner": "ar1415-literature-selector-total-coverage-luna56",
  "plan": "../plans/AR-1415.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make the complete literature workload inventory selectable beside built-in software-engineering fixtures with truthful evidence gates.",
  "task_revision": 80,
  "title": "Total literature workload selector coverage",
  "updated_at": "2026-09-24T18:11:01+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1415"
}
---

This AR closes the selector contract across every benchmark and framework-derived
workload recorded in `docs/WORKLOADS.md`, `docs/RELATED_WORK.md`, and the
versioned registry. It must not download datasets, contact providers, or promote
provenance-only records to executable or qualified status.

Acceptance requires a machine-checked parity table showing that each registry ID
has a stable family/kind, source and dataset revision, selector entry, generated
documentation entry, and an explicit evidence state. Built-in and literature
workloads must appear in one deterministic inventory, while missing evaluator,
license, image, reset, or platform evidence causes selection to remain visibly
unavailable and execution to fail closed before network/provider access. Unknown,
duplicate, stale, or hand-edited IDs are rejected with positive and negative tests.

Verify selector filters, plan validation, doctor/catalog output, generated docs,
schema parity, and full exact-head/post-merge gates.

- 2026-09-24T17:42:37+00:00: Dependencies AR-1410 and AR-1414 are durably done; begin total
  literature selector coverage audit.

- 2026-09-24T17:43:43+00:00: Claimed by ar1415-literature-selector-total-coverage-luna56.

- 2026-09-24T17:44:30+00:00: Heartbeat by ar1415-literature-selector-total-coverage-luna56.

- 2026-09-24T17:44:33+00:00: Recorded command exit 0; command argv SHA-256
  d04aa803a9fcb854b247572f9b417fd1935a57ca978bb887d2e7c188e99db043.

- 2026-09-24T17:44:48+00:00: Recorded command exit 0; command argv SHA-256
  b04e51d6a8a1cd1d991d96d1b0eeb7f5236f1056ccb95c8f404b26c181dc4797.

- 2026-09-24T17:45:14+00:00: Recorded command exit 0; command argv SHA-256
  6d84b6c7a75bca49c1a5594b7910983c9f45896fc7e3ba41443bffcbde813b6e.

- 2026-09-24T17:45:40+00:00: Recorded command exit 0; command argv SHA-256
  1de9d400e80b59c921d5cbedad1b9627b802704da17704cb1fc71db3235d7814.

- 2026-09-24T17:45:54+00:00: Recorded command exit 0; command argv SHA-256
  73d343fb1b1db6e5e62ebcb1555147e3fb3f2aeb698d7e44ffac3efc7ad50480.

- 2026-09-24T17:46:08+00:00: Recorded command exit 0; command argv SHA-256
  e6dd053754e1bbb8a92a06522822584d6e44618e0bd9be2e2e5511ba5d555182.

- 2026-09-24T17:46:22+00:00: Recorded command exit 0; command argv SHA-256
  cf2f07823d51974ae008665cec43c8415e265afb7fc05e78c431a10b4b766bd3.

- 2026-09-24T17:46:51+00:00: Recorded command exit 0; command argv SHA-256
  98c4842a77b5665b6b9ec38e6822912c54ae6fa8c193e772ebe93cc22defad5b.

- 2026-09-24T17:47:13+00:00: Recorded command exit 0; command argv SHA-256
  85ad9fbcfaf60704c8369958bf63db2e4faac23124289356d8a5f44ad8422b1d.

- 2026-09-24T17:48:08+00:00: Recorded command exit 0; command argv SHA-256
  64ad0b4c87eb2b317897ef5f6304eaf5248b4d51e5703219dc996350ee7e9ab0.

- 2026-09-24T17:48:27+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-24T17:49:04+00:00: Recorded command exit 0; command argv SHA-256
  85dd84dd56580a2afa98117bce810d456ae12d097a2b8939972e106ed547fadc.

- 2026-09-24T17:49:30+00:00: Package gate passed completely: asb-cli 105 unit + integration tests
  and asb-workloads 33 unit/integration/doc tests all green. The wrapper then returned LOCK_TIMEOUT
  after 10s acquiring the exclusive coordinator lock while recording command evidence; no product
  test failure occurred.

- 2026-09-24T17:49:37+00:00: Recorded command exit 0; command argv SHA-256
  d04aa803a9fcb854b247572f9b417fd1935a57ca978bb887d2e7c188e99db043.

- 2026-09-24T17:49:51+00:00: Recorded command exit 0; command argv SHA-256
  5882166f925a7392d5afbac44f9caa6cb1c5885b57088e8b68d4974019d14058.

- 2026-09-24T17:50:14+00:00: Recorded command exit 0; command argv SHA-256
  64ad0b4c87eb2b317897ef5f6304eaf5248b4d51e5703219dc996350ee7e9ab0.

- 2026-09-24T17:50:28+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-09-24T17:50:48+00:00: Recorded command exit 0; command argv SHA-256
  82d9161d0c2c4773f85b2ccd4f715ef9973227a3bc56d4941f67deec196163cb.

- 2026-09-24T17:51:02+00:00: Recorded command exit 0; command argv SHA-256
  c6684a48d77d25e85a861643602430a771be5b564b0154d4969d394919f4a57e.

- 2026-09-24T17:51:22+00:00: Recorded command exit 0; command argv SHA-256
  1ff5ecc078b4a2c30e89e1e442312b20a7c190210f58a4d688d6c62e4e9ed025.

- 2026-09-24T17:51:37+00:00: Recorded command exit 0; command argv SHA-256
  9d7fe3c569a7d58642fa4e8c319b2da1db1dc9aa56cf2b361ef7675029dc2c4f.

- 2026-09-24T17:52:00+00:00: Recorded command exit 0; command argv SHA-256
  7562a8d9f316aec960e43cab091a5894539b6c1aa824d8adfadb7910001f99a7.

- 2026-09-24T17:52:27+00:00: Committed and pushed signed+DCO bc0cfaff: machine-checked
  docs/registry/generated-catalog parity and explicit evidence-state coverage, including Exercism
  Tracks documentation gap. PR #303 opened at exact branch
  codex/ar-1415-literature-selector-total-coverage. Focused Python suite 15 passed; package Rust
  gates passed.

- 2026-09-24T17:52:36+00:00: Recorded command exit 0; command argv SHA-256
  1d66c1d5d52f6a24b195a419e5526e97bf51d80d983a44b567cc18515d8c7e40.

- 2026-09-24T17:55:11+00:00: Heartbeat by ar1415-literature-selector-total-coverage-luna56.

- 2026-09-24T17:56:59+00:00: Recorded command exit 0; command argv SHA-256
  57ec6e9d5619f109899446c730ce0a4ba266c015de2dccf3c047e47617a9672d.

- 2026-09-24T17:57:56+00:00: Heartbeat by ar1415-literature-selector-total-coverage-luna56.

- 2026-09-24T17:58:03+00:00: Recorded command exit 0; command argv SHA-256
  aaea4af1d103a3225046fa1fbcac6d4cb0482146dba1d61af276675e871eb733.

- 2026-09-24T17:58:23+00:00: Heartbeat by ar1415-literature-selector-total-coverage-luna56.

- 2026-09-24T17:58:30+00:00: Recorded command exit 0; command argv SHA-256
  aaea4af1d103a3225046fa1fbcac6d4cb0482146dba1d61af276675e871eb733.

- 2026-09-24T17:58:49+00:00: Heartbeat by ar1415-literature-selector-total-coverage-luna56.

- 2026-09-24T17:58:57+00:00: Recorded command exit 0; command argv SHA-256
  aaea4af1d103a3225046fa1fbcac6d4cb0482146dba1d61af276675e871eb733.

- 2026-09-24T17:59:15+00:00: Heartbeat by ar1415-literature-selector-total-coverage-luna56.

- 2026-09-24T17:59:23+00:00: Recorded command exit 0; command argv SHA-256
  55e542ae5ec0ed29ee5f72bd7d0516170055471a3eecb903620fcded8093b467.

- 2026-09-24T17:59:43+00:00: Recorded command exit 0; command argv SHA-256
  aaea4af1d103a3225046fa1fbcac6d4cb0482146dba1d61af276675e871eb733.

- 2026-09-24T18:00:04+00:00: Recorded command exit 0; command argv SHA-256
  465f00b1cac0c57061f5e9c95450afa095a418dcd7aeb51f070824da5be2e645.

- 2026-09-24T18:00:31+00:00: Recorded command exit 0; command argv SHA-256
  e75d80c3ba62dea40e24a10fcaf0a3ec117e5aaed5703e78d0826a86b800b98d.

- 2026-09-24T18:00:52+00:00: Recorded command exit 0; command argv SHA-256
  4955b2e5ed1a8d958cd433002c67124ea03b6fb42e2842979009daf9fd7affae.

- 2026-09-24T18:01:12+00:00: Recorded command exit 0; command argv SHA-256
  05e97daf385cbc62f6d9bcaa8492d316d45c36baeba9684cc9b9692c4b5b25b4.

- 2026-09-24T18:01:39+00:00: PR #303 merged after exact-base review and all seven required checks
  succeeded. Merge commit c533734a486a8c3a8c854c1fce395b915986d874. Post-merge workflow IDs
  recorded; Huawei MIT source headers 36038241020 already SUCCESS, six remain in progress.

- 2026-09-24T18:01:51+00:00: Recorded command exit 0; command argv SHA-256
  05e97daf385cbc62f6d9bcaa8492d316d45c36baeba9684cc9b9692c4b5b25b4.

- 2026-09-24T18:02:09+00:00: Heartbeat by ar1415-literature-selector-total-coverage-luna56.

- 2026-09-24T18:02:18+00:00: Recorded command exit 0; command argv SHA-256
  05e97daf385cbc62f6d9bcaa8492d316d45c36baeba9684cc9b9692c4b5b25b4.

- 2026-09-24T18:02:38+00:00: Recorded command exit 0; command argv SHA-256
  05e97daf385cbc62f6d9bcaa8492d316d45c36baeba9684cc9b9692c4b5b25b4.

- 2026-09-24T18:02:56+00:00: Heartbeat by ar1415-literature-selector-total-coverage-luna56.

- 2026-09-24T18:03:06+00:00: Recorded command exit 0; command argv SHA-256
  05e97daf385cbc62f6d9bcaa8492d316d45c36baeba9684cc9b9692c4b5b25b4.

- 2026-09-24T18:03:26+00:00: Recorded command exit 0; command argv SHA-256
  05e97daf385cbc62f6d9bcaa8492d316d45c36baeba9684cc9b9692c4b5b25b4.

- 2026-09-24T18:03:45+00:00: Heartbeat by ar1415-literature-selector-total-coverage-luna56.

- 2026-09-24T18:03:56+00:00: Recorded command exit 0; command argv SHA-256
  05e97daf385cbc62f6d9bcaa8492d316d45c36baeba9684cc9b9692c4b5b25b4.

- 2026-09-24T18:04:15+00:00: Recorded command exit 0; command argv SHA-256
  05e97daf385cbc62f6d9bcaa8492d316d45c36baeba9684cc9b9692c4b5b25b4.

- 2026-09-24T18:04:35+00:00: Heartbeat by ar1415-literature-selector-total-coverage-luna56.

- 2026-09-24T18:04:44+00:00: Recorded command exit 0; command argv SHA-256
  05e97daf385cbc62f6d9bcaa8492d316d45c36baeba9684cc9b9692c4b5b25b4.

- 2026-09-24T18:05:03+00:00: Recorded command exit 0; command argv SHA-256
  f9770b0d3a8fac1446b0badd0aa58fdd886c32c7de69a39347132dca69e9e241.

- 2026-09-24T18:05:23+00:00: Heartbeat by ar1415-literature-selector-total-coverage-luna56.

- 2026-09-24T18:05:32+00:00: Recorded command exit 0; command argv SHA-256
  05e97daf385cbc62f6d9bcaa8492d316d45c36baeba9684cc9b9692c4b5b25b4.

- 2026-09-24T18:05:53+00:00: Heartbeat by ar1415-literature-selector-total-coverage-luna56.

- 2026-09-24T18:06:01+00:00: Recorded command exit 0; command argv SHA-256
  05e97daf385cbc62f6d9bcaa8492d316d45c36baeba9684cc9b9692c4b5b25b4.

- 2026-09-24T18:06:22+00:00: Recorded command exit 0; command argv SHA-256
  3c886159e8e99aa4118511aa3bba251fbf783f97cb46ad32ac2e3a4cfc705a21.

- 2026-09-24T18:06:41+00:00: Recorded command exit 0; command argv SHA-256
  9b21e256a77cc00ff1e7cbe1cb4a05ae75132134c8228ecb8e954a0a8a708cc2.

- 2026-09-24T18:07:13+00:00: Recorded command exit 0; command argv SHA-256
  5045e4710ba5c0c8bebbae7fcf3dea4af04c948ad3ae1a8cb57220b3f01916fe.

- 2026-09-24T18:07:34+00:00: Recorded command exit 0; command argv SHA-256
  d5c46a9787e3e5457b735b04aea3e83784bf557e6bcc1f9edef67765cb2a4690.

- 2026-09-24T18:07:56+00:00: Recorded command exit 0; command argv SHA-256
  d5c46a9787e3e5457b735b04aea3e83784bf557e6bcc1f9edef67765cb2a4690.

- 2026-09-24T18:08:25+00:00: Post-merge workflow 36038241138 failed only at Materialize immutable
  aarch64 guest userspace after goose::tests::diagnostic_and_symlink_fail_closed observed unwrap_err
  got Ok GooseOutcome Failed exit 127. Exact test passed three consecutive times in isolated
  worktree on current merged tree; no product mutation. Treat as runner/environment flake and rerun
  exact workflow, never waive failure.

- 2026-09-24T18:08:34+00:00: Recorded command exit 0; command argv SHA-256
  6c1ad1835367ca8142d250d5177b0416eb9e16680adfe38b24ea42e2a00c7fa8.

- 2026-09-24T18:08:53+00:00: Recorded command exit 0; command argv SHA-256
  97b929e0db4c20ff1b2006ecfc1bce731a0a256b17bb244dc3f0149b36c7b599.

- 2026-09-24T18:09:12+00:00: Heartbeat by ar1415-literature-selector-total-coverage-luna56.

- 2026-09-24T18:09:23+00:00: Recorded command exit 0; command argv SHA-256
  05e97daf385cbc62f6d9bcaa8492d316d45c36baeba9684cc9b9692c4b5b25b4.

- 2026-09-24T18:09:44+00:00: Recorded command exit 0; command argv SHA-256
  09abf547b0477aa99dd2c49fe8ed72659731b610d3ef0f1e839e74a0993d997f.

- 2026-09-24T18:10:04+00:00: Heartbeat by ar1415-literature-selector-total-coverage-luna56.

- 2026-09-24T18:10:13+00:00: Recorded command exit 0; command argv SHA-256
  05e97daf385cbc62f6d9bcaa8492d316d45c36baeba9684cc9b9692c4b5b25b4.

- 2026-09-24T18:10:34+00:00: Recorded command exit 0; command argv SHA-256
  09abf547b0477aa99dd2c49fe8ed72659731b610d3ef0f1e839e74a0993d997f.

- 2026-09-24T18:10:53+00:00: Heartbeat by ar1415-literature-selector-total-coverage-luna56.

- 2026-09-24T18:11:01+00:00: Recorded command exit 0; command argv SHA-256
  05e97daf385cbc62f6d9bcaa8492d316d45c36baeba9684cc9b9692c4b5b25b4.
