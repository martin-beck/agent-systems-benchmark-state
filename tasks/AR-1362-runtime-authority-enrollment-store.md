---
{
  "branch": "feature/ar-1362-runtime-authority-enrollment-store",
  "checkpoint_commit": "7bf91f5e846b5a7af6a1297baf9553c29b401fa9",
  "claim_expires": "",
  "depends_on": [
    "AR-1359"
  ],
  "id": "AR-1362",
  "next_action": "Run independent review, publish exact-head PR from clean signed head 7bf91f5, monitor required CI, repair failures without weakening gates, then merge only green and verify all seven post-merge workflows.",
  "observed_branch": "feature/ar-1362-runtime-authority-enrollment-store",
  "observed_dirty": 0,
  "observed_head": "7bf91f5e846b5a7af6a1297baf9553c29b401fa9",
  "owner": "",
  "plan": "../plans/AR-1362-runtime-authority-enrollment-store.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "done",
  "summary": "Persist authenticated runtime authority enrollment required for receipt issuance without exposing secrets.",
  "task_revision": 24,
  "title": "Runtime authority enrollment store",
  "updated_at": "2026-09-23T23:27:33+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1362-runtime-authority-enrollment-store"
}
---

Successor for blocked AR-1361. Do not touch asb-tui or synthesize provider
authority from CLI/config inputs.

- 2026-09-24T00:00:00+00:00: Created after AR-1361 found the control catalog
  lacks authenticated certificate-chain and runtime-owned target/tool/lease/
  relay authority required to issue a receipt.

- 2026-09-23T23:05:20+00:00: Promote durable runtime authority enrollment successor after AR-1361
  found missing control-owned chain and target/tool/root state.

- 2026-09-23T23:05:23+00:00: Claimed by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T23:06:41+00:00: Recorded command exit 0; command argv SHA-256
  29ede43916064a98acdbde0d2d535f5b65786a0b08295ba9845de85bc001da1a.

- 2026-09-23T23:07:00+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-23T23:07:18+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T23:07:36+00:00: Recorded command exit 0; command argv SHA-256
  907b1b1f743859290d1b107a1971b1dbf4bfaf02a4014ca1961d94cfbbf81467.

- 2026-09-23T23:07:58+00:00: Recorded command exit 0; command argv SHA-256
  d9fa5fa9d6b1edd0744be1b0aa7351347516f8475fbf10364d8f42e7873456ab.

- 2026-09-23T23:08:19+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T23:08:37+00:00: Recorded command exit 0; command argv SHA-256
  b2f7111306aa7c03c56215bdb77e1811ed87e0363612681320219865a955e4c7.

- 2026-09-23T23:09:08+00:00: Bounded implementation complete: added RuntimeAuthorityEnrollmentV1 in
  asb-control with deny-unknown-fields digest-only fields, chain/generation/validity/public-target
  validation, receipt issuance, and positive/negative tests. Focused certificate tests 2/2, full
  asb-control tests 62+26+7+4 plus doc tests passed, workspace clippy -D warnings passed, fmt/diff
  clean. Product commit 7bf91f5 is SSH-signed+DCO and worktree clean.

- 2026-09-23T23:09:16+00:00: Recorded command exit 0; command argv SHA-256
  4ce516914a18a642d02d424723e11c693b46482e27e0a729dc2ec6d96294369f.

- 2026-09-23T23:09:37+00:00: Recorded command exit 0; command argv SHA-256
  d7ca20cc50b664f4ed02a0cd55a957ab4f28604bca378f8f632365808b26394e.

- 2026-09-23T23:10:04+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T23:12:04+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T23:14:24+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T23:19:37+00:00: Recorded command exit 0; command argv SHA-256
  9d597d9ecf6ec569270a7be1b2fde14da2c2d724d80211aa99edb633fcfaa28c.

- 2026-09-23T23:20:06+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T23:22:10+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T23:24:11+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T23:26:19+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T23:27:33+00:00: Completed AR-1362: signed+DCO commit 7bf91f5 added
  RuntimeAuthorityEnrollmentV1 with strict digest-only, deny-unknown-fields,
  chain/generation/validity/public-target validation and positive/negative tests. PR #267 passed all
  12 exact-head checks, merged as e9d4d3d1c6a4d67d0ce0e49fa8eaf696561fe45e. All seven post-merge
  workflows passed: 35933025054 headers, 35933025064 hosted portability, 35933025056 repository
  quality, 35933025015 emulated AArch64, 35933025089 formal, 35933025029 Rust, 35933025074 fault
  assurance. Lease cleared; resume blocked AR-1361/1360 only after this durable evidence.

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
