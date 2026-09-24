---
{
  "branch": "codex/ar-1405-dependency-reconcile",
  "checkpoint_commit": "f213b29624bff8bdc2edd005711e2f70eeb70472",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1405",
  "next_action": "Monitor seven post-merge workflows for exact SHA f213b296; after all green, close/supersede scoped stale PRs with exact evidence, then release AR done. Action PRs #235/#234/#148 require a future policy-pin migration AR; #147 requires separate sha2 compatibility AR.",
  "observed_branch": "codex/ar-1405-dependency-reconcile",
  "observed_dirty": 0,
  "observed_head": "9c1ddea3df54555dc1127239916198c2f7e926ef",
  "owner": "",
  "plan": "../plans/AR-1405-open-dependency-pr-reconciliation.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "done",
  "summary": "Rebase, repair, verify, and truthfully resolve stale open dependency PRs.",
  "task_revision": 100,
  "title": "Open dependency PR reconciliation",
  "updated_at": "2026-09-24T12:11:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1405"
}
---

This AR does not authorize merging stale or incompatible dependency updates;
all changes remain subject to current exact-head gates.


- 2026-09-24T11:16:06+00:00: Open PR audit identified stale dependency candidates requiring
  current-main rebase and exact compatibility gates.

- 2026-09-24T11:25:27+00:00: Claimed by ar1405_dependency_pr_luna56b.

- 2026-09-24T11:26:12+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-24T11:27:16+00:00: Heartbeat by ar1405_dependency_pr_luna56b.

- 2026-09-24T11:27:25+00:00: Claimed isolated worktree; current protected main is e41d4df. Auditing
  PRs 237,236,235,234,150,149,148,147; no stale checks will be reused.

- 2026-09-24T11:27:41+00:00: Recorded command exit 0; command argv SHA-256
  f33e2e2ae36e4c67a500e7ce8e6ea3022e41a7b487659fab7c095c20d08fc793.

- 2026-09-24T11:27:55+00:00: Recorded command exit 0; command argv SHA-256
  d04aa803a9fcb854b247572f9b417fd1935a57ca978bb887d2e7c188e99db043.

- 2026-09-24T11:28:38+00:00: Recorded command exit 0; command argv SHA-256
  5510ea1d949b617e2567814f3302f41e369d0053872ec9f59529f6917f1d3594.

- 2026-09-24T11:29:13+00:00: Recorded command exit 0; command argv SHA-256
  2c64e9f2aad66e2ebc67b0df1c20cd7a67dee681cf6d782ff18929684b15b037.

- 2026-09-24T11:29:28+00:00: Recorded command exit 0; command argv SHA-256
  45bdd2ef3bd1c768bfa492841e34a36546ad72b6ff2ea46251ea1c9636131c07.

- 2026-09-24T11:29:45+00:00: Recorded command exit 0; command argv SHA-256
  b0758a960ba6e860a462400b071c0bfc4f97b3e927ba3ae1c3bd5eeddd8afe19.

- 2026-09-24T11:30:15+00:00: Recorded command exit 0; command argv SHA-256
  3ceb5b3c7a4b1b62042fd3fc4ec3ac72fe0f3324909ca15b91e145d82c375f99.

- 2026-09-24T11:30:30+00:00: Recorded command exit 0; command argv SHA-256
  74b639ddac4020c501d10e7e4ff0e1e7dfbc83bf9310c0fcb175b0bd88defaea.

- 2026-09-24T11:30:45+00:00: Recorded command exit 0; command argv SHA-256
  7380af9eb41db27fd81b048dbd122c0719717e96c5d53ae81c0b827c3bd173ad.

- 2026-09-24T11:32:11+00:00: Recorded command exit 0; command argv SHA-256
  d04aa803a9fcb854b247572f9b417fd1935a57ca978bb887d2e7c188e99db043.

- 2026-09-24T11:32:35+00:00: Recorded command exit 0; command argv SHA-256
  111607bc2d176d4a0265f375752f795decbb4809a82298cb2596a43d649ba132.

