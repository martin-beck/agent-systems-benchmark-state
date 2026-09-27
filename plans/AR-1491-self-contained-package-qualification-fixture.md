# AR-1491: Self-contained package qualification fixture

## Objective

Create a checked-in ASB qualification fixture/harness that can verify a
deterministically generated package with the existing offline verifier's test
key, install it into an isolated owner-only temporary root, and exercise the
credential-free local/mock run, sweep, strict replay, evidence, and cleanup
journey.

This is explicitly non-production qualification. It must never be used as
release evidence or substitute for AR-1490's exact externally signed package.

## Dependencies

AR-1461 supplies release contracts and AR-1462 supplies deterministic bundle
manifest/SBOM/provenance contracts. AR-1488 and AR-1489 document the owner-backed
journey and package-consumption boundaries. AR-1490 records the missing external
package/signing-input blocker.

## Acceptance

- The fixture uses the existing offline verifier test-key pattern and is fully
  deterministic, checked in, and labeled `non-production`.
- Positive verification succeeds for manifest, checksums, SBOM/provenance, and
  test signature; tampered payload, manifest, checksum, signature, and unknown
  fields fail closed.
- A fresh owner-only temporary XDG root can run doctor/setup and the existing
  local/mock run/sweep plus strict offline replay/evidence and cleanup checks.
- Tests prove no provider, credential, network, asb-tui, or production release
  signer is needed; the fixture contains no secret or private host path.
- Focused and full workspace/docs/privacy/policy/release gates pass with signed
  SSH+DCO history. The report explicitly distinguishes qualification evidence
  from customer release evidence.

## Implementation boundary

Add only the fixture/harness, tests, and concise workflow documentation. Do not
change production signing policy, weaken package verification, fabricate release
inputs, or modify asb-tui.
