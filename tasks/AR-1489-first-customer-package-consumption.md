---
{
  "branch": "feature/ar-1489-first-customer-package-consumption",
  "checkpoint_commit": "b048fef92f4bdb4eedd5379d645f4288a4b6ab20",
  "claim_expires": "2026-09-27T17:33:12+00:00",
  "depends_on": [
    "AR-1461",
    "AR-1462",
    "AR-1488"
  ],
  "id": "AR-1489",
  "next_action": "Monitor eight exact-main post-merge workflows for merge b048fef9; release done only after all terminal SUCCESS.",
  "observed_branch": "feature/ar-1489-first-customer-package-consumption",
  "observed_dirty": 0,
  "observed_head": "c4578eecd93183eaadaf9c34defbc4137ba03657",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1489-first-customer-package-consumption.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Verify first-customer release package installation and owner-backed local/mock/replay consumption.",
  "task_revision": 56,
  "title": "First-customer package consumption",
  "updated_at": "2026-09-27T15:34:17+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1489-first-customer-package-consumption"
}
---

Dependency-safe successor after AR-1488. It verifies the package/install
boundary and a fresh credential-free local/mock/replay journey without
touching asb-tui or requiring a live provider.

- 2026-09-27T15:05:00+00:00: Created after AR-1488 completion to close the
  remaining fresh package installation and consumption evidence gap.

- 2026-09-27T15:08:05+00:00: Dependencies AR-1461, AR-1462, and AR-1488 are done. Promote ASB-only
  first-customer package/install consumption qualification with local/mock/replay evidence.

- 2026-09-27T15:08:07+00:00: Claimed by ar1332-record-replay-luna56.

- 2026-09-27T15:08:18+00:00: Recorded command exit 0; command argv SHA-256
  1e11db425c6c6e86fb3846c57ea38401e187d9f08872a074c431e074467f14a4.

- 2026-09-27T15:08:42+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T15:08:44+00:00: Recorded command exit 0; command argv SHA-256
  adb665d3caea9f5fce5c4aa0bca3ad091ad3070b792198e1161e976b0ad3f97d.

- 2026-09-27T15:09:58+00:00: Recorded command exit 0; command argv SHA-256
  0547dbb3f7eb89ce1f2fdc0389057bbcb1dd141b173afcff27a67101ef23550c.

- 2026-09-27T15:10:22+00:00: Recorded command exit 0; command argv SHA-256
  007ea00c422c1a8708fadc4704ed7fe732b5b7b24edd1cb7ffee7c4bb045ce61.

- 2026-09-27T15:10:38+00:00: Recorded command exit 0; command argv SHA-256
  80f647aaa893d98055d5c8265a458880f733cebc9cc17a49c4b0ad843887ed86.

- 2026-09-27T15:11:55+00:00: Recorded command exit 0; command argv SHA-256
  35c0f39185807cecd42be1d8874e4cdf75f68254401ff71b64ef2fb0e5e6722e.

- 2026-09-27T15:12:11+00:00: Recorded command exit 0; command argv SHA-256
  a21456e014650b08b2b19cc1e81f4a5379c92b0d61fb8f7745d9bcf4ef7c0835.

- 2026-09-27T15:12:36+00:00: Recorded command exit 0; command argv SHA-256
  cc7fde5f57e3c6ee9f74520ca102040b5067efc37478d64ab548ca0e28fccbba.

- 2026-09-27T15:13:42+00:00: Recorded command exit 0; command argv SHA-256
  0f4547345791f4da487b7a1c9ef0e74738ca2b1cc1493c41919fd36606c30990.

- 2026-09-27T15:14:03+00:00: Recorded command exit 0; command argv SHA-256
  1bdc07befa2dbc140bdf7ff1f7258e5237227cbdc48922689563fd9850137828.

- 2026-09-27T15:14:33+00:00: Recorded command exit 0; command argv SHA-256
  64b8035d63315d09447c0e304f18799485a91eca71d85ab06a188806e6a1a5f1.

