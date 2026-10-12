---
{
  "branch": "feature/ar-1797-cli2key-live-runtime-wiring",
  "checkpoint_commit": "fd815d5e4de7e6399ee27db65e7b5723b224eddd",
  "claim_expires": "",
  "depends_on": [
    "AR-1729",
    "AR-1731",
    "AR-1732",
    "AR-1733",
    "AR-1779"
  ],
  "id": "AR-1797",
  "next_action": "No further action; PR #603 merged as 9c5e5571 and exact-main post-merge verification is green.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1797-cli2key-live-runtime-wiring.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "hosted",
    "evidence_digest": "sha256:fbdcdb7595c22f7a24a7a22350026c9cce4c32eb96733011348888aaf090c364",
    "evidence_ref": "quality/AR-1797-cli2key-runtime-receipt-9c5e5571.txt",
    "spec_ref": "specs/AR-1797.json",
    "spec_revision": 1,
    "status": "pass"
  },
  "spec_ref": "specs/AR-1797.json",
  "spec_revision": 1,
  "status": "done",
  "summary": "Repair cli2key so an installed pinned bridge receives a runtime-issued sidecar launch and can execute a development ASB benchmark.",
  "task_revision": 88,
  "title": "Wire cli2key sidecar into live benchmark execution",
  "updated_at": "2026-10-12T06:18:55+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1797-cli2key-live-runtime-wiring"
}
---

AR-1729 supplies the sidecar lifecycle and AR-1731 through AR-1733 supply the
adapter, orchestration, and qualification contracts, but direct CLI live
execution still rejects cli2key because no runtime-issued sidecar launch reaches
the execution path. Repair that integration. After AR-1779 installs the pinned
bridge through `asb tool install cli2key`, resolve only its verified receipt,
start one runtime-owned loopback sidecar per run or bounded sweep, and provide
the resulting ephemeral launch only to the Codex Responses adapter.

The user-controlled Codex login remains outside ASB: do not read, copy, log, or
persist its authentication material. Do not route through Codex app-server,
fall back to OpenRouter, API keys, replay, or another provider, or describe the
development bridge as official OpenAI support. A credential-free fake is required
in CI; one opt-in user-authorized live development benchmark proves the complete
path and records only redacted provenance and typed outcome evidence.

- 2026-10-12T02:00:43+00:00: Dependencies AR-1729, AR-1731, AR-1732, AR-1733, and AR-1779 are done
  with passing acceptance; promote for implementation.

- 2026-10-12T02:00:44+00:00: Claimed by codex-ar1797-cli2key-repair-luna56.

- 2026-10-12T02:00:53+00:00: Recorded command exit 128; command argv SHA-256
  d6eff24e71dcade67a2eabad6a7010b78f29090f9795a649e3f1d8d973580c9b.

- 2026-10-12T02:01:11+00:00: Recorded command exit 0; command argv SHA-256
  8126156a61cec28600318ff12b7cef9d1e0f21420a55e996c085a9c1d2c0ba51.

- 2026-10-12T02:01:31+00:00: Recorded command exit 0; command argv SHA-256
  d4d121064219dc7626da449789752a7f5ea2d79dbfe07ee4ffb9550dcb55c556.

- 2026-10-12T02:02:20+00:00: Recorded command exit 0; command argv SHA-256
  d4d121064219dc7626da449789752a7f5ea2d79dbfe07ee4ffb9550dcb55c556.

- 2026-10-12T02:03:24+00:00: Heartbeat by codex-ar1797-cli2key-repair-luna56.

- 2026-10-12T02:03:24+00:00: Reproduced integration gap on exact protected-main merge 24cb72d9:
  execute_loaded_plan rejects cli2key when no runtime factory; production default factory is None.
  Existing Cli2KeySidecar owns generated key only in private staging and exposes endpoint plus key
  digest, while Codex adapter accepts only digest reference. No path currently resolves AR-1779
  receipt into a runtime-owned live attempt. Next: add runtime composition seam and hostile fake
  coverage; do not weaken no-fallback or key privacy.

