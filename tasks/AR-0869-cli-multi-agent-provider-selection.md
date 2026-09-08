---
{
  "branch": "feature/cli-multi-agent-provider-selection",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T01:17:00+00:00",
  "depends_on": [
    "AR-0313",
    "AR-0318",
    "AR-0320",
    "AR-0801"
  ],
  "id": "AR-0869",
  "next_action": "Create a signed+DCO empty CI-provenance attestation atop repaired main a3696385be31c4ab86f6fb75cfa055ff6b098574, push normally, and require fresh exact-main post-merge workflows on that reachable base; preserve older historical merge-boundary limitations.",
  "observed_branch": "feature/cli-multi-agent-provider-selection",
  "observed_dirty": 0,
  "observed_head": "0d9d317716d557b916e4da7022f58197d287987a",
  "owner": "replay_20260906",
  "plan": "../plans/AR-0869.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Select several agents and apply one preconfigured provider profile through inspectable command-line options.",
  "task_revision": 94,
  "title": "Add CLI multi-agent provider selection",
  "updated_at": "2026-09-08T22:48:32+00:00",
  "worktree_key": "agent-systems-benchmark-cli-multi-agent-provider-selection"
}
---
## AR-0869

Add a safe command-line workflow for selecting several agents and one advertised provider profile.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-08T21:05:54+00:00: Fresh dependency/overlap audit: AR-0869 dependencies AR-0313, AR-0318,
  AR-0320, and AR-0801 are all durably done. Its CLI-only agent/provider selection, plan rendering,
  validation, help/examples and focused-test paths are disjoint from active AR-0806 TUI
  history/analysis and AR-0855 state/vendor header work. Higher numeric-frontier P1 leaves are not
  safely claimable: AR-0704 lacks its plan-required external authorization, AR-0819 overlaps active
  TUI/frontend paths, and AR-0832 is blocked by AR-0703 in its complete plan. Declared worktree and
  branch do not exist locally or remotely. Promote AR-0869 as the highest-priority compatible ready
  leaf.

- 2026-09-08T21:05:57+00:00: Claimed by replay_20260906.

- 2026-09-08T21:38:23+00:00: Heartbeat by replay_20260906.

- 2026-09-08T21:38:42+00:00: Recorded command exit 0; command argv SHA-256
  ebc36c2c7dfb453910e2ae0d87dd6d64b4a10b9fb1f64d02c36afd5d0c1cc857.

- 2026-09-08T21:42:46+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-08T21:44:26+00:00: Recorded command exit 0; command argv SHA-256
  322f9bc80dea741a0371c3f13be68849eb656212410de80f2a14581604ed4823.

- 2026-09-08T21:44:46+00:00: Recorded command exit 101; command argv SHA-256
  91d6107fd9dbb507a99f01d6240ebd3f00b7132d82e30a3a2e50a9ad973aa714.

- 2026-09-08T21:45:20+00:00: Recorded command exit 0; command argv SHA-256
  56a3cb3fb4b9cef1b96a950c130be3e0a7c3baaf869e78e6d97538937c9feb6d.

- 2026-09-08T21:46:41+00:00: Recorded command exit 0; command argv SHA-256
  33da9216d0f33a42d452f7fec39c378bc12208440079358404719a36c49fa84f.

- 2026-09-08T21:47:03+00:00: Recorded command exit 0; command argv SHA-256
  2af15b06cb3057c8cb0e23f1e5a359179626ecbf7ff2821f7abd8a1ed4d24960.

- 2026-09-08T21:47:59+00:00: Recorded command exit 1; command argv SHA-256
  ef0ecc86282c93ce06ef28270247c4c45ab06646e016b39b33e9a7b70486d2f5.

- 2026-09-08T21:48:55+00:00: Recorded command exit 0; command argv SHA-256
  951c6b5df0673b552eb961e4f140c3545da43d7937b63bae29ec9118fa4e797a.

- 2026-09-08T21:49:21+00:00: Recorded command exit 0; command argv SHA-256
  2af15b06cb3057c8cb0e23f1e5a359179626ecbf7ff2821f7abd8a1ed4d24960.

