# AR-1567 — ASB development trusted toolchain discovery

## Scope

Make dev clone/build/materialization portable across standard user toolchains
and hosted runners without assuming `/usr/bin/cargo`.

## Acceptance

- A clean host with cargo in the configured trusted toolchain installs dev ASB.
- Explicit development override is bounded and visibly development-only.
- Missing or untrusted tools produce a typed actionable diagnostic.
- Stable installation behavior and security boundaries are unchanged.
- Tests cover PATH/toolchain discovery, rejection of unsafe paths, and offline mode.

## Boundaries

Development/mock only. Authentication, signatures, and key management remain
future hardening and must not block this prototype.
