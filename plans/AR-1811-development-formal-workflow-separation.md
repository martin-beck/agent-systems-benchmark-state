# AR-1811 development/formal workflow separation

## Scope

- Make ordinary pull requests and development pushes skip TLC/Alloy execution.
- Preserve all applicable non-TLC assurance jobs and their exact-head behavior.
- Keep one explicit final-delivery formal lane, documented as future/non-claimable
  during development.
- Add workflow-contract tests covering both ordinary development and final delivery.

## Acceptance

1. Ordinary development PRs have no TLC/Alloy job and no TLC result dependency.
2. The final-delivery lane invokes the pinned formal suite exactly once.
3. Existing non-formal required checks remain unchanged and green.
4. Documentation and negative tests reject accidental TLC invocation on development events.
5. Signed DCO commit, independent review, exact-head CI, merge, and post-merge verification pass.

## Constraints

Do not weaken native/QEMU, privacy, provenance, source, Rust, Kani, Loom, fuzz,
or supply-chain gates. Do not run TLC during development implementation or
qualification. All product and publication mutations use the state repository's
`handoffctl run` wrapper.
