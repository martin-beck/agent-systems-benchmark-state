---
{
  "branch": "feature/redacted-request-pointer-replay",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0502",
    "AR-0503",
    "AR-0504",
    "AR-0101"
  ],
  "id": "AR-0517",
  "next_action": "Apply bounded cassette request redaction pointers during strict incoming JSON comparison and align dialect option invariants.",
  "owner": "",
  "plan": "../plans/AR-0517.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Make privacy-safe redacted request bodies strictly replayable.",
  "task_revision": 2,
  "title": "Replay redacted request pointers",
  "updated_at": "2026-09-07T14:59:50+00:00",
  "worktree_key": "agent-systems-benchmark-redacted-request-pointer-replay"
}
---
## AR-0517

Make recorded request-body redaction pointers effective during strict replay without persisting volatile prompts or run metadata. Apply only bounded exact pointers before canonical comparison, align dialect option invariants with the redaction descriptor, and fail closed on missing, malformed, out-of-bounds, or unselected pointers.

Require privacy/Gitleaks, schema and formal checks, adversarial pointer negatives, native x86_64/aarch64 gates, and a real credential-free Codex replay proving tool, grading, cancellation, and redaction parity.

- 2026-09-07T14:59:50+00:00: Promote Codex privacy-safe replay pointer repair after AR-0516 release;
  shared replay fence is now available.
