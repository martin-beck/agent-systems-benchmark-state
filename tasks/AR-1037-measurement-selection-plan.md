---
{
  "branch": "feature/measurement-selection-plan",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T06:32:03+00:00",
  "depends_on": [
    "AR-0104",
    "AR-1036"
  ],
  "id": "AR-1037",
  "next_action": "After AR-1036, add canonical measurement IDs to validated ASB plans and make collection honor them without any UI code.",
  "observed_branch": "feature/measurement-selection-plan",
  "observed_dirty": 9,
  "observed_head": "a01f38f20982516fc93f58482e536896c49246df",
  "owner": "codex-root-ar1037-selection-20260911",
  "plan": "../plans/AR-1037.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Carry catalog-backed measurement choices through ASB plan validation, collection and evidence.",
  "task_revision": 104,
  "title": "Add measurement selection to validated run plans",
  "updated_at": "2026-09-11T04:44:01+00:00",
  "worktree_key": "agent-systems-benchmark-measurement-selection-plan"
}
---
## AR-1037

Implement only the ASB runner/control semantics required to make measurement choices real: closed
plan fields, catalog validation, canonical hashing, source gating and evidence provenance. All
search, group tri-state behavior, selection/deselection controls, rendering and help remain
exclusively in `martin-beck/asb-tui` under AR-1014.

- 2026-09-11T03:31:52+00:00: Dependencies AR-0104 and AR-1036 are done; fully green protected-main
  descendant 1a19b692 qualifies the catalog control boundary. Promote ASB-only measurement selection
  semantics with no frontend implementation.

- 2026-09-11T03:32:03+00:00: Claimed by codex-root-ar1037-selection-20260911.

- 2026-09-11T03:32:25+00:00: Recorded command exit 0; command argv SHA-256
  e93ce83471cb6810cbe793116d30cf552be146bcaee414eb9dd68d1b35c47e90.

- 2026-09-11T03:40:05+00:00: Recorded command exit 101; command argv SHA-256
  f8f5cfd8b7ce540eefbcf1ed8593289dcea998c3c67ea623a330a2542845d0e8.

- 2026-09-11T03:40:29+00:00: Recorded command exit 0; command argv SHA-256
  dc4208b7165aebbd5611033bf943ec0ee209e69a0410bd55afd62e8f31008cbd.

- 2026-09-11T03:41:28+00:00: Recorded command exit 1; command argv SHA-256
  0ea6fe112897f4953580feb3bbd086ea218eaea05048e5dfabc08e70b91b8c71.

- 2026-09-11T03:41:41+00:00: Recorded command exit 0; command argv SHA-256
  09c15c70d984c743b03913b5a4a636b645d98c882e9c14f86f69af03ba63b252.

- 2026-09-11T03:41:59+00:00: Recorded command exit 0; command argv SHA-256
  9ccfcfa9c389668cf5c8f871d8115e0a1d8e06c78ef5b3135f5f0f79d08664ab.

- 2026-09-11T03:45:25+00:00: Recorded command exit 101; command argv SHA-256
  476105f72caa4cc95ff415ef324a9ee1e1a12507c57629e7848ad27364dad583.

- 2026-09-11T03:46:13+00:00: Recorded command exit 0; command argv SHA-256
  476105f72caa4cc95ff415ef324a9ee1e1a12507c57629e7848ad27364dad583.

- 2026-09-11T03:46:43+00:00: Recorded command exit 101; command argv SHA-256
  baf579661282d83e638b954ec98e02553246afabb34f1d5c8487dd77135c9272.

- 2026-09-11T03:47:42+00:00: Recorded command exit 0; command argv SHA-256
  09c15c70d984c743b03913b5a4a636b645d98c882e9c14f86f69af03ba63b252.

- 2026-09-11T03:48:05+00:00: Recorded command exit 0; command argv SHA-256
  baf579661282d83e638b954ec98e02553246afabb34f1d5c8487dd77135c9272.

- 2026-09-11T03:49:42+00:00: Recorded command exit 101; command argv SHA-256
  1a30159cf316e006bd585fb4c6ea47760f8381910b664cd68ee3eb97f0cfba26.

