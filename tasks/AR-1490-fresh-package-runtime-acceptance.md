---
{
  "branch": "qualification/ar-1490-fresh-package-runtime-acceptance",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-28T17:14:46+00:00",
  "depends_on": [
    "AR-1461",
    "AR-1462",
    "AR-1488",
    "AR-1489"
  ],
  "id": "AR-1490",
  "next_action": "Create a clean verifier root from the exact development bundle archive, leaving installed CLI and fixture helpers outside that root; rerun unsigned-development verification with the bounded placeholder signature, then remove temporary helpers and run final gates.",
  "observed_branch": "qualification/ar-1490-fresh-package-runtime-acceptance",
  "observed_dirty": 3,
  "observed_head": "45df6590cbf9ab75f07dcc0b753335949e28d937",
  "owner": "ar1490-dev-acceptance-luna56",
  "plan": "../plans/AR-1490-fresh-package-runtime-acceptance.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Run fresh package first-customer runtime acceptance and produce an explicit readiness report.",
  "task_revision": 91,
  "title": "Fresh package runtime acceptance",
  "updated_at": "2026-09-28T15:16:20+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1490-fresh-package-runtime-acceptance"
}
---

Dependency-safe successor after AR-1489. This task performs actual fresh
package/runtime acceptance where the prior AR documented the contract. It
remains credential-free, local/mock/replay-only, ASB-only, and fail-closed
when exact package or clean-environment inputs are absent.

- 2026-09-27T15:35:00+00:00: Created after AR-1489 completion to produce fresh
  package execution evidence and an explicit first-customer readiness report.

- 2026-09-27T15:36:26+00:00: Dependencies AR-1461, AR-1462, AR-1488, and AR-1489 are done. Promote
  fresh ASB package/runtime acceptance with local/mock/replay-only readiness evidence.

- 2026-09-27T15:36:29+00:00: Claimed by ar1332-record-replay-luna56.

- 2026-09-27T15:36:38+00:00: Recorded command exit 0; command argv SHA-256
  13f4f9c5f67aa4aed2c2b85c387264f5d51709a5131bd7ca39d58e9e03b0f72d.

- 2026-09-27T15:37:02+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T15:37:05+00:00: Recorded command exit 0; command argv SHA-256
  9c871eb63a09d923032d11427c68c4161a79ef46972d321b12953fd680a23d43.

- 2026-09-27T15:37:28+00:00: Recorded command exit 0; command argv SHA-256
  a82b9d78dcb8d4efcf094a688a35b769dde348a2e6f10888f6ea9e7219af138d.

- 2026-09-27T15:38:50+00:00: BLOCKED by missing external qualification inputs, not product failure.
  Approved bounded search via handoffctl covered current worktree and /srv/data/projects for runtime
  bundle archives/manifests; no ASB runtime tar archive or verified release package found.
  docs/RUNTIME_BUNDLES.md and build_runtime_bundle.py require supervisor/sidecar plus signing key,
  allowed-signers, principal, ssh-keygen digest; none are provisioned. Unsigned-development output
  would not be first-customer release evidence and was not substituted. Next action: provision exact
  signed package and rerun clean install/doctor/setup/run/sweep/replay/cleanup acceptance. No
  product/asb-tui/provider changes made.

- 2026-09-28T14:36:37+00:00: User-authorized development build may use the explicit
  unsigned-development bundle profile; preserve customer-release signing evidence as an optional
  future gate and do not treat development output as a customer release.

- 2026-09-28T14:36:40+00:00: Claimed by ar1490-dev-acceptance-luna56.

- 2026-09-28T14:38:48+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-28T14:39:07+00:00: Recorded command exit 0; command argv SHA-256
  9e808f764c153d2f3035fc39bfa8cca7bbe5bc485685eb9f14c5241806c63cb2.

- 2026-09-28T14:39:24+00:00: Heartbeat by ar1490-dev-acceptance-luna56.

- 2026-09-28T14:39:31+00:00: Recorded command exit 0; command argv SHA-256
  91c481d4f1a058d3265e9102b0531d1eefe09cb45e5c1807ecda5e8c8b6b67d5.

- 2026-09-28T14:40:31+00:00: Recorded command exit 0; command argv SHA-256
  f9c92d9ddfe3cd1a3128731ad7e01ed88f99a3d42e745721f25b7aca37e63c8c.

