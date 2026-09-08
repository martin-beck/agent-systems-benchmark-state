---
{
  "branch": "feature/provider-recording-choice",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0104",
    "AR-0310",
    "AR-0313",
    "AR-0503",
    "AR-0504",
    "AR-0318"
  ],
  "id": "AR-0314",
  "next_action": "Paused by coordinator pending dependency update for missing credential-reference resolver. Preserve exact dirty two-path replay-only catalog/source-choice skeleton; after confirmation, correct only the PolicyVersion test fixture and continue bounded boundedBut do not implement live credential resolution.",
  "observed_branch": "feature/provider-recording-choice",
  "observed_dirty": 2,
  "observed_head": "9feeba6524357df38e3ad118d4c3740306d3ec8e",
  "owner": "",
  "plan": "../plans/AR-0314.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Offer matching prior recordings or an actual provider connection without silently choosing either.",
  "task_revision": 17,
  "title": "Choose matching replay or live provider execution",
  "updated_at": "2026-09-08T14:10:26+00:00",
  "worktree_key": "agent-systems-benchmark-provider-recording-choice"
}
---
## AR-0314

Offer matching prior recordings or an actual provider connection without silently choosing either.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-08T13:37:26+00:00: Dependency audit: AR-0104, AR-0310, AR-0503, AR-0504, and AR-0313 are
  durably done; AR-0803 is done. Promote as highest-priority compatible provider/replay leaf.

- 2026-09-08T13:37:29+00:00: Claimed by quality_20260906.

- 2026-09-08T13:38:40+00:00: Recorded command exit 0; command argv SHA-256
  c2a25f84ed443b9770bf82f9936459b9a8b8dc5e072d4c915fbb2fd7643af8d2.

- 2026-09-08T13:39:07+00:00: Recorded command exit 0; command argv SHA-256
  d60eb14ae9128e35a0b23dbc6d74e92e0a232a68a2318aed870d56226eb6f4be.

- 2026-09-08T00:00:00+00:00: Independent provider/TUI audit found no implementation for resolving
  credential references, verifying their digest, or injecting them at a bounded process boundary.
  Added dependency AR-0318; recording catalog work may proceed, but live credential preflight remains
  fenced until AR-0318 proves the fail-closed resolver and privacy boundary.

- 2026-09-08T13:39:27+00:00: Recorded command exit 0; command argv SHA-256
  a12133e023147b1cbdb6246af3266c39f570839f1079a40b8d37d93d1dfdc0a5.

- 2026-09-08T13:42:28+00:00: Recorded command exit 101; command argv SHA-256
  c73a16ca22deceac2bf5e7129b39a604808a95cd3c2917f4524e0ec324f9bbf1.

- 2026-09-08T13:43:53+00:00: Paused checkpoint on exact base
  9feeba6524357df38e3ad118d4c3740306d3ec8e. Dirty paths: crates/asb-replay/src/lib.rs plus untracked
  crates/asb-replay/src/selection.rs. Delta authenticates cassette roots, indexes explicit
  profile-digest+agent compatibility metadata, offers deterministic recording identities, and
  requires explicit replay or live choice with no fallback. No live connection or credential
  resolver mutation. Focused cargo test exited 101 at compile time because the new test fixture
  incorrectly supplied nonexistent PolicyVersion.name; product code did not run. Preserve unchanged
  until dependency update.

- 2026-09-08T13:45:01+00:00: Paused safely: replay/catalog skeleton remains in declared worktree;
  live provider path is fenced on new AR-0318. Release lane so credential boundary can be
  implemented.

- 2026-09-08T14:04:53+00:00: Claimed by quality_20260906.

- 2026-09-08T14:06:33+00:00: Recorded command exit 101; command argv SHA-256
  6dab8e4e0daf4974e48901fca9cc72f1bf8ff91dd686f51563d8bab821fa6621.

- 2026-09-08T14:06:41+00:00: No durable progress after repeated follow-ups; preserve the dirty
  replay/catalog skeleton and exact fixture blocker. Release lane so the worker can implement ready
  AR-0319; AR-0314 may be reclaimed only after fixture repair is explicitly resumed.

- 2026-09-08T14:08:52+00:00: Claimed by quality_20260906.

- 2026-09-08T14:10:07+00:00: Recorded command exit 0; command argv SHA-256
  6dab8e4e0daf4974e48901fca9cc72f1bf8ff91dd686f51563d8bab821fa6621.

- 2026-09-08T14:10:26+00:00: Repeated resumed exit-101 with no diagnosis or fixture repair; preserve
  dirty replay/catalog worktree and exact blocker. Release inactive claim; reclaim only when the
  worker can execute the configured focused repair.
