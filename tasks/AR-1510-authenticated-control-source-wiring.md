---
{
  "branch": "feature/ar-1510-authenticated-control-source-wiring",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-29T03:16:31+00:00",
  "depends_on": [
    "AR-1505"
  ],
  "id": "AR-1510",
  "next_action": "Blocked: obtain and integrate a real authenticated platform authority provider plus production control-client bootstrap/CLI wiring; create a narrower successor when that source/capability contract is available.",
  "observed_branch": "feature/ar-1510-authenticated-control-source-wiring",
  "observed_dirty": 0,
  "observed_head": "f92c2e941913129d7db50480f71e8361a0d43a0c",
  "owner": "ar1510-control-source-luna56",
  "plan": "../plans/AR-1510-authenticated-control-source-wiring.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide the authenticated platform control source and production lifecycle wiring required by the authority-provider receipt.",
  "task_revision": 13,
  "title": "Authenticated control source and production provider wiring",
  "updated_at": "2026-09-29T03:06:45+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1510-authenticated-control-source-wiring"
}
---

AR-1509 proved the receipt façade and lifecycle tests but was correctly blocked:
all material construction is test-only, receipts are self-attested from caller
inputs, and no live runtime/sweep path obtains authority from an authenticated
control source. This successor owns the missing production boundary.

Acceptance requires:

- a non-test platform/control adapter that obtains private roots, namespace,
  tool bundle, policy/allowlist, credential capability and enrollment material
  from authenticated control state without caller/config/PATH injection;
- an independently verifiable control-authenticated receipt binding endpoint,
  namespace, lease/relay roots, tool/policy digests, credential reference,
  generation, restart, cancellation and expiry claims;
- production runtime/control bootstrap, ordinary CLI live run/sweep and
  scheduler attempt transitions consume only the verified receipt/provider;
- expiry, revocation, cancellation, restart, teardown and alternate-egress
  denial are checked at every transition, with deterministic provider-free
  positive and negative tests;
- preserve zero-runtime-dependency/offline-after-install boundaries and do not
  require live external provider reachability;
- independent exact-head review, SSH-signed DCO commit, focused and full gates,
  hosted checks, protected merge, and terminal post-merge assurance.

Non-goals: asb-tui changes, public credentials, synthetic production authority,
test-only façade publication, or weakening native/formal/privacy gates.

- 2026-09-29T02:55:00+00:00: Created as the narrow successor to AR-1509.
  AR-1509 focused gate passed 53/53, but independent audit found no
  non-test authenticated provider construction/callsite, only self-attested
  local-input digests, and no production transition fencing. Preserve its
  unmerged commits as evidence only; start from protected main.
  AR-1509 remains a blocked audit rather than a prerequisite; this successor
  starts from the protected AR-1505 merge and owns the missing boundary.

- 2026-09-29T02:58:10+00:00: AR-1509 blocker evidence reconciled; successor starts from protected
  AR-1505 and owns authenticated control-source production wiring.

- 2026-09-29T02:58:16+00:00: Claimed by ar1510-control-source-luna56.

- 2026-09-29T02:59:27+00:00: Heartbeat by ar1510-control-source-luna56.

- 2026-09-29T02:59:42+00:00: Initial heartbeat/setup audit: state lease renewed; protected product
  main f92c2e941913129d7db50480f71e8361a0d43a0c verified. Product checkout is dirty with unrelated
  in-progress changes, so work will use an isolated worktree. AR-1509 commits will not be reused.

- 2026-09-29T03:00:29+00:00: Recorded command exit 0; command argv SHA-256
  50ed27b19fa10dbd81bbbc22a461533a005f4c833af7c90efa4234855887898b.

- 2026-09-29T03:02:20+00:00: Recorded command exit 0; command argv SHA-256
  3b47dab5249ed79d8d94244ee308b7a7e49c78e7b6a110bb8eafbd47db3a9f11.

- 2026-09-29T03:03:26+00:00: Heartbeat by ar1510-control-source-luna56.

- 2026-09-29T03:05:54+00:00: Blocked after exact protected-main audit at
  f92c2e941913129d7db50480f71e8361a0d43a0c. Evidence: asb-runtime live_service.rs exposes
  RuntimeControlBootstrap::materialize_provisioner only as a crate-private test-fixture seam taking
  caller-provided RuntimeAuthorityInputs and state_path; every callsite is under the runtime
  unit-test module (lines 2657-2666). RuntimePlatformAuthorityProvider/production provider
  construction is absent on protected main. asb-cli control.rs persists RuntimeAuthorityRecord only
  through private install_runtime_authority called during restart validation and test fixtures
  (lines 1115-1119, 2073-2105, 5097-5199); no production AuthEnroll/AuthHelperInvoke path creates
  authenticated authority material. asb-cli ordinary run/sweep rejects absent live_factory (lib.rs
  lines 3214-3217), and runtime dispatch source helpers are only API/test seams, not ordinary
  dispatch callsites. Implementing now would require inventing
  certificate/roots/tools/policy/allowlist or accepting caller/PATH authority, violating AR-1510
  non-goals and fail-closed requirements. Next action: create narrower successor to integrate a real
  authenticated platform authority provider and production control-client bootstrap/CLI wiring once
  that platform source and capability contract are available; do not publish AR-1509 façade commits.

- 2026-09-29T03:06:20+00:00: Temporary state correction: retain blocked audit while setting the
  explicit durable next action.

- 2026-09-29T03:06:31+00:00: Claimed by ar1510-control-source-luna56.

- 2026-09-29T03:06:45+00:00: Durable next_action corrected after blocker audit; exact evidence is in
  the subsequent blocked-release note.
