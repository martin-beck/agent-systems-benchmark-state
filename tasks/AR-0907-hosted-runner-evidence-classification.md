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
  "next_action": "Run full workspace, policy, privacy, failure and platform gates; then create a focused signed candidate for independent review.",
  "observed_branch": "fix/hosted-runner-evidence-classification",
  "observed_dirty": 6,
  "observed_head": "b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0907.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Separate rolling hosted portability checks from immutable native qualification evidence.",
  "task_revision": 39,
  "title": "Classify hosted runner evidence without weakening native qualification",
  "updated_at": "2026-09-09T17:24:25+00:00",
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
