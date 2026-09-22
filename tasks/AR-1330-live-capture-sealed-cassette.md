---
{
  "branch": "feature/ar-1330-live-capture-sealed-cassette",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0502",
    "AR-0503",
    "AR-1329"
  ],
  "id": "AR-1330",
  "next_action": "Invoke the existing StrictReplayService::capture_authenticated_connection boundary from the live run path and seal the sanitized, redacted provider exchange as a content-addressed cassette.",
  "owner": "",
  "plan": "../plans/AR-1330.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Capture and seal a real authenticated provider exchange as a content-addressed cassette.",
  "task_revision": 1,
  "title": "Live provider capture into a sealed cassette",
  "updated_at": "2026-09-22T13:39:37+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1330-live-capture-sealed-cassette"
}
---

The AR-0502/AR-0503 replay cassette and strict-replay contracts are complete,
and `StrictReplayService::capture_authenticated_connection` exists as a
runtime-owned seam, but no live run invokes it. This AR wires the AR-1329 live
execution path into that seam so every real provider exchange is captured,
sanitized and redacted by the existing `Redactor`, sealed as a
content-addressed `CassetteContents`, and recorded with its digest and
redaction/verification result. Credentials, prompts, responses and raw capture
data never enter durable state or public control responses, and interrupted
captures reconcile without repeating uncertain paid work.
