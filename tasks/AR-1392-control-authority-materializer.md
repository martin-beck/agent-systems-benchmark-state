---
{
  "branch": "feature/ar-1392-control-authority-materializer",
  "checkpoint_commit": "78ab92bdb87645ac5567fb3341b1b0b73dba5029",
  "claim_expires": "2026-09-29T14:29:53+00:00",
  "depends_on": [
    "AR-1388",
    "AR-1385",
    "AR-1373",
    "AR-1366",
    "AR-1341",
    "AR-1342",
    "AR-1339",
    "AR-1340"
  ],
  "id": "AR-1392",
  "next_action": "Resolve unrelated Rust CI failure or obtain coordinator-approved retry; do not merge PR #339 until every exact-head check is green.",
  "observed_branch": "feature/ar-1392-control-authority-materializer",
  "observed_dirty": 0,
  "observed_head": "0ea9671224ff6b51fbe0a3be4ac9817c4526356c",
  "owner": "ar1392-topology-repair-luna56",
  "plan": "../plans/AR-1392-control-authority-materializer.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Resolve private live authority from authenticated control enrollment without caller injection.",
  "task_revision": 136,
  "title": "Control-owned private authority materializer",
  "updated_at": "2026-09-29T12:29:53+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1392-control-authority-materializer"
}
---

This successor owns the control-side authority gap found by AR-1391. It must
not touch asb-tui, expose secrets, synthesize authority, or require external
provider connectivity in development or CI.

- 2026-09-24T07:45:20+00:00: Runtime authority dependencies verified; AR-1391 audit identifies
  missing private control authority materialization.

- 2026-09-24T07:46:08+00:00: Claimed by codex-asb-ar1329-repair-luna56.

- 2026-09-24T07:46:33+00:00: Protected-main audit confirms deeper missing primitive remains: control
  catalog RuntimeAuthorityRecord stores only digest metadata (credential reference, tool/lease/relay
  digests, target/generation), with no protected local authority resolver or durable private
  roots/tools/policy/allowlist/namespace/launch-token/teardown issuer. Runtime APIs require
  caller-supplied private inputs and CLI cannot access crate-private bootstrap APIs. No safe
  control-owned materializer can be implemented without inventing authority or accepting caller
  injection. Worktree clean at 10bffbf015bd7ca78d8c0d18f04cf0190195e933; no PR published.

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

- 2026-09-26T22:50:12+00:00: AR-1371 is durably done and provides the owner-checked authenticated
  authority injection; resume AR-1392 for the remaining control-side materializer/receipt-source
  integration.

- 2026-09-26T22:50:14+00:00: Claimed by coordinator-ar1392-control-materializer.

- 2026-09-26T22:50:32+00:00: Heartbeat by coordinator-ar1392-control-materializer.

- 2026-09-26T22:50:40+00:00: Recorded command exit 0; command argv SHA-256
  181ae5cc638894561812f1d985b5943f2577e6351ab029560b670efe555bc60c.

- 2026-09-26T22:51:01+00:00: Recorded command exit 0; command argv SHA-256
  5c3966008ce108193ec4d3c3d9464e1fc1f348fc7ed46a1b32c0f7143d79fe06.

- 2026-09-26T22:52:14+00:00: Heartbeat by coordinator-ar1392-control-materializer.

- 2026-09-26T22:52:31+00:00: Recorded command exit 2; command argv SHA-256
  578d3326f108f75f304d9be60d8b7e9c1f4159cf40d30f2b762f679f2b77ff16.

- 2026-09-26T22:52:46+00:00: Recorded command exit 0; command argv SHA-256
  0ab45c2f43d6e96bb283c746c826d4b7a7cdc7b2dad278743bb9f6baa020abe0.

- 2026-09-26T22:53:05+00:00: Recorded command exit 0; command argv SHA-256
  bbffd26e88e50797d59654edbf9141196ff37c63c14854f27cc07eb7ef63c9ef.

- 2026-09-26T22:53:23+00:00: Recorded command exit 0; command argv SHA-256
  6b5938adfc3ba1d1eb656708cfb8d5ef87598f88f591d5482c4f90552bc63ca9.

