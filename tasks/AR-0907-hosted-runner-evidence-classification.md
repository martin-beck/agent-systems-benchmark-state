---
{
  "branch": "fix/hosted-runner-evidence-classification",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T19:25:36+00:00",
  "depends_on": [
    "AR-0702",
    "AR-0848"
  ],
  "id": "AR-0907",
  "next_action": "Hold unpublished 2953f23470e5d6ad31fc1098f0b967e1e8b263e6 for fresh independent immutable review; publish only after approval and hosted exact-head CI.",
  "observed_branch": "fix/hosted-runner-evidence-classification",
  "observed_dirty": 0,
  "observed_head": "2953f23470e5d6ad31fc1098f0b967e1e8b263e6",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0907.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Separate rolling hosted portability checks from immutable native qualification evidence.",
  "task_revision": 66,
  "title": "Classify hosted runner evidence without weakening native qualification",
  "updated_at": "2026-09-09T17:51:09+00:00",
  "worktree_key": "agent-systems-benchmark-hosted-runner-evidence"
}
---
## AR-0907

Repair the native-platform workflow boundary exposed by the rolling `ubuntu-24.04` hosted image.
Keep AR-0848's exact Ubuntu 24.04.4 native qualification immutable and fail closed while allowing
the hosted runner to report a separately named, non-qualification portability result when its
patch release has advanced.

- 2026-09-09T16:25:32+00:00: Dependencies AR-0702 and AR-0848 are done. The focused
  hosted-portability schema/workflow fence is disjoint from preserved AR-0877/AR-0906 candidates and
  keeps exact native qualification immutable.

- 2026-09-09T16:25:36+00:00: Claimed by quality_20260906.

- 2026-09-09T17:01:56+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-09-09T17:02:19+00:00: Recorded command exit 0; command argv SHA-256
  e4e034d4fe6a0cbcf1b8f2a5b85ed359ee43f7f7fdd8579c0483c523e8b29e8d.

- 2026-09-09T17:02:50+00:00: Recorded command exit 0; command argv SHA-256
  f1b21bc4b1375b43be257a40b139b7b4cc1b1254f16619601de5d42a67c68ed9.

- 2026-09-09T17:06:06+00:00: Recorded command exit 0; command argv SHA-256
  0594fdb22df731bf29f15cdaa373cbe4520119c9851ee20d67a0e0aff2c10158.

- 2026-09-09T17:08:03+00:00: Recorded command exit 0; command argv SHA-256
  effefcb8fba57c2643d3f1fb8ca081872939baf26756d7f7e061c06ba5516227.

- 2026-09-09T17:09:34+00:00: Recorded command exit 1; command argv SHA-256
  a2dfd636fd11a3d4b4fc083d87939e5be5f64d2716d14dbfd1c279574430b0df.

- 2026-09-09T17:11:03+00:00: Recorded command exit 0; command argv SHA-256
  e6da57bcc0d0010e9cfac4ba8776cb05e211ab26ebd48477b1e35988ac60a52a.

- 2026-09-09T17:11:24+00:00: Recorded command exit 1; command argv SHA-256
  69e28ec24d7ef5afadde96b2adcaf023dfe1cd1c91192d3317d988115dd8eba6.

- 2026-09-09T17:11:46+00:00: Recorded command exit 1; command argv SHA-256
  67b373ac3aad4f612afb5c38c6ac7202744c9d848af58ca3383abcf94750a7fa.

- 2026-09-09T17:12:16+00:00: Recorded command exit 1; command argv SHA-256
  2e86ffd4d29a0c27e561bfb4a5467c1d33c63824bcfc3a7b37dee4d9a87cf360.

- 2026-09-09T17:12:43+00:00: Recorded command exit 0; command argv SHA-256
  89f7a3ecb2ebe8546462875441e60e8cff46b28a141745bc569ae72ab2f81dd3.

