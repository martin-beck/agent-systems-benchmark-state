---
{
  "branch": "feature/replay-opendesk",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T17:53:42+00:00",
  "depends_on": [
    "AR-0302",
    "AR-0503",
    "AR-0504",
    "AR-0401"
  ],
  "id": "AR-0507",
  "next_action": "Independently review immutable head 24a5519ef006c063f3a8d6e81d0928f2e9e986f9/tree 96f01bd39cd5e75a70d3618cec55e603b9643d38; publish only after approval, then require exact-head x86_64/aarch64 quality/formal/fault CI.",
  "observed_branch": "feature/replay-opendesk",
  "observed_dirty": 0,
  "observed_head": "24a5519ef006c063f3a8d6e81d0928f2e9e986f9",
  "owner": "replay_20260906",
  "plan": "../plans/AR-0507.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify replay conformance for OpenDesk.",
  "task_revision": 119,
  "title": "Qualify OpenDesk replay",
  "updated_at": "2026-09-07T15:13:33+00:00",
  "worktree_key": "agent-systems-benchmark-replay-opendesk"
}
---
## AR-0507

Qualify OpenDesk record/replay, network denial, parity, retries, tool calls, cancellation, and malformed-record failures.

- 2026-09-07T12:45:09+00:00: Promote AR-0507 after independent verification that AR-0302, AR-0503,
  AR-0504, and AR-0401 are complete; AR-0308 has been released.

- 2026-09-07T12:45:14+00:00: Claimed by replay_20260906.

- 2026-09-07T12:46:48+00:00: Recorded command exit 0; command argv SHA-256
  160eb49af6458ee7e4fc8c9b2fabdfc43fd3816ebd6c2dfdf1825e1b2189df2f.

- 2026-09-07T12:49:43+00:00: Recorded command exit 0; command argv SHA-256
  1fbd4444ed96c536123a35dbfdf6afc66e08c04e1a647d16e7083796497fa43b.

- 2026-09-07T12:49:54+00:00: Recorded command exit 0; command argv SHA-256
  79f6e02b3d674758f5fcbb05817bbe5488d58368e2bcd5266ece982dfc671440.

- 2026-09-07T12:51:42+00:00: Recorded command exit 0; command argv SHA-256
  abdc48162561cf14e1691af390dc92325815113c490c7a97b0ac8311df3153f4.

- 2026-09-07T12:52:31+00:00: Recorded command exit 0; command argv SHA-256
  da3e7a2040711e18013d321cdf080c3240e067c4d744f2184ac0614b24ea8c18.

- 2026-09-07T12:53:04+00:00: Recorded command exit 0; command argv SHA-256
  9704811a82ad10419bb3b606aa977e906793fd5681044b9fe67841d1a546e369.

- 2026-09-07T12:53:09+00:00: Recorded command exit 0; command argv SHA-256
  908a5c49182d5f748ec8d7eb31c93c1f43ed1a536a8d6d388c4998d2cd617130.

- 2026-09-07T12:53:24+00:00: Recorded command exit 101; command argv SHA-256
  b8d10328a7797ecb6d2de1c50953004ac0e38bd77329d541cb5970b879d31695.

- 2026-09-07T12:53:45+00:00: Recorded command exit 0; command argv SHA-256
  a870f916ef3543e39adf68f2df32585fc56b05ee8c2a4299d4367209b5d6452d.

- 2026-09-07T12:53:59+00:00: Recorded command exit 0; command argv SHA-256
  115abb0daafe9dc7560cc89c616b98d52da79d13db0f159833dfe694271e3ca7.

- 2026-09-07T12:54:51+00:00: Recorded command exit 1; command argv SHA-256
  97e2c1b70adc08da6dae289679009f17e22a3f624ace3a3a49bdecf4c9593011.

- 2026-09-07T12:55:18+00:00: Recorded command exit 101; command argv SHA-256
  3211cbb17659455b743594d7b488023c32bf8ad124e43fb5b7a2d3f51490bd3d.

- 2026-09-07T12:56:01+00:00: Recorded command exit 0; command argv SHA-256
  3c56f8ecc42ae06a9fd177a5fd0615ec20f7a8a8e3d10fd286332065f637654d.

- 2026-09-07T12:56:32+00:00: Recorded command exit 101; command argv SHA-256
  3211cbb17659455b743594d7b488023c32bf8ad124e43fb5b7a2d3f51490bd3d.