- 2026-09-27T15:14:49+00:00: Recorded command exit 0; command argv SHA-256
  9412a3f5048de0257a0e197c071b647bacce27b99c30edbb991f1810a2006d19.

- 2026-09-27T15:15:15+00:00: Recorded command exit 0; command argv SHA-256
  2e837e3d8f24778e834d0b7beb81cbefd79cf9e0f1911c185be1b418d6e7f89f.

- 2026-09-27T15:15:42+00:00: AR-1489 package-consumption qualification is docs-only: added bundle
  verification/install/doctor/setup/local-mock/replay/cleanup walkthrough and README route. Existing
  bundle and lifecycle contracts audited. Focused guide 5/5, transcript 3/3, bundle schema 2/2,
  clippy, rustdoc, release build, serial workspace tests, policy, signature, and clean-tree gates
  passed. Signed SSH+DCO head c4578eecd93183eaadaf9c34defbc4137ba03657.

- 2026-09-27T15:15:56+00:00: Recorded command exit 0; command argv SHA-256
  e84482ef76dc4486a872ddc324daba82f7bbeba993b6b7f883f57bf0e2a86aea.

- 2026-09-27T15:16:22+00:00: Published PR #369 from exact signed/DCO head
  c4578eecd93183eaadaf9c34defbc4137ba03657; branch
  feature/ar-1489-first-customer-package-consumption pushed successfully.

- 2026-09-27T15:16:31+00:00: Recorded command exit 0; command argv SHA-256
  f0ad34729e67608e492af228eaa5ad1666818002a44b4197d67c3b26b3f41317.

- 2026-09-27T15:17:53+00:00: Recorded command exit 0; command argv SHA-256
  f0ad34729e67608e492af228eaa5ad1666818002a44b4197d67c3b26b3f41317.

- 2026-09-27T15:18:26+00:00: Recorded command exit 0; command argv SHA-256
  f0ad34729e67608e492af228eaa5ad1666818002a44b4197d67c3b26b3f41317.

- 2026-09-27T15:19:05+00:00: Recorded command exit 0; command argv SHA-256
  f0ad34729e67608e492af228eaa5ad1666818002a44b4197d67c3b26b3f41317.

- 2026-09-27T15:19:21+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T15:19:39+00:00: Recorded command exit 0; command argv SHA-256
  f0ad34729e67608e492af228eaa5ad1666818002a44b4197d67c3b26b3f41317.

- 2026-09-27T15:20:29+00:00: Recorded command exit 0; command argv SHA-256
  f0ad34729e67608e492af228eaa5ad1666818002a44b4197d67c3b26b3f41317.

- 2026-09-27T15:21:00+00:00: Recorded command exit 0; command argv SHA-256
  f0ad34729e67608e492af228eaa5ad1666818002a44b4197d67c3b26b3f41317.

- 2026-09-27T15:21:43+00:00: Recorded command exit 0; command argv SHA-256
  f0ad34729e67608e492af228eaa5ad1666818002a44b4197d67c3b26b3f41317.

- 2026-09-27T15:22:16+00:00: Recorded command exit 0; command argv SHA-256
  f0ad34729e67608e492af228eaa5ad1666818002a44b4197d67c3b26b3f41317.

- 2026-09-27T15:22:57+00:00: Recorded command exit 0; command argv SHA-256
  f0ad34729e67608e492af228eaa5ad1666818002a44b4197d67c3b26b3f41317.

- 2026-09-27T15:23:13+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T15:23:28+00:00: Recorded command exit 0; command argv SHA-256
  f0ad34729e67608e492af228eaa5ad1666818002a44b4197d67c3b26b3f41317.

- 2026-09-27T15:24:24+00:00: Recorded command exit 0; command argv SHA-256
  f0ad34729e67608e492af228eaa5ad1666818002a44b4197d67c3b26b3f41317.