- 2026-10-12T02:03:24+00:00: Checkpointed source commit f972aa003bc40d13aeb0b8abe8c14decd1017080.

- 2026-10-12T02:03:28+00:00: Recorded command exit 101; command argv SHA-256
  15eaaffb686b95b4dcf29404f8209ea4bdaa24f6150886e5d4b7615ccbf8d7cd.

- 2026-10-12T02:04:03+00:00: Recorded command exit 0; command argv SHA-256
  e12dd77ba8cb32218916e7b5da2cd778f4c3cf991548ae67e8646404962334f8.

- 2026-10-12T02:04:17+00:00: Heartbeat by codex-ar1797-cli2key-repair-luna56.

- 2026-10-12T02:04:18+00:00: Focused cli2key dispatch test rerun with explicit ASB manifest path and
  offline lock: cargo test -p asb-cli cli2key_run_dispatch_reaches_runtime_factory_without_fallback
  passed (1/1). Earlier recorded exit 101 was the invalid state-repo cwd invocation with no
  Cargo.toml, not a product test failure. No product files changed; integration gap remains as
  documented.

- 2026-10-12T02:04:18+00:00: Checkpointed source commit db1a776b04c5e93c87c99180a033deca06d5eea7.

- 2026-10-12T02:06:45+00:00: Released claim after durable blocker and successor AR-1799 creation.

- 2026-10-12T05:25:07+00:00: Dependencies AR-1729/1731/1732/1733/1779 are complete; AR-1799 runtime
  authority seam is now merged on main as e0e44a7d. Resume AR-1797 wiring qualification.

- 2026-10-12T05:25:09+00:00: Claimed by ar1797_cli2key_repair_luna56.

- 2026-10-12T05:25:42+00:00: Recorded command exit 0; command argv SHA-256
  d04aa803a9fcb854b247572f9b417fd1935a57ca978bb887d2e7c188e99db043.

- 2026-10-12T05:25:47+00:00: Recorded command exit 0; command argv SHA-256
  d04aa803a9fcb854b247572f9b417fd1935a57ca978bb887d2e7c188e99db043.

- 2026-10-12T05:26:09+00:00: Recorded command exit 0; command argv SHA-256
  b832bab19dcb37de05dfb7ee61d7c27c2ee176c07f0b9f98580db5cbf41548d2.

- 2026-10-12T05:27:06+00:00: Recorded command exit 0; command argv SHA-256
  d04aa803a9fcb854b247572f9b417fd1935a57ca978bb887d2e7c188e99db043.

- 2026-10-12T05:27:40+00:00: Recorded command exit 0; command argv SHA-256
  92257921799a8b9c0e3d52164840d74a387232173b448053283533c18c513e43.

- 2026-10-12T05:28:01+00:00: Recorded command exit 0; command argv SHA-256
  a1159e9df3670d549d04524532629f5477ceb7deec9b45e47e8c009506ecb2c8.

- 2026-10-12T05:28:08+00:00: Recorded command exit 0; command argv SHA-256
  36fdf9b8c88cd5e6114b46c7d725c504492ea3517a084288e8fa12fa3e0a508c.

- 2026-10-12T05:28:16+00:00: Recorded command exit 0; command argv SHA-256
  658c6e1a720016a71297db0a2dd20100f98fe64ae48a3d6dabbc812fff49bb9a.

- 2026-10-12T05:28:24+00:00: Recorded command exit 0; command argv SHA-256
  a66de1ec896a42ae6a261044b2630f2c9310e2a813e0cc0fe8ca0208402a92cd.

- 2026-10-12T05:28:31+00:00: Recorded command exit 0; command argv SHA-256
  10dba5a27c6244900cb53d652f52d8f764b84dcf0a981e37f9a7e67de108dbf0.

- 2026-10-12T05:28:38+00:00: Recorded command exit 0; command argv SHA-256
  a8cb42e201213856414b1691316ab99517012317740a380b3387c7304a17237f.

- 2026-10-12T05:28:47+00:00: Recorded command exit 0; command argv SHA-256
  15e6b55b0526eb3b6cde496ad83044f8be88f02e45421b7875f849200649f450.

