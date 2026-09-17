---
{
  "branch": "feature/ar-1306-authenticated-fault-matrix-qualification",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T23:56:48+00:00",
  "depends_on": [
    "AR-1300",
    "AR-1287"
  ],
  "id": "AR-1306",
  "next_action": "Repair implementation paused after two failed patch commands: exit 2 because apply_patch received no stdin through handoffctl; exit 1 because attempted Python wrapper preserved literal newline escapes and was invalid syntax. No product files changed. Use bounded, reviewed handoffctl mutation method, then rerun focused tests before commit.",
  "observed_branch": "feature/ar-1306-authenticated-fault-matrix-qualification",
  "observed_dirty": 1,
  "observed_head": "910af9a3c380ecf035f839460f3304ccb8159e50",
  "owner": "codex-ar1306-auth-listener-20260917",
  "plan": "../plans/AR-1306.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify the real authenticated strict-replay service and fault matrix missing from PR #221.",
  "task_revision": 50,
  "title": "Authenticated strict-replay fault-matrix qualification",
  "updated_at": "2026-09-17T21:59:43+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1306-authenticated-fault-matrix-qualification"
}
---

## AR-1306

Implement the narrowly scoped ASB follow-on required by the independent review of PR #221 and
blocked AR-1301. The current fault helper does not prove a real `StrictReplayService`/relay
listener, positive authenticated identity/response parity, or cause-specific provider and
descendant egress denial. This AR owns those missing executable fixtures and their approved KVM
qualification evidence.

AR-1301 is the review predecessor, while AR-1300 and AR-1287 are hard runtime dependencies. The
predecessor is deliberately recorded in this task's scope rather than as a hard dependency to avoid
an impossible AR-1301 -> AR-1306 -> AR-1301 cycle. ASB only: do not change asb-tui, handoffctl,
credentials, live providers, or unrelated coordinator implementation.

Completion requires a real runtime-owned service/listener positive path, exact authenticated
cassette identity and response parity, distinct provider/descendant egress-denial causes, all
remaining lifecycle faults, bounded cleanup, sanitized provenance-bound evidence, signed+DCO
publication, independent review, green exact-head CI, protected merge and post-merge verification.

- 2026-09-17T21:31:46+00:00: Dependencies AR-1300 and AR-1287 are done; promote the real
  authenticated fault-matrix successor.

- 2026-09-17T21:32:09+00:00: Claimed by codex-ar1306-auth-listener-20260917.

- 2026-09-17T21:32:25+00:00: Recorded command exit 0; command argv SHA-256
  14925a15c4fe5ba5963acec8c3090fe2ca9ca1056d727a54d0042009cae057a2.

- 2026-09-17T21:34:09+00:00: Recorded command exit 128; command argv SHA-256
  a1d94ce312c5b430d26e3e641bea256dc176743e4ed993ef53757d7c6561be6f.

- 2026-09-17T21:34:31+00:00: Recorded command exit 0; command argv SHA-256
  c1d752b5a0735f834ef0bd43f0c8229908e54cf34bc2eabb9452d73fd8bd5780.

- 2026-09-17T21:34:45+00:00: Recorded command exit 0; command argv SHA-256
  6f51030fcf3d8503d756059362fedf4ee980de09d8ad5ef62bd0b2948c0e5c2e.

- 2026-09-17T21:35:10+00:00: Recorded command exit 0; command argv SHA-256
  d9cb9225467d2352b997b2d36975ca3ac6aff5ab46113190af547a0a2a0178d1.

- 2026-09-17T21:35:26+00:00: Recorded command exit 1; command argv SHA-256
  a772f749e37282ce900b60b5c7c9909360b075c1dd03702a6f39cb7a7fb5d6c3.

- 2026-09-17T21:35:46+00:00: Recorded command exit 0; command argv SHA-256
  379b0aaa17109cd9bd7d425c10655c6549ec8983aab554e34bf218cc90d0a7c1.

- 2026-09-17T21:36:10+00:00: Recovered the 21:35:26 exit-1: the initial cargo invocation passed two
  test filters, but cargo test accepts one TESTNAME and rejected the second as an unexpected
  argument. Correct rerun used the single prefix filter native_supervisor_, and passed 3/3:
  authenticated negative matrix, fault matrix, and real cassette HTTP forwarding. No product gate
  failure.

- 2026-09-17T21:36:34+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-17T21:36:52+00:00: Recorded command exit 0; command argv SHA-256
  10772469dd0ddaf5069a4685da5064075f92454b37971ddc36dadc60a7e22e22.

- 2026-09-17T21:37:10+00:00: Recorded command exit 0; command argv SHA-256
  97ee782321facf1df64b14b3500c62b04b8b48c9904b8abb83044328a904f4b2.

- 2026-09-17T21:37:37+00:00: Recorded command exit 0; command argv SHA-256
  e0e814b48e1909b50ccabd4bb0699237298e6f32cf543810dd57274837794bd9.

- 2026-09-17T21:37:52+00:00: Recorded command exit 0; command argv SHA-256
  9ceeabdfd43099b6aecf1259deea68d9d6514939a9b2b2cf5cf11f2969189b6f.

- 2026-09-17T21:38:18+00:00: Implementation candidate 910af9a: fault matrix now uses ReplayRelay
  rather than an unauthenticated raw UnixListener. Focused 3/3, full asb-runtime tests, fmt and
  clippy pass. No asb-tui or handoffctl changes.

