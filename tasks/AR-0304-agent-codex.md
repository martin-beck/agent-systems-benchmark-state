---
{
  "branch": "feature/agent-codex",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T00:50:09+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0102"
  ],
  "id": "AR-0304",
  "next_action": "Add self-contained real Codex fixture test, then request shared registration fence.",
  "observed_branch": "feature/agent-codex",
  "observed_dirty": 4,
  "observed_head": "52b8b3b12d1fb2ae7cdda0afbc7f728d5e08f44a",
  "owner": "replay-20260906",
  "plan": "../plans/AR-0304.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Use Codex noninteractive structured events or app-server with declared capability boundaries.",
  "task_revision": 51,
  "title": "Implement Codex client adapter",
  "updated_at": "2026-09-06T23:43:15+00:00",
  "worktree_key": "agent-systems-benchmark-agent-codex"
}
---
## AR-0304

Use Codex noninteractive structured events or app-server with declared capability boundaries.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-06T23:15:34+00:00: Dependencies AR-0101 and AR-0102 are done; promote next
  highest-priority non-overlapping agent adapter after AR-0401 exact-head integration.

- 2026-09-06T23:15:49+00:00: Claimed by replay-20260906.

- 2026-09-06T23:17:35+00:00: Recorded command exit 0; command argv SHA-256
  1f8497443a221bad65419cfee2c5376e1032bff7ce540c15480c73f8bb45db44.

- 2026-09-06T23:18:32+00:00: Recorded command exit 0; command argv SHA-256
  ac067706cea3c3d019bf0d01bfe2b072f1f287e80805babf38ba7dac78c7e57b.

- 2026-09-06T23:20:09+00:00: Heartbeat by replay-20260906.

- 2026-09-06T23:20:41+00:00: Recorded command exit 0; command argv SHA-256
  bcb6aabffa3857c7f1f9e0353e247adaa14e467a703ce7c0216100cb7eff79f6.

- 2026-09-06T23:20:54+00:00: Recorded command exit 0; command argv SHA-256
  199b221a0a45d679ea08991590cef8650dd29b0e8bcb8685b0400739edf16b0b.

- 2026-09-06T23:21:49+00:00: Recorded command exit 2; command argv SHA-256
  cb76f2eadc7d84a08940326c617e2bf9e8f94bdca84bf86b5de2ac1eaaae9c80.

- 2026-09-06T23:22:21+00:00: Recorded command exit 127; command argv SHA-256
  2ee2528c11cf2efc48a33b76e535338b008e62f7e9b7b7b1d44eddbe97df9a65.

- 2026-09-06T23:22:53+00:00: Recorded command exit 127; command argv SHA-256
  4adc8807b746485a693a13b0bc41cf15020e7d4c144ed97d54ed8e062a2aba2d.

- 2026-09-06T23:23:39+00:00: Recorded command exit 1; command argv SHA-256
  9b04460509234c213de029b61f9775d444e3c0708511973a01d5ffc1489edad5.

- 2026-09-06T23:24:11+00:00: Recorded command exit 0; command argv SHA-256
  625d86dcec39a52fd965ace866f3c892838af287df1a22234ffd0a76070aa5db.

- 2026-09-06T23:24:19+00:00: Recorded command exit 1; command argv SHA-256
  31fba9016c3743a01a0082138d883bbbd12d128f8c4c09ecf6c7989cc70d9b9e.

- 2026-09-06T23:26:05+00:00: Recorded command exit 0; command argv SHA-256
  6c087395ad3d85044388ea34f0d00eb97c5d05740dc8719b8f6c8f1fa5fb54d0.

- 2026-09-06T23:26:16+00:00: Recorded command exit 1; command argv SHA-256
  15de9539d4cec79bbc621e077f56a49c3482b593446ec6aed8eb7d026ce0aac3.

- 2026-09-06T23:26:52+00:00: Recorded command exit 0; command argv SHA-256
  f26ffbfa2cb9da9e861c574a6ad36c7ba909068c4d3dfb802535d4290fd085ec.

