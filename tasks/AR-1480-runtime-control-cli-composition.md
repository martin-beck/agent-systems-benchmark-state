---
{
  "branch": "feature/ar-1480-runtime-control-cli-composition",
  "checkpoint_commit": "fdc7f59f83f647ce099439b003848291e81dd3bb",
  "claim_expires": "2026-09-27T13:51:46+00:00",
  "depends_on": [
    "AR-1473",
    "AR-1472"
  ],
  "id": "AR-1480",
  "next_action": "Monitor eight exact-main post-merge workflows for fdc7f59f83f647ce099439b003848291e81dd3bb to terminal SUCCESS; then reconcile/doctor and release done.",
  "observed_branch": "feature/ar-1480-runtime-control-cli-composition",
  "observed_dirty": 0,
  "observed_head": "440a06427d6e6fe2aacaebc2a50c5f924527dd04",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1480-runtime-control-cli-composition.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Compose authenticated runtime enrollment into opaque normal CLI run and sweep dispatch.",
  "task_revision": 71,
  "title": "Runtime-control CLI composition",
  "updated_at": "2026-09-27T11:53:49+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1480-runtime-control-cli-composition"
}
---

Successor to the stale AR-1374/1375 adapter chain. AR-1473 and AR-1472 are
the only implementation dependencies; live provider reachability is optional
and never gates local qualification.

- The composition must preserve opaque authority and fail closed on missing,
  stale, revoked, replayed, mismatched, or caller-supplied inputs.
- Qualification uses deterministic local/mock/replay evidence only.

- 2026-09-27T11:17:28+00:00: AR-1473 and AR-1472 are durably done; promote dependency-safe CLI
  composition successor with no circular AR-1374/1375 edge.

- 2026-09-27T11:17:30+00:00: Claimed by ar1332-record-replay-luna56.

- 2026-09-27T11:17:41+00:00: Recorded command exit 0; command argv SHA-256
  31ef8dba69cadb96f0eab7a54672aa35e58192283fa68f6c82d04e7f76edc9be.

- 2026-09-27T11:18:08+00:00: Recorded command exit 0; command argv SHA-256
  e5e483509179e2d1e0604ee0f63271ced6232cbfb60eb6ccdf9fe0c6ad23a76a.

- 2026-09-27T11:20:14+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T11:20:31+00:00: After complete AR-1480 plan/docs review and current-main audit,
  implementation adds RuntimeControlDispatchSource and run_with_runtime_control_source in asb-cli.
  The seam resolves only an opaque LiveProviderRuntimeDispatchSource from runtime/control and fails
  closed before CLI effects when unavailable; docs state ordinary process run/sweep cannot construct
  authority. Added hostile unavailable-source test; no asb-tui/live provider.

- 2026-09-27T11:21:04+00:00: Recorded command exit 0; command argv SHA-256
  b2f3fb06dee43d704705616108ddb13e7dcca021834cb50f5a41e895d2b16eff.

- 2026-09-27T11:21:37+00:00: Recorded command exit 0; command argv SHA-256
  c9a2916a927594a512151f14eab59803113f12061a17b617a103789a4ff6a824.

- 2026-09-27T11:22:04+00:00: Recorded command exit 0; command argv SHA-256
  b7a391741901b8aade6d43c13786c703d443b46d94efdaa27c0f02fa2d51a198.

- 2026-09-27T11:22:34+00:00: Recorded command exit 0; command argv SHA-256
  c44ed960f90bd281b4395dd1445881d59d09fa681f7e317ba9f0254abb8780d1.

- 2026-09-27T11:24:25+00:00: Implementation checkpoint: AR-1480 adds RuntimeControlDispatchSource
  and run_with_runtime_control_source to asb-cli. The runtime/control seam resolves only an opaque
  LiveProviderRuntimeDispatchSource and returns bounded Unavailable before CLI effects; existing
  runtime-owned source remains private. Added hostile unavailable-source test and docs/workflow
  boundary note. After refreshing clean worktree to protected main 59323f41, focused runtime source
  and CLI fail-closed tests pass. Full workspace gates are currently running under handoffctl.

- 2026-09-27T11:24:40+00:00: Recorded command exit 101; command argv SHA-256
  e1c351c46494fcbac29ac31b75b8949233e665b6ae0d88686ef9580974dee8dc.

- 2026-09-27T11:25:35+00:00: Recorded command exit 101; command argv SHA-256
  d6ece9b50bad2e5bcf4979b15480d66d38cc94e188f9c1155f51ca9f32af5728.

