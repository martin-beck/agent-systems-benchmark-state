---
{
  "branch": "feature/ar-1768-exhaustive-actionable-human-diagnostics",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1766", "AR-1767"],
  "id": "AR-1768",
  "next_action": "Render every cataloged ASB error, failure, partial outcome, and warning as concise cause-specific human guidance with an honest next action when one exists.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1768-exhaustive-actionable-human-diagnostics.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {"evidence_class": "contract-test", "evidence_digest": "", "evidence_ref": "", "spec_ref": "specs/AR-1768.json", "spec_revision": 1, "status": "pending"},
  "spec_ref": "specs/AR-1768.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Give every human-visible ASB error, failure, partial result, and warning a precise cause, affected target, impact, and useful recovery.",
  "task_revision": 1,
  "title": "Exhaustive actionable human diagnostics",
  "updated_at": "2026-10-09T17:21:34+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1768-exhaustive-actionable-human-diagnostics"
}
---

Use the AR-1766 catalog and AR-1767 path behavior to make every default human
diagnostic self-explanatory. A message must identify the current command, the
specific failed or warning condition, the affected target when safe, what state
did or did not change, and the most useful recovery. For example, do not print
`parent does not exist`; print `Parent directory <PATH> does not exist.` and then
either create it automatically when ASB owns it or explain the concrete safe
correction when it is caller-owned.

Preserve fine granularity in wording. Permission denial must not look like a
missing file; a file where a directory was expected must not look like a missing
parent; provider authentication must not look like transport failure; timeout
must not look like cancellation; warning-only development limitations must not
look like command failure. Broad messages such as `operation failed`,
`unavailable`, `invalid`, `rejected`, or `cannot be written` are insufficient by
themselves whenever ASB knows the subject or cause.

Remediation must be honest and actionable. Emit one exact copyable ASB command
only when valid for the observed state; otherwise give a concise instruction
that names the path, option, capability, provider, or prerequisite to correct.
Never recommend blind retry of a non-idempotent operation. Terminal successes do
not invent next steps, warnings explain their consequence, and partial results
say what remains usable.