- 2026-09-06T23:28:41+00:00: Recorded command exit 0; command argv SHA-256
  116bbc3c0fedc327369abbf49f43d526e1c2452ddc1b766fb1a84e27febb6538.

- 2026-09-06T23:29:26+00:00: Recorded command exit 0; command argv SHA-256
  b08ae6cdb2802d1ec6d8cb6be5676f0b670a990bd19eb125fa9cead3db3f6383.

- 2026-09-06T23:30:13+00:00: Recorded command exit 0; command argv SHA-256
  7cad7901cc1e6b631c3a8c09003b91497777c8ccf5362fd1051659f2292d523e.

- 2026-09-06T23:31:03+00:00: Recorded command exit 2; command argv SHA-256
  1ba8374ae79702f22fb8b7572a53d1a17ceee2d7ae9695a7cff9fc75d8586f68.

- 2026-09-06T23:31:18+00:00: Recorded command exit 0; command argv SHA-256
  c19bd12a9ee0eb0bf2ac6bca5fd804744890adc7a2d320886ba635d6dbc18a28.

- 2026-09-06T23:31:59+00:00: Recorded command exit 0; command argv SHA-256
  808d7e6a523920bcf2e4d5347b6de26d009075b73900f2ebfc243bc62e478940.

- 2026-09-06T23:32:21+00:00: Recorded command exit 0; command argv SHA-256
  3dc5c8a5422c4ed82811c86c874352a71a436bc6d9fd2da43272030b5f95fb77.

- 2026-09-06T23:32:32+00:00: Recorded command exit 127; command argv SHA-256
  88110329842f4c420defd8f48f26e36436b2bcd98c9d5ecfcfffc0def55152d6.

- 2026-09-06T23:33:04+00:00: Recorded command exit 101; command argv SHA-256
  9be5401ecfd0103fd3b497a9039e46169ab37a708ae310b7d77510f5f2683bae.

- 2026-09-06T23:33:24+00:00: Recorded command exit 0; command argv SHA-256
  b7363541e307301c54418d9d45c3e8bf6cb1e224b7edeca7eab78ca5f2762e03.

- 2026-09-06T23:33:37+00:00: Recorded command exit 101; command argv SHA-256
  061d0d4f6551736ac8b9511153fad99d66da3052311a23fb95bd5d38e89abc00.

- 2026-09-06T23:33:50+00:00: Recorded command exit 0; command argv SHA-256
  07eab9a54924e836219610402ea766e2a83214403c070084b950c15944752407.

- 2026-09-06T23:34:51+00:00: Recorded command exit 0; command argv SHA-256
  316739fd79f52944eff449bccfdcf864d06b6e65de0bc16dd68e1f81a30921b0.

- 2026-09-06T23:35:40+00:00: Recorded command exit 0; command argv SHA-256
  04125db281b9de3db765b440a00fb2ec8c8923db600efb22ac772deee3540b39.

- 2026-09-06T23:35:43+00:00: Recorded command exit 124; command argv SHA-256
  76a1c9ed16324b76ea34de6b5ad9fa4bd1e329b2177476b5ead8121d7cd0b548.

- 2026-09-06T23:36:01+00:00: Recorded command exit 0; command argv SHA-256
  a2a1c91a46f9a02736d0999496ba0ba585c37df1050f9562ddcb9411f8d1be15.

- 2026-09-06T23:36:52+00:00: Recorded command exit 0; command argv SHA-256
  635d13892cbffb6566a3648ffc1c911a496359a4002fc825dada3273d450cd4d.

- 2026-09-06T23:37:28+00:00: Recorded command exit 0; command argv SHA-256
  c9148fbd27abbaa555b23a1a9ef04cb4e67c9a4bcc2a380f3c47b226463aa302.

- 2026-09-06T23:38:10+00:00: Recorded command exit 0; command argv SHA-256
  72116cd52a08b35d4538a6d6de8890a0539040fda40000ed6393975c86adb8a0.