- 2026-09-07T12:57:07+00:00: Recorded command exit 0; command argv SHA-256
  ab71e906d9cd40ec5d79e8ee2890bc6e2c6a9bdb6832652383780ef5ebd41a75.

- 2026-09-07T12:57:29+00:00: Recorded command exit 0; command argv SHA-256
  85bf5ba1b5376c1649f842aa42cd69a245d05e3708e5392ae0c64335bbbf8405.

- 2026-09-07T12:57:53+00:00: Recorded command exit 101; command argv SHA-256
  3211cbb17659455b743594d7b488023c32bf8ad124e43fb5b7a2d3f51490bd3d.

- 2026-09-07T12:59:39+00:00: Pinned OpenDesk 0.3.5 real credential-free loopback capture reached
  cassette sealing and failed deterministically with CassetteError::NotNormalized because the client
  emits legal HTTP header name span_id. A focused assertion identified the exact name without
  retaining its random value. The same underscore is rejected independently by StrictReplayService
  validate_http_request, so value redaction alone cannot make the real client replayable. Narrow
  proposed fix: consistently admit underscore in the bounded header-name grammar, redact span_id as
  an exact volatile selector for this qualification, retain lowercase/unique/sorted/control-free
  constraints, and add cassette/schema/service negatives for spaces, colons, controls, duplicates,
  and unselected value mismatch. Precise shared paths: crates/asb-replay/src/cassette.rs,
  crates/asb-replay/src/service.rs, crates/asb-replay/schema/v1/cassette.schema.json,
  crates/asb-replay/tests/cassette_roundtrip.rs, crates/asb-replay/tests/schema_conformance.rs,
  crates/asb-replay/tests/strict_replay.rs; generated schema only if generator changes. Shared paths
  remain untouched pending coordinator authorization. Initial unshare --mount-proc attempt failed
  with EPERM before test execution; corrected user+network namespace enabled only loopback and
  exposed the contract failure.

- 2026-09-07T13:00:00+00:00: Recorded command exit 0; command argv SHA-256
  06fce4d7dd4c1e35cb1fabe7c80d5d63299415cde979422e6592d9a0e72cc6ba.

- 2026-09-07T13:00:28+00:00: Recorded command exit 101; command argv SHA-256
  3211cbb17659455b743594d7b488023c32bf8ad124e43fb5b7a2d3f51490bd3d.

- 2026-09-07T13:00:50+00:00: Recorded command exit 0; command argv SHA-256
  93260d26ce18d4eff94eab4722e6257ef71ada08ff203c0979b7a22d73c81d9c.

- 2026-09-07T13:01:27+00:00: Recorded command exit 101; command argv SHA-256
  3211cbb17659455b743594d7b488023c32bf8ad124e43fb5b7a2d3f51490bd3d.

- 2026-09-07T13:02:00+00:00: Recorded command exit 0; command argv SHA-256
  d9750742e3a44d264dcc425fc00b2af2b39095bc58220c2e746f2038922734f9.

- 2026-09-07T13:02:34+00:00: Recorded command exit 101; command argv SHA-256
  3211cbb17659455b743594d7b488023c32bf8ad124e43fb5b7a2d3f51490bd3d.

- 2026-09-07T13:02:55+00:00: Recorded command exit 0; command argv SHA-256
  9cb38b396e41065b8a5c33bce2bc1d2be54e37e1396ed75e3e5b71fb19960f0b.

- 2026-09-07T13:03:27+00:00: Recorded command exit 101; command argv SHA-256
  3211cbb17659455b743594d7b488023c32bf8ad124e43fb5b7a2d3f51490bd3d.

- 2026-09-07T13:03:55+00:00: Recorded command exit 0; command argv SHA-256
  ad2915801c83a51a79514044dd8eb8d97109811c412962b8d44137568f565c63.

- 2026-09-07T13:04:23+00:00: Recorded command exit 101; command argv SHA-256
  3211cbb17659455b743594d7b488023c32bf8ad124e43fb5b7a2d3f51490bd3d.

- 2026-09-07T13:04:58+00:00: Recorded command exit 0; command argv SHA-256
  7a956ad5882cc5a98702757d9e0a6a0ce2c6f8f954a0d5d14408a4f4ec2d0e7f.

- 2026-09-07T13:05:25+00:00: Recorded command exit 101; command argv SHA-256
  3211cbb17659455b743594d7b488023c32bf8ad124e43fb5b7a2d3f51490bd3d.

