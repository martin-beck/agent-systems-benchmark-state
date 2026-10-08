---
{
  "branch": "repair/ar-1748-portable-main-provenance",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T20:27:25+00:00",
  "depends_on": [
    "AR-1427",
    "AR-1431"
  ],
  "id": "AR-1748",
  "next_action": "Implement a generally available required CI provenance check and capability-aware ruleset admission, then independently review, merge, verify post-merge CI, and perform one bounded live settings apply with two consecutive audits.",
  "observed_branch": "repair/ar-1748-portable-main-provenance",
  "observed_dirty": 0,
  "observed_head": "7c3e9e3eca962474c03db9b77dbe09a30e95099d",
  "owner": "ar1748_portable_main_provenance_20261008",
  "plan": "../plans/AR-1748-protected-main-portable-provenance.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1748.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Replace the unavailable Enterprise-only commit-metadata ruleset with a required portable provenance check while preserving Web Flow rejection and atomic protected-main admission.",
  "task_revision": 126,
  "title": "Portable protected-main provenance and capability admission",
  "updated_at": "2026-10-08T20:21:42+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1748-portable-main-provenance"
}
---

AR-1746 merged bounded settings diagnostics and passed every exact-main
post-merge workflow, but its single live ruleset creation attempt was rejected
atomically with HTTP 422. Two audits prove that no repository setting or
ruleset was partially changed. Read-only diagnosis identifies the requested
`committer_email_pattern` restriction as an Enterprise-organization metadata
feature, while ASB is a public user-owned GitHub Free repository. Core public
rulesets are available and repository administration is working.

This successor must preserve the actual admission predicate. It may not remove
the metadata rule and then claim Web Flow rejection is enforced: GitHub Web
Flow commits can be GitHub-signed and web signoff supplies DCO but does not
prove the reviewed local merge path. Instead, add a mandatory portable CI
provenance check that rejects Web Flow/noreply commits and validates the exact
signed-DCO merge identity, require that check in the generally available core
ruleset, and make the settings tool capability-aware before any mutation.

Development integration requires an independent technical worker but permits
the same GitHub account; it does not require a second account, production
credentials, a verified release, or an Enterprise upgrade. If the portable
contract cannot be expressed and observed on the current repository, fail
closed with an exact typed blocker rather than weakening it.

- 2026-10-08T17:24:52+00:00: Promoted after AR-1746 atomic rejection diagnosis: implement portable
  Web Flow provenance enforcement and capability-aware core ruleset admission without weakening
  development policy.

- 2026-10-08T17:27:25+00:00: Claimed by ar1748_portable_main_provenance_20261008.

- 2026-10-08T17:27:34+00:00: Recorded command exit 0; command argv SHA-256
  b7023a6f6301c30be2548d060b4866d61bffe515b6b2c81f33dc2fb25c858b10.

- 2026-10-08T17:30:20+00:00: Recorded command exit 0; command argv SHA-256
  3a8b5522600b1ac244d11f78d2a060d1a8e60b8ba3477ef6aa7586d54d5a5d8c.

- 2026-10-08T17:31:33+00:00: Recorded command exit 1; command argv SHA-256
  1933e16a4a920a306a9d32682500f1537f49a615d94c6d095dcc6c288fa88e6f.

- 2026-10-08T17:32:11+00:00: Recorded command exit 0; command argv SHA-256
  2c04dad3bf114734e4dadc332f2895b056f1a1c0391d5f3afe4b112cf60dd603.

- 2026-10-08T17:33:15+00:00: Recorded command exit 0; command argv SHA-256
  89271759062811bdecd44b61893fc6c5e9f84d22e32c3680c24a59f1830bca23.

- 2026-10-08T17:34:18+00:00: Recorded command exit 0; command argv SHA-256
  d63e90f8ae54457d339f9b47686f46eba967265df5d7642f02d6501a1414dda7.

- 2026-10-08T17:35:29+00:00: Recorded command exit 0; command argv SHA-256
  3800c82124d3a3bd5076f14ef9f4015d941c14d433b648213f7e7f98b22f7194.

- 2026-10-08T17:36:23+00:00: Recorded command exit 0; command argv SHA-256
  01776cc343dc72841b6be96cc94385211af3f567a39ee755aa05cfdd729a120c.

- 2026-10-08T17:37:22+00:00: Recorded command exit 0; command argv SHA-256
  e715f1e7710a316d80a9064a93f4026cf086ee34e28008219a961375550ec482.

