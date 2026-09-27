# AR-1492: Customer bundle signing handoff

## Objective

Prepare a deterministic, reviewable customer-bundle staging directory from the
pinned ASB source and provide the exact external signing handoff required by
the release contract. Verify all unsigned inputs locally, but never create a
fake release signature or claim customer acceptance.

## Dependencies

AR-1461 supplies release workflow contracts, AR-1462 supplies manifest/SBOM/
provenance/checksum tooling, and AR-1491 supplies the non-production offline
qualification fixture. AR-1490 remains the blocked consumer acceptance task and
is intentionally not a dependency because its missing external signer is the
gap this slice prepares for.

## Acceptance

- A deterministic staging command produces the exact runtime component tree,
  manifest, checksums, SPDX/CycloneDX SBOMs, and source/provenance identities.
- Staging is reproducible and fail-closed on missing components, drift,
  unexpected files, unsupported target, or unpinned source identity.
- The handoff documents the required SSHSIG namespace/principal, allowed
  signers, ssh-keygen digest, detached signature location, and verifier command.
- Positive and negative tests cover staging, manifest/SBOM/checksum consistency,
  signature absence, wrong namespace/principal, and tampered payloads.
- No network, provider, credential, asb-tui, private path, or fabricated signing
  authority is used. Staging and test-key outputs remain non-production.
- Actual customer release remains blocked until the authorized external signer
  supplies the detached signature and post-signature verification passes.

## Implementation boundary

Change only ASB release tooling, tests, and documentation needed for this
handoff. Do not weaken signed-package policy, publish a release, or modify
asb-tui.
