# AR-1512 plan: authenticated process-owner material contract

1. Reconcile state and verify AR-1511's blocked evidence. Start an isolated
   worktree from protected main; do not reuse its reverted dirty façade.
2. Read all ASB development, architecture and quality documentation and audit
   owner lifecycle, enrollment, certificate, credential, lease/relay, tool
   bundle, sandbox launch and CLI control contracts.
3. Define a stable serde contract with deny-unknown-fields for an authenticated
   process-owner material response. Keep secrets out of evidence; expose only
   opaque capability handles where appropriate and bind every public digest to
   the authenticated source material.
4. Implement the owner-side issuer/store and ordinary runtime/control/CLI
   caller. It must supply provider-owned material to the runtime issuer and
   dispatch source, reject caller/PATH/config authority, and bind executable and
   adapter provenance to pinned tools and policy.
5. Add deterministic positive/negative tests for unknown fields, replay,
   endpoint/session mismatch, credential and namespace drift, expiry,
   restart/cancel/revoke/teardown, target/egress and launch-provenance drift.
   Run focused, serial workspace, clippy, docs, format, formal/privacy and
   fresh-install gates.
6. Independently review the complete exact diff and signed DCO commit. Publish
   only from a clean tree, await exact-head CI, protected merge, terminal
   post-merge assurance, and release this AR with durable evidence for the
   AR-1511 consumer repair.

If the existing control owner cannot issue this material without new authority,
record the exact missing primitive and create a narrower contract AR; never
derive private authority from public digests or publish a test-only seam.
