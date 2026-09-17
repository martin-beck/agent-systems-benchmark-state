---
{
  "branch": "feature/ar-1306-authenticated-fault-matrix-qualification",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T22:32:09+00:00",
  "depends_on": [
    "AR-1300",
    "AR-1287"
  ],
  "id": "AR-1306",
  "next_action": "Refactor the authenticated relay/service fixture into the complete fault matrix: retain ReplayRelay generation authentication, route positive cases through StrictReplayService::serve_authenticated_connection, and add cause-specific provider/descendant denial assertions with bounded cleanup. Then run repeated focused matrix and full locked ASB gates before signed review/publication.",
  "observed_branch": "feature/ar-1306-authenticated-fault-matrix-qualification",
  "observed_dirty": 1,
  "observed_head": "18698e48ce86229a387740fdd690dd79866e1755",
  "owner": "codex-ar1306-auth-listener-20260917",
  "plan": "../plans/AR-1306.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify the real authenticated strict-replay service and fault matrix missing from PR #221.",
  "task_revision": 17,
  "title": "Authenticated strict-replay fault-matrix qualification",
  "updated_at": "2026-09-17T21:37:37+00:00",
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
