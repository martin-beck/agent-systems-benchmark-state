---
{
  "branch": "feature/ar-1436-local-guided-cli-wrapper",
  "checkpoint_commit": "ae48046d980237d078dd2a5aa155400d20330059",
  "claim_expires": "2026-09-25T02:43:20+00:00",
  "depends_on": [
    "AR-1435",
    "AR-1328"
  ],
  "id": "AR-1436",
  "next_action": "Monitor PR #317 exact head ae48046 until all required checks pass; merge only after CLEAN state and exact-head verification.",
  "observed_branch": "feature/ar-1436-local-guided-cli-wrapper",
  "observed_dirty": 0,
  "observed_head": "ae48046d980237d078dd2a5aa155400d20330059",
  "owner": "codex-asb-ar1436-local-guided-luna56",
  "plan": "../plans/AR-1436-local-guided-cli-wrapper.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add a catalog-driven guided CLI wrapper for deterministic local mock qualification.",
  "task_revision": 56,
  "title": "Local guided CLI wrapper",
  "updated_at": "2026-09-25T01:07:08+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1436-local-guided-cli-wrapper"
}
---

Local-only successor to AR-1435. This task may use only the deterministic
runtime-owned local mock. AR-1329 and AR-1338 remain blocked/planned and are
not resumed. AR-1332 and AR-1333 are future integration references, not
completion dependencies; AR-1333 reaches the blocked live-provider chain.

The wrapper must remain a thin catalog/config-driven delegation layer over
`asb run` and `asb sweep --use-config`, with explicit local qualification,
offline/default denial, no external provider, no credential bytes, no caller
endpoint, no `LiveProviderAttempt`, and no production egress or authority
weakening. Require focused/full/review/PR/seven post-merge gates.

- 2026-09-25T00:43:12+00:00: Promoted: completed dependencies AR-1435 and AR-1328 verified.
  AR-1332/AR-1333 remain planned references only; AR-1329/AR-1338 untouched. Begin local-only
  catalog-driven wrapper with explicit mock qualification and fail-closed live path.

- 2026-09-25T00:43:20+00:00: Claimed by codex-asb-ar1436-local-guided-luna56.

- 2026-09-25T00:43:33+00:00: Recorded command exit 0; command argv SHA-256
  b3c54e469f86e1ddbb6f6063fc4d2921be9e210b1bfce5de3610ed8e03380946.

- 2026-09-25T00:45:36+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-25T00:45:55+00:00: Recorded command exit 1; command argv SHA-256
  856c2c32ebf286180f6e23e7f1e8ae20312ff6548988a044a5afc15e6a8595d4.

- 2026-09-25T00:46:32+00:00: Recorded command exit 0; command argv SHA-256
  2b5b77c523555f81a83fb1ed2aaa818f88f25b6db436c1330b5c91c185b2f167.

- 2026-09-25T00:47:03+00:00: Diagnosed prior exit-1 records: 00:45:36 cargo fmt was invoked from the
  coordination state checkout, which has no Cargo.toml; corrected by running through handoffctl in
  the bound product worktree. 00:45:55 cargo fmt --check correctly found only rustfmt layout changes
  in the new dispatch/parser code; applied cargo fmt and continued. No product gate was weakened and
  live-provider boundaries remain fail-closed.

- 2026-09-25T00:47:12+00:00: Recorded command exit 0; command argv SHA-256
  61f8fd0e64a80ce461c03f246c8626084bffdf38268a3f72045ff85a809d9f03.

- 2026-09-25T00:48:04+00:00: Recorded command exit 101; command argv SHA-256
  2b5b77c523555f81a83fb1ed2aaa818f88f25b6db436c1330b5c91c185b2f167.

- 2026-09-25T00:48:30+00:00: Recorded command exit 0; command argv SHA-256
  2b5b77c523555f81a83fb1ed2aaa818f88f25b6db436c1330b5c91c185b2f167.

- 2026-09-25T00:49:19+00:00: Implementation committed and pushed as signed+DCO 2dbbfd8. Added
  explicit asb easy run|sweep PATH --use-config --local-mock delegation, hostile option/absence
  tests, positive catalog-bound local mock run test, help/completion entries, and workflow
  documentation. Focused two-test gate passes; no live provider or external endpoint path added.

