---
{
  "branch": "feature/record-replay-docs",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1202", "AR-1203", "AR-1204", "AR-1205"],
  "id": "AR-1206",
  "next_action": "Correct the stale README record/replay claims and PLAN command list, document the exact integrated journey with CLI/TUI/noninteractive forms and OpenRouter free-model setup, and regenerate checked transcripts and doctor/capabilities outputs.",
  "owner": "",
  "plan": "../plans/AR-1206.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Bring doctor, capabilities, help, completion, README, PLAN, and the workflow/quickstart guides in line with the integrated record/replay/benchmark surface, and regenerate the checked workflow transcripts.",
  "task_revision": 1,
  "title": "Publish the integrated CLI surface and workflow documentation",
  "updated_at": "2026-09-22T09:39:55+00:00",
  "worktree_key": "agent-systems-benchmark-record-replay-docs"
}
---
Align all user-facing documentation and command surface with the implemented record/replay/benchmark
integration. Correct the stale README paragraph that denies the existence of `record`/`replay`,
the `docs/PLAN.md` command list (`asb record EXPERIMENT.toml`, `asb replay RUN`), and
help/completion text. Document the exact integrated journey from AR-1204 with CLI, TUI and
noninteractive forms, evidence boundaries, and OpenRouter free-model setup. Regenerate checked
transcripts and update `doctor`/`capabilities` so planned commands cannot appear as working
features. Repository: `martin-beck/agent-systems-benchmark`.

- 2026-09-22T09:39:55+00:00: Defined from the record/replay/benchmark integration proposal.
  Depends on AR-1202, AR-1203, AR-1204 and AR-1205. Text-only docs and transcript regeneration;
  rendering updates land last.