- 2026-09-07T13:06:19+00:00: Recorded command exit 0; command argv SHA-256
  47bc0cb0a5bb4cd1c2d8027ac3528a58aa7f8e0770209cb496068d83c13517a2.

- 2026-09-07T13:06:49+00:00: Recorded command exit 101; command argv SHA-256
  3211cbb17659455b743594d7b488023c32bf8ad124e43fb5b7a2d3f51490bd3d.

- 2026-09-07T13:07:30+00:00: Recorded command exit 0; command argv SHA-256
  bc142277f63742b37270e35fd93c2132b22526bda0f19450394c9e5d5b56f7c6.

- 2026-09-07T13:08:02+00:00: Recorded command exit 101; command argv SHA-256
  3211cbb17659455b743594d7b488023c32bf8ad124e43fb5b7a2d3f51490bd3d.

- 2026-09-07T13:09:12+00:00: A second credential-free loopback capture using the same workspace and
  state root proved all normalized headers and request JSON stable except /messages/0/content: the
  only changed 174-175 byte slice in the 21,763-byte system content contains the generated
  attempt-<pid>-<nonce> private run path. Coordinator authorized an adapter-owned deterministic
  SHA-256 route-derived run directory with fail-closed exclusive creation, cleanup, and same-route
  concurrency fencing. Proposed owned paths/tests: crates/asb-agents/src/opendesk.rs unit tests for
  stable opaque route path, distinct routes, concurrent duplicate rejection, stale-directory
  rejection, no public-ID/path leakage, cleanup/reuse; crates/asb-agents/tests/replay_opendesk.rs
  real successive-attempt request parity. A third shared replay blocker is now exact: OpenDesk 0.3.5
  receives SSE while omitting request member stream; StrictReplayService rejects
  ResponseBody::Events as InvalidCassette. Proposed shared tests: cassette/service accepts exact
  text/event-stream response for an absent stream flag only under the documented compatibility rule,
  rejects wrong/missing content type and contradictory buffered/event cases, and reproduces exact
  socket bytes. Shared cassette.rs/service.rs/schema/strict/schema-test paths remain untouched.

- 2026-09-07T13:10:04+00:00: Recorded command exit 0; command argv SHA-256
  86f6426fdf3e0c8340c752b2d6937c4c1c1da6fc0ba2b136c5913b326fed531e.

- 2026-09-07T13:10:54+00:00: Recorded command exit 0; command argv SHA-256
  fcf836e01ec7212f8a9eef69230e6f79c16947432fa3122d972448db6a587595.

- 2026-09-07T13:11:13+00:00: Recorded command exit 1; command argv SHA-256
  682b1d43bcb060dc2cd7b8a62945794d6c434fe7fd0d3e52d168512af26d3f84.

- 2026-09-07T13:11:30+00:00: Recorded command exit 0; command argv SHA-256
  5ec653fdefa799f92a1ae5098090f7a6d8a1ffea3cd8e7068102011bce64314a.

- 2026-09-07T13:11:37+00:00: Recorded command exit 0; command argv SHA-256
  682b1d43bcb060dc2cd7b8a62945794d6c434fe7fd0d3e52d168512af26d3f84.

- 2026-09-07T13:11:49+00:00: Recorded command exit 101; command argv SHA-256
  ee3635faa6b035c2d5f6d25862f4822c4445fd40757721d9cc4d35ca79924552.

- 2026-09-07T13:12:04+00:00: Recorded command exit 0; command argv SHA-256
  18b36d349ce96687d1e1fdbc83175c9a37b7ac2160ac4113f9ad077243e1a235.

- 2026-09-07T13:12:23+00:00: Recorded command exit 101; command argv SHA-256
  ee3635faa6b035c2d5f6d25862f4822c4445fd40757721d9cc4d35ca79924552.

- 2026-09-07T13:12:45+00:00: Recorded command exit 0; command argv SHA-256
  44a303a8541b165e8beb19e4f45d2133e0ce9515bd29d334331d9c9cb051dfae.

- 2026-09-07T13:13:33+00:00: Recorded command exit 127; command argv SHA-256
  183c28caee2dabeabee794871ab94c75eae1e3f9914f2ec6d5a1ad1e323b39b8.

