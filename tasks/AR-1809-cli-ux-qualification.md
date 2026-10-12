---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1806", "AR-1807", "AR-1808"],
  "id": "AR-1809",
  "next_action": "Run end-to-end CLI UX qualification against the complete contract and close contract gaps.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1809-cli-ux-qualification.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {"evidence_class":"contract-test","evidence_digest":"","evidence_ref":"","spec_ref":"specs/AR-1809.json","spec_revision":1,"status":"pending"},
  "spec_ref": "specs/AR-1809.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Qualify the complete ASB command tree for human output, help, list discovery, and selection round trips.",
  "task_revision": 1,
  "title": "End-to-End CLI UX Contract Qualification",
  "updated_at": "2026-10-12T10:15:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1809-cli-ux-qualification"
}
---

## Outcome

The complete ASB command tree is qualified through realistic clean-project
journeys. A user can discover supported choices, understand commands from help,
select valid IDs, and receive clear default output without reading JSON.

## Acceptance

- Execute contract-driven clean-project journeys across all public command
  families in human, JSON, quiet, TTY, and redirected modes.
- Verify help and list are pure; verify list-to-selection round trips for every
  advertised ID and clear handling of unavailable capabilities.
- Verify output from successful and failed commands is concise, actionable, and
  free of raw serialization, secret material, and private host paths.
- Run exact-head quality/independent-review and post-merge verification; leave
  any unqualified route as a narrowly scoped successor rather than a waiver.