- 2026-09-08T21:49:58+00:00: Recorded command exit 0; command argv SHA-256
  9ac36a532731ec90503da33a1623c2c5b28eb8da28d9788dd69d34767df7cdba.

- 2026-09-08T21:50:31+00:00: Substantive AR-0869 implementation checkpoint on exact base
  559fbcc825234bb98a64ba554a53f38b004d24f6. Added  and side-effect-free  CLI surfaces backed by the
  authoritative asb-agents all-agent preflight. A required catalog SHA fences stale choices; bounded
  repeated  plus one  reject empty, duplicate, unknown, incompatible, over-bound and mixed/duplicate
  option shapes before effects. OpenAI output is canonically ordered, binds every agent to one
  credential-free profile SHA/model/API mode, exposes only credential source kind, omits the
  credential-reference digest, and includes a deterministic content-addressed selection SHA. Ollama
  is advertised honestly but rejected without constructor-controlled verified daemon evidence; no
  probe occurs in dry-run. Exact dirty scope is Cargo.lock, crates/asb-cli/Cargo.toml and
  crates/asb-cli/src/lib.rs. Authorized Cargo delta is only asb-cli -> existing asb-agents path
  dependency plus one lock package-edge line. Pinned Rust 1.93 offline check passed; asb-cli lib
  tests 26/26, focused Clippy -D warnings, fmt and diff-check pass. A real binary catalog ->
  two-agent OpenAI plan round trip passed with stable opendesk/codex order, 64-byte selection
  identity and no supplied reference digest in output. Remaining criteria are persisted in
  next_action; no candidate/publication yet.

- 2026-09-08T21:50:53+00:00: Correction to prior durable checkpoint: shell command substitution
  stripped four literal CLI names from the note only; product tests and files were unaffected. The
  implemented commands are provider-catalog and provider-plan. Provider-plan accepts bounded
  repeated --agent and exactly one --provider-profile, with the behavior and green results recorded
  in the preceding note. This is an operator-only state-note formatting correction.

- 2026-09-08T22:04:27+00:00: Recorded command exit 0; command argv SHA-256
  6806d0c18eeb6857ad7994afc784e3c9c398328da994855afee60dfc9aa25d7a.

- 2026-09-08T22:05:30+00:00: Recorded command exit 0; command argv SHA-256
  7d8e34b113e6c2805c6306bd4a06d88bedbec5ca99c8ed09e2b7a356f51c5451.

- 2026-09-08T22:06:43+00:00: Recorded command exit 0; command argv SHA-256
  b8863423a2110b49717088ebcbec2c551d53a10a89971105c8a8520c55edd363.

- 2026-09-08T22:07:04+00:00: Recorded command exit 127; command argv SHA-256
  1d8e6b8a6a29ea19228942d072593715c1b534f661357a0a7ed3349286855f64.

- 2026-09-08T22:07:41+00:00: Recorded command exit 101; command argv SHA-256
  cc991c0a829242acf4204f3be163a7cb8a2fa9f1fcf7a886c676a7a390c40aa9.

- 2026-09-08T22:07:50+00:00: Recorded command exit 101; command argv SHA-256
  1cdb57c48b26414dc6fd88df1df164765a52692f3032152570312454b5f1d393.

- 2026-09-08T22:08:02+00:00: Recorded command exit 1; command argv SHA-256
  023e391fe9ab4e8399b069af9fbf076cae14aba04b70d01a8ca2a8c5372c95c9.

- 2026-09-08T22:08:21+00:00: Recorded command exit 0; command argv SHA-256
  0287808d80b6d4c07ac817d1db5f1779a26e61a79d8633fd194ab22cd8dc554a.

- 2026-09-08T22:08:37+00:00: Recorded command exit 0; command argv SHA-256
  1cdb57c48b26414dc6fd88df1df164765a52692f3032152570312454b5f1d393.