- 2026-09-26T22:53:46+00:00: Recorded command exit 0; command argv SHA-256
  9d66dfae65ea04a9cc0d503545bae7fb35c915a13008564ba140215771e44e16.

- 2026-09-26T22:54:05+00:00: Recorded command exit 0; command argv SHA-256
  d19707c9302cce6bd32583887e5bb8d19fbc7cea92bc74389d3b721a9e538a8b.

- 2026-09-26T22:54:31+00:00: Recorded command exit 0; command argv SHA-256
  a2a3a8c30ea5191befa1d7554b4407cd05f03ff28a69ed3b0b13b5e39e87bd69.

- 2026-09-26T22:55:05+00:00: Recorded command exit 101; command argv SHA-256
  ab543b6ebc99399495da7e082d78069ed76bcea1b63491bea5dac280976addf0.

- 2026-09-26T22:55:41+00:00: Recorded command exit 0; command argv SHA-256
  3f9289827e42106b2489ff602d49e86ddd8813a7434cb53818900d5396431ad0.

- 2026-09-26T22:56:01+00:00: Recorded command exit 0; command argv SHA-256
  330db0e3f57c8c06d99a723a9b13365cdc2ed3944a4901d8726ce15b0eabef8a.

- 2026-09-26T22:56:15+00:00: Recorded command exit 0; command argv SHA-256
  1270d294c2b444ffa41c1e91e4b42e2e60c39c72663081fbf395aac0f84b06ab.

- 2026-09-26T22:56:32+00:00: Recorded command exit 0; command argv SHA-256
  0864717eb584b50b0a09714281b4a0c34183f903b16e3b694fde25a0c762a98d.

- 2026-09-26T22:57:04+00:00: Recorded command exit 0; command argv SHA-256
  3f9289827e42106b2489ff602d49e86ddd8813a7434cb53818900d5396431ad0.

- 2026-09-26T22:57:32+00:00: Recorded command exit 101; command argv SHA-256
  21e8bf2294f08efad33e7ee364162533bcf16feaa7716e5e5afa988aef3bf049.

- 2026-09-26T22:57:49+00:00: Recorded command exit 0; command argv SHA-256
  21e8bf2294f08efad33e7ee364162533bcf16feaa7716e5e5afa988aef3bf049.

- 2026-09-26T22:58:05+00:00: Recorded command exit 0; command argv SHA-256
  4c6912831c082658fe5b5cf82046bbf45a9696347187a3e94cbb5c140e206bfd.

- 2026-09-26T22:58:19+00:00: Recorded command exit 1; command argv SHA-256
  5529860e81b3eae421d490f3680d522ddfa0e8a6afcc4a90c451bfea06efa2fa.

- 2026-09-26T22:58:39+00:00: Recorded command exit 0; command argv SHA-256
  0c1349d31ed7a00d8576f27ec9984489b5e90b9781e118ef1ea99cc17d48c701.

- 2026-09-26T22:59:00+00:00: Recorded command exit 101; command argv SHA-256
  534c8af3bc41c2968ce178e678b330272d36ffc40f3472bb58db7acda7aba900.

- 2026-09-26T22:59:17+00:00: Recorded command exit 0; command argv SHA-256
  534c8af3bc41c2968ce178e678b330272d36ffc40f3472bb58db7acda7aba900.

- 2026-09-26T22:59:36+00:00: Recorded command exit 0; command argv SHA-256
  fe71279d7aa7d9727a04ad83f8cb1d5a7bd91860f29280f9603c3e71162d667c.

- 2026-09-26T22:59:54+00:00: Recorded command exit 0; command argv SHA-256
  a13065c6c66fd43a97949173a188fc7be621cb253a7583afbf045be2d8976493.

- 2026-09-26T23:00:15+00:00: Recorded command exit 0; command argv SHA-256
  f66a647c33c5e255449936a05dc6231203f1a55d067cb82e4e183742a0e03fef.

- 2026-09-26T23:00:29+00:00: Recorded command exit 0; command argv SHA-256
  7655b26f3ca818ad7f4aecdede21e84fcc727c9f2d820ef89be499147034a13b.

- 2026-09-26T23:00:50+00:00: Recorded command exit 0; command argv SHA-256
  bbffd26e88e50797d59654edbf9141196ff37c63c14854f27cc07eb7ef63c9ef.

