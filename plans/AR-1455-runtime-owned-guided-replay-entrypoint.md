# AR-1455: Runtime-owned guided replay entrypoint

## Objective

Provide the missing runtime-owned provisioning entrypoint required by the
guided ASB command wrapper (AR-1338). The wrapper must ask the central
orchestration service for an opaque local-replay authority and may not build a
SandboxBackend, ResourceLease, relay, namespace, or capability itself.

## Dependencies

Depends on completed AR-1448, AR-1450, and AR-1453. Do not touch asb-tui.

## Required work

Add one bounded CLI/runtime entrypoint that accepts only a validated plan and
cassette identity, asks the central service to provision and execute a local
strict-replay attempt, and returns typed public status. Ensure authority is
opaque, idempotency is journal-backed, frontend disconnect does not cancel a
run, and cancellation/timeout/restart cleanup remains runtime-owned. Reject
missing or stale cassette digests, caller-supplied authority objects, path
escapes, network fallback, and unknown options before effects.

## Acceptance

AR-1338 can call the entrypoint for a guided local replay using deterministic
mock/replay fixtures without live-provider access. Positive and negative CLI,
restart, idempotency, cancellation, teardown, and egress-denial tests pass;
all product and coordination gates, independent review, exact-head CI, and
seven post-merge workflows pass. No credential or host path enters output or
evidence.

## Qualification boundary

Local deterministic replay or LiteLLM-compatible doubles are the required
development and CI path. External provider reachability is optional evidence
and never a dependency or gate.
