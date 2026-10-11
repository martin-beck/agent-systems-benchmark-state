---
{
  "branch": "feature/ar-1781-external-workload-acquisition-catalog",
  "checkpoint_commit": "cefc884dfbbb43aa9679821154d5d04892670a39",
  "claim_expires": "",
  "depends_on": [
    "AR-1760"
  ],
  "id": "AR-1781",
  "next_action": "Wait for all exact-main workflows at 4a8f0925 to finish green, then post-merge verify and close AR-1781.",
  "observed_branch": "feature/ar-1781-external-workload-acquisition-catalog",
  "observed_dirty": 0,
  "observed_head": "286cccd6d7c0337fe19fbfba4aadacfa0c8b40f5",
  "owner": "",
  "plan": "../plans/AR-1781-external-workload-acquisition-catalog.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "hosted",
    "evidence_digest": "sha256:80ddddc1f96a1895fec0b21ad53c4e40949ba4df68428dae6ffcd7f5a1fc167e",
    "evidence_ref": "github:martin-beck/agent-systems-benchmark/commit/4a8f0925f438a114a0eb61d0fdd52508dadf618b/exact-main-workflows",
    "spec_ref": "specs/AR-1781.json",
    "spec_revision": 2,
    "status": "pass"
  },
  "spec_ref": "specs/AR-1781.json",
  "spec_revision": 2,
  "status": "done",
  "summary": "PR #578 merged at signed local merge 4a8f0925.",
  "task_revision": 42,
  "title": "External workload acquisition catalog",
  "updated_at": "2026-10-11T11:55:19+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1781-external-workload-acquisition-catalog"
}
---

Create the dedicated authoritative catalog behind `asb workload`. The initial
development-supported set is `agentbench`, `agentdojo`, `agentops`,
`ai-agents-that-matter`, `aider-polyglot`, `bigcodebench`, `core-bench`,
`evalplus`, `exercism-tracks`, `hal`, `harbor`, `helm`, `inspect-ai`,
`livecodebench`, `swe-bench`, `swe-bench-pro`, `swe-fficiency`, `swe-lancer`,
`swe-mini`, `swe-perf`, `swe-rebench`, `tau-bench`, and `terminal-bench`.
Inventory any subsequently documented external suite in the same way and define
its official primary source, immutable dataset/release
identity, digest/signature/provenance checks, license/terms, supported platform,
size/resource requirements, required preparation/runtime dependencies, bounded
normalization recipe, workload adapter entrypoint, and compatibility limits.

An external workload is a data/bundle lifecycle, not a tool executable. Do not
reuse `asb tool` records, accept arbitrary URLs, scrape moving upstream state, or
download datasets merely because they appear in a catalog. In development,
absence of a production release authorization, signature, or hosted verification
must not demote a documented suite to methodology-only or block its catalog entry,
installation, selection, or bounded execution. Preserve pinned source identity
and explicit legal/resource constraints; report genuine license, compatibility,
or source failures distinctly. Production qualification may remain separately
labelled.

- 2026-10-11T09:12:57+00:00: Dependency AR-1760 is done; promote AR-1781 for implementation.

- 2026-10-11T09:13:08+00:00: Claimed by ar1781-luna56.

- 2026-10-11T09:17:53+00:00: Recorded command exit 0; command argv SHA-256
  379d22b10394143332e165d35aef5072d33bcfe42a074b67c37a24320167a0ea.

- 2026-10-11T09:26:53+00:00: Heartbeat by ar1781-luna56.

- 2026-10-11T09:26:59+00:00: Checkpointed source commit fd5868cf4c33c67db01cca18eefa4b8aacc024f1.

- 2026-10-11T09:27:06+00:00: PR #572 exact head 66b0df47; refreshed stale workflow provenance digest
  after Rust CI failure. Focused tests and local gates pass; exact-head CI rerun has
  platform/provenance/header/AWQ/fault/fuzz/credential/Kani/Loom green, remaining required jobs
  pending.

- 2026-10-11T09:31:02+00:00: Heartbeat by ar1781-luna56.

- 2026-10-11T09:31:09+00:00: Checkpointed source commit 3827523be8ee914c66368789e2c0dc841743d2de.

- 2026-10-11T09:31:12+00:00: Rust CI root cause was generated catalog capability-family drift:
  generator omitted agentops, helm, AI Agents That Matter, and swe-mini mappings. Added mappings and
  regenerated catalog; focused parity and transcript tests pass. New signed head 72abf364 pushed to
  PR #572.

- 2026-10-11T09:34:52+00:00: Heartbeat by ar1781-luna56.

- 2026-10-11T09:34:57+00:00: Repair 72abf364 is pushed and exact-head CI has no failures. Green:
  AWQ, fuzz, credential-free, headers, Kani, Loom, TLC/Alloy, retained faults, platform, provenance,
  matcher/SLO, TUI. Pending: Rust, emulated AArch64, policy/coverage/supply-chain.

- 2026-10-11T09:45:10+00:00: Heartbeat by ar1781-luna56.

- 2026-10-11T09:46:40+00:00: Heartbeat by ar1781-luna56.

