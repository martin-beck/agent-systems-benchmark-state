---
{
  "branch": "feature/ar-1392-control-authority-materializer",
  "checkpoint_commit": "739b67d9888e8aced90a13cab79fb67291b297de",
  "claim_expires": "2026-09-27T01:52:14+00:00",
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
  "next_action": "Publish signed PR from reviewed exact head; require exact-head CI before merge.",
  "observed_branch": "feature/ar-1392-control-authority-materializer",
  "observed_dirty": 0,
  "observed_head": "739b67d9888e8aced90a13cab79fb67291b297de",
  "owner": "coordinator-ar1392-control-materializer",
  "plan": "../plans/AR-1392-control-authority-materializer.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Resolve private live authority from authenticated control enrollment without caller injection.",
  "task_revision": 41,
  "title": "Control-owned private authority materializer",
  "updated_at": "2026-09-26T23:02:07+00:00",
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
