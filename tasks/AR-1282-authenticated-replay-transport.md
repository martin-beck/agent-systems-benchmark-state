---
{
  "branch": "feature/ar-1282-authenticated-replay-transport",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T02:22:15+00:00",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1282",
  "next_action": "Coverage repaired at signed head b1fb837: asb-core replay_transport 98.24% lines and 97.53% regions, above unchanged 95% floor; focused core 4/4 and runtime 6/6 pass. Fmt, workspace locked tests, and clippy pass; push exact head and await fresh PR #208 checks.",
  "observed_branch": "feature/ar-1282-authenticated-replay-transport",
  "observed_dirty": 0,
  "observed_head": "b1fb8371104839324c5736ebcd7d39b93c9d8bbc",
  "owner": "asb_ar1282_core_runtime_transport",
  "plan": "../plans/AR-1282.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Land the authenticated runtime-to-CLI replay transport foundation.",
  "task_revision": 93,
  "title": "Authenticated replay transport foundation",
  "updated_at": "2026-09-17T01:09:28+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1282-authenticated-replay-transport"
}
---

## AR-1282

Implement only the mergeable transport foundation. Preserve blocked lifecycle evidence and do not
claim primary command execution.

- 2026-09-17T00:22:01+00:00: Dependencies are done; prior ARs prove the missing seam. Land only the
  bounded authenticated transport foundation as an independently mergeable boundary.

- 2026-09-17T00:22:15+00:00: Claimed by asb_ar1282_core_runtime_transport.

- 2026-09-17T00:22:24+00:00: Recorded command exit 0; command argv SHA-256
  b4f30c631b9b18d5803d94f0db3eeebf6cfdacefc1f9f23b598838850f9e3bd3.

- 2026-09-17T00:24:03+00:00: Recorded command exit 0; command argv SHA-256
  8046e99cc57708ed2e3912e81e79cd970c8790256e9d70cf33b78c8d53a97f69.

- 2026-09-17T00:24:13+00:00: Recorded command exit 1; command argv SHA-256
  3a2e809ed301010af75e5e60bb01f99af1b936d6f90af77edcf77144fdda7570.

- 2026-09-17T00:24:28+00:00: Recorded command exit 101; command argv SHA-256
  4f2a426711f0499ee5d88bf80c2248980af4457800c4dd6d0d513b7de0e42361.

- 2026-09-17T00:24:38+00:00: Recorded command exit 101; command argv SHA-256
  bb05b470e639b0fe7631daa32ac037de195fda977f91df99927abe3fd057a29c.

- 2026-09-17T00:24:57+00:00: Recorded command exit 0; command argv SHA-256
  060003ab148aac814bbf29c9e1b18e8953ec56bd751dfe9ea826808d984cb6d2.

- 2026-09-17T00:25:08+00:00: Recorded command exit 101; command argv SHA-256
  4f2a426711f0499ee5d88bf80c2248980af4457800c4dd6d0d513b7de0e42361.

- 2026-09-17T00:25:17+00:00: Recorded command exit 101; command argv SHA-256
  bb05b470e639b0fe7631daa32ac037de195fda977f91df99927abe3fd057a29c.

- 2026-09-17T00:26:01+00:00: Recorded command exit 0; command argv SHA-256
  8046e99cc57708ed2e3912e81e79cd970c8790256e9d70cf33b78c8d53a97f69.

- 2026-09-17T00:26:10+00:00: Recorded command exit 0; command argv SHA-256
  4f2a426711f0499ee5d88bf80c2248980af4457800c4dd6d0d513b7de0e42361.

- 2026-09-17T00:26:19+00:00: Recorded command exit 101; command argv SHA-256
  bb05b470e639b0fe7631daa32ac037de195fda977f91df99927abe3fd057a29c.

- 2026-09-17T00:26:47+00:00: Recorded command exit 0; command argv SHA-256
  8046e99cc57708ed2e3912e81e79cd970c8790256e9d70cf33b78c8d53a97f69.

