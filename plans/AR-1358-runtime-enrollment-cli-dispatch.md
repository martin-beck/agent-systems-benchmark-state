# AR-1358: Runtime enrollment CLI dispatch

## Objective

Consume the merged AR-1357 runtime-attested enrollment record in `asb run` and
`asb sweep`, preserving fail-closed provider selection, offline/replay behavior,
credential privacy, cancellation and teardown.

## Dependencies

Depends on AR-1357. This is the coordinator-created consumer repair for AR-1329;
AR-1329 remains fail-closed until this task is merged and verified.

## Required work

- Load only a bounded, versioned runtime enrollment record from the authenticated
  control/runtime channel; CLI arguments cannot supply target, endpoint, tools,
  lease root, relay root, namespace, token, or credentials.
- Dispatch live `run` and `sweep` through the runtime-owned record ingestion and
  opaque handle path, with one lease/relay/namespace per scheduler attempt.
- Preserve strict replay/offline rejection and `NetworkPolicy::Deny`.
- Add positive and negative CLI tests for valid dispatch, missing/stale/replayed
  records, provider-selection mismatch, cancellation cleanup, alternate egress,
  and secret/path-free public output.

## Acceptance

Focused and full gates, exact-head CI, independent review, signed+DCO commit,
protected merge, and all post-merge workflows pass. AR-1329 may advance only
after exact merge and post-merge evidence is durable.
