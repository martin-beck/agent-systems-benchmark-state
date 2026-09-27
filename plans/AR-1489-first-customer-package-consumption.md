# AR-1489: First-customer package consumption

## Objective

Verify the published ASB release/package boundary by installing a clean local
bundle, running doctor and setup, executing the owner-backed credential-free
local/mock run and sweep, consuming strict offline replay evidence, and
removing the disposable installation without leaking private data.

## Dependencies

AR-1461 and AR-1462 provide the published pinned release/bundle workflow;
AR-1488 provides the documented owner-backed journey. This is ASB-only and
does not require asb-tui, remote providers, credentials, downloads, or native
ARM.

## Acceptance

- Build or consume one exact release bundle from a pinned protected-main
  revision; verify manifest, checksums, SBOM/provenance, and signature policy
  before installation.
- Install into a disposable owner-only XDG root, run doctor and setup
  preflight, and exercise owner-backed local/mock run and sweep.
- Validate bounded result/receipt evidence, strict offline replay/comparison,
  cancellation/restart recovery, and teardown/cleanup from the installed
  artifact.
- Negative tests reject altered checksums/manifests, unknown setup fields,
  missing authority, replay/tamper mismatch, and unsafe cleanup paths.
- Full build/test/docs/privacy/policy/release gates, signed DCO review,
  exact-head CI, and all post-merge workflows pass. No live-provider,
  asb-tui, or native-platform claim is made.

## Implementation boundary

Prefer a deterministic package-consumption harness and docs. Repair only a
concrete ASB packaging/install gap with the smallest fail-closed change; never
weaken release or authority gates.