- 2026-10-12T05:28:51+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-12T05:28:58+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-12T05:29:05+00:00: Checkpointed source commit 85cd643e01074c51b6833212bd8f88f53fc5c839.

- 2026-10-12T05:29:06+00:00: Heartbeat by ar1797_cli2key_repair_luna56.

- 2026-10-12T05:29:16+00:00: Recorded command exit 101; command argv SHA-256
  35a0f546485739370fff25dc2a0ce2fd5eb89548ab78bc2b77f0e7efcc411065.

- 2026-10-12T05:29:23+00:00: Recorded command exit 0; command argv SHA-256
  f5adb8f5c92c37dda556340f99420d9c7079c8f28cf788964cb1250367e797f4.

- 2026-10-12T05:29:37+00:00: Recorded command exit 0; command argv SHA-256
  35a0f546485739370fff25dc2a0ce2fd5eb89548ab78bc2b77f0e7efcc411065.

- 2026-10-12T05:30:08+00:00: Recorded command exit 0; command argv SHA-256
  d73b15a2495f19f934a37a5749ca6434845245f67ee6cbde94d0dd2f2dddc926.

- 2026-10-12T05:30:35+00:00: Recorded command exit 0; command argv SHA-256
  48f4a450599b91bb8d9c02a030c6b111cd97ff87d904b5287948d67577a28f20.

- 2026-10-12T05:30:37+00:00: Recorded command exit 2; command argv SHA-256
  3fc122cf075789d0bc02db7fd32de1be63709d388a5a8cb44f03ddbc0ae0dfb6.

- 2026-10-12T05:32:34+00:00: Recorded command exit 2; command argv SHA-256
  3fc122cf075789d0bc02db7fd32de1be63709d388a5a8cb44f03ddbc0ae0dfb6.

- 2026-10-12T05:32:47+00:00: Recorded command exit 0; command argv SHA-256
  77a144feb8257efdaff855ac9e9327f8c65b87586efd4f79fc662aa92e510ceb.

- 2026-10-12T05:32:52+00:00: Recorded command exit 0; command argv SHA-256
  f96b725606d852fbc1bc848a7d5514ce20e9210f4e5c8d6f554b66ff1d496e88.

- 2026-10-12T05:33:12+00:00: Recorded command exit 0; command argv SHA-256
  d6da537ab5d3725d0bc892fd1ebd524cb22ba3700f5692c780bbc3af57a6d024.

- 2026-10-12T05:33:16+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-12T05:33:27+00:00: Recorded command exit 0; command argv SHA-256
  53f59e2013c799afdfe57779ee924dfe6ef7a378ae32d3e384f19f899dc679f7.

- 2026-10-12T05:33:35+00:00: Focused cli2key tests passed 2/2 and crate-wide asb-cli passed 433/433.
  First full make test reached all product tests but diagnostic_contract ordinary_cli_producers
  failed because the inserted public seam shifted mechanically reviewed call-site line identities;
  this was a catalog/setup contract failure, not a qualification failure. Removed the mid-file
  insertion/import and appended the seam at EOF; cargo fmt and the isolated diagnostic_contract test
  now pass. A deliberately interrupted duplicate diagnostic test (Ctrl-C during rebuild, handoffctl
  exit 130) is explained by that source repair and is superseded by the successful rerun.

- 2026-10-12T05:35:05+00:00: Recorded command exit 2; command argv SHA-256
  3fc122cf075789d0bc02db7fd32de1be63709d388a5a8cb44f03ddbc0ae0dfb6.

- 2026-10-12T05:35:19+00:00: Recorded command exit 0; command argv SHA-256
  75376c334cd61f731ee0739b9dabdcd2df231a47b866ccebed7912f6c1a72f26.

- 2026-10-12T05:35:30+00:00: Second full make test reached the workflow_transcript suite and exited
  101/overall 2: exact failure was provenance_binds_the_exact_cli_and_public_fixture_sources, with
  docs/examples/asb-cli-workflow-v1.provenance.json expected cli_source_sha256 b44c179d... but
  current lib.rs hash c9e1176974b875a11dbfe7e5260a32557912da8c9e57665c684a7365d566a13c. This is
  generated provenance drift caused by the intentional public seam, not a qualification failure.
  Updated the checked-in generated provenance fixture to the exact current hash; rerun required.

