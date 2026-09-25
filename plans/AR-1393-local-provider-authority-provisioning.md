# AR-1393: Runtime-owned local-provider authority provisioning

## Objective

Provide a bounded, runtime-owned authority provisioning contract for the
credential-free deterministic local provider used by development and CI. The
contract must persist only digest-bound public enrollment metadata while
materializing private lease/relay roots, pinned mock tool identity, loopback
allowlist, namespace/teardown generation, and opaque credential capability in
runtime memory. This gives AR-1390 a real source without requiring an external
OpenRouter/backend connection.

## Dependencies

AR-1388, AR-1385, AR-1373, AR-1366, AR-1341, AR-1342, AR-1339, and AR-1340 are
done. AR-1391 and AR-1392 are blocked audits proving that external-provider
authority is absent; this AR intentionally scopes the safe local deterministic
provider required by the development policy. External provider authority must
remain optional evidence and must never be synthesized from public metadata.

## Acceptance

- A runtime/control-owned provisioning operation installs a fixed, digest-pinned
  loopback provider profile (LiteLLM-compatible mock), private ephemeral lease
  and relay roots, tool identity, namespace generation, teardown generation,
  and opaque in-memory capability; CLI/config/environment cannot supply them.
- Public catalog and receipts contain only bounded digests and identities;
  private paths, credentials, prompts, transcripts, endpoints, and mock output
  never enter evidence or durable state.
- Provisioning validates generation, replay, expiry, revocation, root
  ownership, loopback-only target, tool digest, and teardown fencing; malformed
  or copied records fail closed before launch.
- Positive, tamper, replay, cancellation, cleanup, and privacy tests run
  entirely offline against the local deterministic mock. No external
  OpenRouter/backend connection is required for AR completion or CI.
- Signed+DCO implementation, full gates, independent review, exact-head CI,
  seven post-merge workflows, and durable evidence enable AR-1390 to wire the
  normal run/sweep path without caller authority injection.

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