- 2026-09-24T11:33:04+00:00: Recorded command exit 0; command argv SHA-256
  dc8cf90baf75a4b57c5b598f0d3440f5d3b53566e2a070334d1b29a6d5f3bce3.

- 2026-09-24T11:33:31+00:00: Recorded command exit 0; command argv SHA-256
  0f95183a283571fff5acbe6fa81af02f546011cb668eab66e4759b7329eb1dd5.

- 2026-09-24T11:33:46+00:00: Recorded command exit 0; command argv SHA-256
  4bf5c5aac5f74d433677410e9a3b28b6de4aa5af7f8374045db59c41796542e6.

- 2026-09-24T11:34:01+00:00: Recorded command exit 0; command argv SHA-256
  47753ebca7ad6883d0d8f92b160f505a365f902fe317282454df259529d57bfc.

- 2026-09-24T11:34:20+00:00: Recorded command exit 0; command argv SHA-256
  1c8edc888e9afd227817f3198fae7e877976b1cdd12b34649563f5d1152cd50e.

- 2026-09-24T11:34:34+00:00: Recorded command exit 0; command argv SHA-256
  97c6c847a328616426bd75308201356d23454711f393332efb761f212d5f7540.

- 2026-09-24T11:34:50+00:00: Recorded command exit 0; command argv SHA-256
  521296d245b730b72bbeb19a4d5a3bba9dddb444802cd12657c584ded37b7f30.

- 2026-09-24T11:35:07+00:00: Recorded command exit 0; command argv SHA-256
  1abc82ca835ad09646d9629fd0c6728c7b1496eda52e40f4584165602d59247d.

- 2026-09-24T11:35:22+00:00: Recorded command exit 0; command argv SHA-256
  7f6307d812e9b6c0c99de455d8b627b4b14ff9fcb62d93f00743271049e9710d.

- 2026-09-24T11:35:49+00:00: Recorded command exit 0; command argv SHA-256
  9c79f555b878aaf95aa187f4a143d99fe9bd8d89dfd3f63bb6b8f66d65bf2d69.

- 2026-09-24T11:37:06+00:00: Recorded command exit 0; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-24T11:37:29+00:00: Recorded command exit 0; command argv SHA-256
  dba59eb50b942bae0cd9d41fc42431cde5f1f9be1cf15194fdbcac6ec1886c30.

- 2026-09-24T11:37:44+00:00: Recorded command exit 0; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-09-24T11:38:03+00:00: Recorded command exit 0; command argv SHA-256
  6b0340b78e00b5e8d62e9973b7e72f6c6de22448e8636894d4001797a91460ec.

- 2026-09-24T11:38:30+00:00: Recorded command exit 0; command argv SHA-256
  b81afee8325ab6f1bf13947a6caa0ea72524dada376a74238381164005fbeefc.

- 2026-09-24T11:38:45+00:00: Recorded command exit 0; command argv SHA-256
  9179f057853a58bd03ec0b792d8520c200d6c55f6ca0d6ba739771a63939c3d2.

- 2026-09-24T11:39:06+00:00: Recorded command exit 0; command argv SHA-256
  46019371c08db5eb4a4ca4502a10caf67ed30f368b768151c43bfac35e6a0c0d.

- 2026-09-24T11:39:34+00:00: Recorded command exit 0; command argv SHA-256
  137b51219beb7633949a6805df71bac0f3f62f151ee3989493233526894d3d6c.

- 2026-09-24T11:40:30+00:00: Recorded command exit 0; command argv SHA-256
  d48c8d8f057297768d98aca5b601a7ef34cca144660561128b034b4e5f8db5e4.

- 2026-09-24T11:40:46+00:00: Recorded command exit 0; command argv SHA-256
  5bf9a05fcfc88b3e1d35fb91b1fe6665f3769969781162ec7d5c4df2f70f0021.

- 2026-09-24T11:41:01+00:00: Recorded command exit 0; command argv SHA-256
  3bce7f4ff3e5844ba2d4eb2bff340fee51003a4091a145e2b5280f1010fd844b.