- 2026-09-09T17:12:59+00:00: Recorded command exit 0; command argv SHA-256
  0402fbceb9beb0a89d6cbd398aa5c104c6a87812da627e5ba3fd61d94d83229d.

- 2026-09-09T17:13:24+00:00: Recorded command exit 0; command argv SHA-256
  2e86ffd4d29a0c27e561bfb4a5467c1d33c63824bcfc3a7b37dee4d9a87cf360.

- 2026-09-09T17:13:57+00:00: Recorded command exit 1; command argv SHA-256
  3840ca0770c999e00fefc1da5f7457a297a4cb4c3c1f19edef8fbd864cfe1167.

- 2026-09-09T17:14:12+00:00: Recorded command exit 0; command argv SHA-256
  0e2e94b8cab29de96ed540bf0e279ff4a7b88106a92604d306202ba96aa53894.

- 2026-09-09T17:14:30+00:00: Recorded command exit 0; command argv SHA-256
  5a129cbafdf9833de0ae264d89a23ae673db92a86a1454144f6845bd486994dd.

- 2026-09-09T17:14:53+00:00: Recorded command exit 1; command argv SHA-256
  3840ca0770c999e00fefc1da5f7457a297a4cb4c3c1f19edef8fbd864cfe1167.

- 2026-09-09T17:15:12+00:00: Recorded command exit 1; command argv SHA-256
  a5f7fdafdc6b68477d21d16b6c55e356bc3b5cf9b728738f47251cee5b8e73a9.

- 2026-09-09T17:15:31+00:00: Recorded command exit 0; command argv SHA-256
  6835c2458c867b3096c7cc176220a0519e7f28484016264563c9ef02e825561c.

- 2026-09-09T17:15:50+00:00: Recorded command exit 0; command argv SHA-256
  b96b6d37abf12ef7ec2a8e7d4ee8d0a61f87e19f7e609e9329e37f9099c8a683.

- 2026-09-09T17:17:02+00:00: Recorded command exit 0; command argv SHA-256
  8916e384b09ecdd2d394855e5b7744be5cc9f0186d1c0e5cce640f4357787ec3.

- 2026-09-09T17:17:21+00:00: Recorded command exit 2; command argv SHA-256
  2cabf2ab38f872db52dc8ad99fb44c994b0fe4ee284a5e35744999220a14bef8.

- 2026-09-09T17:17:41+00:00: Recorded command exit 1; command argv SHA-256
  00d051053106e2ae54c7089466e691e7719756974aa5cb92e4b1ce5463d74415.

- 2026-09-09T17:17:58+00:00: Recorded command exit 0; command argv SHA-256
  1ade0f291b8d88b6f24c065862f72c72762f5198a8990f4c416b8168dec74907.

- 2026-09-09T17:18:19+00:00: Recorded command exit 0; command argv SHA-256
  41a16a2105427681cad5d8f1815611a7969170850fdcd26d2e3876b55bdc9242.

- 2026-09-09T17:18:55+00:00: Implemented the seven-path AR-0907 slice on exact base b6d04a8. The
  workflow now routes exact Ubuntu 24.04.4 through unchanged native_evidence and newer well-formed
  Noble patch releases through a distinct hosted-portability collector/schema; artifacts are
  conditionally named and native partial evidence cannot upload. The native validator and historical
  evidence are unchanged, and a focused negative proves 24.04.5 is still rejected. Closed schema
  fixture runs 16 unique mutations; source-race, raw-private-diagnostic redaction, stale/symlink
  output and workflow-kind tests are included. Focused hosted tests 6/6 and existing native capacity
  tests 11/11 pass; Ruff, strict mypy with imported legacy module skipped, actionlint, zizmor and
  diff-check pass. Earlier exit 1/2 results were operator harness issues only: non-package unittest
  import, missing jsonschema in system Python, one mistyped test filename, and Ruff-requested
  context consolidation; corrected commands are green. Dirty scope is exactly seven planned paths;
  f385fb27 and PRs #120/#121/#122 remain unchanged.