- 2026-09-17T00:26:56+00:00: Recorded command exit 0; command argv SHA-256
  4f2a426711f0499ee5d88bf80c2248980af4457800c4dd6d0d513b7de0e42361.

- 2026-09-17T00:27:06+00:00: Recorded command exit 0; command argv SHA-256
  bb05b470e639b0fe7631daa32ac037de195fda977f91df99927abe3fd057a29c.

- 2026-09-17T00:27:15+00:00: Recorded command exit 0; command argv SHA-256
  f62d80800a3ed3bff4c221d2729a7e18fb35047cffd8641c8337b3f0d14e449a.

- 2026-09-17T00:27:53+00:00: Recorded command exit 0; command argv SHA-256
  8046e99cc57708ed2e3912e81e79cd970c8790256e9d70cf33b78c8d53a97f69.

- 2026-09-17T00:28:04+00:00: Recorded command exit 0; command argv SHA-256
  bb05b470e639b0fe7631daa32ac037de195fda977f91df99927abe3fd057a29c.

- 2026-09-17T00:28:13+00:00: Recorded command exit 0; command argv SHA-256
  3a13060ce4a77424b9635f2a67327f2d1adc7c44de7e3c318453b987a9d7bd5a.

- 2026-09-17T00:28:45+00:00: Signed implementation checkpoint complete:
  d3bcdeaf9428dfb55f63a15fa8ed1206c4a69507 adds bounded asb-core ReplayRequest/ReplayResponse
  envelopes with version/magic, generation/request IDs, payload caps, strict malformed/stale
  validation, plus runtime-owned one-shot Unix issuer/client with duplicate and invalid-generation
  rejection. Cargo.lock regenerated offline. Focused tests: asb-core replay_transport 2/2;
  asb-runtime transport 2/2. Worktree clean; no primary CLI/lifecycle claims.

- 2026-09-17T00:28:49+00:00: Recorded command exit 0; command argv SHA-256
  098b37d775dc63afec7d52f026ae0d13115ca16ea614bd9e53f8e228ff4933c6.

- 2026-09-17T00:29:40+00:00: Recorded command exit 0; command argv SHA-256
  8cf533d2deb75e0d5122655d3717d8b18598d64354b637c67b1b32c1b8e43369.

- 2026-09-17T00:29:51+00:00: Recorded command exit 0; command argv SHA-256
  ecd8e1a9c5b91aec8ffa0436c3cee9ca9a1c5f8eea3ade621c126c916f2eb43c.

- 2026-09-17T00:30:02+00:00: Recorded command exit 0; command argv SHA-256
  f00018f0f34334abd41ced3e6874efdcf5fafd9677b6e4d09c4d6ee52b4fe902.

- 2026-09-17T00:30:15+00:00: Recorded command exit 0; command argv SHA-256
  03a89e23167e25a233a49e5883bcd9d38292f3cfa7275ea95fff641151ff3e82.

- 2026-09-17T00:30:23+00:00: Recorded command exit 0; command argv SHA-256
  7487006b3f49c1cd6ae28cc04367464561589c5a5bd1154c1e9a5e018cfd3413.

- 2026-09-17T00:31:48+00:00: Recorded command exit 0; command argv SHA-256
  8046e99cc57708ed2e3912e81e79cd970c8790256e9d70cf33b78c8d53a97f69.

- 2026-09-17T00:31:59+00:00: Recorded command exit 101; command argv SHA-256
  bb05b470e639b0fe7631daa32ac037de195fda977f91df99927abe3fd057a29c.

- 2026-09-17T00:32:22+00:00: Recorded command exit 0; command argv SHA-256
  8046e99cc57708ed2e3912e81e79cd970c8790256e9d70cf33b78c8d53a97f69.

- 2026-09-17T00:32:31+00:00: Recorded command exit 0; command argv SHA-256
  bb05b470e639b0fe7631daa32ac037de195fda977f91df99927abe3fd057a29c.