- 2026-09-26T23:01:21+00:00: Implemented control-owned receipt materializer over AR-1371: every
  RuntimeReceipt revalidates active auth status, endpoint digest, credential reference, and
  generation before issuing; revoked/rotated enrollment fails closed. Added hostile local test
  covering receipt issuance then revocation. Focused authority/receipt tests, 103 asb-cli + 66
  asb-control library tests (successful rerun after transient state-root ownership race), cargo fmt
  --all --check, and clippy -D warnings passed. Initial cargo fmt invocation failed with cargo
  'Failed to find targets' because --all was omitted; corrected command passed. Independent diff
  review: one-file scoped change, no caller-provided authority, no secrets/asb-tui/live provider.
  Signed+DCO commit 739b67d9888e8aced90a13cab79fb67291b297de; worktree clean.

- 2026-09-26T23:01:31+00:00: Recorded command exit 0; command argv SHA-256
  6451f045bd9829abc6348f8b68c81713b1aabe9b49756c3ed9dc0d58f35acf78.

- 2026-09-26T23:01:46+00:00: Recorded command exit 0; command argv SHA-256
  75666d308f0944d58bb3086bcca87c743bf5a16d6af4d88ffefe4a81d0f28008.

- 2026-09-26T23:02:07+00:00: Recorded command exit 1; command argv SHA-256
  f5d3278bd770d3781e98e55c9216125a9511b118ca9d31a0c781a127a57fddee.

- 2026-09-26T23:02:44+00:00: Recorded command exit 0; command argv SHA-256
  39d7bf24a637c2d98c79c0adc029468e33bea0ae0bad9d50c3a5a3ad0c4ac7d4.

- 2026-09-26T23:03:05+00:00: Recorded command exit 0; command argv SHA-256
  6e1469bfd3603f64c6d7a647a1775177c983aad23d3b75fa73f0674fb2f7ddb4.

- 2026-09-26T23:03:20+00:00: Recorded command exit 1; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:03:41+00:00: Recorded command exit 0; command argv SHA-256
  fd004b4df6e65740c1a1b4db63326c768e7918511de757621b27f4b005e8d0a7.

- 2026-09-26T23:03:56+00:00: Recorded command exit 0; command argv SHA-256
  9a67bd5cfd19b8e545d4cc3914a48b8be6cede8d8f09176bb34e06eda7d0c3a3.

- 2026-09-26T23:04:17+00:00: Recorded command exit 0; command argv SHA-256
  9511a8c0fcc195d879e06c697a730dfe365555c1995661e29b3872764413f455.

- 2026-09-26T23:04:32+00:00: Recorded command exit 0; command argv SHA-256
  807e76a0f7df3a18f3274825ee08019d73e50feb4bf0da1dee362070488e931c.

- 2026-09-26T23:04:53+00:00: Recorded command exit 0; command argv SHA-256
  bbffd26e88e50797d59654edbf9141196ff37c63c14854f27cc07eb7ef63c9ef.

- 2026-09-26T23:05:09+00:00: Recorded command exit 0; command argv SHA-256
  7cd50436b7d19267cfdb4b0fbb58465253bde870718f9a0ff962fdc67affa551.

- 2026-09-26T23:05:39+00:00: Publication repair: PR #339 checks correctly rejected the prior topic
  because it was behind protected main and hosted source identity was not immutable. Fetched
  origin/main and rebased the single scoped signed+DCO change; new exact head
  78ab92bdb87645ac5567fb3341b1b0b73dba5029, based on protected merge 01b70e8. Diff remains one file,
  45 insertions/8 deletions; worktree clean; force-with-lease updated remote branch. The original
  platform source-identity failure is an integrity gate being rechecked on the rebased exact head,
  not bypassed.

- 2026-09-26T23:05:47+00:00: Recorded command exit 0; command argv SHA-256
  18b0117fd34663839eb1c200771ba236a438f304eac511ad276cb645d34de064.

- 2026-09-26T23:06:03+00:00: Recorded command exit 8; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:06:56+00:00: Recorded command exit 8; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:07:18+00:00: Recorded command exit 8; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:07:37+00:00: Recorded command exit 8; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:07:56+00:00: Heartbeat by coordinator-ar1392-control-materializer.

