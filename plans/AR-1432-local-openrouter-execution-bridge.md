# AR-1432: Local OpenRouter execution bridge

## Objective

Close the credential-free OpenRouter user journey with a deterministic,
loopback-only LiteLLM-compatible provider mock. Exercise the existing
runtime-owned live-attempt seam from `asb run` and `asb sweep --use-config`
without synthesizing production authority or contacting OpenRouter.

## Dependencies and boundaries

Dependencies: AR-1327, AR-1328, AR-1341, AR-1342, AR-1385, AR-1388, and
AR-1393. The product must continue to deny live provider execution unless a
runtime-issued opaque attempt is present. CLI/config input must not provide an
endpoint, credential, target, lease, relay, namespace, tool, or certificate
authority. The fixture binds only to loopback, uses a deterministic mock secret
channel, and is never evidence of external-provider support.

## Required work

1. Refresh an isolated product worktree at protected main and audit the current
   `run`/`sweep` dispatch and OpenRouter config path.
2. Add or repair the local mock-only runtime enrollment/attempt fixture at the
   existing authenticated seam; keep the external-provider path fail-closed.
3. Add positive and hostile tests for configured model projection, loopback
   request/response, missing or mismatched enrollment, direct/alternate
   egress denial, cancellation/teardown, and secret non-disclosure.
4. Run focused and full applicable gates, independent review, signed+DCO
   exact-head PR checks, and all seven exact post-merge workflows.

## Acceptance and non-claims

`asb run` and `asb sweep --use-config` complete against the deterministic local
mock only when explicitly enabled by the test fixture. Offline/default and
replay modes remain network-denied. No external provider access, real API key,
or production live-provider qualification is required or implied.