- 2026-09-25T00:49:53+00:00: Recorded command exit 101; command argv SHA-256
  88f7af68d2ecc3638bfd9fff251cc79e4f54fee616e0c550b931fe77cecde9a1.

- 2026-09-25T00:50:19+00:00: Full workspace test at 2dbbfd8 failed only
  capability_contract::command_ignores_hostile_environment_and_help_completion_are_explicit because
  adding easy between setup and capabilities changed the stable completion token sequence. Corrected
  in signed+DCO 3e80aa3 by appending easy after the existing sequence; no behavior or security
  boundary weakened.

- 2026-09-25T00:50:44+00:00: Recorded command exit 101; command argv SHA-256
  88f7af68d2ecc3638bfd9fff251cc79e4f54fee616e0c550b931fe77cecde9a1.

- 2026-09-25T00:51:28+00:00: Diagnosed full-test exit 101 at 00:50:44: workflow_transcript
  provenance guard detected stale CLI source digest after the completion-order fix (actual
  d09919d1e5025c5e43dfd3a057b9ccad62510107e7952004636dce68124121f versus recorded 0af35b...).
  Refreshed docs/examples/asb-cli-workflow-v1.provenance.json in signed+DCO 4b1213d and pushed. No
  gate suppression or runtime boundary change.

- 2026-09-25T00:52:02+00:00: Recorded command exit 0; command argv SHA-256
  88f7af68d2ecc3638bfd9fff251cc79e4f54fee616e0c550b931fe77cecde9a1.

- 2026-09-25T00:52:31+00:00: Recorded command exit 101; command argv SHA-256
  000f7c77b968663638076c946bf0f392f0cbc82d5f370a66d5405fe755f41a42.

- 2026-09-25T00:53:02+00:00: Clippy gate after provenance refresh found one real lint: needless
  borrow in guided_local_at SelectionSource::Config(&store). Corrected to pass the existing
  reference in signed+DCO 671bb7e; no allow or gate weakening.

- 2026-09-25T00:53:23+00:00: Recorded command exit 101; command argv SHA-256
  11bd125eca1a90017ea3ff21b22e028ea8405e6387607e767fde008f6bf77b8d.

- 2026-09-25T00:53:49+00:00: Diagnosed full test exit 101 at 00:53:23: two pre-existing control
  tests failed under parallel workspace execution with control state root already owned
  (state_root_is_exclusive_and_uncertain_restart_fails_closed;
  recording_campaign_plan_is_durable_idempotent_and_not_offline_ready). Guided wrapper tests passed;
  no wrapper or live-boundary failure. Preserve evidence and rerun serially before publication.

- 2026-09-25T00:54:17+00:00: Recorded command exit 101; command argv SHA-256
  24610b46a7959f76b8edc7911bb3f62d348b8bfa908d3c54d7e8e2bec6530733.

- 2026-09-25T00:54:50+00:00: Serial rerun confirmed the parallel state-root ownership failures were
  environmental test contention, but provenance also changed after the final clippy fix (actual CLI
  digest ab38037e...). Refreshed provenance to ab38037e in signed+DCO ae48046; run provenance only
  after all source edits are final.

- 2026-09-25T00:55:37+00:00: Recorded command exit 0; command argv SHA-256
  2bdf430229143084d857d5758bce071c8591b34978263e4c2ff495a656da7663.

- 2026-09-25T00:56:07+00:00: Recorded command exit 0; command argv SHA-256
  81fdfca6bb17c874795965cd83bc5fb0d9485a90aa5c7bc7d016cba9e8b84107.

- 2026-09-25T00:56:21+00:00: Recorded command exit 0; command argv SHA-256
  b8aa4d9423c48391fdb37551ba52798ece46a7d1a1aa62d23241d5b58ecdc408.

- 2026-09-25T00:56:46+00:00: Recorded command exit 0; command argv SHA-256
  d9fa98eb37c2a5f5730abda7f8e795d6ee6272c5b08391d589f9a0003668e04a.

- 2026-09-25T00:57:01+00:00: Recorded command exit 0; command argv SHA-256
  c5bbbecf121e9d271a452fb82b5c24a5d2a3fcd8e5429f12e5d56ccc0ed7dec8.

- 2026-09-25T00:57:21+00:00: Recorded command exit 0; command argv SHA-256
  66e26fb6680d408213c6237fa57c597cad20281b82f42afc57ad5d6d9a48fddb.