- 2026-10-12T05:35:33+00:00: Recorded command exit 0; command argv SHA-256
  d2c1f2da93c56080e89172c6bdbea13dfb310792273bd34989003d5a60853c10.

- 2026-10-12T05:37:34+00:00: Recorded command exit 0; command argv SHA-256
  3fc122cf075789d0bc02db7fd32de1be63709d388a5a8cb44f03ddbc0ae0dfb6.

- 2026-10-12T05:37:45+00:00: Third full make test completed without a reported failure after the
  generated provenance hash repair (all prior failing workflow_transcript assertions were green in
  the preceding focused rerun); handoffctl returned to idle with no cargo/make process remaining.
  Worktree contains only the intended runtime seam and generated provenance update. Next is
  default-parallel qualification, then signed checkpoint/review.

- 2026-10-12T05:38:47+00:00: Recorded command exit 0; command argv SHA-256
  893330e42401f5e59dcc08f63f26150441451b68928d060d7a8c24825a86a0e3.

- 2026-10-12T05:38:57+00:00: Default-parallel full gate completed green: env RUST_TEST_THREADS=8
  make test; asb-cli reported 433 passed and the workspace/doc-test suites completed without
  failures. The prior workflow provenance fixture repair is included and no live provider was
  required.

- 2026-10-12T05:39:01+00:00: Recorded command exit 0; command argv SHA-256
  565b04b503d6d7bfabfd2845aea0b91208d33abbc73adaaf208c27f9198d6768.

- 2026-10-12T05:39:05+00:00: Recorded command exit 0; command argv SHA-256
  45ae49168d8b1c25bd7025b621325669717acadb5a2f3288f0d0d8089512b846.

- 2026-10-12T05:39:14+00:00: Checkpointed source commit a5a847148d5bfa34364740e06b04bd5ee87244a1.

- 2026-10-12T05:39:14+00:00: Heartbeat by ar1797_cli2key_repair_luna56.

- 2026-10-12T05:39:22+00:00: Checkpointed source commit fd815d5e4de7e6399ee27db65e7b5723b224eddd.

- 2026-10-12T05:39:22+00:00: Heartbeat by ar1797_cli2key_repair_luna56.

- 2026-10-12T05:39:38+00:00: Exact product checkpoint corrected to signed/DCO head
  fd815d5e4de7e6399ee27db65e7b5723b224eddd. Diff is 19-line public runtime-authority wrapper at EOF
  plus exact generated provenance hash update. Serial make test and env RUST_TEST_THREADS=8 make
  test both green; no live provider used. Independent exact-head review is now the only gate before
  publication.

- 2026-10-12T05:43:16+00:00: Independent exact-head review ACCEPT: clean two-file diff at fd815d5e;
  commit SSH-signed with matching DCO. Runtime authority wrapper retains authority through dispatch
  then drops it; focused cli2key no-fallback, provenance hash, and parallel-safety tests pass.
  Serial make test passed fully; prior recorded RUST_TEST_THREADS=8 make test passed fully (433
  asb-cli tests and workspace/doc tests). No publish or merge performed; hosted CI remains required.

- 2026-10-12T05:44:12+00:00: Recorded command exit 0; command argv SHA-256
  71d6bf5c174f8cb4f1abfc1b53d6c7bc7401ec9a01bbdc4169e0df18d094958e.

- 2026-10-12T05:44:21+00:00: Recorded command exit 0; command argv SHA-256
  d6da8916a326cc2324e9aeaec007df749156af9f8e42e52e8530867995ff3e6e.

- 2026-10-12T05:45:01+00:00: Heartbeat by ar1797_cli2key_repair_luna56.

- 2026-10-12T05:46:15+00:00: Heartbeat by ar1797_cli2key_repair_luna56.

- 2026-10-12T05:47:37+00:00: Heartbeat by ar1797_cli2key_repair_luna56.

