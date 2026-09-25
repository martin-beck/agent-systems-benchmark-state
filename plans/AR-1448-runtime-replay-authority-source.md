# AR-1448: Runtime-owned replay authority source

## Outcome

Provide the missing runtime/control-owned source that materializes a
`ReplayLaunchAuthority` for the strict offline replay CLI path. The source must
construct and validate the sandbox launch input, benchmark lease, replay
cassette binding, runtime launch token, and retained backend inside the runtime
boundary; `asb-cli` receives only the opaque authority.

## Boundaries

No CLI/configuration caller may supply launch paths, lease identity, token,
backend, or authority fields. Replay remains network-denied, one-shot,
credential-free, bounded, and fail-closed on stale, copied, mismatched, or
revoked inputs. This AR does not implement live-provider capture or asb-tui.

## Acceptance

- A clean local-mock cassette can be replayed through the normal CLI dispatch
  only after runtime issuance of the opaque authority.
- CLI-only replay remains rejected and creates no execution roots.
- Positive, stale, copied, mismatch, cancellation, teardown, and restart tests
  cover the source and preserve strict offline behavior.
- Focused and full applicable gates pass on an exact reviewed tree.