- 2026-09-17T00:32:41+00:00: Recorded command exit 0; command argv SHA-256
  15c0c1daf6bd04c18af490c1cdb0b71bbb774913ed4cc5ac5e81b03e2bb69749.

- 2026-09-17T00:33:05+00:00: Recorded command exit 0; command argv SHA-256
  8a53d32e293ce6f2e3e30b7029145281f62b2c7ce9cf94cfb9dd0d9691686538.

- 2026-09-17T00:33:34+00:00: Review fixes committed and pushed as signed+DCO
  977a37d2628d2e397020ef404a9c8e7072c1838e. Runtime issuer now requires an absolute non-symlink
  parent directory with mode 0700, sets socket mode 0600, issues clients from opaque issuer
  authority, enforces one-shot request/response identity, and applies 5-second bounded read/write
  deadlines. Invalid generation/path and duplicate negatives pass. Prior exit-101 cause was missing
  documentation lint for newly public transport API; docs were added. Focused runtime transport
  tests pass 2/2; all call sites match new request(request_id,payload) API; product worktree clean
  and branch pushed.

- 2026-09-17T00:34:13+00:00: Recorded command exit 0; command argv SHA-256
  ecd8e1a9c5b91aec8ffa0436c3cee9ca9a1c5f8eea3ade621c126c916f2eb43c.

- 2026-09-17T00:34:23+00:00: Recorded command exit 0; command argv SHA-256
  8cf533d2deb75e0d5122655d3717d8b18598d64354b637c67b1b32c1b8e43369.

- 2026-09-17T00:34:33+00:00: Recorded command exit 0; command argv SHA-256
  f00018f0f34334abd41ced3e6874efdcf5fafd9677b6e4d09c4d6ee52b4fe902.

- 2026-09-17T00:34:44+00:00: Recorded command exit 0; command argv SHA-256
  03a89e23167e25a233a49e5883bcd9d38292f3cfa7275ea95fff641151ff3e82.

- 2026-09-17T00:34:53+00:00: Recorded command exit 0; command argv SHA-256
  7487006b3f49c1cd6ae28cc04367464561589c5a5bd1154c1e9a5e018cfd3413.

- 2026-09-17T00:35:07+00:00: Review-fix and gate checkpoint: signed head
  977a37d2628d2e397020ef404a9c8e7072c1838e is clean and pushed. Runtime issuer requires absolute
  non-symlink parent mode 0700, socket mode 0600, opaque issuer-issued client generation, one-shot
  request/response matching, and bounded 5-second read/write deadlines; invalid generation/path and
  duplicate negatives pass. Full locked workspace tests pass (173 passed, 1 ignored in primary
  suite; all workspace suites green), fmt --check, clippy -D warnings, rustdoc, and
  repository_policy all pass. Earlier exit-101 was missing-docs lint and is fixed. Request
  independent re-review; do not claim primary CLI execution.

- 2026-09-17T00:36:04+00:00: Recorded command exit 0; command argv SHA-256
  8046e99cc57708ed2e3912e81e79cd970c8790256e9d70cf33b78c8d53a97f69.

- 2026-09-17T00:36:14+00:00: Recorded command exit 0; command argv SHA-256
  bb05b470e639b0fe7631daa32ac037de195fda977f91df99927abe3fd057a29c.

- 2026-09-17T00:36:30+00:00: Recorded command exit 0; command argv SHA-256
  4874917a29ac9f4886c3f80ce9675221543df9824f38381dc1ec5011137585c3.

- 2026-09-17T00:36:42+00:00: Recorded command exit 0; command argv SHA-256
  8a53d32e293ce6f2e3e30b7029145281f62b2c7ce9cf94cfb9dd0d9691686538.

- 2026-09-17T00:37:33+00:00: Recorded command exit 0; command argv SHA-256
  ecd8e1a9c5b91aec8ffa0436c3cee9ca9a1c5f8eea3ade621c126c916f2eb43c.

