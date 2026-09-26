---
{
  "branch": "release/ar-1462-pinned-release-toolchain-bundle-workflow",
  "checkpoint_commit": "36d4bdf35a644a36a8acfdb31078eb7f668a17c4",
  "claim_expires": "2026-09-26T21:35:08+00:00",
  "depends_on": [
    "AR-1460"
  ],
  "id": "AR-1462",
  "next_action": "Promote and implement the pinned offline-capable cargo-deny/cargo-audit toolchain and reviewed first-customer bundle/tag workflow, then rerun release readiness against exact protected main.",
  "observed_branch": "release/ar-1462-pinned-release-toolchain-bundle-workflow",
  "observed_dirty": 0,
  "observed_head": "76f099487da31b0ee7d7d29b9561785ccbb4e11f",
  "owner": "coordinator-ar1462-release-tooling",
  "plan": "../plans/AR-1462.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Establish reproducible supply-chain checks and first-customer release bundle publication workflow.",
  "task_revision": 58,
  "title": "Pinned release toolchain and first-customer bundle workflow",
  "updated_at": "2026-09-26T19:37:28+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1462-pinned-release-toolchain-bundle-workflow"
}
---

This P0 repair AR addresses the exact release-readiness failures recorded by
AR-1461. It must add a reproducible, pinned and offline-capable way to run the
required cargo-deny and cargo-audit checks, plus a reviewed first-customer
release workflow that derives its version/tag, checksums, SBOM/provenance and
bundle manifest from one clean exact commit. The workflow must be fail-closed,
credential-free by default, and must not require a remote provider, native
ARM host, asb-tui source, or external signing authority. An unsigned bundle is
permitted where the established release policy says signing is optional, but
all integrity, provenance, privacy and exact-head checks remain mandatory.

- 2026-09-26T19:20:00+00:00: Created from AR-1461's exact blocker: cargo-deny and
  cargo-audit are absent, and no checked-in release/tag/bundle/SBOM/provenance
  workflow exists. AR-1460's exact protected-main qualification is the input.

- 2026-09-26T19:17:00+00:00: AR-1460 is done; AR-1461 identified the release-tooling blocker;
  promote bounded P0 repair.

- 2026-09-26T19:17:03+00:00: Claimed by coordinator-ar1462-release-tooling.

- 2026-09-26T19:17:35+00:00: Recorded command exit 0; command argv SHA-256
  032da1cbce6ee6ab9b84a18cde263eec8332a57d995e1c47d0fe0c574ab0955f.

- 2026-09-26T19:19:06+00:00: Recorded command exit 0; command argv SHA-256
  d548db58f4ae0860bb692ee6d4196e355223f305ba6cbbc6da2cf15f21cc1454.

- 2026-09-26T19:19:21+00:00: Recorded command exit 0; command argv SHA-256
  d04aa803a9fcb854b247572f9b417fd1935a57ca978bb887d2e7c188e99db043.

- 2026-09-26T19:20:06+00:00: Recorded command exit 1; command argv SHA-256
  0783c4ca231a8c433c4fc4883db0fdec7edf10d94ee0a829627bc64f82738587.

- 2026-09-26T19:20:23+00:00: Recorded command exit 1; command argv SHA-256
  2b8344c1a8344c07788a5a55bb876d13fe3167bb202e50b5621728afa367641f.

- 2026-09-26T19:20:41+00:00: Recorded command exit 0; command argv SHA-256
  882450e35df46d21d00fe38c6e4dd55a42f6d722d854dccce7f39306335e4104.

- 2026-09-26T19:20:57+00:00: Recorded command exit 0; command argv SHA-256
  3111209c79dd189eada14700ee56edcabe74337ee74490b00dc4917b7bdc14f0.

- 2026-09-26T19:21:22+00:00: Recorded command exit 0; command argv SHA-256
  2b8344c1a8344c07788a5a55bb876d13fe3167bb202e50b5621728afa367641f.

- 2026-09-26T19:22:45+00:00: Recorded command exit 0; command argv SHA-256
  8920d3af11aaa0d16797d120a5b2a95755788ebd7343fe5cd03127681263a9d5.

- 2026-09-26T19:23:18+00:00: Heartbeat by coordinator-ar1462-release-tooling.

- 2026-09-26T19:24:00+00:00: Recorded command exit 0; command argv SHA-256
  37eadbd7126ccb695c8136e9133304ee20ae50023cb486664605c871c3af495b.

- 2026-09-26T19:24:48+00:00: Recorded command exit 0; command argv SHA-256
  2b8344c1a8344c07788a5a55bb876d13fe3167bb202e50b5621728afa367641f.

- 2026-09-26T19:25:06+00:00: Recorded command exit 1; command argv SHA-256
  66171b019b13f4cc7a97b253232d6fbc544aa3dd6e21e55381e2b2bb0cdb50e4.

- 2026-09-26T19:25:23+00:00: Recorded command exit 1; command argv SHA-256
  66171b019b13f4cc7a97b253232d6fbc544aa3dd6e21e55381e2b2bb0cdb50e4.

