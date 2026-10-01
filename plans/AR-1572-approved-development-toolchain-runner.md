# AR-1572 — ASB approved development toolchain runner

## Scope

Create the bounded toolchain runner/fixture that makes the first-time
credential-free development journey runnable on a clean host.

## Acceptance

- Runner exposes cargo/git/setsid through private, immutable tool paths accepted
  by AR-1567.
- Clean online and offline clone/build/materialization qualification succeeds.
- Runner reports typed diagnostics when unavailable and does not widen trust to
  arbitrary PATH or group-writable parents.
- No API key, authentication, signature, or key-management requirement is
  introduced for development mode.

## Boundaries

Development/CI runner only; production toolchain and authentication hardening
remain separate concerns.