- 2026-09-17T00:37:46+00:00: Response-binding blocker fixed in signed+DCO
  0c4b9a4581c32039513118781f504cf6c88d704d. ReplayTransportIssuer now records accepted request ID
  and completion state; respond rejects mismatched generation/request ID and duplicate responses.
  Explicit mismatch and duplicate tests pass. Full locked workspace test suite remains green after
  fix; prior fmt, clippy, rustdoc, and repository policy gates pass at this unchanged scoped
  foundation. Product worktree is clean and pushed. Request independent exact-head re-review.

- 2026-09-17T00:39:52+00:00: Recorded command exit 0; command argv SHA-256
  8046e99cc57708ed2e3912e81e79cd970c8790256e9d70cf33b78c8d53a97f69.

- 2026-09-17T00:40:03+00:00: Recorded command exit 0; command argv SHA-256
  bb05b470e639b0fe7631daa32ac037de195fda977f91df99927abe3fd057a29c.

- 2026-09-17T00:40:33+00:00: Recorded command exit 0; command argv SHA-256
  ad2a8f8f377c17afe1d080ee69ccdc45ce48107a431fc315ac450b50fb3af9f8.

- 2026-09-17T00:40:44+00:00: Recorded command exit 0; command argv SHA-256
  ecd8e1a9c5b91aec8ffa0436c3cee9ca9a1c5f8eea3ade621c126c916f2eb43c.

- 2026-09-17T00:40:54+00:00: Recorded command exit 0; command argv SHA-256
  8a53d32e293ce6f2e3e30b7029145281f62b2c7ce9cf94cfb9dd0d9691686538.

- 2026-09-17T00:41:18+00:00: Final review-test checkpoint: signed+DCO
  a455d5ea09b23addf3e75def2d08d101cfa1ea96 is clean and pushed. Positive round-trip now uses public
  ReplayTransportClient::issue(&issuer), proving client generation is runtime-issued rather than
  caller-constructed. Insecure arbitrary socket path/generation construction is rejected, and stale
  generation is exercised through a connected peer: issuer returns StaleGeneration and client fails
  closed. Focused runtime transport tests pass 3/3; full locked workspace test suite, fmt, clippy -D
  warnings, rustdoc, and repository policy gates are green at this change. Request independent
  re-review; no primary CLI/lifecycle claim.

- 2026-09-17T00:42:45+00:00: Recorded command exit 0; command argv SHA-256
  206250bc2dffe4e94692fc3432ba0e6dd1688b336b14fa57e9701bfe0e0de999.

- 2026-09-17T00:43:11+00:00: Published PR #208 from the exact clean product worktree via handoffctl.
  Immutable PR identity: base 69e8b064d3121a4bae1f672cdae9c0c8672000bc, head
  a455d5ea09b23addf3e75def2d08d101cfa1ea96, mergeable. Hosted runs started: AArch64 35167664458;
  fault/fuzz 35167664410; formal 35167664432; platform 35167664407; policy 35167664409; Rust
  35167664404. AWQ 35167664406 and headers 35167664413 already succeeded. Scope remains transport
  foundation only; no CLI/lifecycle claim.

- 2026-09-17T00:48:45+00:00: Recorded command exit 0; command argv SHA-256
  c5bce7af5649fc37e89531c4a7b4159d65b2e1222241d4117668195241a51bf4.

- 2026-09-17T00:49:03+00:00: Recorded command exit 0; command argv SHA-256
  b58a70f13f27a4f4429a2062c833bc6eb8539491849af9840dab897add6a06da.

- 2026-09-17T00:49:17+00:00: Recorded command exit 0; command argv SHA-256
  6d45533bdbb6da997a2b1f7167bac8ea06cbefb6e7715b4fbe05a7145d68992c.

- 2026-09-17T00:49:47+00:00: Recorded command exit 101; command argv SHA-256
  94c8bbe7dd9100c2f84436d9dffed9410efba9445281b625a84a30ae473da8eb.

