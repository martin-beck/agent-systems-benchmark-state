---
{
  "branch": "feature/ar-1774-status-progress-completeness-ci",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1769", "AR-1773", "AR-1775"],
  "id": "AR-1774",
  "next_action": "Add required CI enforcement and controlled-defect tests for quiet, status, and progress completeness after universal instrumentation lands.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1774-status-progress-completeness-ci.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {"evidence_class": "hosted", "evidence_digest": "", "evidence_ref": "", "spec_ref": "specs/AR-1774.json", "spec_revision": 1, "status": "pending"},
  "spec_ref": "specs/AR-1774.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Make CI reject missing quiet support, status/progress bypasses, false estimates, and any human output in JSON mode.",
  "task_revision": 1,
  "title": "Status and progress completeness CI",
  "updated_at": "2026-10-09T21:29:29+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1774-status-progress-completeness-ci"
}
---

Make the AR-1771 through AR-1775 interaction promises durable. Add required PR
and protected-main CI that derives the public command inventory and rejects a
command missing global quiet support or output-router use, an eligible operation without a structured
step, a direct human status/progress write outside the reporter, a malformed or
non-fixed-width state token, a fabricated progress total/ETA, missing terminal
outcome, or an unsafe stream/color rendering.

The gate must prove by executable controlled defects that `--json` produces no
human status, update, ANSI, carriage-return, or progress bytes on stdout or
stderr; `-q` produces no ASB human operational output; a sub-second step creates
no bar; a step beyond one second updates through completion; redirected output is
plain append-only text; and warnings/errors retain their appropriate state and
diagnostic distinction. Test terminal resize, narrow widths, broken pipes,
interruption, nested steps, and asynchronous/slow provider behavior without
network-dependent timing assumptions.

Do not accept a hand-maintained checklist as the only guard. Tie coverage to
closed command/step/status types or generated inventories so future commands and
human output additions fail closed until instrumented and tested.
