---
{
  "branch": "feature/ar-1436-local-guided-cli-wrapper",
  "checkpoint_commit": "4b1213d7e58aa3ed8591ac2d1ac6e9484db86cc6",
  "claim_expires": "2026-09-25T02:43:20+00:00",
  "depends_on": [
    "AR-1435",
    "AR-1328"
  ],
  "id": "AR-1436",
  "next_action": "Rerun full workspace tests and applicable offline gates at 4b1213d; then independent review and exact-head PR.",
  "observed_branch": "feature/ar-1436-local-guided-cli-wrapper",
  "observed_dirty": 0,
  "observed_head": "4b1213d089833a78fa73a3402c16576611415e5f",
  "owner": "codex-asb-ar1436-local-guided-luna56",
  "plan": "../plans/AR-1436-local-guided-cli-wrapper.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add a catalog-driven guided CLI wrapper for deterministic local mock qualification.",
  "task_revision": 22,
  "title": "Local guided CLI wrapper",
  "updated_at": "2026-09-25T00:52:13+00:00",
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