- 2026-09-27T11:26:08+00:00: Recorded command exit 0; command argv SHA-256
  a7f68e4c0b3fa94122973819ed7485fa9cfc8473bfd3fa2043727b74f6172a40.

- 2026-09-27T11:26:30+00:00: Recorded command exit 0; command argv SHA-256
  19d47c10c4c4e824f5a4b03933e6b89ad4378dcfbd931f0f6da06e7d709b71a8.

- 2026-09-27T11:26:58+00:00: Full workspace test initially exited 101 on existing provenance
  contract test crates/asb-cli/tests/workflow_transcript.rs: expected cli_source_sha256 4696... but
  current lib hash was f5ee7317... due this intentional CLI change. No behavioral failure. Updated
  docs/examples/asb-cli-workflow-v1.provenance.json through handoffctl product run to the exact
  current hash; focused provenance test now passes 1/1. Preserve this deterministic
  provenance-refresh evidence before full rerun.

- 2026-09-27T11:28:37+00:00: Recorded command exit 1; command argv SHA-256
  8aec24a200be13f45450c587096d341e2afdfa97823b21330001e5162e0de7c2.

- 2026-09-27T11:29:29+00:00: Recorded command exit 0; command argv SHA-256
  e6f9d6dc8581eb1ebfccd6a34944eb45eca27527ddac007d7ae2bf727be4d15f.

- 2026-09-27T11:29:47+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T11:29:59+00:00: Classified full-gate exit 1 at 11:28:37: test -z git status failed
  because intended AR-1480 edits remained uncommitted (crates/asb-cli/src/lib.rs,
  docs/workflows/live-benchmark.md, docs/examples/asb-cli-workflow-v1.provenance.json); git diff
  --check passed. No product/test failure. Next action is run all substantive gates, then commit and
  re-run clean-tree gate.

- 2026-09-27T11:30:53+00:00: Recorded command exit 0; command argv SHA-256
  d6ed271cd6406f5cd02bcbd13ceedf92e245ea54caa56c28331cc3096e6b4a73.

- 2026-09-27T11:31:42+00:00: Recorded command exit 0; command argv SHA-256
  aa4b2716e98888b03b64f7839366d14c6e17396f41897c106dd5da48ad9892d3.

- 2026-09-27T11:32:04+00:00: Recorded command exit 0; command argv SHA-256
  7b73527d07973b86f8af466c4657187927e5242172187adc5adf973bcf72f8fa.

- 2026-09-27T11:32:25+00:00: Recorded command exit 0; command argv SHA-256
  2bf60254e3012389c378045204c8538ea36bc5527904a611d872dbca7d1124e3.

- 2026-09-27T11:32:52+00:00: Independent diff review complete: scoped changes are
  crates/asb-cli/src/lib.rs, live-benchmark.md, and provenance JSON only; runtime/control seam
  returns only opaque source, fail-closed unavailable path has positive/negative coverage, no
  asb-tui/live-provider dependency or authority leakage. Substantive workspace
  test/clippy/rustdoc/release build, repository policy/contract/signature/verify tests, provenance
  test, and diff check exited 0. Signed+DCO commit 440a06427d6e6fe2aacaebc2a50c5f924527dd04 verified
  with SSH signature.

- 2026-09-27T11:33:24+00:00: Recorded command exit 0; command argv SHA-256
  b1707df17cb53b6b197afd0b19bcff87c5a010c73a97a7713f682652ea99c53f.

- 2026-09-27T11:33:48+00:00: Recorded command exit 0; command argv SHA-256
  524d5d8eef94ae98cb212b7ecc32ff8eb32720a9a0e6d858275c8278d63cb279.

- 2026-09-27T11:34:13+00:00: Recorded command exit 0; command argv SHA-256
  19ee90ebc11b82d6cb7b9f45925314fc8a4733cdf91f0613cea620cc6e4ebb5d.

- 2026-09-27T11:34:45+00:00: Published PR #357:
  https://github.com/martin-beck/agent-systems-benchmark/pull/357 at exact signed head
  440a06427d6e6fe2aacaebc2a50c5f924527dd04, base main. Initial statusCheckRollup: 13 required checks
  IN_PROGRESS (Credential-free benchmark path; Emulated aarch64; Retained faults; TLC/Alloy;
  Platform evidence; Policy/coverage/supply chain; Rust; Bounded fuzz; Kani; Matcher/SLO; Loom/state
  models), plus AWQ shadow and Huawei/SPDX header checks SUCCESS. PR remains OPEN/UNSTABLE; no merge
  attempted.

