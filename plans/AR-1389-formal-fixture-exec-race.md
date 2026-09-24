# AR-1389: Repair formal fixture executable race

## Objective

Repair the formal TLA artifact-acquisition fixture path so the generated
online-build helper can be launched without an `ETXTBSY` (`ExecutableFileBusy`)
race. The repair must preserve the production acquisition contract and must not
weaken offline, cache-integrity, bounded-execution, or fail-closed assertions.

## Dependencies

AR-1388 is merged at `8c88b9ec9b4f529ebe30cb230029b2575ad4e6e5`, but its
post-merge Formal assurance workflow `35967157429` failed in
`formal/tests/tla_artifact_acquisition.rs:332` during
`bounded_online_build_and_verified_cache_reuse_succeed` with OS error 26,
`ExecutableFileBusy` (`Text file busy`). The failure evidence is preserved in
AR-1388; this repair must land separately and must not mutate the released
AR-1388 branch.

## Acceptance

- The generated online-build fixture is created, closed, and executed through
  a race-free bounded path; no test sleep, retry-only masking, gate weakening,
  or platform-specific skip is used.
- The focused fixture test passes repeatedly, including a stress loop that
  exercises creation, replacement, and execution, and the complete formal test
  suite passes.
- Existing positive, missing-input, partial-input, hostile-cache, offline,
  digest, concurrency, and network-denial assertions remain intact.
- No production runtime authority, provider connectivity, credentials,
  endpoints, or live OpenRouter backend is required; local deterministic mocks
  remain sufficient for all tests and CI.
- Commit is SSH-signed with matching DCO; independent review, full applicable
  gates, exact-head CI, post-merge workflows, and durable AR release evidence
  pass before AR-1389 or its predecessor is released.
