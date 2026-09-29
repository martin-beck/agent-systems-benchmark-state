# AR-1508 — Platform-owned authority provider

Implement the missing authenticated authority-provider contract between the
AR-1505 bootstrap protocol and runtime-owned authority materialization.

Scope:

- define the smallest versioned platform-owned provider contract for private
  lease/relay roots, namespace, tool pins, policy, credential reference, and
  enrollment/receipt material;
- bind every materialized value to the authenticated AR-1505 session and
  digest claims, reject unknown/mismatched/tampered values, and keep private
  values inside runtime/control;
- change `RuntimeControlBootstrap::materialize_provisioner` so callers cannot
  supply `RuntimeAuthorityInputs` or fixed paths, then add the opaque dispatch
  handoff needed by AR-1507;
- add deterministic provider-free negative and lifecycle tests and document
  the first-customer platform deployment handoff.

Do not modify asb-tui, use live provider credentials, discover authority from
PATH or fixed host paths, synthesize roots/tools/policy, or weaken fail-closed
formal/privacy/native gates. Completion requires independent exact-head review,
signed DCO commit, hosted CI, protected merge, and post-merge verification.