- 2026-10-08T17:38:29+00:00: Recorded command exit 0; command argv SHA-256
  43deabf539411468532103a845b08e52516b30a6e20b99d1145432b4963a4496.

- 2026-10-08T17:39:39+00:00: Recorded command exit 1; command argv SHA-256
  46b0463d9ed539cd84e65e997ecb9d9571e8df343ebc30e4c851d07dfe5625fc.

- 2026-10-08T17:40:23+00:00: Recorded command exit 0; command argv SHA-256
  2bbc8f4f0f4125bfc994cf95057cc8a4fa60bb76c8ebc5127a77d018f2935779.

- 2026-10-08T17:41:03+00:00: Recorded command exit 0; command argv SHA-256
  22cb95ff0d85fc0440379c12418996e08dab806f5bae5a4292a987d567092e52.

- 2026-10-08T17:42:12+00:00: Recorded command exit 0; command argv SHA-256
  fd78dfa56fa41d002935de144ab8a008f414b2bafc8c12d590b0d461585ab114.

- 2026-10-08T17:42:49+00:00: Recorded command exit 0; command argv SHA-256
  b9978a9768478b4fac353b36a0e9e95b094202a9b22ecb6b021234ed3cdd8534.

- 2026-10-08T17:44:04+00:00: Recorded command exit 0; command argv SHA-256
  5eea8a427c9a57ea2f558ec5c86789945653999259c3cf77417272ebb27803df.

- 2026-10-08T17:44:55+00:00: Recorded command exit 0; command argv SHA-256
  cb245c16ea28293d29b342611d152ffebc7d568569be45bfbdfcafed41884c66.

- 2026-10-08T17:45:39+00:00: Recorded command exit 12; command argv SHA-256
  80dc188013551b9d2dcdc7b74af8619dcc30df876d8deb5487ebb87a2fa16d2b.

- 2026-10-08T17:46:17+00:00: Recorded command exit 0; command argv SHA-256
  fdeb4253daa9df8b1c917332717e6494505617cf5d27d8164ce2830c47be57c5.

- 2026-10-08T17:46:55+00:00: Recorded command exit 5; command argv SHA-256
  2aae2265f1e6dec0c9c43f56a332dca8155568efcc4cdf0cbfbaf3ea27498bd5.

- 2026-10-08T17:47:40+00:00: Recorded command exit 1; command argv SHA-256
  d4cad40b7a8688c7636908c9b8113eda17610796d887bd7cfc462226600a38d1.

- 2026-10-08T17:49:50+00:00: Recorded command exit 1; command argv SHA-256
  75da18d879a32eefe687325d3ed4c8ee76b4978d01e06baa175956eb9313c48b.

- 2026-10-08T17:50:43+00:00: Recorded command exit 1; command argv SHA-256
  9c7a68d117c36bf8183561fd3817bece91718e1f7b4f4bdf13cdec31f05e36b7.

- 2026-10-08T17:51:23+00:00: Recorded command exit 0; command argv SHA-256
  b670188e94c8944bf1790db0f6014e9f33a6cd1982f9d8e9cc5bbd16187af03c.

- 2026-10-08T17:52:48+00:00: Recorded command exit 0; command argv SHA-256
  365705a1e124e3860b942a54890fac049776eb1e389b00c11eba9998aa38edce.

- 2026-10-08T17:53:17+00:00: Recorded command exit 1; command argv SHA-256
  796d7d1ed7b79fdc1d888c0a65f65adafd30f881bab11916e0847b99153f7126.

- 2026-10-08T17:53:47+00:00: Recorded command exit 0; command argv SHA-256
  f9535a1710caa4aa90fd3050bfc65744db68f1f58bdce8c6a803aaaebc230b1d.

- 2026-10-08T17:54:31+00:00: Recorded command exit 0; command argv SHA-256
  6c3fae1e52c9e718f6d822904b44b99ccaeb2cce67ebda5f91ebbb8c4dacfdba.

- 2026-10-08T17:55:20+00:00: Recorded command exit 0; command argv SHA-256
  97064ed7cb0c9d071cbf447c550d33c000c2c0f2b3ff79146cf5e6a782616a9d.

- 2026-10-08T17:56:45+00:00: Recorded command exit 0; command argv SHA-256
  aa057277b14752f4512606dbae84c1e311b43395938d79aa7e389f4dbd74f430.

