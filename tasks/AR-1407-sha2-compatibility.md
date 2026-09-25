---
{
  "branch": "repair/ar-1407-sha2-compatibility",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1405"
  ],
  "id": "AR-1407",
  "next_action": "Keep current sha2 0.10.9 implementation authoritative; PR #147 sha2 0.11.0 remains superseded unless a separately reviewed compatibility migration addresses all digest formatting sites and proves exact parity.",
  "observed_branch": "repair/ar-1407-sha2-compatibility",
  "observed_dirty": 0,
  "observed_head": "7390bcd2082700d0c9f04409732b48de8e9f8628",
  "owner": "",
  "plan": "../plans/AR-1407-sha2-compatibility.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "done",
  "summary": "Qualify or repair the closed sha2 0.11 dependency update without weakening crypto or MSRV contracts.",
  "task_revision": 27,
  "title": "sha2 compatibility repair",
  "updated_at": "2026-09-25T11:47:30+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1407-sha2-compatibility"
}
---

The current protected cryptographic implementation remains authoritative until
compatibility and digest parity are proven.


- 2026-09-25T11:38:03+00:00: AR-1405 is complete at merged f213b296 with seven green post-merge
  workflows; promote bounded sha2 compatibility qualification

- 2026-09-25T11:38:10+00:00: Claimed by ar1407_sha2_compat_luna56.

- 2026-09-25T11:38:40+00:00: Blocked before product qualification: promoted task has empty
  branch/worktree_key metadata; handoffctl correctly refuses wrapped product command. Coordinator
  metadata repair required before claim.

- 2026-09-25T11:41:39+00:00: Promote compatibility repair after generated state reconciliation.

- 2026-09-25T11:41:42+00:00: Claimed by ar1407_sha2_compat_luna56.

- 2026-09-25T11:41:49+00:00: Recorded command exit 0; command argv SHA-256
  9ce2906a9cc3d0767230e00ba7678e5e28c488288ef0188c0854bd5a346f26f3.

- 2026-09-25T11:42:12+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-25T11:42:26+00:00: Recorded command exit 0; command argv SHA-256
  6c60282ffe3be1b0d956437e8b3d302cd8b7181ac977a3908b608d0319ea3fa8.

- 2026-09-25T11:42:41+00:00: Recorded command exit 0; command argv SHA-256
  52f92cf852962461f85285a350842e59a09d20fdc1eccdb6ede9e2f55bd71325.

- 2026-09-25T11:43:08+00:00: Heartbeat by ar1407_sha2_compat_luna56.

- 2026-09-25T11:43:15+00:00: Recorded command exit 0; command argv SHA-256
  9cb360e8a40e5a2162b4324c5ce8eec1b353d40bfb59b28b51f16237df2b31ba.

- 2026-09-25T11:43:36+00:00: Recorded command exit 0; command argv SHA-256
  4ea9179736e858bc68655c7440f25cf6e27c1a8ff80fdfe1c2a65e236bd6d56c.

- 2026-09-25T11:43:51+00:00: Recorded command exit 0; command argv SHA-256
  18190881ee56a1751182829bfc5b1c19158a92923189bf3551c28419d6182ff6.

- 2026-09-25T11:44:09+00:00: Recorded command exit 0; command argv SHA-256
  907064b216b621b3d62946f6128468076d6c7dea3a9a179111146263d0e187bf.

- 2026-09-25T11:44:34+00:00: Recorded command exit 0; command argv SHA-256
  6bae05a85a67a379583ab3d23b3876119093b6e9c9ae4fa462c988aeaac0fd8d.

- 2026-09-25T11:44:56+00:00: Recorded command exit 101; command argv SHA-256
  a37d35e290b63ddfe8627f9bdb0474ef6d3f2654ade91f05cd9a55c3a713fceb.

- 2026-09-25T11:45:31+00:00: Recorded command exit 101; command argv SHA-256
  a37d35e290b63ddfe8627f9bdb0474ef6d3f2654ade91f05cd9a55c3a713fceb.

- 2026-09-25T11:46:08+00:00: Recorded command exit 101; command argv SHA-256
  a37d35e290b63ddfe8627f9bdb0474ef6d3f2654ade91f05cd9a55c3a713fceb.

- 2026-09-25T11:46:36+00:00: Recorded command exit 0; command argv SHA-256
  7a03f3b05d79b94b2e4e2555fd57095edfeb2564035e4e4879ce5de5c9c30b71.

- 2026-09-25T11:46:51+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-25T11:47:19+00:00: Reproduced PR #147 head f130ffe4e5735438f3e048c323b1069f148bd15e under
  Rust 1.93.0 with locked workspace check. sha2 0.11.0 upgrades digest to 0.11.3/hybrid-array and
  removes LowerHex from digest output; cargo check fails in asb-config at lib.rs:404,502,561,1157,
  then asb-protocol at experiment.rs:461, measurement.rs:542,917, provider.rs:770. Failure is
  API-wide across digest formatting, not an isolated MSRV issue. Restored clean worktree; no crypto
  patch or gate weakening made.

- 2026-09-25T11:47:30+00:00: Qualified and preserved supersession: PR #147 head
  f130ffe4e5735438f3e048c323b1069f148bd15e with sha2 0.11.0 fails locked Rust 1.93 workspace compile
  because digest 0.11.3 output no longer implements LowerHex; exact failures recorded in task
  evidence at asb-config and asb-protocol. Worktree clean; current sha2 0.10.9 remains
  authoritative. No product PR.
