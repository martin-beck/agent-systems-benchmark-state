---
{
  "branch": "feature/asb-tui-release-contract-hardening",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T22:13:59+00:00",
  "depends_on": [
    "AR-1017",
    "AR-1018",
    "AR-1019",
    "AR-1020",
    "AR-1021"
  ],
  "id": "AR-1022",
  "next_action": "Harden the standalone lifecycle trust root, clock, classification and release-compatible schemas before any public install route consumes them.",
  "owner": "codex-ar1022-lifecycle-20260910",
  "plan": "../plans/AR-1022.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Turn the tested unverified asb-tui lifecycle boundary into a release-safe delegated contract.",
  "task_revision": 8,
  "title": "Harden the asb-tui release lifecycle contract",
  "updated_at": "2026-09-10T19:30:05+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-release-contract-hardening"
}
---
Repair the pre-release lifecycle boundary without weakening its existing signature, bundle,
transaction, recovery or isolation guarantees. Production requests must not choose their own trust
root or verification time, and a verified public release must not remain labelled as an unverified
extension. Preserve deterministic injection seams only inside tests.

Acceptance requires closed generated schemas, backward/rejection behavior documented explicitly,
embedded signer identity, system-clock verification, honest verified-channel state, hostile request
and filesystem tests, complete local gates, independent review, exact-head CI and post-merge checks.

- 2026-09-10T19:13:59+00:00: Claimed by codex-ar1022-lifecycle-20260910.

- 2026-09-10T19:14:17+00:00: Recorded command exit 0; command argv SHA-256
  8944772fadc13e086aeb779120b568f0f9c23190d34e1aa24ce37ea79900fd7f.

- 2026-09-10T19:24:52+00:00: Baseline wrapper call from the standalone asb-tui worktree was rejected
  by the project binding before cargo ran; subsequent wrapped commands originate in the bound state
  checkout and use explicit asb-tui paths.

- 2026-09-10T19:25:46+00:00: Recorded command exit 101; command argv SHA-256
  2046939d4755a9d214168dbeabd77c7b63f39f4d6101cd267eaf16b3f4abb651.

- 2026-09-10T19:26:09+00:00: Recorded command exit 0; command argv SHA-256
  081a5b53bc688cbe824f1b81961676e1dfeb9b20a2da0f4527b5729a607bb5ca.

- 2026-09-10T19:29:51+00:00: Recorded command exit 0; command argv SHA-256
  f8b3ce4feca9ace76a7b4534afdb5be1641487571f856a9b93e314c2ff927e83.

- 2026-09-10T19:30:05+00:00: Recorded command exit 0; command argv SHA-256
  9433db6b7bf38cc09dd37ed43e53985ab8fa2a08279972a69d672ae9265d4d55.