- 2026-09-28T14:41:18+00:00: Recorded command exit 0; command argv SHA-256
  8f88dd87044422ff7dc83e0d414f2d0cc66c2d4276edb4147c1e789c0e383015.

- 2026-09-28T14:42:18+00:00: Recorded command exit 0; command argv SHA-256
  d390d27c4ed46df463802c4ad5b858653ca03e940169f758a71c7c4914ba97c0.

- 2026-09-28T14:43:24+00:00: Recorded command exit 0; command argv SHA-256
  b49a90ee600c1023cee9ee9f9e8a4f9a06c53eef8c48d3932d88e482126c7c01.

- 2026-09-28T14:43:57+00:00: Recorded command exit 0; command argv SHA-256
  994b8cdfb6f43f8b69b424c11fe7ddfd0461c3828b69b44f3e46851093275100.

- 2026-09-28T14:44:23+00:00: Recorded command exit 0; command argv SHA-256
  fa1894b0e944e220dc5db5ff43d12d6517531832363cd96f63d4940e49c2fa02.

- 2026-09-28T14:44:49+00:00: Recorded command exit 0; command argv SHA-256
  0ea33d8e77fb93f7bba377fb23d135003b4f010654080aa5fdb5b04249115f0f.

- 2026-09-28T14:45:16+00:00: Recorded command exit 0; command argv SHA-256
  f1e5d98a9666cf7f804f09ac78c31a60f8d63c09089043443bed6014b2d428a3.

- 2026-09-28T14:45:41+00:00: Recorded command exit 0; command argv SHA-256
  2e43c64d82f76986d6dafb407d725bffa3470028320ebbd2848f2226d155eebe.

- 2026-09-28T14:45:58+00:00: Recorded command exit 0; command argv SHA-256
  dcaafadcd6200426c55f6465aa8e70e146bbb580067e67f21a9c79d3cc895da1.

- 2026-09-28T14:46:31+00:00: Recorded command exit 0; command argv SHA-256
  2bd4c84f2d3f9af31bf02cd144d693558fa6e56f91a8b131e1f50267af820bf8.

- 2026-09-28T14:47:31+00:00: Recorded command exit 0; command argv SHA-256
  b04345386e0670e350203b5e5d84e3ced2a7f795d5cdca112ff349e26b25eac2.

- 2026-09-28T14:47:55+00:00: Recorded command exit 0; command argv SHA-256
  43e18db767ce8b56c813e2f36cde7a1b7ad1b85fa3619f7edf6561e62e8c1900.

- 2026-09-28T14:49:34+00:00: Recorded command exit 1; command argv SHA-256
  8698233ac2bb504fe4fae3bc1799d976984bb5a0bf65d268d3f607a9062df03a.

- 2026-09-28T14:49:58+00:00: Heartbeat by ar1490-dev-acceptance-luna56.

- 2026-09-28T14:50:12+00:00: Recorded failure: the first fixture-agent creation attempt exited 1
  because apply_patch placed ar1490-fixture-agent.sh in the unrelated agent-workflow-quality
  checkout, so the AR worktree had no fixture file and no product mutation occurred. The stray file
  was immediately deleted. Next action is to create the fixture only in this declared ASB AR
  worktree and continue acceptance.

- 2026-09-28T14:50:31+00:00: Recorded command exit 0; command argv SHA-256
  8698233ac2bb504fe4fae3bc1799d976984bb5a0bf65d268d3f607a9062df03a.

- 2026-09-28T14:50:49+00:00: Recorded command exit 0; command argv SHA-256
  81f9636cb9dd8e7701a939a718fd72850a82de80e748f8a99a9ab278fb0b706f.

- 2026-09-28T14:51:06+00:00: Recorded command exit 0; command argv SHA-256
  d5209591d632cba1f114d1ebd8524bd1110a6cef0eda7020c851727c8e1e5db1.

- 2026-09-28T14:51:33+00:00: Recorded command exit 0; command argv SHA-256
  9fc3c1847e959cc1ac6b82dd3891b4279a45201559b27938e13abf844a068163.

- 2026-09-28T14:53:08+00:00: Recorded command exit 0; command argv SHA-256
  70c85ca57fbe3f9d41057c711bcbf7d34b027c711ac5bbc8b4ff20067a803335.