- 2026-09-08T22:08:50+00:00: Recorded command exit 101; command argv SHA-256
  3b3f2bd67130e2255c5597047489529ae6e21e3f8a405bd67a38ce14ff3c4a49.

- 2026-09-08T22:08:59+00:00: Recorded command exit 0; command argv SHA-256
  e61ec413e0192c752e77d9655164a237e65626922c32359f14dea62d1420dadb.

- 2026-09-08T22:09:35+00:00: Recorded command exit 0; command argv SHA-256
  2cbb9c8a37f1d8addc38b6fd5bb34027d79899b0602c501a297518d473e4bfdf.

- 2026-09-08T22:09:50+00:00: Recorded command exit 1; command argv SHA-256
  e61ec413e0192c752e77d9655164a237e65626922c32359f14dea62d1420dadb.

- 2026-09-08T22:10:14+00:00: Recorded command exit 0; command argv SHA-256
  3b3f2bd67130e2255c5597047489529ae6e21e3f8a405bd67a38ce14ff3c4a49.

- 2026-09-08T22:11:48+00:00: Recorded command exit 0; command argv SHA-256
  11b9120a1c543cc278b418f5485232a6326bde7f91f4d32e2f286575efd3ed82.

- 2026-09-08T22:12:06+00:00: Recorded command exit 101; command argv SHA-256
  d5deb1410c4566fde6b5db2a57656d29635861a33f10cf785830ed72fb95cf47.

- 2026-09-08T22:12:43+00:00: Recorded command exit 0; command argv SHA-256
  2bcf43596e0e814b171216cefb9a7d94c93d0fcf9e5b2410c85c8f740c8ec5cb.

- 2026-09-08T22:12:59+00:00: Recorded command exit 0; command argv SHA-256
  b1f5ffe5f89b312c2cca4f175638ae39cf06dc8ea6f67116ab9a46dcd938003b.

- 2026-09-08T22:13:55+00:00: Recorded command exit 0; command argv SHA-256
  c760e96bb94ce6430274ed43cf7d9a8837f240a40c039ccd8f68827db9da1684.

- 2026-09-08T22:14:13+00:00: Recorded command exit 0; command argv SHA-256
  4ed12731f0dee3e853dec0dec3ca9cb759385638f30041f81836636e38aee829.

- 2026-09-08T22:14:36+00:00: Recorded command exit 0; command argv SHA-256
  c201d3595a03354f2e4fdbd9e8073ba65cdc8b1945bc565993ebd4ef8ccc9799.

- 2026-09-08T22:14:57+00:00: Recorded command exit 0; command argv SHA-256
  5aedf04c196d56bd86f3ea9e73049a7a2619519edc8b15b267b9f859d72ae897.

- 2026-09-08T22:15:19+00:00: Recorded command exit 0; command argv SHA-256
  d0d3793a4113dc85847df4d173bb359bfd42acad4f8df8e2e887f7e0cd02654b.

- 2026-09-08T22:15:44+00:00: Recorded command exit 0; command argv SHA-256
  d95d38221e285adbbd08ae05d2bb3bca7633e56e1bb46834c440f8ad6df87cab.

- 2026-09-08T22:16:35+00:00: Recorded command exit 0; command argv SHA-256
  f0dc147217da6e4d02747fa742abf24cabaf89ad54cffb62114f3513d6ad16aa.

- 2026-09-08T22:17:00+00:00: Heartbeat by replay_20260906.

- 2026-09-08T22:17:18+00:00: Recorded command exit 0; command argv SHA-256
  472f447c8d4e5c9e4100c9a2b6b6ce76c51b6850bf078fab6e12dcec9c66ef1e.

- 2026-09-08T22:18:14+00:00: Recorded command exit 0; command argv SHA-256
  c635d124417aa6ce737cb0b89657318e708679f478c2d444025eebb386957423.

- 2026-09-08T22:18:46+00:00: Recorded command exit 0; command argv SHA-256
  44c143e7c1a35a01075cbbd494e0fad065aea32d79002c552140849483c2503c.

