# AR-1511 plan: runtime/control authority issuer and capability source

1. Reconcile state and verify AR-1510's protected-main audit. Start a clean
   worktree from protected main; do not copy unmerged AR-1509/1510 façade code.
2. Read the complete ASB development, architecture and quality docs and audit
   the existing owner lifecycle, enrollment, certificate-chain, receipt,
   RuntimeAuthorityRecord, lease/relay and cancellation contracts.
3. Define the smallest authenticated control-source contract. Requests must
   carry an owner/session nonce and public binding; only the runtime/control
   authority issuer may derive private roots, tool/policy/allowlist material,
   credential capability and expiry. Return opaque capability plus an
   independently verifiable receipt/chain, never caller-built authority.
4. Implement the issuer and capability store using existing ASB contracts,
   with bounded memory/file state and explicit generation/restart/revocation
   fencing. Reject unknown fields, replay, mismatched endpoint/namespace,
   stale credentials, expired leases, cancellation and alternate egress.
5. Add deterministic provider-free tests and generated docs for every positive
   and negative path. Run focused crates, workspace quality, formal/privacy and
   fresh offline-install gates.
6. Independently review the full diff against protected main, publish only a
   clean exact-head SSH-signed DCO PR, await all required CI, merge through
   handoffctl, run terminal post-merge assurance, then release this AR with
   durable evidence for AR-1510's consumer wiring.

If the existing contracts cannot support a safe issuer, record the exact
missing contract and create a narrower design AR; never fabricate receipts or
weaken the fail-closed production boundary.
