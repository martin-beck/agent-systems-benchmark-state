# AR-1474: Runtime-owned authority-input resolver

## Objective

Implement the runtime/control-owned persistence and resolver for the concrete
inputs required to materialize authenticated live authority. This is the
missing foundation identified by AR-1470, AR-1391, and AR-1473; it must feed
opaque runtime sources without exposing authority to the CLI or callers.

## Dependencies

AR-1362 provides durable authority enrollment storage; AR-1471 binds
control-owned enrollment to runtime certificate-chain storage; AR-1472 and
AR-1379 provide the authenticated live-dispatch adapter and production CLI
consumer. Do not depend on blocked predecessor records.

## Required work

- Define a versioned, bounded runtime-owned record/resolver for policy and
  allowlist identity, target and tool pins, lease/relay roots, credential
  capability references, namespace, generation, cancellation, and teardown
  authority. Store only public digests/opaque handles in evidence.
- Make the resolver owner-checked, authenticated, generation-fenced,
  revocation-aware, and restart-safe. Reject missing, stale, replayed,
  forged, mismatched, alternate-egress, caller-supplied, or cross-namespace
  inputs before any live attempt is created.
- Provide the narrow constructor consumed by the runtime enrollment source;
  preserve argument-only CLI fail-closed behavior and never synthesize
  authority from environment/configuration.
- Add deterministic local/mock/replay positive and negative tests for
  lifecycle, cancellation, teardown, privacy, egress, and failure ordering.
  Live providers and remote credentials are optional and never completion
  requirements.
- Update public schemas/docs and run focused/full/formal/privacy/platform
  gates. Publish only from a clean signed+DCO exact head, merge after exact
  CI and independent review, then verify all post-merge workflows.

## Boundaries

No asb-tui changes, no provider requirement, no secrets/private paths/raw
transcripts, no synthetic or caller-built authority, no gate weakening, and no
edits to `handoffctl`.