- 2026-09-08T22:19:11+00:00: Recorded command exit 0; command argv SHA-256
  279e85f1ad2b5657da6e0b37b9a6867c9168ce51e4f698fb3c13589d86e87fb7.

- 2026-09-08T22:19:20+00:00: Recorded command exit 101; command argv SHA-256
  f55345a64f104fcb86a0de61e67b1d3517b3a8595ebd9320d228933b97b591a6.

- 2026-09-08T22:20:04+00:00: Recorded command exit 0; command argv SHA-256
  54bb665eeb5f8cd6c43009b703953ebbf323042287ff312c631d8297e6c7c022.

- 2026-09-08T22:21:09+00:00: Recorded command exit 0; command argv SHA-256
  ca1c6fe31fb1d24c70209ff03c75ee6c31dd9ca1023b3abc99f9d109a5400f39.

- 2026-09-08T22:21:27+00:00: Recorded command exit 0; command argv SHA-256
  5022c88b355343bd20b051c7ac29fd637d0c92643eff1142fba6e7f158f045b3.

- 2026-09-08T22:21:46+00:00: Recorded command exit 1; command argv SHA-256
  566be22dbeb19641415bdaf8f5259f0863a5b6ba8994cabeb3be3dab5b5ce329.

- 2026-09-08T22:22:13+00:00: Recorded command exit 0; command argv SHA-256
  7c9c2bd17a49eb866eef25ee4112ff4669d501c6c42941ca9f48e79623f162c7.

- 2026-09-08T22:23:02+00:00: Recorded command exit 0; command argv SHA-256
  8fec1b117395608be43ec75237a9ed828a5b4a11e591eb0185e78384de6514e0.

- 2026-09-08T22:23:23+00:00: Recorded command exit 127; command argv SHA-256
  207404d49faa2da5d15e0381e1e18853473582bc427a0f93ac7e5133d9146c99.

- 2026-09-08T22:23:32+00:00: Recorded command exit 0; command argv SHA-256
  a636b48edca1cc33419133ed5fd2531282ad5d119fdaf6b7c2d3c1a4ddfaf884.

- 2026-09-08T22:24:29+00:00: Recorded command exit 0; command argv SHA-256
  d4b184ce7687e35af9cd79075d9de930a54a6e3d2040b0726dee6026aa206f42.

- 2026-09-08T22:24:56+00:00: Recorded command exit 101; command argv SHA-256
  25538cf2bc768c5a2c74d27ed2e86c4ed005ab422586531996b1c6515b512031.

- 2026-09-08T22:25:12+00:00: Recorded command exit 0; command argv SHA-256
  23effdbd239832ec3a6f8462cc4d7ad2b9bb25ce7ededbc3aac3d88f7af3ffcf.

- 2026-09-08T22:25:30+00:00: Recorded command exit 0; command argv SHA-256
  165683969ba1962d9c954c85336035157f22a8e5f6999d68ac30d316321fabc5.

- 2026-09-08T22:26:19+00:00: Recorded command exit 0; command argv SHA-256
  8e437ec3de4cd0bb00b68d7e0c8714a2cee70567692047ea8b27815297db344c.

- 2026-09-08T22:26:42+00:00: Recorded command exit 0; command argv SHA-256
  d43b688715d4edc15c4e3459fac20e29885653d052946aa594b660359a5fb10f.