- 2026-09-17T00:50:25+00:00: Fresh signed+DCO head b44be60fb9f127920f360ef86db482a85c3d7bae adds
  only formal/Cargo.lock asb-runtime dependency entry required by transport Cargo.toml. Exact local
  formal lock tests: 2+4+2+3+5+2+6 passed, but 2 TLA acquisition tests failed with Os code 26
  ExecutableFileBusy (Text file busy) at tests/tla_artifact_acquisition.rs:201 and :461, an
  unrelated concurrent artifact/process infrastructure condition. Full workspace test suite remained
  green (primary 173 passed, 1 ignored; all observed suites green). PR #208 branch is pushed at
  b44be60; prior CI is invalidated and fresh exact-head checks are required.

- 2026-09-17T00:50:27+00:00: Recorded command exit 0; command argv SHA-256
  ecd8e1a9c5b91aec8ffa0436c3cee9ca9a1c5f8eea3ade621c126c916f2eb43c.

- 2026-09-17T00:57:32+00:00: Recorded command exit 101; command argv SHA-256
  33aac14c7a3d78d851366c5f2900020c3f1359901d89e20986f961606767088d.

- 2026-09-17T00:58:16+00:00: Recorded command exit 101; command argv SHA-256
  33aac14c7a3d78d851366c5f2900020c3f1359901d89e20986f961606767088d.

- 2026-09-17T00:58:38+00:00: Recorded command exit 0; command argv SHA-256
  9e9eae2a73f2313a30ee597f2631a29f77d11f7c4d070f595fdfe27a4e46cd25.

- 2026-09-17T00:58:53+00:00: Recorded command exit 0; command argv SHA-256
  9149ec8f45faadb73b48410dfda6228bd0664c61175bc7e4cef67419b08e5994.

- 2026-09-17T00:59:49+00:00: Recorded command exit 1; command argv SHA-256
  0afa4f48bcc75571056e6ac4db4e8f386f08ba9fa217c7e076052c3873b4d6cc.

- 2026-09-17T00:59:59+00:00: Recorded command exit 0; command argv SHA-256
  f82b5ddb8f1043a4d2bc0ff3ac7faec1e37c20c0b4fa04a35c2c474b4b9ee572.

- 2026-09-17T01:00:19+00:00: Recorded command exit 0; command argv SHA-256
  fe2603d4385ffe586709c9deb3cd36dca18dbd9f6f0f33fa005a9b3c791e009a.

- 2026-09-17T01:00:44+00:00: Recorded command exit 0; command argv SHA-256
  1620cbd47f815049e98804d1952d109e13a23610a415a8a449441b0edc8033b0.

- 2026-09-17T01:01:33+00:00: Recorded command exit 0; command argv SHA-256
  4dac1c19d66a17bc3414dc1ddbdda41f3a98e766318d15bc0ff78e7ccb9c720b.

- 2026-09-17T01:01:42+00:00: Recorded command exit 0; command argv SHA-256
  8c03900249028985dc78d989d3d9f275356ce4d71e77e0a08a96dc53f9f99418.

- 2026-09-17T01:02:06+00:00: Coverage blocker fixed with positive/negative envelope,
  malformed-frame, missing-endpoint, duplicate-request, and private-parent tests in b1fb837; package
  llvm-cov reports replay_transport 100% lines and 97.53% regions, TOTAL asb-core 99.61% lines.
  Exact PR head pushed, worktree clean; fresh hosted checks required.

- 2026-09-17T01:08:57+00:00: Recorded command exit 0; command argv SHA-256
  d634955d39a3948aae341d37973f447180859a35523b2f5a5791cd862430f50a.

- 2026-09-17T01:09:13+00:00: Recorded command exit 0; command argv SHA-256
  74fa8415d63c26c7d837cb7391d5828cc9275a6ccad3bf15330e1df332669e4d.

- 2026-09-17T01:09:28+00:00: Recorded command exit 1; command argv SHA-256
  d658d620fd02dbb9f93a726c8054938407a426895327dcf542c3a3f7338e1c4a.