- 2026-09-26T23:08:02+00:00: Recorded command exit 8; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:08:21+00:00: Recorded command exit 0; command argv SHA-256
  fb02fb0ab06b47544c07818bf1dc49debc8d63e66062b6d9e23f505b775e2167.

- 2026-09-26T23:08:41+00:00: Recorded command exit 8; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:09:00+00:00: Recorded command exit 8; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:09:20+00:00: Heartbeat by coordinator-ar1392-control-materializer.

- 2026-09-26T23:09:24+00:00: Recorded command exit 0; command argv SHA-256
  26d46f6fe71293305ef40ecc10bce23a87d8a31a9fd95b10043428bb179f4d3c.

- 2026-09-26T23:09:42+00:00: Recorded command exit 1; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:10:02+00:00: Recorded command exit 0; command argv SHA-256
  2665a5bcfe9cbcc4bb3ddc2f2f1bcd90f83d70613fabea0e3edc87ea83b16d9b.

- 2026-09-26T23:10:32+00:00: Exact-head CI classification: Rust workflow 36278328681 failed with
  112/113 tests passed; production_backend_runs_without_frontend_and_recovers_idempotency hit the
  known concurrent state-root ownership race (control state root is already owned) before assertion.
  No changed-file path implicated. Focused local reproduction had passed; rerunning only failed
  workflow against unchanged exact head 78ab92b.

- 2026-09-26T23:10:41+00:00: Recorded command exit 0; command argv SHA-256
  603b3156771a6019000b9188b6d87d7b97a486296d9e3d228121b844763b2628.

- 2026-09-26T23:11:04+00:00: Recorded command exit 8; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:11:22+00:00: Recorded command timeout; classification=SUBPROCESS_TIMEOUT;
  deadline=300.0s; command argv SHA-256
  af2446f2c21ffd97e13e97a46a0bda0c386a59f0885388acd2715892cfc6a434.

- 2026-09-26T23:11:40+00:00: Recorded command exit 8; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:12:00+00:00: Recorded command exit 8; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:12:18+00:00: Recorded command exit 8; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:12:38+00:00: Recorded command exit 0; command argv SHA-256
  cff08cc5e3fecdde8b04c1fd2a6fdf69d9c0f087e1cb24699f828435bcbdf1d3.

- 2026-09-26T23:12:56+00:00: Recorded command exit 8; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:13:15+00:00: Recorded command exit 0; command argv SHA-256
  cff08cc5e3fecdde8b04c1fd2a6fdf69d9c0f087e1cb24699f828435bcbdf1d3.

- 2026-09-26T23:13:34+00:00: Heartbeat by coordinator-ar1392-control-materializer.

- 2026-09-26T23:13:38+00:00: Recorded command exit 8; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:13:57+00:00: Recorded command exit 8; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:14:19+00:00: Recorded command exit 0; command argv SHA-256
  cff08cc5e3fecdde8b04c1fd2a6fdf69d9c0f087e1cb24699f828435bcbdf1d3.

- 2026-09-26T23:14:38+00:00: Recorded command exit 8; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:14:58+00:00: Recorded command exit 0; command argv SHA-256
  cff08cc5e3fecdde8b04c1fd2a6fdf69d9c0f087e1cb24699f828435bcbdf1d3.

- 2026-09-26T23:15:18+00:00: Recorded command exit 1; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:15:48+00:00: Recorded command exit 0; command argv SHA-256
  2665a5bcfe9cbcc4bb3ddc2f2f1bcd90f83d70613fabea0e3edc87ea83b16d9b.

- 2026-09-26T23:16:27+00:00: Recorded command exit 0; command argv SHA-256
  a52c2db125ac76bf7a79fbe290b51e90b09416e54026c136aed69ae059d834da.

- 2026-09-26T23:16:59+00:00: Rust rerun 36278328681 failed again, now in unrelated asb-metrics
  kernel::tests::missing_malformed_and_unsafe_configuration_fail_closed: expected MalformedEvidence,
  observed ProbeRejected. This is outside the one-file AR-1392 diff. Focused local reproduction
  through handoffctl passed 1/1, indicating CI/environment-sensitive failure; no product change
  made. All other PR checks are green at exact head 78ab92b (AArch64, hosted, faults, formal,
  repository quality, Huawei, AWQ). PR #339 remains unmergeable pending a clean exact-head Rust
  result; do not weaken gates.