- 2026-09-27T15:24:46+00:00: Independent exact-head review passed: two-file docs-only
  package-consumption walkthrough and README route, preserving verifier/install/authority
  boundaries; signed SSH+DCO head c4578eecd93183eaadaf9c34defbc4137ba03657. PR #369 exact head
  confirmed, mergeState CLEAN, all 13 required checks terminal SUCCESS.

- 2026-09-27T15:24:53+00:00: Recorded command exit 0; command argv SHA-256
  f0ad34729e67608e492af228eaa5ad1666818002a44b4197d67c3b26b3f41317.

- 2026-09-27T15:25:30+00:00: Recorded command exit 0; command argv SHA-256
  31694fc220207d6c14b90d13fe61e4a93a39170de9234dbd2dab91778554c705.

- 2026-09-27T15:25:57+00:00: Recorded command exit 0; command argv SHA-256
  55926cc3212b41428dbe1075b43eb01eb55443e2b67ef5d9d52d88feff68cad2.

- 2026-09-27T15:26:20+00:00: Recorded command exit 0; command argv SHA-256
  d4b21b9fa84bddbff736766a979ee6bd6f7610dbdc4da1c43b6e9d69758f5d31.

- 2026-09-27T15:26:49+00:00: PR #369 merged 2026-09-27T15:25:29Z. Merge
  b048fef92f4bdb4eedd5379d645f4288a4b6ab20; reviewed head c4578eec. Exact-main workflows launched:
  Huawei 36329496606 SUCCESS, Hosted 36329496670, Credential-free 36329496593, Formal 36329496626,
  AArch64 36329496650, Repository quality 36329496635, Rust 36329496563, Fault 36329496583.

- 2026-09-27T15:27:54+00:00: Recorded command exit 0; command argv SHA-256
  d4b21b9fa84bddbff736766a979ee6bd6f7610dbdc4da1c43b6e9d69758f5d31.

- 2026-09-27T15:28:13+00:00: Recorded command exit 0; command argv SHA-256
  d4b21b9fa84bddbff736766a979ee6bd6f7610dbdc4da1c43b6e9d69758f5d31.

- 2026-09-27T15:29:08+00:00: Recorded command exit 0; command argv SHA-256
  d4b21b9fa84bddbff736766a979ee6bd6f7610dbdc4da1c43b6e9d69758f5d31.

- 2026-09-27T15:29:24+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T15:29:42+00:00: Recorded command exit 0; command argv SHA-256
  d4b21b9fa84bddbff736766a979ee6bd6f7610dbdc4da1c43b6e9d69758f5d31.

- 2026-09-27T15:30:28+00:00: Recorded command exit 0; command argv SHA-256
  d4b21b9fa84bddbff736766a979ee6bd6f7610dbdc4da1c43b6e9d69758f5d31.

- 2026-09-27T15:31:03+00:00: Recorded command exit 0; command argv SHA-256
  d4b21b9fa84bddbff736766a979ee6bd6f7610dbdc4da1c43b6e9d69758f5d31.

- 2026-09-27T15:31:43+00:00: Recorded command exit 0; command argv SHA-256
  d4b21b9fa84bddbff736766a979ee6bd6f7610dbdc4da1c43b6e9d69758f5d31.

- 2026-09-27T15:32:16+00:00: Recorded command exit 0; command argv SHA-256
  d4b21b9fa84bddbff736766a979ee6bd6f7610dbdc4da1c43b6e9d69758f5d31.

- 2026-09-27T15:32:56+00:00: Recorded command exit 0; command argv SHA-256
  d4b21b9fa84bddbff736766a979ee6bd6f7610dbdc4da1c43b6e9d69758f5d31.

- 2026-09-27T15:33:12+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T15:33:31+00:00: Recorded command exit 0; command argv SHA-256
  d4b21b9fa84bddbff736766a979ee6bd6f7610dbdc4da1c43b6e9d69758f5d31.

- 2026-09-27T15:34:17+00:00: Recorded command exit 0; command argv SHA-256
  d4b21b9fa84bddbff736766a979ee6bd6f7610dbdc4da1c43b6e9d69758f5d31.
