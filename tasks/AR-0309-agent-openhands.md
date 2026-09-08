---
{
  "branch": "feature/agent-openhands",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T06:49:55+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0102",
    "AR-0103"
  ],
  "id": "AR-0309",
  "next_action": "Implement the isolated OpenHands module and fixture around the proven SDK-only custom-tool boundary; pin and verify the 136-package Python graph before requesting shared lib.rs registration.",
  "observed_branch": "feature/agent-openhands",
  "observed_dirty": 2,
  "observed_head": "3a07b57b8265d98eeebbcd4fd21339d72fac0663",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-0309.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Run a maintained MIT OpenHands SDK or canonical headless client.",
  "task_revision": 27,
  "title": "Implement maintained OpenHands SDK client adapter",
  "updated_at": "2026-09-08T04:15:40+00:00",
  "worktree_key": "agent-systems-benchmark-agent-openhands"
}
---
## AR-0309

Run a maintained MIT OpenHands SDK or canonical headless client.

Implementation has not started. Read the linked plan before claiming.


- 2026-09-08T03:49:45+00:00: Verified AR-0101, AR-0102 and AR-0103 are durably done. Selected
  highest-priority safe disjoint leaf after P1 authorization/dependency/path blockers; OpenHands
  module and fixtures do not overlap active frontend protocol, verifier integrity, or kernel
  diagnostics paths.

- 2026-09-08T03:49:55+00:00: Claimed by contracts_20260906.

- 2026-09-08T03:50:41+00:00: Recorded command exit 0; command argv SHA-256
  07036c4ad1b996ca80da9bef22d326a3298e0fa2af6aa940f96f17b07676a4b3.

- 2026-09-08T03:55:22+00:00: Official-source boundary resolved: use active MIT
  OpenHands/software-agent-sdk v1.45.0, signed tag commit 49ea74587c376b90700f6eff128c3d9b57585d27
  and tree 639a6850375c0d8e04c9f045a5a74c15fea0406c. Exclude OpenHands/OpenHands enterprise paths.
  Do not use OpenHands-CLI 1.16.0 for this adapter: although MIT and maintained, its latest release
  pins older SDK/tools 1.21.0 and documented headless operation is always-approve, so it cannot
  expose the required bounded confirmation policy as cleanly as the SDK.

- 2026-09-08T03:57:02+00:00: Recorded command exit 1; command argv SHA-256
  10c15ae9e6c277a981542655bf485392a3392b9b9505a04cd20806bfee47a5f6.

- 2026-09-08T03:57:30+00:00: Recorded command exit 1; command argv SHA-256
  66da4fbe5e6464ee9d68e3834c74fb42921242e766b1a2034ec420c1ef435f21.

- 2026-09-08T03:57:44+00:00: Recorded command exit 1; command argv SHA-256
  a70f1bec1335a8a298c55d63e5fc86519af84c76b83ea9cd68b18201618a534f.

- 2026-09-08T03:57:56+00:00: Recorded command exit 0; command argv SHA-256
  e046063cdec35e5ac2dbf813eb115fc953730f3e03311593c44b06f6516ac43b.

- 2026-09-08T03:58:16+00:00: Recorded command exit 0; command argv SHA-256
  9fe3ace62ad35d411bb905dd2705e9f7d79b3ceb478a126d89f6a69420d7abe6.

- 2026-09-08T04:00:15+00:00: Recorded command exit 2; command argv SHA-256
  cb76f2eadc7d84a08940326c617e2bf9e8f94bdca84bf86b5de2ac1eaaae9c80.

- 2026-09-08T04:04:01+00:00: Recorded command exit 0; command argv SHA-256
  62f7e88cca66e94b3960fdd21aea322fc297518ec6d1f8e85a57859d59815363.

- 2026-09-08T04:04:30+00:00: Recorded command exit 1; command argv SHA-256
  6d819964b1301e94d9f87cb995f8e740fe9292a49829e809bcd0459299e90be5.

- 2026-09-08T04:04:42+00:00: Recorded command exit 0; command argv SHA-256
  6fc8587a9a6a662fe07b64324f08c93893fd0642ce7d3a85c73afd2fc988b76a.

- 2026-09-08T04:05:10+00:00: Recorded command exit 0; command argv SHA-256
  b843a942da9e23c42becd7c8321107d1e2604df3eb69e56d1497f6f28962d4a4.

- 2026-09-08T04:06:18+00:00: Native credential-free SDK probe succeeded with OpenHands SDK 1.45.0 on
  CPython 3.12: isolated HOME/XDG roots, no persistence_dir (InMemoryFileStore), AlwaysConfirm
  pending-action validation, a custom bounded write tool, finish event, positive aggregate usage (20
  input/8 output), and exact workspace edit. Closed proxies exposed one denied LiteLLM remote
  cost-map attempt, so production must force the local cost map and reject diagnostics. The first
  all-wheel install failed because func-timeout 4.3.5 is sdist-only; sdk-only resolves 136 packages,
  while adding openhands-tools/workspace expands to 194 packages. Use SDK-only plus ASB-owned
  bounded tool to minimize attack surface.

- 2026-09-08T04:13:03+00:00: Recorded command exit 0; command argv SHA-256
  f1ed95d4565d704f631d934aaba61d6ff0d10990eb20b1c29fe6b01067540429.

- 2026-09-08T04:13:41+00:00: Recorded command exit 0; command argv SHA-256
  f03f14a4247d608d63dd21bc9152c3cfbcb749c39750ac882aff3713eac8bfb5.

- 2026-09-08T04:14:07+00:00: Recorded command exit 101; command argv SHA-256
  73ace59d4f0fe2f69761406da10d9d0939a4b3f693e34b49bb753040bb97450d.

- 2026-09-08T04:14:16+00:00: Recorded command exit 0; command argv SHA-256
  1eaa9f61492f2fa1edf39d0edf9b9a06d9fed16270d338827188a7b0d21f64ba.

- 2026-09-08T04:14:44+00:00: Recorded command exit 101; command argv SHA-256
  14a63e3bea35a89d4ad3486f63c95f0799d2369b8ea961c6a9fe0d578f3dd77f.

- 2026-09-08T04:14:57+00:00: Recorded command exit 0; command argv SHA-256
  763962ff3b0e6a2f13ff08bc4467a1ec365ad6efaff40757cc7a074492f3b1ce.

- 2026-09-08T04:15:12+00:00: Recorded command exit 0; command argv SHA-256
  14a63e3bea35a89d4ad3486f63c95f0799d2369b8ea961c6a9fe0d578f3dd77f.

- 2026-09-08T04:15:40+00:00: Recorded command exit 0; command argv SHA-256
  fe167aadf3ab5243ef1c89cc19a5d83748303e4ac63fc017fcad23703e07b109.