- 2026-09-09T17:20:59+00:00: Recorded command exit 0; command argv SHA-256
  76bae6a04d7e57cfe901b77289ca19d0548d2b017db5e59b9cea2437a0dedfcd.

- 2026-09-09T17:21:52+00:00: Recorded command exit 1; command argv SHA-256
  d290e55ef438a7ef9dcf959911fd4e647a0849b03d4dae976016033dc51538eb.

- 2026-09-09T17:22:20+00:00: Recorded command exit 0; command argv SHA-256
  fc0252eb1bd0c076f890fde4a64f4247c27eb69046f6bcd80fba417f4f642945.

- 2026-09-09T17:22:47+00:00: Recorded command exit 0; command argv SHA-256
  89ec80e6e0261fcef9cf073d492b5681ae5c885c77824a2a692c1d93fe85ebb3.

- 2026-09-09T17:24:25+00:00: Recorded command exit 1; command argv SHA-256
  8641fa3ee015caf341a75a0121505e10a122e8af4be59c1558aa35d7e6c60b37.

- 2026-09-09T17:25:08+00:00: Recorded command exit 1; command argv SHA-256
  b523189e89e807b94bf92402d6a6b7be2d56b8d7817b29235246716e6867912a.

- 2026-09-09T17:25:29+00:00: Recorded command exit 0; command argv SHA-256
  01095e9bf655e7a35a300e83898c8e43ec4a43918a5f892ccea615d512ffcd25.

- 2026-09-09T17:26:33+00:00: Recorded command exit 0; command argv SHA-256
  e3dd28e4499b825b6ee0ed87bab551c6cc0236de9c6c3779bfdc4c63fd038e0e.

- 2026-09-09T17:27:10+00:00: Recorded command exit 1; command argv SHA-256
  7ae2e13ad1f8198a47329d5f4516371d04d0d5cd165eafd1b7e45b57a1f4fb1d.

- 2026-09-09T17:27:29+00:00: Recorded command exit 1; command argv SHA-256
  62f85140f59f659a13760681dc118da8e539a3b6257e38b3ae8221fb40c02525.

- 2026-09-09T17:27:55+00:00: Recorded command exit 1; command argv SHA-256
  4f5bb41046bfafeff82b17c992b57609b3b8478ca167448d92b8132bc7281666.

- 2026-09-09T17:28:50+00:00: Recorded command exit 0; command argv SHA-256
  d864b8e6f0fd769a5ed96fe728e21d901bdd3a11abff280e38060dd1e4071ad3.

- 2026-09-09T17:29:15+00:00: Recorded command exit 0; command argv SHA-256
  41a16a2105427681cad5d8f1815611a7969170850fdcd26d2e3876b55bdc9242.

- 2026-09-09T17:30:09+00:00: Recorded command exit 0; command argv SHA-256
  a9eda37ce25a73d0ccd6deda85f41cf7e4338b6776531738f335ed3819cf4405.

- 2026-09-09T17:30:34+00:00: Recorded command exit 0; command argv SHA-256
  d3c3620d3956f2c271c39826f02d102599beeb6c6cef657ecaf5336784a1fde5.

- 2026-09-09T17:31:06+00:00: Signed+DCO candidate faca6aa9ddddbbed8b925cfbf6a380d622726902 (tree
  1b8b2acc47332aec27dea27ea24cc96e88ab6851, exact parent b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b)
  is clean and exactly seven owned paths. Fixtures live in a dedicated hosted-portability
  subdirectory so the existing root failure-fixture loader remains closed. Focused hosted 6/6,
  native capacity 11/11, all platform 52/52, full workspace fmt/clippy/tests/docs/release, contract
  consistency, failure paths, coverage, deny/audit, Ruff, strict mypy boundary, actionlint, zizmor,
  source headers, exact-range policy, Gitleaks, diff and privacy gates pass. First all-platform
  attempt exposed fixture namespace collision and was repaired; first coverage run hit a
  pre-existing asb-metrics subprocess classification flake after the ordinary workspace suite had
  passed, while the unchanged-tree full coverage rerun passed. Native validator/native 24.04.4
  evidence and integration f385fb27/PRs #120-#122 are unchanged. SSH signature, exact DCO, parent
  and scope verified; unpublished.

