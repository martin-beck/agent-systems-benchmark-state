# AR-1629 post-bootstrap launch progression

## Scope

Repair the exact ASB/TUI top-level `tui launch` path after broker and PTY
bootstrap succeed. The current candidate no longer exits with status 2, but it
does not reach an interactive lifecycle and instead expires at the ASB
15-second development launch deadline.

## Acceptance

- Reproduce the timeout on clean detached ASB/TUI heads with a real controlling
  PTY and capture the first missing control/render transition.
- Add a narrow paired integration test covering successful bootstrap through
  the first interactive lifecycle response and bounded cleanup.
- Preserve warning-only development authentication, signatures, and key
  management; none may block this prototype path.
- Run hosted quality gates and exact paired PTY qualification before closure.

## Out of scope

Production credential secrecy, signature hardening, and unrelated benchmark
workloads.
