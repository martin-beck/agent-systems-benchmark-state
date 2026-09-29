---
{
  "branch": "feature/ar-1511-runtime-control-authority-issuer",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1502",
    "AR-1484"
  ],
  "id": "AR-1511",
  "next_action": "Promote after AR-1510 blocker evidence is reconciled; implement the runtime/control authority issuer and capability contract from protected main.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1511-runtime-control-authority-issuer.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Implement the authenticated runtime/control authority issuer and opaque capability source required by production dispatch.",
  "task_revision": 2,
  "title": "Runtime/control authority issuer and capability source",
  "updated_at": "2026-09-29T03:07:20+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1511-runtime-control-authority-issuer"
}
---

AR-1510 audited the consumer boundary and proved that protected main has no
authenticated platform authority source: all provider material is test-only,
RuntimeCertificateChainStore accepts caller-provided chains, and CLI control
paths persist only public digests. This AR supplies the missing source rather
than allowing a consumer to invent authority.

Acceptance requires:

- a production ASB-only runtime/control authority issuer backed by the existing
  authenticated process-owner/enrollment contracts, with opaque capability
  handles rather than caller-supplied private roots, tools, policy or paths;
- a versioned request/response contract that authenticates the control session,
  namespace, endpoint, credential capability, generation, lease/relay roots,
  tool bundle, policy/allowlist, restart and cancellation fences, and expiry;
- independently verifiable receipt/chain issuance and replay, mismatch,
  expiry, revocation, cancellation, restart, alternate-egress and teardown
  rejection, without external provider reachability or runtime downloads;
- provider-free deterministic positive/negative tests, generated contract docs,
  and compatibility with existing RuntimeCertificateChainStore,
  RuntimeAuthorityRecord and owner lifecycle without caller/PATH injection;
- exact-head independent review, SSH-signed DCO, focused/full/formal/privacy
  gates, hosted checks, protected merge and terminal post-merge assurance.

Non-goals: asb-tui, live provider tests, public credentials, synthetic
production authority, or weakening fail-closed/native/formal gates.

- 2026-09-29T03:07:00+00:00: Created as prerequisite successor to AR-1510.
  AR-1510 passed the existing workspace tests but was blocked because no
  authenticated authority issuer/capability source exists on protected main.
  Implement this source first, then re-open the consumer wiring in a follow-on
  AR; preserve AR-1509/1510 unmerged façade work as evidence only.

- 2026-09-29T03:07:20+00:00: AR-1510 blocker evidence reconciled; promote the prerequisite authority
  issuer/capability source before consumer wiring.
