# AR-1367: AR-1329 production dispatch integration

## Objective

Complete the production `asb run`/`asb sweep --live-provider` path by consuming
the runtime-owned authenticated bridge from AR-1366 and issuing one opaque live
provider attempt per scheduler admission. The CLI may select a validated
profile but cannot provide endpoint, credential, target, tool, lease, relay,
namespace, or certificate authority.

## Dependencies

Depends explicitly on AR-1366, AR-1340, AR-1339, and AR-1328. AR-1341 is the
namespace-attestation repair associated with AR-1340 and is already complete;
the implementation must preserve its runtime-observed child namespace gate.
This task supersedes stale AR-1329 metadata without mutating AR-1329.

## Required work

- Wire the existing run/sweep live-provider dispatch seam to a runtime-owned
  enrollment/receipt consumer, not caller-supplied authority.
- Resolve only pinned provider policy and concrete allowlisted public targets;
  obtain credentials through the enrolled environment channel without exposing
  bytes or evidence; reject missing, stale, mismatched, revoked, or replayed
  material.
- Reserve `ResourceLease`, construct the pinned `SandboxBackend`, attest the
  runtime-observed child namespace, create the relay, and issue exactly one
  opaque `LiveProviderAttempt` per scheduler attempt.
- Preserve `NetworkPolicy::Deny` at the process boundary, deny direct and
  alternate egress, bound every command and relay, and tear down lease,
  namespace, relay, credential channel, and child on success, cancellation,
  failure, or timeout.
- Add positive and hostile negative run/sweep tests, schema/docs updates where
  needed, and privacy checks proving no credentials, private paths, prompts, or
  authority are returned.

## Acceptance

Focused and full applicable gates, independent review, signed+DCO exact-head
PR, all required hosted checks, protected merge, and all seven post-merge
workflows must pass. Do not release or advance any further AR until the exact
production call path and post-merge evidence are durable.

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