- 2026-09-07T13:14:02+00:00: Recorded command exit 0; command argv SHA-256
  5ec653fdefa799f92a1ae5098090f7a6d8a1ffea3cd8e7068102011bce64314a.

- 2026-09-07T13:14:31+00:00: Recorded command exit 101; command argv SHA-256
  3211cbb17659455b743594d7b488023c32bf8ad124e43fb5b7a2d3f51490bd3d.

- 2026-09-07T13:14:59+00:00: Authorized OpenDesk adapter repair now derives its private run
  directory as attempt- plus a domain-separated SHA-256 over fixed-size SHA-256 hashes of session
  and attempt IDs. It leaks neither public ID, is platform-independent, stable for the same route,
  distinct for different attempts, and uses exclusive DirBuilder creation so stale or concurrently
  duplicated route ownership fails with AlreadyExists; successful cancellation cleanup permits later
  reuse. Focused 10/10 OpenDesk unit tests pass, including stable/opaque/distinct roots, stale
  rejection, concurrent duplicate fencing, cancellation cleanup, and reuse. A first combined
  patch-plus-format wrapper applied the intended patch but then failed because cargo was not on that
  bash PATH; explicit pinned cargo formatting then passed. The corrected real 0.3.5 loopback-only
  capture now proves successive attempts have byte-identical request bodies and stable nonvolatile
  headers after only the temporary diagnostic span_id spelling normalization;
  StrictReplayService::new then fails exactly InvalidCassette because the request omits stream while
  the recorded wire response is SSE events. No shared runtime/schema was changed and no support
  claim is made.

- 2026-09-07T13:15:15+00:00: Recorded command exit 0; command argv SHA-256
  57188bdd289251883e0eae3f57f6f5d7cc52a477c549cf3ddee54005f97fb208.

- 2026-09-07T13:15:23+00:00: Recorded command exit 0; command argv SHA-256
  560095fd5c069dc58b07c1d794b59de71e498e998af272953db733358e953799.

- 2026-09-07T13:17:00+00:00: Recorded command exit 0; command argv SHA-256
  324f009f685495f024cccb54239db85ccb9dff3e6b6d042379089453f01b28e9.

- 2026-09-07T13:17:18+00:00: Recorded command exit 0; command argv SHA-256
  a870f916ef3543e39adf68f2df32585fc56b05ee8c2a4299d4367209b5d6452d.

- 2026-09-07T13:17:44+00:00: Recorded command exit 101; command argv SHA-256
  3211cbb17659455b743594d7b488023c32bf8ad124e43fb5b7a2d3f51490bd3d.

- 2026-09-07T13:22:09+00:00: Recorded command exit 0; command argv SHA-256
  783cd3c226a55576bfc59409e9135a611eaed954275c131b1857fcc324942f57.

- 2026-09-07T13:22:32+00:00: Recorded command exit 0; command argv SHA-256
  a870f916ef3543e39adf68f2df32585fc56b05ee8c2a4299d4367209b5d6452d.

- 2026-09-07T13:23:08+00:00: Recorded command exit 101; command argv SHA-256
  127ecc29cb139c32c0f45c73a7e5eefd03be18290ec2aca32c08ecbd8a42feb6.

- 2026-09-07T13:23:36+00:00: Recorded command exit 0; command argv SHA-256
  07af1c601275f55cbceb8ad22829cdd53bca7682b773a0e601ac58d309afc4dd.

- 2026-09-07T13:24:06+00:00: Recorded command exit 101; command argv SHA-256
  127ecc29cb139c32c0f45c73a7e5eefd03be18290ec2aca32c08ecbd8a42feb6.

- 2026-09-07T13:24:50+00:00: Changed isolated evidence after the authorized deterministic route fix:
  the first instrumented real rerun failed earlier because the test compared the initial
  title-generation request with the later retried tool request. The focused oracle now locates the
  unique 429 interaction and requires its immediately following request body to be byte-identical;
  that correction is fixture-only and the rerun then again reached StrictReplayService::new and
  failed exactly InvalidCassette for absent stream plus event response. The same run proves pinned
  OpenDesk 0.3.5 performs at least one GET model-catalog probe before completion; successive
  captures require the same nonzero probe count. This is a third shared compatibility boundary
  because StrictReplayService currently admits only POST /v1/chat/completions. Proposed shared path
  is crates/asb-replay/src/service.rs with tests in crates/asb-replay/tests/strict_replay.rs: bound
  and serve exact GET /v1/models and /v1/models/{validated-model} fixtures only when explicitly
  recorded/versioned, reject arbitrary paths/query/control/oversize/unrecorded models, and ensure
  catalog traffic neither consumes nor reorders completion interactions. Existing span_id
  paths/tests remain cassette.rs, service.rs, cassette.schema.json, cassette_roundtrip.rs,
  schema_conformance.rs, strict_replay.rs. The isolated test scratch no longer contains a committed
  host path and unrelated OpenCode redaction selectors were removed. No shared runtime/schema was
  changed and support remains blocked.