- 2026-09-26T19:25:45+00:00: Recorded command exit 0; command argv SHA-256
  66171b019b13f4cc7a97b253232d6fbc544aa3dd6e21e55381e2b2bb0cdb50e4.

- 2026-09-26T19:26:12+00:00: Recorded command exit 0; command argv SHA-256
  66171b019b13f4cc7a97b253232d6fbc544aa3dd6e21e55381e2b2bb0cdb50e4.

- 2026-09-26T19:26:42+00:00: Recorded command exit 0; command argv SHA-256
  79dbef86830ba9a8de5b2263b9ea87740ed11a231b723096149fbe71d54f06c0.

- 2026-09-26T19:27:51+00:00: Recorded command exit 0; command argv SHA-256
  12938f82fbaa9857db28f5434d0af3e082e02e4471a57c1807c2e82d77a69772.

- 2026-09-26T19:28:42+00:00: Recorded command exit 0; command argv SHA-256
  0feba3381ba22f65bf003563399a3fbe5a391f316cbf5149d404000e499c90bb.

- 2026-09-26T19:29:15+00:00: Heartbeat by coordinator-ar1462-release-tooling.

- 2026-09-26T19:29:21+00:00: Recorded command exit 0; command argv SHA-256
  66171b019b13f4cc7a97b253232d6fbc544aa3dd6e21e55381e2b2bb0cdb50e4.

- 2026-09-26T19:29:56+00:00: Heartbeat by coordinator-ar1462-release-tooling.

- 2026-09-26T19:30:03+00:00: Recorded command exit 0; command argv SHA-256
  ffbf4202617ed6a357419020065e8a853bae1cefc4021821d951d9958e5bfbab.

- 2026-09-26T19:30:24+00:00: Recorded command exit 1; command argv SHA-256
  78a65e32de36a78a3ec5905fc689b11d5c3df89ceb27dd5872a5922fa05f26bf.

- 2026-09-26T19:30:38+00:00: Recorded command exit 0; command argv SHA-256
  9cd2d0774db259487f5447b84a3f2b28f0483ff22f943f59e32a6283ec79bb04.

- 2026-09-26T19:31:01+00:00: Recorded command exit 0; command argv SHA-256
  78a65e32de36a78a3ec5905fc689b11d5c3df89ceb27dd5872a5922fa05f26bf.

- 2026-09-26T19:31:23+00:00: Recorded command exit 0; command argv SHA-256
  fe11dbc7dd5b8ebc773d30733d7aaf2dd397130dc97c20926c5d6c5bd5c4a741.

- 2026-09-26T19:31:44+00:00: Recorded command exit 0; command argv SHA-256
  04ceeb6173c80bd1c0054278338ba8a249ebd430a9fd362ae424d840d6122c99.

- 2026-09-26T19:32:22+00:00: Recorded command exit 0; command argv SHA-256
  d3d4af6418bf6bfb136696d4255c3261c0b4b8706323712b5e0f33419715664b.

- 2026-09-26T19:32:45+00:00: Recorded command exit 0; command argv SHA-256
  4a32ba9902d76aaf8f799497b8c003491fdf54dcca8c3980e04cf7e8d6432c1d.

- 2026-09-26T19:33:09+00:00: Recorded command exit 0; command argv SHA-256
  912a6125a1ee212ad5ab68bfde76adfd5ba156954cb0c930350a96732e37395c.

- 2026-09-26T19:33:29+00:00: Recorded command exit 0; command argv SHA-256
  522c21edced83643b27b5e98cb54572f5bad6fea5622554516bbf7bd8e449b74.

- 2026-09-26T19:34:05+00:00: Heartbeat by coordinator-ar1462-release-tooling.

- 2026-09-26T19:34:08+00:00: Recorded command exit 0; command argv SHA-256
  84dc2de8d2c7ae2f4e2de8d9805f575f40232fd58750f43ced239c0aa144b837.

- 2026-09-26T19:35:08+00:00: Heartbeat by coordinator-ar1462-release-tooling.

- 2026-09-26T19:35:10+00:00: Recorded command exit 0; command argv SHA-256
  e98b23e769f62c0accb274a3f2d03d9f548dd206d0b82076adc22cb504c535ef.

- 2026-09-26T19:35:25+00:00: Recorded command exit 0; command argv SHA-256
  64bb0529f3f33cb1504f047ba762f22e11ff717bcd1a725dac07e22b30366eba.

- 2026-09-26T19:35:50+00:00: Recorded command exit 0; command argv SHA-256
  9ba775d41e546e364f3ab38b2ffc92525044206e44b93a4fac1d63b594183144.

- 2026-09-26T19:36:11+00:00: Recorded command exit 0; command argv SHA-256
  912a6125a1ee212ad5ab68bfde76adfd5ba156954cb0c930350a96732e37395c.

- 2026-09-26T19:36:38+00:00: Recorded command exit 0; command argv SHA-256
  912a6125a1ee212ad5ab68bfde76adfd5ba156954cb0c930350a96732e37395c.

- 2026-09-26T19:37:28+00:00: Recorded command exit 0; command argv SHA-256
  912a6125a1ee212ad5ab68bfde76adfd5ba156954cb0c930350a96732e37395c.