- 2026-09-26T23:17:10+00:00: Recorded command exit 0; command argv SHA-256
  c73769d24c5bb1fb97e794fc4d47477a4bbc64c6049dbf8b418bb9255609eab7.

- 2026-09-26T23:17:34+00:00: Heartbeat by coordinator-ar1392-control-materializer.

- 2026-09-26T23:18:16+00:00: Heartbeat by coordinator-ar1392-control-materializer.

- 2026-09-26T23:18:19+00:00: Recorded command exit 0; command argv SHA-256
  603b3156771a6019000b9188b6d87d7b97a486296d9e3d228121b844763b2628.

- 2026-09-26T23:18:41+00:00: Recorded command exit 8; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:19:02+00:00: Recorded command exit 0; command argv SHA-256
  cff08cc5e3fecdde8b04c1fd2a6fdf69d9c0f087e1cb24699f828435bcbdf1d3.

- 2026-09-26T23:19:23+00:00: Recorded command exit 8; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:19:44+00:00: Recorded command exit 0; command argv SHA-256
  cff08cc5e3fecdde8b04c1fd2a6fdf69d9c0f087e1cb24699f828435bcbdf1d3.

- 2026-09-26T23:20:04+00:00: Recorded command exit 8; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:20:35+00:00: Recorded command exit 0; command argv SHA-256
  cff08cc5e3fecdde8b04c1fd2a6fdf69d9c0f087e1cb24699f828435bcbdf1d3.

- 2026-09-26T23:20:55+00:00: Recorded command exit 8; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:21:14+00:00: Recorded command exit 0; command argv SHA-256
  cff08cc5e3fecdde8b04c1fd2a6fdf69d9c0f087e1cb24699f828435bcbdf1d3.

- 2026-09-26T23:21:40+00:00: Recorded command exit 8; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:22:02+00:00: Recorded command exit 0; command argv SHA-256
  cff08cc5e3fecdde8b04c1fd2a6fdf69d9c0f087e1cb24699f828435bcbdf1d3.

- 2026-09-26T23:22:24+00:00: Recorded command exit 8; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:22:44+00:00: Recorded command exit 0; command argv SHA-256
  cff08cc5e3fecdde8b04c1fd2a6fdf69d9c0f087e1cb24699f828435bcbdf1d3.

- 2026-09-26T23:23:14+00:00: Recorded command exit 0; command argv SHA-256
  cff08cc5e3fecdde8b04c1fd2a6fdf69d9c0f087e1cb24699f828435bcbdf1d3.

- 2026-09-26T23:23:34+00:00: Recorded command exit 8; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:23:55+00:00: Recorded command exit 0; command argv SHA-256
  cff08cc5e3fecdde8b04c1fd2a6fdf69d9c0f087e1cb24699f828435bcbdf1d3.

- 2026-09-26T23:24:20+00:00: Recorded command exit 0; command argv SHA-256
  cff08cc5e3fecdde8b04c1fd2a6fdf69d9c0f087e1cb24699f828435bcbdf1d3.

- 2026-09-26T23:24:49+00:00: Recorded command exit 0; command argv SHA-256
  cff08cc5e3fecdde8b04c1fd2a6fdf69d9c0f087e1cb24699f828435bcbdf1d3.

- 2026-09-26T23:25:10+00:00: Recorded command exit 8; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:25:35+00:00: Recorded command exit 0; command argv SHA-256
  cff08cc5e3fecdde8b04c1fd2a6fdf69d9c0f087e1cb24699f828435bcbdf1d3.

- 2026-09-26T23:25:56+00:00: Recorded command exit 0; command argv SHA-256
  cff08cc5e3fecdde8b04c1fd2a6fdf69d9c0f087e1cb24699f828435bcbdf1d3.

- 2026-09-26T23:26:18+00:00: Recorded command exit 0; command argv SHA-256
  134217ead7e872f78fd674a12114afce4e09d8d7721930072950f54e61d6384d.

