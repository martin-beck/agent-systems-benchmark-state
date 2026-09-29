---
{
  "branch": "feature/ar-1511-runtime-control-authority-issuer",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-29T05:17:29+00:00",
  "depends_on": [
    "AR-1502",
    "AR-1484"
  ],
  "id": "AR-1511",
  "next_action": "Authority issuer module added on clean protected-main worktree; run focused cargo checks, repair compiler/lint failures, then add deterministic issuer tests and generated contract documentation.",
  "observed_branch": "feature/ar-1511-runtime-control-authority-issuer",
  "observed_dirty": 2,
  "observed_head": "f92c2e941913129d7db50480f71e8361a0d43a0c",
  "owner": "ar1511-authority-issuer-luna56",
  "plan": "../plans/AR-1511-runtime-control-authority-issuer.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Implement the authenticated runtime/control authority issuer and opaque capability source required by production dispatch.",
  "task_revision": 15,
  "title": "Runtime/control authority issuer and capability source",
  "updated_at": "2026-09-29T03:18:12+00:00",
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

- 2026-09-29T03:07:26+00:00: Claimed by ar1511-authority-issuer-luna56.

- 2026-09-29T03:09:33+00:00: Heartbeat by ar1511-authority-issuer-luna56.

- 2026-09-29T03:09:47+00:00: Recorded command exit 128; command argv SHA-256
  f191dd0fbda4e553585d5f35f001b74f00b2469b9897cf8e131123086d044dcb.

- 2026-09-29T03:10:16+00:00: Recorded command exit 0; command argv SHA-256
  bf7d0931c592ad3af8a21d778a3e4043e3ab3385d3765e4101138a38171673af.

- 2026-09-29T03:11:57+00:00: Heartbeat by ar1511-authority-issuer-luna56.

- 2026-09-29T03:12:00+00:00: Setup audit: initial worktree command targeted the state checkout and
  failed with invalid reference; explicit git -C product worktree creation then succeeded. Clean
  branch feature/ar-1511-runtime-control-authority-issuer is at protected main
  f92c2e941913129d7db50480f71e8361a0d43a0c with no product changes.

- 2026-09-29T03:12:20+00:00: Recorded command exit 0; command argv SHA-256
  295a35f99d4aa7024b5e0a35d1dd38654014d35e0d6da14a79231d3b8d7d50ba.

- 2026-09-29T03:15:43+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-29T03:17:29+00:00: Heartbeat by ar1511-authority-issuer-luna56.

- 2026-09-29T03:17:44+00:00: Baseline cargo check --locked -p asb-runtime -p asb-cli completed
  successfully at protected main (exit 0); earlier state recorded exit 2 for a setup attempt, but no
  product diagnostic was present. Product implementation now adds the runtime-owned issuer seam;
  focused compile follows.

- 2026-09-29T03:17:59+00:00: Recorded command exit 101; command argv SHA-256
  44858bcc1bea325f8e4ec42626fdf2970d2310a4694e160101531722dea4dfa4.
