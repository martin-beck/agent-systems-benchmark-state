---
{
  "branch": "",
  "checkpoint_commit": "45427b6ec7fc73f896574701df5e35b6d72b7cf4",
  "claim_expires": "2026-10-13T17:17:35+00:00",
  "depends_on": [],
  "id": "AR-1826",
  "next_action": "Supported repair unavailable in vendored handoffctl v0.7.5: bind-worktree rejects retained legacy worktree_key agent-systems-benchmark-ar-1826-explicit-setup-config-contract while branch is empty, and no coordinator command clears the pair. Add/use an explicitly reviewed coordinator repair version, then re-claim, bind codex/ar-1826-explicit-setup-contract to the exact non-overlapping worktree, and requalify reviewed e9d95999 onto current main d0e6a28.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "ar1826_setup_contract_luna",
  "plan": "../plans/AR-1826-explicit-setup-config-contract.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1826.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1826.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Define the explicit setup-file and config-bound plan contract that replaces implicit user configuration and provider-selection artifacts.",
  "task_revision": 43,
  "title": "Define explicit setup configuration and plan-binding contract",
  "updated_at": "2026-10-13T15:18:27+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1826-explicit-setup-config-contract"
}
---

This is the migration root for a deliberately breaking development CLI route:
`asb setup --output CONFIG`, `asb plan create --config CONFIG --output PLAN`,
then config-bound plan validation, run, and sweep. It replaces implicit XDG or
user-home configuration and all public ProviderSelection artifacts. It does not
implement the commands; it fixes the shared schema, path, secret, freshness,
and compatibility contract on which the remaining ARs depend.

- 2026-10-13T05:54:15+00:00: Opening dependency-free setup contract implementation for assigned
  worker.

- 2026-10-13T06:01:59+00:00: Claimed by ar1826_setup_contract_luna.

- 2026-10-13T06:02:05+00:00: Recorded command exit 0; command argv SHA-256
  9c59abdd443caaa4ce7e0e388ff8b2083eb2af27df45f54ffcbd017cddb53661.

- 2026-10-13T06:02:14+00:00: Recorded command exit 101; command argv SHA-256
  12938f82fbaa9857db28f5434d0af3e082e02e4471a57c1807c2e82d77a69772.

- 2026-10-13T06:02:19+00:00: Recorded command exit 1; command argv SHA-256
  7d251720c242e896bb416014a762bbdbc11b16b58cfa1bf45c02cf997dd84aba.

- 2026-10-13T06:03:21+00:00: Recorded command exit 0; command argv SHA-256
  2c7f822d0c4efeef82f7adbe3a43e7da667905bd9457da1c77d1da9d1f259a66.

- 2026-10-13T06:03:32+00:00: Recorded command exit 0; command argv SHA-256
  7d6f16d53a17172ad4507879d088aec762476d4325da9aead5d1e916f51d5b5c.

- 2026-10-13T06:03:50+00:00: Recorded command exit 1; command argv SHA-256
  4ed1af5d496f1d4b6201b07244668bf400be6d64b3a48a32924d2d955c6a1a2e.

- 2026-10-13T06:03:53+00:00: Recorded command exit 0; command argv SHA-256
  67c551c37b0d108afcaf8e886265f2ef1808a9265c09206b8567f6bb260a9d5c.

- 2026-10-13T06:04:19+00:00: Recorded command exit 0; command argv SHA-256
  181f7a1a3795944457260a38f6bb5c4e59bcd08a1f1f224b8aa8f6c5b2e08d8e.

- 2026-10-13T06:04:44+00:00: Recorded command exit 0; command argv SHA-256
  2b5576c87310da96af7c428f99ab2b57d1e725de0920e1bd54f695c9fd0359c8.

- 2026-10-13T06:05:06+00:00: Recorded command exit 0; command argv SHA-256
  a023f8ba4cadbc90fd0a7bb8a9bdecd5e3628a8fe72b5797eed8f79d14f77498.

- 2026-10-13T06:05:29+00:00: Recorded command exit 0; command argv SHA-256
  945e09a138030348fecf684eaf951186d1c1bb46a5fe73675c77d361579b43f1.

- 2026-10-13T06:05:55+00:00: Recorded command exit 0; command argv SHA-256
  fcfe00a36f1f324f4565ae4b364f1439e26ccccbe4a7087b286f19d2eb9cb172.

- 2026-10-13T06:06:16+00:00: Checkpointed source commit 45427b6ec7fc73f896574701df5e35b6d72b7cf4.

- 2026-10-13T06:06:43+00:00: Published signed product commits 7c9a3fb7 and 256fe639 on PR #629. Full
  cargo test --workspace --locked passed; header gate repaired at exact head 256fe639. Await
  independent review and remaining exact-head checks.

- 2026-10-13T06:12:15+00:00: Recorded command exit 0; command argv SHA-256
  28061e28e437287b0013d27fd47fed2ddc8350b90a82501da677b92b21ec027d.

- 2026-10-13T06:12:40+00:00: Recorded command exit 0; command argv SHA-256
  c1fc274cfda2da90a8dbc60e1c4acebdc3a68b75f2078ea1cfae8f39ae5012ff.

- 2026-10-13T06:13:10+00:00: Recorded command exit 0; command argv SHA-256
  fcfe00a36f1f324f4565ae4b364f1439e26ccccbe4a7087b286f19d2eb9cb172.

- 2026-10-13T06:13:33+00:00: Applied independent review fixes: strict plan identity/selection
  membership validation, digest/schema case alignment, duplicate selection schema constraints, and
  schema positive/negative tests. Focused tests and clippy/fmt pass; published ecf3ed20.

