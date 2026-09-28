---
{
  "branch": "feature/ar-1505-control-plane-platform-authority",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-29T00:59:05+00:00",
  "depends_on": [
    "AR-1473",
    "AR-1474",
    "AR-1480",
    "AR-1484",
    "AR-1485",
    "AR-1502"
  ],
  "id": "AR-1505",
  "next_action": "Implement versioned RuntimeBootstrap control operation and runtime adapter; add provider-free identity/generation/nonce/expiry/revocation/restart/cancellation/egress tests.",
  "observed_branch": "feature/ar-1505-control-plane-platform-authority",
  "observed_dirty": 0,
  "observed_head": "3c6af6b351e0c32ee8f5e48716654d854dcbbac2",
  "owner": "ar1505-control-plane-luna56",
  "plan": "../plans/AR-1505-control-plane-platform-authority.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide an authenticated platform protocol that issues private runtime bootstrap inputs to ASB.",
  "task_revision": 10,
  "title": "Control-plane platform authority/bootstrap protocol",
  "updated_at": "2026-09-28T23:02:29+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1505-control-plane-platform-authority"
}
---

Successor to the exact AR-1504 blocker. AR-1504 proved owner-only control
socket discovery but could not obtain the private authority inputs needed to
construct an authenticated runtime owner: the current control protocol has no
platform-owned bootstrap/authority operation, while ASB CLI still dispatches
with `None,None`. This AR defines that missing control-plane boundary without
merging the incomplete discovery-only patch.

Acceptance requires:

- a versioned, authenticated control-plane operation that issues or references
  runtime-owned bootstrap authority, certificate enrollment, namespace, relay
  and lease roots, credential reference, expiry, cancellation and restart
  binding without exposing private material;
- an ASB runtime adapter that consumes only that source and constructs private
  `RuntimeAuthorityInputs`, `RuntimeCertificateAuthoritySource`, bootstrap and
  receipt requests, with no caller/config/socket/chain authority injection;
- deterministic provider-free protocol and negative tests for identity,
  generation, nonce, expiry, revocation, restart, cancellation and egress
  denial;
- an explicit handoff contract for AR-1504 to wire the launcher and CLI
  entrypoint, with no fabricated authority or live-provider requirement;
- independent review, SSH-signed DCO commit, exact-head hosted CI, protected
  merge, and post-merge verification.

Non-goals: asb-tui changes, live provider reachability, synthetic authority,
public credential/socket paths, or weakening fail-closed gates.

- 2026-09-28T22:56:27+00:00: Dependencies are done; promote the narrow control-plane
  authority/bootstrap protocol successor required by AR-1504 exact blocker.

- 2026-09-28T22:56:32+00:00: Claimed by ar1505-control-plane-luna56.

- 2026-09-28T22:57:44+00:00: Heartbeat by ar1505-control-plane-luna56.

- 2026-09-28T22:58:32+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-28T22:58:49+00:00: Recorded command exit 0; command argv SHA-256
  6840d2f0cea6f9cf6ffce81b9b1b74dcdddaff8701fc6cc1705c309033813254.

- 2026-09-28T22:59:05+00:00: Heartbeat by ar1505-control-plane-luna56.

- 2026-09-28T23:00:14+00:00: Setup audit at protected origin/main 3c6af6b: declared worktree
  agent-systems-benchmark-ar-1505-control-plane-platform-authority is clean. Existing protocol
  symbols: ControlCall::RuntimeReceipt and CONTROL_RUNTIME_RECEIPT_V1=1.10 return chain+receipt but
  accept only provider/generation/request nonce; ControlBackend lacks peer/session identity;
  RunnerBackend handles RuntimeReceipt at crates/asb-cli/src/control.rs:3177; RuntimeAuthorityRecord
  and RuntimeCertificateAuthoritySource remain private runtime inputs. Existing
  ProvisionedControlServer/handoff.rs only passes an anonymous descriptor. This exact gap requires a
  new versioned authenticated bootstrap operation, not caller-supplied authority or synthetic paths.

- 2026-09-28T23:02:29+00:00: Recorded command exit 101; command argv SHA-256
  51ba69d4c610737a26b3ee3167f118767410cbc10708f3e6931f62c061247358.
