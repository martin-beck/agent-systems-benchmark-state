# AR-1812: cli2key ordinary CLI bootstrap

Implement the missing production composition seam between the verified
project-local cli2key installation and the ordinary ASB `run`/`sweep` command
paths. The seam must resolve only the AR-1779 receipt, construct the existing
`Cli2KeyCommand` and `Cli2KeyRuntimeAuthority` through the AR-1799 runtime
boundary, and retain the opaque authority for each bounded run or sweep.

## Scope

1. Add a typed runtime/control-owned resolver for the verified AR-1779
   project-local receipt. It must validate catalog identity, platform, source
   and executable digests, entrypoint, and installation status before creating
   a command; it must not read credential bytes or accept CLI-provided paths.
2. Wire the resolver into ordinary `run` and `sweep` dispatch while preserving
   the existing injected fake path and typed fail-closed errors.
3. Ensure cancellation, timeout, crash, and bounded-sweep teardown release the
   opaque authority and never fall back to OpenRouter, replay, or another
   provider.
4. Add positive and negative contract tests, update public CLI/runtime docs,
   and keep secrets, private paths, and unbounded subprocess output out of
   evidence.

## Evidence and gates

- Focused resolver, command-construction, run, sweep, and hostile lifecycle
  tests pass.
- Formatting, clippy, full offline workspace tests, headers, privacy, and
  applicable hosted CI pass.
- Independent exact-head review verifies SSH signatures, DCO, no fallback,
  and the AR-1779/AR-1799 authority boundary.
- No TLC/TLA+/model-check execution is required for development; formal
  checks remain reserved for the future final-delivery lane.

## Out of scope

Do not implement a provider fallback, expose invocation keys, scrape auth
files, or invent a receipt when AR-1779 evidence is absent. Do not change the
AR-1779 installer contract or the AR-1799 authority internals except for a
minimal typed integration adapter.