- 2026-09-28T14:53:34+00:00: Recorded command exit 3; command argv SHA-256
  f17628d279336fa6a409883e518e3b534f49416dc1e889a504f8423982d0aac7.

- 2026-09-28T14:54:31+00:00: Recorded failure: installed unsigned-development package was verified
  successfully, but asb plan rejected the generated flat [experiment] TOML with structured
  validation error experiment plan syntax or shape is invalid. No result/work roots or process were
  created. Next action is to regenerate the same plan with nested
  agent/model/tool_policy/workload/execution/platform/controls tables and re-run plan before
  execution.

- 2026-09-28T14:54:48+00:00: Recorded command exit 0; command argv SHA-256
  70c85ca57fbe3f9d41057c711bcbf7d34b027c711ac5bbc8b4ff20067a803335.

- 2026-09-28T14:55:14+00:00: Recorded command exit 3; command argv SHA-256
  f17628d279336fa6a409883e518e3b534f49416dc1e889a504f8423982d0aac7.

- 2026-09-28T14:56:11+00:00: Recorded second plan failure: the regenerated nested plan still exited
  3 with experiment plan syntax or shape is invalid. Inspection of the exact generated file found
  controls.replay emitted cassette_sha256 = null, which is invalid TOML syntax; the validator
  therefore never reached semantic checks and created no result/work roots. The helper is being
  corrected to omit absent optional fields.

- 2026-09-28T14:56:19+00:00: Recorded command exit 0; command argv SHA-256
  70c85ca57fbe3f9d41057c711bcbf7d34b027c711ac5bbc8b4ff20067a803335.

- 2026-09-28T14:56:45+00:00: Recorded command exit 0; command argv SHA-256
  f17628d279336fa6a409883e518e3b534f49416dc1e889a504f8423982d0aac7.

- 2026-09-28T14:57:11+00:00: Recorded command exit 5; command argv SHA-256
  d3911253abcdda827e8931919c2bf8d9e83912114139d1f4ad6baed0241695c7.

- 2026-09-28T14:57:32+00:00: Recorded execution failure: installed unsigned-development package
  passed plan and owner-backed run admission, but the fixture agent omitted the required tests.txt
  artifact; run ar1490-run terminal decision was fail with failed_check_count=1, exit_code=0, no
  timeout/cancellation/infrastructure error, and cleanup left work root empty. This is a harness
  fixture defect, not an ASB runtime failure. Next action is to add the exact tests.txt expected
  fixture and rerun with fresh result/work roots.

- 2026-09-28T14:57:52+00:00: Recorded command exit 0; command argv SHA-256
  8698233ac2bb504fe4fae3bc1799d976984bb5a0bf65d268d3f607a9062df03a.

- 2026-09-28T14:58:10+00:00: Recorded command exit 0; command argv SHA-256
  81f9636cb9dd8e7701a939a718fd72850a82de80e748f8a99a9ab278fb0b706f.

- 2026-09-28T14:58:28+00:00: Recorded command exit 0; command argv SHA-256
  d5209591d632cba1f114d1ebd8524bd1110a6cef0eda7020c851727c8e1e5db1.

- 2026-09-28T14:58:49+00:00: Recorded command exit 0; command argv SHA-256
  70c85ca57fbe3f9d41057c711bcbf7d34b027c711ac5bbc8b4ff20067a803335.

- 2026-09-28T14:59:17+00:00: Recorded command exit 0; command argv SHA-256
  f17628d279336fa6a409883e518e3b534f49416dc1e889a504f8423982d0aac7.

- 2026-09-28T14:59:35+00:00: Recorded command exit 5; command argv SHA-256
  d3911253abcdda827e8931919c2bf8d9e83912114139d1f4ad6baed0241695c7.

- 2026-09-28T15:00:30+00:00: Recorded second local/mock execution failure: plan ar1490-run2
  validated and admitted one attempt, but terminal decision was fail (handoff exit 5),
  failed_check_count=1, exit_code=0, no timeout/cancel/infrastructure failure, stdout_bytes=92;
  tests.txt was emitted, while parser.py contained a literal two-backslash \\r sequence instead of
  the expected single escaped \\r source. This is a disposable fixture content error, not an ASB
  runtime defect. Next action is to correct and inspect installed bytes before retry.

- 2026-09-28T15:01:09+00:00: Recorded command exit 0; command argv SHA-256
  8698233ac2bb504fe4fae3bc1799d976984bb5a0bf65d268d3f607a9062df03a.