- 2026-10-08T17:57:43+00:00: Recorded command exit 1; command argv SHA-256
  d297c0b0a581b166b49116fbc5ae7cb6f5093792793d5ba09c17bbdc36e09749.

- 2026-10-08T17:58:19+00:00: Recorded command exit 0; command argv SHA-256
  e6721fe6c82a8d3baf7c5273cd8d98f231162e20ad6a4a7e1c0ca9126c515760.

- 2026-10-08T17:59:06+00:00: Recorded command exit 1; command argv SHA-256
  6c3fae1e52c9e718f6d822904b44b99ccaeb2cce67ebda5f91ebbb8c4dacfdba.

- 2026-10-08T17:59:38+00:00: Recorded command exit 0; command argv SHA-256
  a8485bc578fa832f684c1d15b88c90fd5e02f735c47b373693535bb2ae479dc6.

- 2026-10-08T18:00:15+00:00: Recorded command exit 0; command argv SHA-256
  6c3fae1e52c9e718f6d822904b44b99ccaeb2cce67ebda5f91ebbb8c4dacfdba.

- 2026-10-08T18:00:56+00:00: Recorded command exit 0; command argv SHA-256
  91e411b2ca14fdbeab2e918129c0cf8f8b89c85c851eb40e3c06d2984a4254f7.

- 2026-10-08T18:02:03+00:00: Recorded command exit 1; command argv SHA-256
  d28dcd36fe2139b55ed5097dad019d42f53306625fcc04857a9e29071e799287.

- 2026-10-08T18:02:56+00:00: Recorded command exit 0; command argv SHA-256
  6e984ad65f7fb71f5a445d0d884382b3fbf195690b6a0d23b399e6a112f07017.

- 2026-10-08T18:04:27+00:00: Recorded command exit 101; command argv SHA-256
  07754ba7533aa3cd130e27b4aa2b6da57f71c000d2b2f2b3a097ddaf86c26cb4.

- 2026-10-08T18:05:32+00:00: Recorded command exit 101; command argv SHA-256
  ab5a9c92aaf85b753c7682039890e23f35d075b18d538e9be6114dd2986f23f8.

- 2026-10-08T18:06:13+00:00: Recorded command exit 0; command argv SHA-256
  85126b8b38c89ca1823cf2baea6599fad768cf4e2d6c563b6103dc47c8c8264e.

- 2026-10-08T18:06:50+00:00: Recorded command exit 0; command argv SHA-256
  0929435abe4feb91e69776e5a5192d27ba752d1d94e5759c90b9d2888c90e08d.

- 2026-10-08T18:07:24+00:00: Recorded command exit 0; command argv SHA-256
  51a4143eb35a51916331b3ef4eb07fbc474855a7735625c7d42a2adfb3ddb55b.

- 2026-10-08T18:08:55+00:00: Recorded command exit 0; command argv SHA-256
  ab5a9c92aaf85b753c7682039890e23f35d075b18d538e9be6114dd2986f23f8.

- 2026-10-08T18:10:09+00:00: Recorded command exit 0; command argv SHA-256
  425198fcaaff87f0bf83fd832687fe910831ddc4574fc59da86bb48d5ea8bfa9.

- 2026-10-08T18:12:20+00:00: Recorded command exit 0; command argv SHA-256
  2de4b1a3978070f7f22ebe7e49fb1e510ba4c1ea2f4dcebdc352d31afc071b38.

- 2026-10-08T18:12:59+00:00: Recorded command exit 0; command argv SHA-256
  5f911c67d347b3bc7b8025afe5325248af3c75656b6a20da65ed100e8312ddd7.

- 2026-10-08T18:13:41+00:00: Recorded command exit 1; command argv SHA-256
  7c269005a8a30ec5f599bf91fb0947d876aeee626fcb19acb840b01c68754e93.

- 2026-10-08T18:14:27+00:00: Recorded command exit 0; command argv SHA-256
  27a837858958e9b02be97773f30c325e2515ce965b3aa78d46cd7b889f1112c7.

- 2026-10-08T18:15:03+00:00: Recorded command exit 0; command argv SHA-256
  af326710efca773f617a97805edf40c05ab77988c1abbdc129079494e958e1d4.

- 2026-10-08T18:15:45+00:00: Recorded command exit 0; command argv SHA-256
  96e1203066957fc10044e44bea3bffce7e109064afc40eb18769b0d115eee368.

