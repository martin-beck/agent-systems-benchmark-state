# AR-1350: Sandbox-owned credential channel

## Objective

Add a runtime-owned, rollback-safe credential delivery channel from an opaque
provider capability into the bubblewrap child without placing credential bytes
in host-visible argv, `SandboxLaunchInput`, authority fields, logs, or
evidence. This is the prerequisite for AR-1349 production acquisition and
AR-1329 CLI wiring.

## Dependencies and ownership

Depends on AR-1349 and AR-1329. Do not modify asb-tui. Preserve offline and
replay defaults, `NetworkPolicy::Deny`, direct/alternate egress denial, and
credential non-disclosure.

## Required work

1. Inspect and, if bounded, extend the runtime sandbox with sealed memfd/FD or
   an equivalent private child-boundary transport that survives bubblewrap
   namespace setup without argv exposure.
2. Bind the transport to the selected credential reference and adapter target;
   consume it once, erase/close on success, cancellation, timeout, child
   failure, and every partial-acquisition rollback.
3. Add positive delivery tests and negative tests for missing/invalid/duplicate
   descriptors, copied authority, wrong target/reference, direct egress,
   cancellation, teardown, and credential disclosure in argv/evidence.
4. Run focused and full workspace gates with SSH-signed DCO commits and record
   exact failures. Expose only the private runtime seam needed by AR-1349.

## Acceptance criteria

The provider child receives the credential only through the runtime-owned
channel; no host-visible command argument or public caller-built authority can
carry it. All failures fail closed and clean up descriptors/resources. No CLI
integration is enabled until this AR is merged and verified.
