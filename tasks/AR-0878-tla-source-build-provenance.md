---
{
  "branch": "feature/tla-source-build-provenance",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0003",
    "AR-0901",
    "AR-0902"
  ],
  "id": "AR-0878",
  "next_action": "Determine whether upstream can publish an immutable TLA+ 1.8.0 asset; otherwise freeze an independently reproducible source-build/toolchain contract.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-0878.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Qualify immutable TLA+ tool provenance through an authoritative publication or deterministic source build.",
  "task_revision": 2,
  "title": "Qualify immutable TLA tool provenance",
  "updated_at": "2026-09-09T02:09:49+00:00",
  "worktree_key": "agent-systems-benchmark-tla-source-build-provenance"
}
---
## AR-0878

Resolve AR-0877's mutable and disappearing upstream release-asset blocker without accepting an
unsupported digest override. Qualify either a durable authoritative publication or a deterministic
source-build boundary whose output can safely seed AR-0877's verified online/offline cache.

Implementation has not started. Read the linked plan before claiming.


- 2026-09-09T02:09:49+00:00: AR-0003, AR-0901, and AR-0902 are durably done. AR-0878 provenance-only
  paths are disjoint from active AR-0806 TUI history and AR-0872 workflow documentation, and AR-0877
  is released open with its four-path prototype preserved. Promote the dependency-free provenance
  repair to resolve the exact mutable-upstream blocker.