- 2026-10-13T06:15:05+00:00: Recorded command exit 0; command argv SHA-256
  2c7f822d0c4efeef82f7adbe3a43e7da667905bd9457da1c77d1da9d1f259a66.

- 2026-10-13T06:15:28+00:00: Full owner-scoped cargo test --workspace --locked passed after review
  fixes; focused 39 unit + 2 schema tests and clippy/fmt pass. Exact-head CI is progressing with
  header, provenance, shadow, platform, Kani, Loom, fuzz, and retained-fault gates green.

- 2026-10-13T08:32:08+00:00: PR #629 exact-head checks and independent local review pass;
  merge/publication awaits restored GitHub authentication and durable review recording.

- 2026-10-13T08:37:31+00:00: Claimed by ar1826_setup_contract_luna.

- 2026-10-13T08:47:15+00:00: Reconciliation attempt: bind-worktree refused because legacy worktree
  metadata is non-empty. Product worktree remains clean at signed
  ecf3ed20fa150a4aaa8289e68e6b91f5cdae291f on PR #629; exact repaired signed commit
  e9d95999c0cacff327dd350670d611aab64e69b2 is present locally on codex/ar1826-schema-contract-repair
  and verifies SSH signature plus DCO. Unauthenticated public GitHub API confirms PR #629 open,
  unmerged, mergeable, and all 14 check-runs success for ecf3ed20fa150a4aaa8289e68e6b91f5cdae291f.
  Publication is blocked by invalid/hanging GitHub auth and absent durable independent review; no
  merge attempted.

- 2026-10-13T08:47:23+00:00: Blocked publication recovery: PR #629 is open and all 14 public
  check-runs are success at ecf3ed20fa150a4aaa8289e68e6b91f5cdae291f; exact repaired signed
  e9d95999c0cacff327dd350670d611aab64e69b2 is locally verified with SSH signature and DCO. GitHub
  auth is invalid/hanging, and independent review is not durably recorded. No merge or publication
  mutation attempted.

- 2026-10-13T08:55:47+00:00: GitHub authentication is restored; resume exact-head review/publication
  recovery at e9d95999c0cacff327dd350670d611aab64e69b2.

- 2026-10-13T08:55:50+00:00: Claimed by ar1826_setup_contract_luna.

- 2026-10-13T08:56:58+00:00: Independent review completed for exact head
  e9d95999c0cacff327dd350670d611aab64e69b2: complete diff reviewed in isolated review worktree;
  strict schema identity/selection, digest case, duplicate-selection and source-header repairs are
  present; no privacy/secret/path or gate weakening findings. SSH signature and matching DCO
  verified; git diff --check passes. Required exact-head checks remain in progress.

- 2026-10-13T08:58:11+00:00: Heartbeat by ar1826_setup_contract_luna.

- 2026-10-13T09:00:56+00:00: Heartbeat by ar1826_setup_contract_luna.

- 2026-10-13T09:05:49+00:00: Heartbeat by ar1826_setup_contract_luna.

- 2026-10-13T09:11:26+00:00: Requalification blocked: PR #629 is behind base 4a486e97 after PR #630
  merged main d0e6a28. handoffctl bind-worktree refuses retained legacy worktree_key with empty
  branch; handoffctl run refuses undeclared branch/worktree. No product mutation or stale merge
  attempted.

- 2026-10-13T09:14:13+00:00: Narrow repair audit: doctor --live is clean, but bind-worktree
  correctly refuses the inconsistent legacy pair (branch empty, worktree_key
  agent-systems-benchmark-ar-1826-explicit-setup-config-contract). No product, PR, owner, or
  evidence mutation performed.

- 2026-10-13T11:09:38+00:00: Recovered expired claim formerly owned by ar1826_setup_contract_luna.
  Recovered after expired lease; no worker process, product worktree clean at e9d95999, preserved
  checkpoint/evidence for metadata repair and requalification.

- 2026-10-13T11:09:46+00:00: Claimed by ar1826_setup_contract_luna.

- 2026-10-13T11:09:52+00:00: Recorded command exit 0; command argv SHA-256
  fa8b5b71edf3200d321ee3c09e348eccd55c38732142f7ba47f3a35c7d1b1356.

- 2026-10-13T11:10:32+00:00: Durable recovery checkpoint: expired claim recovered, same owner
  re-claimed for metadata repair, oversized generated bytecode removed through handoffctl run,
  bind-worktree attempted with exact owner/revision/branch/key and rejected by the coordinator
  legacy-metadata precondition; no product mutation.

- 2026-10-13T11:10:37+00:00: Released open after bounded recovery attempt. Exact blocker is
  coordinator bind-worktree rejecting retained legacy worktree_key with empty branch; preserve
  owner/evidence, then perform supported legacy-pair repair and re-claim before product
  requalification. Product remains clean at reviewed e9d95999; no mutation or stale merge attempted.

- 2026-10-13T15:17:35+00:00: Claimed by ar1826_setup_contract_luna.

- 2026-10-13T15:17:41+00:00: Recorded command exit 0; command argv SHA-256
  4d384260108a96a48c8692a5721b3df1f8d87ecac31cc8c647f738f6df9b5ca0.

- 2026-10-13T15:18:27+00:00: Repair audit complete: doctor --live passes; no active product
  worker/process; product checkout remains clean at reviewed e9d95999. bind-worktree was not retried
  because the same legacy-metadata precondition remains and no supported clearing operation exists.
  No product, PR, or reviewed commit mutation.