- 2026-10-08T18:16:40+00:00: Recorded command exit 0; command argv SHA-256
  434b673a65fa18b8acba005c4ee073f52e527f091d4cc1190aad215fbe738440.

- 2026-10-08T18:17:20+00:00: Recorded command exit 0; command argv SHA-256
  218343e6b2e9fa8f64ae6dea942aedf5f78f7b40ba48b5c437d4cd2576455c23.

- 2026-10-08T18:18:03+00:00: Recorded command exit 0; command argv SHA-256
  91196c8c1cb6a2bb800fb358d7d538dad138fa98e58155781e4e095fd8eb5fc8.

- 2026-10-08T18:18:56+00:00: Recorded command exit 0; command argv SHA-256
  84077bff7b6cefbf835176d8cc49a2b6fd57a736c3db483a1e6397d7534e33b3.

- 2026-10-08T18:19:31+00:00: Recorded command exit 0; command argv SHA-256
  6799f3a95abc42cb8362405102c707d6edf71ff988918b3116f260d066a21ba8.

- 2026-10-08T18:20:11+00:00: Recorded command exit 0; command argv SHA-256
  c41bb6591fe733e03bff1714a8a16f2e4f6e9b740bfd8b36ee29e81616a7c400.

- 2026-10-08T18:20:49+00:00: Recorded command exit 1; command argv SHA-256
  937b3d74617137c2232d72e656cfaf1a83c4cfdcbdfc63a76fe3903c4e9b903a.

- 2026-10-08T18:21:28+00:00: Recorded command exit 0; command argv SHA-256
  488f59d4d87e1d1222fa0c4d5478de6e7e3269a7514cb223d354b581f4aa0385.

- 2026-10-08T18:27:07+00:00: Recorded command exit 0; command argv SHA-256
  a697bb3a541d644e687cab2264fb45ae005ee9a48d5e4f4e6f0a097ed0160725.

- 2026-10-08T18:28:17+00:00: Recorded command exit 0; command argv SHA-256
  78762a6c913efa9f70aa1fcf60dccf53bf2f37d4fbbf6799ced4e57b82b7d766.

- 2026-10-08T18:29:12+00:00: Recorded command exit 0; command argv SHA-256
  58b321741371a9c4446b7e38f5814dda07731757fcf9aa157b3414c95e378015.

- 2026-10-08T18:29:58+00:00: Recorded command exit 1; command argv SHA-256
  9f0dc36c1944b736835593836fda952ceb22258ade07e54c9412e355390f79e1.

- 2026-10-08T18:30:31+00:00: Recorded command exit 0; command argv SHA-256
  203131779541b693a5eeb983203eccb8ae7c6b06c8aa2cc3149b377abc72deb0.

- 2026-10-08T18:49:43+00:00: Recorded command exit 0; command argv SHA-256
  21c83d27752532381b68931bcbcb5fa169ef446e9fdd844eb2c83726571066a3.

- 2026-10-08T18:50:39+00:00: Recorded command exit 1; command argv SHA-256
  34a0a4a3459facae8aa3809865742b67031404af903a033e033f7d11b3ad71fc.

- 2026-10-08T18:51:25+00:00: Recorded command exit 0; command argv SHA-256
  9fec2bd7aa4ae13b42c33e8202656d0d2c1b07e2db0dcb22e2c71b1b22c8615a.

- 2026-10-08T18:52:24+00:00: Recorded command exit 1; command argv SHA-256
  34a0a4a3459facae8aa3809865742b67031404af903a033e033f7d11b3ad71fc.

- 2026-10-08T18:53:48+00:00: Recorded command exit 0; command argv SHA-256
  9f0ade5a472c4ee3ac33978a6ab38b239c22dba19c5fb2b071fb462e074419e2.

- 2026-10-08T19:02:02+00:00: Recorded command exit 0; command argv SHA-256
  30d341e4e962becea9214199a4afc55c5ce5063870f2a6970ecd7833e7630405.

- 2026-10-08T19:02:46+00:00: Recorded command exit 0; command argv SHA-256
  28b06e3bcdba9162a3bcc7e8e2247f34d7fbb2b50b9a2bdefdaff2215faa29ca.

- 2026-10-08T19:03:34+00:00: Recorded command exit 1; command argv SHA-256
  9f0dc36c1944b736835593836fda952ceb22258ade07e54c9412e355390f79e1.

