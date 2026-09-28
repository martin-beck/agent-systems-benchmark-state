# AR-1505 — Control-plane platform authority/bootstrap protocol

Define the missing platform-owned control-plane contract required before
AR-1504 can connect the runtime launcher to the actual CLI dispatch path.
AR-1504's socket discovery is retained as blocked evidence; it must not be
merged alone because a `ControlClient` does not authorize runtime dispatch.

Scope:

- extend the existing versioned control protocol with an authenticated,
  bounded bootstrap-authority operation or equivalent platform-owned handle;
- bind the issued source to control session identity, generation/nonce,
  namespace, relay and lease roots, credential reference, expiry and lifecycle;
- provide runtime-only composition that materializes private authority inputs,
  certificate enrollment, receipt requests and an opaque dispatch source;
- add provider-free local/mock protocol fixtures for success, mismatch,
  missing authority, expiry, revocation, cancellation, restart and egress
  denial;
- publish the precise adapter handoff that AR-1504 will consume.

Do not expose private authority, accept caller-supplied runtime inputs, or
contact a live provider. Completion requires independent review, signed/DCO
commit, exact-head CI, protected merge and post-merge verification.
