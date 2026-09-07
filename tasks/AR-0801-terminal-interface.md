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
  "next_action": "Audit public library seams and implement honest doctor/plan/run/sweep/compare/report boundaries with stable JSON, meaningful exits, cancellation and PTY tests.",
  "observed_branch": "feature/terminal-interface",
  "observed_dirty": 5,
  "observed_head": "b79534b627e28792a46e1a0074be762bb425d2a6",
  "owner": "root-coordination-20260906",
  "plan": "../plans/AR-0801.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide doctor, plan, run, sweep, compare and report with stable JSON output.",
  "task_revision": 56,
  "title": "Implement terminal and automation interfaces",
  "updated_at": "2026-09-07T01:39:20+00:00",
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