- 2026-09-27T11:34:56+00:00: Recorded command exit 0; command argv SHA-256
  36858f90dedbb97237067ef509fb80b72c2131f33bbf313a3da978919a9b4667.

- 2026-09-27T11:35:22+00:00: PR #357 poll at exact head 440a06427d6e6fe2aacaebc2a50c5f924527dd04
  remains UNSTABLE with required checks pending. Newly terminal SUCCESS: Retained faults and
  Loom/state models; AWQ shadow and Huawei/SPDX headers remain SUCCESS. Still IN_PROGRESS:
  Credential-free, Emulated aarch64, TLC/Alloy, Platform evidence, Policy/coverage/supply chain,
  Rust, Bounded fuzz, Kani, Matcher/SLO. No failures; continue bounded polling.

- 2026-09-27T11:35:32+00:00: Recorded command exit 0; command argv SHA-256
  36858f90dedbb97237067ef509fb80b72c2131f33bbf313a3da978919a9b4667.

- 2026-09-27T11:35:58+00:00: PR #357 exact-head poll: SUCCESS now includes Platform evidence,
  Bounded fuzz regressions, Kani bounded proofs, Matcher/SLO mutation sentinels, plus prior Retained
  faults, Loom/state models, AWQ shadow, Huawei/SPDX. Remaining IN_PROGRESS: Credential-free
  benchmark path, Emulated aarch64, TLC/Alloy recovery models, Policy/coverage/supply chain, Rust
  checks. PR remains UNSTABLE; no failures or merge.

- 2026-09-27T11:36:07+00:00: Recorded command exit 0; command argv SHA-256
  36858f90dedbb97237067ef509fb80b72c2131f33bbf313a3da978919a9b4667.

- 2026-09-27T11:36:35+00:00: PR #357 exact-head poll: Credential-free benchmark path completed
  SUCCESS. Remaining IN_PROGRESS only Emulated aarch64, TLC/Alloy recovery models,
  Policy/coverage/supply chain, Rust checks. All other required checks terminal SUCCESS; no
  failures; PR remains UNSTABLE pending these four.

- 2026-09-27T11:36:46+00:00: Recorded command exit 0; command argv SHA-256
  36858f90dedbb97237067ef509fb80b72c2131f33bbf313a3da978919a9b4667.

- 2026-09-27T11:37:06+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T11:37:38+00:00: Recorded command exit 0; command argv SHA-256
  36858f90dedbb97237067ef509fb80b72c2131f33bbf313a3da978919a9b4667.

- 2026-09-27T11:37:57+00:00: PR #357 poll: TLC and Alloy recovery models completed SUCCESS.
  Remaining IN_PROGRESS are Emulated aarch64, Policy/coverage/supply chain, and Rust checks; all
  other checks terminal SUCCESS. Exact head unchanged; no failures or merge.

- 2026-09-27T11:38:26+00:00: Recorded command exit 0; command argv SHA-256
  36858f90dedbb97237067ef509fb80b72c2131f33bbf313a3da978919a9b4667.

- 2026-09-27T11:38:43+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T11:39:25+00:00: Recorded command exit 0; command argv SHA-256
  36858f90dedbb97237067ef509fb80b72c2131f33bbf313a3da978919a9b4667.

- 2026-09-27T11:39:41+00:00: Recorded command exit 0; command argv SHA-256
  36858f90dedbb97237067ef509fb80b72c2131f33bbf313a3da978919a9b4667.

- 2026-09-27T11:40:52+00:00: Recorded command exit 0; command argv SHA-256
  36858f90dedbb97237067ef509fb80b72c2131f33bbf313a3da978919a9b4667.

- 2026-09-27T11:41:21+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T11:42:26+00:00: Recorded command exit 0; command argv SHA-256
  36858f90dedbb97237067ef509fb80b72c2131f33bbf313a3da978919a9b4667.

- 2026-09-27T11:42:56+00:00: PR #357 exact-head poll: Rust checks and Emulated aarch64 completed
  SUCCESS. 12/13 required checks are terminal SUCCESS; only Policy, coverage, and supply chain
  remains IN_PROGRESS. Exact signed head unchanged; no failures or merge.

- 2026-09-27T11:43:35+00:00: Recorded command exit 0; command argv SHA-256
  36858f90dedbb97237067ef509fb80b72c2131f33bbf313a3da978919a9b4667.