- 2026-09-06T23:38:15+00:00: Recorded command exit 0; command argv SHA-256
  fa9d6f13dda1ff293b8a30133b6cb0a9d435f6a94d1ef2a1430dcb05e16cca17.

- 2026-09-06T23:38:46+00:00: Recorded command exit 0; command argv SHA-256
  ca44fb20ff251a8b50fad6210e5d1abbe3700e928b61e9bed6e8f6f9b2e2c3bd.

- 2026-09-06T23:39:07+00:00: Recorded command exit 0; command argv SHA-256
  09e4f25fe28555a423e2e0cdf6599bd07382cc71e5e31e36174cbbfe5933123a.

- 2026-09-06T23:39:57+00:00: Recorded command exit 0; command argv SHA-256
  18533c2edd2ecea3e6b126eb1fb492981c3afaf4d71def0b7309a8886801f1d2.

- 2026-09-06T23:40:21+00:00: Recorded command exit 0; command argv SHA-256
  925a43e84508ce1163737eac8d63af13ff7d4b835496b9c514c61d1770803941.

- 2026-09-06T23:40:40+00:00: Recorded command exit 0; command argv SHA-256
  84a8236cb9a8e73983eafe5263e68aa703b6a8a65a6aa1c4b7091a7a479c7a93.

- 2026-09-06T23:41:01+00:00: Inspected installed Codex CLI 0.153.4 help and generated app-server
  schemas; pinned exercised x86_64 executable SHA-256
  56ef98ab4032d317ab26e9b5e5a175650717351edb16ed9cde0cb6d1734d62da without recording its private
  path. Official Codex exec/config/Responses docs establish --json JSONL, --ephemeral,
  model_provider/base_url/env_key/requires_openai_auth and responses-only wire API. Implemented
  isolated codex.rs plus CODEX.md: content pin, env/config isolation, unlinked prompt fd, explicit
  credential-free Responses provider, process-group cancellation, bounded duplicate-free JSONL
  decoder, redacted lifecycle/tool/usage results, and explicit unsupported
  subscription/app-server/WebSocket/replay/account routes. Isolated cargo test 6/6 and clippy -D
  warnings pass under /srv scratch. Initial cargo commands failed exit 127 because wrapper PATH
  omitted cargo; explicit /srv toolchain fixed environment. First real fixture attempt exited 124
  because the server handled a GET model probe then stopped; repaired server lifecycle. Real pinned
  binary credential-free loopback fixture then completed two Responses requests, executed
  exec_command write inside the declared /srv workspace, emitted thread/turn/tool/message/usage
  JSONL, and provider authorization/base route/model assertions passed. Ambient manual invocation
  exposed configured plugins; repeating with empty environment and isolated HOME removed app/plugin
  tools, matching adapter boundary. Scratch fixture script digest
  cdf6663a7b24eb871937f4da9b19533671b5f1ad3d32fa95e2a54b022432a26f before subsequent transparent
  repairs; scratch is not committed. Shared lib.rs/Cargo registration remains untouched due AR-0303
  overlap/fence.

- 2026-09-06T23:42:14+00:00: Recorded command exit 0; command argv SHA-256
  534f75b1c4956049758cab19882c20e406a93b86ca10adcee03acf2b0d202e55.

- 2026-09-06T23:42:33+00:00: Recorded command exit 101; command argv SHA-256
  2e8bb7f2617b355ffbbc46b865da8ddd37d668f4261e191ec8342e0a3b6d8fc3.

- 2026-09-06T23:42:42+00:00: Recorded command exit 0; command argv SHA-256
  8640805c70c3eed86b06459691e35f7b5b202b2cd64d9476cd2e19d23e28e551.

- 2026-09-06T23:43:15+00:00: Recorded command exit 101; command argv SHA-256
  e76455592dff5452ccbcf9f351478833018458b7969ddc0cd92f41a00def7a93.