- 2026-09-11T03:50:08+00:00: Recorded command exit 0; command argv SHA-256
  3f6b94c7ee5251023b9777cd611070f333030f05751c7ff6efc759f69f112bb5.

- 2026-09-11T03:50:24+00:00: Recorded command exit 0; command argv SHA-256
  84735ce5b140a26f41287c5e9470022eb54e2354bb57b1dc53154eda2deac183.

- 2026-09-11T03:50:45+00:00: Recorded command exit 101; command argv SHA-256
  effb686fd5ddcae8042cee59da0779f82e1f6dac9272213feae15475372b7d48.

- 2026-09-11T03:52:06+00:00: Recorded command exit 0; command argv SHA-256
  09c15c70d984c743b03913b5a4a636b645d98c882e9c14f86f69af03ba63b252.

- 2026-09-11T03:52:25+00:00: Recorded command exit 101; command argv SHA-256
  effb686fd5ddcae8042cee59da0779f82e1f6dac9272213feae15475372b7d48.

- 2026-09-11T03:54:43+00:00: Recorded command exit 0; command argv SHA-256
  09c15c70d984c743b03913b5a4a636b645d98c882e9c14f86f69af03ba63b252.

- 2026-09-11T03:54:59+00:00: Recorded command exit 0; command argv SHA-256
  66b605b717c5a7e0669e4c3b56b03e3292b60b93599cb2aac180bc48b4807143.

- 2026-09-11T03:56:53+00:00: Recorded command exit 101; command argv SHA-256
  090b850845d3902400b8dba91f08d8fd0686ea1771d7e661c10a4475f2c78c9d.

- 2026-09-11T03:57:37+00:00: Recorded command exit 0; command argv SHA-256
  090b850845d3902400b8dba91f08d8fd0686ea1771d7e661c10a4475f2c78c9d.

- 2026-09-11T03:59:42+00:00: Recorded command exit 0; command argv SHA-256
  2ae237e8bf230a319428216a20d8d44a784760418ac276e5456c7ba8a40e7b62.

- 2026-09-11T04:00:22+00:00: Recorded command exit 0; command argv SHA-256
  b261f2db642db5afa1636ea290ff223389d8206813eea15fee65fe9f83827b97.

- 2026-09-11T04:05:25+00:00: Recorded command exit 0; command argv SHA-256
  09c15c70d984c743b03913b5a4a636b645d98c882e9c14f86f69af03ba63b252.

- 2026-09-11T04:05:41+00:00: Recorded command exit 101; command argv SHA-256
  ab5db4159478c7bb637151e6412eb5eb2f80528493a4950e3d63fa25aaae3b50.

- 2026-09-11T04:06:01+00:00: Recorded command exit 101; command argv SHA-256
  ab5db4159478c7bb637151e6412eb5eb2f80528493a4950e3d63fa25aaae3b50.

- 2026-09-11T04:07:02+00:00: Recorded command exit 0; command argv SHA-256
  09c15c70d984c743b03913b5a4a636b645d98c882e9c14f86f69af03ba63b252.

- 2026-09-11T04:07:28+00:00: Recorded command exit 0; command argv SHA-256
  ab5db4159478c7bb637151e6412eb5eb2f80528493a4950e3d63fa25aaae3b50.

- 2026-09-11T04:07:50+00:00: Recorded command exit 101; command argv SHA-256
  effb686fd5ddcae8042cee59da0779f82e1f6dac9272213feae15475372b7d48.

- 2026-09-11T04:09:41+00:00: Recorded command exit 0; command argv SHA-256
  7a423e08b2040b2558c8d3853534387da26cd917d95acf109bb9ffd1f074085f.

- 2026-09-11T04:11:13+00:00: Recorded command exit 101; command argv SHA-256
  effb686fd5ddcae8042cee59da0779f82e1f6dac9272213feae15475372b7d48.

- 2026-09-11T04:12:14+00:00: Recorded command exit 0; command argv SHA-256
  09c15c70d984c743b03913b5a4a636b645d98c882e9c14f86f69af03ba63b252.

- 2026-09-11T04:12:45+00:00: Recorded command exit 101; command argv SHA-256
  effb686fd5ddcae8042cee59da0779f82e1f6dac9272213feae15475372b7d48.