- 2026-09-24T11:41:18+00:00: Recorded command exit 0; command argv SHA-256
  5467b0de0c333c190eb7fe404ce00a3e6dc10f033edd264bea3392b19e5a17a6.

- 2026-09-24T11:42:33+00:00: Recorded command exit 0; command argv SHA-256
  d2a6db643a5591504aa8e8027dd2df94e2c93800c0b213b65a8c06102908f96a.

- 2026-09-24T11:42:48+00:00: Recorded command exit 0; command argv SHA-256
  0e7771055ceb2eda2509a648695453bc2c51382005bedff23f2231025d98196b.

- 2026-09-24T11:43:03+00:00: Recorded command exit 0; command argv SHA-256
  3999e4946d5a415722566c958094a970db914a1bf13a5339db613fa2ec365a62.

- 2026-09-24T11:43:39+00:00: Recorded command exit 0; command argv SHA-256
  5467b0de0c333c190eb7fe404ce00a3e6dc10f033edd264bea3392b19e5a17a6.

- 2026-09-24T11:46:26+00:00: Recorded command exit 101; command argv SHA-256
  5c8da9b34935360f7399b9d4b260d9a460b442f2f0ca08eddaee6e8f11776ef0.

- 2026-09-24T11:46:58+00:00: Recorded command exit 0; command argv SHA-256
  c9452a9b577fd064041bd3855b98c6f5a6569de23aed5356fe37a2cb523ec796.

- 2026-09-24T11:47:36+00:00: Recorded command exit 0; command argv SHA-256
  5c8da9b34935360f7399b9d4b260d9a460b442f2f0ca08eddaee6e8f11776ef0.

- 2026-09-24T11:48:02+00:00: Recorded command exit 0; command argv SHA-256
  18bd4aff9a09c3fb87a532f0a7fcc2d0fe00607e496aacf84775e9e758436f78.

- 2026-09-24T11:48:22+00:00: Recorded command exit 0; command argv SHA-256
  57e2feb5797b95ffb758adbab5db951af1ab83d6c5dfe7ca4b98ccd7352b7959.

- 2026-09-24T11:48:38+00:00: Recorded command exit 0; command argv SHA-256
  5467b0de0c333c190eb7fe404ce00a3e6dc10f033edd264bea3392b19e5a17a6.

- 2026-09-24T11:48:54+00:00: Recorded command exit 0; command argv SHA-256
  5467b0de0c333c190eb7fe404ce00a3e6dc10f033edd264bea3392b19e5a17a6.

- 2026-09-24T11:51:30+00:00: Recorded command exit 0; command argv SHA-256
  37beae6b72397b7366cc8c55e58d7b831f4525e813702f16d920c1539d10af79.

- 2026-09-24T11:51:56+00:00: Recorded command exit 0; command argv SHA-256
  54cfa4ab52b081ad454343a8f7cd6d4e6bedecbf67d597aeab2967cebdb2fb5d.

- 2026-09-24T11:52:10+00:00: Recorded command exit 0; command argv SHA-256
  a82f45f59df80d683641649bfa1a08ece3b3252a1c9612fe9474172b49552a40.

- 2026-09-24T11:52:27+00:00: Recorded command exit 0; command argv SHA-256
  5467b0de0c333c190eb7fe404ce00a3e6dc10f033edd264bea3392b19e5a17a6.

- 2026-09-24T11:52:42+00:00: Recorded command exit 101; command argv SHA-256
  4a40d397b2e44a3308828118cf8c43157feb162ac04b944a18c3900705cda19e.

- 2026-09-24T11:52:57+00:00: Heartbeat by ar1405_dependency_pr_luna56b.

- 2026-09-24T11:53:15+00:00: Repaired stale lock coverage: formal/Cargo.lock and fuzz/Cargo.lock now
  refresh thiserror/url transitions. Local formal cargo test passed; local cargo deny unavailable
  (cargo-deny not installed), so hosted policy/fuzz gates are authoritative. PR #291 head 9c1ddea is
  running exact checks.