- 2026-09-07T13:25:23+00:00: Heartbeat by replay_20260906.

- 2026-09-07T13:38:53+00:00: Fresh reconcile/snapshot at state 9316970d verified AR-0507 remains the
  sole replay_20260906 claim, head 68345a631a2c865a9e339ade574c0b53ec73367a with only isolated
  replay_opendesk.rs untracked, valid lease through 16:25Z, and no OpenDesk/cargo test process.
  AR-0516 now durably contains the three shared compatibility requirements and is planned/unclaimed
  for serialized implementation. No further sound isolated execution can cross the
  StrictReplayService constructor boundary without duplicating or weakening that shared repair;
  preserve the exact fixture and avoid repeated expected-failure runs. After AR-0516 merges: rebase
  exact main, remove temporary span_id spelling normalization, capture model-catalog GET
  interactions rather than side-serving them, prove strict ordering and byte-exact SSE, then run
  native cancel/malformed/network-denial plus all full gates.

- 2026-09-07T14:49:19+00:00: Recorded command exit 0; command argv SHA-256
  d55314f2408b36a09f3dec1c1d6183e5b0e2c532da213ea1a30265a06f4bee14.

- 2026-09-07T14:51:22+00:00: Recorded command exit 1; command argv SHA-256
  056697e936f24e75ee717cc5a8839ce99bf1cfc67b880c21fdaa7cdeaad5f78a.

- 2026-09-07T14:52:28+00:00: Recorded command exit 0; command argv SHA-256
  b1ef1f2488a82f51e79414e0ca1461c78d10b87ad70b16ac5d104cf935d6c185.

- 2026-09-07T14:53:04+00:00: Recorded command exit 0; command argv SHA-256
  b41ecd724cbfa41dd792121a4e7c162469d9fd7073dac00943f36c6a98fc9fe4.

- 2026-09-07T14:53:35+00:00: Recorded command exit 1; command argv SHA-256
  136b3c022223f6141b59f5ac77158c58e8f8d7a9f9d3ddc7f5478f06903040de.

- 2026-09-07T14:53:42+00:00: Heartbeat by replay_20260906.

- 2026-09-07T14:54:27+00:00: Recorded command exit 1; command argv SHA-256
  4ba63b2d0d4c7e31155c64a8bbb7cf7d1ff73cdce432dac89aee20d75512bc18.

- 2026-09-07T14:54:58+00:00: Recorded command exit 0; command argv SHA-256
  0ebfb1eccd34130548ab7320b91e21fa7d555a39a87e7a2dd683015c0a092521.

- 2026-09-07T14:55:28+00:00: Recorded command exit 0; command argv SHA-256
  d7f90f337672124eefa9dd82e4734c952dc539cc11e0c00bd2ab60f757eaebfc.

- 2026-09-07T14:55:35+00:00: Recorded command exit 0; command argv SHA-256
  a870f916ef3543e39adf68f2df32585fc56b05ee8c2a4299d4367209b5d6452d.

- 2026-09-07T14:56:22+00:00: Recorded command exit 0; command argv SHA-256
  127ecc29cb139c32c0f45c73a7e5eefd03be18290ec2aca32c08ecbd8a42feb6.

- 2026-09-07T14:57:44+00:00: Recorded command exit 0; command argv SHA-256
  30963768f4630d63b48365227684023929e34dfb5b647bb378c92b80b8278e1f.

- 2026-09-07T14:57:51+00:00: Recorded command exit 1; command argv SHA-256
  783cd3c226a55576bfc59409e9135a611eaed954275c131b1857fcc324942f57.

- 2026-09-07T14:58:00+00:00: Recorded command exit 0; command argv SHA-256
  a870f916ef3543e39adf68f2df32585fc56b05ee8c2a4299d4367209b5d6452d.

