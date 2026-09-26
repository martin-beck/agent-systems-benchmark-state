---
{
  "branch": "feature/ar-1332-record-live-replay-offline",
  "checkpoint_commit": "97d9bbc3b6a9e0f793ac6a5a4ba3103e85f5e4a7",
  "claim_expires": "2026-09-26T19:05:31+00:00",
  "depends_on": [
    "AR-1331"
  ],
  "id": "AR-1332",
  "next_action": "Open reviewed PR from exact signed head, then run exact-head CI and protected-main publication gates.",
  "observed_branch": "feature/ar-1332-record-live-replay-offline",
  "observed_dirty": 0,
  "observed_head": "97d9bbc3b6a9e0f793ac6a5a4ba3103e85f5e4a7",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1332.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add the record-live then replay-offline end-to-end CLI workflow.",
  "task_revision": 55,
  "title": "Record-live to replay-offline workflow",
  "updated_at": "2026-09-26T17:05:31+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1332-record-live-replay-offline"
}
---

Live capture (AR-1330) and the runtime launch authority (AR-1331) exist in
isolation, but the user-visible workflow that connects them is missing: record a
real run under an explicit opt-in, seal the cassettes, then replay the exact
evidence strictly offline. This AR defines and documents that
`record-live -> replay-offline` workflow in the CLI: a bounded live record mode
that persists intent before provider contact and seals per-tuple cassettes, and
a replay mode that accepts only runtime-issued authority and never contacts a
provider. Replay results are recorded against the sealed cassette digests with
no fallback, and interrupted or duplicated records fail closed.

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

- 2026-09-26T16:46:13+00:00: AR-1331 is durably done; promote the ASB-only record-live to
  replay-offline workflow. Qualification must use local/mock or strict replay; external provider
  access remains optional.

- 2026-09-26T16:47:28+00:00: Claimed by ar1332-record-replay-luna56.

- 2026-09-26T16:48:03+00:00: Recorded command exit 0; command argv SHA-256
  86373cbbaffb66da63f9e5e10e308b45d7f25c83c016f6830b3db0bab7042f89.

- 2026-09-26T16:48:23+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-26T16:48:37+00:00: Recorded command exit 0; command argv SHA-256
  b04e51d6a8a1cd1d991d96d1b0eeb7f5236f1056ccb95c8f404b26c181dc4797.

- 2026-09-26T16:48:52+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-26T16:49:06+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-26T16:50:47+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-26T16:51:09+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-26T16:51:47+00:00: Recorded command exit 0; command argv SHA-256
  e215d0db01020814fc50d2807f060b6e361dc519077025571a93a090ac1d6613.

- 2026-09-26T16:52:19+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-26T16:52:38+00:00: Recorded command exit 101; command argv SHA-256
  e215d0db01020814fc50d2807f060b6e361dc519077025571a93a090ac1d6613.

- 2026-09-26T16:53:18+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-26T16:53:35+00:00: Recorded command exit 0; command argv SHA-256
  e215d0db01020814fc50d2807f060b6e361dc519077025571a93a090ac1d6613.

- 2026-09-26T16:54:38+00:00: Recorded command exit 101; command argv SHA-256
  5e3d7817f0afba28e5aaab104bd49513090d0424642bd97634a5373b02bde924.

- 2026-09-26T16:55:04+00:00: Recorded command exit 101; command argv SHA-256
  5e3d7817f0afba28e5aaab104bd49513090d0424642bd97634a5373b02bde924.

- 2026-09-26T16:55:32+00:00: Recorded command exit 0; command argv SHA-256
  5e3d7817f0afba28e5aaab104bd49513090d0424642bd97634a5373b02bde924.

- 2026-09-26T16:55:48+00:00: Recorded command exit 0; command argv SHA-256
  e215d0db01020814fc50d2807f060b6e361dc519077025571a93a090ac1d6613.

- 2026-09-26T16:56:32+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-26T16:56:55+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-26T16:57:12+00:00: Recorded command exit 0; command argv SHA-256
  65b187fffb8d15b430c4a6abb6c9b57647249f140e8ef8f05b2c79466df6e418.

- 2026-09-26T16:57:28+00:00: Recorded command exit 0; command argv SHA-256
  e215d0db01020814fc50d2807f060b6e361dc519077025571a93a090ac1d6613.