- 2026-09-09T17:38:42+00:00: Recorded command exit 0; command argv SHA-256
  d431d9f3bf519cc3be5a57272fef1e6bfac0bd8d5c581bc522e39e59201dc741.

- 2026-09-09T17:39:26+00:00: Recorded command exit 0; command argv SHA-256
  9ac90b5c523f74ce987d39c17c9b626c7384605fa2bebe353ff7b8ea500eed5a.

- 2026-09-09T17:39:54+00:00: Recorded command exit 1; command argv SHA-256
  30deaf4cef52961646c75915bab43c324e6e7576de1172af9a6ccfd258862650.

- 2026-09-09T17:40:12+00:00: Recorded command exit 0; command argv SHA-256
  739fff2444ae54c8e7e4545dee3d7115053b712c78bcc061eb05b0648e78b4e5.

- 2026-09-09T17:40:31+00:00: Recorded command exit 1; command argv SHA-256
  30deaf4cef52961646c75915bab43c324e6e7576de1172af9a6ccfd258862650.

- 2026-09-09T17:41:09+00:00: Recorded command exit 0; command argv SHA-256
  77a80fc75e184307da9927790521095cbee36ecb5baa9e1fa6475ce878d63705.

- 2026-09-09T17:41:28+00:00: Recorded command exit 0; command argv SHA-256
  30deaf4cef52961646c75915bab43c324e6e7576de1172af9a6ccfd258862650.

- 2026-09-09T17:42:01+00:00: Recorded command exit 0; command argv SHA-256
  603df57952191fa4683e2ac6d5c988d11a05e29c3b975b723fddb0aeac5f722e.

- 2026-09-09T17:42:22+00:00: Recorded command exit 0; command argv SHA-256
  41a16a2105427681cad5d8f1815611a7969170850fdcd26d2e3876b55bdc9242.

- 2026-09-09T17:42:52+00:00: Recorded command exit 0; command argv SHA-256
  5515bd3c50e7ae051b88b81919d6353fcd78d0c66bb687de6332851a59b182a2.

- 2026-09-09T17:44:26+00:00: Recorded command exit 0; command argv SHA-256
  9c46012ea7d8037a2d52c0b470ebde4423aa6729ef0b557795045f4cba83d72a.

- 2026-09-09T17:45:31+00:00: Reviewer repair complete. Candidate
  2953f23470e5d6ad31fc1098f0b967e1e8b263e6, tree 5673b12807d3821ec9a3933a8058848b6e54e7aa, parent
  faca6aa9ddddbbed8b925cfbf6a380d622726902; clean two-commit seven-path range on exact base
  b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b, SSH signatures and DCO verified. Public workflow now
  distinguishes hosted portability from native qualification; exact closed route schema and semantic
  pair validate before upload; failures remove artifacts and emit no raw diagnostics; executable
  hosted/native positives plus malformed, ambiguous and unknown-route no-artifact negatives pass.
  Final handoffctl gate batch exit 0: both signatures, DCO, exact-range policy, contract
  consistency, manifest validation, all platform tests, failure paths, artifact outcome, Ruff,
  strict mypy boundary, actionlint, zizmor, Gitleaks, cargo fmt/clippy workspace all-targets -D
  warnings, diff/clean checks. Unsupported native qualification on rolling hosted images remains
  explicit.

- 2026-09-09T17:51:09+00:00: Recorded command exit 127; command argv SHA-256
  d47783a22c0773184ae348243555e8eb8edd90e90b2f1cbe35a0dc8fb675e37c.
