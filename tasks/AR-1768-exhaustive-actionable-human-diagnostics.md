---
{
  "branch": "feature/ar-1768-exhaustive-actionable-human-diagnostics",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T23:16:14+00:00",
  "depends_on": [
    "AR-1766",
    "AR-1767"
  ],
  "id": "AR-1768",
  "next_action": "Render every cataloged ASB error, failure, partial outcome, and warning as concise cause-specific human guidance with an honest next action when one exists.",
  "observed_branch": "feature/ar-1768-exhaustive-actionable-human-diagnostics",
  "observed_dirty": 4,
  "observed_head": "dc67390494805693aef21d917319253b2e705da7",
  "owner": "codex-ar1768-diagnostics",
  "plan": "../plans/AR-1768-exhaustive-actionable-human-diagnostics.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1768.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1768.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Give every human-visible ASB error, failure, partial result, and warning a precise cause, affected target, impact, and useful recovery.",
  "task_revision": 19,
  "title": "Exhaustive actionable human diagnostics",
  "updated_at": "2026-10-09T21:18:48+00:00",
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


- 2026-10-09T21:11:00+00:00: AR-1766 and AR-1767 are durably done with exact-main post-merge
  evidence; promote diagnostics implementation.

- 2026-10-09T21:11:06+00:00: Claimed by codex-ar1768-diagnostics.

- 2026-10-09T21:11:52+00:00: Recorded command exit 0; command argv SHA-256
  0bb5160d7752f24d35f7fd2b0ae34eaca3c86fdb0fac72bd9b5fd8ecc443c3d8.

- 2026-10-09T21:14:25+00:00: Recorded command exit 101; command argv SHA-256
  d73b15a2495f19f934a37a5749ca6434845245f67ee6cbde94d0dd2f2dddc926.

- 2026-10-09T21:15:03+00:00: Recorded command exit 1; command argv SHA-256
  19ec7a9a00e227b25f36c927d3f7c0e18811a8a59ef539752c4804b6b3d77a76.

- 2026-10-09T21:15:10+00:00: Recorded command exit 101; command argv SHA-256
  6b8224777d0c3ebf662a6ce6f68fab05e6a2967c4c63727d959a1b8723d3bbb0.

- 2026-10-09T21:16:08+00:00: Heartbeat by codex-ar1768-diagnostics.

- 2026-10-09T21:16:14+00:00: Heartbeat by codex-ar1768-diagnostics.

- 2026-10-09T21:16:33+00:00: Implemented cause-specific error explanations, safe
  subject/state/recovery facts, reviewed next-action mapping, explicit TUI failure text, and warning
  semantics; focused tests added; baseline exposed unrelated parallel-test state-root ownership
  race.

- 2026-10-09T21:16:43+00:00: Recorded command exit 101; command argv SHA-256
  6b8224777d0c3ebf662a6ce6f68fab05e6a2967c4c63727d959a1b8723d3bbb0.

- 2026-10-09T21:16:59+00:00: Recorded command exit 101; command argv SHA-256
  6b8224777d0c3ebf662a6ce6f68fab05e6a2967c4c63727d959a1b8723d3bbb0.

- 2026-10-09T21:17:15+00:00: Recorded command exit 0; command argv SHA-256
  c7d8e590f8ef999fa2490be403111205996be0057695dbc35d0ce2aa8e3de8cf.

- 2026-10-09T21:18:34+00:00: Recorded command exit 101; command argv SHA-256
  0773d8c85b5829e988afe2b6f07ab7b21187e7b64364fedba30a5c23fb8f0530.

- 2026-10-09T21:18:48+00:00: Recorded command exit 0; command argv SHA-256
  0773d8c85b5829e988afe2b6f07ab7b21187e7b64364fedba30a5c23fb8f0530.
