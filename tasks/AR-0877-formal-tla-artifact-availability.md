---
{
  "branch": "fix/formal-tla-artifact-availability",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T04:01:25+00:00",
  "depends_on": [
    "AR-0003",
    "AR-0901",
    "AR-0902"
  ],
  "id": "AR-0877",
  "next_action": "Audit authoritative TLA+ v1.8.0 release metadata and replace the current partial repin with bounded approved-host acquisition, exact offline cache verification, fail-closed mutation fixtures, and preserved TLC/Alloy proofs.",
  "observed_branch": "fix/formal-tla-artifact-availability",
  "observed_dirty": 3,
  "observed_head": "dca243ab7b8cbb0b2b49a568dec99c517e0719c2",
  "owner": "replay_20260906",
  "plan": "../plans/AR-0877.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair the formal workflow's unavailable TLA+ artifact pin without weakening provenance or offline verification.",
  "task_revision": 14,
  "title": "Repair formal TLA artifact availability",
  "updated_at": "2026-09-09T01:21:45+00:00",
  "worktree_key": "agent-systems-benchmark-formal-tla-artifact-availability"
}
---
## AR-0877

Replace the TLA+ release-asset URL that returns HTTP 404 with an authoritative, durable,
content-verified acquisition and offline-cache boundary. Preserve all positive and deliberate
mutation formal checks.

Implementation has not started. Read the linked plan before claiming.


- 2026-09-09T01:01:21+00:00: Dependencies AR-0003, AR-0901, and AR-0902 are done; owned formal
  acquisition paths are disjoint from active AR-0806 TUI, AR-0855 state vendor, and AR-0876
  provider-launch scopes. Promote for the blocking TLA+ artifact availability repair.

- 2026-09-09T01:01:25+00:00: Claimed by replay_20260906.

- 2026-09-09T01:01:44+00:00: Recorded command exit 0; command argv SHA-256
  dd885d3beb1c7712be2c40fc7a268651d94964934cea87ee439edf2d698d0f77.

- 2026-09-09T01:02:47+00:00: Claimed clean isolated worktree
  /srv/data/projects/agent-systems-benchmark-formal-tla-artifact-availability at exact product main
  dca243ab7b8cbb0b2b49a568dec99c517e0719c2 after reading required docs and full plan. Initial audit
  found existing signed commit 7add29f already changed four owned paths to GitHub API asset
  551007111, SHA-256 4c7bb1f6..., and 4487756 bytes, but the current shell fetch still follows
  redirects generically and lacks the plan's metadata/approved-final-host, create-new atomic
  concurrency, hardlink/owner-mode, bounded retry, and comprehensive offline/cache fault boundary.
  Preserve this partial repin as provenance and implement the remaining fail-closed acquisition
  contract without changing authoritative TLA/Alloy models.

- 2026-09-09T01:15:21+00:00: Recorded command exit 0; command argv SHA-256
  70f1fead417b3551ce217b80588f20f9dbde4f1dcadb78008ccc4be6ff343440.

- 2026-09-09T01:16:06+00:00: Recorded command exit 0; command argv SHA-256
  5e5ecd106803e960373de65301f4e5653ca8202f0b4a5150d59a5b3ccdeeeded.

- 2026-09-09T01:18:10+00:00: Recorded command exit 0; command argv SHA-256
  ba8ee64e9597bd068dffbae0ae9f9eee17f60682a6c59868f2dcae8a4b48f195.

- 2026-09-09T01:19:30+00:00: Recorded command exit 1; command argv SHA-256
  32b5fe4cf3e4b6847c396e7fc5fd5e904e79d55d6de51d689484ea716904e270.

- 2026-09-09T01:20:05+00:00: Recorded command exit 2; command argv SHA-256
  5f2552aa6dd90afe912fa78e648362c3ca4d79143c30fa8a390c6f20faa59895.

- 2026-09-09T01:21:40+00:00: Recorded command exit 127; command argv SHA-256
  4b17e7752a0c32c0141c6e60bcda040b8eb37f78ac08d824c892eabbe339a747.