- 2026-09-27T11:43:59+00:00: PR #357 exact-head final matrix is fully green: all 13 required checks
  SUCCESS at signed head 440a06427d6e6fe2aacaebc2a50c5f924527dd04; mergeStateStatus CLEAN.
  Independent review already recorded; authorized to merge normally.

- 2026-09-27T11:44:11+00:00: Recorded command exit 0; command argv SHA-256
  b492be8f08129c5766ac1d742da982e4c24205df57dc5fb49c84c2e51eb86445.

- 2026-09-27T11:44:35+00:00: Recorded command exit 0; command argv SHA-256
  2a163713d1f19f267be05b465a32c8af5ad692ecc87892e8ac14e8d1b1e8ad1c.

- 2026-09-27T11:45:04+00:00: PR #357 merged normally at 2026-09-27T11:44:10Z. Merge SHA
  fdc7f59f83f647ce099439b003848291e81dd3bb; PR head was 440a06427d6e6fe2aacaebc2a50c5f924527dd04.
  Exact-main workflows launched: Repository quality 36316693442, Credential-free benchmark path
  36316693423, Huawei MIT source headers 36316693365 (SUCCESS), Fault assurance 36316693349
  (QUEUED), Rust verification 36316693344, Emulated aarch64 portability 36316693340, Formal
  assurance 36316693339, Hosted portability/native qualification 36316693310 (remaining
  IN_PROGRESS/QUEUED). No release yet.

- 2026-09-27T11:45:51+00:00: Recorded command exit 0; command argv SHA-256
  c959ff840bb803270069c9b4f4fb7cdb6b332e30f47ca07b7fa4531327d0060d.

- 2026-09-27T11:46:20+00:00: Post-merge poll for exact SHA fdc7f59f83f647ce099439b003848291e81dd3bb:
  Credential-free 36316693423 and Huawei headers 36316693365 SUCCESS; Repository quality
  36316693442, Fault assurance 36316693349, Rust 36316693344, Emulated aarch64 36316693340, Formal
  36316693339, Hosted portability/native 36316693310 remain IN_PROGRESS. No failures; continue
  monitoring.

- 2026-09-27T11:47:15+00:00: Recorded command exit 0; command argv SHA-256
  c959ff840bb803270069c9b4f4fb7cdb6b332e30f47ca07b7fa4531327d0060d.

- 2026-09-27T11:47:46+00:00: Post-merge poll exact SHA fdc7f59f83f647ce099439b003848291e81dd3bb:
  Fault assurance 36316693349 and Hosted portability/native 36316693310 now SUCCESS; Credential-free
  and Huawei headers remain SUCCESS. Repository quality 36316693442, Rust 36316693344, Emulated
  aarch64 36316693340, Formal 36316693339 remain IN_PROGRESS; no failures.

- 2026-09-27T11:48:42+00:00: Recorded command exit 0; command argv SHA-256
  c959ff840bb803270069c9b4f4fb7cdb6b332e30f47ca07b7fa4531327d0060d.

- 2026-09-27T11:49:07+00:00: Post-merge poll exact SHA fdc7f59f83f647ce099439b003848291e81dd3bb:
  Formal assurance 36316693339 completed SUCCESS. Six workflows now SUCCESS; only Repository quality
  36316693442, Rust verification 36316693344, and Emulated aarch64 36316693340 remain IN_PROGRESS.
  No failures.

- 2026-09-27T11:50:04+00:00: Recorded command exit 0; command argv SHA-256
  c959ff840bb803270069c9b4f4fb7cdb6b332e30f47ca07b7fa4531327d0060d.

- 2026-09-27T11:50:32+00:00: Post-merge poll exact SHA fdc7f59f83f647ce099439b003848291e81dd3bb:
  Rust verification 36316693344 completed SUCCESS. Six workflows plus Rust are green; only
  Repository quality 36316693442 and Emulated aarch64 36316693340 remain IN_PROGRESS. No failures.

- 2026-09-27T11:51:27+00:00: Recorded command exit 0; command argv SHA-256
  c959ff840bb803270069c9b4f4fb7cdb6b332e30f47ca07b7fa4531327d0060d.

- 2026-09-27T11:51:46+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T11:52:41+00:00: Recorded command exit 0; command argv SHA-256
  c959ff840bb803270069c9b4f4fb7cdb6b332e30f47ca07b7fa4531327d0060d.

- 2026-09-27T11:53:49+00:00: Recorded command exit 0; command argv SHA-256
  ad4444b0126de6a5a24acb41006f4c0ede7cff63cc27673a50874efa968fdf93.
