---
{
  "branch": "feature/terminal-interface",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T02:37:14+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0104",
    "AR-0204"
  ],
  "id": "AR-0801",
  "next_action": "Add failure-path and PTY/resize-adjacent terminal tests, run workspace/full quality/formal gates, then create a focused signed DCO candidate for independent immutable review.",
  "observed_branch": "feature/terminal-interface",
  "observed_dirty": 0,
  "observed_head": "3374572d09476bc45ceeac84776d73f52cee8211",
  "owner": "root-coordination-20260906",
  "plan": "../plans/AR-0801.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide doctor, plan, run, sweep, compare and report with stable JSON output.",
  "task_revision": 95,
  "title": "Implement terminal and automation interfaces",
  "updated_at": "2026-09-07T01:53:17+00:00",
  "worktree_key": "agent-systems-benchmark-terminal-interface"
}
---
## AR-0801

Provide doctor, plan, run, sweep, compare and report with stable JSON output.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-07T01:07:00+00:00: Dependencies AR-0101, AR-0104, and AR-0204 are durably done on
  synchronized signed product main b79534b; asb-cli ownership is disjoint from active Gemini, Goose,
  and mini-SWE adapter paths.

- 2026-09-07T01:07:14+00:00: Claimed by root-coordination-20260906.

- 2026-09-07T01:07:33+00:00: Recorded command exit 0; command argv SHA-256
  363c68c50f2b2e053c643e4c2b2f71566885660eb8e7d143586d2c240ab187b5.