- 2026-09-26T16:57:43+00:00: Recorded command exit 0; command argv SHA-256
  e215d0db01020814fc50d2807f060b6e361dc519077025571a93a090ac1d6613.

- 2026-09-26T16:58:12+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-26T16:58:33+00:00: Recorded command exit 0; command argv SHA-256
  8c4fd32c78513c384f0fb18ce1df2a63c64483f19fbc845bb2cbb9b9778d0fb6.

- 2026-09-26T16:58:48+00:00: Recorded command exit 0; command argv SHA-256
  f818c61097624cacd337badb2e88b0ba3c169b5f1e1c98b1f790f62a6e538648.

- 2026-09-26T16:59:09+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-26T16:59:23+00:00: Recorded command exit 0; command argv SHA-256
  20b5944c441fe68a8c2c99aba8a407bba3529fc6e58cc74c926e93b210d3f15b.

- 2026-09-26T16:59:39+00:00: Recorded command exit 0; command argv SHA-256
  a6a5efdb86c85189ff80d01586394470aa8cf22450cb65e795bbb78f2ea3af7e.

- 2026-09-26T16:59:55+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-26T16:59:58+00:00: Implementation commit 705f0c8 is SSH-signed with matching DCO. Added
  explicit record-live --local-mock --confirm-record and authority-bound replay-offline aliases,
  hostile tests, docs, and refreshed CLI provenance. Focused tests, guide_examples, workflow
  transcript/provenance, workspace tests, fmt, and clippy passed. Await independent review and
  exact-head CI.

- 2026-09-26T17:01:05+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-26T17:01:22+00:00: Recorded command exit 0; command argv SHA-256
  65b187fffb8d15b430c4a6abb6c9b57647249f140e8ef8f05b2c79466df6e418.

- 2026-09-26T17:01:38+00:00: Recorded command exit 0; command argv SHA-256
  3e048d0a21aa96cdd2b52175d07dc10803815f7726129670096f8775ba3c08e9.

- 2026-09-26T17:01:53+00:00: Recorded command exit 0; command argv SHA-256
  83b909925984aadeeb44f46ac4ff96e83640a26e446249d2e9c167bd94db8b0a.

- 2026-09-26T17:02:19+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-26T17:02:22+00:00: Independent review gates addressed: local/mock qualification is
  explicitly documented as the required boundary; production provider capture is separately
  supervised/deferred. record-live requires both --local-mock and --confirm-record; replay-offline
  consumes the existing one-shot runtime authority, cassette digest binding, network-denied strict
  service, and no-fallback error path. Duplicate fallback wording removed. Follow-up signed+DCO
  commit 97d9bbc updates help/docs/provenance. Workflow transcript/provenance, focused tests, fmt
  and clippy remain green.

- 2026-09-26T17:02:34+00:00: Recorded command exit 0; command argv SHA-256
  dd884500c3c195c42a6d56185b2dafee6c380d949d06a7020b07ed5b49529c35.

- 2026-09-26T17:02:58+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-26T17:03:16+00:00: Recorded command exit 0; command argv SHA-256
  802d15f50903691d692b95eb46d0745af34c69fc82aafca8c6ee307b412d71d1.

- 2026-09-26T17:03:33+00:00: Recorded command exit 0; command argv SHA-256
  d7cc2db8c6cffa19a9b0bb23e79987a3a6d13bb553cda1f29de43addf8b6c9b5.

- 2026-09-26T17:03:47+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-26T17:04:14+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-26T17:04:30+00:00: Recorded command exit 0; command argv SHA-256
  802d15f50903691d692b95eb46d0745af34c69fc82aafca8c6ee307b412d71d1.

- 2026-09-26T17:04:46+00:00: Recorded command exit 0; command argv SHA-256
  d7cc2db8c6cffa19a9b0bb23e79987a3a6d13bb553cda1f29de43addf8b6c9b5.

- 2026-09-26T17:05:05+00:00: Recorded command exit 0; command argv SHA-256
  938500e2b3d4d91a8e10791c4c98e26ace6a65de04b7881e534898b8580e59a8.

- 2026-09-26T17:05:31+00:00: Heartbeat by ar1332-record-replay-luna56.