- 2026-09-28T15:01:26+00:00: Recorded command exit 0; command argv SHA-256
  81f9636cb9dd8e7701a939a718fd72850a82de80e748f8a99a9ab278fb0b706f.

- 2026-09-28T15:01:44+00:00: Recorded command exit 0; command argv SHA-256
  d5209591d632cba1f114d1ebd8524bd1110a6cef0eda7020c851727c8e1e5db1.

- 2026-09-28T15:02:09+00:00: Recorded command exit 0; command argv SHA-256
  70c85ca57fbe3f9d41057c711bcbf7d34b027c711ac5bbc8b4ff20067a803335.

- 2026-09-28T15:02:36+00:00: Recorded command exit 0; command argv SHA-256
  f17628d279336fa6a409883e518e3b534f49416dc1e889a504f8423982d0aac7.

- 2026-09-28T15:02:54+00:00: Recorded command exit 4; command argv SHA-256
  790db972f135a9c7143b9bac48bbcdf0165c92c79a231cef0310afad59b6deb8.

- 2026-09-28T15:03:22+00:00: Recorded retry failure: the corrected fixture was installed and plan
  ar1490-run2 validated, but execution was intentionally refused with operation error run identity
  already exists or cannot be stored because the prior failed attempt had already created that run
  journal. No duplicate execution occurred. Next action is to use a fresh run identity and disjoint
  result/work roots.

- 2026-09-28T15:03:39+00:00: Recorded command exit 0; command argv SHA-256
  70c85ca57fbe3f9d41057c711bcbf7d34b027c711ac5bbc8b4ff20067a803335.

- 2026-09-28T15:04:05+00:00: Recorded command exit 0; command argv SHA-256
  f17628d279336fa6a409883e518e3b534f49416dc1e889a504f8423982d0aac7.

- 2026-09-28T15:04:40+00:00: Recorded command exit 5; command argv SHA-256
  d3911253abcdda827e8931919c2bf8d9e83912114139d1f4ad6baed0241695c7.

- 2026-09-28T15:05:56+00:00: Recorded third local/mock execution failure: plan ar1490-run3 validated
  and admitted one attempt but failed with handoff exit 5, failed_check_count=1, exit_code=0,
  stdout_bytes=91, no timeout/cancel/infrastructure failure. Installed byte inspection proved
  tests.txt emitted exactly; parser.py was not modified because the fixture printed the expected
  91-byte source to stdout without redirecting it to parser.py, so the grader correctly rejected the
  existing initial file. Next action is to redirect parser output and use a fresh run identity.

- 2026-09-28T15:06:14+00:00: Recorded command exit 0; command argv SHA-256
  8698233ac2bb504fe4fae3bc1799d976984bb5a0bf65d268d3f607a9062df03a.

- 2026-09-28T15:06:32+00:00: Recorded command exit 0; command argv SHA-256
  81f9636cb9dd8e7701a939a718fd72850a82de80e748f8a99a9ab278fb0b706f.

- 2026-09-28T15:06:49+00:00: Recorded command exit 0; command argv SHA-256
  d5209591d632cba1f114d1ebd8524bd1110a6cef0eda7020c851727c8e1e5db1.

- 2026-09-28T15:07:07+00:00: Recorded command exit 0; command argv SHA-256
  70c85ca57fbe3f9d41057c711bcbf7d34b027c711ac5bbc8b4ff20067a803335.

- 2026-09-28T15:07:36+00:00: Recorded command exit 0; command argv SHA-256
  f17628d279336fa6a409883e518e3b534f49416dc1e889a504f8423982d0aac7.

- 2026-09-28T15:08:01+00:00: Recorded command exit 0; command argv SHA-256
  d3911253abcdda827e8931919c2bf8d9e83912114139d1f4ad6baed0241695c7.

- 2026-09-28T15:08:35+00:00: Recorded command exit 0; command argv SHA-256
  17c3d08f1d01567b37497830b4fd381eaf947f8b7ac21a68656afb03b8c7debb.

- 2026-09-28T15:09:03+00:00: Recorded command exit 0; command argv SHA-256
  03f1ddc2d5d3017fd0e5e15547cc2a5eb1b691abd3977531ca9e0bf092aa709a.