- 2026-10-08T19:04:23+00:00: Recorded command exit 0; command argv SHA-256
  c2f4e9ff25ae2d66a86f25d2c0f7ff211786d5c154a6b951d4d050ee0e3a419b.

- 2026-10-08T19:05:10+00:00: Recorded command exit 0; command argv SHA-256
  9f0dc36c1944b736835593836fda952ceb22258ade07e54c9412e355390f79e1.

- 2026-10-08T19:06:07+00:00: Recorded command exit 1; command argv SHA-256
  1c15a630ae2daa75e97295cff1270da9b63add6c913fbfdd38da4840a2ad3729.

- 2026-10-08T19:07:05+00:00: Recorded command exit 0; command argv SHA-256
  938313d595a7457a4f1b091de759e5e994f0de4a24fae18fa339e4f4b135aaf6.

- 2026-10-08T19:16:47+00:00: Recorded command exit 0; command argv SHA-256
  1f99b6585a776560240df57f845dba32ecd32f193d4b658788d1cd1936e3fdb5.

- 2026-10-08T19:17:38+00:00: Recorded command exit 1; command argv SHA-256
  7cff2e4a564bc140e04ee63e43281659a53c71234d7e9bc2caec1bd54fe7478e.

- 2026-10-08T19:18:21+00:00: Recorded command exit 0; command argv SHA-256
  7b604dff172f76e30c2431400d6622358f4ca1a3c6364ba403ab2e1417b255d9.

- 2026-10-08T19:19:20+00:00: Recorded command exit 0; command argv SHA-256
  ca6cb5b8fabed74ab1201f0aebcc1b4559c8959979d5c79cced4bafcb3d3f012.

- 2026-10-08T19:27:20+00:00: Recorded command exit 0; command argv SHA-256
  09c6b378731d65d6feb8694235c699361607565b0c2dadc4798303f62e415096.

- 2026-10-08T19:28:01+00:00: Recorded command exit 0; command argv SHA-256
  b06f0094b1877a8676b4aaea2d7df2292b44c9b2da64530d622630d2e90aaca3.

- 2026-10-08T19:28:58+00:00: Recorded command exit 0; command argv SHA-256
  4df7df561f19056db74f57d06822223e0f4577409e855a22cecd1297fbb988f1.

- 2026-10-08T19:38:49+00:00: Recorded command exit 1; command argv SHA-256
  5eaee305eeedc0729333588084a7c7d9a778fa20018d62155426d0e829413492.

- 2026-10-08T19:39:44+00:00: Recorded command exit 0; command argv SHA-256
  9744695b23f129b84f6824c02407a4a69b0c4eecd12c2ac311780db03f5d71ee.

- 2026-10-08T19:49:49+00:00: Recorded command exit 1; command argv SHA-256
  572b904162572408e611d0f60d9eb7c1651fa0c35aa23c3780a6497b3d525df5.

- 2026-10-08T20:17:00+00:00: Recorded command exit 0; command argv SHA-256
  3ff28b20c58d19b9e79b62433fb1279eed6b667e64329ebd06a96d7a7fb351d6.

- 2026-10-08T20:17:43+00:00: Recorded command exit 0; command argv SHA-256
  f3c03efcac8aa95064794d51004c4aed7acc7ab9031ce9d24b6629a890988a05.

- 2026-10-08T20:18:36+00:00: Recorded command exit 0; command argv SHA-256
  eb660a0c3ae56012d8affd62f2df30d5c33c5ac2145a9989b89afd902fd6726e.

- 2026-10-08T20:19:15+00:00: Recorded command exit 1; command argv SHA-256
  ddf369b60498657daccf963e31a1655201cfc96750f63dfe6480cb497fd609a9.

- 2026-10-08T20:19:58+00:00: Recorded command exit 0; command argv SHA-256
  bd72702454d9208d2dc19bc9de1437453f6ed8a01f1cff049f4f466e7b23be8d.

- 2026-10-08T20:21:05+00:00: Recorded command exit 0; command argv SHA-256
  631d5f5b60eb21dd1e929b1cb28bcdd3101ffa558c6e0eaca76e11bc67ca2ff5.

- 2026-10-08T20:21:42+00:00: Recorded command exit 0; command argv SHA-256
  376c2fe2f4af3644d0bfca4a76636f0792c551d6df4f4d10b6f3c9ed8cf61b34.