- 2026-09-11T04:13:07+00:00: Recorded command exit 0; command argv SHA-256
  dc4208b7165aebbd5611033bf943ec0ee209e69a0410bd55afd62e8f31008cbd.

- 2026-09-11T04:13:29+00:00: Recorded command exit 0; command argv SHA-256
  3b7d06ce0619f0624c1733d6f57d0ca676bc5d886e1fee3b81496810a6408148.

- 2026-09-11T04:13:49+00:00: Recorded command exit 0; command argv SHA-256
  053f1638aa53c5bfb58c4b51315447c9fdf9a78d5d33c6434abc748067e78835.

- 2026-09-11T04:14:04+00:00: Recorded command exit 0; command argv SHA-256
  31d4ced0013afeccc0a324eed65c1f743d315f3888be3187f310d251d812d7a1.

- 2026-09-11T04:14:24+00:00: Recorded command exit 0; command argv SHA-256
  60a46a7cb90a6c7a92e02edcd2458c9019671d40611d3eb5f3dc6577cf91b660.

- 2026-09-11T04:15:31+00:00: Recorded command exit 0; command argv SHA-256
  40f0936cb1081edaa92a9570992ef27d1d30dcf3d1a171df0cd63f0da2c2c9fc.

- 2026-09-11T04:16:57+00:00: Recorded command exit 0; command argv SHA-256
  0ea6fe112897f4953580feb3bbd086ea218eaea05048e5dfabc08e70b91b8c71.

- 2026-09-11T04:17:05+00:00: Recorded command exit 1; command argv SHA-256
  7e404920ce7d70d501afb19ed1a98381144f4d23405be01737ae73c162b72b6c.

- 2026-09-11T04:17:22+00:00: Recorded command exit 0; command argv SHA-256
  296f46e63def08424842fa538a108a613d92ef0f6ec66bf61366618b5c525dc5.

- 2026-09-11T04:17:40+00:00: Recorded command exit 0; command argv SHA-256
  ccdd6c4088d0260bfad7e4e60d3965bc70b66257007d6c02d0bc95de91117b8c.

- 2026-09-11T04:18:30+00:00: Recorded command exit 0; command argv SHA-256
  ea67df0a48df945f20cf8d159c5881e5750832e76dad52e0389e6acfb4ab8881.

- 2026-09-11T04:18:45+00:00: Recorded command exit 0; command argv SHA-256
  5bcbab346d86bbcf6b93fb191ec26448d31be456e4077668fbf75b1cb18fbd1b.

- 2026-09-11T04:19:20+00:00: Recorded command exit 0; command argv SHA-256
  df68e75629258051b97d951e77a5b523910caff36afb5a6e167c20a08fc09daa.

- 2026-09-11T04:19:35+00:00: Recorded command exit 0; command argv SHA-256
  bb1701dc5fdc90559ccdc6fed827d5c60ef58eaccb12055cf4a5ec967f5bd4e3.

- 2026-09-11T04:19:42+00:00: Recorded command exit 0; command argv SHA-256
  c993bbb987b9b38ee7ad85b02f76d10cd7098afa2f2272178fcc6e344dd1b63e.

- 2026-09-11T04:20:08+00:00: Recorded command exit 0; command argv SHA-256
  3b607b70d3e9cdcceed161b94351148d4886da923032ecb8a1d5ec2aad473bac.

- 2026-09-11T04:20:15+00:00: Recorded command exit 0; command argv SHA-256
  48814298bc5421d691ac2bd21debcb0a8db24235f4d59da8d99351e52ec92c48.

- 2026-09-11T04:20:23+00:00: Recorded command exit 0; command argv SHA-256
  214f13e0769508baaa8264794600c2d832cbd62f238bac278ab7a7d73b89fe13.

- 2026-09-11T04:20:38+00:00: Recorded command exit 1; command argv SHA-256
  5818b76ac3c65cf07db2139769405c28eb66392436582c0c22ce7ca8a6b9c8dd.

- 2026-09-11T04:26:53+00:00: Recorded command exit 127; command argv SHA-256
  ebe1fca530a16ad94ee824371fbb281c6af9ce884e4007601bf8f7d7644d85ef.