- 2026-09-28T15:09:35+00:00: Recorded command exit 1; command argv SHA-256
  69b335ffa8ffefb85bc18edfe4ab3230bad2c29beb5433f856ad93a81f30c57f.

- 2026-09-28T15:10:04+00:00: Recorded command failure at recovery stage: the attempted cargo test
  invocation `cargo test --locked -p asb-runtime control_owner launch_factory live_service` exited 1
  because Cargo accepts only one positional TESTNAME filter; it rejected launch_factory as an
  unexpected argument before compiling or running any test. This is coordinator command syntax, not
  a product/test failure. Next action is to run the same targeted filters as separate handoffctl
  commands.

- 2026-09-28T15:10:14+00:00: Recorded command exit 0; command argv SHA-256
  f7d9933b8fcd922bf02eae7a47191750b74e85b7aa47faba915f3e9070d2d801.

- 2026-09-28T15:10:39+00:00: Recorded command exit 0; command argv SHA-256
  df67a9d0ce5480f3a4e24c9129c3d97e27653fc7928de450349b3e165de4e3e0.

- 2026-09-28T15:11:01+00:00: Recorded command exit 0; command argv SHA-256
  60cbc3cc3a1ff413d952b8e1f2dd45dcd2894b6f1ce4359728347a5ce119d091.

- 2026-09-28T15:11:26+00:00: Recorded command exit 0; command argv SHA-256
  6cc918db7715dcb3f9d421e6487a3b7bb311665eeb02af302cb4fbc0338551a5.

- 2026-09-28T15:11:55+00:00: Recorded command exit 0; command argv SHA-256
  334a01169d03abf10161041207c4df54be82e786f1615724b337385773176013.

- 2026-09-28T15:12:29+00:00: Recorded command exit 0; command argv SHA-256
  637ba1f66119225ce385a2574d2db5de2c47c45424249b3ab904ad3fd4c82f8f.

- 2026-09-28T15:12:47+00:00: Recorded command exit 2; command argv SHA-256
  0ea33d8e77fb93f7bba377fb23d135003b4f010654080aa5fdb5b04249115f0f.

- 2026-09-28T15:14:38+00:00: 2026-09-28T15:12:47+00:00: Recorded exit 2 at the unsigned-development
  verifier smoke-test stage after writing a bounded 13-byte placeholder manifest.json.sig. The task
  projection retained only the command hash, not stderr; this is an acceptance-command failure
  requiring immediate reproduction of the exact verifier invocation and stderr, not a product
  result. Next action: inspect the installed verifier usage and rerun the single verifier command
  through handoffctl with explicit --profile unsigned-development and the exact target/hash
  arguments; preserve strict default verification evidence separately.

- 2026-09-28T15:14:46+00:00: Heartbeat by ar1490-dev-acceptance-luna56.

- 2026-09-28T15:14:59+00:00: Recorded command exit 2; command argv SHA-256
  0ea33d8e77fb93f7bba377fb23d135003b4f010654080aa5fdb5b04249115f0f.

- 2026-09-28T15:15:32+00:00: 2026-09-28T15:14:59+00:00: Reproduced the prior exit-2 exactly. The
  installed verifier reached content validation and reported: bundle verification failed: runtime
  bundle content mismatch: signed inventory does not equal bundle files. The clean bundle manifest
  inventories LICENSE, bin/asb_loopback_sidecar, bin/asb_loopback_supervisor, sbom.spdx.json, and
  sbom.cdx.json; the acceptance install root also contained non-bundle bin/asb and
  bin/ar1490-fixture-agent helpers, so enumeration correctly failed closed. This is an
  acceptance-root contamination error, not a product defect. Next action: extract the exact archive
  into a separate clean verifier root and keep runtime helpers in the execution install root only.

- 2026-09-28T15:15:45+00:00: Recorded command exit 0; command argv SHA-256
  0274a5a12f6e2c37e68f3fd7620064f997863c5b1a0f6edc72fd15735f175b7d.

- 2026-09-28T15:16:03+00:00: Recorded command exit 0; command argv SHA-256
  f30aa1d8dc53f08965298f3b371471e524d7d15495755706ed8f6f1fbc271978.

- 2026-09-28T15:16:20+00:00: Recorded command exit 0; command argv SHA-256
  e00b5cb1c885d88f8d6a8edeada7a68b8136099226c36aa56938927edc9cdab2.
