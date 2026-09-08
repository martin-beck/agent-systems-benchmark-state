---
{
  "branch": "feature/cli-multi-agent-provider-selection",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T00:38:23+00:00",
  "depends_on": [
    "AR-0313",
    "AR-0318",
    "AR-0320",
    "AR-0801"
  ],
  "id": "AR-0869",
  "next_action": "Extend the green provider-plan slice into exact manifest export/import and run/sweep consumption without per-agent overrides; keep Ollama fail-closed until verified daemon evidence is available, then add compare/report/help fixtures and full gates.",
  "observed_branch": "feature/cli-multi-agent-provider-selection",
  "observed_dirty": 4,
  "observed_head": "559fbcc825234bb98a64ba554a53f38b004d24f6",
  "owner": "replay_20260906",
  "plan": "../plans/AR-0869.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Select several agents and apply one preconfigured provider profile through inspectable command-line options.",
  "task_revision": 36,
  "title": "Add CLI multi-agent provider selection",
  "updated_at": "2026-09-08T22:11:48+00:00",
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
