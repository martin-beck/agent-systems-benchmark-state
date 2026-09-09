---
{
  "branch": "feature/tla-source-build-provenance",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T05:09:52+00:00",
  "depends_on": [
    "AR-0003",
    "AR-0901",
    "AR-0902"
  ],
  "id": "AR-0878",
  "next_action": "Determine whether upstream can publish an immutable TLA+ 1.8.0 asset; otherwise freeze an independently reproducible source-build/toolchain contract.",
  "observed_branch": "feature/tla-source-build-provenance",
  "observed_dirty": 0,
  "observed_head": "af9fb7dcaabc162b13d6ee1e77d8915b6d82df20",
  "owner": "replay_20260906",
  "plan": "../plans/AR-0878.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify immutable TLA+ tool provenance through an authoritative publication or deterministic source build.",
  "task_revision": 9,
  "title": "Qualify immutable TLA tool provenance",
  "updated_at": "2026-09-09T02:18:55+00:00",
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

- 2026-09-09T02:09:52+00:00: Claimed by replay_20260906.

- 2026-09-09T02:10:21+00:00: Recorded command exit 0; command argv SHA-256
  87591628a4708da948baeca8de57baa3f6a9e497f59362495507839baa5db451.

- 2026-09-09T02:17:02+00:00: Recorded command exit 0; command argv SHA-256
  d08d8411b19e92c040e2cd567daf71d855e13bade075081b5dac56e26d89843a.

- 2026-09-09T02:17:23+00:00: Recorded command exit 0; command argv SHA-256
  4219e4c199150d62da6cf2c66417e42ee4b33de347f0ad2d3729feda716b4992.

- 2026-09-09T02:18:01+00:00: Recorded command exit 0; command argv SHA-256
  55472ab8ad1b582a14fea8d6a164d5db57451bedb3ef23690b5bd97ea4fd768b.

- 2026-09-09T02:18:55+00:00: Recorded command exit 0; command argv SHA-256
  a72c152b345720bf774b58f0a195c9dc83dab2bb1d2a78a8ed69f89822171fc6.