- 2026-09-08T22:27:21+00:00: Completed AR-0869 implementation on exact base
  559fbcc825234bb98a64ba554a53f38b004d24f6. Exact dirty scope is Cargo.lock,
  crates/asb-cli/Cargo.toml, crates/asb-cli/src/lib.rs, docs/QUICKSTART.md, and
  docs/examples/guide-contract.json. The CLI exports a closed content-addressed provider selection,
  reconstructs the exact OpenAI profile from its credential-free logical-reference digest, and binds
  plan/run/sweep before effects to the selected agent plus experiment
  provider/model/additional-settings identity. Stored execution binds the selection digest; compare
  detects selection drift; report exposes only selection/profile identities; help, doctor inventory,
  guide contract, and Bash completion are synchronized. Ollama remains advertised but unavailable
  without verified daemon evidence and there is no fallback. Focused CLI 29 unit plus 3 e2e plus 3
  guide tests pass; workspace tests, workspace Clippy, rustdoc, release build, formal tests,
  mutation 7/7, coverage 93.42 percent workspace and all critical floors, cargo-deny, offline
  cargo-audit, repository policy, actionlint, zizmor, diff-check, and dirty-diff Gitleaks all pass.
  A broad directory Gitleaks attempt found one generated target-tree artifact; the source diff stdin
  scan was clean, so this is classified as generated-build output and exact-commit Gitleaks remains
  required. Earlier checkpoint statement that the logical-reference digest was omitted is
  superseded: exact manifest import requires it to reconstruct and validate the profile, and the
  asb-agents contract explicitly classifies this digest as credential-free; no credential value is
  accepted, retained, or rendered.

- 2026-09-08T22:27:33+00:00: Recorded command exit 0; command argv SHA-256
  edb10e451349a5940f7f7cfbe4382e66e9bcd85a921dba375e0f2cf00e2cefb5.

- 2026-09-08T22:28:00+00:00: Recorded command exit 0; command argv SHA-256
  45def28cb00c69640d75e3fc549e6544e0414c7ddb0b94db0d72d31d43c8206e.

- 2026-09-08T22:28:12+00:00: Recorded command exit 0; command argv SHA-256
  0e0bff720ef03a9b054a08929d460178ea9303d8c6583c2cf5fe173a74b48716.

- 2026-09-08T22:28:52+00:00: Recorded command exit 0; command argv SHA-256
  75d43b9ec3915987efaed6d34e49b43ad422241f72703256f5b1b24de58236b1.

- 2026-09-08T22:29:37+00:00: Recorded command exit 0; command argv SHA-256
  ca1aff8d97373f764fb3a97f3c77ae32cd21f9f08066b5814e16b0f38b4e636f.

- 2026-09-08T22:30:30+00:00: Recorded command exit 0; command argv SHA-256
  8dae376bd972e6b6584a96f02959606f7f789e4df13bea179b5f92e2221b3f9f.

- 2026-09-08T22:31:06+00:00: Immutable AR-0869 candidate is exact commit
  0d9d317716d557b916e4da7022f58197d287987a, tree 25183d10ffb50bd465dd93efb5b69001a20273e4, parent
  559fbcc825234bb98a64ba554a53f38b004d24f6. Martin Beck SSH signature verifies with the allowed
  ED25519 identity and the final Signed-off-by trailer exactly matches the author. Worktree is
  clean. Exact five-path scope is Cargo.lock, crates/asb-cli/Cargo.toml, crates/asb-cli/src/lib.rs,
  docs/QUICKSTART.md, and docs/examples/guide-contract.json; Cargo delta remains only asb-cli to
  existing asb-agents and its lock package edge. Exact-candidate workspace tests, formal tests,
  workspace Clippy with warnings denied, rustdoc warnings denied, and release build pass.
  Exact-candidate mutation run found seven and caught seven. Exact-candidate coverage passes at
  93.43 percent workspace lines, 99.40 percent asb-core, 96.83 percent asb-protocol, and 97.73
  percent asb-replay. Exact commit range repository policy, diff-check, Git-history Gitleaks, scope,
  signature, and DCO pass. Cargo-deny, offline cargo-audit, actionlint, zizmor, and prior
  source-diff Gitleaks pass. No Kani harness covers this CLI orchestration slice; hosted formal
  remains required at exact head. Candidate is ready only for independent review, not publication or
  merge.

- 2026-09-08T22:32:36+00:00: Independent immutable review complete: exact candidate
  0d9d317716d557b916e4da7022f58197d287987a has parent/current origin/main
  559fbcc825234bb98a64ba554a53f38b004d24f6, clean worktree, SSH signature and exact DCO, five-path
  scope matching the recorded checkpoint, clean diff-check, no candidate secret material in changed
  paths, and all recorded local gates pass. Approved for exact-head publication; hosted CI remains
  required.