- 2026-09-07T01:08:21+00:00: Fresh snapshot read after claim. Declared ownership: crates/asb-cli/**
  plus only its required Cargo dependency/lock integration and dedicated CLI fixtures; no asb-agents
  registration, schemas, or active adapter paths. Root holds the serialized Cargo.lock fence for
  AR-0801; Gemini separately holds only the additive asb-agents lib.rs fence.

- 2026-09-07T01:10:52+00:00: Recorded command exit 0; command argv SHA-256
  ad10ed9ff5eac4e58674b8db7e75e27da84a50f5ed14019df1f28374c7acefd0.

- 2026-09-07T01:11:10+00:00: Recorded command exit 0; command argv SHA-256
  3dd3eaf82bf30b385e1b3f64d82c82f503819d1d27cb5394e36d9e648c9522b9.

- 2026-09-07T01:11:23+00:00: Recorded command exit 101; command argv SHA-256
  43c75150b89cb4cd84e541d9b8a224e5343e69e1388fda77b8f9640574675ba7.

- 2026-09-07T01:11:34+00:00: Recorded command exit 0; command argv SHA-256
  149425b7cb1d24082dec8dec4c4b52f3a3066a79b954892dc2d0692139414a2b.

- 2026-09-07T01:11:47+00:00: Recorded command exit 0; command argv SHA-256
  8cb5de329818bcd8e38406d96ed5a7f1b0aa89664e3613fbdac4e3e5e89ba339.

- 2026-09-07T01:12:15+00:00: Recorded command exit 0; command argv SHA-256
  43c75150b89cb4cd84e541d9b8a224e5343e69e1388fda77b8f9640574675ba7.

- 2026-09-07T01:13:17+00:00: Recorded command exit 0; command argv SHA-256
  57502537a44a55474c5893c492744114e25880e605a7783c8ddcaf37ffb60c25.

- 2026-09-07T01:15:26+00:00: Recorded command exit 0; command argv SHA-256
  b80b21714c4b44788133d3e61f7c55e11ffe7b7374b00edda452b8dd1b6767bb.

- 2026-09-07T01:22:03+00:00: Recorded command exit 2; command argv SHA-256
  cb76f2eadc7d84a08940326c617e2bf9e8f94bdca84bf86b5de2ac1eaaae9c80.

- 2026-09-07T01:23:03+00:00: Recorded command exit 0; command argv SHA-256
  6302896ef9d6d14694c9e0d12bebfcfcb1fbce54550bc0e56c0fe0432e376573.

- 2026-09-07T01:24:00+00:00: Recorded command exit 0; command argv SHA-256
  2f212fbc8592687c62420636e0ab8c76f48a1245ce27535173e1986bf60c7dd3.

- 2026-09-07T01:24:40+00:00: Recorded command exit 0; command argv SHA-256
  f9a894ddb0db51511612d7f5eaaea565eec0bb0f2433c6e75b954223a53de429.

- 2026-09-07T01:25:21+00:00: Recorded command exit 1; command argv SHA-256
  3c03ded811b49e82d94de91e5c4ab957950034ed389c4b58ec65a25d312a2946.

- 2026-09-07T01:25:35+00:00: Recorded command exit 0; command argv SHA-256
  d71c685daeb1d8edc5209b98ce247460b7c1cc66d24dfbed10c9d1e2857f6674.

- 2026-09-07T01:25:45+00:00: Recorded command exit 101; command argv SHA-256
  8b6f5f97e0d3fbb67a605d8764ad01cacd8d35ab473bc497967f608c1429ef18.

- 2026-09-07T01:26:15+00:00: Recorded command exit 101; command argv SHA-256
  a0d915a338e74165aa7b1cc653ab2ef5ed0e104cb45ee259615ebc8aacb1be99.

- 2026-09-07T01:26:27+00:00: Recorded command exit 0; command argv SHA-256
  2f7e887b1574407bd34f87f830235098a23fdd948dbd52ec28fa4795d8067859.

- 2026-09-07T01:26:38+00:00: Recorded command exit 0; command argv SHA-256
  3c03ded811b49e82d94de91e5c4ab957950034ed389c4b58ec65a25d312a2946.

- 2026-09-07T01:26:45+00:00: Recorded command exit 0; command argv SHA-256
  cac4becf7f56a962f8fe515eca48b56d04d6de23868db08122a72280f7b04850.

- 2026-09-07T01:29:04+00:00: Recorded command exit 0; command argv SHA-256
  85fafbdc6787024f7053c4fd643f87a79a79c29670dc6dfefde1c831a5b48493.

- 2026-09-07T01:30:02+00:00: Recorded command exit 0; command argv SHA-256
  1d90fd84e6d55912eb2be49f761062663b5ebbd5f9ecaeb131c41febbc1dcd57.

- 2026-09-07T01:30:19+00:00: Recorded command exit 0; command argv SHA-256
  db137ece179e9f96fef7c126a22bbc479445c3e41c1e7bca026945f65e9a3eff.

- 2026-09-07T01:30:36+00:00: Recorded command exit 101; command argv SHA-256
  e3226e09ed262c5b980bdb2a3d26d56462f9c8d10e016352ba2be60128245435.

- 2026-09-07T01:30:59+00:00: Recorded command exit 0; command argv SHA-256
  2ccd5477e89422f462cc5c736e1c6f7ef46565c7ea8a50440bac79624a7e62a5.

- 2026-09-07T01:31:17+00:00: Recorded command exit 101; command argv SHA-256
  e3226e09ed262c5b980bdb2a3d26d56462f9c8d10e016352ba2be60128245435.

- 2026-09-07T01:31:33+00:00: Recorded command exit 1; command argv SHA-256
  1033f0b3aa4b7dd4b5551b3285a380fb73aeb54d53fe3e9656584bf037152cc6.

- 2026-09-07T01:31:54+00:00: Recorded command exit 0; command argv SHA-256
  5c59888bd501526b9432cb28b567c49446f66e9ee02a77cecccca51db9e422bc.

- 2026-09-07T01:32:06+00:00: Recorded command exit 101; command argv SHA-256
  aa4af57774166589c10457d7ea71b9013e886d4876c0b3296b5921ef2a30fd58.

- 2026-09-07T01:32:33+00:00: Recorded command exit 0; command argv SHA-256
  4d6952da5bfeac4435ddf7d97849078ab35566e2f087309930c79a192b052f03.

- 2026-09-07T01:32:46+00:00: Recorded command exit 101; command argv SHA-256
  e3226e09ed262c5b980bdb2a3d26d56462f9c8d10e016352ba2be60128245435.

- 2026-09-07T01:33:05+00:00: Recorded command exit 0; command argv SHA-256
  d436adae869d5b9b6e036201c6023b3d3f145cae7721d05a2735334498542083.

- 2026-09-07T01:33:23+00:00: Recorded command exit 0; command argv SHA-256
  e3226e09ed262c5b980bdb2a3d26d56462f9c8d10e016352ba2be60128245435.

- 2026-09-07T01:34:16+00:00: Recorded command exit 0; command argv SHA-256
  72c7c727e4661e0eda438da33e6a03f78f81f528ccc152f8a37231de16f52fac.

- 2026-09-07T01:34:41+00:00: Recorded command exit 0; command argv SHA-256
  8132e05105fadef022e8cd36ee9812252fa98f22151efb340f442379cdbc6c4f.

- 2026-09-07T01:34:59+00:00: Recorded command exit 0; command argv SHA-256
  db137ece179e9f96fef7c126a22bbc479445c3e41c1e7bca026945f65e9a3eff.

- 2026-09-07T01:35:05+00:00: Recorded command exit 0; command argv SHA-256
  1e65c04f56c34ddcd81928f295ae75acd318cee7965056f1a4f0d243419d9b4c.

- 2026-09-07T01:35:11+00:00: Recorded command exit 0; command argv SHA-256
  e3226e09ed262c5b980bdb2a3d26d56462f9c8d10e016352ba2be60128245435.

- 2026-09-07T01:36:27+00:00: Recorded command exit 1; command argv SHA-256
  8cbe4d5e274381e44c1698cbe3f36931a7eee660ebbc1eaaafea1ae8f4bac0d8.

- 2026-09-07T01:36:53+00:00: Recorded command exit 0; command argv SHA-256
  bab86e5b091743457c2d7b091b3220d7e3a79d62c67d868c8ee4ab3d1fcf289d.

- 2026-09-07T01:37:52+00:00: Recorded command exit 0; command argv SHA-256
  2679c9a9b8daab031fa3b0928009fbe9121de1ee023cc3180a3301b93320488c.

- 2026-09-07T01:38:03+00:00: Recorded command exit 0; command argv SHA-256
  db137ece179e9f96fef7c126a22bbc479445c3e41c1e7bca026945f65e9a3eff.

- 2026-09-07T01:38:09+00:00: Recorded command exit 101; command argv SHA-256
  e3226e09ed262c5b980bdb2a3d26d56462f9c8d10e016352ba2be60128245435.

- 2026-09-07T01:38:28+00:00: Recorded command exit 1; command argv SHA-256
  d2bbbc4e117eb4062f74078633c7e440df8f1ee8a8549d1597b24b70aef728e3.

- 2026-09-07T01:38:41+00:00: Recorded command exit 0; command argv SHA-256
  360536495ba121b7b710c7ce44350c7846851619fc4fc9707ab756cb1d4c678f.

- 2026-09-07T01:38:57+00:00: Recorded command exit 0; command argv SHA-256
  e3226e09ed262c5b980bdb2a3d26d56462f9c8d10e016352ba2be60128245435.

- 2026-09-07T01:39:20+00:00: Recorded command exit 0; command argv SHA-256
  acceaa8242f67686fee41a74c673fa6b78dd7bd7bfbfad23cea957128c14fde5.

- 2026-09-07T01:39:32+00:00: Recorded command exit 0; command argv SHA-256
  db137ece179e9f96fef7c126a22bbc479445c3e41c1e7bca026945f65e9a3eff.

- 2026-09-07T01:39:41+00:00: Recorded command exit 0; command argv SHA-256
  e3226e09ed262c5b980bdb2a3d26d56462f9c8d10e016352ba2be60128245435.

- 2026-09-07T01:40:01+00:00: Recorded command exit 1; command argv SHA-256
  038ed5a8e41c9d36a69a0e6b5b3b4c35c02ab862b0f047914ebdd90221bb7f53.

- 2026-09-07T01:40:25+00:00: Recorded command exit 101; command argv SHA-256
  0dfcd5d1f06de9d564dad0abe30b91f0e84df8aa34e9c584b7e961b742f50464.

- 2026-09-07T01:41:06+00:00: Recorded command exit 0; command argv SHA-256
  1bb53d9ef4dc322353a17ff53acd951783bc9e83a5a57ce4cf49966a7d5740bb.

- 2026-09-07T01:41:38+00:00: Recorded command exit 0; command argv SHA-256
  c13e3f19cbac3bd37e9ea5761f211ab6037076c6a238386ea6a7e9f427577d6b.

- 2026-09-07T01:41:55+00:00: Recorded command exit 0; command argv SHA-256
  e4c3c12e5fcdb9a9425ee92b9c1ce799246ce07729c1d916e88471d90b82396d.

- 2026-09-07T01:42:56+00:00: Recorded command exit 0; command argv SHA-256
  f42df6d908810b8ef89682c04d6396241a83242efe9a0c80934c9fdcd9857e7a.

- 2026-09-07T01:43:10+00:00: Recorded command exit 0; command argv SHA-256
  db137ece179e9f96fef7c126a22bbc479445c3e41c1e7bca026945f65e9a3eff.

- 2026-09-07T01:43:21+00:00: Recorded command exit 0; command argv SHA-256
  e3226e09ed262c5b980bdb2a3d26d56462f9c8d10e016352ba2be60128245435.

- 2026-09-07T01:43:40+00:00: Recorded command exit 0; command argv SHA-256
  6507c5870a79ad471fc7024721449b38c8a34b1bd3bb29f0da9f1cf0e36b149e.

- 2026-09-07T01:44:29+00:00: Implemented compiling doctor/plan/run/sweep/compare/report boundary in
  declared worktree. Strict TOML and exact executable digest validate before launch; nonempty
  unpinned argv is rejected in favor of a pinned wrapper. Real scheduler/workload/store/metrics
  integration, protected grading, JSON-only result stream, stderr progress, timeout and SIGINT
  process-group cancellation are green. Focused evidence: 8 unit plus 2 native executable e2e tests
  green; warmup/measured accounting, failed run, two-point sweep, report/comparison, invalid-plan
  no-side-effect, timeout cleanup and descendant cleanup covered. cargo-llvm-cov focused
  denominator: 1,796 regions / 1,190 lines, 90.14% regions and 91.01% lines; installed LLVM exposes
  no branch denominator. Earlier failures recorded: bare cargo unavailable under sanitized handoff
  PATH; store lifecycle omitted Planned; fixture printf interpreted CR; each was investigated and
  repaired.

- 2026-09-07T01:44:53+00:00: Recorded command exit 0; command argv SHA-256
  9c75ab35cfdb9db2f397a7c4385ff99e0e0e4af1304727ae6746f778308363c9.

- 2026-09-07T01:45:07+00:00: Recorded command exit 1; command argv SHA-256
  fed2a82cf419d707d0d8e002b9240967534b0fae5ac12877f52913cbf6bd441f.

- 2026-09-07T01:45:13+00:00: Recorded command exit 101; command argv SHA-256
  e3226e09ed262c5b980bdb2a3d26d56462f9c8d10e016352ba2be60128245435.

- 2026-09-07T01:45:26+00:00: Recorded command exit 0; command argv SHA-256
  89a3496e5117075971d12508ecfd25c942e156da699b78047d054b6d539ba181.

- 2026-09-07T01:45:37+00:00: Recorded command exit 0; command argv SHA-256
  e3226e09ed262c5b980bdb2a3d26d56462f9c8d10e016352ba2be60128245435.

- 2026-09-07T01:46:44+00:00: Recorded command exit 0; command argv SHA-256
  41a8e805595160361ac4fecb9cfc5d65a9470b0db252693cbd0be3ea06f471bf.

- 2026-09-07T01:46:59+00:00: Recorded command exit 0; command argv SHA-256
  ebd7308980661021ee6af3520e1fd0f0ac1ae91e31376f2df6745d55b31f31a2.

- 2026-09-07T01:47:37+00:00: Recorded command exit 0; command argv SHA-256
  fed2a82cf419d707d0d8e002b9240967534b0fae5ac12877f52913cbf6bd441f.

- 2026-09-07T01:47:42+00:00: Recorded command exit 101; command argv SHA-256
  1e65c04f56c34ddcd81928f295ae75acd318cee7965056f1a4f0d243419d9b4c.

- 2026-09-07T01:47:48+00:00: Recorded command exit 0; command argv SHA-256
  e3226e09ed262c5b980bdb2a3d26d56462f9c8d10e016352ba2be60128245435.

- 2026-09-07T01:48:16+00:00: Recorded command exit 0; command argv SHA-256
  7efde6f88b6c6fb1da0ffecb51d5f561c63e2a95eaa01bc4a51b148fc0542174.

- 2026-09-07T01:48:44+00:00: Recorded command exit 0; command argv SHA-256
  12eb316d25e6cc9da959ef9e47c85d84a22a859df5e046c89319b48038f1c9ba.

- 2026-09-07T01:49:07+00:00: Recorded command exit 0; command argv SHA-256
  886a0e69cbcf7cc15a53550bcc31b3c0568e6376342429d095bd894f3ef9abee.

- 2026-09-07T01:50:20+00:00: Recorded command exit 0; command argv SHA-256
  21f93064b6f4f946ae23c62e2c77b9bd3ec2462b60860e6d69094016f168292d.

- 2026-09-07T01:50:33+00:00: Recorded command exit 0; command argv SHA-256
  4bfe7ffc949ee8aeac6a969c0dff23d598a8c016a2647216421fdf58a0ff2ef5.

- 2026-09-07T01:51:03+00:00: Recorded command exit 0; command argv SHA-256
  2e0082b0bf2b3a4a1258d33884a588f9a3e1e4f483b47b099ee2c5ad9c4c5cd8.

- 2026-09-07T01:51:22+00:00: Recorded command exit 0; command argv SHA-256
  fed2a82cf419d707d0d8e002b9240967534b0fae5ac12877f52913cbf6bd441f.

- 2026-09-07T01:51:33+00:00: Recorded command exit 0; command argv SHA-256
  12eb316d25e6cc9da959ef9e47c85d84a22a859df5e046c89319b48038f1c9ba.

- 2026-09-07T01:51:51+00:00: Recorded command exit 0; command argv SHA-256
  886a0e69cbcf7cc15a53550bcc31b3c0568e6376342429d095bd894f3ef9abee.

- 2026-09-07T01:52:01+00:00: Recorded command exit 0; command argv SHA-256
  487921bddd4e238647a82aa49c66ee10e909a689d1576a42af85808ae9848e7f.

- 2026-09-07T01:52:14+00:00: Recorded command exit 0; command argv SHA-256
  aaa3d915fdc4e6419ea88149e92b82dcd618c2f39f335dc2b4679f9750b5491f.

- 2026-09-07T01:52:48+00:00: Recorded command exit 0; command argv SHA-256
  eaae531d815a4a4c86fcb47fab5cebc0f875a3cd87b96c6acf475326df257b29.

- 2026-09-07T01:52:56+00:00: Recorded command exit 0; command argv SHA-256
  c7d144244d110a2a8a6f4a380cfbe22a66a6c537dd94a5fba8189515b42f4c44.

- 2026-09-07T01:53:03+00:00: Recorded command exit 2; command argv SHA-256
  e499338bb36e46b4b8153a522bfb6aa1fc43007813f5c79719db4227561fcc38.

- 2026-09-07T01:53:17+00:00: Recorded command exit 0; command argv SHA-256
  ba4fb9dba35a86ead5b78f20f95c98752d2b7b1575f2eab4a2555d5aa1132f90.
