# AR-1571 — ASB development broker channel transport handoff

## Scope

Wire ASB's development launch to the existing asb-tui inherited broker
channel, rather than only passing a descriptor and invoking a child with no
fd-0 transport.

## Acceptance

- ASB creates and passes the bounded broker channel/socketpair to the child on
  fd 0 using the existing packet and identity contract.
- asb-tui `run --broker --development` completes the handshake under a valid
  TTY and returns a bounded result.
- Child timeout/failure, malformed packet, stale identity, and cleanup paths
  fail closed without descriptor or socket leaks.
- Stable/non-development launches are unchanged.
- Exact-head cross-project tests pass without production credentials.

## Boundaries

Development/mock only. Authentication, signatures, and key management remain
future hardening and must not block this functional prototype.
