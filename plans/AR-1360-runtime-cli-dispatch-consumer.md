# AR-1360: Runtime CLI dispatch consumer

## Objective

Connect `asb run` and `asb sweep` to the merged runtime/control enrollment
receipt bridge. The CLI may request an opaque runtime-owned attempt but may not
provide target, endpoint, tool bundle, lease root, relay root, namespace,
credential, or launch-token authority.

## Dependencies

Depends on AR-1359. AR-1329 remains fail-closed until this task is merged and
post-merge verified.

## Required work

- Add a bounded versioned CLI/control request path that obtains an authenticated
  `RuntimeEnrollmentReceiptV1` from the runtime-owned control boundary.
- Consume the receipt through the private runtime bridge and dispatch one
  lease/relay/namespace per scheduler attempt for both `run` and `sweep`.
- Preserve strict provider/catalog matching, replay and freshness rejection,
  offline mode, `NetworkPolicy::Deny`, cancellation teardown, and secret/path-
  free output.
- Add positive and negative tests for missing/stale/replayed/tampered receipts,
  provider mismatch, caller-supplied authority, cancellation cleanup, and
  alternate egress.
- Update generated protocol/schema documentation and keep all new constructors
  runtime/control-owned and non-public to CLI callers.

## Acceptance

Focused and full gates pass locally; SSH-signed DCO commit; exact-head PR with
independent review; all required checks green; protected merge; and all seven
post-merge workflows terminal-success. Record exact evidence before advancing
AR-1329.

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