- 2026-09-25T00:58:14+00:00: Recorded command exit 0; command argv SHA-256
  4217c6f99114ae85cdff40b45d0e30caad4c5f72aa14d0f264d3a64c2d8e8a19.

- 2026-09-25T00:58:51+00:00: Recorded command exit 0; command argv SHA-256
  4217c6f99114ae85cdff40b45d0e30caad4c5f72aa14d0f264d3a64c2d8e8a19.

- 2026-09-25T00:59:11+00:00: Recorded command exit 1; command argv SHA-256
  ef4f054ead02151d61872b693b6e93e55373cf9b15abb03438d03411b2f9b846.

- 2026-09-25T00:59:41+00:00: Independent review attempt recorded exit 1 because the operator
  supplied four mistyped/truncated commit IDs to git verify-commit; the first commit verified before
  those IDs failed. No product or gate issue. Correct commit IDs are now taken directly from git log
  and review is being rerun.

- 2026-09-25T00:59:53+00:00: Recorded command exit 0; command argv SHA-256
  f42bd652a687adb2c854f0a13fcb38de2fe455173a2b3e909446b2c5b8fa8bab.

- 2026-09-25T01:00:15+00:00: Recorded command exit 0; command argv SHA-256
  33cbfdda1832615f6abf63be1cd0c901568f764d7108057579d800d95b30a108.

- 2026-09-25T01:00:43+00:00: Recorded command exit 0; command argv SHA-256
  4f6df6b217998d9d2b4428224c82b80d60852514254b0d14e70acbd6c1456ce5.

- 2026-09-25T01:01:03+00:00: Recorded command exit 8; command argv SHA-256
  e8cb740c48ade1352a2d26719cd68def8b381feb08d97404c33117a3457855b3.

- 2026-09-25T01:01:32+00:00: Independent review passed at exact head: clean tree, diff-check, five
  SSH-signed commits, five matching DCO trailers, privacy scan clean. PR #317 published with base
  cc82333a and exact head ae48046; checks are running, no merge until all required checks pass.

- 2026-09-25T01:01:44+00:00: Recorded command exit 8; command argv SHA-256
  e8cb740c48ade1352a2d26719cd68def8b381feb08d97404c33117a3457855b3.

- 2026-09-25T01:02:09+00:00: Recorded command exit 8; command argv SHA-256
  e8cb740c48ade1352a2d26719cd68def8b381feb08d97404c33117a3457855b3.

- 2026-09-25T01:02:58+00:00: Recorded command exit 8; command argv SHA-256
  e8cb740c48ade1352a2d26719cd68def8b381feb08d97404c33117a3457855b3.

- 2026-09-25T01:03:38+00:00: Recorded command exit 8; command argv SHA-256
  e8cb740c48ade1352a2d26719cd68def8b381feb08d97404c33117a3457855b3.

- 2026-09-25T01:03:56+00:00: Recorded command exit 8; command argv SHA-256
  e8cb740c48ade1352a2d26719cd68def8b381feb08d97404c33117a3457855b3.

- 2026-09-25T01:04:41+00:00: Recorded command exit 8; command argv SHA-256
  e8cb740c48ade1352a2d26719cd68def8b381feb08d97404c33117a3457855b3.

- 2026-09-25T01:05:19+00:00: Recorded command exit 8; command argv SHA-256
  e8cb740c48ade1352a2d26719cd68def8b381feb08d97404c33117a3457855b3.

- 2026-09-25T01:05:37+00:00: Recorded command exit 8; command argv SHA-256
  e8cb740c48ade1352a2d26719cd68def8b381feb08d97404c33117a3457855b3.

- 2026-09-25T01:05:56+00:00: Recorded command exit 0; command argv SHA-256
  b102a9f575a94aa0d93ba796db41110a8580761f8d73aa6d3867fdf2aaf1da70.

- 2026-09-25T01:06:49+00:00: Recorded command exit 8; command argv SHA-256
  e8cb740c48ade1352a2d26719cd68def8b381feb08d97404c33117a3457855b3.

- 2026-09-25T01:07:08+00:00: Recorded command exit 0; command argv SHA-256
  e1bd3d8a696e72ae151425fda18e0d02b5e5f82eb724c4d6dac2a15b7ea9f472.