- 2026-10-11T09:46:46+00:00: Checkpointed source commit cefc884dfbbb43aa9679821154d5d04892670a39.

- 2026-10-11T09:46:51+00:00: Independent-review repair complete on product head c4cd8ea6 (signed
  DCO). Added SWE-mini to docs inventory/parity, corrected fixture-boundary wording, and expanded
  Rust/Python/CLI positive dispatch and bounded local-evaluation coverage for agentops,
  ai-agents-that-matter, helm, inspect-ai, harbor, hal, and swe-mini. Local gates: pytest 40 passed;
  cargo test --locked -p asb-workloads passed 43 unit + 4 integration + 5 validity + 2 doctests;
  cargo test --locked -p asb-cli passed 348. PR #572 remains open; parent must merge.

- 2026-10-11T09:48:01+00:00: Hosted exact-head check-runs for c4cd8ea6 are active: 15 total, 3
  completed success (headers, AWQ, provenance), 12 in_progress including Rust, emulated AArch64,
  policy/supply-chain, fuzz, Kani, Loom, TLC, platform, retained faults, credential-free, exact TUI,
  and matcher/SLO. No failures observed; PR remains open and unmerged.

- 2026-10-11T09:54:11+00:00: Heartbeat by ar1781-luna56.

- 2026-10-11T09:54:18+00:00: Repaired hosted Rust/policy diagnostic_contract failure on product head
  7271331b (signed DCO). Refreshed reviewed legacy producer catalog identity legacy_cli_0676 from
  crates/asb-cli/src/lib.rs:16921 to :16958, preserving cause MalformedInput; no contract weakening.
  Focused diagnostic_contract: 9 passed. Full cargo test --locked -p asb-cli: 348 passed. PR remains
  open and unmerged; rerun hosted gates on 7271331b.

- 2026-10-11T10:02:25+00:00: Heartbeat by ar1781-luna56.

- 2026-10-11T10:02:29+00:00: Workflow provenance repair complete on signed DCO product head
  286cccd6. Refreshed docs/examples/asb-cli-workflow-v1.provenance.json cli_source_sha256 from stale
  3021fc... to actual 8d69d7f1c010bb9b3e70570f10e186a9473e2a8bec35846008508e06375aab70; all other
  pinned digests unchanged. Focused workflow_transcript: 3 passed. PR remains open and unmerged;
  hosted gates rerun on 286cccd6.

- 2026-10-11T10:13:37+00:00: Recorded command exit 0; command argv SHA-256
  279a83e801c2421a21b8ba2ad28361837263ce39e61279d163229ba361d275a4.

- 2026-10-11T10:14:19+00:00: PR #572 merged at af75cd06 after exact-head green checks and
  independent review. Post-merge Portable protected-main provenance failed run 38131187031 because
  merge committer is GitHub <noreply@github.com>, while repository policy requires local integration
  identity. Preserve failure; no acceptance/release yet.

- 2026-10-11T10:57:23+00:00: Heartbeat by ar1781-luna56.

- 2026-10-11T10:58:31+00:00: Created repair PR #577 from af75cd06 with empty signed+DCO commit
  198bf869; local merge integrity/signature tests: 54 passed, 23 subtests passed. Historical
  GitHub-committer failure remains preserved; no web merge or history rewrite.

- 2026-10-11T10:59:12+00:00: Heartbeat by ar1781-luna56.

- 2026-10-11T11:03:31+00:00: Heartbeat by ar1781-luna56.

- 2026-10-11T11:04:55+00:00: Heartbeat by ar1781-luna56.

- 2026-10-11T11:29:11+00:00: Independent review and all hosted checks are complete; coordinator
  resumes signed local merge.

- 2026-10-11T11:44:40+00:00: Claimed by coordinator.

- 2026-10-11T11:44:47+00:00: Recorded command exit 1; command argv SHA-256
  666ffef27c4d7fe7010153f3c4a24bd27a3c204b2eee8c55e3f440147312054b.

- 2026-10-11T11:44:57+00:00: Recorded command exit 1; command argv SHA-256
  8cb116041948a2e383ff1e422f8bc819955156a0bdf0875e996297dc25fb715f.

- 2026-10-11T11:45:13+00:00: Recorded command exit 0; command argv SHA-256
  37a53e9bd33eda1a473c3c0349e2fe71b8a062faa0536cf32374dda1be27fd72.

- 2026-10-11T11:45:28+00:00: PR #578 exact head 323aa8c2 passed all hosted checks and independent
  review; merged with base 14de8bce and unchanged tree b4ca9f20.

- 2026-10-11T11:45:31+00:00: Recorded command exit 0; command argv SHA-256
  b91449aa47d635e78e9d59f098f49c726db46333b92a91ba4b6953a5304842f4.

- 2026-10-11T11:54:49+00:00: All exact-main workflows passed at 4a8f0925 after signed merge PR #578.

- 2026-10-11T11:54:52+00:00: Recorded command exit 0; command argv SHA-256
  042079d0f402f52718ba78df47fa3d504e23ba09020e642893521014ec1b682c.

- 2026-10-11T11:55:19+00:00: Post-merge verification complete: all exact-main workflows passed at
  4a8f0925, including Rust verification and repository quality.
