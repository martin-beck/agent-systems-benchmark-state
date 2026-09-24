---
{
  "branch": "ci/ar-1216-tutorial-freshness",
  "checkpoint_commit": "f387877be93e890123404bad3dc1ba213ea34db6",
  "claim_expires": "2026-09-25T00:57:14+00:00",
  "depends_on": [
    "AR-1210",
    "AR-1211",
    "AR-1212",
    "AR-1213",
    "AR-1214",
    "AR-1215"
  ],
  "id": "AR-1216",
  "next_action": "Open reviewed PR from ci/ar-1216-tutorial-freshness; run exact-head CI and seven post-merge workflows.",
  "observed_branch": "ci/ar-1216-tutorial-freshness",
  "observed_dirty": 0,
  "observed_head": "f387877be93e890123404bad3dc1ba213ea34db6",
  "owner": "ar1216-tutorial-freshness-luna56",
  "plan": "../plans/AR-1216.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Continuously keep ASB tutorial commands and steps syntactically current.",
  "task_revision": 19,
  "title": "ASB tutorial freshness CI and documentation qualification",
  "updated_at": "2026-09-24T22:05:48+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1216"
}
---

Implement the linked CI gate. It validates syntax and fixtures only and must never execute a
tutorial command or require a provider/LLM connection.

- 2026-09-24T21:55:48+00:00: All tutorial contract predecessors AR-1210 through AR-1215 are durably
  done; promote repository-wide freshness CI implementation.

- 2026-09-24T21:57:14+00:00: Claimed by ar1216-tutorial-freshness-luna56.

- 2026-09-24T21:57:34+00:00: Recorded command exit 128; command argv SHA-256
  cf431012bc31a84f18ffdc3f1ea1953efdb3d26bc2be4d23aafaba616d1a8841.

- 2026-09-24T21:57:52+00:00: Recorded command exit 128; command argv SHA-256
  44ecb4cb5cce1371b95b32254c3a0807a784d0a4b6d359bf416ee25627ba0d4a.

- 2026-09-24T21:58:13+00:00: Recorded command exit 0; command argv SHA-256
  2920af4f1fc77762c48a8d794dbe2818fa3e861c909d07b13c0699151d2d21f4.

- 2026-09-24T22:01:23+00:00: Recorded command exit 0; command argv SHA-256
  f38f63c1bb4bcfe7d9aa9a4bf1bb089d720b105299e3e01071a2545ebdeb287b.

- 2026-09-24T22:01:46+00:00: Recorded command exit 0; command argv SHA-256
  14b84a46d7d8a708ca50daefb40473c8269400be7a767dda71e68ba272d3cafc.

- 2026-09-24T22:02:00+00:00: Recorded command exit 0; command argv SHA-256
  775c83aefed8595372e699c4c329e34f1459a5eddcb16474021603e8c3ba4acb.

- 2026-09-24T22:02:36+00:00: Implemented repository-wide tutorial discovery and syntax freshness
  gate in f387877. CI validates all five versioned tutorial contracts, strict duplicate-key
  metadata, documentation references, deterministic diagnostics, renamed/removed command and option
  mutations, clean-home execution, and no process/network imports. Local 28 tutorial tests,
  freshness gate, Ruff, diff check, SSH signature and DCO passed.

- 2026-09-24T22:03:32+00:00: Recorded command exit 0; command argv SHA-256
  c2d1df31cb0d40c80075ceceb089eb0d6a02a356d52a65238ec1c5de5d48d9e5.

- 2026-09-24T22:03:57+00:00: Recorded command exit 0; command argv SHA-256
  c1d331d1fcb5892e616ca6d5e8d0136355885539714b7e02daf2989354fc2c07.

- 2026-09-24T22:04:16+00:00: Recorded command exit 0; command argv SHA-256
  4fdf15256377d191dccb26eb36d10e591e45565a8300f998053e6b8625dfc8cd.

- 2026-09-24T22:05:13+00:00: Recorded command exit 0; command argv SHA-256
  fe77c783f90ee837dbb794f28802f79c80ed23b04aacedd136cb6c3aeaf1d6a9.

- 2026-09-24T22:05:29+00:00: Recorded command exit 0; command argv SHA-256
  b94dd08ec380622834be9b7bcc217c3dc1d2cf1e85586c3c32748886687de7bf.

- 2026-09-24T22:05:48+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.
