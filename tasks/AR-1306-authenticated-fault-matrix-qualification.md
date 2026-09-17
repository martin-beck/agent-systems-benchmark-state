---
{
  "branch": "feature/ar-1306-authenticated-fault-matrix-qualification",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T22:42:24+00:00",
  "depends_on": [
    "AR-1300",
    "AR-1287"
  ],
  "id": "AR-1306",
  "next_action": "PR #222 exact head 910af9a3c380ecf035f839460f3304ccb8159e50 has all 12 CI checks green, but independent review blocks acceptance: run_supervised_fault now allocates authenticated ReplayRelay yet never starts/accepts a StrictReplayService connection, and provider/descendant egress cases assert only nonzero exit rather than cause-specific denial. Add executable matrix-level authenticated positive/parity and distinct cause assertions, then publish a new signed head and rerun CI.",
  "observed_branch": "feature/ar-1306-authenticated-fault-matrix-qualification",
  "observed_dirty": 0,
  "observed_head": "1ab79c1faaff483bd419ca4d2d184201b8335566",
  "owner": "codex-ar1306-auth-listener-20260917",
  "plan": "../plans/AR-1306.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify the real authenticated strict-replay service and fault matrix missing from PR #221.",
  "task_revision": 42,
  "title": "Authenticated strict-replay fault-matrix qualification",
  "updated_at": "2026-09-17T22:16:12+00:00",
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