- 2026-09-08T22:32:59+00:00: Recorded command exit 0; command argv SHA-256
  01e9bfc649d41d80ca1d652e6b8a3073c74ddff61e1c5aa4b317ab76be9e7254.

- 2026-09-08T22:33:15+00:00: Recorded command exit 0; command argv SHA-256
  463384de3467da61fd2e6cd271bf2f8621ad882888c73939ca5469292e9daeb0.

- 2026-09-08T22:38:36+00:00: PR #88 exact-head hosted CI is fully green and PR is OPEN/MERGEABLE at
  immutable head 0d9d317716d557b916e4da7022f58197d287987a over base
  559fbcc825234bb98a64ba554a53f38b004d24f6. All listed Rust, quality, formal, fault, portability,
  headers, and AWQ checks completed SUCCESS. Coordinator authorizes merge followed by exact-main
  post-merge verification.

- 2026-09-08T22:38:57+00:00: Recorded command exit 0; command argv SHA-256
  307645f2e0723d6f222e925e9620ba52147569c5a7e9a795995fcabf104d72d0.

- 2026-09-08T22:41:28+00:00: Post-merge repository-quality run 34286967367 failed because GitHub
  merge commit 7571592990bf1e4a5474fbd8a183ea110e5d242c lacks a matching Signed-off-by trailer.
  Exact PR-head CI was fully green; this is an integration-boundary defect. Preserve reviewed tree
  25183d10ffb50bd465dd93efb5b69001a20273e4 and parents 559fbcc825234bb98a64ba554a53f38b004d24f6 plus
  0d9d317716d557b916e4da7022f58197d287987a. Narrow signed-DCO replacement is authorized; do not
  alter product contents.

- 2026-09-08T22:41:53+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-09-08T22:42:07+00:00: Recorded command exit 0; command argv SHA-256
  fbe0bb957cc9331b91283184cc3f566e23593b2dcec6d8ffd668fbba82f241a8.

- 2026-09-08T22:42:26+00:00: Recorded command exit 2; command argv SHA-256
  3acf3e54554a976a2297dc3e65109c1408a70d038172332daf23586a27f33454.

- 2026-09-08T22:42:46+00:00: Recorded command exit 0; command argv SHA-256
  3f1a62db96c6f782a1f4b14fcfda6d40a9d8348cb1b9c516648dbc16f78ef4aa.

- 2026-09-08T22:43:04+00:00: Recorded command exit 0; command argv SHA-256
  072be43361c7d88e6490eca79408bacaa917983e8b8e6015ddab726d7cbbcdc3.

- 2026-09-08T22:44:23+00:00: Recorded command exit 0; command argv SHA-256
  1f0f755dbd6dd702bc0dbec5d818f0669e12d9ce4f54129e1376edf447dfe3b5.

- 2026-09-08T22:45:55+00:00: Fresh push quality 34287289472 correctly failed only because GitHub
  supplied discarded base 7571592, which is unreachable after narrow repair. Workflow-dispatch
  quality 34287379302 reached two older pre-existing GitHub merge commits 909078c and e0554b5
  lacking matching DCO; these are documented historical boundaries. Do not rewrite unrelated
  history. Use additive signed-DCO CI-provenance attestation atop repaired tree, then fresh push
  post-merge gates.

- 2026-09-08T22:46:12+00:00: Recorded command exit 0; command argv SHA-256
  1cfbc4789172041ab81d9516fe2d0759723fa9eed556ebaac13c520d6b5e5917.

- 2026-09-08T22:46:29+00:00: Recorded command exit 0; command argv SHA-256
  7c6d5f932d577d1c550708e4c02f02fbb7d510213a7d064dad9525f6e73e317b.

- 2026-09-08T22:48:32+00:00: Recorded command exit 0; command argv SHA-256
  65a9d0f621432f943c539daa5551b75b3a4ff4d2ca26d3502ee9dd741d8732d2.