- 2026-09-26T23:26:33+00:00: Recorded command exit 0; command argv SHA-256
  7bd3966f99b8510d63e1ac1116c37a27bb3f659576f01f0be9724caa57f17abd.

- 2026-09-26T23:26:53+00:00: Recorded command exit 0; command argv SHA-256
  8c38bdf34db34415a6d1afc385ef7eb30abcce6ae5759accce036704cab17d3d.

- 2026-09-26T23:27:12+00:00: Recorded command exit 0; command argv SHA-256
  20bb8f37416bbc757a6789e1b268d8eaf9cd1a501db7d5d240919fcf4b4e48a0.

- 2026-09-26T23:27:32+00:00: Recorded command exit 0; command argv SHA-256
  49572412bbbe30c402dca1457996ea8cd519499d1a26f601ef5714d48548ca46.

- 2026-09-26T23:27:51+00:00: Recorded command exit 0; command argv SHA-256
  fede5ab15daccf3e7ee8bb7ef4cfdcec27bdef0540cd6c0a0a0a5c956c65672f.

- 2026-09-26T23:28:19+00:00: Recorded command exit 0; command argv SHA-256
  49572412bbbe30c402dca1457996ea8cd519499d1a26f601ef5714d48548ca46.

- 2026-09-26T23:28:43+00:00: Heartbeat by coordinator-ar1392-control-materializer.

- 2026-09-26T23:28:50+00:00: Recorded command exit 0; command argv SHA-256
  49572412bbbe30c402dca1457996ea8cd519499d1a26f601ef5714d48548ca46.

- 2026-09-26T23:29:09+00:00: Recorded command exit 0; command argv SHA-256
  49572412bbbe30c402dca1457996ea8cd519499d1a26f601ef5714d48548ca46.

- 2026-09-26T23:29:28+00:00: Recorded command exit 0; command argv SHA-256
  49572412bbbe30c402dca1457996ea8cd519499d1a26f601ef5714d48548ca46.

- 2026-09-26T23:30:03+00:00: Terminal post-merge evidence: merge
  3cd6a5a84493842e402dff55e1c2c266f2454752 is single-parent; repository quality workflow 36279474851
  failed protected-main policy with 'merge topology or first parent differs'. This is immutable
  merge topology, not a product/test failure. PR exact head 78ab92b and all 12 PR checks were green;
  post-merge hosted, fault, Huawei, and other workflows are green or still completing. AR-1392 is
  blocked/ownerless pending a separate topology-repair successor; next action is create that
  successor using a non-squash protected-main merge topology and rerun all seven workflows. No code
  or unrelated metrics changes.

- 2026-09-29T12:18:00+00:00: Repair only the protected-main merge-topology policy failure for PR
  #339; preserve green product checks and do not change authority-materializer behavior.

- 2026-09-29T12:18:03+00:00: Claimed by ar1392-topology-repair-luna56.

- 2026-09-29T12:19:38+00:00: Recorded command exit 0; command argv SHA-256
  570dabf9edffd4125d21ef78768dd7a405e00bd4b62eb797a5ad1737825b024f.

- 2026-09-29T12:20:07+00:00: Recorded command exit 0; command argv SHA-256
  2e822c8b2d4b1664a0a8b6b01e63d29e74ceef5e364baa59ab28ead34ddc926d.

- 2026-09-29T12:21:13+00:00: Recorded command exit 0; command argv SHA-256
  8ecf2d13e7205660984e0f7b6c72f26dd5c4c8a9886f8af2253ef4741714a102.

- 2026-09-29T12:21:35+00:00: Recorded command exit 0; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-09-29T12:22:00+00:00: Recorded command exit 0; command argv SHA-256
  0dab39724d94444f6cbfc798426880079e9d8dd4c0fe3b0a57176f433ac8b861.

- 2026-09-29T12:22:31+00:00: Recorded command exit 0; command argv SHA-256
  11a920b74edb07b2a63dd89ae8c66aa5bc4577813cacf63f3b687fd3b41f1345.

- 2026-09-29T12:23:05+00:00: Recorded command exit 0; command argv SHA-256
  3a5b5704ff2ae692c693fb95667249b4d4fe16df735e45db1fb48e11a6b2ec50.

- 2026-09-29T12:29:53+00:00: Heartbeat by ar1392-topology-repair-luna56.
