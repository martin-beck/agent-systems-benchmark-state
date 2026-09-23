---
{
  "branch": "feature/ar-1357-runtime-attested-enrollment-record",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1356"],
  "id": "AR-1357",
  "next_action": "Promote after AR-1356 is done, then implement the versioned control-issued enrollment record transport and opaque runtime ingestion with positive and negative tests.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1357-runtime-attested-enrollment-record.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Transport authenticated enrollment records into runtime without exposing authority to the CLI.",
  "task_revision": 1,
  "title": "Runtime-attested enrollment record transport",
  "updated_at": "2026-09-23T21:45:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1357-runtime-attested-enrollment-record"
}
---

Successor for AR-1355. AR-1356 supplies the authenticated control/runtime attestation primitive; this task supplies the missing bounded transport and runtime consumer. Preserve fail-closed AR-1329 behavior and do not touch asb-tui.

- 2026-09-23T21:45:00+00:00: Created after AR-1355 audit found only an in-process enrollment trait and opaque handle seam; no versioned authenticated record transport or CLI consumer exists.
