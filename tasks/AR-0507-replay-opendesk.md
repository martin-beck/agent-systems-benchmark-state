---
{
  "branch": "feature/replay-opendesk",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T15:45:14+00:00",
  "depends_on": [
    "AR-0302",
    "AR-0503",
    "AR-0504",
    "AR-0401"
  ],
  "id": "AR-0507",
  "next_action": "Await serialized shared replay compatibility repair for legal underscore headers and absent-stream SSE; retain cleanly tested adapter route-root fix and isolated real conformance test.",
  "observed_branch": "feature/replay-opendesk",
  "observed_dirty": 1,
  "observed_head": "68345a631a2c865a9e339ade574c0b53ec73367a",
  "owner": "replay_20260906",
  "plan": "../plans/AR-0507.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify replay conformance for OpenDesk.",
  "task_revision": 61,
  "title": "Qualify OpenDesk replay",
  "updated_at": "2026-09-07T13:22:09+00:00",
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
