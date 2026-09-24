---
{
  "branch": "ci/ar-1216-tutorial-freshness",
  "checkpoint_commit": "",
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
  "next_action": "Implement the repository-wide tutorial discovery and syntax-freshness CI gate after all tutorial contracts are defined.",
  "observed_branch": "ci/ar-1216-tutorial-freshness",
  "observed_dirty": 0,
  "observed_head": "9d97e1684ecddc091b46edb0a1a65a63534175e6",
  "owner": "ar1216-tutorial-freshness-luna56",
  "plan": "../plans/AR-1216.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Continuously keep ASB tutorial commands and steps syntactically current.",
  "task_revision": 8,
  "title": "ASB tutorial freshness CI and documentation qualification",
  "updated_at": "2026-09-24T22:01:23+00:00",
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
