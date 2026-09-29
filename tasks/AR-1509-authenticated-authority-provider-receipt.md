---
{
  "branch": "feature/ar-1509-authenticated-authority-provider-receipt",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-29T03:15:24+00:00",
  "depends_on": [
    "AR-1473",
    "AR-1474",
    "AR-1480",
    "AR-1484",
    "AR-1485",
    "AR-1502",
    "AR-1505"
  ],
  "id": "AR-1509",
  "next_action": "Takeover recovery: audit preserved AR-1509 worktree/diff against protected merge f92c2e941913129d7db50480f71e8361a0d43a0c before deciding repair or truthful block.",
  "observed_branch": "feature/ar-1509-authenticated-authority-provider-receipt",
  "observed_dirty": 1,
  "observed_head": "e437261f6fed268956cd436e06beb117549611ac",
  "owner": "ar1509-repair-luna56",
  "plan": "../plans/AR-1509-authenticated-authority-provider-receipt.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Replace the AR-1508 test fa\u00e7ade with an authenticated production authority-provider receipt and lifecycle fence.",
  "task_revision": 22,
  "title": "Authenticated authority-provider receipt",
  "updated_at": "2026-09-29T02:47:15+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1509-authenticated-authority-provider-receipt"
}
---

AR-1508 established the intended private provider boundary but independent
review found it is only a test façade. This AR owns the concrete production
contract required before the launcher can serve first-customer workloads.

Acceptance requires:

- a non-test runtime/control provider implementation that obtains private
  roots, namespace, tools, policy, credential capability, and enrollment/receipt
  material from an authenticated platform source;
- a signed/attested provider receipt or equivalent independently verifiable
  binding that proves endpoint identity, namespace, lease/relay roots, tool
  bundle, policy/allowlist, credential reference, generation, restart,
  cancellation, and expiry claims—not merely a provider-selected digest;
- runtime materialization and ordinary CLI dispatch consume only this provider
  receipt; no caller/config/PATH/fixed-path/synthetic authority injection;
- expiry, revocation, cancellation, restart, teardown, and alternate-egress
  fences remain active after materialization, with deterministic provider-free
  tests for every negative path;
- independent exact-head review, SSH-signed DCO, hosted checks, protected
  merge, and terminal post-merge assurance.

Non-goals: asb-tui, live provider reachability, public credentials, fixed or
mock production authority, or weakening formal/privacy/native gates.

- 2026-09-29T04:33:00+02:00: Created from independent AR-1508 P1/P2 review.
  Its signed local commits remain unmerged evidence only.

- 2026-09-29T02:32:37+00:00: Dependencies through AR-1505 verified done; AR-1508 review established
  the need for an independently verifiable production provider receipt and lifecycle fence.

- 2026-09-29T02:34:45+00:00: Claimed by ar1509-receipt-luna56.

- 2026-09-29T02:34:57+00:00: Heartbeat by ar1509-receipt-luna56.

- 2026-09-29T02:35:00+00:00: Setup audit: state reconciled and AR-1509 claimed; product docs,
  architecture, quality, complete task/plan, and AR-1508 rejection evidence inspected. Starting
  protected-main audit and isolated worktree.

- 2026-09-29T02:35:36+00:00: Recorded command exit 0; command argv SHA-256
  f37b2453c85f09b341744c0388afcea4a2996bd5cf9a487d3590768224d1a498.

- 2026-09-29T02:36:05+00:00: Recorded command exit 0; command argv SHA-256
  0c6490261aa9396fc6772d6824bb81823b5ad3db12630d427aef3eddfbe99507.

- 2026-09-29T02:39:15+00:00: Recorded command exit 2; command argv SHA-256
  d95c6d26f0a6c034f3346e054e522a4e446147c9866d120568d0c5d5f2635eea.

- 2026-09-29T02:39:46+00:00: Recorded command exit 0; command argv SHA-256
  2bb97bf4392e626c79c4466d212454229b4ca3a14bc0ddae072adfd59de5461d.

- 2026-09-29T02:40:35+00:00: Recorded command exit 0; command argv SHA-256
  3aab0a27a931c32a402924336a3316ecc59654350a729682e4381c7da6c424a0.

- 2026-09-29T02:41:14+00:00: Recorded command exit 0; command argv SHA-256
  0e37ee7f7df3e5ecb159410799f0bd7b9a7e3bf137cd83298e2f0440635678cf.

- 2026-09-29T02:41:45+00:00: Recorded command exit 101; command argv SHA-256
  44858bcc1bea325f8e4ec42626fdf2970d2310a4694e160101531722dea4dfa4.

- 2026-09-29T02:42:23+00:00: Recorded command exit 0; command argv SHA-256
  49e3be4357af2b4200bbd1710f92d2a5552317c4cce8b2e2c67bfd4809387483.

- 2026-09-29T02:42:48+00:00: Recorded command exit 101; command argv SHA-256
  44858bcc1bea325f8e4ec42626fdf2970d2310a4694e160101531722dea4dfa4.

- 2026-09-29T02:44:35+00:00: Coordinator stopped the worker and is recovering this AR for a repair
  worker; preserve existing commits, dirty diff, and command evidence. No completion claim.

- 2026-09-29T02:44:42+00:00: Claimed by ar1509-repair-luna56.

- 2026-09-29T02:45:24+00:00: Heartbeat by ar1509-repair-luna56.

- 2026-09-29T02:45:43+00:00: Replacement repair worker takeover recorded; heartbeat completed and
  preserved commits/dirty diff will be inspected before implementation.

- 2026-09-29T02:47:15+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.
