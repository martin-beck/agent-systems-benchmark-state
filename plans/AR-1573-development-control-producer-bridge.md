# AR-1573 — ASB development control producer bridge

## Scope

Expose the missing ASB producer-side control handshake/backend/result bridge so
the asb-tui adopted broker stream can negotiate and complete a development
launch.

## Acceptance

- Public bounded producer API uses existing control protocol/backend types.
- Exact protocol minor, generation, and ASB/asb-tui identities are validated.
- Supported development lifecycle result is returned and resources are cleaned
  on timeout, malformed input, or child failure.
- Existing stable/production control interfaces are unchanged.
- Contract tests cover valid, stale, malformed, unsupported, and timeout cases.

## Boundaries

Development/mock only; no production authentication, signatures, or key
management requirement.