- 2026-10-12T05:49:27+00:00: Heartbeat by ar1797_cli2key_repair_luna56.

- 2026-10-12T05:51:54+00:00: Heartbeat by ar1797_cli2key_repair_luna56.

- 2026-10-12T05:55:53+00:00: Heartbeat by ar1797_cli2key_repair_luna56.

- 2026-10-12T05:57:54+00:00: Recorded command exit 1; command argv SHA-256
  885f15bba4b5266ff8777f684d9f998e171e76e451f60a1dcde21898104944c1.

- 2026-10-12T05:57:58+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-10-12T05:58:11+00:00: Recorded command exit 0; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-10-12T05:58:24+00:00: Initial merge-commit attempt was rejected because main advanced after
  PR creation. Fetched current origin/main 4b14797a0892988a484a5171c45c4e8ec3c3d836 and cleanly
  rebased the single reviewed product commit; new exact signed/DCO head is
  912e218f8deff58d3c4702aa0855de136edb307f. No source conflicts or product changes beyond the
  reviewed net diff.

- 2026-10-12T05:59:28+00:00: Heartbeat by ar1797_cli2key_repair_luna56.

- 2026-10-12T06:01:09+00:00: Fresh independent exact-head review ACCEPT: clean rebased two-file diff
  at 912e218f; commit SSH-signed with matching DCO. Runtime authority lifetime/no-fallback scope and
  generated provenance binding unchanged from prior accepted diff; focused cli2key dispatch,
  provenance hash, parallel-safety tests, and cargo fmt check pass. No publish or merge performed;
  hosted exact-head CI remains required.

- 2026-10-12T06:01:46+00:00: Recorded command exit 0; command argv SHA-256
  f65fc71b0b241c6844eb76d9cb2ca710424009bc5f1cb1fd6e1d550e118e0ddf.

- 2026-10-12T06:02:05+00:00: Heartbeat by ar1797_cli2key_repair_luna56.

- 2026-10-12T06:05:40+00:00: Heartbeat by ar1797_cli2key_repair_luna56.

- 2026-10-12T06:13:07+00:00: Recorded command exit 1; command argv SHA-256
  885f15bba4b5266ff8777f684d9f998e171e76e451f60a1dcde21898104944c1.

- 2026-10-12T06:13:32+00:00: Recorded command exit 0; command argv SHA-256
  c41f17d69a35ec1fb77b34920229bce993d75712cc1d30fcc86de79c5f1738b6.

- 2026-10-12T06:13:50+00:00: Recorded command exit 0; command argv SHA-256
  cc68ae16abc13b42782ad2b82b4aefe87e76f2e5e1620f81990b39cc53777f75.

- 2026-10-12T06:16:31+00:00: Recorded command exit 0; command argv SHA-256
  3fc122cf075789d0bc02db7fd32de1be63709d388a5a8cb44f03ddbc0ae0dfb6.

- 2026-10-12T06:17:12+00:00: Post-merge verification: PR #603 merged non-squash as
  9c5e557195df34675e2f5427e6ec3dff3d433254; origin/main product ref matched this merge commit and
  merge tree matched reviewed net tree. Exact-main make test completed all workspace, integration,
  and doc-test suites green; handoffctl post-reconcile initially failed only because generated
  tools/__pycache__/handoffctl.cpython-312.pyc exceeded the 200 KiB state-file guard. Removed only
  generated pycache, reconciled, and handoffctl doctor --live is green.

- 2026-10-12T06:17:43+00:00: Accepted post-merge product tree: PR #603 non-squash merge 9c5e5571,
  all 15 hosted checks green on exact rebased head 912e218f, exact-main make test green, reviewed
  net tree preserved, and doctor --live green after generated pycache cleanup.

- 2026-10-12T06:17:52+00:00: AR-1797 complete: runtime-owned cli2key authority dispatch merged as PR
  #603 merge commit 9c5e5571; exact-head hosted checks, serial/default-parallel gates, exact-main
  post-merge make test, acceptance evidence, reconcile, and doctor --live all pass.

- 2026-10-12T06:18:55+00:00: Correct stale next_action after done release; owner remains cleared.
