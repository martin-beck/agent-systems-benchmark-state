---
{
  "branch": "feature/ar-1505-control-plane-platform-authority",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-29T00:57:44+00:00",
  "depends_on": [
    "AR-1473",
    "AR-1474",
    "AR-1480",
    "AR-1484",
    "AR-1485",
    "AR-1502"
  ],
  "id": "AR-1505",
  "next_action": "Promote after dependency verification; define and implement the authenticated control-plane platform authority/bootstrap protocol needed by the runtime launcher.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "ar1505-control-plane-luna56",
  "plan": "../plans/AR-1505-control-plane-platform-authority.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide an authenticated platform protocol that issues private runtime bootstrap inputs to ASB.",
  "task_revision": 4,
  "title": "Control-plane platform authority/bootstrap protocol",
  "updated_at": "2026-09-28T22:57:44+00:00",
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
