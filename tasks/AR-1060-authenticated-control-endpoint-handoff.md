---
{
  "branch": "feature/authenticated-control-endpoint-handoff",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T08:36:18+00:00",
  "depends_on": [
    "AR-1022",
    "AR-1023"
  ],
  "id": "AR-1060",
  "next_action": "Obtain immutable review of the frozen SOCK_SEQPACKET framing, then implement only the ASB authenticated-generation producer and broker state machine; keep launch and consumer behavior in AR-1024/1025.",
  "observed_branch": "feature/authenticated-control-endpoint-handoff",
  "observed_dirty": 0,
  "observed_head": "10a353e0342ced88dabbebac7d1da5b0f2511d84",
  "owner": "codex-ar1060-asb-endpoint-provider-20260911",
  "plan": "../plans/AR-1060.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Hand the standalone frontend an authenticated ASB control connection without exposing endpoint paths.",
  "task_revision": 23,
  "title": "Add authenticated control endpoint handoff",
  "updated_at": "2026-09-11T06:02:18+00:00",
  "worktree_key": "agent-systems-benchmark-authenticated-control-endpoint-handoff"
}
---

Define and implement the non-UI boundary that connects the separately installed `asb-tui` frontend
to the authoritative ASB control service. ASB owns endpoint discovery, connection provisioning and
reconnection authority. The standalone repository owns transport consumption and independent peer
re-authentication. Prefer a safely transferred, already-connected Unix descriptor; never disclose
raw socket paths or endpoints through environment variables, arguments, public responses, logs or
diagnostics.

This AR coordinates two repository-local implementation halves with separate commits, tests,
immutable reviews and protected merges. It assigns no renderer, Ratatui, Crossterm, navigation,
widget, screen or application-shell implementation to ASB. AR-1024 remains open and AR-1025 remains
planned until their full dependency sets are done.

- 2026-09-11T05:28:38+00:00: Created under the coordinator lock after confirming AR-1060 is the
  next free identifier. AR-1022 and AR-1023 are durably done; AR-1024 and AR-1025 retain their
  existing status and owner while gaining this prerequisite.

- 2026-09-11T05:28:38+00:00: Claimed by
  codex-ar1060-control-endpoint-handoff-state-20260911 for state-only task definition and graph
  validation; release OPEN/unowned after the signed state commit.

- 2026-09-11T05:32:00+00:00: Initial schema command exited 1 because the base Python environment
  lacks `jsonschema`; its automatic result reconciliation then detected the concurrently committed
  duplicate AR-1060 node. Preserved that commit in history, removed only its colliding task in this
  authorized successor, and restored AR-1010 byte-for-byte to origin/main so its dependency does not
  point at this unrelated endpoint-handoff task.

- 2026-09-11T05:32:22+00:00: Recorded command exit 1; command argv SHA-256
  f42ab07ce4e4d1a4d356a15458f58b78063c28c29356959d63aadf8968d17b7a.

- 2026-09-11T05:32:55+00:00: Recorded command exit 0; command argv SHA-256
  3adf945d41e31464bc901f1cb355cd00146cd5cb01e2faa01ac63df19394e675.

- 2026-09-11T05:33:14+00:00: Recorded command exit 0; command argv SHA-256
  87414d9a6590bb528ce5f6f01fce65456f2534893bc171d39be2cbd41c120d17.

- 2026-09-11T05:33:31+00:00: Recorded command exit 0; command argv SHA-256
  2a5f18a018eac4703aa065a1484ea3190893d02da0a4a6cf358510cff78afa0c.

- 2026-09-11T05:33:52+00:00: Recorded command exit 0; command argv SHA-256
  c4a330b7ccefa4b6288c65da978caef1065aa1fb108be3ca3156284cafbdd15f.

- 2026-09-11T05:34:20+00:00: Recorded command exit 1; command argv SHA-256
  5769dcc760f79949f509a5b6662af5819e2f3255176c0e792023b37fefd4f716.

- 2026-09-11T05:34:39+00:00: Classified the latest exit 1 as the expected zero-match result from the
  privacy scan: no private checkout path, host/address, password, credential assignment or token
  assignment appears in the six owned task/plan files. Earlier full schema validation also exposed
  only pre-existing repository-wide checkpoint and AR-1043 next_action violations; targeted strict
  schema validation of AR-1024, AR-1025 and AR-1060 passed.

- 2026-09-11T05:35:04+00:00: State-only AR definition complete. AR-1060 is the P0 non-UI
  cross-repository contract; it depends only on done AR-1022/AR-1023. AR-1024 remains OPEN/unowned
  and AR-1025 remains PLANNED/unowned, both with one-way AR-1060 dependencies. Unique-ID, targeted
  strict schema, graph/render, privacy, reconcile and live doctor checks passed; implementation
  awaits a separately claimed worker and repository-local immutable reviews.

- 2026-09-11T05:36:18+00:00: Claimed by codex-ar1060-asb-endpoint-provider-20260911.

- 2026-09-11T05:36:37+00:00: Recorded command exit 0; command argv SHA-256
  6a50527cfbf9c1b1a7134978d79d1c1d487a995e9ac4a7df2ae767403992cd6f.

- 2026-09-11T05:46:24+00:00: Recorded command exit 1; command argv SHA-256
  b30530402bd8595b97dc1d6ae429774e1a0d1619552ef474bb8ce31a1a724450.

- 2026-09-11T05:50:32+00:00: Recorded command exit 0; command argv SHA-256
  f863cdeb4914ccf6c503db659344a2a79b87e1d9ed0b1e744ddcd14ea2e2bef4.

- 2026-09-11T05:50:50+00:00: Recorded command exit 0; command argv SHA-256
  49723ec677ff4d68e7414ff3e327399d50b4aeb6f504a404c432ec5a0bbfc70f.

- 2026-09-11T05:51:10+00:00: Recorded command exit 0; command argv SHA-256
  5e5ffc5446b96baebf2bdd9959d49e029211155440bf2076151c1897c9029dfc.

- 2026-09-11T05:51:33+00:00: Pre-freeze review incorporated before product mutation. Removed unsafe
  arbitrary fixed-FD adoption, CLOEXEC clearing, proc-fd socket reopening, socketpair peer-identity
  claims, PID authority/signaling, launch-command acceptance and application continuity ownership.
  Froze child-stdin SOCK_SEQPACKET possession authority, exact request/reply plus one SCM_RIGHTS
  descriptor, monotonic deadlines/retry ceilings, probe negotiation plus a second
  same-UID/PID/starttime unnegotiated stream, typed AuthenticatedGeneration and post-adoption
  validator seam, receiver shape/CMSG_CLOEXEC checks, explicit epoch/sequence no-wrap ordering and
  changed-runner behavior owned by AR-1025. Product worktree is clean at 10a353e.

- 2026-09-11T05:51:40+00:00: Recorded command exit 0; command argv SHA-256
  2a5f18a018eac4703aa065a1484ea3190893d02da0a4a6cf358510cff78afa0c.

- 2026-09-11T05:56:18+00:00: Recorded command exit 0; command argv SHA-256
  49723ec677ff4d68e7414ff3e327399d50b4aeb6f504a404c432ec5a0bbfc70f.

- 2026-09-11T05:56:30+00:00: Recorded command exit 0; command argv SHA-256
  c5b9bd47d141c50b39e7edb2f72d51e1fd374eebafb3f6379c9433a204406bf7.

- 2026-09-11T06:02:18+00:00: Recorded command exit 0; command argv SHA-256
  49723ec677ff4d68e7414ff3e327399d50b4aeb6f504a404c432ec5a0bbfc70f.