- 2026-09-24T12:01:44+00:00: Recorded command exit 0; command argv SHA-256
  d9d5486ed4c4c9460e0cb6f81ea5f954ed31c258f92d05eb54decd08e3d406ca.

- 2026-09-24T12:02:11+00:00: Recorded command exit 2; command argv SHA-256
  c3574e79b7476d01109b971e46597893082389523294cc21644fc133f34840de.

- 2026-09-24T12:02:39+00:00: Recorded command exit 0; command argv SHA-256
  9b8be1155f7d2011866cb5ddd61c1073394ccdaa6042b220881ef690fc031766.

- 2026-09-24T12:04:36+00:00: Heartbeat by ar1405_dependency_pr_luna56b.

- 2026-09-24T12:04:47+00:00: PR #291 merged through signed exact-base integration: merge f213b296,
  parents e0b15fc and 9c1ddea, tree 04dc4ab3. Seven post-merge workflows launched; headers already
  green, six still pending.

- 2026-09-24T12:07:27+00:00: Recorded command exit 0; command argv SHA-256
  fe8eccb81df79754a96a5fd90d3a965721eb27b982d9576abffce9ce6bce546b.

- 2026-09-24T12:07:46+00:00: Recorded command exit 0; command argv SHA-256
  b20da9b373a3365b3e2ed2914e24fa996cce90c2a9411e66960001404776f31a.

- 2026-09-24T12:08:21+00:00: Recorded command exit 0; command argv SHA-256
  f7865a8279b30f37b26f9d6b769c590d33ba160dd464b45c11f31bc40500d6b2.

- 2026-09-24T12:08:50+00:00: Recorded command exit 0; command argv SHA-256
  57e94965f5610c87c410e302d188808074e7333ac8444099d398432c036a9363.

- 2026-09-24T12:09:04+00:00: Recorded command exit 0; command argv SHA-256
  3d4ab895049b45da839d0ed624bf0db096654583e3d25603f53cd85dc9599625.

- 2026-09-24T12:09:19+00:00: Recorded command exit 0; command argv SHA-256
  7ae39c47ce51c4223c231a77369c9011c359f1550503d9703216e620f5441382.

- 2026-09-24T12:09:34+00:00: Recorded command exit 0; command argv SHA-256
  bbefc759d2fbb85d73fe4147ee5934e95f7f1c076e675ae4157e40f910b77b74.

- 2026-09-24T12:09:52+00:00: Recorded command exit 0; command argv SHA-256
  64473990500469ae67e7b8a507fcf41cd57930d881cfa20df596c5c2e41d33da.

- 2026-09-24T12:10:08+00:00: Recorded command exit 0; command argv SHA-256
  6209448a4b55411db0871c22220f3a351483be5f1fe21b3ec66e6dc466da7b76.

- 2026-09-24T12:10:30+00:00: Recorded command exit 0; command argv SHA-256
  77d2666627a2c3ab53c31d3c41a2fd66086b94cb452c044d8a55c245cddef7e9.

- 2026-09-24T12:11:00+00:00: Done: merged PR #291 through signed exact-base integration. Merge
  f213b29624bff8bdc2edd005711e2f70eeb70472 has parents e0b15fc23be83eeea3882dcee39f9cdd43b45254 and
  9c1ddea3df54555dc1127239916198c2f7e926ef, reviewed tree 04dc4ab3cb0f27ff16e43dc1da28967ab796488f.
  All seven required post-merge workflows succeeded: 35996591324 hosted, 35996591279 formal,
  35996591194 Rust, 35996591302 emulated-aarch64, 35996591343 fault, 35996591314 repository quality,
  35996591364 headers. Safe stale PRs #237/#236/#150/#149 and unrelated stale #171/#125 are closed
  as superseded. PR #147 is closed as blocked/incompatible (missing DCO plus sha2 API/MSRV
  compatibility decision). PRs #235/#234/#148 remain open and explicitly blocked because current
  policy requires their old action pins; future policy migration ARs are required.