- 2026-09-07T14:58:18+00:00: Recorded command exit 0; command argv SHA-256
  ecb997c7813cdcde63ad19178b336eff8ebbd2e8f93493973b734dfabf1cc982.

- 2026-09-07T14:58:24+00:00: Recorded command exit 0; command argv SHA-256
  783cd3c226a55576bfc59409e9135a611eaed954275c131b1857fcc324942f57.

- 2026-09-07T14:59:31+00:00: Recorded command exit 0; command argv SHA-256
  518e55d32d8079921dbed26f807bc13edd329b846290dea2941155ca44413cb5.

- 2026-09-07T15:00:26+00:00: Recorded command exit 0; command argv SHA-256
  127ecc29cb139c32c0f45c73a7e5eefd03be18290ec2aca32c08ecbd8a42feb6.

- 2026-09-07T15:00:57+00:00: Recorded command exit 0; command argv SHA-256
  633db6a8b6b9d0ebe4cc319749a6ac5d007a117fcc298b4dd4507d2e67df0a54.

- 2026-09-07T15:01:04+00:00: Recorded command exit 0; command argv SHA-256
  783cd3c226a55576bfc59409e9135a611eaed954275c131b1857fcc324942f57.

- 2026-09-07T15:01:10+00:00: Recorded command exit 0; command argv SHA-256
  fce881067e2b528dd0b55565501385a0b1aa68314995d76714c4c19d5d1e895a.

- 2026-09-07T15:01:52+00:00: Recorded command exit 0; command argv SHA-256
  127ecc29cb139c32c0f45c73a7e5eefd03be18290ec2aca32c08ecbd8a42feb6.

- 2026-09-07T15:02:52+00:00: Recorded command exit 0; command argv SHA-256
  44a303a8541b165e8beb19e4f45d2133e0ce9515bd29d334331d9c9cb051dfae.

- 2026-09-07T15:02:59+00:00: Recorded command exit 0; command argv SHA-256
  dd962d510f9ec6270c43ffb600462c647ad7782adc0ed97ded2ff0dda63389e5.

- 2026-09-07T15:03:45+00:00: Recorded command exit 0; command argv SHA-256
  899d57ac43fa9a874bf5886b0ca38f3e3dc5a5134890b893988cd229b8c80db0.

- 2026-09-07T15:03:53+00:00: Recorded command exit 0; command argv SHA-256
  868061d27094d423b0f35d142e3021361d9d59261438ca13d6ad3a434c778cb2.

- 2026-09-07T15:04:17+00:00: Recorded command exit 0; command argv SHA-256
  841cabc5d5ae6953228d0380e0f0ccfef48d0d419bc369485e901bb4c8cd98f4.

- 2026-09-07T15:05:06+00:00: Recorded command exit 0; command argv SHA-256
  a114940c8e24b317101278b33c2759cc7b6b97eeb0475c77d7f1181cb2be20ab.

- 2026-09-07T15:05:28+00:00: Recorded command exit 0; command argv SHA-256
  95fefd33b379981f95026df39c8e9ebe6db676cf664d39702b0aa41daf185f0b.

- 2026-09-07T15:05:42+00:00: Recorded command exit 0; command argv SHA-256
  cf7f2fe022a3674731adf51820e3fddb62b696518370594ef61e8223b8d34344.

- 2026-09-07T15:06:03+00:00: Recorded command exit 0; command argv SHA-256
  e5be65a1438b50e056159b3c6eca2aa6bca33bd301e1c3307251d9e227f5af62.

- 2026-09-07T15:06:36+00:00: Recorded command exit 0; command argv SHA-256
  bf935ed1f426351599e011358215079c0af07730be3e16b0f215336fcd587e36.

- 2026-09-07T15:06:47+00:00: Recorded command exit 0; command argv SHA-256
  a6c606224ee395db5f25c6f032d37a75174ea6184d8d627d10d0ed00cdd2ce66.

- 2026-09-07T15:07:40+00:00: Recorded command exit 0; command argv SHA-256
  fb8f740089e49df2380025144a463c997d66c42a004d0030582f824606c2d79b.

- 2026-09-07T15:07:57+00:00: Recorded command exit 0; command argv SHA-256
  5337a656f847b5498f5a4277b6c8c5e272b2fc61e9dc48a3ddc00277d1a01da8.

