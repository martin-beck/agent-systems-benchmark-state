# AR-1357: Runtime-attested enrollment record transport

## Objective

Implement the bounded, versioned transport that carries a control-issued enrollment record into the runtime and yields only an opaque live-provider handle. The CLI must never choose provider authority, target, tool pins, lease roots, relay roots, namespace identities, credentials, or launch tokens.

## Dependencies

Depends on AR-1356. It supersedes the incomplete AR-1355 seam; AR-1329 remains fail-closed until this transport is merged.

## Required work

- Define a versioned, bounded enrollment record owned by the authenticated control/runtime bridge.
- Bind the record to the AR-1356 control attestation, generation, provider endpoint identity, concrete allowlisted target, pinned tool identities, canonical lease/relay roots, and NetworkPolicy::Deny.
- Validate authenticity, freshness, replay/copy resistance, target and tool allowlists, canonical roots, and credential-reference presence inside asb-runtime before minting a handle.
- Keep credential values, private paths, namespace details, and launch authority out of serialized records and public evidence.
- Expose only a runtime-owned ingestion method and opaque LiveProviderRuntimeHandle; no public caller-supplied authority constructors.
- Add positive and negative tests for valid transport, forged/stale/replayed records, target/endpoint/tool/root mismatch, alternate egress, missing credentials, unknown fields, oversized input, and secret/path leakage.
- Add the minimal runtime consumer seam needed for asb run/sweep without weakening offline/replay fail-closed behavior, cancellation, or teardown.

## Acceptance

Focused and full gates pass; signed+DCO commits and exact-head CI pass; merge and all post-merge workflows are green. Independent review confirms the CLI cannot fabricate or inspect authority and public evidence is sanitized.
