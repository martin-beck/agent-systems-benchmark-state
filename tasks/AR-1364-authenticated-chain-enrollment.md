---
{
  "branch": "feature/ar-1364-authenticated-chain-enrollment",
  "checkpoint_commit": "47914d8fd49ca5b5132c0734d3739df4502b7853",
  "claim_expires": "",
  "depends_on": [
    "AR-1362"
  ],
  "id": "AR-1364",
  "next_action": "Run full applicable gates, independently review the chain-enrollment boundary, then publish a clean exact-head PR and monitor all required checks.",
  "observed_branch": "feature/ar-1364-authenticated-chain-enrollment",
  "observed_dirty": 0,
  "observed_head": "47914d8fd49ca5b5132c0734d3739df4502b7853",
  "owner": "",
  "plan": "../plans/AR-1364-authenticated-chain-enrollment.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "done",
  "summary": "Materialize authenticated certificate-chain authority for control-owned runtime receipt issuance.",
  "task_revision": 27,
  "title": "Authenticated chain enrollment",
  "updated_at": "2026-09-23T23:53:44+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1364-authenticated-chain-enrollment"
}
---

Successor for blocked AR-1363, explicitly depending on AR-1362. Do not touch
asb-tui or synthesize certificate authority from CLI/config input.

- 2026-09-24T00:00:00+00:00: Created after AR-1363 found the control backend
  has no authenticated certificate-chain material or runtime-owned issuer.

- 2026-09-23T23:30:22+00:00: Promote authenticated certificate-chain enrollment successor after
  AR-1363 found no control-owned chain materialization.

- 2026-09-23T23:30:25+00:00: Claimed by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T23:31:30+00:00: Recorded command exit 0; command argv SHA-256
  060858f3c09d8a7ce03dfae54a20a77cf22bbd921bdbef41e45dd9ebed4ea5fa.

- 2026-09-23T23:31:58+00:00: Recorded command exit 0; command argv SHA-256
  52273bbc70421eaf60328c6cdb72560a92655e0a34ae284ee3a05d326ed12e17.

- 2026-09-23T23:32:12+00:00: Recorded command exit 0; command argv SHA-256
  907b1b1f743859290d1b107a1971b1dbf4bfaf02a4014ca1961d94cfbbf81467.

- 2026-09-23T23:32:26+00:00: Recorded command exit 0; command argv SHA-256
  ad07c34640072cd4977d553ab1dec38416afbfa93b1805db738c19b36a9ca5ab.

- 2026-09-23T23:32:45+00:00: Implemented AuthenticatedChainEnrollmentV1: bounded public identity
  chain, pairing digest and generation binding, strict unknown-field rejection, authority-backed
  issue_chain validation, and positive/negative tests. Focused tests 2/2 pass; cargo fmt pass.
  Signed+DCO product commit is 47914d8.

- 2026-09-23T23:33:08+00:00: Correction: exact signed+DCO product checkpoint is
  47914d8fd49ca5b5132c0734d3739df4502b7853; prior abbreviated checkpoint typo is superseded.

- 2026-09-23T23:33:16+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T23:33:21+00:00: Recorded command exit 0; command argv SHA-256
  d9fa5fa9d6b1edd0744be1b0aa7351347516f8475fbf10364d8f42e7873456ab.

- 2026-09-23T23:33:50+00:00: Recorded command exit 0; command argv SHA-256
  b2f7111306aa7c03c56215bdb77e1811ed87e0363612681320219865a955e4c7.

- 2026-09-23T23:34:36+00:00: Recorded command exit 0; command argv SHA-256
  230d83ebbf8a53eeecd6ce3aee49b142013ffd414b68179a12532ea02a52291d.

- 2026-09-23T23:34:51+00:00: Recorded command exit 0; command argv SHA-256
  075e640f0ebaa1b08851a3f14111c1f1590ec65f305c3912207a79c52049aac9.

- 2026-09-23T23:35:13+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T23:37:13+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T23:38:48+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T23:44:13+00:00: Recorded command exit 0; command argv SHA-256
  e6d1b57291ceb8593afb499ead596be1727f5492f636c90efe7df71b35e92c5c.

- 2026-09-23T23:44:40+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T23:46:45+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T23:48:01+00:00: Recorded command exit 0; command argv SHA-256
  126f3a436a547330141bfa423e31c948e3d8c63693dfb8a02b9cf449360c756c.

- 2026-09-23T23:48:24+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T23:50:29+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T23:52:02+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T23:53:44+00:00: Completed AR-1364: signed+DCO commit
  47914d8fd49ca5b5132c0734d3739df4502b7853 added AuthenticatedChainEnrollmentV1 with bounded public
  identity chains, pairing/generation binding, strict unknown-field rejection, and positive/negative
  tests. PR #268 passed all 12 exact-head checks and merged as
  3a4007be828db04f3b57492e5c5f230199cb8d5a. All seven post-merge workflows passed: 35935060568
  headers, 35935060564 hosted portability, 35935060604 repository quality, 35935060566 emulated
  AArch64, 35935060558 formal after a successful rerun of transient ExecutableFileBusy, 35935060544
  Rust, and 35935060587 fault assurance. Lease cleared.

## Current development and CI qualification boundary

The mandatory development and CI qualification path for this AR is a deterministic
local provider/LLM mock (LiteLLM-compatible where practical), including hostile
negative tests and offline replay where applicable. External/live OpenRouter or
other provider reachability is optional supplementary evidence only; it is never a
completion, dependency-readiness, or CI gate. Production egress policy, credential
non-disclosure, runtime-owned authority, namespace/relay attestation, cancellation
and teardown, and fail-closed denial of unapproved external traffic remain required
contracts. Existing live-provider dependency edges describe production integration
ordering only and must not be used to block local qualification or to claim external
reachability.