- 2026-09-11T04:27:26+00:00: Recorded command exit 101; command argv SHA-256
  1b1924f9d97856e2a45cd2be13a3629e3ad8c002e0086572538c5d42d2c8dffe.

- 2026-09-11T04:27:47+00:00: Recorded command exit 0; command argv SHA-256
  9abacb603cb523aad9692c4f128eff1dac2750ee6abb572cbf9bb31d80c62aed.

- 2026-09-11T04:28:13+00:00: Recorded command exit 0; command argv SHA-256
  1daae83a6d7e92321ee0deff0417fde2fbdf26ebc20eb0c65590e048a1f0f3ad.

- 2026-09-11T04:28:33+00:00: Recorded command exit 0; command argv SHA-256
  745eb87872c7ec5e07fed60b06752b22353ab2e3fdfbe69b69e25537d56d7853.

- 2026-09-11T04:28:49+00:00: Recorded command exit 0; command argv SHA-256
  884f854c8cc9076d0e2ae375ecf16dd9f23af12088a7af3a32b1849877800049.

- 2026-09-11T04:29:49+00:00: Recorded command exit 101; command argv SHA-256
  2af870897a745423cd80238d934c2081aaf5106daac66b47f46aa2d24a4e3096.

- 2026-09-11T04:30:05+00:00: Recorded command exit 101; command argv SHA-256
  41a5f6888f65ffd48ec0bd84e17dc822b72baf888b1ad7603b6a5e0e26f8e6c9.

- 2026-09-11T04:30:58+00:00: Recorded command exit 0; command argv SHA-256
  634374708e42699582fefca1f819af94738c47da2fe8713e6f9018c7c77be2c0.

- 2026-09-11T04:31:07+00:00: Recorded command exit 0; command argv SHA-256
  0e52810a7a81754dc9fd6e4343a2fdd63beb4d0f890ab57cb644b5162154871c.

- 2026-09-11T04:36:27+00:00: Recorded command exit 0; command argv SHA-256
  09c15c70d984c743b03913b5a4a636b645d98c882e9c14f86f69af03ba63b252.

- 2026-09-11T04:37:01+00:00: Recorded command exit 101; command argv SHA-256
  fb732a0bd33297ceb53e3a6d7426daf84d11b9a09f07430c79cdc6919d1b51f5.

- 2026-09-11T04:38:04+00:00: Recorded command exit 0; command argv SHA-256
  a0e093e56de0ba509355b06826e3b14783b67e4957c4d1ae4e2f266ae48426a7.

- 2026-09-11T04:38:40+00:00: Recorded command exit 0; command argv SHA-256
  60056ce0c6f8110edf4e0da8588f45f06793d2b6250807226d626888f1c65eb2.

- 2026-09-11T04:38:51+00:00: Recorded command exit 0; command argv SHA-256
  40526df3d1f866e95a727280db43068526fde4681d822bdabfb5d2aad3d66309.

- 2026-09-11T04:39:20+00:00: Recorded command exit 0; command argv SHA-256
  9877de4e8ce2a9a25440f7aeae6f69fee6a10b9534294b9639701beadd36445e.

- 2026-09-11T04:39:43+00:00: Recorded command exit 0; command argv SHA-256
  2c93161c406a42f7f5a201c0e04d2c17268d98d1a4a1f763bcdb63acd73d4b2d.

- 2026-09-11T04:42:56+00:00: Recorded command exit 0; command argv SHA-256
  09c15c70d984c743b03913b5a4a636b645d98c882e9c14f86f69af03ba63b252.

- 2026-09-11T04:43:15+00:00: Recorded command exit 0; command argv SHA-256
  a0e093e56de0ba509355b06826e3b14783b67e4957c4d1ae4e2f266ae48426a7.

- 2026-09-11T04:43:47+00:00: Recorded command exit 0; command argv SHA-256
  09c15c70d984c743b03913b5a4a636b645d98c882e9c14f86f69af03ba63b252.

- 2026-09-11T04:43:55+00:00: Recorded command exit 0; command argv SHA-256
  a0e093e56de0ba509355b06826e3b14783b67e4957c4d1ae4e2f266ae48426a7.
