---
{
  "branch": "feature/redacted-request-pointer-replay",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T18:04:23+00:00",
  "depends_on": [
    "AR-0502",
    "AR-0503",
    "AR-0504",
    "AR-0101"
  ],
  "id": "AR-0517",
  "next_action": "Apply bounded cassette request redaction pointers during strict incoming JSON comparison and align dialect option invariants.",
  "observed_branch": "feature/redacted-request-pointer-replay",
  "observed_dirty": 0,
  "observed_head": "8eff6f95d8c5598fc89259013dfdd019149885e3",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0517.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make privacy-safe redacted request bodies strictly replayable.",
  "task_revision": 6,
  "title": "Replay redacted request pointers",
  "updated_at": "2026-09-07T15:04:23+00:00",
  "worktree_key": "agent-systems-benchmark-redacted-request-pointer-replay"
}
---
## AR-0517

Make recorded request-body redaction pointers effective during strict replay without persisting volatile prompts or run metadata. Apply only bounded exact pointers before canonical comparison, align dialect option invariants with the redaction descriptor, and fail closed on missing, malformed, out-of-bounds, or unselected pointers.

Require privacy/Gitleaks, schema and formal checks, adversarial pointer negatives, native x86_64/aarch64 gates, and a real credential-free Codex replay proving tool, grading, cancellation, and redaction parity.

- 2026-09-07T14:59:50+00:00: Promote Codex privacy-safe replay pointer repair after AR-0516 release;
  shared replay fence is now available.

- 2026-09-07T14:59:57+00:00: Claimed by quality_20260906.

- 2026-09-07T15:00:43+00:00: Recorded command exit 0; command argv SHA-256
  3ae36c55e2d0091850d4417e7c90ac0a2f01ab8eb9f5610aea2653ed52814046.

- 2026-09-07T15:04:23+00:00: Heartbeat by quality_20260906.
