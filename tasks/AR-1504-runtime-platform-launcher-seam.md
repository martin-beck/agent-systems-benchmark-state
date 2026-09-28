---
{
  "branch": "feature/ar-1504-runtime-platform-launcher-seam",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-29T00:46:43+00:00",
  "depends_on": [
    "AR-1473",
    "AR-1474",
    "AR-1480",
    "AR-1484",
    "AR-1485",
    "AR-1502"
  ],
  "id": "AR-1504",
  "next_action": "Implement the missing runtime-owned platform adapter/session locator on protected main, with authenticated socket ownership/permissions, private input construction, opaque source handoff and lifecycle tests; do not copy AR-1503 fa\u00e7ade. If platform authority contract cannot be established from existing control protocol, create a narrowly scoped successor AR for that protocol contract with exact symbols and keep this AR blocked.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "ar1504-launcher-luna56",
  "plan": "../plans/AR-1504-runtime-platform-launcher-seam.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide the real runtime/platform-owned launcher and authenticated session discovery for AR-1503.",
  "task_revision": 9,
  "title": "Runtime/platform launcher seam",
  "updated_at": "2026-09-28T22:48:18+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1504-runtime-platform-launcher-seam"
}
---

Successor to the exact AR-1503 review finding. AR-1503's authenticated
process-owner contract and tests are retained as historical evidence, but its
implementation is not accepted as complete because it is a tests-only façade.

- 2026-09-28T22:41:00+00:00: Created from AR-1503's independent review. The
  runtime/platform launcher and authenticated session discovery are still absent:
  no production path constructs or invokes `RuntimeControlProcessOwner`, and
  ASB CLI entry/run/sweep continue to pass `None,None`. This AR must implement
  the real owner-only seam without caller/config authority injection.

Acceptance requires:

- a production runtime/platform-owned launcher or session-discovery path that
  constructs the owner from authenticated platform inputs and invokes the
  opaque dispatch source;
- no public CLI/config/socket/chain/authority bypass and fail-closed behavior
  for missing, stale, mismatched, revoked, cancelled, restarted, or expired
  sessions;
- deterministic provider-free tests covering launch, dispatch, cancellation,
  teardown, restart, and negative authority cases;
- independent diff review, SSH-signed DCO commit, exact-head hosted CI,
  protected merge, and all required post-merge verification.

Non-goals: asb-tui changes, live provider reachability, generated authority,
caller-built runtime inputs, or weakening native/credential/egress gates.

- 2026-09-28T22:42:58+00:00: Dependencies AR-1473, AR-1474, AR-1480, AR-1484, AR-1485, and AR-1502
  are done; promote the successor to implement the missing production runtime/platform launcher seam
  identified by AR-1503.

- 2026-09-28T22:43:05+00:00: Claimed by ar1504-launcher-luna56.

- 2026-09-28T22:43:51+00:00: Heartbeat by ar1504-launcher-luna56.

- 2026-09-28T22:44:50+00:00: Setup attempt at protected origin/main: handoffctl run rejected
  worktree creation because invocation worktree 'agent-systems-benchmark' does not match declared
  'agent-systems-benchmark-ar-1504-runtime-platform-launcher-seam'; no product mutation occurred.
  Next: create declared worktree using documented setup exception, then run all worktree operations
  through handoffctl.

- 2026-09-28T22:45:34+00:00: Protected origin/main is 3c6af6b (PR #381 merge). Dependencies
  AR-1473/1474/1480/1484/1485/1502 are durable done. AR-1503 is not merged and its process_owner.rs
  exists only in its dirty worktree; therefore AR-1504 cannot truthfully compile against
  RuntimeControlProcessOwner yet. Declared AR-1504 worktree created at protected origin/main; no
  product files changed.

- 2026-09-28T22:46:43+00:00: Heartbeat by ar1504-launcher-luna56.

- 2026-09-28T22:47:36+00:00: Exact protected-main symbol audit: asb-cli::run at
  crates/asb-cli/src/lib.rs:96 invokes dispatch(args, stdout, stderr, None, None), while
  live-provider branches at lines 402-430 pass optional LiveProviderAttemptFactory; only
  run_with_runtime_control_source (lines 212-229) accepts an opaque source and fails closed. AR-1502
  exposes RuntimeBootstrapRequestV1, RuntimeCertificateChainStore,
  RuntimeCertificateAuthoritySource::new, RuntimeAuthorityInputResolver, and
  LiveProviderRuntimeBridge, but constructors needed for authenticated platform inputs remain
  crate-private and no default control-session discovery exists. Existing control client requires
  caller path via ControlClient::connect_with_versions; no fixed runtime-owned socket locator is
  defined. A real AR-1504 implementation therefore needs a new runtime-owned platform adapter that
  authenticates/discovers the control endpoint and constructs private authority inputs; simply
  wrapping optional inputs would be another façade and is rejected.

- 2026-09-28T22:48:18+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.
