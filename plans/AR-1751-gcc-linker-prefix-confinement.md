# AR-1751 plan: GCC linker-prefix trust confinement

## Scope and ownership

This P0 repair is limited to the ASB development TUI source-materialization
toolchain path introduced by AR-1737, its focused tests, documentation, and
privacy-safe qualification evidence. It must not change provider authority,
benchmark semantics, release policy, the asb-tui renderer, or unrelated
coordinator state.

## Implementation sequence

1. Reproduce the defect from exact current ASB main with a private, ownership-
   and mode-valid `ld` plus hostile sibling `collect2` and a recognizable
   library/startup-object candidate. Capture only sanitized selection facts.
2. Trace the effective Cargo/rustc/GCC argument and environment chain. Record
   which GCC helper, program-prefix, library-prefix, and linker search inputs
   are influenced by the current `-B` value.
3. Select the narrowest portable repair that keeps ambient `PATH` absent and
   preserves deterministic remapping. Every executable, helper, startup object,
   or library made reachable by the repair must be independently validated and
   bound, or the design must avoid making it reachable.
4. Keep one authoritative `CARGO_ENCODED_RUSTFLAGS` channel. Reject conflicting
   ambient `RUSTFLAGS`, target-specific flags, linker variables, relative paths,
   symlink substitutions, descriptor/path drift, untrusted ownership or mode,
   and unsupported compiler-driver semantics with stable typed diagnostics.
5. Add focused unit and integration tests covering the real production
   environment-construction path and effective child arguments. Include:
   trusted `ld` plus hostile sibling `collect2`; hostile library/startup object;
   symlink and post-validation substitution; missing helper; GCC-compatible
   success; unsupported/non-GCC driver; empty ambient `PATH`; deterministic
   artifacts across different roots; and no credential/path leakage.
6. Run formatting, Clippy with warnings denied, locked workspace tests, rustdoc
   warnings denied, relevant lifecycle/materialization journeys, privacy and
   secret scans, source-header policy, coverage regression, dependency/security
   gates, and applicable cross-repository inherited-fd/PTTY qualification.
7. Commit with SSH signature and matching DCO trailer. Publish one focused PR
   from an isolated registered worktree. Require a separate technical worker to
   review the exact candidate commit/tree and adversarial proof.
8. Synchronize without rewriting published history if main advances. Rerun all
   exact-head checks and independent review after any tree change. Construct a
   signed DCO two-parent merge locally, preserve the reviewed tree, push with an
   exact target-ref lease, and verify every exact-main post-merge workflow.
9. Publish a privacy-safe receipt with immutable base/head/tree/merge identities,
   test and CI run identities, and the precise trust boundary. Attach spec
   acceptance, release AR-1751 done, reconcile, render, and run live doctor.

## Stop conditions

- Stop fail-closed if no portable invocation can avoid or completely validate
  GCC's helper/library prefix closure.
- Do not restore ambient `PATH`, accept a shell wrapper, weaken ownership/mode
  validation, or silently fall back to a different linker.
- Do not treat development authentication, production release attestation, or a
  second GitHub account as a functional blocker.