- 2026-09-07T15:08:20+00:00: Recorded command exit 0; command argv SHA-256
  cfb9f92c4a20631b6f064fac665e26c4e0b5d4334a35a006d81b3484cfcdb043.

- 2026-09-07T15:08:26+00:00: Recorded command exit 0; command argv SHA-256
  be649150cab90864aa99c6d60e6d9a3a648fafdaba1d2da547843f2f9e129fd6.

- 2026-09-07T15:08:32+00:00: Recorded command exit 0; command argv SHA-256
  6e96ecf992245eb44a9980b6c1326b5f61ea39fd86ae89c92b9475a7fdc4d57e.

- 2026-09-07T15:08:50+00:00: Recorded command exit 0; command argv SHA-256
  86acde0d235e68572fd270d0b276f1ff2e379dc9706cb483f1806a321ad7176c.

- 2026-09-07T15:08:59+00:00: Recorded command exit 1; command argv SHA-256
  8a8bd5ebde72e69413e7f8718535b3deb39c9f3ed078a5434c78865e9a5c98d9.

- 2026-09-07T15:09:49+00:00: Recorded command exit 0; command argv SHA-256
  5de25e30de59651dc01ee0cd61d31d252b41a0b2aaf2bdfd99c943e40f2d53f0.

- 2026-09-07T15:10:39+00:00: AR-0507 exact-tree candidate is
  24a5519ef006c063f3a8d6e81d0928f2e9e986f9, tree 96f01bd39cd5e75a70d3618cec55e603b9643d38, two-path
  scope over exact signed main 8eff6f95: adapter route-root repair plus replay_opendesk integration.
  Both commits verify with the allowed SSH signer and exact Martin Beck DCO; diff-check, clean
  worktree, scope and privacy scans pass; exact-range Gitleaks scanned 2 commits/~38 KB with no
  leaks. Pinned OpenDesk 0.3.5 and Node 26.3.0 ran in a user+network namespace exposing only
  loopback: record plus strict offline replay, exact 18 catalog GET sequence/framing, real span_id
  redaction, absent-stream SSE bytes, one 429 exact retry, tool-call causality, graded trajectory
  parity, cancellation and state cleanup all passed in 18.43s after final assertions. Focused
  adapter units 10/10 and malformed cassette integration 1/1 pass. Exact-tree fmt, workspace
  all-target Clippy -D warnings, full locked workspace tests, rustdoc -D warnings, release build,
  formal workspace tests, cargo-deny, refreshed cargo-audit, actionlint, zizmor, repository policy,
  and negative quality fixtures pass. Coverage passes at 91.82% workspace lines, 98.44% asb-protocol
  lines and 97.66% asb-replay lines. Initial negative-fixture invocation passed through
  documentation checks then failed only because cargo was absent from PATH; corrected pinned PATH
  rerun passed every positive/negative fixture. No cassette/raw prompt/response/private
  path/transcript is committed. Real execution is proven only on Linux x86_64; aarch64 remains
  build/test CI, not a native OpenDesk runtime claim.

- 2026-09-07T15:11:24+00:00: Recorded command exit 0; command argv SHA-256
  e4608873677cf13faf8a990be171cc4f15266384d639824293265a6b9dfcf215.

- 2026-09-07T15:11:31+00:00: Recorded command exit 0; command argv SHA-256
  e82fbde8e67a0edf7f8860760c847520bad0a8f6531c2b99fc413647a5368fd3.

- 2026-09-07T15:11:45+00:00: Recorded command exit 0; command argv SHA-256
  3efc46ccfe625b207d5da3a76090be5783eae6badeb84a97c13d68eb2e48c92a.

- 2026-09-07T15:11:52+00:00: Recorded command exit 0; command argv SHA-256
  e4608873677cf13faf8a990be171cc4f15266384d639824293265a6b9dfcf215.

- 2026-09-07T15:12:19+00:00: Recorded command exit 0; command argv SHA-256
  b3be88d1b9c2f4fc72a216eb48b2fd7503097ed71929c72e9e3233f1e14e284a.

- 2026-09-07T15:12:37+00:00: Recorded command exit 0; command argv SHA-256
  4b4732b03a052f692705af3385bdd3f6e0d9d42086c87f2c98e946f9aa380d17.

- 2026-09-07T15:13:33+00:00: Recorded command exit 0; command argv SHA-256
  034ce7bafbb88425fb989f7224fb7f6a022cfbc944be11c09511ff8b612ceb65.
