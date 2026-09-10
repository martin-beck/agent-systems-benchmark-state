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
  "task_revision": 31,
  "title": "Harden the asb-tui release lifecycle contract",
  "updated_at": "2026-09-10T19:46:05+00:00",
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

- 2026-09-10T19:32:28+00:00: Recorded command exit 0; command argv SHA-256
  d0baeb7d63933a86af1accd1c32e3bde030c665e14d854e0088bb252f682ffd5.

- 2026-09-10T19:33:08+00:00: Recorded command exit 101; command argv SHA-256
  081a5b53bc688cbe824f1b81961676e1dfeb9b20a2da0f4527b5729a607bb5ca.

- 2026-09-10T19:33:57+00:00: Recorded command exit 0; command argv SHA-256
  d0baeb7d63933a86af1accd1c32e3bde030c665e14d854e0088bb252f682ffd5.

- 2026-09-10T19:34:06+00:00: Recorded command exit 101; command argv SHA-256
  02966aaacd1d8c320ad8cbc910eaa8057f02af6621e5ef2540ab601665b224e2.

- 2026-09-10T19:34:36+00:00: Classified focused test exit 101: intended self-test response expanded
  from 9 to 14 closed identity fields; source-only binary correctly exited 3 with ready=false.
  Updated assertions now bind classification, target, empty unpromoted identities, ASB/protocol
  versions and exact field count; rerunning focused and full gates.

- 2026-09-10T19:34:53+00:00: Recorded command exit 101; command argv SHA-256
  7f9593ea33e58ce66d9e808b9aa937d337139e94cebbc422e94711fbbbc7f1fa.

- 2026-09-10T19:36:27+00:00: Recorded command exit 0; command argv SHA-256
  d0baeb7d63933a86af1accd1c32e3bde030c665e14d854e0088bb252f682ffd5.

- 2026-09-10T19:36:55+00:00: Recorded command exit 101; command argv SHA-256
  0a3cb09fcc4269379326bd7ad243e1c6d3093c1b7715eee7ab2ada5aa5a26020.

- 2026-09-10T19:37:29+00:00: Recorded command exit 0; command argv SHA-256
  7ee2bf737d03fcce86b526409ffea167f88e25e15048bda3db1eb72c70259649.

- 2026-09-10T19:38:15+00:00: Recorded command exit 0; command argv SHA-256
  ecfb73e71d4b8750c31c66df8486c07b2409ec5d41013849f23fa91ead9b4a41.

- 2026-09-10T19:38:52+00:00: Recorded command exit 101; command argv SHA-256
  081a5b53bc688cbe824f1b81961676e1dfeb9b20a2da0f4527b5729a607bb5ca.

- 2026-09-10T19:40:11+00:00: Recorded command exit 0; command argv SHA-256
  d0baeb7d63933a86af1accd1c32e3bde030c665e14d854e0088bb252f682ffd5.

- 2026-09-10T19:40:33+00:00: Recorded command exit 0; command argv SHA-256
  0a3cb09fcc4269379326bd7ad243e1c6d3093c1b7715eee7ab2ada5aa5a26020.

- 2026-09-10T19:40:43+00:00: Recorded command exit 0; command argv SHA-256
  0727ab62751f97ac3f8005e4337de58183d93dade158ff996213ea3f424b966a.

- 2026-09-10T19:41:08+00:00: Recorded command exit 0; command argv SHA-256
  d1bf97ecaf19a01bdc1778df6ddd739d67302f6d35e5b209f1de6869be238bde.

- 2026-09-10T19:42:21+00:00: Recorded command exit 0; command argv SHA-256
  d0baeb7d63933a86af1accd1c32e3bde030c665e14d854e0088bb252f682ffd5.

- 2026-09-10T19:42:43+00:00: Recorded command exit 101; command argv SHA-256
  081a5b53bc688cbe824f1b81961676e1dfeb9b20a2da0f4527b5729a607bb5ca.

- 2026-09-10T19:43:23+00:00: Recorded command exit 0; command argv SHA-256
  d0baeb7d63933a86af1accd1c32e3bde030c665e14d854e0088bb252f682ffd5.

- 2026-09-10T19:44:55+00:00: Recorded command exit 0; command argv SHA-256
  d0baeb7d63933a86af1accd1c32e3bde030c665e14d854e0088bb252f682ffd5.

- 2026-09-10T19:45:15+00:00: Recorded command exit 0; command argv SHA-256
  2534fa89248632489007e34c2ce7f46ad54115b65865b76576241a7304fe1f06.

- 2026-09-10T19:45:25+00:00: Recorded command exit 0; command argv SHA-256
  0727ab62751f97ac3f8005e4337de58183d93dade158ff996213ea3f424b966a.

- 2026-09-10T19:45:35+00:00: Recorded command exit 0; command argv SHA-256
  d1bf97ecaf19a01bdc1778df6ddd739d67302f6d35e5b209f1de6869be238bde.

- 2026-09-10T19:46:05+00:00: Recorded command exit 0; command argv SHA-256
  37f93b176210021a8307057c83c9872923de576b22bc81440102a34a8363ed32.
