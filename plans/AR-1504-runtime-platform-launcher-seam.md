# AR-1504 — Runtime/platform launcher seam

Implement the missing production boundary identified by the AR-1503 review.
The runtime must own authenticated session discovery and launch the process
owner from platform-issued inputs; the current test-only constructor is not
enough for customer production use.

Scope:

- identify the existing ASB runtime/CLI launch boundary and add a narrow,
  authenticated platform-owned launcher/session handle;
- invoke `RuntimeControlProcessOwner` only from that owner-owned path and hand
  downstream code an opaque dispatch source;
- bind lifecycle cancellation, teardown, restart recovery, expiry, revocation,
  and no-authority failure to the owner contract;
- add deterministic local/mock tests for success and every negative lifecycle
  path, without contacting a live provider;
- document the production adapter contract and deployment handoff.

Do not expose caller-supplied sockets, clients, chains, certificate authority,
policy, roots, tools, namespace, or launch inputs through public CLI/config
surfaces. Do not modify asb-tui.

Completion requires independent review, signed/DCO commit, exact-head hosted
checks, protected merge, and post-merge verification. A mock/platform fixture
proves contract behavior only; it must not be presented as first-customer
production evidence.