- 2026-09-17T21:38:28+00:00: Recorded command exit 0; command argv SHA-256
  19512d543cbca16558243694b400506ff05b53a567fdc394e8f00a631ebcc519.

- 2026-09-17T21:38:51+00:00: Recorded command exit 0; command argv SHA-256
  ef85fb183c77c7e3b1e0160721ea3cfb7744ba74dfae7b503d20709f6c42d3ee.

- 2026-09-17T21:39:48+00:00: Recorded command exit 0; command argv SHA-256
  21bb067315f65c46cd41da23bbb54aaab64ee2308e46515053bbe240e08914a0.

- 2026-09-17T21:40:23+00:00: Recorded command exit 127; command argv SHA-256
  5cdaf45d72ef36a99b39aaa63b92c7a02c7964d16cc57fd77ec472b41780879a.

- 2026-09-17T21:41:01+00:00: Recorded command exit 0; command argv SHA-256
  2222b35d93cfb76ad4c18c76f1d43461b6f70e1b42958891d5abfa84b17eee3c.

- 2026-09-17T21:41:28+00:00: Recorded command exit 0; command argv SHA-256
  d2d4b48386618890ba2aebf7e26cdfcd28b02930dd6ec7bd12524a826acd6501.

- 2026-09-17T21:41:51+00:00: Recorded command exit 0; command argv SHA-256
  3ec9aeb34fd0df436d625673333a87d330c2a13ca70fff36c4c7a2bd2406e4da.

- 2026-09-17T21:42:07+00:00: Recorded command exit 0; command argv SHA-256
  345de5b2da25e9b37d7563eb7df85bd1a31e8c9322cf708237be1d5a076b3001.

- 2026-09-17T21:42:24+00:00: Heartbeat by codex-ar1306-auth-listener-20260917.

- 2026-09-17T21:42:37+00:00: Published PR #222 after clean exact-head review; signed/DCO candidate
  and all local workspace gates passed. Exact-head hosted checks now running.

- 2026-09-17T21:42:49+00:00: Recorded command exit 8; command argv SHA-256
  70f9830c04f328234bb27442bd2464edd9e1aa80f655ba60d4c71b02409306eb.

- 2026-09-17T21:43:39+00:00: Recorded command exit 8; command argv SHA-256
  70f9830c04f328234bb27442bd2464edd9e1aa80f655ba60d4c71b02409306eb.

- 2026-09-17T21:43:54+00:00: Recorded command exit 8; command argv SHA-256
  70f9830c04f328234bb27442bd2464edd9e1aa80f655ba60d4c71b02409306eb.

- 2026-09-17T21:44:05+00:00: Exact-head CI monitored: 6 checks passed, 6 remain pending, no
  failures. PR is clean and unchanged at signed candidate head.

- 2026-09-17T21:44:15+00:00: Recorded command exit 0; command argv SHA-256
  3e4db653e5225bc40a001949e7ffcf89be0311192c38d74ed08e0edf578ddc6f.

- 2026-09-17T21:49:46+00:00: Recorded command exit 0; command argv SHA-256
  70f9830c04f328234bb27442bd2464edd9e1aa80f655ba60d4c71b02409306eb.

- 2026-09-17T21:50:07+00:00: Monitored PR #222 exact-head checks to terminal: all 12 passed,
  including emulated-aarch64. No reviewer approval yet; merge remains blocked pending independent
  review.

- 2026-09-17T21:54:32+00:00: Independent acceptance review: BLOCK. The one-file diff removes raw
  UnixListener, but the fault matrix still does not exercise a service/listener positive path;
  existing separate positive test does not bind matrix cases. Provider/descendant egress cases only
  assert nonzero exit, so unrelated failure could satisfy them. All 12 hosted checks are green, but
  this is a substantive acceptance gap; do not merge.

- 2026-09-17T21:55:58+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-17T21:56:48+00:00: Heartbeat by codex-ar1306-auth-listener-20260917.

- 2026-09-17T21:56:54+00:00: Recorded command exit 1; command argv SHA-256
  413d8cfd8985157151fc7fe5325e3a83caa44052436e65b6a51ca5cecf1bec69.

- 2026-09-17T21:57:20+00:00: Recorded exact repair-tool failures: apply_patch invocation via
  handoffctl had no stdin (exit 2); Python subprocess wrapper had syntax error from escaped newlines
  (exit 1). Working tree remains at signed 910af9a; no source mutation occurred.

- 2026-09-17T21:57:35+00:00: Recorded command exit 0; command argv SHA-256
  7ffaca487c8c23bde2f0805b3e20381b5d056946fefa174c76d596424982dc27.

- 2026-09-17T21:58:05+00:00: Recorded command exit 0; command argv SHA-256
  08a7a3e36743fed63d32305d5ff41c121406a2f7acb002ea97634373b46b442c.

- 2026-09-17T21:58:33+00:00: Recorded command exit 0; command argv SHA-256
  58dbe59a808992086bab07b3b2cf79c6db23ba4d00aadbc811addab1176a458b.

- 2026-09-17T21:58:48+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-17T21:58:58+00:00: Recorded command exit 0; command argv SHA-256
  264fcedabcf0d93cdabd2200bdda093ee9401500fb70f47a7ef269009f979713.

- 2026-09-17T21:59:20+00:00: Recorded command exit 0; command argv SHA-256
  2d59387dc86f926c7f5f779a537514d92accf52f6e22c573ffbec0cfbb8a213b.

- 2026-09-17T21:59:43+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.
