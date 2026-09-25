# AR-1366: Runtime-owned dispatch consumer

## Objective

Connect the authenticated control/runtime receipt source from AR-1365 to the
production benchmark dispatch path. The consumer must obtain its request and
receipt through runtime-owned control state and return only an opaque runtime
handle; CLI/config callers must not be able to fabricate provider, endpoint,
credential, target, tool, lease, relay, namespace, or certificate authority.

## Dependencies

Depends explicitly on AR-1362 (durable enrollment), AR-1364 (authenticated
chain materialization), and AR-1365 (bound receipt request/response source).
AR-1360/AR-1361/AR-1363 remain historical blocked tasks; do not resume stale
metadata. AR-1329 remains fail-closed until this consumer is verified.

## Required work

- Identify the existing asb run/sweep dispatch seam and add a private,
  runtime-owned consumer factory that receives only authenticated control
  state and bounded request context.
- Validate provider/generation/nonce, target/tool/lease/relay roots, endpoint
  policy, namespace attestation, and replay/revocation state before dispatch.
- Consume `RuntimeReceiptResponseV1` only after authenticated binding checks;
  return an opaque handle with no secrets, private paths, or authority fields.
- Preserve offline, fail-closed, bounded-command, and network policy behavior;
  reject missing, forged, mismatched, stale, replayed, or CLI-supplied
  authority.
- Add positive, tamper, replay, missing-source, policy, and privacy tests;
  update stable schemas/generated docs where required.

## Acceptance

Focused and full applicable gates pass; the complete diff receives independent
review; commit is SSH-signed with DCO; exact-head hosted checks are green;
protected merge succeeds; and all seven post-merge workflows pass. Do not
advance AR-1329 or expose a public authority constructor before exact evidence
is durable.

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
