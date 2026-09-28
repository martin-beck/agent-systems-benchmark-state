# AR-1502 — Runtime-owned bootstrap authority

Implement the missing production authority boundary identified by AR-1470. The
control/runtime path must receive a runtime-owned, authenticated bootstrap
issuer from an explicitly owned platform adapter and use it to materialize the
certificate-chain enrollment consumed by normal live dispatch.

Scope:

- define a bounded opaque bootstrap-authority handle and authenticated
  enrollment operation;
- bind the handle to the control session, namespace, relay/lease roots, and
  provider credential reference without serializing private key material;
- materialize `RuntimeCertificateChainStore` only from that owned source;
- provide deterministic local/mock adapter tests for success, mismatch,
  expiry, cancellation, restart recovery, and fail-closed absence;
- document platform adapter requirements and the production deployment handoff.

Non-goals: caller-supplied chains, generated/fake authority, live provider
reachability, asb-tui changes, or weakening existing fail-closed gates.

Completion requires independent review, exact-head hosted gates, protected
merge, post-merge verification, and explicit evidence of the platform adapter
boundary. A mock adapter proves contract behavior only; it does not claim
first-customer production authority.
