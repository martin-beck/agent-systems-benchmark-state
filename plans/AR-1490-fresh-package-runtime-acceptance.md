# AR-1490: Fresh package runtime acceptance

## Objective

Execute the first-customer readiness report against a fresh exact ASB package
in a clean disposable environment: verify the package, install it, run doctor
and setup, execute owner-backed local/mock run and sweep, consume strict
offline replay evidence, inspect receipts, and verify cancellation/restart
cleanup.

## Dependencies

AR-1461 and AR-1462 provide the release and bundle contracts; AR-1488 and
AR-1489 provide the documented journey and package-consumption boundaries.
This is ASB-only and uses no asb-tui, provider, credential, network, or native
ARM prerequisite.

## Acceptance

- A fresh exact package or reproducibly built bundle is verified against its
  manifest, checksums, SBOM/provenance, and signature policy before install.
- A clean owner-only XDG root accepts the package; installed doctor/setup
  succeed without credential values or network access.
- The installed bytes execute owner-backed local/mock run and sweep, produce
  bounded receipts/evidence, consume strict offline replay/comparison, and
  recover cancellation/restart with complete teardown.
- A readiness report records exact source/package identities, pass/fail and
  unavailable cells, privacy/egress results, and explicit exclusions. It
  never upgrades local/mock/replay evidence to live-provider quality.
- Positive/negative tests and full build/docs/privacy/policy/release gates pass;
  no claim is made if the exact package or clean environment is unavailable.

## Implementation boundary

Use a deterministic local package harness or checked-in test fixture. Repair
only a concrete ASB package/runtime defect with the smallest fail-closed
change; otherwise record the missing artifact/environment as a truthful
blocker and next action.
